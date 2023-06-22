import time
import sys
import mysql.connector as connection
myconn = connection.connect(host = "127.0.0.1", user = "root", passwd = "@Arikeade2408", database = "ONLINE_BANKING_SYSTEM")
cursor = myconn.cursor()
def OBS():
    print(f"Welcome to Online Banking System!")
    time.sleep(2)
    print(f"""which of the Bank Operation would you like to perform?
        1. Guaranty Trust Bank PLC (GTB)
        2. First Bank Plc (FBN)
        3. Deposit
        4. Exit the system (Exit)""")
    Response = input(">>> ")
    if Response == "1":
        from GTB import GTBplc
        GTBplc()
    elif Response == "2":
        from FIRSTBANK import FBN
        FBN()
    elif Response == "3":
        deposit()
    elif Response == "4":
        sys.exit()
    else:
        print(f" Invalid input. Try again!!!")
        OBS ()

def deposit():
    print("""
    Enter 1 to deposit to GTB
    Enter 2 to deposit to FIRSTBANK""")
    decision = input(">>> ")
    if decision == "1":
        deposit_gtb()
    elif decision == "2":
        deposit_fbn()

def deposit_gtb():
    time.sleep(2)
    acc = int(input("Enter beneficiary account number "))
    val = (acc, )
    querry = "SELECT * FROM gtbbank WHERE Account_Number = %s"
    cursor.execute(querry, val)
    result = cursor.fetchone()
    time.sleep(1)
    print(f"You are sending money to {result[1]} {result[2]} {result[3]}")
    if result:
        amount = int(input("Enter amount to deposit "))
        newbalance = result[10] + amount
        val = (newbalance, acc)
        querry = "update gtbbank set Balance =%s where Account_number =%s"
        cursor.execute(querry, val)
        myconn.commit()
        time.sleep(1)
        print("please wait, your transaction is processing...")
        time.sleep(2)
        print(f"You have succesfully deposit {amount} into the beneficiary account. Thanks for banking with us")
        OBS()    
    else:
        print("Invalid input! Try again!")
        deposit_gtb()

def deposit_fbn():
    time.sleep(2)
    acct = int(input("Enter beneficiary account number "))
    val = (acct, )
    query = "SELECT * FROM FBN WHERE Account_Number = %s"
    cursor.execute(query, val)
    result = cursor.fetchone()
    time.sleep(1)
    print(f'You are sending money to {result[1]} {result[2]} {result[3]}')
    if result:
        amount = int(input("Enter amount to deposit "))
        newbalance = result[10] + amount
        val = (newbalance, acct)
        querry = "update FBN set Balance =%s where Account_number =%s"
        cursor.execute(querry, val)
        time.sleep(1)
        print("please wait, your transaction is processing...")
        time.sleep(2)        
        print(f"You have succesfully deposit {amount} into the beneficiary account. Thanks for banking with us")
        OBS()
    else:
        print("Invalid input! Try again!")
        deposit_fbn()
        print('Junaid')
OBS()