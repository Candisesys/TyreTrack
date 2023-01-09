from pyray import *

class Car:
    def __init__(self, pos_vec: Vector2, speed: Vector2 = Vector2(0, 0)):
        self.pos_vec = pos_vec
        self.speed = speed
        self.move_speed = Vector2(2, 0)
        self.collrec = Rectangle(0, 0, 0, 0)
    def update(self):
       self.pos_vec = vector2_add(self.pos_vec, self.speed)
       if (is_key_down(ord("D"))):
            self.speed = vector2_multiply(self.move_speed, Vector2(1, 1))
       elif (is_key_down(ord("A"))):
            self.speed = vector2_multiply(self.move_speed, Vector2(-1, -1))
       else:
            self.speed = Vector2(0, 0)
       self.collrec = Rectangle(self.pos_vec.x, self.pos_vec.y, 30, 10)
    def draw(self):
        draw_rectangle_v(self.pos_vec, Vector2(60, 50), RED)

class Road(Car):
    def __init__(self, pos_vec: Vector2, speed: Vector2 = Vector2(0, 0)):
        super().__init__(pos_vec, speed)
        self.collrec = Rectangle(0, 0, 0, 0)
    def update(self):
        self.pos_vec = vector2_add(self.pos_vec, self.speed)
        self.collrec = Rectangle(self.pos_vec.x, self.pos_vec.y, 300, 200)
    def draw(self):
        draw_rectangle_v(self.pos_vec, Vector2(300, 400), GRAY)