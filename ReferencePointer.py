# Arguments are passed by assignment in Python
# https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
# https://stackoverflow.com/questions/534375/passing-values-in-python
# Part I
a=1 # In Python, a is a reference to integer object 1.
    # In C, a is a memory location that stores the value 1.
b=2
# print('a=1,b=2')
# print('id(a)=',id(a)) # id(a): identity of the location of the object 1 in memory
# print('id(1)=',id(1))
# print('id(b)=',id(b))
# print('id(2)=',id(2))

c=b # c points to the object 2.
print('c=',c)
b=3
print('c=',c) 

# Part II
# Why did changing list ‘y’ also change list ‘x’?
# If you wrote code like:
# >>> x = []
# >>> y = x
# >>> y.append(10)
# >>> y
# [10]
# >>> x
# [10]
# you might be wondering why appending an element to y changed x too.
# There are two factors that produce this result:
# Variables are simply names that refer to objects. 
    # Doing y = x doesn’t create a copy of the list – 
    # it creates a new variable y that refers to the same object x refers to. 
    # This means that there is only one object (the list), and both x and y refer to it.
# Lists are mutable, which means that you can change their content.
# After the call to append(), the content of the mutable object has changed from [] to [10]. 
# Since both the variables refer to the same object, using either name accesses the modified value [10].

# Part III
# >>> x = 5  # ints are immutable
# >>> y = x
# >>> x = x + 1  # 5 can't be mutated, we are creating a new object here
# >>> x
# 6
# >>> y
# 5


''' In other words:

If we have a mutable object (list, dict, set, etc.), 
we can use some specific operations to mutate it and all the variables that refer to it will see the change.
If we have an immutable object (str, int, tuple, etc.), 
all the variables that refer to it will always see the same value, 
but operations that transform that value into a new value always return a new object.
If you want to know if two variables refer to the same object or not, 
you can use the is operator, or the built-in function id().
'''