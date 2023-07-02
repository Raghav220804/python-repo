lucky_numbers = [43, 8, 15, 16, 23, 42] #list
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"] #list
friends.extend(lucky_numbers) #adds both list
print(friends)
friends.append("Creed")#adds creed to the list
print(friends)
friends.insert(1, "Kelly") #replace the index number with the given string
print(friends)
friends.remove("Jim") #removes the object from the list
print(friends)
friends.clear() #clears the list
print(friends)
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"] #created list again
friends.pop() #pops out last element
print(friends)
print(friends.index("Kevin")) #tells the index of the given element
print(friends.count(friends[1])) #tells how many times the given element is present in the list
print(friends.count("Karen"))
friends.sort() #sorts the list in ascending order
print(friends)
lucky_numbers.sort() #sorts the list in ascending order
print(lucky_numbers)
lucky_numbers.reverse() #prints list in reverse order
print(lucky_numbers)
friends2 = friends.copy() #copies the given list to the other list
print(friends2)