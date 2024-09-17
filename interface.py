from tables import Vaccine,Pet,Owner
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("sqlite:///Vaccinations.db")
Session=sessionmaker(bind=engine)
session=Session()

def add_vaccine():
    vaccine_name=input("Vaccine name:")
    vaccine=Vaccine(vaccine_name)
    session.add(vaccine_name)
    session.commit()
    pass

def add_owner():
    owner_name=input("Owner name:")
    contact_number=input("Contact number:")
    email=input("Email:")
    owner=Owner(owner_name,contact_number,email)
    session.add(owner)
    session.commit()
    owner_id=list(session.query(Owner.OwnerID).filter_by(OwnerName=owner_name).first())[0]
    
    # add_pet(owner_id)

def add_pet(owner_id):
    pet_name= input("Pet Name:")
    pet_type=input("Pet type:")
    pet_age=input("Pet age:")
    pet_owner_id=owner_id
    pet_vaccine_id=""


while True:
    print("-_"*20)

    selection1=int(input("""
    1->Add pet
    2->Search pet
    3->Update
    4->Add vaccine
    0->Exit 
    __"""))
    if selection1==1:
        add_owner()
        
        print("Adding pet....")
        print("Pet added successful!")
    elif selection1==2:
        print("Searching for a pet...")
    elif selection1==3:
        print("updating the system...")
    elif selection1==4:
        add_vaccine()
        print("Adding vaccine")
        print("Vaccine added successful!!!")
    elif selection1==0:
        print("Exiting...")
        print("Exit successful!")
        exit()
    else:
        print("Invalid entry try again..")

    

p1=Pet("nm","DOg",5)
print(p1.add_pet())

