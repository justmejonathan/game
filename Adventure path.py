import time
import timeit
import sqlite3

conn = sqlite3.connect("calculations.db")
c = conn.cursor()
# c.execute("""CREATE TABLE calculations (
#             aufgabe text,
#             ergebnis integer
#             )""")
#c.execute("INSERT INTO calculations VALUES('18+18-36+1', 1)")
c.execute("SELECT * FROM calculations ORDER BY RANDOM() LIMIT 1;")

calculation = (c.fetchone())
calculation_list = list(calculation)
equation = calculation_list[0]
solution = calculation_list[1]
conn.commit()
conn.close()

def zeit_ende():
    end = time.time()
    finale_zeit = end - start + added_time
    print("%.2f" % finale_zeit)

start = time.time()

print("Willkommen zu einer langen, gefährlichen Reise.")
answer = input("Bist du sicher, dass du dich ins Jurastudium wagen willst? (ja/nein)")
# .lower() -> sets all to lower 
# .strip() -> gets rid of any lowercases around the word 
if answer.lower().strip() == "ja":
    print("Mutig! Es werden dich so einige Challenges erwarten, aber wenn du sie schaffst gebührt dir viel Gel... ähm viel Ruhm und Ehre.")
    time.sleep(3)
    answer = input("Es ist Erstiwoche und die Fachschaft ruft zum Bierballturnier (der einzig wahre Name) auf. Gehst du hin? (ja/nein)")
    if answer.lower().strip() =="ja":
        print("Es war ein aufregender Abend und du hast wichtige Bekanntschaften gemacht. Vielleicht helfen sie dir im Laufe des Studiums weiter.")
        kontakt = True
        added_time = 3 #adding time because of drinking
        zeit_ende()
        print("Achtug! Juristen sind dafür bekannt, dass sie SEHR GUT in Mathe sind. Was ergibt",equation, "?" )
        answer = input()
        if int(answer) == solution:
            print("Good job!")
        else:
            print("try again!")
    else:
        print("Du möchtest also den absoluten Fokus auf die Straße bringen. Hustle mode: ON")
        kontakt = False
        added_time = 0
        zeit_ende()

else: 
    print("Gute Entscheidung, ich war mir auch nicht sicher ob du es in dir hast.")
    #do I need to end the time function?