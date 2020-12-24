"""
def func(a, b=5, c=10):
    print("a is", a, "and b is", b, "and c is", c)
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(1, c=100)
func(b=22, c=33)
"""
def func(a, b=5, c=10):
    print("a is", a)
    print('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)
func(25, c=24)
func(c=50, a=100)
func(c=20, a=20)
