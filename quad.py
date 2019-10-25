#!/usr/bin/local/python3
class Quad:
    def __init__(self,isRegular):
        self.isRegular = isRegular

    def DefineType(self):
        if(self.isRegular):
            a = int(input("Enter the value: "))
            print("It is a square with side {}".format(a))
            self.sides = [a]
            
        else:
            h = [ int(input("Enter the value: ")) for _ in range(2)]
            print("It is NOT a regular quadrilateral and sides are {} and {}".format(h[0],h[1]))
            self.sides = h

# class Irregular_Perim(Quad):
#     super().__init__(self,isRegular)
#     def CalculatePerim(self):
#         x,y = self.sides
#         return 2*(x+y)

if input("Is it a regular quadrilateral? ") in ['True','yes','y']:
    n = True
else:
    n = False

z = Quad(n)
z.DefineType()
print(z.sides)