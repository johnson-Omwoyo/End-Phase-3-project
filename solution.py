from sqlalchemy import create_engine,Column,Integer,String,Text,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base=declarative_base()
engine=create_engine("sqlite:///Vaccinations.db")

##Owner class
class Owner(Base):
    __tablename__='owners'
    OwnerID=Column(Integer,primary_key=True)
    OwnerName=Column(String)
    ContactNumber=Column(String)
    Email=Column(String)




##Pet class
class Pet(Base):

    __tablename__="pets"
    PetID=Column(Integer,primary_key=True)
    PetName=Column(String)
    PetType=Column(String)
    PetAge=Column(String)
    OwnerID=Column(ForeignKey("owners.OwnerID") )

    # def __init__(self,home_name,home_id):
    #     self.name_id=home_id
    #     self.home_name=home_name
   
class Vaccine(Base):
    __tablename__='vaccines'
    VaccineID=Column(Integer,primary_key=True)
    VaccineName=Column(String)
    VaccinationDate=Column(String)
    PetID=Column(Integer,ForeignKey("pets.PetID"),nullable=False)

Base.metadata.create_all(bind=engine)

Session=sessionmaker(bind=engine)
session=Session()
