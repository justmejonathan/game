# Spiel Tic-Tac-Toe
spiel_aktiv = True 
spieler_aktuell = "X"
spielfeld = [" ",
            "1","2","3",
            "4","5","6",
            "7","8","9"]

#Spielfeld ausgeben (tried building it with a for loop, but failed)
def spielfeld_ausgeben():
    print(spielfeld[1] +  "|" + spielfeld[2] +  "|" + spielfeld[3])
    print(spielfeld[4] +  "|" + spielfeld[5] +  "|" + spielfeld[6])
    print(spielfeld[7] +  "|" + spielfeld[8] +  "|" + spielfeld[9])
spielfeld_ausgeben()

def spieler_eingabe():
    #Eingabe durch Spieler und Überprüfung
    global spiel_aktiv
    while True:
        spielzug = input("Bitte Feld eingeben: ")
        # vorzeitiges Spielende durch Spieler
        if spielzug == "q":
            spiel_aktiv = False
            print("Spiel beendet")
            return
        try: 
            spielzug = int(spielzug)
        except ValueError:
            print("Bitte Zahl von 1 bis 9 eingeben")
        else:
            if spielzug >=1 and spielzug <= 9:
                if spielfeld[spielzug] == "X" or spielfeld[spielzug] == "O":
                    print("Das Feld ist bereits belegt - bitte wähle ein anderes!")
                else:
                    return spielzug
            else:
                print("Zahl muss zwischen 1 und 9 liegen")

def spieler_wechseln():
        global spieler_aktuell
        if spieler_aktuell== "X":
            spieler_aktuell = "O"
        else:
            spieler_aktuell = "X"

# Kontrolle, ob ein Spieler gewonnen hat
def kontrolle_gewonnen():
    # wenn alle 3 Felder gleich sind, hat der entsprechende Spieler gewonnen
    # Kontrolle auf Reihen
    if spielfeld[1] == spielfeld[2] == spielfeld[3]:
        return spielfeld[1]
    if spielfeld[4] == spielfeld[5] == spielfeld[6]:
        return spielfeld[4]
    if spielfeld[7] == spielfeld[8] == spielfeld[9]:
        return spielfeld[7]
    # Kontrolle auf Spalten
    if spielfeld[1] == spielfeld[4] == spielfeld[7]:
        return spielfeld[1]
    if spielfeld[2] == spielfeld[5] == spielfeld[8]:
        return spielfeld[2]
    if spielfeld[3] == spielfeld[6] == spielfeld[9]:
        return spielfeld[3]
    # Kontrolle auf Diagonalen
    if spielfeld[1] == spielfeld[5] == spielfeld[9]:
        return spielfeld[5]
    if spielfeld[7] == spielfeld[5] == spielfeld[3]:
        return spielfeld[5]

def kontrolle_auf_unentschieden():
    if (spielfeld[1] == 'X' or spielfeld[1] == 'O') \
      and (spielfeld[2] == 'X' or spielfeld[2] == 'O') \
      and (spielfeld[3] == 'X' or spielfeld[3] == 'O') \
      and (spielfeld[4] == 'X' or spielfeld[4] == 'O') \
      and (spielfeld[5] == 'X' or spielfeld[5] == 'O') \
      and (spielfeld[6] == 'X' or spielfeld[6] == 'O') \
      and (spielfeld[7] == 'X' or spielfeld[7] == 'O') \
      and (spielfeld[8] == 'X' or spielfeld[8] == 'O') \
      and (spielfeld[9] == 'X' or spielfeld[9] == 'O'):
        return ('unentschieden')

while spiel_aktiv:
    #Eingabe des aktiven Spielers
    print ("Spieler " + spieler_aktuell + " am Zug")
    # Eingabe des aktiven Spielers macht ein X auf dem Feld das eingegeben wurde
    spielzug = spieler_eingabe()
    if spielzug:
        spielfeld[spielzug] = spieler_aktuell
        #aktuelles Spielfeld ausgeben
        spielfeld_ausgeben()
        #Kontrolle, ob jemand gewonnen hat
        gewonnen = kontrolle_gewonnen()
        if gewonnen:
            print ("Spieler " + gewonnen + " hat gewonnen!")
            spiel_aktiv = False
        #Kontrolle, ob unentschieden
        unentschieden = kontrolle_auf_unentschieden()
        if unentschieden:
            print("Das Spiel ist unentschieden ausgegangen.")
            spiel_aktiv = False
        #Spieler wechseln
        spieler_wechseln()
    print("Spielzug:" + str(spielzug))