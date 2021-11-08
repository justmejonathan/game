import time
import timeit
import sqlite3

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

def zeit_ende():
    end = time.time()
    finale_zeit = end - start + added_time
    finale_zeit_zwei_kommastellen = "%.2f" % finale_zeit
    print("Deine Zeit ist: " + finale_zeit_zwei_kommastellen + " Sekunden")
    return finale_zeit_zwei_kommastellen

def bierball_turnier():  
    answer = input("Es ist Erstiwoche und die Fachschaft ruft zum Bierballturnier (der einzig wahre Name) auf. Gehst du hin? (ja/nein)")
    if answer.lower().strip() =="ja":
        print("Es war ein aufregender Abend und du hast wichtige Bekanntschaften gemacht. Vielleicht helfen sie dir im Laufe des Studiums weiter.")
        kontakt = True
        added_time = 3 #adding time because of drinking
        zeit_ende()
    else:
        print("Du möchtest also den absoluten Fokus auf die Straße bringen. Hustle mode: ON")
        kontakt = False
        added_time = 0
        zeit_ende()   

def matheaufgabe():
    # I shoulf bring the "Achtung..." at the end of the last function to only ask the input question in this function, so it can be repeated again if the answer is wrong
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
        conn_ranking = sqlite3.connect("ranking.db")
        first_name = input("Stark, wie heißt du (Vorname)?")
        last_name = input("Nett dich kennenzulernen " + first_name + ". Was ist dein Nachname?")
        uni = input("Wo studierst du?")
        c_ranking.execute("INSERT INTO ranking (Vorname, Nachname, Universität, Zeit) VALUES (?, ?, ?, ?)",(first_name,last_name,uni,time))
        conn_ranking.commit()
        rank = c_ranking.execute("SELECT COUNT(*) as cnt FROM ranking WHERE Zeit<?", (time, )).fetchone()[0]
        conn_ranking.commit()
        conn_ranking.close() #only close at the very end of using SQLite3
        print("Du bist auf Position " + str(rank) + " gelandet.")
    else:
        print("Okay, dann scheint die Zeit ja nicht so 'dolle' gewesen zu sein! Viel Glück beim nächsten Mal")
        #c_ranking.execute("SELECT ROW_NUMBER () OVER (ORDER BY Zeit ASC) RowNum, Vorname, Nachname, Universität, Zeit FROM ranking")
        c_ranking.execute("SELECT * FROM ranking")
        print_pos = c_ranking.fetchall()
        print(print_pos)



# --> start of game
print("Willkommen zu einer langen, gefährlichen Reise.")
answer = input("Bist du sicher, dass du dich ins Jurastudium wagen willst? (ja/nein)")
# .lower() -> sets all to lower 
# .strip() -> gets rid of any lowercases around the word 
if answer.lower().strip() == "nein":
    print("Gute Entscheidung, ich war mir auch nicht sicher ob du es in dir hast.")

elif answer.lower().strip() == "ja":
    print("Mutig! Es werden dich so einige Challenges erwarten, aber wenn du sie schaffst gebührt dir viel Gel... ähm viel Ruhm und Ehre.")
    time.sleep(3)
    matheaufgabe()
    leaderboard_entry(zeit_ende()) #das mache ich um finale_zeit_zwei_kommastellen in die leaderboard function zu bekommen, dann bekomme ich aber einen Error

