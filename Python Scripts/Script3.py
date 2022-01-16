import json
try:
    with open('contacts.json') as json_file:
        contactBook = json.load(json_file)
except:
    contactBook=[]

def addContact():
    try:
        name = str(input("Enter Name of contact : "))
        print("Is "+ name + " has multiple contact ? y/n : ",end='')
        mul = str(input())
        if mul == 'y':
            number = []
            print('How many numbers ' + name + ' have : ',end='')
            contacts = int(input())
            for contact in range(contacts):
                print('Enter Number ' + str(contact+1) + ' : ',end='')
                number.append(str(input()))
        else:
            number = str(input('Enter contact number : '))
        contact_dict = {'name':name,'number':number}
        contactBook.append(contact_dict)
    except:
        print('Somenthing went wrong please try again')

def searchordel(dell = False):
    try:
        if contactBook:
            key = str(input('Search by name or number? : '))
            if dell == True:
                print('Enter ' + key + ' you want to Delete : ',end='')
            else:
                print('Enter ' + key + ' you want to search : ',end='')
            srch_data = str(input())
            for contact in contactBook:
                if str(contact[key]).lower() == str(srch_data).lower():
                    if dell == True:
                        i = contactBook.index(contact)
                        del(contactBook[i])
                    else:
                        print(contact)
                    return 0
            else:
                print('Contact not found!')
        else:
            print('Your Contacts are empty!')
    except:
        print('Somenthing went wrong please try again')




while True:
    print("|------------Menu------------|")
    print('1. Add Contact')
    print('2. Search Contact')
    print('3. Delete Contact')
    print('4. Delete all Contacts')
    print('5. Display all Contacts')
    print('6. Exit')
    print('|----------------------------|')
    choice = str(input('Enter Your Choice : '))
    if choice == '1':
        addContact()
        contactBook = sorted(contactBook, key = lambda i: i['name'])
        print(contactBook)
        print('contact added successfully')
    elif choice == '2':
        searchordel()
    elif choice == '3':
        searchordel(dell=True)
    elif choice == '4':
        if contactBook:
            print('All contacts deleted successfully')
            contactBook = []
        else:
            print('Your Contacts are empty!')
    elif choice == '5':
        if contactBook:
            for contact in contactBook:
                print(contact)
        else:
            print('Your Contacts are empty!')
    elif choice == '6':
        print('Good Bye!!')
        with open("contacts.json", "w") as outfile:
            json.dump(contactBook, outfile,indent=4)
        exit()
    else:
        print('Invalid Choice')
        
        
