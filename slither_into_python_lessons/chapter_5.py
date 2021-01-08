#question 1
# fibinocci sequence

num = int(input("How many numbers: "))

n2 = 0
n1 = 1

if num <= 0:
    print("Enter a number greater than 0")
elif num == 1:
    print(n2)
else:
    count = 0
    while count < num:
        print(n2)
        next_num = n1 + n2
        n2 =n1
        n1 = next_num
        count += 1

# question 2

width = int(input("enter width: "))

current_width = 1
while current_width < width:
    print("*" * current_width)
    current_width += 1

while current_width > 0:
    print("*" * current_width)
    current_width -= 1


#question 3

number = int(input("Enter number: "))

check = int(input("enter another number: "))
while check != 0:
    if check < number:
        print("lower")
    else:
        print("higher")
    check = int(input("enter another number: "))

print("Exiting...")