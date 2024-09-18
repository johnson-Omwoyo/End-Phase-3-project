from tables import Vaccine,Pet,Owner
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


engine=create_engine("sqlite:///Vaccinations.db")
Session=sessionmaker(bind=engine)
session=Session()


def manage_vaccines():
    while True:
        do_this=input("""
        1->Add Vaccine
        2->Remove Vaccine
        3->View availabe vaccines
        0->Back
        __""")
        if do_this=="1":
            add_vaccine()
        elif do_this=="2":
            remove_vaccine()
           

        elif do_this=="3":
            available_vaccines()
            
        elif do_this=="0":
            return
        elif do_this=="":
            print("You enterd nothing try again!!")
        else:
            print("Invalid choice, try again!!")
        

def add_vaccine():
    vaccine_name=input("Vaccine name:")
    vaccine=Vaccine(vaccine_name)
    session.add(vaccine)
    session.commit()
    print("Adding vaccine...")
    print("Vaccine added successful!!!")
    
def remove_vaccine():
    available_vaccines=session.query(Vaccine.VaccineName).all()
    counter=1
    for single_vaccine in available_vaccines:
        print(f'{counter}->{single_vaccine[0]}')
    
    remove=int(input("Remove:"))
    remove_name=available_vaccines[remove-1][0]
    session.query(Vaccine).filter_by(VaccineName=remove_name).delete()
    session.commit()
    print (f'Vaccine {remove_name} removed succesfully!')
    # print(available_vaccines)
def available_vaccines():
    available_vaccines=session.query(Vaccine.VaccineName).all()
    counter=1
    for available_vaccine in available_vaccines:
        print(f'{counter}.{list(available_vaccine)[0]}')
        counter+=1


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

def search_pet():
    
    searched_pets=session.query(Pet).filter(Pet.PetName.like(f'%{input("Enter pet name:")}%')).all()
    print(searched_pets)
    counter=1

    for searched_pet in searched_pets:
        print(f'{counter}->{searched_pet.PetName}')
        counter+=1
    select_pet=int(input ("Select pet"))
    selected_pet=searched_pets[select_pet-1]
    manage_pet(selected_pet)

def manage_pet(selected_pet):
    print(selected_pet.Vaccinated)
    while True:
        selected_pet
        edit_pet= input("""
        1->Mark Vaccinated
        2->Drop
        0->Back
        __""")
        if edit_pet=="1":
            selected_pet.Vaccinated=True
            session.commit()
            print("Pet vaccinated")
        elif edit_pet=="2":
            selected_pet.delete()
            session.commit()
            print('Pet removed')
        elif edit_pet=="0":
            return
        else:
            print("Wrong entry")
        
while True:
    print("**_-"*20)

    selection1=input("""
    1->Add pet
    2->Search pet
    3->Manage vaccines
    0->Exit 
    __""")
    if selection1=="1":
        try:
            add_owner()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"SQLAlchemy error occurred: {e}")
        
        print("Adding pet....")
        print("Pet added successful!")
    elif selection1=="2":
        search_pet()
        
    elif selection1=="3":
        manage_vaccines()
    
    elif selection1=="0":
        print("Exiting...")
        print("Exit successful!")
        exit()
    else:
        print("Invalid entry try again..")

    


