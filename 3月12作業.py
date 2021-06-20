class Student:
    def __init__(self,name,id ,height,weight,gender):
        self.name=name
        self.id=id
        self.height=height
        self.weight=weight
        self.gender=gender

def showinfo(x):
    print(x.name,"\t",x.id,"\t",x.height,"\t",x.weight,"\t",x.gender)

x1=Student("王小明","109021494","181","70","男")
x2=Student("陳小國","109021959","176","65","男")
x3=Student("張小美","109021355","160","50","女")

print(showinfo(x1))
print(showinfo(x2))
print(showinfo(x3))
