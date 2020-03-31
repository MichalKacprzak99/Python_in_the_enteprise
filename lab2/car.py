import sys
import logging
from events import Accident, Faster, Slower, Left, Right, PitStop, CoronaVirus, EndSimulation

logging.basicConfig(
     filename='car_simulator.log',
     level=logging.INFO,
     format='[%(asctime)s] - %(message)s%(funcName)s',
     datefmt='%H:%M:%S'
 )
class ValueTooLargeError(Exception):
   pass

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


class Enviroment:
    def __init__(self, car):
        self.car = car
        self.available_events = {
            1: Accident,
            2: Faster,
            3: Slower,
            4: Left,
            5: Right,
            6: PitStop,
            7: CoronaVirus,
            8: EndSimulation,
        }

    def __str__(self):
        option_str = ""
        for key in self.available_events:
            option_str += "{} : {} \n".format(key,self.available_events[key].__name__)
        return option_str

    def handle_bad_input(self):
        bad_input_str = 'This is not proper input, try again'   
        return bad_input_str
        
    def start(self):
        print(self)
        self.car.launch_engine()
        while True:
            try:
                event_number = int( input('Which event do you wanna test? ') )
                if event_number >= 9:
                    raise ValueTooLargeError
                event = self.available_events[event_number]
                self.car.act(event)
                self.car.print_parameters()
            except (ValueError,KeyError):
                logging.info('This is not proper input, try again, Class: {} ; Method: '.format(self.__class__.__name__))
                print(self.handle_bad_input())
            except ValueTooLargeError:
                logging.info('This is not proper input, try again, Class: {} ; Method: '.format(self.__class__.__name__))
                print(self.handle_bad_input())

if __name__ == "__main__":
    enviroment = Enviroment(Car(10))
    enviroment.start()