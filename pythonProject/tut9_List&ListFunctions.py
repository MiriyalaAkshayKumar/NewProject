grocery=["harpic","vim bar","Dabur Red",56,"Xtra Soap"]
print(grocery[4])
print(grocery[0:7])
print(len(grocery))
grocery.insert(3,"Lux Soap")
print(grocery)
Numbers=[10,20,30,40,50]
Numbers.sort()
#Numbers.reverse()
print(Numbers)
Numbers.insert(3,43)
Numbers.append(24)
print(Numbers)
#print(Numbers[::-1])
"""Tuple is immutable
Mutable can be change
Immutable can't change
"""
tp=(1,2,3)
print(tp)
#tp[2]=10
#print(tp)
"""Reversing the Number"""
a=10
b=20
a,b=b,a
print(a   ,",", b)