from tables import Vaccine,Pet,Owner


while True:
    print("-_"*20)

    selection1=int(input("""
    1->Add pet
    2->Search pet
    3->Update
    0->Exit 
    __"""))
    if selection1==1:
        print("Adding pet..")
    elif selection1==2:
        print("Searching for a pet...")
    elif selection1==3:
        print("updating the system...")
    elif selection1==0:
        print("Exiting...")
        print("Exit successful!")
        exit()
    else:
        print("Invalid entry try again..")

    

p1=Pet("nm","DOg",5)
print(p1.add_pet())

