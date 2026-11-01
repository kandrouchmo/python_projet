class forme:
    def __init__(self, x=0 , y=0):
        self.x=x
        self.y=y
class rectangle(forme):
    def __init__(self, x=0 , y=0):
        forme.__init__(self, x, y)
    def air(self):
          return ( self.x * self.y)

class triangle(forme):
    def __init__(self, x=0 , y=0):
        forme.__init__(self, x , y)
    def air(self):
        return ( self.x * self.y/2)

R=rectangle(int(input("entrer la varieble x et y pour faire le calcule")))
T=triangle(int(input("entrer la varieble x et y pour faire le calcule")))

print(f"la valeur {R.air()}" )
print(f"la valeur {T.air()}" )