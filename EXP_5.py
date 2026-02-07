print("Date: 27/01/26, UIN: 251A015")
l=[]
name=[]
age=[]
section=[]
name.extend([input("enter your name: "),input("enter your Friends name: ")])

age.extend([input("enter your age: "),input("enter your friends age: ")])
section.extend([input("enter your section: "),input("Enter your friends section: ")])

l.extend([(name[0],age[0],section[0]),(name[1],age[1],section[1])])
print(l)
