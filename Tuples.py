names = ("Paul","Cephas","Tyson","Shiku","Shiku")
print(names)
print(len(names))
print(type(names))

a = list(names)
print(a)
a.remove("Shiku")
names = tuple(a)
print(names)