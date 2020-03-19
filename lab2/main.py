# Write a module that will simulate autonomic car.
# The simulation is event based, an example:
# car1 = Car()
# car1.act(event)
# print(car1.wheel_angle, car1.speed)
# where event can be anything you want, i.e. :
# `('obstacle', 10)` where `10` is a duration (time) of the event.
##The program should:
# - act on the event
# - print out current steering wheel angle, and speed
# - run in infinite loop
# - until user breaks the loop

#The level of realism in simulation is of your choice, but more sophisticated solutions are better.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to github repository. 
#
#Delete these comments before commit!
#Good luck.
import sys
import math
class Car:
    def __init__(self, x=0, y=0, vel=0, acc= 0, wheel_angle = 0):
        self.velocity = vel
        self.acc = acc
        self.pos_x = x
        self.pos_y = y
        self.wheel_angle = wheel_angle
    def faster(self, time_duration):
            t = 0
            dt = 0.5
            while t<time_duration:
                self.velocity += self.acc*dt
                self.pos_x += self.velocity*dt + self.acc*math.cos(self.wheel_angle)*dt**2
                self.pos_y += self.velocity*dt + self.acc*math.sin(self.wheel_angle)*dt**2
                t += dt
            
    def slower(self, time_duration):
            t = 0
            dt = 0.5
            while t<time_duration:
                self.velocity += self.acc*dt
                self.pos_x -= self.velocity*dt + self.acc*math.cos(self.wheel_angle)*dt**2
                self.pos_y -= self.velocity*dt + self.acc*math.sin(self.wheel_angle)*dt**2
                t += dt
            

class Interface:
    def __init__(self):
        self.choices_interface ={
            "1": self.create_car,                
            "2": self.show_param,
            "5": self.quit 
        }     
        self.choices_car = {                
            "3": self.faster, 
            "4": self.slower                                         
            }
    def display_menu(self):
        print(""" Notebook Menu
            1. Create car
            Car oprtion:
            2. Parameters
            3. Faster
            4. Slower
            5. Quit """)
    def run(self):
        while True:            
            self.display_menu()            
            choice = input("Enter an option: ")     
            action = self.choices_interface.get(choice)           
            if action:       
                action()
            action =  self.choices_car.get(choice)               
            if action:
                time =int(input("How long car should accelarate?: "))
                action(time)
    def quit(self):        
        print("Thank you for using.")       
        sys.exit(0)
    def create_car(self):
        choice_x = int(input("Position x: "))
        choice_y = int(input("Position y: "))
        choice_vel = int(input("initial velocity: "))
        choice_acc = int(input("initial acceleration: "))
        choice_wheel_angle = int(input("wheel_angle: "))
        self.car = Car(choice_x, choice_y, choice_vel, choice_acc, choice_wheel_angle)
    def faster(self, time):
        self.car.faster(time)
    def show_param(self):
        print("pos_x= "+str(self.car.pos_x) + " pos_x= " + str(self.car.pos_y) +
         " velocity= " + str(self.car.velocity) + " speed= " + str(self.car.acc) + 
         " wheel_angle= " + str(self.car.wheel_angle))
    def slower(self,time):
        self.car.slower(time)
if __name__ == "__main__":    
    Interface().run() 

