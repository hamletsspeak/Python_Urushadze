import math

class Shape:
    def __init__(self, identifier, x, y):
        if not isinstance(identifier, str) or len(identifier) == 0:
            raise ValueError("Идентификатор должен быть непустой строкой")
        self.identifier = identifier

        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"{self.identifier} переехал в ({self.x}, {self.y})")

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Quad(Shape):
    def __init__(self, identifier, x, y, side_length):
        super().__init__(identifier, x, y)
        if side_length <= 0:
            raise ValueError("Длина стороны должна быть положительным числом")
        self.side_length = side_length

    def is_intersect(self, other):
        distance = self.distance_to(other)
        if distance <= (self.side_length + other.side_length) / 2:
            print(f"{self.identifier} пересекается с {other.identifier}")
        else:
            print(f"{self.identifier} не пересекается с {other.identifier}")

class Pentagon(Shape):
    def __init__(self, identifier, x, y, side_length):
        super().__init__(identifier, x, y)
        if side_length <= 0:
            raise ValueError("Длина стороны должна быть положительным числом")
        self.side_length = side_length

    def is_intersect(self, other):
        distance = self.distance_to(other)
        if distance <= (self.side_length + other.side_length) / 2:
            print(f"{self.identifier} пересекается с {other.identifier}")
        else:
            print(f"{self.identifier} не пересекается с {other.identifier}")

# Пример использования с обработкой исключений

try:
    quad1 = Quad("T1", 0, 0, 5)
    quad2 = Quad("t1", 6, 6, 4)
    pentagon1 = Pentagon("T2", 3, 3, 6)

    quad1.move(2, 2)
    pentagon1.move(5, 5)

    quad1.is_intersect(quad2)
    pentagon1.is_intersect(quad1)

except ValueError as e:
    print("Произошла ошибка:", e)
