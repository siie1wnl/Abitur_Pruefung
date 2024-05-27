from WI_P5_DB import sessionmaker
from WI_P5_DB import Bedarf, Bestand, Material, Rechnung, Session, engine

my_session = Session(bind=engine)

Holz = Material(material_name='Holz',material_price= 5.00)
Metall = Material(material_name='Stahl',material_price= 8.50)
Metall2 = Material(material_name='Messing', material_price= 6.00)

anzahl1 = Bestand(lagerID= 1, materialID= 1, anzahl = 100)
anzahl2 = Bestand(lagerID= 1, materialID= 2, anzahl = 50)
anzahl3 = Bestand(lagerID= 1, materialID= 3, anzahl= 0)
anzahl4 = Bestand(lagerID = 2, materialID= 1, anzahl= 0)
anzahl5 = Bestand(lagerID = 2, materialID= 2, anzahl= 200)
anzahl6 = Bestand(lagerID = 2, materialID= 3, anzahl= 0)

my_session.add(Holz)
my_session.add(Metall)
my_session.add(Metall2)
my_session.add(anzahl1)
my_session.add(anzahl2)
my_session.add(anzahl3)
my_session.add(anzahl4)
my_session.add(anzahl5)
my_session.add(anzahl6)

my_session.commit()
