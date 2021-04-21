import random 
import datetime as dt
current_datetime = dt.datetime.now()
amountAllow= range(100000)
currentBalance= (1000000)
    
database = {
    'Tolu': 'Tolu2020',
    'Fola': 'Fola2021',
    'John': 'John2022',
    '': ''
    
}
database_new = {}
access_passwords = ["Tolu2020","Fola2021",'John2022']
def init():
    isValidOptionSelected = False
    print('Welcome to T Bank')
    print ('Your favourite bank')
    print (current_datetime)


    while isValidOptionSelected == False:
        haveAccount = int(input("Do you have an account with us: 1(YES) 2 (NO) \n"))
        
         
        if(haveAccount== 1):
            isValidOptionSelected =True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected =True
            register()
        else:
            print('You have selescted an invalid option')
        

    
    


def login():
    print("********Login********")
    user_name = input('What is your name? \n')
    accountNumber = generatedAccountNumber()
    password = input('What is your password? \n')
    if password in access_passwords:
        bankOperations()
    else:
        print('Invalid password')
        login()    
def register():
    print('*********Register*************')
    email = input('What is your email? \n')
    first_name = input('what is your first name?\n')
    last_name = input('what is your last name? \n')
    user_name = input('What is your new username? \n')
    password_1 =input('What is your password? \n')
        

    accountNumber = generatedAccountNumber()

    database[accountNumber] = [first_name, last_name, password_1]
    print (generatedAccountNumber())

    print('Your account has been created')
    print('Welcome to T bank \n')
    print (first_name, last_name)
    print("********Login********")
    name = input('What is your name? \n')
    password_2 = input('What is your password? \n')
    if password_2 == password_1:
        bankOperations()
    else:
        register()

def bankOperations():
    print('Welcome')
    selectedOption = int(input('What will you like to do? (1) Deposite (2) Withdrawal (3) Complaints (4) KYC update (5) Logout (6) Exit \n'))
    if(selectedOption == 1):
        depositeOperations()
    elif(selectedOption == 2):
        withdrawalOperation()
    
    elif(selectedOption == 3):
        complaintsOperations()

    elif(selectedOption== 4):
        updateKYC()

        
    elif(selectedOption == 5):
        login()
    elif(selectedOption == 6):
        exit()
    else:
        print('You have selescted an invalid option')
        bankOperations()

        



    

def withdrawalOperation():
    amount= int(input('Amount \n'))
    if(amount > 100):
        print(amount + 'Withdrawn')
        print('Thank you for banking with T bank')
    else:
        print ('Insufficient funds')
    new_transaction()
        


def depositeOperations():
    depositeAllowed= int(input('Amount to Deposit \n'))
    if (depositeAllowed > 100):
        print ('Amount deposited')
        print('Thank you for banking with T bank')
    else:
        print('Amount not allowed please use the bank')
    new_transaction()    



def complaintsOperations():
    compliants= input('What is your complaint ? \n')
    print('Thank you for your feedback')
    new_transaction()

def updateKYC():
    update1= int(input('Your BVN? \n'))
    print('Your information will be verified. Thank you')

    
    update2 = int(input('Your NIN \n'))
    print('Your information will be verified. Thank you')
    new_transaction()

    




def generatedAccountNumber():

    return random.randrange(1111111111,99999999999)

def new_transaction():
    new_transaction = int(input('Will you like to perform a new transaction? (1) YES (2) NO \n'))
    if new_transaction ==1:
        bankOperations()
    else:
        exit()



#### ACTUAL BANKING SYSTEM  #####


init() 
