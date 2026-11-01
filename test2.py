class forme:
    def __init__(self, x=0 , y=0):
        self.x=x
        self.y=y

class rectangle(forme):
    def __init__(self, x=0 , y=0):
        forme.__init__(self, x , y)
    def air(self):
        return self.x * self.y 
class triangle(forme):
    def __init__(self, x=0 , y=0):
        forme.__init__(self, x, y)
    def air(self):
        return(self.x * self.y/2)

R=rectangle(5,7)
T=triangle(2,3)

print(f"la variable de rectangle {R.air()}")
print(f"la variable de triangle {T.air()}")
