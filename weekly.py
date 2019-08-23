bal = 500
accountUser = input("What is your name?  ") #/ Challenge 1
pinNum = '901'
userChoice = 0
yourPin = 0
# opening while loop
while userChoice != '4':
    print(
        'Hello ' + accountUser + ', please choose one of the following options:\n'
        '1) Check Balance \n'
        '2) Add money to account\n'
        '3) Withdraw money from account\n'
        '4) Quit')
    userChoice = input('What would you like to do?  ')
    # choice '1' balance

    if userChoice == '1':
        print(f'Your current balance is ${bal}')
        # choice '2' add

    elif userChoice == '2':
        addMon = int(input('How much money would you like to add?  '))
        newBal = bal + addMon
        print(f'Your balance is now ${newBal}.')
        # choice '3' withdraw

    elif userChoice == '3':
        while yourPin != pinNum:
            yourPin = input('What is your pin number?  ')
            if yourPin != pinNum:
                print('Try again')
        minMon = int(input("How much would you like to withdraw?  "))
        subBal = bal - minMon
        if subBal < 0:
            print("Insufficient Funds.")
        else:
            print(f' Your new balance is ${subBal}')
#end of the loop
print("Thank you for banking with us!!!")