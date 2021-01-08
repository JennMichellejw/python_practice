print("Let's", "print", "this", "sting!")

oh_its_a_tuple = "Let's", "oh here let me just break this thing really quick", "this", "sting!"
my_string = oh_its_a_tuple[1]

print(len(oh_its_a_tuple))

print(type(oh_its_a_tuple))

print(my_string)
print(my_string[5:9])
print(my_string[2:45])

#exersizes

# question 1

num = int(input("how many decimal places? "))

other_number = 2.7182818284590452353602874713527

print('The number is {:.{}f}'.format(other_number, num))

# question 2

lower_index = int(input("Enter lower index: "))
upper_index = int(input("Enter upper index: "))

string_to_slice = "This is a string."

if lower_index > len(string_to_slice) or upper_index > len(string_to_slice):
    print("Cannot slice string.")
else:
    print(string_to_slice[lower_index: upper_index])


password = input("Please enter a password: ")

contains_digit = 0
contains_upper = 0
contains_lower = 0
contains_special = 0
special = "@$*^"

for char in password:
    if char.isdigit():
        contains_digit = 1

    elif char.islower():
        contains_lower = 1

    elif char.isupper():
        contains_upper = 1

    elif char in special:
        contains_special = 1

score = contains_upper + contains_special + contains_lower + contains_digit

if score >= 3:
    print("Your password is valid and your security score is: " + str(score))
elif score < 3:
    print("your password is not valid and the score is: " + str(score))

# question 4

radius = int(input("Enter radius: "))
inc = int(input("Enter increment: "))
end = int(input("Enter ending radius: "))

max_width = 42

print("{:>10s}{:>16s}{:>16s}".format("Radius", "Area", "Volume"))
print("{:>10s}{:>16s}{:>16s}".format("---------", "---------", "---------"))

i = 0

while i < end:
    area = 4 * 3.14 * radius ** 2
    volume = (4/3) * 3.14 * radius ** 3
    print("{:>10.")
