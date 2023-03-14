def print_items(n):
    for i in range(n):
        print(i)

# print_items(10)

# This is O(n) since it is proportional

def print_items(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)

# print_items(10)

# This is still O(n) because of dropping the constant.

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

# print_items(10)

# This is O(n^2) since we have 100 output with 10 input value

def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)

# print_items(10)

# This is still O(N^2), it does not matter if it is n^3 or n^4 we just simplify it as O(N^2)

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(k)