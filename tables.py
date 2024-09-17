from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()
engine=create_engine("sqlite:///Vaccinations.db")

Session=sessionmaker(bind=engine)
session=Session()
##Owner class
class Owner(Base):
    __tablename__='owners'
    OwnerID=Column(Integer,primary_key=True,autoincrement=True)
    OwnerName=Column(String(24))
    ContactNumber=Column(String(18))
    Email=Column(String(24))

    def __init__(self,owner_name,contact_number,email):
        self.owner_name=owner_name
        self.contact_number=contact_number
        self.email=email


##Pet class
class Pet(Base):

    __tablename__="pets"
    PetID=Column(Integer,primary_key=True,autoincrement=True)
    PetName=Column(String(12))
    PetType=Column(String(12))
    PetAge=Column(Integer)
    OwnerID=Column(ForeignKey("owners.OwnerID") )
    VaccineID=Column(ForeignKey("vaccines.VaccineID"))

    def __init__(self,pet_name,pet_type,pet_age,pet_owner_id):
        self.pet_name=pet_name
        self.pet_type=pet_type
        self.pet_age=pet_age
        self.pet_owner_id=pet_owner_id
   
class Vaccine(Base):
    __tablename__='vaccines'
    VaccineID=Column(Integer,primary_key=True,autoincrement=True)
    VaccineName=Column(String(24))
    VaccinationDate=Column(String(24))
    PetID=Column(Integer,ForeignKey("pets.PetID"),nullable=False)

    def __init__(self,vaccine_name,vaccination_date,pet_id):
        self.vaccine_name=vaccine_name
        self.vaccination_date=vaccination_date
        self.pet_id=pet_id


Base.metadata.create_all(bind=engine)


