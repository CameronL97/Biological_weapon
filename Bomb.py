"""
Bacteria Bomb Model
Created by Cameron Leighton
"""
#import the operators 
import csv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import tkinter
import time


#creates the figure and the axes 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 300, 0, 300])


#create the number of bacteria being modelled
num_of_bacteria = 500

#create an empty list to append the bacteria data to 
bacteria = []

#create an empty list to append the environment to 
environment = []

#create an empty list to append append the bacteria that have hit the ground to
fallen = []

#create the environment
with open ('City.csv') as f:
#open CSV 
    readCSV = csv.reader(f,delimiter = ',')
#for each row in CSV it creates a new list 
    for row in readCSV:
        rowlist = []
#for each value in the rows of the CSV it appends the interger
        for value in row:
#            print(float(value))
            rowlist.append(int(value))
#the rowlist is then appended into the environment 
        environment.append(rowlist)


#this give values to the conditions we will append to each bacteria such as the x,y postion and height(t) and whether or not it has fallen
t = None
x = None
y = None       
has_fallen = 0

#append the x,y,t & has_fallen data to the bactria for each individual bacteria 
for i in range(num_of_bacteria):
     bacteria.append(agentframework.Bacteria(bacteria,environment,has_fallen,fallen,t,x,y))
carry_on = True


# starts a clock for testing the time the model takes to run 
start = time.clock()


# defines the update in the model for each time the model moves    
def update(frame_number):
#    counter = 0
    fig.clear()   
    global carry_on

#each time the model moves the bacteria will do 3 things dependig if conditions are met
    for i in range(num_of_bacteria):
#here a switch is used where if the bacteria has hit the ground the loop wont run 
        if ((len(bacteria))) != 0 and bacteria[i].has_fallen == 0:
#moves the bacteria 
            bacteria[i].move()
#makes the bacteria fall to the ground            
            bacteria[i].fall()
#changes the state of the bacteria if they hit the ground   
            bacteria[i].landed()
    
#plots the envrioment using matplotlib and shows the environment on the plot
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.imshow(environment)
    
#plots the bacteria was used in the testing porcess to make sure the bacteria moved and fell
    for i in range(num_of_bacteria):
#simple switch again for the bacteria 
       if bacteria[i].has_fallen == 0:
#if the abacteria are still airborne then they are ploted in white 
           matplotlib.pyplot.scatter(bacteria[i]._x,bacteria[i]._y, marker = "*", color = 'white')
       else:
#if the bacteria have landed they are plotted by a yellow cross 
           matplotlib.pyplot.scatter(bacteria[i]._x,bacteria[i]._y, marker = "x", color = 'yellow')


#create the stopping condtion
def gen_function(b = [0]):
    for i in range(num_of_bacteria):
        global carry_on #Not actually needed as we're not assigning, but clearer
        
#while the list size of bacteria doesnt = the list size of the fallen and the carry on is true the model will run  
        while ((len(bacteria)) != (len(fallen))) & (carry_on) :
            yield len(bacteria)
            
#if the list of fallen does = list size of bacteria then the model stops 
        if (len(fallen)) == (len(bacteria)):
            carry_on = False
            
#writes the x and y data to a text file so it can be inputted into the density program
        with open ('fallen.csv',mode ='w') as fallen_list:
            fallen_writer = csv.writer(fallen_list,delimiter = ',')
#currently this only puts the last x and y coordinate into the text file 
            fallen_writer.writerow([fallen[i]._x,fallen[i]._y])
    
   
#prints the x and y of all the landed bacteria 
            print (fallen[i]._x,fallen[i]._y)
    
#prints to say all the bacteria have landed 
    print ("all the bacteria have landed")
    
#ends the clock 
    end = time.clock()
#prints the run time of the model 
    print("time = " + str(end - start))    

#creates the tkinter animations and the gui 
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

root = tkinter.Tk()
root.wm_title("Bacteria Bomb")
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


tkinter.mainloop()           
