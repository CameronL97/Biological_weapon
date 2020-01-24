"""
Agent Framework for use with the bacteria bomb model
Created by Cameron Leighton
"""
#import the modules
import random

#create a new class called bacteria 
class Bacteria:
#create the variable that will be modified in the model
    def __init__(self,bacteria,environment,has_fallen,fallen,t=None,x=None,y=None):
#makes the bacteria 
        self.bacteria = bacteria   
#sets the state to be modified
        self.has_fallen = has_fallen
#sets the height of the bacteria at 75 due to the brief when t = none else t = t 
        self.fallen = fallen
        if (t==None):
            self._t = 75
        else :
            self._t = t 
#sets the x cooridinate at 50 as per the brief when x = none else x = x
        if (x==None):
            self._x = 50
        else:
            self._x = x
#sets the y coordinate at 150 as per brief when y = none else y =y 
        if (y==None):
            self._y = 150
        else:
            self._y = y

    
# this next bit of code moves the bacteria through the environment 
    def move (self):
#this moves the code west at a 5% chance 
        if random.random() < 0.05:
            self._x = (self._x - 1)
# then there is a 75% to move east that is used by using the elif command
        elif random.random() > 0.25:
            self._x = (self._x + 1) 
        else:
# else the bacteria has a 20% chance to remain in the same place on the x axis 
            self._x = self._x
# the bacteria has a 10% chance to move north
        if random.random () <0.1:
            self._y = (self._y + 1) 
# the bacteria also has a 10% chance to move south
        elif random.random () > 0.9:
            self._y = (self._y - 1) 
# if neither condition is met then y remains the same
        else:
            self._y = self._y 
            
            
#creates the fall command 
    def fall (self):
#while t>75 there is a 20% chance the bacteria may be blown upward by 1 metre 
        while self._t >= 75 and random.random () < 0.2:
            self._t = (self._t + 1)
        else :
            self._t = self._t
#while t> 75 there is a 70% chance for it to fall by 1 metre 
        while self._t >= 75 and random.random () > 0.3:
            self._t = (self._t - 1)
        else:
            self._t = self._t
# while t<75 the bacteria falls by 1 metre on each update 
        if self._t < 75:
            self._t = (self._t - 1)
#ensures that t can never be under 0        
        if self._t < 0:
            self._t = 0
            
            
#creates the landed switch
    def landed (self):
#if t = 0 then the switch turns to 1 
        if self._t == 0:
            self.has_fallen = (self.has_fallen + 1)
        else:
#if not then it remains the same 
            self.has_fallen = self.has_fallen
#the next part appends code to another list 
        for bacteria in self.bacteria:
#if t = 0 then the model will append the index to the fallen list
            if self.has_fallen == 1:
                index_fallen = self.bacteria.index(bacteria)
                if bacteria not in self.fallen:
                    self.fallen.append(bacteria)
                    
# tried experimenting with deleting from list however this threw up lots of errors 
#                    del self.bacteria[index_fallen]

            
                    
