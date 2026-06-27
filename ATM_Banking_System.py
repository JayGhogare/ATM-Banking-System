Pin = 1234
Balance = 5000
attempt = 0
while attempt < 3:
    
    Password = int(input("Enter your Pin: "))

    if Password == Pin:
        print("Access Granted, Welcome!!")
        while True:
            print("========= ATM MENU =========")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")  
            print("4. Exit")
        
            Choice = int(input("Choice the function:"))
        
            if Choice == 1:
                print("Balance = Rs.", Balance)
            
            elif Choice == 2:
                Deposit_amount = int(input("Enter the amount:"))
                print("Rs.", Deposit_amount, "Deposited Succesfully!!")
                Balance += Deposit_amount
                print("Current Balance = Rs.", Balance)
            
            elif Choice == 3:
            
                Withdraw_amount = int(input("Enter the amount:"))
                if Withdraw_amount > Balance:
                    print("Insufficient Balance")
                else:
                    print("Rs.", Withdraw_amount, "Withdraw Succesfully!!")
                    Balance -= Withdraw_amount
                    print("Current Balance = Rs.", Balance)
            elif Choice == 4:
                print("🙏Thankyou! For using our ATM")
                print("Have a nice Day!!")
                break
               
            else:
                print("Invalid Choice")   
        break         
    else:
        attempt = attempt + 1
        print("Wrong Pin (attempt", attempt, "/3)")

if Password != Pin:
    print("Account is Locked after 3 Attempts")
    
        