# Script for "Create AgileTrimeTracker Database"
# Oprettet: 15. december 2020
# Redigeret: 17. december 2020
# Dev team: Gruppe2 - Sohrab, Gustav, Emil, Mathias, Sebastian
# Projekt: Big Corp - Semesterprojekt, modul 5
# Hold: BE-IT S21DA (2. semester)
# Institut: Københavns Erhvervsakademi, Guldbergsgade


# Modul for mysql forbindelse importeres
import mysql.connector as mc
# Relevante variabler hentes fra Connection.py
from Connection import host, user, password

# En forbindelse defineres
mydb = mc.connect(
    host=host,
    user=user,
    password=password,
    database='sys'
)

# Pegenpind defineres
cursor = mydb.cursor()

# 1. oprettes en database
cursor.execute("CREATE SCHEMA AgileTimeTracker")

# 2. Kundetabel oprettes
cursor.execute('''
CREATE TABLE AgileTimeTracker.Kunde (
  ID int NOT NULL AUTO_INCREMENT,
  Navn varchar(45) DEFAULT NULL,
  CVR int DEFAULT NULL,
  Telefon varchar(45) DEFAULT NULL,
  PRIMARY KEY (ID));
''')


# 2.1 Kunder indsættes i kundetabel
cursor.execute('''
INSERT INTO AgileTimeTracker.Kunde (ID,Navn,CVR,Telefon)
VALUES

(1,'Danske Bank A/S',61126228, 76171322),
(2,'Nordea Finans Danmark A/S',21634905, 54344678),
(3,'Visma Dinero ApS',34731543, 95845519),
(4,'EPOS GROUP A/S',39820242, 36089669),
(5,'Sentia Denmark A/S',10008123, 51950813),
(6,'Microsoft Danmark ApS',13612870, 25647433),
(7,'Rigshospitalet',41469269, 75773241),
(8,'Elgiganten A/S',17237977, 98885827),
(9,'Power A/S',25380088, 46327365),
(10,'TDC A/S',14773908, 42023090),
(11,'Netcompany Group A/S',39488914, 93500605),
(13,'KPMG ApS',74912739, 60293844),
(14,'GLS ApS',21323142, 47730735),
(15,'Copenhagen Business School',27318421, 38599801),
(16,'Syddansk Universitet',12378421, 95180874);
''')

# 3. Medarbejdertabel oprettes
cursor.execute('''
CREATE TABLE AgileTimeTracker.Medarbejder (
  ID int NOT NULL AUTO_INCREMENT,
  Fornavn varchar(45) DEFAULT NULL,
  Efternavn varchar(45) DEFAULT NULL,
  Telefon varchar(45) DEFAULT NULL,
  Dato_ansat varchar(45) DEFAULT NULL,
  Titel varchar(45) DEFAULT NULL,
  Email varchar(45) DEFAULT NULL,
  Adgangskode varchar(45) DEFAULT NULL,
  Timelon int DEFAULT NULL,
  Status varchar(45) DEFAULT NULL,
  PRIMARY KEY (ID));
''')


# 3.1 medarbejdere indsættes i medarbejdertabellen
cursor.execute('''
INSERT INTO AgileTimeTracker.Medarbejder (ID, Fornavn, Efternavn, Telefon, Dato_ansat, Titel, Email, Adgangskode, Timelon, Status)
VALUES
(1, 'Tierney', 'Feige', '1357652789', '04.07.2021', 'ScrumMaster', 'tfeige0@seattletimes.com', 'JaLa3gz', 684, 'Ikke-tilknyttet'),
(2, 'Matias', 'Darlasson', '3605272545', '25.11.2018', 'ScrumMaster', 'mdarlasson1@opensource.org', 'Tm4arqo2j', 578, 'Ikke-tilknyttet'),
(3, 'Liana', 'Gibard', '9796506382', '30.04.2015', 'Manager', 'lgibard2@moonfruit.com', '4pjmkAIL4b', 427, 'Tilknyttet'),
(4, 'Doro', 'Avey', '4489114612', '29.11.2018', 'Konsulent', 'davey3@example.com', 'da61gaDapCB', 358, 'Ikke-tilknyttet'),
(5, 'Dukie', 'Cuffin', '6528623647', '05.10.2018', 'ScrumMaster', 'dcuffin4@rambler.ru', 'FGDX6uzN', 456, 'Ikke-tilknyttet'),
(6, 'Brocky', 'Mounch', '1596492563', '26.06.2018', 'Manager', 'bmounch5@aol.com', 'xyqRvjtY', 519, 'Ikke-tilknyttet'),
(7, 'Emelyne', 'Lowndes', '2597150281', '24.05.2015', 'Konsulent', 'elowndes6@networksolutions.com', 'pik9NVvZ', 613, 'Tilknyttet'),
(8, 'Dalila', 'Solly', '5129907971', '11.04.2020', 'Konsulent', 'dsolly7@1688.com', 'wST9aeL', 613, 'Tilknyttet'),
(9, 'Dane', 'Merrigan', '3791201213', '04.03.2019', 'Manager', 'dmerrigan8@mit.edu', 'yHN3jWPvbq', 666, 'Tilknyttet'),
(10, 'Hamish', 'Meekins', '9868199045', '22.01.2017', 'ScrumMaster', 'hmeekins9@imdb.com', '7MMWjV', 734, 'Tilknyttet'),
(11, 'Kermy', 'Finkle', '4132032068', '01.09.2021', 'Konsulent', 'kfinklea@linkedin.com', 'XIwObeAqR', 573, 'Tilknyttet'),
(12, 'Kristo', 'Wrassell', '1322180209', '29.02.2016', 'Manager', 'kwrassellb@deviantart.com', 'eXkN8ki1B3', 705, 'Tilknyttet'),
(13, 'Miltie', 'Geater', '9788232109', '14.12.2018', 'Konsulent', 'mgeaterc@eventbrite.com', 'eMX4xCiNr', 606, 'Tilknyttet'),
(14, 'Carmella', 'McKernan', '4801009628', '28.05.2020', 'Manager', 'cmckernand@tumblr.com', 'eJxMJBcI', 390, 'Tilknyttet'),
(15, 'Tani', 'Marshal', '3177376819', '31.07.2015', 'Konsulent', 'tmarshale@rakuten.co.jp', 'Eui7LeXQvNAV', 368, 'Ikke-tilknyttet'),
(16, 'Channa', 'Eilers', '5667352309', '09.02.2020', 'Manager', 'ceilersf@shareasale.com', '3HZLaJBPQ', 639, 'Ikke-tilknyttet'),
(17, 'Norri', 'Albrighton', '5002922085', '31.10.2019', 'Konsulent', 'nalbrightong@de.vu', 'a6t2zv0Qjr', 299, 'Tilknyttet'),
(18, 'Tris', 'Jankiewicz', '7531171521', '16.04.2017', 'Konsulent', 'tjankiewiczh@yandex.ru', '18aAsElp', 511, 'Ikke-tilknyttet'),
(19, 'Jocko', 'Philippou', '7399336552', '28.08.2021', 'Manager', 'jphilippoui@hexun.com', 'TTSiifK6d', 450, 'Tilknyttet'),
(20, 'Noelle', 'Yurinov', '1028955467', '04.07.2019', 'Manager', 'nyurinovj@pinterest.com', 'Ngu9X9', 585, 'Ikke-tilknyttet'),
(21, 'Vevay', 'Youdell', '7724417900', '09.03.2019', 'Manager', 'vyoudellk@toplist.cz', 'LQA7Mo', 492, 'Tilknyttet'),
(22, 'Robyn', 'Gosnoll', '7591753212', '28.03.2017', 'Konsulent', 'rgosnolll@yandex.ru', 'QnYDfaw', 486, 'Tilknyttet'),
(23, 'Beale', 'Hoy', '6756359385', '12.07.2016', 'Manager', 'bhoym@prlog.org', '7YW18V4Oem5c', 687, 'Ikke-tilknyttet'),
(24, 'Desmond', 'Croizier', '9048542594', '25.04.2019', 'Konsulent', 'dcroiziern@twitpic.com', 'o5itFQjgG0', 471, 'Ikke-tilknyttet'),
(25, 'Claudie', 'Hawler', '1338715429', '17.04.2021', 'Manager', 'chawlero@gmpg.org', '9FS2hh0zDOS', 594, 'Tilknyttet'),
(26, 'Humbert', 'Easson', '7596808495', '31.12.2017', 'ScrumMaster', 'heassonp@howstuffworks.com', 'ApH533KTV', 466, 'Tilknyttet'),
(27, 'Oliviero', 'Walework', '3338265666', '20.07.2017', 'ScrumMaster', 'owaleworkq@who.int', '7tBEaUbexGXm', 375, 'Tilknyttet'),
(28, 'Fred', 'Nutting', '5415352859', '13.06.2018', 'Konsulent', 'fnuttingr@com.com', 'FbqWsQN7SnX', 271, 'Tilknyttet'),
(29, 'Tiebold', 'Arkil', '1287129801', '04.07.2019', 'ScrumMaster', 'tarkils@imgur.com', 'qxSQycQAqF9S', 264, 'Tilknyttet'),
(30, 'Fairleigh', 'Rooksby', '5314587037', '15.01.2017', 'ScrumMaster', 'frooksbyt@ocn.ne.jp', 'soSM2c0Zq1u', 680, 'Ikke-tilknyttet'),
(31, 'Oralle', 'Ouslem', '1553005008', '08.03.2017', 'ScrumMaster', 'oouslemu@hud.gov', 'NzPeg5FjWq', 256, 'Ikke-tilknyttet'),
(32, 'Frederique', 'Antonik', '7735183744', '18.04.2015', 'Konsulent', 'fantonikv@blogspot.com', 'JiPoC5', 615, 'Tilknyttet'),
(33, 'Mikol', 'Vickarman', '9031537969', '29.07.2017', 'Konsulent', 'mvickarmanw@google.co.jp', 'Xhz80S', 309, 'Tilknyttet'),
(34, 'Sylas', 'Beert', '7475950909', '09.08.2018', 'Manager', 'sbeertx@reverbnation.com', 'es4vsJx', 641, 'Tilknyttet'),
(35, 'Celle', 'Tyrwhitt', '6121000477', '08.09.2020', 'Manager', 'ctyrwhitty@arstechnica.com', 'JmzsDpm', 684, 'Tilknyttet'),
(36, 'Max', 'Dawidowicz', '9154941863', '01.07.2018', 'Manager', 'mdawidowiczz@dagondesign.com', 'BHEYlCL', 392, 'Ikke-tilknyttet'),
(37, 'Auberon', 'Woodes', '5614155640', '17.11.2018', 'Manager', 'awoodes10@shop-pro.jp', 'khc8qVB', 643, 'Tilknyttet'),
(38, 'Clemente', 'Dripp', '9278950759', '14.07.2015', 'ScrumMaster', 'cdripp11@washingtonpost.com', 'bN5RxqIY5', 431, 'Tilknyttet'),
(39, 'Rozanna', 'Kiddey', '8862102366', '22.02.2019', 'ScrumMaster', 'rkiddey12@free.fr', 'dqvJvpJfIlp', 681, 'Ikke-tilknyttet'),
(40, 'Gaile', 'Cardo', '2374257183', '05.08.2020', 'Konsulent', 'gcardo13@naver.com', 'Graksy6e', 485, 'Tilknyttet'),
(41, 'Lyn', 'Jerratsch', '3173474078', '07.12.2016', 'Konsulent', 'ljerratsch14@naver.com', 'g7TQOeZOBWW', 743, 'Tilknyttet'),
(42, 'Alvin', 'Hurling', '4685488237', '26.03.2020', 'Konsulent', 'ahurling15@ibm.com', 'mcgt7Xr6', 504, 'Tilknyttet'),
(43, 'Ashley', 'Semiraz', '6548368965', '04.02.2017', 'Manager', 'asemiraz16@skype.com', 'eau9sA19O', 264, 'Ikke-tilknyttet'),
(44, 'Sophronia', 'Dicken', '8151611292', '06.05.2019', 'ScrumMaster', 'sdicken17@ezinearticles.com', 'AaiLvSS', 265, 'Ikke-tilknyttet'),
(45, 'Priscella', 'Kagan', '7447957152', '12.09.2021', 'Konsulent', 'pkagan18@imgur.com', 'KkYkuMD', 487, 'Ikke-tilknyttet'),
(46, 'Malia', 'Searle', '8281187866', '04.02.2017', 'Manager', 'msearle19@salon.com', 'LCrBRNMgs', 394, 'Ikke-tilknyttet'),
(47, 'Kassie', 'Frede', '2155662353', '25.05.2021', 'ScrumMaster', 'kfrede1a@nps.gov', 'yX7Ktj8Coe', 533, 'Tilknyttet'),
(48, 'Cirstoforo', 'Mitchel', '4211588433', '01.11.2015', 'Manager', 'cmitchel1b@ask.com', 'oHMQugtRV4C', 294, 'Ikke-tilknyttet'),
(49, 'Marin', 'Petruszka', '3791867218', '16.03.2020', 'ScrumMaster', 'mpetruszka1c@imgur.com', 'HxbwqcmeO', 635, 'Tilknyttet'),
(50, 'Cora', 'Keming', '5934879129', '11.04.2016', 'Manager', 'ckeming1d@prnewswire.com', 'ELphQGJomIL', 227, 'Tilknyttet'),
(51, 'Melony', 'Bedding', '6904108262', '22.11.2017', 'Manager', 'mbedding1e@delicious.com', 'XrcifZD', 635, 'Tilknyttet'),
(52, 'Violante', 'Egentan', '4171831328', '17.04.2016', 'ScrumMaster', 'vegentan1f@seesaa.net', 'qJXlU8', 424, 'Tilknyttet'),
(53, 'Jsandye', 'Danielovitch', '5243824835', '13.01.2020', 'Manager', 'jdanielovitch1g@unblog.fr', 'DBvmOEfV', 237, 'Ikke-tilknyttet'),
(54, 'Valeria', 'Jenne', '6942161155', '17.02.2015', 'Manager', 'vjenne1h@webs.com', 'pgZstCfQ', 566, 'Tilknyttet'),
(55, 'Maisie', 'Whitlow', '2066455329', '02.03.2021', 'ScrumMaster', 'mwhitlow1i@rediff.com', 'oObYTlcgxG5', 746, 'Tilknyttet'),
(56, 'Asa', 'Huskinson', '4049040569', '30.10.2017', 'ScrumMaster', 'ahuskinson1j@theguardian.com', 'SUPHgAIZ', 379, 'Ikke-tilknyttet'),
(57, 'Briney', 'Cotsford', '8957775522', '04.09.2015', 'Manager', 'bcotsford1k@phoca.cz', 'AXmGMQcb', 289, 'Ikke-tilknyttet'),
(58, 'Lynne', 'Crickmoor', '5318036664', '17.04.2015', 'Manager', 'lcrickmoor1l@about.me', 'HiA8lPQ', 704, 'Tilknyttet'),
(59, 'Bridgette', 'McDowell', '4122647547', '10.05.2018', 'ScrumMaster', 'bmcdowell1m@bbb.org', 'kiZfUqGdiz', 465, 'Tilknyttet'),
(60, 'Billie', 'de Courcey', '8942681477', '02.05.2017', 'Konsulent', 'bdecourcey1n@soup.io', 'hTtWKe9S', 449, 'Ikke-tilknyttet'),
(61, 'Boyd', 'Triebner', '4286155160', '25.11.2017', 'Konsulent', 'btriebner1o@businesswire.com', '3WGMW7iV', 577, 'Tilknyttet'),
(62, 'Gigi', 'Bessant', '9774112898', '22.01.2020', 'Manager', 'gbessant1p@homestead.com', 'lZGWM78', 351, 'Tilknyttet'),
(63, 'Gustave', 'Street', '8677855915', '26.11.2018', 'Konsulent', 'gstreet1q@yellowpages.com', 'L1mDCXX', 242, 'Ikke-tilknyttet'),
(64, 'Laughton', 'Miskimmon', '9518570120', '23.10.2018', 'ScrumMaster', 'lmiskimmon1r@fotki.com', 'Uh9YAar8Q', 237, 'Tilknyttet'),
(65, 'Karalee', 'Starton', '8721099640', '12.12.2016', 'Manager', 'kstarton1s@cnbc.com', '8OqL5VAOIbi', 628, 'Tilknyttet'),
(66, 'Domingo', 'Brookwell', '1363051023', '12.12.2020', 'Manager', 'dbrookwell1t@discuz.net', 'bOkVLedEdHY', 406, 'Tilknyttet'),
(67, 'Lethia', 'Lowndsborough', '9368043409', '06.08.2015', 'Manager', 'llowndsborough1u@pinterest.com', 'ssH9Wd9K725', 387, 'Ikke-tilknyttet'),
(68, 'Rey', 'Tewkesberry', '5651260407', '27.07.2016', 'ScrumMaster', 'rtewkesberry1v@t-online.de', 'LeuxqzK000O', 419, 'Tilknyttet'),
(69, 'Linn', 'Slinn', '4361509310', '20.08.2018', 'Manager', 'lslinn1w@usa.gov', 'QEQthHFte', 290, 'Ikke-tilknyttet'),
(70, 'Armstrong', 'Lampart', '1945068149', '08.10.2018', 'Konsulent', 'alampart1x@buzzfeed.com', '4NaVt7cjsb', 319, 'Tilknyttet'),
(71, 'Hyman', 'O''Devey', '6082408090', '31.07.2017', 'Konsulent', 'hodevey1y@deviantart.com', '85NBAOo70K2', 580, 'Ikke-tilknyttet'),
(72, 'Ransom', 'Yon', '5984505131', '25.10.2021', 'Konsulent', 'ryon1z@pbs.org', 'zACbpfb', 555, 'Tilknyttet'),
(73, 'Correna', 'Notti', '7827103858', '06.03.2015', 'ScrumMaster', 'cnotti20@wiley.com', 'svaaFihSjor', 425, 'Ikke-tilknyttet'),
(74, 'Ricardo', 'Curreen', '4131108160', '13.01.2018', 'Konsulent', 'rcurreen21@live.com', 'Xlmaqc', 638, 'Ikke-tilknyttet'),
(75, 'Jacquenette', 'Restall', '8257978626', '24.11.2015', 'Konsulent', 'jrestall22@360.cn', 'IFidVRcI8Wz', 701, 'Ikke-tilknyttet'),
(76, 'Burgess', 'Lobe', '7522200379', '29.01.2019', 'Konsulent', 'blobe23@google.de', 'NuP7xteA', 365, 'Ikke-tilknyttet'),
(77, 'Lanie', 'Axe', '9601228500', '24.07.2016', 'Konsulent', 'laxe24@wp.com', 'evwopia0Sa', 534, 'Tilknyttet'),
(78, 'Ciro', 'Mew', '2339076405', '27.04.2017', 'ScrumMaster', 'cmew25@pinterest.com', 'AnJxG29bTE', 289, 'Ikke-tilknyttet'),
(79, 'Deny', 'Axelby', '4773448912', '01.08.2019', 'Manager', 'daxelby26@shinystat.com', 'ADG34OF6Wmvl', 676, 'Tilknyttet'),
(80, 'Iona', 'Keri', '7828542510', '17.11.2017', 'Manager', 'ikeri27@theglobeandmail.com', 'yfb0KToG3aeP', 358, 'Tilknyttet'),
(81, 'Derrik', 'Lemmon', '5839116534', '30.08.2018', 'Manager', 'dlemmon28@amazon.co.jp', 'YsFKRZa', 360, 'Tilknyttet'),
(82, 'Loretta', 'Hundy', '4444251844', '16.07.2019', 'ScrumMaster', 'lhundy29@exblog.jp', 'NmcMi1z1uH', 668, 'Tilknyttet'),
(83, 'Brooks', 'Le Gall', '3457695610', '16.03.2017', 'ScrumMaster', 'blegall2a@technorati.com', 'ylrBPeGpbh6', 383, 'Ikke-tilknyttet'),
(84, 'Rip', 'Prendiville', '3371729000', '30.03.2017', 'ScrumMaster', 'rprendiville2b@ameblo.jp', '1TrtEB', 385, 'Tilknyttet'),
(85, 'Claretta', 'Cisneros', '1222492086', '12.02.2019', 'Konsulent', 'ccisneros2c@zdnet.com', 'W2gowbIm0m', 259, 'Tilknyttet'),
(86, 'Sully', 'Berndsen', '8174107652', '15.09.2015', 'Konsulent', 'sberndsen2d@bandcamp.com', 'CeTwmaimU9', 321, 'Ikke-tilknyttet'),
(87, 'Hyacinth', 'Fairfoot', '6498572762', '15.02.2015', 'ScrumMaster', 'hfairfoot2e@yahoo.co.jp', 'cv9EFtNBx', 377, 'Ikke-tilknyttet'),
(88, 'Feliks', 'Di Napoli', '9251941349', '27.03.2021', 'Manager', 'fdinapoli2f@tinyurl.com', 'ozeFFtKr7n', 390, 'Ikke-tilknyttet'),
(89, 'Johannes', 'Worboy', '9606883040', '10.12.2019', 'Manager', 'jworboy2g@columbia.edu', 'C7X1QQ8zVP', 363, 'Tilknyttet'),
(90, 'Cairistiona', 'MacFadzan', '4999882873', '23.12.2017', 'Manager', 'cmacfadzan2h@github.com', 'ghHstBlTRml1', 231, 'Tilknyttet'),
(91, 'Paolo', 'Ryley', '5581346976', '23.09.2018', 'ScrumMaster', 'pryley2i@miibeian.gov.cn', 'S5doAR', 227, 'Tilknyttet'),
(92, 'Consolata', 'Redmore', '8508775550', '11.02.2017', 'Manager', 'credmore2j@posterous.com', 's6eexL', 427, 'Tilknyttet'),
(93, 'Inglebert', 'Larkkem', '8828996206', '14.06.2016', 'Konsulent', 'ilarkkem2k@cornell.edu', 'eCJHRl', 378, 'Ikke-tilknyttet'),
(94, 'Everett', 'Lean', '2847260647', '03.03.2021', 'Konsulent', 'elean2l@house.gov', 'QRSZo4', 254, 'Ikke-tilknyttet'),
(95, 'Marti', 'Skeels', '3921069677', '04.12.2015', 'ScrumMaster', 'mskeels2m@acquirethisname.com', 'JrNT0c2cg', 438, 'Tilknyttet'),
(96, 'Henrietta', 'Pascow', '5751497480', '14.08.2015', 'ScrumMaster', 'hpascow2n@zdnet.com', 'EVJAJrH58', 272, 'Tilknyttet'),
(97, 'Damiano', 'Gatfield', '5359666509', '15.10.2017', 'ScrumMaster', 'dgatfield2o@dropbox.com', '4TP8loGLu', 653, 'Tilknyttet'),
(98, 'Ennis', 'Pledge', '2549801876', '06.10.2021', 'Manager', 'epledge2p@smugmug.com', 'mwWtWOYVI', 519, 'Tilknyttet'),
(99, 'Lind', 'Girth', '5431716753', '06.08.2017', 'ScrumMaster', 'lgirth2q@nydailynews.com', 'XndWpAsF', 662, 'Tilknyttet'),
(100, 'Dylan', 'Marchant', '3935958650', '10.09.2021', 'Manager', 'dmarchant2r@theatlantic.com', 'W90cbgbQVk', 696, 'Ikke-tilknyttet'),
(101,'Sebastian','Christensen','64203812','11.11.2021','Konsulent','sommer@ibm.dk','123sommer123',225,'Tilknyttet'),
(102,'Sohrab','Malek','93804048','11.11.2021','ScrumMaster','sohrab@ibm.dk','123Nga123',400,'Ikke-tilknyttet'),
(103,'Gustav','Mogensen','64228933','11.11.2021','Konsulent','gustavmogensen@ibm.dk','Mogensen!123',235,'Ikke-tilknyttet'),
(104,'Emil','Bernekilde','71398442','12.11.2021','Konsulent','bernekilde_e@ibm.dk','Bernekild!Emil',245,'Tilknyttet'),
(106,'Henrik','Thomsen','65328361','10.10.2021','Konsulent','henrik@ibm.dk','henriksenForever',375,'Tilknyttet'),
(107,'Michael','OBrian','39283922','21.11.2021','Manager','micheObrian','oobrians',750,'Ikke-tilknyttet');
''')


# 4. Projekttabel oprettes
cursor.execute('''

CREATE TABLE AgileTimeTracker.Projekt (
  ID int NOT NULL AUTO_INCREMENT,
  Navn varchar(45) DEFAULT NULL,
  Start varchar(45) DEFAULT NULL,
  Slut varchar(45) DEFAULT NULL,
  Budget_DKK varchar(45) DEFAULT NULL,
  KundeID int DEFAULT NULL,
  PRIMARY KEY (ID));

''')

# 4.1 Projekter indsættes i projektabellen
cursor.execute('''
INSERT INTO AgileTimeTracker.Projekt (ID,Navn,Start,Slut,Budget_DKK,KundeID)
VALUES
(1,'IT Infrastructure','01.06.2021','01.08.2021','250000',1),
(2,'E-commerce','30.08.2021','15.09.2021','500000',2),
(3,'Cybersecurity','22.07.2021','20.08.2021','175000',11),
(4,'Blockchain','01.12.2021','05.01.2022','375000',3),
(5,'Application Services','11.11.2021','30.11.2021','545000',4),
(6,'Analytics','02.11.2021','27.11.2021','150000',7),
(7,'Hybrid Cloud','23.09.2021','25.12.2021','750000',5),
(8,'Analytics','04.03.2021','05.04.2021','150000',8),
(9,'Cloud computing','17.06.2021','29.07.2021','457000',10),
(10,'E-commerce','11.11.2021','26.01.2022','507500',6),
(11,'Cloud Infrastructure','28.10.2021','01.02.2022','245000',9);
''')

# 5. Projekt_har_medarbejder (Mellemtabel) oprettes
cursor.execute('''
  CREATE TABLE AgileTimeTracker.Projekt_har_medarbejder (
  ID int NOT NULL AUTO_INCREMENT,
  ProjektID int DEFAULT NULL,
  Projekt_navn varchar(45) DEFAULT NULL,
  MedarbejderID int DEFAULT NULL,
  Medarbejder_navn varchar(45) DEFAULT NULL,
  Tilknyttet varchar(45) DEFAULT NULL,
  PRIMARY KEY (ID));
''')


# 5.1 Sprint (Registreringer) oprettes
cursor.execute('''

CREATE TABLE AgileTimeTracker.Sprint_registrering (
  ID int NOT NULL AUTO_INCREMENT,
  Dato varchar(45) DEFAULT NULL,
  Starttidspunkt varchar(45) DEFAULT NULL,
  Sluttidspunkt varchar(45) DEFAULT NULL,
  ProjektID int DEFAULT NULL,
  MedarbejderID int DEFAULT NULL,
  Timer varchar(45) DEFAULT NULL,
  Omkostning int DEFAULT NULL,
  PRIMARY KEY (ID));


''')

# 6. Fakturatabel oprettes
cursor.execute('''

CREATE TABLE AgileTimeTracker.Faktura (
  ID int NOT NULL AUTO_INCREMENT,
  KundeID int DEFAULT NULL,
  ProjektID int DEFAULT NULL,
  Dato varchar(45) DEFAULT NULL,
  Belob int DEFAULT NULL,
  Status varchar(45) DEFAULT NULL,
  PRIMARY KEY (ID));
''')


# 7. Notetabel oprettes - Udgangspunktet er beskeder og nyheder
cursor.execute('''

CREATE TABLE AgileTimeTracker.Note (
  ID int NOT NULL AUTO_INCREMENT,
  Medarbejder varchar(45) DEFAULT NULL,
  Text varchar(1000) DEFAULT NULL,
  Dato varchar(45) DEFAULT NULL,
  PRIMARY KEY (ID));
''')

# 7.1 Noter indsættes i notetabellen
cursor.execute('''
INSERT INTO AgileTimeTracker.Note
VALUES
(1,'Henrik Thomsen','Kære projektledere,  se og få tilmeldt jeres hold til julefrokosten.  Deadline 20.11.2021!','15.11.2021'),
(2,'Gustav Mogensen','Hej allesammen. Husk at få skiftet jeres adgangskode snarest','15.11.2021'),
(3,'Sohrab Malek','Kære nye medarbejdere velkommen til vores nye tidsregistreringssystem.  Her kan i tilgå forskellige funktioner alt efter,  hvilke rolle i har i virksomheden.  Til konsulenterne kan vi med glæde meddele at vi nu har tilføjet en funktion,  hvorpå de kan tjekke ind/ud,  når de går på arbejde.  Til projektlederne er det nu muliggjort at kunne se ledige konsulenter og tilknytte disse til projekter efter ønske.  Til Managers,  kan de nu se frem til en optimeret samt automatiseret ansættelsesprocess.  Mange tak for at bruge vores system.  TEAM: Gruppe 2 ','15.11.2021');

''')

# Ovenstående eksekveres og forbindelse slukkes
mydb.commit()
mydb.close()


print(
    f"\nDatabasen 'AgileTimeTracker' er oprettet med følgende tabeller:\n\n-Medarbejder\n-Kunde\n-Projekter\n-Sprint Registreringer\n-Projekt_har_medarbejder\n-Faktura\n-Note")
