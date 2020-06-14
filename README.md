## Newell-Littlewood Coefficient Calculator

This python code is used to calculate Newell-Littlewood Coefficients.

#### Credit

This code uses Dr. Anders Buch's Littlewood-Richardson Calculator as a subroutine. For further information, please visit https://sites.math.rutgers.edu/~asbuch/lrcalc/

 

#### Prerequisites

- Python 3

  ```bash
  sudo apt install python3
  ```

- Littlewood-Richardson Calculator

  Visit https://sites.math.rutgers.edu/~asbuch/lrcalc/ for instructions.

#### Usage

1. Create a file in THIS repository and write the input to the file. The input should follow this format:
   $$
   \begin{align}
   &4\ 2\ 1\\
   &3\ 2\ 2\ 1\\
   &6\ 2
   \end{align}
   $$

2. Run this line of code:

   ```bash
   python3 main.py FILENAME
   ```

   where FILENAME is the name of your input file.

3. The result will be printed to `stdout`.

#### Disclaimer

- This algorithm is very, very inefficient.
- I have not tested the programme, since I do not have any test cases. So, the output might not be correct. Please notify me if you find an error.
- This programme is written solely for the computation of Newell-Littilewood Coefficients. It does not reflect the author's programming skills or coding style for a "serious" software project.