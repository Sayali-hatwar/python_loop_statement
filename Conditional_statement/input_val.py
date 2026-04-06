user_age = input("Enter your age : ")

print(f"user_age = {user_age}, type of user_age = {type(user_age)}")

valid_user_age = int(user_age)

print(f"user_age = {valid_user_age}, type of user_age = {type(valid_user_age)}")


if valid_user_age < 10:
    print("child")
elif valid_user_age < 20:
    print("Adult")
else:
    print('Old')