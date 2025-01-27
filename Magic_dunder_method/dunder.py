## Dunder --> __


class Person:
    def __init__(self, name, age):
        self.name =name
        self.age = age
        
    def __del__(self):
        print("object is being deconstructed")
        
class Vector:
    def __init__(self, x:int, y:int):
        self.x =x
        self.y =y
        
    def __add__(self, other):
        return Vector(self.x +other.x, self.y + other.y)
    
    def __repr__(self):
        return f"X: {self.x}, Y:{self.y}"
    
    def __len__(self):
        return 10
    

    # def __call__(self):
    #     print ("hello I was called!")
        
    def sub(self):
        return (self.x - self.y)
    __call__ = sub
        
if __name__ == "__main__":
    vector1 = Vector(10,20)
    print(vector1)
    print(vector1())
    # vector2 =Vector(50,60)
    # vector3 =vector1+vector2
    # print(len(vector3))
    # print(vector3())
    #print(vector3.x, vector3.y)
    #person =Person("Ankita", 34)