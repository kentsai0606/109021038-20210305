class Book:
    def __init__(self,name,id ,price,language,species):
        self.name=name
        self.id=id
        self.price=price
        self.language=language
        self.species=species

def showinfo(x):
    print(x.name,"\t",x.id,"\t",x.price,"\t",x.language,"\t",x.species)

x1=Book("美食通","102959269","180","中文","工具類")
x2=Book("冒險王","165115168","500","中文","科幻類")
x3=Book("One Night","19491649","760","英文","浪漫類")

print(showinfo(x1))
print(showinfo(x2))
print(showinfo(x3))