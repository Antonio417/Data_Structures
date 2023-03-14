def print_items(n):
    for i in range(n):
        print(i)

print_items(10)

# This is O(n) since it is proportional

def print_items(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)

print_items(10)

# This is still O(n) because of dropping the constant.