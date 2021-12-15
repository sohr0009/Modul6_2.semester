# Main script for "AgileTimeTracker"
# Oprettet: 8. november 2020
# Redigeret: 17. december 2020
# Dev team: Gruppe2 - Sohrab, Gustav, Emil, Mathias, Sebastian
# Projekt: Big Corp - Semesterprojekt, modul 5
# Hold: BE-IT S21DA (2. semester)
# Institut: Københavns Erhvervsakademi, Guldbergsgade


# Importering af nødvendige moduler samt relevante varibaler
from datetime import datetime
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QLineEdit
from PyQt5.uic import loadUi
import Connection


# Main funktion
def main():

    # Global variabel for systemets dato under kørsel af script
    # Denne bruges til bl.a. oprettelsen af nye registreringer/projekter/kunder mm.
    dato = datetime.today().strftime('%d.%m.%Y')

    ################ Forside ##################

    # Bruger vælger en rolle - Her kan vælges tre måder at logge ind på (Konsulent, Scrum Master eller Manager)
    class Forside(QMainWindow):
        def __init__(self):
            super(Forside, self).__init__()
            loadUi("files/Forside.ui", self)

            # Knapper - På forsiden kan der klikkes på knapperne:
            # Konsulent-knap forbinder til funktion "Konsulent"
            self.Konsulent_knap.clicked.connect(self.Konsulent)
            # ScrumMaster-knap forbinder til funktion "ScrumMaster"
            self.ScrumMaster_knap.clicked.connect(self.ScrumMaster)
            # Manager-knap forbinder til funktion "Manager"
            self.Chef_knap.clicked.connect(self.Manager)

        # Konsulentfunktion åbner et nyt vindue "Konsulent_Login"
        def Konsulent(self):
            widget.addWidget(Konsulent_Login())
            widget.setCurrentIndex(widget.currentIndex()+1)

        # ScrumMasterfunktion åbner et nyt vindue "ScrumMaster_Login"
        def ScrumMaster(self):
            widget.addWidget(ScrumMaster_Login())
            widget.setCurrentIndex(widget.currentIndex()+1)

        # Managerfunktion åbner et nyt vindue "Manager_Login"
        def Manager(self):
            widget.addWidget(Manager_Login())
            widget.setCurrentIndex(widget.currentIndex()+1)

    ################ Loginside ##################

    # Loginside for "Konsulent"
    # Siden defineres som en klasse, hvor der tilhører attributter og metoder til

    class Konsulent_Login(QMainWindow):
        def __init__(self):
            super(Konsulent_Login, self).__init__()
            loadUi("files/Konsulent/Konsulent_login.ui", self)

            # Knapper og indputfelter
            # Inputfelt for adgangskode gemmer brugerens indtastning
            self.adgangskode_input.setEchoMode(QLineEdit.EchoMode.Password)
            # Loginknap forbindes til en funktion
            self.login_knap.clicked.connect(self.login)
            # Tilbageknap forbindes til en funktion
            self.tilbage_knap.clicked.connect(self.tilbage)

        # Tilbagefunktion - Tilbagesender bruger til forsiden
        def tilbage(self):
            widget.addWidget(Forside())
            widget.setCurrentIndex(widget.currentIndex()+1)

        # Loginfunktion - Logger brugeren ind hvis specifikke betingelser opfyldes

        def login(self):
            # Email globaliseres, scriptet kan agere på baggrund af denne bruger
            global Global_email
            # Email input gemmer brugerens indtastning
            Global_email = self.email_input.text().lower()
            # Adgangskodeinput gemmer brugerens indtastning
            adgangskode = self.adgangskode_input.text()

            # Forbindelse oprettes
            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()                                       # Cursor oprettes
            # DML-udsagn defineres som skal indhente alle eksisterende emails
            cursor.execute('SELECT Email FROM Medarbejder')
            # Via en for loop sættes disse emails ind i en liste
            alle_medarbejdere = [i[0] for i in cursor.fetchall()]

            # Hvis brugerens indtastninger er 0 tegn, skal en fejl meddeles
            if len(Global_email) == 0 or len(adgangskode) == 0:
                self.error.setText("Udfyld venligst alle felter")

            # Hvis den indtastede email ikke eksistere i en liste, skal en fejl meddeles
            elif Global_email not in alle_medarbejdere:
                self.error.setText("Bruger eksisterer ikke.")

            # Hvis oventående betingelser opfyldes, skal brugeren logges ind
            else:
                cursor.execute(
                    f"SELECT Adgangskode FROM Medarbejder WHERE Email = '{Global_email}'")       # DML-udsagn defineres som skal indhente den specifikke brugeres adgangskode

                # For-loop som henter værdien (uden specialtegn) fra ovenstående DML-udsagn
                for i in cursor.fetchone():
                    # Hvis brugerens indtastede adgangskode er == værdien fra databasen
                    if adgangskode == i:
                        # Oprettes der hertil en forbindelse igen
                        thisCon = Connection.dbconnect()
                        cursor = thisCon.cursor()
                        cursor.execute(                                                          # Et DML-udsagn defineres som skal hente titlen på den specifikke bruger
                            f"SELECT Titel FROM Medarbejder WHERE Email = '{Global_email}'")
                        # For-loop som henter værdien (uden specialtegn) fra ovenstående DML-udsagn
                        for i in cursor.fetchone():
                            # Hvis brugerens titel/rolle er == Konsulent er login godkendt
                            if i == "Konsulent":

                                print("Logger ind...")
                                # Brugeren videresendes til konsulentsiden
                                widget.addWidget(Konsulent())
                                widget.setCurrentIndex(widget.currentIndex()+1)

                            else:
                                # Hvis brugerens titel/rolle er != Konsulent skal en fejl meddeles om at brugeren ikke er berettiget for at logge ind
                                self.error.setText("Du er ikke ScrumMaster")
                    else:
                        # Hvis brugerens indtastede adgangskode ikke er ens med værdien fra databasen, skal en fejl meddeleses om at adgangskoden er forkert
                        self.error.setText("Forkert adgangskode")

    # Loginside for "Scrum Master" - Her har vi undladt at kommentere, da denne klasse er identisk med ovenstående "Konsulent"-login
    # Siden defineres som en klasse, hvor der tilhører attributter og metoder til

    class ScrumMaster_Login(QMainWindow):
        def __init__(self):
            super(ScrumMaster_Login, self).__init__()
            loadUi("files/ScrumMaster/ScrumMaster_Login.ui", self)
            self.adgangskode_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.login_knap.clicked.connect(self.login)
            self.tilbage_knap.clicked.connect(self.tilbage)

        def login(self):
            global Global_email
            Global_email = self.email_input.text().lower()
            adgangskode = self.adgangskode_input.text()

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()
            cursor.execute('SELECT Email FROM Medarbejder')
            alle_medarbejdere = [i[0] for i in cursor.fetchall()]

            if len(Global_email) == 0 or len(adgangskode) == 0:
                self.error.setText("Udfyld venligst alle felter")

            elif Global_email not in alle_medarbejdere:
                self.error.setText("Bruger eksisterer ikke.")

            else:
                cursor.execute(
                    f"SELECT Adgangskode FROM Medarbejder WHERE Email = '{Global_email}'")

                for i in cursor.fetchone():
                    if adgangskode == i:
                        thisCon = Connection.dbconnect()
                        cursor = thisCon.cursor()
                        cursor.execute(
                            f"SELECT Titel FROM Medarbejder WHERE Email = '{Global_email}'")
                        for i in cursor.fetchone():
                            if i == "ScrumMaster":

                                print("Logger ind...")
                                widget.addWidget(ScrumMaster())
                                widget.setCurrentIndex(widget.currentIndex()+1)
                            else:
                                self.error.setText("Du er ikke ScrumMaster")
                    else:
                        self.error.setText("Forkert adgangskode")

        def tilbage(self):
            widget.addWidget(Forside())
            widget.setCurrentIndex(widget.currentIndex()+1)

    # Loginside for "Mananger" - Her har vi undladt at kommentere, da denne klasse er identisk med ovenstående "Konsulent"-login
    # Siden defineres som en klasse, hvor der tilhører attributter og metoder til
    class Manager_Login(QMainWindow):
        def __init__(self):
            super(Manager_Login, self).__init__()
            loadUi("files/Manager/manager_login.ui", self)
            self.adgangskode_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.login_knap.clicked.connect(self.login)
            self.tilbage_knap.clicked.connect(self.tilbage)

        def tilbage(self):
            widget.addWidget(Forside())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def login(self):
            global Global_email
            Global_email = self.email_input.text().lower()
            adgangskode = self.adgangskode_input.text()

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()
            cursor.execute('SELECT Email FROM Medarbejder')
            alle_medarbejdere = [i[0] for i in cursor.fetchall()]

            if len(Global_email) == 0 or len(adgangskode) == 0:
                self.error.setText("Udfyld venligst alle felter")

            elif Global_email not in alle_medarbejdere:
                self.error.setText("Bruger eksisterer ikke.")

            else:
                cursor.execute(
                    f"SELECT Adgangskode FROM Medarbejder WHERE Email = '{Global_email}'")

                for i in cursor.fetchone():
                    if adgangskode == i:
                        thisCon = Connection.dbconnect()
                        cursor = thisCon.cursor()
                        cursor.execute(
                            f"SELECT Titel FROM Medarbejder WHERE Email = '{Global_email}'")
                        for i in cursor.fetchone():
                            if i == "Manager":

                                print("Logger ind...")
                                widget.addWidget(Manager())
                                widget.setCurrentIndex(widget.currentIndex()+1)
                            else:
                                self.error.setText("Du er ikke Manager")
                    else:
                        self.error.setText("Forkert adgangskode")

    ################ Efter at der logges ind som konsulent ##################

    # Konsulentklasse definerer "forsiden/hjemme-fanen" for konsulenten
    class Konsulent(QMainWindow):
        def __init__(self):
            super(Konsulent, self).__init__()
            loadUi("files/konsulent/Konsulent_hjem.ui", self)

            # Panelknapper
            # Hvis brugeren vil hoppe videre til "Registrerings-fanen" forbinder denne knap til en funktion
            self.ny_registrering_knap.clicked.connect(self.ny_registrering)
            # Hvis brugeren ville hoppe til videre "Sprint historik-fanen" forbinder denne knap til en funktion
            self.historik_knap.clicked.connect(self.historik)
            # Brugeren kan til enhver tid vælge at logge ud - Denne knap forbindses til en funktion
            self.logud_knap.clicked.connect(self.logud)

            # En tabel for beskeder fra organisationen defineres, hvor størrelsen sættes
            self.tabelwidget.setColumnWidth(0, 100)
            self.tabelwidget.setColumnWidth(1, 500)
            self.tabelwidget.setColumnWidth(2, 89)
            # En forbindelse oprettes
            thisCon = Connection.dbconnect()
            # En pegepind defineres
            cursor = thisCon.cursor()
            cursor.execute(
                f"SELECT concat(Fornavn, ' ', Efternavn) FROM Medarbejder WHERE Email = '{Global_email}'")      # Den specifikke brugeres navn hentes fra databasen
            # For-loop som henter denne værdi (uden specieltegn)
            for x in cursor.fetchone():
                # Navnet sættes øverst i højre venstre hjørne
                self.navn.setText(x)

            cursor.execute(
                "SELECT Medarbejder, Text, Dato FROM Note ORDER BY ID DESC")                                    # Et nyt DML-udsagn som skal hente data til tabellen

            self.tabelwidget.setRowCount(0)

            # Rækker indsættes
            for row_number, row_data in enumerate(cursor.fetchall()):
                self.tabelwidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tabelwidget.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

        # Registreringsfunktionen - Her vil scriptet først se om brugeren er tilknyttet et projekt - Hvis ikke, skal brugeren ikke have adgang til denne fane
        def ny_registrering(self):
            thisCon = Connection.dbconnect()            # En forbindelse oprettes
            cursor = thisCon.cursor()                   # En pegepind defineres

            # DML-udsagn defineres som skal indhente alle brugeres ID fra mellemleddet "Projekt_har_Medarbejder"
            cursor.execute("SELECT MedarbejderID FROM Projekt_har_medarbejder")
            # Disse ID indsættes i en liste
            tilknyttede_konsulenter = [i[0] for i in cursor.fetchall()]

            cursor.execute(                                                         # DML-udsagn for at den specifikke brugeres ID udplukkes fra medarbejdertabellen
                f"SELECT ID From Medarbejder WHERE Email = '{Global_email}'")
            # For-loop som skal hente værdien fra det ovenstående
            for i in cursor.fetchone():
                # Hvis den specifikke brugeres ID eksisterer i listen, skal brugeren viderestilles til registreringsfanen
                if i in tilknyttede_konsulenter:
                    widget.addWidget(Konsulent_registrering())
                    widget.setCurrentIndex(widget.currentIndex()+1)

                # Hvis den specifikke brugeres ID ikke eksisterer i listen, har brugeren ikke adgang til denne fane
                else:
                    # Fejl meddeles
                    self.error.setText("Handling ikke mulig")
                    # Fejl meddeles
                    self.error2.setText("da du ikke er tilknyttet")
                    # Fejl meddeles
                    self.error3.setText("et projekt")

        # Historikfunktion - Denne funktion videresender brugeren til historiksiden "Konsulent_Historik"
        def historik(self):
            widget.addWidget(Konsulent_Historik())
            widget.setCurrentIndex(widget.currentIndex()+1)

        # Logudfunktionen - Brugeren logger ud ved at scriptet Tilbagesender brugeren til forsiden
        def logud(self):
            widget.addWidget(Forside())
            widget.setCurrentIndex(widget.currentIndex()+1)

    # Konsulent_registrering definerer registreringsfanen, hvor brugeren kan indtjekke eller udtjekke (Arbejdstider)
    class Konsulent_registrering(QMainWindow):
        def __init__(self):
            super(Konsulent_registrering, self).__init__()
            loadUi("files/konsulent/ny_registrering.ui", self)

            # Panelkanpper
            self.hjem_knap.clicked.connect(self.hjem)
            self.optellinger_knap.clicked.connect(self.historik)
            self.tjekind_knap.clicked.connect(self.tjekind)
            self.tjekud_knap.clicked.connect(self.tjekud)

            # De kommende funktioner henter information til brugeren
            # Disse informationer er: Projekt, kunde, tilknytningsdato, sidste indtjekning/udtjekningstidspunkt, optjent løn, summeret antal timer arbejdet
            thisCon = Connection.dbconnect()                # En forbindelse oprettes
            cursor = thisCon.cursor()                       # En pegepind defineres

            cursor.execute(                                 # DML-udsagn defineres som skal hente den specifikke brugeres navn
                f"SELECT concat(Fornavn, ' ', Efternavn) FROM Medarbejder WHERE Email = '{Global_email}'")
            for i in cursor.fetchone():
                self.navn.setText(i)

            cursor.execute(                                 # DML-udsagn defineres som skal hente den specifikke brugeres ID
                f"SELECT ID From Medarbejder WHERE Email = '{Global_email}'")
            # For-loop som henter værdien fra eksekveringen og tilknytter denne til variablen medarbejderID
            for i in cursor.fetchone():
                global medarbejderID
                medarbejderID = i

            cursor.execute(                                 # DML-udsagn defineres som skal hente projektID fra rækken, hvor brugerens ID er placeret i mellemledstabellen
                f"SELECT ProjektID FROM Projekt_har_medarbejder WHERE MedarbejderID = '{medarbejderID}'")
            for i in cursor.fetchone():
                projektID = i                               # Værdi tilknyttes variablen projektID

            cursor.execute(                                 # DML-udsagn som skal hente projektets navn fra mellemledstabellen
                f"SELECT Projekt_navn FROM Projekt_har_medarbejder WHERE MedarbejderID = '{medarbejderID}'")

            for i in cursor.fetchone():
                self.projekt.setText(f"Projekt: {i}")

            cursor.execute(                                 # DML-udsagn som skal hente kundeID fra Projekttabellen
                f"SELECT KundeID FROM Projekt WHERE ID = '{projektID}'")
            for i in cursor.fetchone():
                KundeID = i                                 # Værdi tilknyttes variablen KundeID

            # DML-udsagn defineres som skal indhente kundens navn fra kundetabellen
            cursor.execute(f"SELECT Navn FROM Kunde WHERE ID = '{KundeID}'")
            for i in cursor.fetchone():
                # Værdien tilknyttes rubrikken kunde:
                self.kunde.setText(f"Kunde: {i}")

            cursor.execute(
                f"SELECT Tilknyttet From Projekt_har_medarbejder WHERE MedarbejderID = '{medarbejderID}'")      # DML-udsagn som henter tilknytningsdato fra mellemledstabellen
            for x in cursor.fetchone():
                # Værdien tilnyttes rubrikken "Dato tilknyttet:"
                self.tilknyttet.setText(f"Dato tilknyttet: {x}")

            # Seneste indtjek og udtjek

            cursor.execute("SELECT MedarbejderID FROM Sprint_registrering")
            registreringer = [i[0] for i in cursor.fetchall()]

            if medarbejderID in registreringer:
                cursor.execute(
                    f"SELECT Starttidspunkt FROM Sprint_registrering WHERE MedarbejderID = '{medarbejderID}' ORDER BY ID DESC")
                for x in cursor.fetchone():
                    self.seneste_indtjek.setText(x)

                thisCon = Connection.dbconnect()
                cursor = thisCon.cursor()
                cursor.execute(
                    f"SELECT Sluttidspunkt FROM Sprint_registrering WHERE MedarbejderID = '{medarbejderID}' ORDER BY ID DESC")
                for x in cursor.fetchone():
                    self.seneste_udtjek.setText(x)

                # Timer i alt & Løn i alt
                thisCon = Connection.dbconnect()
                cursor = thisCon.cursor()

                cursor.execute(
                    f"SELECT SUM(Omkostning) FROM Sprint_registrering WHERE MedarbejderID = '{medarbejderID}'")
                for x in cursor.fetchone():
                    sum_omkostning = x

                cursor.execute(
                    f"SELECT SUM(Timer) FROM Sprint_registrering WHERE MedarbejderID = '{medarbejderID}'")
                for x in cursor.fetchone():
                    sum_timer = x

                self.optjent_lon.setText(str(sum_omkostning))
                self.timer_ialt.setText(str(round(sum_timer, 2)))

            # Hvis brugeren endnu ikke har registreringer sig
            else:
                self.seneste_indtjek.setText("Ingen")
                self.seneste_udtjek.setText("Ingen")
                self.optjent_lon.setText("0")
                self.timer_ialt.setText("0")

        # Funktion for tjekind-knap

        def tjekind(self):
            # Forbindelse oprettes
            thisCon = Connection.dbconnect()
            # Cursor defineres
            cursor = thisCon.cursor()
            # Modulet datetime importeres og starttidspunkt defineres
            import datetime
            starttidspunkt = datetime.datetime.now().strftime('%H:%M')
            # 1.DML-query som indhenter data fra projekt, mellemdled samt medarbejdertabellen
            cursor.execute(
                f"SELECT ProjektID FROM Projekt_har_medarbejder WHERE MedarbejderID = '{medarbejderID}'")
            # For-loop som skal looper igennem det indhentede data og udelukke specialtegn
            for x in cursor.fetchone():
                ProjektID = x  # Det indhentede data gemmes i variablen "ProjektID"

            # 2. DML-query som indsætter ny data ind i Sprint_registreringstabellen
            cursor.execute(
                f'''INSERT INTO Sprint_registrering (Dato, Starttidspunkt, ProjektID, MedarbejderID)
                VALUES
                ("{dato}","{starttidspunkt}",{ProjektID}, {medarbejderID})''')

            self.noterror.setText(f"Tjekket ind: {starttidspunkt}")
            self.seneste_indtjek.setText(starttidspunkt)
            # Queries eksekveres på baggrund af den forbundne database
            thisCon.commit()
            # Fobindelsen lukkes
            thisCon.close()

        def tjekud(self):
            # Forbindelse defineres
            thisCon = Connection.dbconnect()
            # Cursor defineres
            cursor = thisCon.cursor()
            # 1.DML-query som indhenter værdien for starttidspunktet, filtreret med størst værdi
            cursor.execute(
                f'''SELECT Starttidspunkt FROM Sprint_registrering
                WHERE MedarbejderID = "{medarbejderID}"
                ORDER BY ID DESC''')

            # For-loop som skal looper igennem det indhentede data og udelukke specialtegn
            for x in cursor.fetchone():
                starttidspunkt = x
                tid = x

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()

            # 2. DML-query som indhenter værdien for dato for den specifikke medarbejder for den specifikke indtjekningstidspunkt
            cursor.execute(
                f'''SELECT Dato FROM Sprint_registrering
                WHERE MedarbejderID = "{medarbejderID}"
                and Starttidspunkt = "{starttidspunkt}"''')

            # For-loop som skal looper igennem det indhentede data og udelukke specialtegn
            for x in cursor.fetchone():
                regist_dato = x

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()

            # 3. DML-query som indhenter Timelønnen for den specifikke medarbejder fra medarbejdertabellen
            cursor.execute(
                f'''SELECT Timelon FROM Medarbejder
                WHERE ID = "{medarbejderID}"''')

            # For-loop som skal looper igennem det indhentede data og udelukke specialtegn
            for x in cursor.fetchone():
                timeløn = x

            # Regnskab for lønomkostninger
            # Start og sluttidspunkt defineres ud fra indhentede data fra databasen
            starttidspunkt = f"{regist_dato} {starttidspunkt}"
            sluttidspunkt = f"{datetime.today().strftime('%d.%m.%Y')} {datetime.now().strftime('%H:%M')}"

            # Ovenstående variabler konverteres til bestemt format til brug i beregningen
            # Timelønnen beregnes
            start = datetime.strptime(starttidspunkt, '%d.%m.%Y %H:%M')
            slut = datetime.strptime(sluttidspunkt, '%d.%m.%Y %H:%M')
            diff = slut - start
            diff_timer = diff.total_seconds() / 3600
            omkostning = round(timeløn * diff_timer)

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()

            # 4. DML-query som opdaterer den samme række og øvrige data udfyldes
            cursor.execute(
                f'''UPDATE Sprint_registrering SET Sluttidspunkt = "{datetime.now().strftime('%H:%M')}", Timer = "{round(diff_timer, 2)}", Omkostning = {omkostning} WHERE MedarbejderID = "{medarbejderID}" and Starttidspunkt = "{tid}"''')
            self.noterror.setText(f"Tjekket ud: {sluttidspunkt}")
            self.seneste_udtjek.setText(datetime.now().strftime('%H:%M'))
            thisCon.commit()

            cursor.execute(
                f"SELECT SUM(Omkostning) FROM Sprint_registrering WHERE MedarbejderID = '{medarbejderID}'")
            for x in cursor.fetchone():
                sum_omkostning = x

            cursor.execute(
                f"SELECT SUM(Timer) FROM Sprint_registrering WHERE MedarbejderID = '{medarbejderID}'")
            for x in cursor.fetchone():
                sum_timer = x

            thisCon.close()

            self.optjent_lon.setText(str(sum_omkostning))
            self.timer_ialt.setText(str(round(sum_timer, 2)))

        def hjem(self):
            widget.addWidget(Konsulent())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def historik(self):
            widget.addWidget(Konsulent_Historik())
            widget.setCurrentIndex(widget.currentIndex()+1)

    # Konsulent: Historik over alle registreringer
    class Konsulent_Historik(QMainWindow):
        def __init__(self):
            super(Konsulent_Historik, self).__init__()
            loadUi("files/Konsulent/Historik.ui", self)
            self.tabelwidget.setColumnWidth(0, 75)
            self.tabelwidget.setColumnWidth(1, 180)
            self.tabelwidget.setColumnWidth(2, 180)
            self.tabelwidget.setColumnWidth(3, 130)
            self.tabelwidget.setColumnWidth(4, 80)
            self.tabelwidget.setColumnWidth(5, 75)
            self.tabelwidget.setColumnWidth(6, 110)
            self.ny_registrering_knap.clicked.connect(self.ny_registrering)
            self.hjem_knap.clicked.connect(self.hjem)
            self.logud_knap.clicked.connect(self.logud)

            ## Main funktion for denne fane ##

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()
            cursor.execute(
                f"SELECT concat(Fornavn, ' ', Efternavn) FROM Medarbejder WHERE Email = '{Global_email}'")
            for x in cursor.fetchone():
                self.navn.setText(x)

            cursor.execute(
                f"SELECT ID FROM Medarbejder WHERE Email = '{Global_email}'")
            for x in cursor.fetchone():
                medarbejderID = x

            cursor.execute(
                f"SELECT ID, Dato, Starttidspunkt, Sluttidspunkt, ProjektID, Timer, Omkostning FROM Sprint_registrering WHERE MedarbejderID = '{medarbejderID}'")

            self.tabelwidget.setRowCount(0)

            for row_number, row_data in enumerate(cursor.fetchall()):
                self.tabelwidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tabelwidget.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

            # Øvrige knapper

        def hjem(self):
            widget.addWidget(Konsulent())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def ny_registrering(self):
            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()

            cursor.execute("SELECT MedarbejderID FROM Projekt_har_medarbejder")
            tilknyttede_konsulenter = [i[0] for i in cursor.fetchall()]

            # Konsulent ID
            cursor.execute(
                f"SELECT ID From Medarbejder WHERE Email = '{Global_email}'")
            for i in cursor.fetchone():
                if i in tilknyttede_konsulenter:
                    widget.addWidget(Konsulent_registrering())
                    widget.setCurrentIndex(widget.currentIndex()+1)

                else:
                    self.error.setText("Handling ikke mulig")
                    self.error2.setText("da du ikke er tilknyttet")
                    self.error3.setText("et projekt")

        def logud(self):
            widget.addWidget(Forside())
            widget.setCurrentIndex(widget.currentIndex()+1)

    ##### Klasser og funktioner tilhørende Scrum Master  #####

    # Scrum Master: Hjem/forside

    class ScrumMaster(QMainWindow):
        def __init__(self):
            super(ScrumMaster, self).__init__()
            loadUi("files/ScrumMaster/ScrumMaster_hjem.ui", self)

            ###################################################### Forside - START ######################################################
            self.tabelwidget.setColumnWidth(0, 100)
            self.tabelwidget.setColumnWidth(1, 620)
            self.tabelwidget.setColumnWidth(2, 95)

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()

            cursor.execute(
                f"SELECT concat(Fornavn, ' ', Efternavn) FROM Medarbejder WHERE Email = '{Global_email}'")

            for i in cursor.fetchone():
                global global_navn
                global_navn = i
                self.navn.setText(i)

            cursor.execute(
                "SELECT Medarbejder, Text, Dato FROM Note ORDER BY ID DESC")

            self.tabelwidget.setRowCount(0)

            for row_number, row_data in enumerate(cursor.fetchall()):
                self.tabelwidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tabelwidget.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

            ###################################################### Nyhedsbrev/Seneste nyt - SLUT ######################################################

            # Knapper
            self.send_knap.clicked.connect(self.send_besked)
            self.projekter_knap.clicked.connect(self.projekter)
            self.konsulenter_knap.clicked.connect(self.konsulenter)
            self.registreringer_knap.clicked.connect(self.registreringer)
            self.kunder_knap.clicked.connect(self.kunder)
            self.logud_knap.clicked.connect(self.logud)

            # Knappers funktioner

        def send_besked(self):
            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()
            text = self.besked_input.text()
            cursor.execute(
                f"INSERT INTO Note (Medarbejder, Text, Dato) VALUES ('{global_navn}', '{text}', '{dato}')")
            thisCon.commit()

            cursor.execute(
                "SELECT Medarbejder, Text, Dato FROM Note ORDER BY ID DESC")

            self.tabelwidget.setRowCount(0)

            for row_number, row_data in enumerate(cursor.fetchall()):
                self.tabelwidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tabelwidget.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))
            thisCon.close()

        def projekter(self):
            widget.addWidget(SELECT_FROM_PROJEKTER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def konsulenter(self):
            widget.addWidget(SELECT_FROM_KONSULETER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def registreringer(self):
            widget.addWidget(SELECT_FROM_REGISTRERINGER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def kunder(self):
            widget.addWidget(SELECT_FROM_KUNDER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def logud(self):
            widget.addWidget(Forside())
            widget.setCurrentIndex(widget.currentIndex()+1)

    # Scrum Master: Se alle projekter

    class SELECT_FROM_PROJEKTER(QMainWindow):
        def __init__(self):
            super(SELECT_FROM_PROJEKTER, self).__init__()
            loadUi("files/ScrumMaster/projekt.ui", self)
            self.hjem_knap.clicked.connect(self.ScrumMaster)
            self.konsulenter_knap.clicked.connect(self.konsulenter)
            self.registreringer_knap.clicked.connect(self.beregn)
            self.kunder_knap.clicked.connect(self.kunder)
            self.logud_knap.clicked.connect(self.logud)
            self.navn.setText(global_navn)
            self.tabelwidget.setColumnWidth(0, 30)
            self.tabelwidget.setColumnWidth(1, 180)
            self.tabelwidget.setColumnWidth(2, 130)
            self.tabelwidget.setColumnWidth(3, 130)
            self.tabelwidget.setColumnWidth(4, 80)
            self.tabelwidget.setColumnWidth(5, 75)

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()
            cursor.execute(
                "SELECT ID, Navn, Start, Slut, Budget_DKK, KundeID FROM Projekt")

            self.tabelwidget.setRowCount(0)

            for row_number, row_data in enumerate(cursor.fetchall()):
                self.tabelwidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tabelwidget.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

        def ScrumMaster(self):
            widget.addWidget(ScrumMaster())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def konsulenter(self):
            widget.addWidget(SELECT_FROM_KONSULETER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def beregn(self):
            widget.addWidget(SELECT_FROM_REGISTRERINGER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def kunder(self):
            widget.addWidget(SELECT_FROM_KUNDER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def logud(self):
            widget.addWidget(Forside())
            widget.setCurrentIndex(widget.currentIndex()+1)

    # Scrum Master: Se eksisterende konsulenter
    class SELECT_FROM_KONSULETER(QMainWindow):
        def __init__(self):
            super(SELECT_FROM_KONSULETER, self).__init__()
            loadUi("files/ScrumMaster/Konsulent.ui", self)
            self.navn.setText(global_navn)
            self.hjem_knap.clicked.connect(self.ScrumMaster)
            self.projekter_knap.clicked.connect(self.projekter)
            self.registreringer_knap.clicked.connect(self.registreringer)
            self.kunder_knap.clicked.connect(self.kunder)
            self.logud_knap.clicked.connect(self.logud)
            self.tilknytkonsulent_knap.clicked.connect(self.tilknytkonsulent)
            self.slet_knap.clicked.connect(self.slet)
            self.refresh_knap.clicked.connect(self.refresh)
            self.refresh_knap_2.clicked.connect(self.refresh2)
            self.tabelwidget.setColumnWidth(0, 30)
            self.tabelwidget.setColumnWidth(1, 80)
            self.tabelwidget.setColumnWidth(2, 80)
            self.tabelwidget.setColumnWidth(3, 80)
            self.tabelwidget.setColumnWidth(4, 110)
            self.tabelwidget.setColumnWidth(5, 250)
            self.tabelwidget.setColumnWidth(6, 95)
            self.tabelwidget_2.setColumnWidth(0, 180)
            self.tabelwidget_2.setColumnWidth(1, 300)

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()

            cursor.execute("SELECT Navn FROM Projekt")
            projekter = [i[0] for i in cursor.fetchall()]

            for x in projekter:
                self.projekt_combo.addItem(x)

            cursor.execute(
                "SELECT Fornavn FROM Medarbejder WHERE Titel = 'Konsulent' and Status = 'Ikke-tilknyttet'")

            konsulenter = [i[0] for i in cursor.fetchall()]

            for x in konsulenter:
                self.konsulent_combo.addItem(x)

            cursor.execute(
                "SELECT ID, Fornavn, Titel, Dato_ansat, Telefon, Email, Timelon, Status FROM Medarbejder WHERE Titel = 'Konsulent'")
            self.tabelwidget.setRowCount(0)

            for row_number, row_data in enumerate(cursor.fetchall()):
                self.tabelwidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tabelwidget.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

            cursor.execute(
                "SELECT Projekt_navn, Medarbejder_navn FROM Projekt_har_medarbejder")
            self.tabelwidget_2.setRowCount(0)

            for row_numberr, row_dataa in enumerate(cursor.fetchall()):
                self.tabelwidget_2.insertRow(row_numberr)

                for column_numberr, dataa in enumerate(row_dataa):
                    self.tabelwidget_2.setItem(
                        row_numberr, column_numberr, QTableWidgetItem(str(dataa)))

            cursor.execute(
                "SELECT COUNT(ID) FROM Medarbejder WHERE Titel = 'konsulent'")
            for x in cursor.fetchone():
                self.konsulentcount.setText(f"Konsulenter: {x}")

        def tilknytkonsulent(self):
            konsulent = self.konsulent_combo.currentText()
            projekt = self.projekt_combo.currentText()

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()
            cursor.execute(
                f"SELECT ID FROM Medarbejder WHERE Fornavn = '{konsulent}'")
            for x in cursor.fetchone():
                konsulentID = x

            cursor.execute(f"SELECT ID FROM Projekt WHERE Navn = '{projekt}'")
            for x in cursor.fetchone():
                projektID = x

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()
            cursor.execute(
                f"INSERT INTO Projekt_har_medarbejder (ProjektID, Projekt_navn, MedarbejderID, Medarbejder_navn, Tilknyttet) VALUES ('{projektID}','{projekt}', '{konsulentID}', '{konsulent}', '{dato}');")

            cursor.execute(
                f"UPDATE Medarbejder SET Status = 'Tilknyttet' WHERE ID = {konsulentID}")

            thisCon.commit()
            thisCon.close()
            self.noterror2.setText(
                f"Konsulent: {konsulent} tilknyttet projekt")

        def slet(self):
            konsulent_navn = self.konsulentnavn_input.text().title()
            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()

            cursor.execute(
                "SELECT Medarbejder_navn FROM Projekt_har_medarbejder")
            tilknyttede_konsulenter = [i[0] for i in cursor.fetchall()]

            if len(konsulent_navn) == 0:
                self.error2.setText("Udfyld venligst feltet")

            elif konsulent_navn not in tilknyttede_konsulenter:
                self.error2.setText(
                    "Denne konsulent er ikke tilknyttet et projekt")

            else:
                konsulent_navn = self.konsulentnavn_input.text().title()
                thisCon = Connection.dbconnect()
                cursor = thisCon.cursor()

                cursor.execute(
                    f"DELETE FROM Projekt_har_medarbejder WHERE Medarbejder_navn = '{konsulent_navn}'")
                cursor.execute(
                    f"UPDATE Medarbejder SET Status = 'Ikke-tilknyttet' WHERE Fornavn = '{konsulent_navn}'")

                thisCon.commit()
                thisCon.close()
                self.noterror2.setText("Konsulent slettet fra projekt")

        def refresh(self):
            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()

            cursor.execute(
                "SELECT Projekt_navn, Medarbejder_navn FROM Projekt_har_medarbejder")
            self.tabelwidget_2.setRowCount(0)

            for row_number, row_data in enumerate(cursor.fetchall()):
                self.tabelwidget_2.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tabelwidget_2.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

        def refresh2(self):
            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()

            cursor.execute(
                "SELECT ID, Fornavn, Titel, Dato_ansat, Telefon, Email, Timelon, Status FROM Medarbejder WHERE Titel = 'Konsulent'")
            self.tabelwidget.setRowCount(0)

            for row_number, row_data in enumerate(cursor.fetchall()):
                self.tabelwidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tabelwidget.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

        def ScrumMaster(self):
            widget.addWidget(ScrumMaster())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def projekter(self):
            widget.addWidget(SELECT_FROM_PROJEKTER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def registreringer(self):
            widget.addWidget(SELECT_FROM_REGISTRERINGER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def kunder(self):
            widget.addWidget(SELECT_FROM_KUNDER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def logud(self):
            widget.addWidget(Forside())
            widget.setCurrentIndex(widget.currentIndex()+1)

    # ScrumMaster: Se eksisterende registreringer samt foretag faktueringer
    class SELECT_FROM_REGISTRERINGER(QMainWindow):
        def __init__(self):
            super(SELECT_FROM_REGISTRERINGER, self).__init__()
            loadUi("files/ScrumMaster/registrering.ui", self)
            self.hjem_knap.clicked.connect(self.ScrumMaster)
            self.projekter_knap.clicked.connect(self.projekter)
            self.konsulenter_knap.clicked.connect(self.konsulenter)
            self.kunder_knap.clicked.connect(self.kunder)
            self.logud_knap.clicked.connect(self.logud)
            self.beregn_omkostninger_knap.clicked.connect(
                self.beregn_omkostninger)
            self.faktura_knap.clicked.connect(self.faktura)
            self.navn.setText(global_navn)
            self.tabelwidget.setColumnWidth(0, 120)
            self.tabelwidget.setColumnWidth(1, 120)
            self.tabelwidget.setColumnWidth(2, 120)
            self.tabelwidget.setColumnWidth(3, 100)
            self.tabelwidget.setColumnWidth(4, 100)
            self.tabelwidget.setColumnWidth(5, 150)

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()

            cursor.execute(
                "SELECT Dato, Starttidspunkt, Sluttidspunkt, ProjektID, MedarbejderID, Omkostning FROM Sprint_registrering")

            self.tabelwidget.setRowCount(0)

            for row_number, row_data in enumerate(cursor.fetchall()):
                self.tabelwidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tabelwidget.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

            cursor.execute("SELECT SUM(Omkostning) FROM Sprint_registrering")
            for x in cursor.fetchone():
                self.payments.setText(f"{x} DKK")

        def beregn_omkostninger(self):
            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()
            cursor.execute("SELECT ProjektID FROM Sprint_registrering")
            projekter = [str(i[0]) for i in cursor.fetchall()]
            projektID = self.projektID_input.text()

            if len(projektID) == 0:
                self.error.setText("Udfyld venligst feltet")

            elif projektID not in projekter:
                self.error.setText("ID eksisterer ikke")
                cursor = thisCon.cursor()
                cursor.execute(
                    f"SELECT SUM(Omkostning) FROM Sprint_registrering")
                for x in cursor.fetchone():
                    self.payments.setText(f"{x} DKK")

            else:
                cursor = thisCon.cursor()
                cursor = thisCon.cursor()
                cursor.execute(
                    f"SELECT SUM(Omkostning) FROM Sprint_registrering WHERE ProjektID = '{projektID}'")
                for x in cursor.fetchone():
                    self.payments.setText(f"{x} DKK")

        def faktura(self):
            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()
            cursor.execute("SELECT ProjektID FROM Sprint_registrering")
            projekter = [str(i[0]) for i in cursor.fetchall()]

            projektID = self.projektID_input.text()

            if len(projektID) == 0:
                self.error.setText("Udfyld venligst feltet")

            elif projektID not in projekter:
                self.error.setText("ID eksisterer ikke")

            else:
                cursor = thisCon.cursor()
                cursor.execute(
                    f"SELECT SUM(Omkostning) FROM Sprint_registrering WHERE projektID = '{projektID}'")
                for x in cursor.fetchone():
                    kostpris = x

                cursor.execute(
                    f"SELECT KundeID FROM Projekt WHERE ID = '{projektID}'")

                for x in cursor.fetchone():
                    kundeID = x

                thisCon = Connection.dbconnect()
                cursor = thisCon.cursor()

                cursor.execute(
                    f"INSERT INTO Faktura (KundeID, ProjektID, Dato, Belob, Status) Values ({kundeID}, {projektID}, '{dato}',{kostpris}, 'Venter')")

                thisCon.commit()
                thisCon.close()

                # Kvittering på højre side
                thisCon = Connection.dbconnect()
                cursor = thisCon.cursor()

                cursor.execute(
                    f"SELECT ID FROM Faktura WHERE ProjektID = '{projektID}'")

                for x in cursor.fetchone():
                    self.FakturaID.setText(f"{x}")
                    self.KundeID.setText(f"{kundeID}")
                    self.ProjektID.setText(f"{projektID}")
                    self.Kostpris.setText(f"{kostpris}")
                    self.Dato.setText(f"{dato}")
                    self.noterror.setText("Faktura oprettet")

        def ScrumMaster(self):
            widget.addWidget(ScrumMaster())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def projekter(self):
            widget.addWidget(SELECT_FROM_PROJEKTER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def konsulenter(self):
            widget.addWidget(SELECT_FROM_KONSULETER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def kunder(self):
            widget.addWidget(SELECT_FROM_KUNDER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def logud(self):
            widget.addWidget(Forside())
            widget.setCurrentIndex(widget.currentIndex()+1)

    # ScrumMaster: Se eksisterende eller opret nye kunder
    class SELECT_FROM_KUNDER(QMainWindow):
        def __init__(self):
            super(SELECT_FROM_KUNDER, self).__init__()
            loadUi("files/ScrumMaster/Kunde.ui", self)
            self.hjem_knap.clicked.connect(self.ScrumMaster)
            self.projekter_knap.clicked.connect(self.projekter)
            self.konsulenter_knap.clicked.connect(self.konsulenter)
            self.registreringer_knap.clicked.connect(self.registreringer)
            self.logud_knap.clicked.connect(self.logud)
            self.navn.setText(global_navn)
            self.tabelwidget.setColumnWidth(0, 40)
            self.tabelwidget.setColumnWidth(1, 250)
            self.tabelwidget.setColumnWidth(2, 250)

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()
            cursor.execute("SELECT * FROM Kunde")

            self.tabelwidget.setRowCount(0)

            for row_number, row_data in enumerate(cursor.fetchall()):
                self.tabelwidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tabelwidget.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

        def ScrumMaster(self):
            widget.addWidget(ScrumMaster())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def projekter(self):
            widget.addWidget(SELECT_FROM_PROJEKTER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def konsulenter(self):
            widget.addWidget(SELECT_FROM_KONSULETER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def registreringer(self):
            widget.addWidget(SELECT_FROM_REGISTRERINGER())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def logud(self):
            widget.addWidget(Forside())
            widget.setCurrentIndex(widget.currentIndex()+1)

    ###### Klasser og funktioner tilhørende en Manager ######

    # Manager: Hjem

    class Manager(QMainWindow):
        def __init__(self):
            super(Manager, self).__init__()
            loadUi("files/Manager/Manager_hjem.ui", self)
            self.modi_instans.clicked.connect(self.modificer_instanser)
            self.fakturering_knap.clicked.connect(self.faktura)
            self.logud_knap.clicked.connect(self.logud)

        ################################################################ FIXED INFO #################################################################
            self.tabelwidget.setColumnWidth(0, 100)
            self.tabelwidget.setColumnWidth(1, 500)
            self.tabelwidget.setColumnWidth(2, 89)

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()
            cursor.execute(
                f"SELECT concat(Fornavn, ' ', Efternavn) FROM Medarbejder WHERE Email = '{Global_email}'")
            for x in cursor.fetchone():
                global global_navn
                global_navn = x
                self.navn.setText(global_navn)

            cursor.execute(
                "SELECT Medarbejder, Text, Dato FROM Note ORDER BY ID DESC")

            self.tabelwidget.setRowCount(0)

            for row_number, row_data in enumerate(cursor.fetchall()):
                self.tabelwidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tabelwidget.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

        ################################################################ FIXED INFO #################################################################

        def modificer_instanser(self):
            widget.addWidget(ModificerInstanser())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def faktura(self):
            widget.addWidget(GodkendFaktura())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def logud(self):
            widget.addWidget(Forside())
            widget.setCurrentIndex(widget.currentIndex()+1)

    # Manager: Her kan manager oprette/slette indhold fra databasen; Medarbejdere, kunde, projekter

    class ModificerInstanser(QMainWindow):
        def __init__(self):
            super(ModificerInstanser, self).__init__()
            loadUi("files/Manager/modificer_instanser.ui", self)
            self.opretmedarbejder_knap.clicked.connect(self.opretmedarbejder)
            self.opretkunde_knap.clicked.connect(self.opretkunde)
            self.opretprojekt_knap.clicked.connect(self.opretprojekt)
            self.hjem_knap.clicked.connect(self.hjem)
            self.fakturering_knap.clicked.connect(self.fakturering)
            self.logud_knap.clicked.connect(self.logud)

            ################################################################ FIXED INFO #################################################################
            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()

            cursor.execute(
                f"SELECT concat(Fornavn, ' ', Efternavn) FROM Medarbejder WHERE Email = '{Global_email}'")

            for i in cursor.fetchone():
                self.navn.setText(i)

            cursor.execute("SELECT Navn FROM Kunde")
            kunder = [i[0] for i in cursor.fetchall()]

            for x in kunder:
                self.kunde_comboBox.addItem(x)

        def hjem(self):
            widget.addWidget(Manager())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def fakturering(self):
            widget.addWidget(GodkendFaktura())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def logud(self):
            widget.addWidget(Forside())
            widget.setCurrentIndex(widget.currentIndex()+1)

            ################################################################ FIXED INFO #################################################################

        def opretmedarbejder(self):
            import random
            fornavn = self.medarbejder_fornavn_input.text().title()
            efternavn = self.medarbejder_efternavn_input.text().title()
            telefon = self.medarbejder_tlf_input.text()
            email = self.medarbejder_email_input.text()
            adgangskode = ''.join(
                (random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(10)))
            timelon = self.medarbejder_timelon_input.text()
            titel = self.rolle_comboBox.currentText()

            if len(fornavn) > 0 or len(efternavn) > 0 or len(telefon) > 0 or len(email) > 0 > len(timelon):

                if titel == 'Manager':

                    thisCon = Connection.dbconnect()
                    cursor = thisCon.cursor()

                    cursor.execute(
                        f"INSERT INTO Medarbejder (Fornavn, Efternavn, Telefon, Dato_ansat, Titel, Email, Adgangskode, Timelon) VALUES ('{fornavn}', '{efternavn}', '{telefon}', '{dato}', '{titel}', '{email}', '{adgangskode}', '{timelon}')")
                    thisCon.commit()
                    thisCon.close()
                    self.noterror.setText(
                        f"Medarbejder: {fornavn},  Adgangskode: {adgangskode} - Oprettet!")

                else:
                    thisCon = Connection.dbconnect()
                    cursor = thisCon.cursor()

                    cursor.execute(
                        f"INSERT INTO Medarbejder (Fornavn, Efternavn, Telefon, Dato_ansat, Titel, Email, Adgangskode, Timelon, Status) VALUES ('{fornavn}', '{efternavn}', '{telefon}', '{dato}', '{titel}', '{email}', '{adgangskode}', '{timelon}', 'Ikke-tilknyttet')")
                    thisCon.commit()
                    thisCon.close()
                    self.noterror.setText(
                        f"Medarbejder: {fornavn},  Adgangskode: {adgangskode} - Oprettet!")

            else:
                self.error.setText("Udfyld venligst alle felter")

        def opretkunde(self):
            kundenavn = self.kundenavn_input.text().title()
            cvr = self.kundecvr_input.text()
            kundetelefon = self.kundetlf_input.text()

            if len(kundenavn) == 0 or len(cvr) == 0 or len(kundetelefon) == 0:
                self.error.setText("Udfyld venligst alle felter")

            else:
                thisCon = Connection.dbconnect()
                cursor = thisCon.cursor()

                cursor.execute(
                    f"INSERT INTO Kunde (Navn, CVR, Telefon) VALUES ('{kundenavn}', '{cvr}', '{kundetelefon}') ")
                thisCon.commit()
                thisCon.close()
                self.noterror.setText(
                    f"Kunde: {kundenavn},  CVR: {cvr} - Oprettet!")

        def opretprojekt(self):
            projektnavn = self.projekt_navn_input.text().title()
            startdato = self.startdato_input.text()
            slutdato = self.slutdato_input.text()
            budget = self.budget_input.text()
            kunde = self.kunde_comboBox.currentText()

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()
            cursor.execute(f"SELECT ID FROM Kunde WHERE Navn = '{kunde}'")
            for i in cursor.fetchone():
                kundeid = i

            if len(projektnavn) == 0 or len(startdato) == 0 or len(slutdato) == 0 or len(budget) == 0:
                self.error.setText("udfyld venligst alle felter")

            else:
                thisCon = Connection.dbconnect()
                cursor = thisCon.cursor()

                cursor.execute(
                    f"INSERT INTO Projekt (Navn, Start, Slut, Budget_DKK, KundeID) VALUES ('{projektnavn}', '{startdato}', '{slutdato}', '{budget}', '{kundeid}')")
                thisCon.commit()
                thisCon.close()
                self.noterror.setText(
                    f"Projekt: {projektnavn},  Tilhørende kunde: {kunde} - Oprettet!")

    # Manager: Fakturering. Her kan Manager godkende fakturaer

    class GodkendFaktura(QMainWindow):
        def __init__(self):
            super(GodkendFaktura, self).__init__()
            loadUi("files/Manager/fakturering.ui", self)
            self.hjem_knap.clicked.connect(self.hjem)
            self.modi_instans.clicked.connect(self.modificer_instanser)
            self.logud_knap.clicked.connect(self.logud)
            self.godkend_knap.clicked.connect(self.godkend)
            self.afvis_knap.clicked.connect(self.afvis)
            self.tabelwidget.setColumnWidth(0, 120)
            self.tabelwidget.setColumnWidth(1, 120)
            self.tabelwidget.setColumnWidth(2, 120)
            self.tabelwidget.setColumnWidth(3, 150)
            self.tabelwidget.setColumnWidth(4, 150)
            self.tabelwidget.setColumnWidth(5, 150)

        ################################################################ FIXED INFO #################################################################

            thisCon = Connection.dbconnect()
            cursor = thisCon.cursor()

            cursor.execute(
                f"SELECT concat(Fornavn, ' ', Efternavn) FROM Medarbejder WHERE Email = '{Global_email}'")

            for i in cursor.fetchone():
                self.navn.setText(i)

            cursor.execute("SELECT * FROM Faktura")

            self.tabelwidget.setRowCount(0)

            for row_number, row_data in enumerate(cursor.fetchall()):
                self.tabelwidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tabelwidget.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

        def hjem(self):
            widget.addWidget(Manager())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def modificer_instanser(self):
            widget.addWidget(ModificerInstanser())
            widget.setCurrentIndex(widget.currentIndex()+1)

        def logud(self):
            widget.addWidget(Forside())
            widget.setCurrentIndex(widget.currentIndex()+1)

        ################################################################ FIXED INFO #################################################################

        def godkend(self):
            fakturaID = self.fakturaId_input.text()

            if len(fakturaID) == 0:
                self.error.setText("Udfyld venligst feltet")

            else:
                thisCon = Connection.dbconnect()
                cursor = thisCon.cursor()

                cursor.execute(
                    (f"UPDATE Faktura SET Status = 'Godkendt' WHERE ID = '{fakturaID}'"))
                thisCon.commit()
                thisCon.close()
                self.noterror.setText(f"Faktura: {fakturaID} er nu Godkendt")

        def afvis(self):
            fakturaID = self.fakturaId_input.text()

            if len(fakturaID) == 0:
                self.error.setText("Udfyld venligst feltet")

            else:
                thisCon = Connection.dbconnect()
                cursor = thisCon.cursor()

                cursor.execute(
                    (f"UPDATE Faktura SET Status = 'Afvist' WHERE ID = '{fakturaID}'"))
                thisCon.commit()
                thisCon.close()
                self.noterror.setText(f"Faktura: {fakturaID} er nu Afvist")

    ################ APP fixed indstillinger ##################
    app = QApplication(sys.argv)

    mainWindow = Forside()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainWindow)
    widget.setFixedWidth(1000)
    widget.setFixedHeight(600)
    widget.setWindowTitle(
        "AgileTimeTracker+")
    widget.show()
    app.exec()
    ################ APP fixed indstillinger ##################


main()
