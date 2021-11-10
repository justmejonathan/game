import time
import timeit
import sqlite3
import sys

# --> connection with databases
conn = sqlite3.connect("calculations.db")
c = conn.cursor()
conn_ranking = sqlite3.connect("ranking.db")
c_ranking = conn_ranking.cursor()
# c.execute("""CREATE TABLE ranking (
#             Vorname text,
#             Nachname text,
#             Universität text,
#             Zeit real
#             )""")
#c.execute("INSERT INTO ranking VALUES('Marvin','Grocholl','HU Berlin', 15.0)")
# --> calling of a random equation for matheaufgabe 
c.execute("SELECT * FROM calculations ORDER BY RANDOM() LIMIT 1;")
calculation = (c.fetchone())
calculation_list = list(calculation)
equation = calculation_list[0]
solution = calculation_list[1]
conn.commit()
conn.close()
# --> Calling parts of the ranking database to check if it works properly
# calculation = (c_ranking.fetchone())
# calculation_list = list(calculation)
# equation = calculation_list[0]
# solution = calculation_list[1]
# print(equation + " " + solution)
# conn_ranking.commit()
# conn_ranking.close()

# variables, which I define before the start to make them accessible to the functions:
added_time = 0
start = time.time()
a = 2

def zeit_ende():
    global added_time
    end = time.time()
    finale_zeit = end - start + added_time
    finale_zeit_zwei_kommastellen = "%.2f" % finale_zeit
    print("Deine Zeit ist: " + finale_zeit_zwei_kommastellen + " Sekunden")
    return finale_zeit_zwei_kommastellen

def bierball_turnier():  
    global added_time
    answer = input("Es ist Erstiwoche und die Fachschaft ruft zum Bierballturnier (der einzig wahre Name) auf. Gehst du hin? (ja/nein)")
    if answer.lower().strip() =="ja":
        print("Es war ein aufregender Abend und du hast wichtige Bekanntschaften gemacht. Vielleicht helfen sie dir im Laufe des Studiums weiter.")
        kontakt = True
        added_time = 3 #adding time because of drinking
        return kontakt, added_time
    else:
        print("Du möchtest also den absoluten Fokus auf die Straße bringen. Hustle mode: ON")
        kontakt = False
        added_time = 0 
        return kontakt, added_time

def matheaufgabe():
    # I shoulf bring the "Achtung..." at the end of the last function to only ask the input question in this function, so it can be repeated again if the answer is wrong
    time.sleep(a)
    print("Achtug! Juristen sind dafür bekannt, dass sie SEHR GUT in Mathe sind. Was ergibt",equation, "?" )
    answer = input()
    if int(answer) == solution:
        print("Good job!")
    else:
        print("Falsch, versuche es nochmal:")
        matheaufgabe() 

def leaderboard_entry(time):
    answer = input("Du hast es geschafft! Möchtest du dich ins Leaderboard eintragen? (ja/nein)")
    if answer.lower().strip() =="ja":
        first_name = input("Stark, wie heißt du (Vorname)?")
        last_name = input("Nett dich kennenzulernen " + first_name + ". Was ist dein Nachname?")
        uni = input("Wo studierst du?")
        c_ranking.execute("INSERT INTO ranking (Vorname, Nachname, Universität, Zeit) VALUES (?, ?, ?, ?)",(first_name,last_name,uni,time))
        conn_ranking.commit()
        rank = c_ranking.execute("SELECT COUNT(*) as cnt FROM ranking WHERE Zeit<?", (time, )).fetchone()[0]
        conn_ranking.commit()
        conn_ranking.close() #only close at the very end of using SQLite3
        print("Du bist auf Position " + str(rank + 1) + " gelandet.")
    else:
        print("Okay, dann scheint die Zeit ja nicht so 'dolle' gewesen zu sein! Viel Glück beim nächsten Mal")
        #c_ranking.execute("SELECT ROW_NUMBER () OVER (ORDER BY Zeit ASC) RowNum, Vorname, Nachname, Universität, Zeit FROM ranking")
        conn_ranking.commit()
        conn_ranking.close()

def vorlesung():
    global added_time
    print("Du stolperst in die erste Vorlesung.") 
    time.sleep(a)
    print ("Noch halbtrunken von der Erstiwoche hörst du deinem Professor zu. Am Ende Fällt der Satz:") 
    time.sleep(a)
    s = "'Um perfekt auf die Klausur vorbereitet zu sein, könnt ihr einfach mein Buch kaufen. Damit habt ihr alle Informationen die es braucht, um zu bestehen.'"
    for character in s: 
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    time.sleep(a)
    print()
    print("Was machst du?")
    time.sleep(a)
    print("1. Ja, natürlich kaufe ich mir das Buch. Ich bin doch nicht lebensmüde. (1)")
    time.sleep(a)
    print()
    print("2. Hmm, ich bin noch unentschlossen, ich schaue mal wie das Semester so läuft. (2)")
    time.sleep(a)
    print()
    print("3. Geldgieriges Etwas. Wenn er mir so kommt, kaufe ich mir das Buch erst recht nicht. Ich schreibe einen Hass-Twitter-Post, dass ich so etwas verabscheue. (3)")
    answer = input("1, 2 oder 3?")
    if answer.strip() == "1":
        zu_allem_ja_sager = True
        print("Sichere Nummer, verständlich.")
        return zu_allem_ja_sager
    elif answer.strip() == "2":
        added_time = added_time + 3
        print("Opportunistische Einstellung. Bist du sicher, dass du im Jurastudium richtig bist?")
    elif answer.strip() == "3":
        unbeliebt_bei_professor = True
        print("Naja, die Klauausern werden sowieso annonym geschrieben, also ist es nicht schlimm wenn dein Prof. den Post sieht.")
        return unbeliebt_bei_professor
    else:
        print("Oh, da ist etwas schiefgelaufen. Gleich nochmal: ")
        vorlesung()

def semesterabschlussklausur():
    global added_time
    print("Die Semesterabschlussklausuren kommen auf dich zu.")
    time.sleep(a)
    print("Nun stellt sich natürlich die Frage: Welche Art von Klausurenlerner:in bist du?")
    time.sleep(a)
    print("1. Ich warte bis 3 Wochen vor der Klausur und kapsel mich dann ab. Three weeks full focus. (1)")
    time.sleep(a)
    print("2. Ich arbeite fleißig im Semester mit (und nach) und gehe dann vor den Klausuren nochmal in eine kurze, heiße Phase. (2)")
    time.sleep(a)
    print("3. Klausuren sind überschätzt. Ich habe das Gesetz und 'wuppe' den Laden auch so. (3)")
    answer = input("1, 2 oder 3?")
    if answer.strip() == "1":
        added_time = added_time - 3
        print("So macht es fast jede:r. Viel Glück.")
    elif answer.strip() == "2":
        added_time = added_time + 3
        consistent = True
        print("Ein fleißiges Bienchen. Das läuft sicher gut.")
        return consistent
    elif answer.strip() == "3":
        added_time = added_time - 5
        reckless = True
        print("Also entweder bist du ein Überflieger oder bald fliegst du garnicht mehr. Wir werden sehen...")
        return reckless
    else:
        print("Oh, da ist etwas schiefgelaufen. Gleich nochmal: ")
        semesterabschlussklausur()



# --> start of game
print("Willkommen zu einer langen, gefährlichen Reise.")
time.sleep(a)
print("Mein Name ist Justus und ich bin der Gamemaster auf diesem Weg.")
time.sleep(a)
print("Es ist ein Weg, der viel Blut, Schweiß, einsame Nächte und Anzugträger:innen mit sich bringt.")
time.sleep(a)
def game():
    answer = input("Bist du sicher, dass du dich ins Jurastudium wagen willst? (ja/nein)")
    # .lower() -> sets all to lower 
    # .strip() -> gets rid of any lowercases around the word 
    if answer.lower().strip() != "ja" and answer.lower().strip() != "nein":
        print("Wie bitte? Ich habe gefragt:")
        game()
    elif answer.lower().strip() == "nein":
        print("Gute Entscheidung, ich war mir auch nicht sicher ob du es in dir hast.")

    elif answer.lower().strip() == "ja":
        print("Mutig! Es werden dich so einige Challenges erwarten, aber wenn du sie schaffst gebührt dir viel Gel... ähm viel Ruhm und Ehre.")
        time.sleep(a)
        bierball_turnier()
        vorlesung()
        matheaufgabe()
        semesterabschlussklausur()
        leaderboard_entry(zeit_ende())

game()