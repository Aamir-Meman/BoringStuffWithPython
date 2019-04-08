p = ('Bob', 'Smith', 34)

print(p)
print(type(p))
print(p[1])
print(p[2])
"""
Unpacking 

"""

fn, ln, age = p

print(fn)
print(ln)
print(age)

"""
Swaping

"""

a = 1

b = 2

b, a = a, b

print(a)
print(b)

""" 
Empty Tuple

"""

q = ()
print(q)
print(type(q))
"""
Output :- 

('Bob', 'Smith', 34)
<class 'tuple'>
Smith
34
Bob
Smith
34
2
1
()
<class 'tuple'>
"""