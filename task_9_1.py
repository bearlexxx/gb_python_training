from time import sleep

class TrafficLight:

    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2), ('Green', 7))

    def running(self):
        while True:
            for color, delay in self.__color:
                print(color)
                sleep(delay)


traffic_light = TrafficLight()
traffic_light.running()

