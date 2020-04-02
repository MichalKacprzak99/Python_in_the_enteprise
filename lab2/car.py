import logging

logging.basicConfig(
     filename='car_simulator.log',
     level=logging.INFO,
     format='[%(asctime)s] - %(message)s%(funcName)s',
     datefmt='%H:%M:%S'
 )


class Car:
    def __init__(self, max_velocity):
        self.velocity = 0
        self.wheel_angle = 0
        self.max_velocity = max_velocity
        self.is_running = False
        self.need_of_repair = False

    def print_parameters(self):
        wheel_angle_str = "Wheel angle = {} ".format(self.wheel_angle)
        car_speed_str = "Car speed = {} ".format(self.velocity)
        logging.info(wheel_angle_str + car_speed_str +'Class: {} ; Method: '.format(self.__class__.__name__))

    def launch_engine(self):
        logging.info('Let\'s begin our journey, Class: {} ; Method: '.format(self.__class__.__name__))
        self.is_running = True

    def auto_repair(self):
        t = 0
        dt = 0.5
        while t <= 10:
            t += dt
        self.need_of_repair = False
        logging.info('Auto repair successful, Class: {} ; Method: '.format(self.__class__.__name__))

    def act(self, event):
        event().trigger(self)
        event().print_info()