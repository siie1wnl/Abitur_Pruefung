from datetime import date, datetime
from decimal import FloatOperation
from sqlalchemy import PrimaryKeyConstraint, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, Integer, Float
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
base = declarative_base()
conn = engine.connect()
Session = sessionmaker()

class Bedarf(base):
    __tablename__ = 'Bedarf'
    
    bedarf_id = Column(Integer , primary_key=True, autoincrement=True)
    materialID = Column(Integer , nullable=False)
    anzahl = Column(Integer, nullable=False)
    
    def __init__(self, materialID: int, anzahl: int) -> None:
        self.materialID = materialID
        self.anzahl = anzahl
        
class Bestand(base):
    __tablename__ = 'Bestand'

    bestandID = Column(Integer, primary_key=True, autoincrement=True)
    lagerID = Column(Integer ,nullable=False)
    materialID = Column(Integer, nullable=False)
    anzahl = Column(Integer, nullable=False)

    def __init__(self,lagerID: int, materialID: int, anzahl: int) -> None:
        self.lagerID = lagerID
        self.materialID = materialID
        self.anzahl = anzahl
    
class Material(base):
    __tablename__ = 'Material'

    materialID = Column(Integer, primary_key=True, nullable=False, autoincrement = True)
    material_name= Column(String, nullable=False)
    material_price= Column(Float, nullable=False)

    def __init__(self,material_name: str, material_price: float) -> None:
        self.material_name = material_name
        self.material_price = material_price

class Rechnung(base):
    __tablename__ = 'Rechnung'

    rechnungID = Column(Integer, primary_key=True, autoincrement=True)
    lagerID = Column(Integer, nullable = False)
    materialID = Column(Integer, nullable = False)
    material = Column(String, nullable = False)
    anzahl = Column(Integer, nullable = False)
    gesamtpreis = Column(Float, nullable = False)


    def __init__(self,lagerID: int, materialID: int, material: str,anzahl: int, gesamtpreis: int) -> None:
        self.lagerID = lagerID
        self.materialID = materialID
        self.material = material
        self.anzahl = anzahl
        self.gesamtpreis = gesamtpreis



base.metadata.create_all(conn)
    