class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} едет')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Вы превысили скорость 60 км/ч')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')
        if self.speed > 40:
            print('Вы превысили скорость 40 км/ч')

class PoliceCar(Car):
    pass

car_1 = SportCar(250, 'Желтая', 'Шевроле Камаро', False)
car_2 = TownCar(90, 'Черная', 'Тойота Камри', False)
car_3 = WorkCar(60, 'Белая', 'Шкода Октавиа', False)

car_1.show_speed()
car_2.show_speed()
car_3.show_speed()
car_3.turn('налево')

