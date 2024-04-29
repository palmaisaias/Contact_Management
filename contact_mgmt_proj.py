import re   #---for regex
import os   #---only used it for 'clear' but super helpful
import colorama #--- you already knowww
from colorama import Back, Fore, Style
colorama.init
colorama.init(autoreset=True)

def read_cont():    #---takes txt. file and puts it back together using regex. Allows for real time interaction with the txt file.
    contacts = {}
    try:
        with open('contact_list.txt', 'r') as file:
            for line in file:   #---loops through every line in the local file
                line = line.strip() #--- strips line in order to deal with '\n' that is implemented when writing the txt file in write_con()
                if line:    #---checks if there is information to begin with
                    data = re.search(r'(^[A-Za-z-0-9]+[\._]?[A-Za-z-0-9]+[@]\w+[.]\w{2,3})::([\w\s]+)::(\d{10}|\d{3}-\d{3}-\d{4}|\d{3} \d{3} \d{4})::(.*)', line.strip())
                    #--- REGEX pattern notes: GROUP 1. Reused the already functioning 'email_validate' regex. GROUP 2. 'Name' allows word characters and
                    #--- white space. '+' allows one or more of both. GROUP 3. 'Phone' allows 3 kinds of phone number formats. Allows 1234567890 OR '|' 
                    #--- 123-456-7890 OR '|' 123 456 7890. GROUP 4. 'Notes' Used wildcard '.' since I wanted to allow liberal entries in this section for the user.
                    #--- '*' allows for 0 or more occurances which accomodates the fact that this 'Notes" section might be empty in the txt file
                    #--- since it is an optional area for the user.  
                    if data:
                        #---uses .group to take the filtered 'groups' from regex and allows us to call them individually
                        email = data.group(1)
                        contacts[email] = {'Name': data.group(2), 'Phone': data.group(3), 'Notes': data.group(4)}
    except FileNotFoundError:
        print(Style.DIM + Fore.LIGHTRED_EX + 'no local files')
    else:
        print()
        print(Style.DIM + Fore.LIGHTGREEN_EX + 'importing local data...')
        return contacts

def write_con(contacts):    #---writes and re-writes the txt file. Incorporated throughout in order to update txt file in real time and automatically
    with open('contact_list.txt', 'w') as file: #---walked Joshua and Aj through this one so our 'write' functions may look similar         
        for email, info in contacts.items():    
            #---calls on 'contacts' which we've fed in to the fuction.
            #---email = the main key
            #---info = the value, containing another dictionary      
            file.write(f"{email}::{info['Name']}::{info['Phone']}::{info.get('Notes', '')}\n")#--- .get() allows me to have the option of an empty key. In this case 'Notes' since
            #---it is optional for the user. In case there is not notes, I have it returning an empty string

def email_validate(unique_id):
    regex_filter = (r'^[A-Za-z-0-9]+[\._]?[A-Za-z-0-9]+[@]\w+[.]\w{2,3}$')
    #---Breakdown of regex. '^' starting anchor so that regex knows what to expect at the begining. FIRST character set allows upper or lowercase letters, allows numbers as well.
    #---'+' following is to state/allow ONE or more occurances of either letters or numbers. SECOND character set allows for a few random characters '\._' followed by a '?' which
    #---makes those optional. In the case that they ARE found, the THIRD character set then allows and expects one or more letter or number character. Im thinking this might be risky
    #--- because it DOES allow common username format BUT if a user decides to have an email (e.g. isaias.@email.com) this filter would reject it since there are no numbers or letters  
    #---following the period. Might take it out all together. FOURTH character set simply expects/requires the '@' symbol. Immediately after is '\w' which expects/allows word characters. 
    #---Adding the '+' expects one or more word characters. FIFTH character set simply expects/requires a '.' Finally the metacharater '\w' allows/expects 2-3 word characters for 
    #---the 'com, org, gov'. at the ending which is anchored as the ending by '$'. I feel that regex is its own language.
    if re.match(regex_filter, unique_id):   #botched the use of 're.match' originally. should note the structure
        return True
    else:
        return False
    
def name_validate(new_name):    #---created this to validate new names when the user decides to edit/update the contact
    regex_filter = (r'([\w\s]+)')
    if re.match(regex_filter, new_name):
        return True
    else:
        return False
    
def phone_validate(new_phone):  #---created to validate phone number when user decides to edit/update
    regex_filter = (r'(\d{10}|\d{3}-\d{3}-\d{4}|\d{3} \d{3} \d{4})')
    if re.match(regex_filter, new_phone):
        return True
    else:
        return False

def note_validate(new_note):    #---created to validate notes when user decides to edit/add/update
    regex_filter = (r'(.*)')
    if re.match(regex_filter, new_note):
        return True
    else:
        return False
    

def add_cont(contacts): #--should allow user to add a contact
    os.system('clear')
    print()
    print('Adding NEW contact:')
    print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
    while True:
        try:    #---running a try/except in order to val the email using the email_validate function
            unique_id = input('Enter Email: ').lower().strip()
            if email_validate(unique_id): #---this is checking if the email passed the regex val and has returned a True
                if unique_id not in contacts:   #---if email is not present, loop breaks and goes on to ask further info
                    break
                else:   #---if it IS found to be in contacts dictionary, Value error raised 
                    raise ValueError(Style.DIM + Fore.LIGHTRED_EX + 'Email already exists in contacts\n')
            else:
                print(Style.DIM + Fore.LIGHTRED_EX + 'Please enter a VALID email address') #---user has not used correct format, aka what we allowed through regex
                print()
        except ValueError as grace:
            print(grace)    #---raised ValueError prints here
            continue
#---Below I structured while loops to validate each entry using the validate functions I created for the editing function. Since only the email is a unique
#---identifier, I didnt build in any try/except to raise errors. Just simple if/else statements. 
    while True:
        name = input('Name: ').title()
        if name_validate(name):
            break
        else:
            print(Style.DIM + Fore.LIGHTRED_EX + 'Please enter a VALID name\n')
    while True:
        phone = input('Phone: ')
        if phone_validate(phone):
            break
        else:
            print(Style.DIM + Fore.LIGHTRED_EX + 'Please enter a VALID phone number\n')
    while True:
        additional = input('Notes: ')
        if note_validate(additional):
            break
        else:
            print(Style.DIM + Fore.LIGHTRED_EX + 'Please enter a VALID note\n')
    print()
    contacts[unique_id] = {'Name': name, 'Phone': phone, 'Notes': additional}   #---adds the information to 'contacts' in the form of a dictionary BY indexing into 'unique_id'
    write_con(contacts)
    os.system('clear')
    print(f'        {Style.BRIGHT + name.title() + Style.RESET_ALL} has been', Style.BRIGHT + Fore.GREEN + 'ADDED','to your contacts')

def edit_cont(contacts):    #--should allow user to edit existing contact
    os.system('clear')
    if contacts:    #---checks if theres anything in contacts list
        print()
        print('Here Is a List Of Your Contacts:')
        print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
        for email, info in contacts.items():    #---printing out the list of contacts becomes super convenient when you need the contact email to start any edits
                print(f'Email:', Style.BRIGHT + email)
                for key in info:
                    print(key + ':', Style.DIM + info[key])
                print()
    else:
                print(Style.DIM + Fore.LIGHTRED_EX + '''                    ____________________
                    You have no contacts
                    ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺''')    
    while True:
        print()
        email = input('Enter the email of the contact youd like to edit OR "back" to return to menu: ').lower().strip()
        if email == 'back':
            os.system('clear')
            break
        elif email in contacts: #---if email entered by user is found in contacts, program flows into the edit of said contact
            os.system('clear')
#--- Built out this menu to allow the user to chose which portion of the contact they would like to edit. Breaking it down, I think, allows for a 
#--- better user experience. ALSO, it allows me to validate each entry with the validate functions. I did raise ValueErrors for all of these
#--- validations which is probably a bit of overkill since I could have done the same if/else that I used in the 'add' function BUT it was good practice.
            while True:
                edit_choice = input(f'''
                    What part of {Style.DIM + email + Style.RESET_ALL} would you like to edit?

                                    1. Email
                                    2. Name
                                    3. Phone
                                    4. Notes
                                    ----> ''')
                print()
                if edit_choice == '1':
                    print(f'The current email is {email}\n')
                    while True:
                        try:
                            new_email = input('What is the new email? ')
                            if email_validate(new_email):
                                if new_email not in contacts:
                                    break
                                else:   #---if it IS found to be in contacts dictionary, Value error raised 
                                    raise ValueError('Email already exists in contact')
                            else:
                                print('Please enter a VALID email address') #---user has not used correct format, aka what we allowed through regex
                        except ValueError as grace:
                            print(grace)
                    contacts[new_email]= contacts.pop(email)    #--- .pop() allows for clean 'swap' of values
                    write_con(contacts)
                    os.system('clear')
                    print('Email has been ' + Style.DIM + Fore.LIGHTCYAN_EX + 'UPDATED')
                    break
                
                elif edit_choice == '2':
                    print(f'The current name is {Style.BRIGHT + contacts[email]['Name'].title()}\n')
                    while True:
                        try:
                            new_name = input('What is the new name? ').title().strip()
                            print()
                            os.system('clear')
                            if name_validate(new_name):
                                break
                            else:
                                raise ValueError('Enter a valid name')
                        except ValueError as grace:
                            print(grace)
                            continue
                    contacts[email]['Name'] = new_name
                    write_con(contacts)
                    print()
                    print(f"'Name' under {Style.DIM + Fore.LIGHTCYAN_EX + email + Style.RESET_ALL} has been updated to {Style.DIM + Fore.LIGHTCYAN_EX + contacts[email]['Name'] + Style.RESET_ALL}")
                    break
                
                elif edit_choice == '3':
                    print(f'The current phone number is {Style.BRIGHT + contacts[email]['Phone']}\n')
                    while True:
                        try:
                            new_phone = input('What is the new phone number? ').strip()
                            print()
                            os.system('clear')
                            if phone_validate(new_phone):
                                break
                            else:
                                raise ValueError('Enter a valid phone number')
                        except ValueError as grace:
                            print(grace)
                            continue
                    contacts[email]['Phone'] = new_phone
                    write_con(contacts)
                    print(f"'Phone' under {Style.DIM + Fore.LIGHTCYAN_EX + email + Style.RESET_ALL} has been updated to {Style.DIM + Fore.LIGHTCYAN_EX + contacts[email]['Phone'] + Style.RESET_ALL}")
                    break

                elif edit_choice == '4':
                    print(f'The current note is {Style.BRIGHT + contacts[email]['Notes']}\n')
                    while True:
                        try:
                            new_note = input('What is the updated note? ').strip()
                            print()
                            os.system('clear')
                            if note_validate(new_note):
                                break
                            else:
                                raise ValueError('Enter a valid note')
                        except ValueError as grace:
                            print(grace)
                            continue
                    contacts[email]['Notes'] = new_note
                    write_con(contacts)
                    print(f"'Notes' under {Style.DIM + Fore.LIGHTCYAN_EX + email + Style.RESET_ALL} has been updated to {Style.DIM + Fore.LIGHTCYAN_EX + contacts[email]['Notes'] + Style.RESET_ALL}")
                    break

                else:
                    os.system('clear')
                    print(Style.BRIGHT + Fore.LIGHTRED_EX + '                         Please enter valid menu option')
        else:
            print()
            print(f'            {Style.BRIGHT + Fore.LIGHTRED_EX + email + Style.RESET_ALL} is not an email in your contacts')
                

def delete_cont(contacts):  #--should allow user to delete contact
    os.system('clear')
    if contacts:
        print()
        print('Here Is a List Of Your Contacts:')
        print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
        for email, info in contacts.items():
                print(f'Email:', Style.BRIGHT + email)
                for key in info:
                    print(key + ':', Style.DIM + info[key])
                print()
    else:
                print(Style.DIM + Fore.LIGHTRED_EX + '''                    ____________________
                    You have no contacts
                    ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺''')            
    while True:
        remove = input('Enter the email of the contact you want to delete OR "back" to return to menu? ').lower().strip()
        print()
        if remove in contacts:
            os.system('clear')
            print(f'            {Style.BRIGHT + remove + Style.RESET_ALL} has been', Style.BRIGHT + Fore.LIGHTRED_EX + 'DELETED', 'from your contact list')
            print()
            del contacts[remove]
        elif remove == 'back':
            os.system('clear')
            break
        else:
            print(Style.DIM + Fore.LIGHTRED_EX + 'Please enter a valid contact email')
            print()    
        write_con(contacts)
        

def search_cont(contacts):  #--should allow user to search for a contact
    os.system('clear')
    while True:
        if not contacts:
            print()
            print(Style.DIM + Fore.LIGHTRED_EX + '''                        ____________________
                        You have no contacts
                        ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺''')
            break    
        print()
        email = input('Enter email of contact youre looking for or "back" to return to menu: ').lower().strip()
        print()
        if email in contacts.keys():    #---checks if the email is in contacts dictionary
            print(f'Email:', Style.BRIGHT + email)
            info = contacts[email]  #---'email' input can now be used as a key to access the remaining values. The value is a nested dictionary.
            for key in info:    #---for every 'key' in this nested dictionary 'info'...
                print(key + ':', Style.DIM + info[key])    #---I print the 'key' (Name, Phone, Notes) along with their corresponding values which are 
            print()                                        #---accessed by info[key]
        elif email == 'back':
            os.system('clear')
            break
        else:
            print(f'                {Style.BRIGHT + Fore.LIGHTRED_EX + email + Style.RESET_ALL} is not an email in your contacts')
            print()
    

def view_all(contacts): #--should allow user to view their complete, current contact list
    os.system('clear')
    if not contacts:
        print()
        print(Style.DIM + Fore.LIGHTRED_EX + '''                    ____________________
                    You have no contacts
                    ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺''')
    else:
        os.system('clear')
        print()
        print('Here Is a List Of Your Contacts:')
        print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
        for email, info in contacts.items():
            print(f'Email:', Style.BRIGHT + email)
            for key in info:
                print(key + ':', Style.DIM + info[key])
            print()
            
def management_system():
    contacts = read_cont()
    while True:
        print()
        print(Fore.LIGHTBLACK_EX + Style.BRIGHT + '             Welcome to the Contact Management System!')
        print('             ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
        choice = input('''
                1. Add a New Contact
                2. Edit an Existing Contact
                3. Delete a Contact
                4. Search For a Contact
                5. View All Contacts
                6. Quit
                   Enter Choice: ''')
        if choice == '1':
            add_cont(contacts)
        elif choice == '2':
            edit_cont(contacts)
        elif choice == '3':
            delete_cont(contacts)
        elif choice == '4':
            search_cont(contacts)
        elif choice == '5':
            view_all(contacts)
        elif choice == '6':
            os.system('clear')
            print()
            print(Style.BRIGHT + Fore.CYAN + '         Thanks for using Contact Management System.')
            print('\n'*4)
            break
        else:
            os.system('clear')
            print()
            print(Style.DIM + Fore.LIGHTRED_EX +'                  Please enter a valid menu option')

management_system()
        