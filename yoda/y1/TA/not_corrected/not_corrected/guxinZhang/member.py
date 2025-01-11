# this file contains all the functions related to memmbers
# including add new member and member login

from database import Database

def add_member(db:Database):
    print('\nOnline Book Store: New Member Registration\n')
    fname = input('Enter first name:')
    lname = input('Enter last name:')
    address = input('Enter street address:')
    city = input('Enter city:')
    zip = input('Enter zip:')
    phone = input('Enter phone:')
    email = input('Enter email address:')
    password = input('\nPassword:')

    try:
        # first check if email already exists
        check_query = f"""SELECT email FROM members WHERE email = '{email}'"""
        if db.execute_with_fetchall(check_query):
            print('\nThis email is already registered!')
            input('\nPress Enter to continue')
            return False
        
        # if the email doesn't exist, insert it to the member table
        insert_query = f""" INSERT INTO members (fname,lname,address,city,zip,phone,email,password) VALUES('{fname}','{lname}','{address}','{city}','{zip}','{phone}','{email}','{password}'); """
        db.execute_with_commit(insert_query)
        print('You have registered successfully!')
        input('Press Enter to go back to Menu')
        return True
    
    except Exception as e:
        print('ADDING member operation is FAILED!')
        print(e)
        input('Press Enter to continue')
        return False
    

def login_member(db: Database):
    print('\nMember Login\n')
    email = input('Enter email: ')
    password = input('Enter password: ')

    try:
        query = f"""SELECT userid, fname, lname, address, city, zip FROM members WHERE email = '{email}' AND password = '{password}'"""
        result = db.execute_with_fetchall(query)
        
        if result:
            print('\nLogin successful!')
            return result[0]  # return member details for later use, in case to create order, which need member's details
            # and result[0] is tuple
        else:
            print('\nInvalid email or password!')
            input('\nPress Enter to continue')
            return None
            
    except Exception as e:
        print('\nLogin FAILED!')
        print(e)
        input('\nPress Enter to continue')
        return None
