#booleans
print(10>9)#is this true or false 
#booleans are used to evaluate expressions and conditions in python
#they are used the check if an expression is true or false
broughtfood= True
print(broughtfood)

is_raining = True
if is_raining:
    print("take an umbrella!")
else:
    print("no umbrella needed.")



tempature = 25 
if tempature > 30:
    print(" it's warm")
    print("drink water")
elif tempature > 20 :
    print("it's nice")
else:
    print("it's cold")

print("done")



age=22
if age>= 18:
    message="eligible"
else:
    mesasge= "not elegible"
message="eligible" if age >= 18 else "not eligible"
print(message)