'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина едет")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула в направлении {direction}")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("Скорость превышена")
        else:
            print(self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("Скорость превышена")
        else:
            print(self.speed)


class PoliceCar(Car):
    pass


town = TownCar(60, "grey", "VW")
sport = SportCar(100, "red", "Ferrari")
work = WorkCar(70, "white", "Gaz")
police = PoliceCar(75, "blue & white", "Lada", is_police=True)

work.show_speed()
print(f'Это полицейская машина? {police.is_police}')
