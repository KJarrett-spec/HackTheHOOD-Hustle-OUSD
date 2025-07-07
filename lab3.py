#1 Lab 3

# Task 1: Working with Strings
food = "ackee and saltfish"
print(food[-3:])
first_last = food[0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_foods = ' '.join(food_list)
print(joined_foods)

# Task 2: Working with Lists
number_list = [16, 3876, -5, 0, -6543]
number_list.append(789)
print(number_list)
number_list.insert(3, -765)
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(number_list[1])
print(number_list)
print(number_list[:3])
print(number_list[-3:])

#Task 3: Working with Dictionaries
books = {'Victor Stafford Reid': 'The Young Warriors', 'Claude McKay': 'Banana Bottom', 'C. Everard Palmer': 'The Lionheart Gal', 'Roger Mais': 'Brother'}
print(books.keys())
print(books.values())
print(books.get('Victor Stafford Reid'))
(books.pop('C. Everard Palmer'))
print(books)
del books['Victor Stafford Reid']
print(books)