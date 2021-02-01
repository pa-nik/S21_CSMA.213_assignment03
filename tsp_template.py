import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# template code for Q5 - Q8 of assignment03

# Lists of x and y coordinates:
x = [
    565.0, 25.0, 345.0, 945.0, 845.0, 880.0, 25.0, 525.0, 580.0, 650.0, 
    1605.0, 1220.0, 1465.0, 1530.0, 845.0, 725.0, 145.0, 415.0, 510.0, 560.0, 
    300.0, 520.0, 480.0, 835.0, 975.0, 1215.0, 1320.0, 1250.0, 660.0, 410.0, 
    420.0, 575.0, 1150.0, 700.0, 685.0, 685.0, 770.0, 795.0, 720.0, 760.0, 475.0, 
    95.0, 875.0, 700.0, 555.0, 830.0, 1170.0, 830.0, 605.0, 595.0, 1340.0, 1740.0
]

y = [
    575.0, 185.0, 750.0, 685.0, 655.0, 660.0, 230.0, 1000.0, 1175.0, 1130.0, 
    620.0, 580.0, 200.0, 5.0, 680.0, 370.0, 665.0, 635.0, 875.0, 365.0, 465.0, 
    585.0, 415.0, 625.0, 580.0, 245.0, 315.0, 400.0, 180.0, 250.0, 555.0, 665.0, 
    1160.0, 580.0, 595.0, 610.0, 610.0, 645.0, 635.0, 650.0, 960.0, 260.0, 920.0, 
    500.0, 815.0, 485.0, 65.0, 610.0, 625.0, 360.0, 725.0, 245.0
]

# Q5: create pandas series nds, xds, yds (see assignment instructions)
# insert your Q5 code here..

# Q6: create a pandas dataframe tsp_data using nds, xds and yds as columns labeled 'city', 'x', 'y'
# insert your Q6 code here..

# uncomment below to run the genetic algorithm (provided tsp_data is properly constructed)
'''
from tsp_ga import TSPGA

tsp_ga = TSPGA(
    generation = 100,  
    population_size = 250, 
    retain_rate = 0.4, 
    mutate_rate = 0.3
)
tsp_ga.fit(tsp_data)  # run the genetic algorithm


# Q7: add code to print out the "best tour" evolved by the algorithm 
# insert your Q7 code here..

# the list of distances evolved by the genetic algorithm:
distanceList = [ g.dist for g in tsp_ga.generation_history ] 

# Q8: add code to plot number of iterations (values from 1 to length of distanceList) 
# horizontally and distances (values in distanceList) vertically, using a solid green line 
# insert your Q8 code here..

'''