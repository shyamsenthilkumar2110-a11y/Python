user_name=str(input("Enter your user name : "))
user_age=int(input("Enter your user age : "))
if(user_age>=18):
    print(f"Dear {user_name} congrigulation you are adult..")
else:
    print(f"Dear {user_name} sorry you are not adult..")

# print number from 1 to age
count=1
user_array =[]
while count<=user_age:
     user_array.append(count)
     count+=1
print("the number from 1 to age is : ",user_array)