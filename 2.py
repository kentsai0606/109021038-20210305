class Chess:
    def __init__(self,name,color ,quantity):
        self.name=name
        self.color=color
        self.quantity=quantity
        
        

def showinfo(x):
    print(x.name,"\t",x.color,"\t",x.quantity)

x1=Chess("炮","red","2")
x2=Chess("馬","black","2",)
x3=Chess("車","black","2")

print(showinfo(x1))
print(showinfo(x2))
print(showinfo(x3))