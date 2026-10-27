
placesToVisit = ['France', 'Italy', 'Greece', 'Australia', 'China']

print(placesToVisit)
print(sorted(placesToVisit))
print("Original:", placesToVisit)

placesToVisit.reverse()
print("Reversed:", placesToVisit)

placesToVisit.reverse()
print("Original from reversed:", placesToVisit)

placesToVisit.sort()
print("True sorted:", placesToVisit)

placesToVisit.sort(reverse=True)
print("Reverse sorted:", placesToVisit)
