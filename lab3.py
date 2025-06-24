#lab 3 Johnny Diaz
#task 1
food = 'Pepperoni pizza'
print(food[0:5])
print(food[-3:])
first_last = food[0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
print(' '.join(food_list))

#task 2

number_list = [1,2,10,32,58]
number_list.append(69)
print(number_list)
number_list.insert(3,"IAmTotallyANumber")
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(number_list[1])
print(number_list)

print(number_list[0:3])
print(number_list[-3:])

#task 3
books= {"Jeff Kinney":"Diary of a Wimpy Kid", "Kazu Kibuishi":"amulet","Raina Telgemeier":"Smile","Aahz Maruch and Stef Maruch":"Python for Dummies"}
print(books.keys())
print(books.values())
print(books.get("Jeff Kinney"))
books.pop("Raina Telgemeier")
print(books)
del books["Jeff Kinney"]
print(books)
