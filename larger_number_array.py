user_array_size=int(input("enter the size of an array : "))
user_array=[]
for x in range(1,user_array_size+1):  #loop to store an values form user
    user_input=int(input(f"enter the number for position {x} in array ; "))
    user_array.append(user_input)

print("largest value(built-in)",max(user_array))  #using inbuilt function

# without using in-built functions
constant_value=user_array[0]
for number in user_array:
    if number > constant_value:
        constant_value = number

print("largest value : ",constant_value)

# sum of N numbera
default_value=0
for number in range(1,user_array_size+1):
    default_value=default_value+number

print("sum(N numbers) : ",default_value)

#sum of array elements without built in function
sum_array=0
for numbers_in_array in user_array:
    sum_array+=numbers_in_array

print("sum : ",sum_array)

# sum of array elements with built in function
print("sum(in-built) : ",sum(user_array))

# even number in array
even_number=0
even_array_number=[]
for even in user_array:
    if(even%2==0):
        even_number+=even
        even_array_number.append(even)

print(f"even numbers: {even_array_number} \n couunt : {even_number}")
     