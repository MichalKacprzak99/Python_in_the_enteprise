import sys
import logging
from events import Accident, Faster, Slower, Left, Right, PitStop, CoronaVirus, EndSimulation
from car import Car

logging.basicConfig(
     filename='car_simulator.log',
     level=logging.INFO,
     format='[%(asctime)s] - %(message)s%(funcName)s',
     datefmt='%H:%M:%S'
 )


class ValueTooLargeError(Exception):
   pass


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