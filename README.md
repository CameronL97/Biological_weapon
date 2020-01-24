# Bacteria Bomb

A model to show fallout of a biological weapon set off in a city

## Project Status

Currently due to the deadline of the Module this is for the model is currently unfinished however the majority of the model is finished. Further work is required to import the output of the model into the density map.

## Roadmap

No further work will be completed on this model at this current time.

1. Create Agents - Completed

2. Create Environment - Completed

3. Create wind conditions - Completed

4. Create falling conditions - Completed

5. Create a landed switch - Completed

6. Append landed bacteria to a new list - Completed

7. Write new list to CSV - Failed (only writes 1 X and Y coordinate to the list)

8. Produce density plots - Completed (with random numbers)

9. Export density plot to Image - Completed

10. Expand the model - Potential for further work if revisited

## Description

The brief of the model was to produce a density map of the fallout of a biological weapon within a city. The bomb is set off a specific point within the city and release a number of deadly bacteria. The bacteria move around the city as the wind blows and have specific chances of moving in any direction. When the bacteria are below 75m they start to fall to the ground and when they land their X and Y coordinates are recorded to a CSV. This CSV is imported into another model the plots a density using Gaussian Kernel Density and exports the graphs to a .png file.

The model currently maps the fallout of the bacteria as an animation, however there is a problem writing to CSV. The density plots therefore only produce a density of random points 


![Model](https://i.imgur.com/mIfZZlp.png)
Model of bacteria falling


## Usage 

![UML](https://i.imgur.com/d56YLob.png)

As we can see from the UML file the model requires the three different codes to run. The agent framework alters the starting height, and coordinates of the bacteria bomb where the bacteria are released from. The Model itself contains the environment from which the bacteria move through and creates the number of bacteria. The model also moves the bacteria through the environment and writes the fallen places to a CSV. The fallen bacteria are then plotted within the density model which then converts it into a density plot.
We can manually alter the number of bacteria.

```bash
num_of_bacteria = 10
```
The code for the moving and falling of bacteria is all based on probability.

```bash
    def move (self): 
        if random.random() < 0.05:
            self._x = (self._x - 1)
        elif random.random() > 0.25:
            self._x = (self._x + 1) 
        else:
            self._x = self._x
        if random.random () <0.1:
            self._y = (self._y + 1) 
        elif random.random () > 0.9:
            self._y = (self._y - 1) 
        else:
            self._y = self._y 

    def fall (self): 
        while self._t >= 75 and random.random () < 0.2:
            self._t = (self._t + 1)
        else :
            self._t = self._t
        while self._t >= 75 and random.random () > 0.3:
            self._t = (self._t - 1)
        else:
            self._t = self._t 
        if self._t < 75:
            self._t = (self._t - 1)       
        if self._t < 0:
            self._t = 0 
``` 
The values can be altered manually to change the windspeed and the way the bacteria rises and falls.

## Output
This is the output of the density model that we should expect to gather for the bacteria.

![Density Plots](https://i.imgur.com/B4ug22R.png)
Density plots showing steps to create the last contoured plot.

## Testing 
To test the model, a simple timing test was run with varying the number of bacteria. To simulate the 5000 bacteria multiple tests were done to calculate the completion time.

```bash
num_of_bacteria = 10
```
The model takes 22 seconds to run so 5000 bacteria would take 183 minutes to simulate all bacteria.   

```bash
num_of_bacteria = 100
```
The model takes 29 seconds to run so 5000 bacteria would take 24 minutes to simulate all the bacteria.

```bash
num_of_bacteria = 200
```
The model takes 40 seconds to run so 5000 bacteria would take 17 minutes to simulate all of the bacteria.

```bash
num_of_bacteria = 500
```
The model takes 72 seconds to run so 5000 bacteria would take 12 minutes to simulate all of the bacteria.

```bash
num_of_bacteria = 5000
```
The model crashes after 13 minutes. 

The best way to simulate all of the bacteria falling seems to be to run 500 bacteria for 10 iterations of the model.

## Limitations 

As we have already stated the model crashes if 5000 bacteria are run through the model. This seems to be a hardware issue. One method to fix this would be to remove the animation from the model and recode the model so the model doesn’t have to redraw the model for 5000 bacteria each time they move.This would increase the eficiency of the model and reduce memory usage allowing it to run faster. However due to time constraints this was not complete.

Currently further work is required to write to the CSV currently the model only writes the X and Y coordinates to the CSV of the last bacteria to land. One potential fix may be the creation of a new environment and to add a 1 to the environment when a bacteria lands and then plotting the density as that.

The current values for windspeed and number of bacteria have to be altered manually within the file. Creating a scrollbar that can modify the number of bacteria and the probability of moving with windspeed would further increase the usage of the model.

The bacteria all start at 75m and X = 50 and Y = 150 which is what is wanted but does not simulate an explosion further coding may add in a probability again for the bacteria to be thrown out in an explosion like simulation around the top of the building with different distances from the point source and different heights so that the bacteria will provide a better density map as currently they are all clumped together.

The bacteria in the air should move according to fluid dynamics. If they are too clumped together then they should push each other away and if they are further away should ideally slow move towards each other till a threshold is hit. This could be done by a creating a neighbourhood for the particles and helps make the simulation more real world like.

## Contributing

This model does not require any contribution at this time however if you wish to work on the model it is free to work on.

## Authors and acknowledgement

Code written by Cameron Leighton.

Further help and reading:

Andy Turner - University of Leeds

https://python-graph-gallery.com/2d-density-plot/

## License 

[MIT](https://choosealicense.com/licenses/mit/)



   
