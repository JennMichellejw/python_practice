#Hello, World!

print("Hello, fellow Humans!")

#Chapter 3
# question 1 & 2

number_of_rabbits = 11
years = int(input("Enter number of years: "))

months = 12 * years
times_doubled = months // 3

pop_after_months = number_of_rabbits * (2 ** times_doubled)
print(pop_after_months)

# question 3

x = input("Enter value of x: ")
y = input("Enter value of y: ")

swap = x
x = y
y = swap


print("x is: " + x + " y is: " + y)

#Chatper 4
#question 1

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

a1 = a == ((b ** 2) + (c ** 2)) ** 0.5
b1 = b == ((a ** 2) + (c ** 2)) ** 0.5
c1 = c == ((a ** 2) + (b ** 2)) ** 0.5

if a1 or b1 or c1:
    print("This will make a right triangle")
else:
    print("This triangle is wrong")


# question 2 fizzbuzz

number = int(input("Enter number: "))

if number % 3 == 0 and number % 5 == 0:
    print("fizz-buzz")
elif number % 3 == 0:
    print("fizz")
elif number % 5 == 0:
    print("buzz")
else:
    print(number)


