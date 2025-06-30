#checking = "yes"

#while checking == "yes":
 #   print("What is your age: ")
    #user_input = input ()
    #if int(user_input) >= 18:
   #     print("Yes you can vote")
    #else:
   #     print ("You can't vote")
  #  print("Would you like to check another age?")
 #   user_input2 = input ( )
#    checking = user_input2


#list1 = [-13,100,0,70,-4]

#for x in list1:
#    if x > 0:
#        print("Value is positive")
#    elif x < 0:

#        print("Value is negative")
#    else:
#        print("Number is zero")

Invintory= ["coal","diamonds" ,"gravel", "Dirt", "iron", "gold"]


for i in Invintory:
    if i == "diamonds":
        print(f"you have hit {i} congragrats!")
        break
    else:
        print(f"you currently have {i}")