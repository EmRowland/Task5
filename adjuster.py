from time import sleep

#cookie make up (recipe)

sugar = 1.5

butter = 1 

flour = 2.75

cookies = 48

while True:

  try:

    # TODO: write code...

    amount = int(input ("Enter amount of cookies you want to produce: \n"))

  except Exception:

    print("please enter a valid number (integer)")

    continue

  else:

    print(f"You want to make {amount} piece of cookies")

    

    sleep(4)

    break

#formal calculation (ratio initials)

shuga = sugar * amount

buta = butter * amount

flo = flour * amount

#finding the ratio of each recipe

total_sugar = shuga / cookies

total_butter = buta / cookies

total_flour = flo / cookies 

print ("calculating number of each recipe")

sleep(3)

print(f"You need {total_sugar} cups of sugar")

sleep(2)

print(f"You need {total_butter} cups of butter")

sleep(2)

print(f"You need {total_flour} cups of flour")

    
