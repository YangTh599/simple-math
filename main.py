# Thayer Yang
# 25 SEP 2024
# Simple Math

#Practice 1

#Assigning variables
num1 = float(input('Enter a number: \n'))
num2 = float(input('Enter another number: \n'))

#Math operators used with the 2 numbers
sum = num1+ num2

difference = num1 + num2

product = num1* num2

quotient = num1 / num2

remainder = num1%num2

#Outputs
print(f'{num1} plus {num2} equals {sum}')
print(f'{num1} minus {num2} equals {difference}')
print(f'{num1} times {num2} equals {product}')
print(f'{num1} divided by {num2} equals {quotient}')
print(f'{num1} mod {num2} equals {remainder}')

# Practice 2
print()

length = float(input('Enter length for a room in ft: \n'))
width = float(input('Enter width for a room in ft: \n'))

area = length*width

print(f'A room thats {length} feet long and {width} feet wide \nhas an area of {area} ft squared')

# Practice 3
print()
#Part 1
text = "I am {0} and I am {1} years old\nMy favorite color is {2}."

name = input("Enter your name: \n")
age = int(input('Enter your age: \n'))
fav_color = input('Eneter your favorite color: \n')

text = text.format(name.capitalize(), age, fav_color.lower())
print(text)

# Part 2
print()

STATE_SALES_TAX = 1.06

price = float(input('Enter price for the item: $'))

grand_total = price*STATE_SALES_TAX

print(f'Your item cost of ${price:.2f} is a total of ${grand_total:.2f} after taxes.')

# Part 3
print()

friends_name = input('Enter your friend\'s name: \n')
friends_school = input("Enter your friend\'s school: \n")

text = 'My friend {0} goes to {1}'.format(friends_name, friends_school)

print(text)