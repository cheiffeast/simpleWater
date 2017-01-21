# SimpleWater.py
SimpleWater.py is a water system that allows dynamics waves and interaction. Using hooke's law and a line of points joined by springs you can create a semi-realistic looking water system that can react to user input or if used correctly, can be used in a game and interact with object.

![Alt Text](https://media.giphy.com/media/l3q2BdJDdVpzkRKX6/source.gif)
#Setup and customisation
SimpleWater.py has a fully customisable system where you can change the spring constant between the points, baseline and damping on the resultant forces. You can change the power of the click on the water, offset and fill. Also you can change the number of points on the system and mass of the points.

#Variable definitions:
  * fill - Set to true it will fill in the area under the wave curve (Can look at bit glitchy if the number of nodes is small, N < 100)
  * Offset - The distance down the surface the waters baseline is at
  * ClickPower - This is the distance the point will be moved when you click on it
  * PConstant - This is the spring constant between points
  * BaselineConstant - This is the spring constant between the point and the baseline
  * Damping - Used to make the water look more realistic
  * mass - The mass of each point
  * pointsNumber - The number of points in the system

#To run:
  1. Install pygame
  2. Run SimpleWater.py
