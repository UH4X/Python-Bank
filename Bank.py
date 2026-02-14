import os, random, time


account = {
    "test": {"password": "123", "Money": 5000, "Admin": False},
    "admin": {"password": "ADMIN666", "Money": 0, "Admin": True},
    "bo": {"password": "MyNameIsBo", "Money": 5000, "Admin": False},
    "idk": {"password": "1234", "Money": 30000, "Admin": False}
}

logged_in = False
account_selected = False



# Login Parameter: You login here
def login():
    global logged_in
    if logged_in == True:
        print("You are already logged in")
        return user_control()
    print("""
    #############################
    # WELCOME TO THE LOGIN PAGE #
    #############################
          """)
    print("Case Sensitive!")
    global account_selected
    while True:
        username = input("Enter Username: ").lower()
        if username in account:
            account_selected = username
            break
        elif username in ["exit", "cancel"]:
            return user_control()
        else:
            print("User does not exist! Try Again!")
    
    incorrect_counter = 0 # Incorrect counter

    while True:
        if incorrect_counter == 3:
            os.system("cls")
            print("Too many wrong attempts!")
            incorrect_counter = 0
            return login()
        if incorrect_counter < 1:
            os.system("cls")
            print(f"Username: {username}")
            password = input(("password: "))
        if incorrect_counter >= 1:
            os.system("cls")
            print(f"Incorrect Counter: {incorrect_counter}")
            print(f"Username: {username}")
            password = input(("password: "))


        if password == account[account_selected]["password"]:
            os.system("cls")
            print("Password Correct!")
            time.sleep(1.2)
            os.system("cls")
            print("You are now logged in!")
            logged_in = True
            break
        else:
            print("Incorrect!")
            incorrect_counter +=1
            os.system("cls")



# Status - Check your status
def status():
    if logged_in == False:
        print(f"""Account status:
        Name: Account not logged in!
        Balance: N/A
        Logged in?: {logged_in}""")
    else:
        print(f"""Account status:
    Name: {account_selected.capitalize()}
    Balance: {account[account_selected]['Money']}
    Logged in?: {logged_in}
""")
    
def plus_money():
    random_plus_money = random.randint(50, 250)
    account[account_selected]["Money"] = account[account_selected]["Money"] + random_plus_money
    print(f"Added Funds: {random_plus_money} to your balance!")
    print(f"New balance: {account[account_selected]["Money"]}")

def negate_money():
    random_plus_money = random.randint(1, 250)
    account[account_selected]["Money"] = account[account_selected]["Money"] - random_plus_money
    print(f"Negated Funds: {random_plus_money} to your balance!")
    print(f"New balance: {account[account_selected]["Money"]}")

def welcome():
    os.system("cls")
    print("""
    #######################
    # WELCOME TO THE BANK #
    #######################
          
          Pro tip!
            - If you need help, just type "Help"!
""")
    
def help():
    print("""
    ###########################
    # WELCOME TO HELP SECTION #
    ###########################
          
          Available commands:
          --------------------------------------------------
          1. "Status" - Check.
          2. "Money+" or "m+" - Adds random positive funds! (LOGIN REQUIRED)
          3. "Money-" or "m-" - Adds random negative funds! (LOGIN REQUIRED)
          4. "Roulette" or "rl" - Like Russian Roulette! (LOGIN REQUIRED)
          5. "Coin" or "cf" - Do a coinflip
          5. "Login" - Log into an account.
          6. "Logout" or "Log out" - Logs you out of your account. (LOGIN REQUIRED)
          
""")


def logged_in_checker():
    if logged_in == False:
        print("ERROR: You are not logged in!")
        return user_control()
    else:
        if logged_in == True:
            pass

def logged_out():
    logged_in_checker()
    global logged_in
    logged_in = False
    print("You logged out!")

def roulette():
    logged_in_checker()
    print("""
Welcome to Russian Roulette!
Except here you do not die;)

          Game rules:
            1. Bet your money!
            2. A Random number will be chosen
            3. Guess the number (1-6) 
            4. You win? Triple the money bet back!
            5. You lose? All betted money lost!
""")
    random_roulette_number = random.randint(1, 6)
    while True:
        try:
            bet = int(input("Money Bet: "))
            if bet > account[account_selected]['Money']:
                print("You cannot withdraw more than your account has!")
                continue
            if bet <= 0:
                print("You cannot withdraw a negative amount!")
                continue
            roulette_bet = int(input("Roulette bet (1-6): "))
            if roulette_bet > 6:
                print("You cannot exceed max 6!")
                continue 
            if roulette_bet <= 0:
                print("You cannot bet outside the given range (1-6)!")
                continue
            break
        except ValueError:
            print("ERROR: You can only write numbers!")
            returnal = input("Do you wish to resume? (Y/n):").lower()
            if returnal in ["y", "yes"]:
                pass
            else:
                os.system("cls")
                return user_control
        
    
    roulette_sleeper = 0.25
    os.system("cls")
    print("\nRolling!")
    time.sleep(0.35)
    os.system("cls")
    print(".")
    time.sleep(roulette_sleeper)
    os.system("cls")
    print("..")
    time.sleep(roulette_sleeper)
    os.system("cls")
    print("...")
    time.sleep(roulette_sleeper)
    os.system("cls")
    print(".")
    time.sleep(roulette_sleeper)
    os.system("cls")
    print("..")
    time.sleep(roulette_sleeper)
    os.system("cls")
    print("...")
    time.sleep(roulette_sleeper)
    os.system("cls")
    print(".")
    time.sleep(roulette_sleeper)
    os.system("cls")
    print("..")
    time.sleep(roulette_sleeper)
    os.system("cls")
    print("...")
    time.sleep(1)
    os.system("cls")
    print(f"IT LANDED ON {random_roulette_number}\n")
    
    
    print(f"Your Money Bet: {bet}")
    print(f"Roulette Number Guess: {roulette_bet}\n")


    if roulette_bet == random_roulette_number:
        print("YOU JUST WON!!")
        print(f"Balance before bet: {account[account_selected]['Money']}")
        added_roulette_bet = bet * 3
        account[account_selected]['Money'] += added_roulette_bet
        print(f"Won: {added_roulette_bet}\n")
        print(f"New Balance: {account[account_selected]['Money']}\n")
    else:
        print(f"Money lost: {bet}")
        print(f"Balance before: {account[account_selected]['Money']}\n")
        account[account_selected]['Money'] -= bet
        print(f"New Balance: {account[account_selected]['Money']}")



def coin_flip_game():
    os.system("cls")
    user_error_input_counter = 0
    user_input_counter = 0
    print("Flat or Crown?")
    print("""
Try to see how much you can win! 50% chance of winning!
          To bet money type "bet". (LOGIN REQUIRED)

          A win = x1.75 back!
          A Loss = Bet Money Lost""")
    print("")
    os.system("pause")
    os.system("cls")
    bet = 0
    while True:
        try:
            

            coin_flip = random.randint(1, 2)
            if coin_flip == 1:
                coin_flip = "flat"
            if coin_flip == 2:
                coin_flip = "crown"
            user_coin = input("(F/C): ").lower()

            if user_coin in ["flat", "f"]:
                user_coin = "flat"
                

            if user_coin in ["crown", "c"]:
                user_coin = "crown"

            if user_coin not in ["crown", "c", "flat", "f", "bet"]:
                print("Error")
                user_error_input_counter += 1
                if user_error_input_counter >= 3:
                    time.sleep(0.8)
                    os.system("cls")
                    user_error_input_counter = 0
                continue

            if user_coin == "bet":
                logged_in_checker()
                os.system("cls")
                while True:
                    try:
                        print("How much do you wish to bet a coin?")
                        print(f"Your current balance: {account[account_selected]['Money']}")
                        new_bet = int(input("Bet: "))
                        
                        if new_bet > account[account_selected]["Money"]:
                            os.system("cls")
                            print("You cannot withdraw more than your account has!")
                            continue

                        if new_bet < 0:
                            os.system("cls")
                            print("Bet cannot be negative!")
                            continue

                        bet = new_bet
                        break
                    except ValueError:
                        os.system("cls")
                        print("Please enter correct value!")
                    except KeyboardInterrupt:
                        os.system("cls")
                        print("Returning!")
                        time.sleep(1.25)
                        return coin_flip_game()

            # FIKS FEJLEN - VIRKER IKKE MENS MAN IKKE ER LOGGET IND!
            # if bet > account[account_selected]["Money"]:
            #     print("INSUFICCIENT FUNDS!")
            #     bet = 0
            #     continue



            if user_coin == coin_flip:
                if bet > 0:
                    print("YOU WON!")
                    account[account_selected]['Money'] += bet * 0.75
                    print(f"New Balance: {account[account_selected]['Money']}")
                elif not bet:
                    print("YOU WON!")

                
            if user_coin != coin_flip:
                if bet > 0:
                    print("You lost!")
                    print(f"Money bet: {bet}")
                    account[account_selected]['Money'] = account[account_selected]['Money'] - bet
                    print(f"New Balance: {account[account_selected]['Money']}")
                elif not bet:
                    print("You lost!")

            user_input_counter += 1
            if user_input_counter >= 3:
                time.sleep(0.8)
                os.system("cls")
                user_input_counter = 0

            print() # Seperate lines
            
        except ValueError:
            print("Unknown value")
        except KeyboardInterrupt:
            print("\n\nDo you wish to exit?")
            user_exit = input("(Y/n): ").lower()
            if user_exit in ["yes", "y"]:
                os.system("cls")
                return user_control()
            elif user_exit in ["no", "n"]:
                pass





def user_control():
    while True:
        try:
            user = input("CMD: ").lower()
            os.system("cls")

            if user == "status":
                status()

            elif user == "login":
                login()

            elif user in ["logout", "log out"]:
                logged_out()

            elif user in ["money+", "m+"]:
                logged_in_checker()
                plus_money()

            elif user in ["money-", "m-"]:
                logged_in_checker()
                negate_money()

            elif user == "help":
                help()

            elif user in ["roulette", "rl"]:
                roulette()

            elif user in ["flip", "coin", "coin flip", "cf"]:
                coin_flip_game()
            
            else:
                print("Command unknown!")


        except KeyboardInterrupt:
            print("Error - You interrupted the process!")
            exit()




###########################################################################################
# ---------------------------------- RUNNING CODE --------------------------------------- #
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV #
###########################################################################################


os.system("cls")
print ("""
    #######################
    # WELCOME TO THE BANK #
    #######################
       
""")



welcome()
user_control()