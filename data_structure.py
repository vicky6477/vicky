
# Data types
num: int = 1
num: float = 1.0
string: str = "abc"
boolean: bool = True    # True or False, True and False ...

# x = 1
# # cond = True or False
# cond = x < 10
# if cond:
#     pass

# Data Structure

# Sequential container (access by index)
lst: list = []  # mutable
tup: tuple = () # immutable

lst = ['a', 'b', 'c']
# .     0 .  1 .  2
# .     0
#       -3 . -2 . -1 

# non-sequential  
my_set: set = {1,2,3,4}

for i in range(3, 10):
    my_set.add(i)

# key : value pair
my_dict: dict = {'a': 1}


# conatainer

if __name__ == "__main__":
    
    print(lst)