# register
#- username and password 
# -generate user ID(generate user action)

# login
# -account and password


#bank operstions

#initializing a system
import random 
import datetime as dt
current_datetime = dt.datetime.now()
amountAllowed= range(10000000)
currentBalance= range (10000000)
    
database = {
    'Tolu': 'Tolu2020',
    'Fola': 'Fola2021',
    'John': 'John2022'
}

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
            print(register())
        else:
            print('You have selescted an invalid option')
        

    
    


def login():
    print("********Login********")
    user_name = input('What is your name? \n')
    accountNumber = generatedAccountNumber()
    password = input('What is your password? \n')
    if password in database.values():
        bankOperations()
    
    else:
        print('Invalid password')
    



    for accountNumber, userDetails in database.items():
        if(accountNumberFromUser == generatedAccountNumber):
            bankOperations()
        else:
            print('Invalid account or password')
    login()

    bankOperations()

def register():
    print('*********Register*************')
    email = input('What is your email? \n')
    first_name = input('what is your first name?\n')
    last_name = input('what is your last name? \n')
    user_name = input('What is your new username? \n')
    password =input('What is your password? \n')

    accountNumber = generatedAccountNumber()

    database[accountNumber] = [first_name, last_name, password]
    print (generatedAccountNumber())

    print('Your account has been created')
    print('Welcome to T bank \n')
    print (first_name, last_name)

    print('***********Login**************')
    accountNumber =int(input('What is your account number? \n'))
    
    if (accountNumber == generatedAccountNumber):
        bankOperations()
    else:
        print('invalid details')

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
    if(amount in amountAllowed):
        print(currentBalance)
        print('Thank you for banking with T bank')
    else:
        print ('Insufficient funds')
    new_transaction()
        


def depositeOperations():
    depositeAllowed= input('Amount to Deposit \n')
    if( depositeAllowed in currentBalance):
        print (currentBalance)
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

    
    update2 = int(input('Your NIN \n'))
    print('Your information will be verified. Thank you')
    new_transaction

    




def generatedAccountNumber():

    return random.randrange(1111111111,99999999999)

def new_transaction():
    new_transaction = input('Will you like to perform a new transaction? (1) YES (2) NO \n')
    if (new_transaction == 1):
        bankOperations()
    else:
        ('Goodbye')



#### ACTUAL BANKING SYSTEM  #####


init() 

