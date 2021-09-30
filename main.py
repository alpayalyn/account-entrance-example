token = 3

account_id = "alpay"
account_password = "123456"

while True:

    ID = str(input("Could you please enter an ID:"))
    password = str(input("Could you please enter a password:"))

    if(ID != account_id and password == account_password ):
        print("You entered wrong ID")
        token -= 1

    elif(ID != account_id and password == account_password ):
        print("You entered wrong password")
        token -= 1

    elif(ID != account_id and password != account_password ):
        print("You entered wrong ID and password")
        token -= 1

    else:

        print("You entered to the system successfully.")
        break

    if(token == 0):

        print("You can no longer enter to the system.")
        break
