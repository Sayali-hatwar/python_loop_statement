user_age = input("Enter your age : ")
valid_user_age = int(user_age)
#print(f"User_age = {valid_user_age}, type of user_age = {type(valid_user_age)}")
print(f"User_age = {valid_user_age}")



if valid_user_age < 10:
     print("Child")
elif valid_user_age < 18:
     print("Teenager")
elif valid_user_age < 35:
     print("Adult")
elif valid_user_age < 60:
     print("Senior")
else:
     print("Supersenior")


user_data = [
{
    'username':'user1',
    'user_age':23 
},
{
     'username':'user2',
     'user_age':34
},
{
     'username':'user3',
     'user_age':98
}
]

for user in user_data:
     print('user',user.get('user_age'))
     userAge = user.get('user_age')
     if userAge <= 10:
          print(f'user {userAge}')


 
