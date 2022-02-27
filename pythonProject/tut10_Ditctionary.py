"""Dictionary is npthing but a key value pair"""
d1={}
print(type(d1))
d2={"Akshay" : "Mutton" , "Ram":"Roti", "Manoj":"Allu" , "Nani":{"B":"Magiee","L":"Rice","D":"Chicken"}}
print(d2)
print(d2["Akshay"])
print(d2["Manoj"] ,"\n", d2["Ram"])
print(d2["Nani"])
print(d2["Nani"]["B"])
d2["Shyam"]={"L":"Junk food", "D":"Non-veg"}
d2[420]={"kabab"}
print(d2)
del d2[420]
print(d2)
d3=d2.copy()
print(d3)
del d3["Nani"]
print(d3)
d3.update({"Geeta": "Choclate"})
print(d3)
print(d2.keys())
print(d2.items())

#Excerise
h1={"Sita":"Veg","Geeta":"Non-veg","Babita":"Bugger","Ankit":{"L":"Dal Rice","D":"Roti curry"}}
i1=input();
print(h1.get(i1))