# This is O(n) since it is proportional
def print_items(n):
    for i in range(n):
        print(i)

# print_items(10)

# This is still O(n) because of dropping the constant.
def print_items(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)

# print_items(10)

# This is O(n^2) since we have 100 output with 10 input value
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

# print_items(10)

# This is still O(N^2), it does not matter if it is n^3 or n^4 we just simplify it as O(N^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)

# print_items(10)

# This is still O(n^2) and not O(n^2 + n) because we dropped the non-dominant 
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(k)

# print_items(10)

# This is just O(1) and not O(3). O(1) is also referred as constant time
def add_items(n):
    return n+n+n

# This is O(a+b) since the two for loops in the function have different parameters
def print_items(a,b):
    for i in range(a):
        print(a)

    for j in range(b):
        print(b)