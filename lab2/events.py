from abc import ABC, abstractmethod
import sys
import logging

logging.basicConfig(
     filename='car_simulator.log',
     level=logging.INFO,
     format='[%(asctime)s]-%(message)s%(funcName)s',
     datefmt='%H:%M:%S'
 )


class Event(ABC):
    def trigger(self, car):
        pass
    def print_info(self):
        pass


class Accident(Event):
    def trigger(self, car,):
        car.need_of_repair = True
        car.auto_repair()
    def print_info(self):
        logging.info('This accident cost you a 100 dolar, Class: {} ; Method: '.format(self.__class__.__name__))


class Faster(Event):
    flag = True
    def trigger(self, car):
        if car.velocity < car.max_velocity:
            car.velocity += 1
            Faster.flag = True
        else:
            Faster.flag = False

    def print_info(self):
        if Faster.flag:
            logging.info('More speed? No problem, Class: {} ; Method: '.format(self.__class__.__name__))
        else:
            logging.info('You reach car maximum speed, Class: {} ; Method: '.format(self.__class__.__name__))


class Slower(Event):
    flag = True
    def trigger(self, car):
        if car.velocity > 0:
            car.velocity -= 1
            Slower.flag = True
        else:
            Slower.flag = False

    def print_info(self):
        if Slower.flag:
            logging.info('Really? Slower?, Class: {} ; Method: '.format(self.__class__.__name__))
        else:
            logging.info('Your speed is zero, tou can\'t go slower, Class: {} ; Method: '.format(self.__class__.__name__))


class Left(Event):
    def trigger(self, car):
        if car.wheel_angle > -90:
            car.wheel_angle -= 1
    def print_info(self):
        logging.info('Turn left, as you wish, Class: {} ; Method: '.format(self.__class__.__name__))


class Right(Event):
    def trigger(self, car):
        if car.wheel_angle < 90:
            car.wheel_angle += 1
    def print_info(self):
        logging.info('Turn right3, as you wish, Class: {} ; Method: '.format(self.__class__.__name__))


class PitStop(Event):
    def trigger(self, car):
        t = 0
        dt = 0.5
        car.is_running = False
        car.velocity = 0
        while t <= 10:
            t += dt
        car.is_running = True
    def print_info(self):
        logging.info('No fuel, we had to stop, Class: {} ; Method: '.format(self.__class__.__name__))

class CoronaVirus(Event):
    def trigger(self,car):
        logging.info('Soup was enough to kill humanity, Class: {} ; Method: '.format(self.__class__.__name__))
        sys.exit(0)


class EndSimulation(Event):
     def trigger(self,car):
        logging.info('Thank you, Class: {} ; Method: '.format(self.__class__.__name__))
        sys.exit(0)