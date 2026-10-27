randomThings = ["Mount Everest", "Football", "PS5", "Hand", "Star Platinum"]

# Adding a new element using append()
randomThings.append("Rohitbir")

# Inserting a new element at a position using insert()
randomThings.insert(0, "PC")

# Deleting an item from a list
del randomThings[0]

# Using pop() to remove the last value from the list and reusing it
popped_randomThing = randomThings.pop()
print(f"Last value popped: {popped_randomThing}")

# Using pop(num) to remove a specific value at any position in the list
popped_randomThing = randomThings.pop(1)
print(f"Second value popped: {popped_randomThing}")

# Removing an Item by Value using remove()
randomThings.remove('PS5')

# Sorting a List Permanently alphabetically with the sort() method
randomThings.sort()

# Sorting a List Permanently in reverse-alphabetical order with the sort(reverse=True) method
randomThings.sort(reverse=True)

# Sorting a List Temporarily with the sorted() function
print(sorted(randomThings))

# Printing a list in Reverse Order
randomThings.reverse()

# Finding the Length of the List
len(randomThings)
