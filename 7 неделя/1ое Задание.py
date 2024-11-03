# сложение +
# вычитание -
# * как скалярное произведение [вектор с вектором]
# * на число [вектор и число]) Реализуйте конструктор, который принимает строку в формате {x, y, z}. Учтите, что в векторе могут лежать только числа (сделайте assert на то, что x,y,z это числа).
class Vector:
    def __init__(self, x, y, z):
        assert isinstance(x, (int, float)) and not isinstance(x, bool)
        assert isinstance(y, (int, float)) and not isinstance(y, bool)
        assert isinstance(z, (int, float)) and not isinstance(z, bool)
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):#Модуль
        return ((self.x**2 + self.y**2 + self.z**2)**0.5)
    def __add__(self, other):#Сумма
        assert isinstance(other, Vector)
        return Vector (self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):#Разность
        assert isinstance(other, Vector)
        return Vector (self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other): #Скалярное произведение и произведение на число
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        if isinstance(other, (int, float)):
            return Vector (self.x*other, self.y*other, self.z*other)
        else:
             raise AssertionError
v1 = Vector(3, 4, 0)
v2 = Vector(1, 2, 3)
v3 = Vector(1, 1, 1)
print(abs(v1*6))