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
    def __matmul__(self,other):   # площадь треугольника, который образуют два вектора
       return (((self.y*other.z-self.z*other.y)**2 + (self.z*other.x-self.x*other.z)**2 + (self.x*other.y-self.y*other.x)**2)**0.5)/2


v1 = Vector(2, 3, 6)
v2 = Vector(1, 2, 4)
v3 = Vector(3, 4, 2)
v4 = Vector(4, 5, 7)
v5 = Vector(1, 8, 4)
vectors = [v1, v2, v3, v4, v5]

def max_area(vectors):
    maximus = 0
    max_area_vectors = [0, 0, 0]
    for i in vectors:
        for j in vectors:
            for k in vectors:
                #находим стороны треугольников
                V1 = i - j 
                V2 = i - k
                #находим площадь треугольника
                area = V1 @ V2
                if area > maximus:
                    maximus = area
                    max_area_vectors[0] = [i.x, i.y, i.z]   #нагляднее будет если выведем координаты точек, а не вектора их задающие
                    max_area_vectors[1] = [j.x, j.y, j.z]
                    max_area_vectors[2] = [k.x, k.y, k.z]
                    
    print(maximus)
    print(max_area_vectors)
max_area(vectors)