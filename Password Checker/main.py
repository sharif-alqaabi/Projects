username = input("Enter your username: ")
password = input("Enter your password: ")
pass_lenght = len(password)

print(f"Hey {username}, your password {"*"*pass_lenght} is {pass_lenght} characters long.")