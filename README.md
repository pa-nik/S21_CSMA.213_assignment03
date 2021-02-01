### S21_CSMA.213 assignment03

This week's assignment deals with genetic algorithms.  The first few questions ask you to perform **crossover** and **mutation** operations similar to what we discussed in class (you can also use Chapter 4 of *Grokking Artificial Intelligence Algorithms* for reference):

Let's assume that the following 2 individuals were chosen out of a population of binary encoded chromosomes that are each 56 bits in length (grouped in 8 bits for readability):

`01000111 01000101 01001110 | 01000111 01010010 | 01001001 01000010`

`11010000 01010010 01001111 | 01000101 01010010 | 01000001 01001101`

**Q1.** [1 point] With crossover points indicated by the ` | ` character, generate 2 offspring of these individuals using **two-point crossover**, starting from the top left of the first parent to begin the chromosome of the first child.

To do this step, simply copy and paste appropriate  sequences from the individual chromosomes above into a new text file, generating 2 new binary encoded strings that are 56 genes (or bits) each.

**Q2.** [1 point] Peform a **bit-string mutation** of the offspring generated in Q1, mutatiing the LSB (least significant bit) of the first child's chromosome and MSB (most signifcant bit) of the second child's (you can look up [Bit Numbering](https://en.wikipedia.org/wiki/Bit_numbering) if confused by the terminology).

Add the 2 new offspring chromosome sequences to the text file you started above.

**Q3.** [1 point] Imagine a different kind of mutation that affects multiple bits of the chromosome using another binary sequence as a bit mask.  Specifically, the bit mask will perform an [exclusive OR](https://en.wikipedia.org/wiki/Exclusive_or) (XOR) operation by fliping any bit that matches a 1 on the mask and copying any bit that matches a 0.

Use the following binary sequence as a mask and apply it to the first child produced in Q2, adding the result to the text file.

`00000000  00000000  00000000  00000000  00000110  00000000  00000000`

**Q4.** [2 points] Let's assume the binary encoded chromosomes you generated represent characters of a string.  Convert the binary codes of the chromosomes (use the first child mutated in Q3 and the second child from Q2) into strings by looking up ASCII codes for each 8 bits of the chromosome sequence.

You can do this step by converting 8-bit binary sequences into decimal numbers first, then looking them up in an [ASCII Table](https://www.rapidtables.com/code/text/ascii-table.html). For example, if the first 8 bits of a sequence are `01000001`, this corresponds to the decimal value `65` and ASCII character `'A'` (note that you can type in the fields above **Dec** or **Char** columns of the ASCII Table to jump to the corresponding table row)

After you convert one 8-bit sequence into a character, move on to the next 8-bit sequence.  At the end of the process you should be able to convert the binary data of each chromosome into a 7-character sring. Add the strings you generated to the text file. 

---


For the second part of the assignment, you will work with the Pandas library objects and methods to help structure data for a genetic algorithm implementation of the classic Traveling Salesman Problem (TSP):

**Q5.** [1 point] Given two lists of data with `x` and `y` containing 52 coordinates each, create **pandas series** objects `xds` and `yds` containing these values.  In addition, create a pandas series `nds` that is a sequence of values from 0 to 51 representing cities to be visited by the traveling salesman (["Introducing Pandas Objects"](https://jakevdp.github.io/PythonDataScienceHandbook/03.01-introducing-pandas-objects.html) is a good reference for getting started with the pandas library)

The lists of coordinates are provided in the code template file `tsp_template.py`, available in this repository.  Note that this file will utilize `tsp_ga.py` as a module incorporating the genetic algorithm implementation that will help evolve a solution to the TSP problem.

**Q6.** [1 point] Construct a **pandas dataframe** object `tsp_data` that will incorporate `nds`, `xds`, and `yds` series as columns of a table labeled `city`, `x` and `y` in order (you may find it useful to looks up how to [create a dataframe from Pandas series](https://www.geeksforgeeks.org/creating-a-dataframe-from-pandas-series/)).  The head (first 5 rows) of your dataframe should like the following, if constructed correctly:

```
   city      x      y
0     0  565.0  575.0
1     1   25.0  185.0
2     2  345.0  750.0
3     3  945.0  685.0
4     4  845.0  655.0
```

**Q7.** [2 points] Uncomment the code that begins with the line 29, which will create the `TSPGA` object and run the genetic algorithm on `tsp_data` using parameters specified in `tsp_ga` instance.

Next, create a matplotlib simple line plot that graphs the list of all distances stored in `distanceList` with distances (distanceList items) plotted on the y-axis and iterations (distanceList item indexes) plotted on the x-axis (you can refer to [Simple Line Plots](https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html) from the *Python Data Science Handbook*)

Figure out how to set the default plot line color to solid green.  Finally, add the title "Traveling Salesman" to the plot, as well as the x-label "Iteration" and y-label "Distance" to complete it.  Plot the resulting graph and save the generated image to submit with this assignment.

**Q8.** [1 point] Look through the file `tsp_ga.py` and figure out how to print the best tour (shortest path) produced by the genetic algorithm after it is run.  

[Extra credit] Programmatically save the results of the best tour into a text file (figure out how to walk through the best tour and write each distance value one by one, separated by spaces or commas) to submit with this assignment.

Good luck!

