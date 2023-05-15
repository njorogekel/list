sum=2+30//5
print(sum)
x=30%2+4+6
print(x)
y=(7%2)*3+4<5
print(y)

perfomance=int(input("enter marks\n"))
attendance=int(input("enter percentage\n"))
if perfomance >= 50 and attendance >= 75:
    print("pass")
elif attendance <= 75:
    print("retake course")
else:
    print("sit for supplimentary exam")

i=int(input("enter amount to buy\t"))
bundles=5*i
print("you have purchased",bundles,"mbs")
