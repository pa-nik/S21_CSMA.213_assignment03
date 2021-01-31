### S21_CSMA.213 assignment03

This week's assignment deals with genetic algorithms.  The first few questions ask you to perform **crossover** and **mutation** operations similar to what we discussed in class (you can also use Chapter 4 of *Grokking Artificial Intelligence Algorithms* for reference).

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

**Q4.** [1 point] Let's assume the binary encoded chromosomes you generated represent characters of a string.  Convert the binary codes of the chromosomes (use the first child mutated in Q3 and the second child from Q2) into strings by looking up ASCII codes for each 8 bits of the chromosome sequence.

You can do this step by converting 8-bit binary sequences into decimal numbers first, then looking them up in an [ASCII Table](https://www.rapidtables.com/code/text/ascii-table.html). For example, if the first 8 bits of a sequence are `01000001`, this corresponds to the decimal value `65` and ASCII character `'A'` (note that you can type in the fields above **Dec** or **Char** columns above to jump to the correct row)

After you convert one 8-bit sequence into a character, move on to the next 8-bit sequence.  At the end of the process you should be able to convert the binary data of each chromosome into a 7-character sring. Add the strings you generated to the text file. 

