# @TODO: Write a function that returns the arithmetic average for a list of numbers
l = range(0,25, 2)

def average(a_list):
    total = 0
    for x in a_list:
        total = total + x
    return total / len(a_list)

# Test your function with the following:
print(average(l))
print(average([1, 5, 9]))
print(average(range(11)))
