class Hero:
    def __init__(self,name,id ,attack,speed,hp):
        self.name=name
        self.id=id
        self.attack=attack
        self.speed=speed
        self.hp=hp

def showinfo(x):
    print(x.name,"\t",x.id,"\t",x.attack,"\t",x.speed,"\t",x.hp)

x1=Hero("一號","001","5","6","50")
x2=Hero("二號","002","2","4","90")
x3=Hero("三號","003","9","8","110")

print(showinfo(x1))
print(showinfo(x2))
print(showinfo(x3))
