#first exercise 

bill = float(input(print("Enter amount of bill: ")))
people = int(input(print("Enter amount of people: ")))
tips = int(input(print("Enter percentage of tips: ")))

tips_per_person = (bill * (tips/100)) /people
per_person = (bill/people)+tips_per_person

print(f"Tip amount per person ${tips_per_person: .2f}" )
print(f"Total amount per person ${per_person: .2f}" )

#second exercise

number = int(input(print("Enter a number: ")))

if number == 2 or number == 3 or number == 5 or number == 7 or number == 11:
    print("The number " + str(number) + " is a prime number" )
elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0:
    print("The number "  + str(number) + " is not a prime number")
else:
    print("The number " + str(number) + " is a prime number" )


#third exercise

how_many = eval(input(print("Enter the number of seconds: ")))

hour = how_many // 3600
minutes = (how_many // 60) %60
seconds = how_many % 60

print(f"Result: {hour}:{minutes}:{seconds}")

