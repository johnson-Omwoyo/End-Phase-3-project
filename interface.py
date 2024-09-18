from tables import Vaccine,Pet,Owner
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


engine=create_engine("sqlite:///Vaccinations.db")
Session=sessionmaker(bind=engine)
session=Session()


def manage_vaccines():
    while True:
        do_this=int(input("""
              1->Add Vaccine
              2->Remove Vaccine
              3->View availabe vaccines
              """))
        if do_this==1:
            add_vaccine()

def add_vaccine():
    vaccine_name=input("Vaccine name:")
    vaccine=Vaccine(vaccine_name)
    session.add(vaccine)
    session.commit()
    print("Adding vaccine")
    print("Vaccine added successful!!!")
    

def add_owner():
    owner_name=input("Owner name:")
    contact_number=input("Contact number:")
    email=input("Email:")
    owner=Owner(owner_name,contact_number,email)
    session.add(owner)
    session.commit()
    owner=session.query(Owner).filter(Owner.Email==email).first()
    try:
        add_pet(owner)
    except:

        session.rollback()

def add_pet(owner):
    pet_name= input("Pet Name:")
    pet_type=input("Pet type:")
    pet_age=int(input("Pet age:"))
    pet_owner_id=owner.OwnerID
    pet_vaccine_id=choose_vaccine()
    pet=Pet(pet_name,pet_type,pet_age,pet_owner_id,pet_vaccine_id)
    session.add(pet)
    session.commit()
    try:
        set_pet_id(owner.OwnerID)
    except:
        session.rollback()
def set_pet_id(Id):
    pet_id=list(session.query(Pet.PetID).filter_by(OwnerID=Id).first())[0]
    session.query(Owner).filter(Owner.OwnerID==Id).first().PetID=pet_id
    session.commit()
        

def choose_vaccine():
    
    while True:
        
        vaccine_searched=session.query(Vaccine).filter(Vaccine.VaccineName.like(f'%{input("Enter vaccine name:")}%')).all()
        counter=1
        if len(vaccine_searched) >0:
            for x in vaccine_searched:
                print(f'{counter}->{x.VaccineName}')
                counter+=1
            
            vaccine_selected=int(input('_'))
            
            if vaccine_selected > 0 and vaccine_selected<=len(vaccine_searched):
                return vaccine_searched[vaccine_selected-1].VaccineID
               
        else:
            print("Vaccine not found !!")
    
while True:
    print("**_-"*20)

    selection1=int(input("""
    1->Add pet
    2->Search pet
    3->Update
    4->Manage vaccines
    0->Exit 
    __"""))
    if selection1==1:
        try:
            add_owner()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"SQLAlchemy error occurred: {e}")
        
        print("Adding pet....")
        print("Pet added successful!")
    elif selection1==2:
        print("Searching for a pet...")
    elif selection1==3:
        print("updating the system...")
    elif selection1==4:
        manage_vaccines()
    
    elif selection1==0:
        print("Exiting...")
        print("Exit successful!")
        
        exit()
    else:
        print("Invalid entry try again..")

    


