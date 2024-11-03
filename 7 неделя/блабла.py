class Vector:
    def __init__(x, y, z):
        assert isinstance(x, (int, float)) and not isinstance(x, bool)
        assert isinstance(y, (int, float)) and not isinstance(y, bool)
        assert isinstance(z, (int, float)) and not isinstance(z, bool)
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)
    def __add__(self, other):
        assert isinstance(other, Vector)
        return Vector (self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        assert isinstance(other, Vector)
        return Vector (self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        if isinstance(other, (int, float)):
            return Vector (self.x*other, self.y*other, self.z*other)
        else:
             raise AssertionError
    def _vec_(self, other):
        assert isinstance(other, Vector)
        v = Vector (self.y*other.z - self.z*other.y, self.z*other.x - other.z*self.x, self.x*other.y - other.x*self.y)
        return abs(v), v.x, v.y, v.z
    def __str_(self):
        return f'x={self.x}, y={self.y}, z={self.z},'
v1 = Vector(1, 2, 3)
v2 = Vector(2, 3, 4)
v3 = Vector(3, 4, 5)
a = [v1,v2,v3]
def max_area(l):
    r = []
    for i in l:
        for j in l:
            if i != j:
                r.append(i-j)
    results = []
    for z in r:
        for k in r:
            results.append(z._vec_(k))
    h = []
    for u in results:
        h.append(abs(u))
    print(max(h))
max_area(a)