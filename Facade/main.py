class Sensor(object):

    def __init__(self):
        ...

    def sensor_on(self):
        print("Sensor on")
    
    def sensor_off(self):
        print("Sensor off")

class Smoke(object):

    def __init__(self):
        ...

    def smoke_on(self):
        print("Smoke on")
    
    def smoke_off(self):
        print("Smoke off")

class Lights(object):

    def __init__(self):
        pass

    def light_on(self):
        print("Lights on")

    def light_off(self):
        print("Light off")

class Facade(object):

    """ Facade Design Patterns """

    def __init__(self) -> None:
        self._sensor = Sensor()
        self._smoke = Smoke()
        self._light = Lights()
    
    def emergency(self):
        self._sensor.sensor_on()
        self._light.light_on()
        self._smoke.smoke_on()

    def no_emergency(self):
        self._sensor.sensor_off()
        self._light.light_off()
        self._smoke.smoke_off()

if __name__ == "__main__":

    facade = Facade()
    sensor = 22
    if sensor > 30:
        facade.emergency()
    else:
        facade.no_emergency()
    
