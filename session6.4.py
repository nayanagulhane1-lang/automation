#Create a simple password attempt system like Paytm:
# Allow the user up to 3 tries to enter the correct password using a while loop. Print 'Access Denied'
# if all attempts fail, or 'Welcome' if the correct password is entered.

correct_password = 1234
attempt = 0

while attempt < 3:
    pwd = int(input("Enter your password: "))

    if pwd == correct_password:
        print("Welcome")
        break

    attempt = attempt + 1

else:
    print("Access Denied")