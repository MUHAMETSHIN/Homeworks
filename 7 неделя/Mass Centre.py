class Vector:
    def __init__(self, x, y, z):
        assert isinstance(x, (int, float)) and not isinstance(x, bool)
        assert isinstance(y, (int, float)) and not isinstance(y, bool)
        assert isinstance(z, (int, float)) and not isinstance(z, bool)
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):#Сумма
        assert isinstance(other, Vector)
        return Vector (self.x + other.x, self.y + other.y, self.z + other.z)
    def __mul__(self, other): #Скалярное произведение и произведение на число + еще и координаты
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        if isinstance(other, (int, float)):
            return Vector (self.x * other, self.y * other, self.z * other), (self.x * other, self.y * other, self.z * other)
            
        else:
             raise AssertionError

def centreMass(vectors):
    a = Vector(0, 0, 0)
    for i in vectors:
        a += i
    print(a * (1/len(vectors)))


v1 = Vector(2, 3, 6)
v2 = Vector(1, 2, 4)
v3 = Vector(3, 4, 2)
vectors = [v1, v2, v3]


centreMass(vectors)

