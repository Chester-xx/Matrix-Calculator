// Running the program with python

If you want to run the program using python, run GUI.py and ensure Main.py is in the same directory
Note that python needs to be installed along with customtkinter and CTkMessagebox using command prompt
to install them with the below commands :
pip install customtkinter
pip install CTkMessagebox

// Matrix Calculator.exe

I've compiled the program into an executable using PyInstaller.
The executable should be able to run on its own without installing anything.

// Other

The current functionality only supports 3x3 matrices and i plan on adding support for 2x2 matrices
and singular matrices for individual calculations.

The program may be buggy as it is my first open project and some functionality may not fully support
certain actions. The datatypes currently only support integer values which exlude numbers with rational
and irrational values such as : 1.23. But does support neegative numbers.

The GUI is a work in progress and does need to be changed as it feels clunky and does not fully support
the layout that it was designed to be implemented as.

// Controls

When opening the application, to use the calculation buttons you will need to enter in matrices A and B
and click store. It unfortunately doesnt support single matrix calculations as of yet so if you are working
on a single matrix, both A and B need to be filled in with some type of placeholder but the buttons such as
power and determinants are independant for A or B.

// Output

The current output panel is not ideal and needs to be fixed, but it works atleast.

// Features to soon be covered

Float data types
Component calculations
2x2 matrices
GUI support for single matrix input for 2x2 and 3x3 matrixes
Inverse operations
Transpose operations
