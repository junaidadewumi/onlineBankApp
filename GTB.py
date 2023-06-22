import time
import random
import sys
import mysql.connector as connection
myconn = connection.connect(host = "127.0.0.1", user = "root", passwd = "@Arikeade2408", database = "ONLINE_BANKING_SYSTEM")
cursor = myconn.cursor()

def GTBplc():
    print(f"Welcome to Guaranty Trust Bank (GTB Plc).")
    time.sleep(2)
    print(f""""
    which of the operation would you like to perform?
    1. Register an account
    2. Log into an account
    3. Home """)
    user = input(">>> ")
    if user == "1":
        Registration()
    elif user == "2":
        log_in()
    elif user == "3":
        from Banking import OBS
        OBS()
    else:
        print(f"Invalid input. Try Again!!!")
        GTBplc()

def Registration():
    val = []
    acc_info = ("First_name", "middle_name", "Last_name", "Email", "BVN", "Account_Number", "'Pswd", "Confirm_pswd",
                "Address")
    querry = ("""INSERT INTO gtbbank(First_name, Middle_name, Last_name, Email, BVN, Account_Number, Pswd, Confirm_pswd,
        Address, Balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""")
    BVN = random.randint(12345678901, 12345678920)
    ACC_NUM = random.randint(4496787004, 4496789004)
    for details in range(9):
        if acc_info[details]=="BVN":
            customer = BVN
        elif acc_info[details]=="Account_Number":
            customer = ACC_NUM
        else:
            customer = input(f"Dear,customer. Kindly enter your {acc_info[details]}: ")
        val.append(customer)
    balance = 0
    val.append(balance)
    print(val)
    cursor.execute(querry,val)
    myconn.commit()
    print(f"Dear customer, your account number and bvn has been generated")
    time.sleep(2)
    print(f"this is your account number {ACC_NUM} ,and your bvn is {BVN} ")
    time.sleep(1)
    print("Enter 1 to log in and 2 to go back home")
    cus = input(">> ")
    if cus == "1":
        log_in()
    elif cus == "2":
        GTBplc()
    else:
        print(f"Invalid input. Try Again!!!")

def checkpassword():
    global password
    global confirm_password
    print(f"Enter your password")
    password = int(input(">>> "))
    if password == password:
        return
    else:
        print(f"Invalid password! Try Again")
        checkpassword()

    print(f"Confirm your password")
    confirm_password = int(input(">>> "))
    if confirm_password == confirm_password:
        return
    else:
        print(f"confirm password unmatch password! Retry!")
        checkpassword()

def checknumber():
    global number
    global  MTN, GLO, AIRTEL, ETISALAT
    MTN = ("0803", "0806", "0703", "0706", "07025", "07026", "0704", "0813", "0816", "0810", "0814", "0903", "0906", "0913", "0916")
    GLO = ("0805", "0807", "0705", "0815", "0811", "0905", "0915")
    AIRTEL = ("0802", "0808", "0708", "0812", "0701", "0902", "0901", "0904", "0907", "0912")
    ETISALAT = ("0809", "0818", "0817", "0909", "0908")
    loyal_cus = input("Enter your number: ")
    if loyal_cus.startswith(MTN):
        print(f"MTN")    
    elif loyal_cus.startswith(GLO):
        print(f"GLO")
    elif loyal_cus.startswith(AIRTEL):
        print(f"AIRTEL")
    elif loyal_cus.startswith(ETISALAT):
        print(f"ETISALAT")
    else:
        print(f"Invalid input! Retry!")

def log_in():
    global password
    global username
    username = input("enter your email: ")
    time.sleep(2)
    password = input("enter your password: ")
    val = (username, password)
    querry = "select * from gtbbank where Email = %s and Pswd = %s"
    cursor.execute(querry, val)
    result = cursor.fetchone()
    if result:
        time.sleep(1)
        print("you have successfully log in ")
    else:
        print("invalid input, try to log in again ")
        log_in()
        time.sleep(2)
    print("""Dear Esteem Cuctomer, which of the transaction would you like to perform?
    1. Transfer to GTB
    2. Transfer - Firstbank
    3. Airtime
    4. Home
    """)
    decision = input(">>> ")
    if decision == "1":
        Transfer_gtb()
    elif decision == "2":
        Transfer_fbn()
    elif decision == "3":
        Airtime_purchase()
    elif decision == "4":
        from Banking import OBS
        OBS()
    else:
        print("You seems to have entered wrong code, Retry!")

def Transfer_gtb():
    transact = int(input("enter beneficiary account number: "))
    val = (transact, )
    querry = "select * from gtbbank where Account_Number = %s"
    cursor.execute(querry, val)
    result = cursor.fetchone()
    print(result)
    if result:
        amount = int(input("Enter amount to transfer "))
        newbalance = result[10] - amount
        val = (newbalance, transact)
        querry = "update GTB set balance =%s where Account_number =%s"
        cursor.execute(querry, val)
        myconn.commit()
        time.sleep(1)
        print("please wait, your transaction is processing...")
        time.sleep(2)
        print(f"You have succesfully transfer {amount} into the beneficiary account. Thanks for banking with us")
    else:
        print("Invalid input! Try again!")
        Transfer_gtb()

def Transfer_fbn():
    trf = int(input("enter beneficiary account number: "))
    val = (trf, )
    querry = "select * from FBN where Account_Number = %s"
    cursor.execute(querry, val)
    result = cursor.fetchone()
    print(result)
    if result:
        amount = int(input("enter amount to transfer: "))
        newbal = result[10] - amount
        charges = 20
        new = newbal - charges
        val = (new, username, password)
        querry = "update gtbbank set Balance = %s where Email = %s and Pswd = %s"
        cursor.execute(querry, val)
        myconn.commit()
        fbnbal = result[10] + amount
        val2 = (fbnbal, trf)
        querry2 = "update FBN set Balance = %s where Account_Number = %s"
        cursor.execute(querry2, val2)
        myconn.commit()
        time.sleep(1)
        print("please wait, your transaction is processing...")
        time.sleep(2)
        print(f"You have succesfully transfer {amount} into the beneficiary account. Thanks for banking with us")
    else:
        print("Invalid input! Try again!")
        Transfer_fbn()

def Airtime_purchase():
    num = input("Enter the phone number to perform the transaction: ")
    MTN = ("0803", "0806", "0703", "0706", "07025", "07026", "0704", "0813", "0816", "0810", "0814", "0903", "0906", "0913", "0916")
    GLO = ("0805", "0807", "0705", "0815", "0811", "0905", "0915")
    AIRTEL = ("0802", "0808", "0708", "0812", "0701", "0902", "0901", "0904", "0907", "0912")
    ETISALAT = ("0809", "0818", "0817", "0909", "0908")
    if num.startswith(MTN):
        print(f"MTN")
    elif num.startswith(GLO):
        print(f"GLO")
    elif num.startswith(AIRTEL):
        print(f"AIRTEL")
    elif num.startswith(ETISALAT):
        print(f"ETISALAT")
    else:
        print("Invalid phone number! Retry!")
        Airtime_purchase()
    amount = int(input("Enter the amount to credit the beneficiary number: "))
    querry = "select * from gtbbank where Email = %s"
    val = (username, )
    cursor.execute (querry, val)
    result = cursor.fetchone()
    newbal = result[10] - amount
    new_querry = "UPDATE gtbbank SET Balance = %s WHERE Pswd = %s"
    val2 = (newbal, password)
    cursor.execute(new_querry, val2)
    myconn.commit()
    time.sleep(1)
    print("please wait, your purchase is processing...")
    time.sleep(2)
    print(f"You have successfuly credit the beneciary phone number with {amount}.")