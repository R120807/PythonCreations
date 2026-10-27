dinnerInvites = ['Josh', "Max", "Leo", "Camel", "Hazy", "Dustin"]
print("We can only invite two people for dinner!")

firstRemoved = dinnerInvites.pop()
print(f"Sorry {firstRemoved} we cannot invite you to dinner!")
firstRemoved = dinnerInvites.pop()
print(f"Sorry {firstRemoved} we cannot invite you to dinner!")
firstRemoved = dinnerInvites.pop()
print(f"Sorry {firstRemoved} we cannot invite you to dinner!")
firstRemoved = dinnerInvites.pop()
print(f"Sorry {firstRemoved} we cannot invite you to dinner!")

print(f"{dinnerInvites[0]} and {dinnerInvites[1]} you guys are still invited!")

del dinnerInvites[0]
del dinnerInvites[0]
print(dinnerInvites)