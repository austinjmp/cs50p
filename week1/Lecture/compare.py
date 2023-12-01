x = int(input("What is x? "))
y = int(input("What is y? "))

# # Works but not concise, does not stop when condition met. continues checking. Slow code
# if x < y:
#     print("x < y")
# if x > y:
#     print("x > y")
# if x == y:
#     print("x = y")


# # More concise, stops when answer becomes 'true', Faster code
# if x < y:
#     print("x < y")
# elif x > y:
#     print("x > y")
# # elif x == y: # asks another question logically no other options. Better but can still be optimized
# else: # only asks two questions, logically if the previous are false this must be true. Fastest code, less complex
#     print("x = y")

# using OR
# if x < y or x > y: # can combine two questions
#     print("x not equal to y")
# else:
#     print("x equal to y")

if x != y: # same answer as previous OR section, but more consise.
    print("x not equal to y")
else:
    print("x equal to y")

# if x == y: # same answer as previous section, but reversed.
#     print("x equal to y")
# else:
#     print("x not equal to y")


