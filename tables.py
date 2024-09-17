from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()
engine=create_engine("sqlite:///Vaccinations.db",echo=True)


##Owner class
class Owner(Base):
    __tablename__='owners'
    OwnerID=Column(Integer,primary_key=True,autoincrement=True)
    OwnerName=Column(String(24))
    ContactNumber=Column(String(18))
    Email=Column(String(24))
    PetID=Column(Integer,ForeignKey("pets.PetID"),nullable=True)

    def __init__(self,owner_name,contact_number,email):
        self.OwnerName=owner_name
        self.ContactNumber=contact_number
        self.Email=email


##Pet class
class Pet(Base):

    __tablename__="pets"
    PetID=Column(Integer,primary_key=True,autoincrement=True)
    PetName=Column(String(12))
    PetType=Column(String(12))
    PetAge=Column(Integer)
    OwnerID=Column(Integer,ForeignKey("owners.OwnerID") )
    VaccineID=Column(Integer,ForeignKey("vaccines.VaccineID"))

    def __init__(self,pet_name,pet_type,pet_age,pet_owner_id,vaccine_id):
        self.PetName=pet_name
        self.PetType=pet_type
        self.PetAge=pet_age
        self.OwnerID=pet_owner_id
        self.VaccineID=vaccine_id

   
class Vaccine(Base):
    __tablename__='vaccines'
    VaccineID=Column(Integer,primary_key=True,autoincrement=True)
    VaccineName=Column(String(24),nullable=False)
    

    def __init__(self,vaccine_name):
        self.VaccineName=vaccine_name
       


Base.metadata.create_all(bind=engine)


