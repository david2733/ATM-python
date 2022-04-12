# atm algorithm by David

import os
import time
#HELPERS

# this is the funcion we are going to use to create the bills of each denomination

def bills(value, amount):
    return {'value': value, 'amount': amount}  

# This funcion asks the user for the money he wants to withdraw, and keep asking until the user enter a valid value

def withdrawal():
    input_is_a_number = False
    while input_is_a_number ==False:
        try:
            money = int(input('How much money would you like to withdralw? < '))
            os.system("clear")
            input_is_a_number = True
        except ValueError:
            print("Please try again")

    return money

# this funcion is made to meet the total amount of a list with bills in it

def meet_total_money(list):
    totalxd = 0
    for i in list:
        totalxd = totalxd+(i['amount']*i["value"])
    return totalxd

#function to see if the user wants to make another transaction 
def choice():
    choice = input('Do you want to do another transaction? Y/n ')
    if choice.upper() == 'Y':
        os.system("clear")
        main()
    else:
        time.sleep(0.5)
        print("Ok :)")
        goodbye()
        

        

# functions to say things in a cool way
def goodbye():
    point = " "
    time.sleep(1)
    os.system("clear")
    for i in range(3):
        time.sleep(1)
        os.system("clear")
        print("Thank you for using me :)")
        point += " ."
        print("Goodbye" + point)
    time.sleep(1)
    os.system("cmatrix")

def transaction():
        point = " "
        for i in range(3):
            os.system("clear")
            point += ' .'
            print("Transaction in progress " + point)
            time.sleep(0.5)
        time.sleep(1)
        os.system('clear')

#function to remove the money from the atm completely
def remove_money(atm_list, given_list):


    for  bill in atm_list:
        for a in given_list:
            if bill["value"] == a["value"]:
                bill["amount"] -= a["amount"]
            else:
                continue



#///////////////////////////////////////////////////


# Now we need a list for our ATM machine and put bills in it
ATM = []
# we add the bills to the atm machine
ATM.append(bills(100,4))
ATM.append(bills(50,4))
ATM.append(bills(10, 10))


#Here we start our main function$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def main():
 
    os.system("clear")
    print("//////////v| Welcome to the best ATM machine algorithm ever created |\/////////////\n")
    atm_total = meet_total_money(ATM)
    print(f"The atm has a total amount of {atm_total}$")

    money = withdrawal()
    given = []
    
    # if the money amount is greater than 0 we continue  our program
    if money > 0:
        for bill in ATM:
            
            division = int(money / bill["value"])
            b= bill["amount"] - division
            if b <= 0:
                papeles = bill["amount"]
                
            else:
                papeles =  bill["amount"] - b
            
            if money>0:
                given.append(bills(bill['value'], papeles))
                money = money - (bill['value']*papeles)
                
            else:
                break
                    
            
    if money!=0:
        print("Sorry, i cannot give you that amount at this moment, please try later")
        choice()
    else:
        atm_total = meet_total_money(ATM) - meet_total_money(given) 
        transaction()
        print("Transaction succesful")
        print("---------------------------------------------------------")
        for i in given:    
            amount = i["amount"]
            if amount != 0:
                value = i["value"]
                print(f"Here you have {amount} of {value}$ ")
        
        print("---------------------------------------------------------\n")

        if atm_total == 0:
            print("Wow, you left my ATM without a dime")
            print("Thank you for your transaction")
            input("Press enter to finish")
            goodbye()
         
        else:
            print(f"The total amount of the atm after your transaction is {atm_total}$\n")
            remove_money(ATM, given)
            choice()
            

        
# we run the main function
if __name__ == "__main__":
    main()
