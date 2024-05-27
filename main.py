from WI_P5_DB import Session, engine, Bedarf, Rechnung, Material, Bestand
import sys

my_session = Session(bind=engine)

#--------------------#
Liste = my_session.query(Material).all()

#Bedarfabfrage
sicherheit = 1

print("Willkommen, hier sehen Sie die Materialliste")
print("-------------")
for item in Liste: 
    print(item.materialID,item.material_name)
print("-------------")
bestellung = input('Was benötigen Sie?:')
stueck = int(input('Welche Menge benötigen Sie?:'))
print("-------------")

anzeige = my_session.query(Material).filter(Material.material_name == bestellung)
for item in anzeige:
    bestellung = item.materialID

auftrag = Bedarf(materialID=bestellung,anzahl=stueck)
my_session.add(auftrag)
my_session.commit()


#Kapazitäten-Check1
ins_anzahl = 0
gesamtpreis = 0

bestand = my_session.query(Bestand).filter(Bestand.materialID == bestellung)
for item in bestand:
    ins_anzahl = ins_anzahl + item.anzahl

uebrig = ins_anzahl - stueck

#Vordefinierung
Lager1 = my_session.query(Bestand).filter(Bestand.lagerID == 1, Bestand.materialID == bestellung)
for item in Lager1:
    La1 = item.anzahl

Lager2 = my_session.query(Bestand).filter(Bestand.lagerID == 2, Bestand.materialID == bestellung)
for item in Lager2:
    La2 = item.anzahl

Preis = my_session.query(Material).filter(Material.materialID == bestellung)
for item in Preis:
    price = item.material_price

K_Material = my_session.query(Material).filter(Material.materialID == bestellung)
for item in Preis:
    k_material = item.material_name




#Aktualisierung des Lagerbestandes
if uebrig >= 0:
    if La1 <= stueck:
        stueck = stueck - La1
        my_session.query(Bestand).filter(Bestand.materialID == bestellung, Bestand.lagerID == 1).update(
            {
                Bestand.anzahl: 0
            }
        )
        my_session.commit()
        La2 = La2 - stueck
        my_session.query(Bestand).filter(Bestand.materialID == bestellung, Bestand.lagerID == 2).update(
            {
                Bestand.anzahl: La2
            }
        )
        my_session.commit()
    else:
        La1 = La1 - stueck
        my_session.query(Bestand).filter(Bestand.materialID == bestellung, Bestand.lagerID == 1).update(
            {
                Bestand.anzahl: La1
            }
        )
        my_session.commit()

#Rechnungserstellung    
else:
    abfrage = 1
    real_stueck = stueck - ins_anzahl
    preis = real_stueck * price
    print(bestellung,k_material)
    print("Stückpreis:",price,"  ","Stück:", real_stueck,"   " "Gesamtpreis:", preis,"Euro")
    print("------------")
    sicher_stellung = input("Möchten Sie wirklich eine Rechnung erstellen?:")
    print("------------")
    while(abfrage == 1):
        if sicher_stellung == "Ja":
            lager_abfrage = int(input("In welches Lager soll geliefert werden?:"))
            Neu_Rechnung = Rechnung(lagerID= lager_abfrage,materialID=bestellung,material = k_material,anzahl= real_stueck, gesamtpreis=preis)
            my_session.add(Neu_Rechnung)
            my_session.commit()
            La1 = La1 + real_stueck
            my_session.query(Bestand).filter(Bestand.lagerID == lager_abfrage,Bestand.materialID == bestellung ).update(
                {
                    Bestand.anzahl: La1
                }
            )
            my_session.commit()
            sys.exit()
        elif sicher_stellung == "Nein":
            print("Auf Wiedersehen")
            sys.exit()
        else:
            print("Sie müssen mit Ja oder Nein antworten")
            print("-------------")
            print(bestellung,k_material)
            print("Stückpreis:",price,"  ","Stück:", real_stueck,"   " "Gesamtpreis:", preis,"Euro")
            print("------------")
            sicher_stellung = input("Möchten Sie wirklich eine Rechnung erstellen?:")
        
        
