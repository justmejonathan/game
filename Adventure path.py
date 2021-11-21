import time
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

# variables, which I define before the start to make them accessible to the functions:
added_time = 0 # you get time penalties or bonuses based on your decisions in the game
start = time.time() # the game is played on time
a = 1.5 # pause between texts
reckless = False
consistent = False
zu_allem_ja_sager = False
unbeliebt_bei_professor = False
kontakt = False

# zeit_ende ends the counting of time and prints it to the player
def zeit_ende():
    global added_time
    end = time.time()
    finale_zeit = end - start + added_time
    finale_zeit_zwei_kommastellen = "%.2f" % finale_zeit
    print()
    slow_text("Deine Zeit ist: " + finale_zeit_zwei_kommastellen + " Sekunden")
    return finale_zeit_zwei_kommastellen

# bierball_turnier is part of the story and lets you decide if you want to take part in a university event (in the game) or not
def bierball_turnier():  
    global added_time
    global kontakt
    print()
    slow_text("Es ist Erstiwoche und die Fachschaft ruft zum Bierballturnier (der einzig wahre Name) auf. Gehst du hin? (ja/nein)")
    answer = input()
    if answer.lower().strip() =="ja":
        slow_text("Es war ein aufregender Abend und du hast wichtige Bekanntschaften gemacht. Vielleicht helfen sie dir im Laufe des Studiums weiter.")
        kontakt = True
        added_time = 10 #adding time because of drinking
        print()
        slow_text("...")
        slow_text("Du stolperst in die erste Vorlesung.")
        time.sleep(a)
        print()
        slow_text ("Noch halbtrunken von der Erstiwoche hörst du deinem Professor zu. Am Ende Fällt der Satz:") 
        return kontakt, added_time
    else:
        slow_text("Du möchtest also den absoluten Fokus auf die Straße bringen. Hustle mode: ON")
        time.sleep(a)
        print()
        slow_text("...")
        slow_text("Völlig ausgeschlafen gehst du zur ersten Vorlesung")
        time.sleep(a)
        print()
        slow_text ("Gemeinsam mit deinen verkaterten Kommoliton:innen hörst du deinem Professor zu. Am Ende Fällt der Satz:") 
        added_time = 0 
        return added_time

# matheaufgabe presents the player with a very simple math task - it is kind of a joke because law students are known for not liking math
def matheaufgabe():
    time.sleep(a)
    answer = input()
    if int(answer) == solution:
        slow_text("Good job!")
    else:
        slow_text("Falsch, versuche es nochmal:")
        matheaufgabe() 

# leaderboard lets the player put their name, uni and time into the leaderboard to determine their position
def leaderboard_entry(time):
    print()
    slow_text("Du hast es geschafft! Möchtest du dich ins Leaderboard eintragen? (ja/nein)")
    answer = input()
    if answer.lower().strip() =="ja":
        slow_text("Stark, wie heißt du (Vorname)?")
        print()
        first_name = input()
        slow_text("Nett dich kennenzulernen " + first_name + ". Was ist dein Nachname?")
        print()
        last_name = input()
        slow_text("Wo studierst du?")
        uni = input()
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

# slow_text is a function which prints the text in a slower form to make it look more game-like
def slow_text(s):
    for character in s: 
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)

# vorlesung puts the player in front of another decision, which will decide on parts of the outcome of the game and enlargens the story
def vorlesung():
    global added_time
    global zu_allem_ja_sager
    global unbeliebt_bei_professor
    time.sleep(a)
    slow_text("'Um perfekt auf die Klausur vorbereitet zu sein, könnt ihr einfach mein Buch kaufen. Damit habt ihr alle Informationen die es braucht, um zu bestehen.'")
    time.sleep(a)
    print()
    slow_text("Was machst du?")
    time.sleep(a)
    print()
    slow_text("1. Ja, natürlich kaufe ich mir das Buch. Ich bin doch nicht lebensmüde. (1)")
    time.sleep(a)
    print()
    print()
    slow_text("2. Hmm, ich bin noch unentschlossen. Ich schaue mal wie das Semester so läuft. (2)")
    time.sleep(a)
    print()
    print()
    slow_text("3. Geldgieriges Etwas. Wenn er mir so kommt, kaufe ich mir das Buch erst recht nicht. Ich schreibe einen Hass-Twitter-Post, dass ich so etwas verabscheue. (3)")
    print()
    answer = input("1, 2 oder 3?")
    if answer.strip() == "1":
        zu_allem_ja_sager = True
        slow_text("Sichere Nummer, verständlich.")
        print()
        print("ACHTUNG! Juristen sind dafür bekannt, dass sie SEHR GUT in Mathe sind. Was ergibt",equation, "?" )
        return zu_allem_ja_sager
    elif answer.strip() == "2":
        added_time = added_time + 10
        slow_text("Opportunistische Einstellung. Bist du sicher, dass du im Jurastudium richtig bist?")
        print()
        print("ACHTUNG! Juristen sind dafür bekannt, dass sie SEHR GUT in Mathe sind. Was ergibt",equation, "?" )
    elif answer.strip() == "3":
        unbeliebt_bei_professor = True
        slow_text("Naja, die Klauausern werden sowieso annonym geschrieben, also ist es nicht schlimm wenn dein Prof. den Post sieht.")
        print()
        print("ACHTUNG! Juristen sind dafür bekannt, dass sie SEHR GUT in Mathe sind. Was ergibt",equation, "?" )
        return unbeliebt_bei_professor
    else:
        slow_text("Oh, da ist etwas schiefgelaufen. Gleich nochmal: ")
        vorlesung()

# vorlesung puts the player in front of yet another decision as part of the game
def semesterabschlussklausur():
    global added_time
    global consistent
    global reckless
    print()
    slow_text("Die Semesterabschlussklausuren kommen auf dich zu.")
    time.sleep(a)
    print()
    slow_text("Nun stellt sich natürlich die Frage: Welche Art von Klausurenlerner:in bist du?")
    time.sleep(a)
    print()
    slow_text("1. Ich warte bis 3 Wochen vor der Klausur und kapsel mich dann ab. Three weeks full focus. (1)")
    time.sleep(a)
    print()
    slow_text("2. Ich arbeite fleißig im Semester mit (und nach) und gehe dann vor den Klausuren nochmal in eine kurze, heiße Phase. (2)")
    time.sleep(a)
    print()
    slow_text("3. Klausuren sind überschätzt. Ich habe das Gesetz und 'wuppe' den Laden auch so. (3)")
    print()
    answer = input("1, 2 oder 3?")
    print()
    if answer.strip() == "1":
        added_time = added_time - 3
        slow_text("So macht es fast jede:r. Viel Glück.")
        print()
        return added_time
    elif answer.strip() == "2":
        added_time = added_time + 3
        consistent = True
        slow_text("Ein fleißiges Bienchen. Das läuft sicher gut.")
        print()
        return consistent, added_time
    elif answer.strip() == "3":
        added_time = added_time - 5
        reckless = True
        slow_text("Also entweder bist du ein Überflieger oder bald fliegst du garnicht mehr. Wir werden sehen...")
        print()
        return reckless, added_time
    else:
        slow_text("Oh, da ist etwas schiefgelaufen. Gleich nochmal: ")
        semesterabschlussklausur()

# outcomes takes in the decisions of the player and returns a different ending for certain decision-combinations
def outcomes():
    global reckless
    global consistent
    global zu_allem_ja_sager
    global unbeliebt_bei_professor
    global kontakt
    global added_time
    if reckless == True and unbeliebt_bei_professor == True:
        print()
        slow_text("Ich habe leider schlechte Nachrichten für dich. Dadurch, dass du so unbeliebt bei deinen Professor:innen bist und dich aufs 'wuppen' deiner Klausuren verlassen hast, bist du leider durchgefallen. Vielleicht ist ja Wild-Water-Rafting-Instructor was für dich?!")
        slow_text("Good bye!")
        quit()    
    elif kontakt == True and reckless == True:
        print()
        slow_text("Deine Kombination aus viel party und rock'n'roll, führt leider zu zu wenig Zeit fürs Studium. Du bekommst über die Zeit andere Interessen und brichst dein Studium ab.")
        slow_text("Good bye!")
        quit()
    elif unbeliebt_bei_professor == True and consistent == True:
        slow_text("Du lernst sehr viel aber bist dennoch unbeliebt bei deinen Professor:innen. Du wirst trotz deines hohen Aufwandes durch deine undurchdachten Taten bestraft. In der echten Welt wirst du aber wahrscheinlich erfolgreich mit deinem Ehrgeiz. Keep it going.")
        added_time = added_time + 20
    elif zu_allem_ja_sager == True and consistent == True:
        slow_text("Du schaffst das Studium mit guter Leistung. Wenn du später deinen eigenen Weg gehst und nicht allzu viel über dich bestimmen lässt, kannst du sehr erfolgreich werden.")
    elif kontakt == True and consistent == True:
        slow_text("Du bist der:die SUPER STUDENT:IN! Du arbeitest hart und hast ein Händchen dafür, wann man sich Zeit für seine Mitmenschen nehmen sollte. Rock on!")
    else:
        slow_text("Das Studium neigt sich dem Ende zu. Du bist sehr gut durchgekommen. Deine Noten sehen vielversprechend aus und du hast schon die ersten Angebote von Kanzleien im Briefkasten.")

# the game function combines all functions, it is the heart of the game so to say
def game():
    slow_text("Bist du sicher, dass du dich ins Jurastudium wagen willst? (ja/nein)")
    answer = input()
    if answer.lower().strip() != "ja" and answer.lower().strip() != "nein":
        slow_text("Wie bitte? Ich habe gefragt:")
        game()
    elif answer.lower().strip() == "nein":
        slow_text("Gute Entscheidung, ich war mir auch nicht sicher ob du es in dir hast.")

    elif answer.lower().strip() == "ja":
        slow_text("Mutig! Es werden dich so einige Challenges erwarten, aber wenn du sie schaffst, gebührt dir viel Gel... ähm viel Ruhm und Ehre.")
        time.sleep(a)
        bierball_turnier()
        vorlesung()
        matheaufgabe()
        semesterabschlussklausur()
        outcomes()
        leaderboard_entry(zeit_ende())

# --> start of game
slow_text("Willkommen zu einer langen, gefährlichen Reise.")
print()
time.sleep(a)
slow_text("Mein Name ist Justus und ich bin der Gamemaster auf diesem Weg.")
time.sleep(a)
print()
slow_text("Es ist ein Weg, der viel Blut, Schweiß, einsame Nächte und Anzugträger:innen mit sich bringt.")
time.sleep(a)
print()
game()