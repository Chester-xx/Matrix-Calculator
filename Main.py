# TODO:
#Format design
# vector calculation
# components
# 2x2 input slide withing matrix_frame
# single matrix with respective functions input
# other functionality
# enable float datatypes, and return values of functions should all return rounded in format .2f


#scripts are not called anywhere so running the program will not output anything
#just makes up functionality of a module

# imports
# from Basic_calculations import *
# from Advanced_calculations import *



class main():

    # inheritancee
    def __init__(self, name) -> None:
        self.name = name
    
    # Console Specific
    def display_matrix_a(matrix_a : list[list[int]] = list[list[int]]) -> None :
        
        """
        User enters a matrix of type list[list[int]] and will print it out into the console
        This is specific to matrix A that will be used for calculations
        """
        
        print(f"Matrix A : ")
        
        for r in range(0,3) :
            
            substr : str = ""
            
            for c in range(0,3) : 
                
                substr += str(matrix_a[r][c]) + "\t"
                
            print(f"{substr}")
            
        print(f"\n")

    # Console Specific
    def display_matrix_b(matrix_b : list[list[int]] = list[list[int]]) -> None :
        
        """
        User enters a matrix of type list[list[int]] and will print it out into the console
        This is specific to matrix B that will be used for calculations
        """

        print(f"Matrix B : ")
        
        for r in range(0,3) :
            
            substr : str = ""
            
            for c in range(0,3) : 
                
                substr += str(matrix_b[r][c]) + "\t"
                
            print(f"{substr}")
            
        print(f"\n")
    
    # GUI Function  
    def addition_a_b(matrix_a : list[list[int]] = list[list[int]], matrix_b : list[list[int]] = list[list[int]]) -> list[list[int]] : 
        
        """
        User enters matrix A and B of types list[list[int]] and will return the result addition \n
        of the matrices as type list[list[int]] \n
        """
        
        print(f"Resultant of adding matrix A & B : ")
        
        result : list[list[int]] = [
                                    [0,0,0],
                                    [0,0,0],
                                    [0,0,0],
                                   ]
        
        for r in range(0,3) :
            
            for c in range(0,3) :
                
                result[r][c] = int(matrix_a[r][c]) + (matrix_b[r][c])
          
        return result
    
    # GUI Function
    def subtraction_a_b(matrix_a : list[list[int]] = list[list[int]], matrix_b : list[list[int]] = list[list[int]]) -> list[list[int]] :
        
        """
        User enters matrix A and B of types list[list[int]] and will return the result subtraction \n
        of the matrices as type list[list[int]] \n
        """
        
        print(f"Resultant of subtracting matrix A & B : ")
        
        result : list[list[int]] = [
                                    [0,0,0],
                                    [0,0,0],
                                    [0,0,0],
                                   ]
        
        for r in range(0,3) :
            
            for c in range(0,3) :
                
                result[r][c] = matrix_a[r][c] - matrix_b[r][c]
          
        return result
        
    # GUI Function
    def multiplication_ab(matrix_a : list[list[int]] = list[list[int]], matrix_b : list[list[int]] = list[list[int]]) -> list[list[int]] : 
        
        """
        User enters matrix A and B of types list[list[int]] and will return the result multiplication \n
        of the matrices as type list[list[int]] \n
        """
        
        print(f"Resultant of multiplying matrix A & B : ")
        
        result : list[list[int]] = [
                                    [0,0,0],
                                    [0,0,0],
                                    [0,0,0],
                                   ]
        
        for i in range(0,3):
    
            for r in range (0,3): #for rows of multiplicand
    
                substr : int = 0
    
                for c in range(0,3): #for columns of multiplier
        
                    substr += matrix_a[i][c] * matrix_b[c][r]
    
                result[i][r] += substr
        
        return result
    
    # Console Specific
    def display_matrix_any(matrix_type : list[list[int]] = list[list[int]]) -> None : 
        
        """
        User enters a  3 dimensional matrix as type list[list[int]] and the function 
        will print out the matrix into the console \n
        DOES NOT return a value, only prints it to the console
        """
        
        for r in range(0,3) : 
            
            substr : str = ""
            
            for c in range(0,3) : 
                
                substr += str(matrix_type[r][c]) + "\t"
                
            print(f"{substr}")
            
        print(f"\n")
    
    # GUI or Console Specific
    def convert_matrix_to_string(matrix_any : list[list[int]] = list[list[int]]) -> str :
        
        # can be used to format output with GUI.Outany but is not necessary 
        
        """
        User enters a 3 dimensional matrix of type list[list[int]] /n
        Function will return the matrix in a format of \n
        \n
        x \t y \t z\n
        a \t b \t c\n
        i \t r \t c\n
        
        """
        
        mainstr : str = ""
        
        for r in range(0,3) :
            
            substr : str = ""
            
            for c in range(0,3) : 
                
                substr += str(matrix_any[r][c]) + "\t"

            mainstr += substr + "\n"
            
        return mainstr
    
    # Console Specific
    def user_input_matrix_any() -> list[list[int]] :
        
        """
        User will enter a 3 dimensional matrix of type list[list[int]] \n
        and will return the matrix as type list[list[int]]
        
        """

        print(f"Matrix Z : \n")

        matrix_x : list[list[int]] =[
                                    [int(input("Enter R1C1 of Matrix : ")),
                                     int(input("Enter R1C2 of Matrix : ")),
                                     int(input("Enter R1C3 of Matrix : "))],
                                    [int(input("Enter R2C1 of Matrix : ")),
                                     int(input("Enter R2C2 of Matrix : ")),
                                     int(input("Enter R2C3 of Matrix : "))],
                                    [int(input("Enter R3C1 of Matrix : ")),
                                     int(input("Enter R3C3 of Matrix : ")),
                                     int(input("Enter R3C3 of Matrix : "))],
                                    ]
        
        print(f"\n")
        
        return matrix_x
        
class Advanced(main) :
    
    # inheritance
    def __init__(self, name) -> None:
        super().__init__(name)
    
    # GUI and Console Specific  NB output type importance
    def Determinant(matrix_any : list[list[int]] = list[list[int]]) -> float :
        
        """
        User enters a 3x3 dimensional matrix of data type list[list[int]] and the function will calculate \n
        the determinant of such matrix.\n
        Result: \n
        Outputs determinant value of data type float
        """

        # needs optimisation, not necessarily slow just uses unnecessary allocations
        
        a : list[list[int]] =   [
                                [matrix_any[1][1],matrix_any[1][2]],
                                [matrix_any[2][1],matrix_any[2][2]]
                                ]

        b : list[list[int]] =   [
                                [matrix_any[1][0],matrix_any[1][2]],
                                [matrix_any[2][0],matrix_any[2][2]]
                                ]

        c : list[list[int]] =   [
                                [matrix_any[1][0],matrix_any[1][1]],
                                [matrix_any[2][0],matrix_any[2][1]]
                                ]
        
        Result : float =    matrix_any[0][0] * ((a[0][0] * a[1][1]) - (a[0][1] * a[1][0])) \
                            - matrix_any[0][1] * ((b[0][0] * b[1][1]) - (b[0][1] * b[1][0])) \
                            + matrix_any[0][2] * ((c[0][0] * c[1][1]) - (c[0][1] * c[1][0]))
                           
        
        return Result

    # functionality coming in the future
    def Inverse() :
        pass
    
    # functionality coming in the future
    def Transpose() :
        pass
    
    # GUI and Console Specific, wheen calling in console ensure to output it correctly 
    def Power(matrix_any : list[list[int]] = list[list[int]], x : int = int) -> list[list[int]]:
        
        """
        User will enter a 3 dimensional matrix of type list[list[int]] \n
        The matrix will be raised to the power of the second variable x of type int \n
        \n
        Result : \n
        returns a 3 dimensional matrix of type list[list[int]] that has been calculated by the value of matrix to the power of x
        """

        # identity matrix
        if x == 0 :
            identity : list[list[int]] = [[1,0,0],[0,1,0],[0,0,1]]
            return identity

        # power of itself
        if x == 1 :
            return matrix_any
        
        # loop
        if x >= 2 :
            
            result : list[list[int]] = [[0,0,0],[0,0,0],[0,0,0]]
            process : list[list[str]] = [[1,1,1],[1,1,1],[1,1,1]]
            
            for raised in range(1,x) :
                
                if raised == 1 :
                    
                    for r in range(0,3) :
                    
                        for c in range(0,3) :
                        
                            result[r][c] = matrix_any[r][c]
                
                for i in range(0,3) :

                    for r in range(0,3) :

                        substr : int = 0

                        for c in range(0,3) : 

                            substr += matrix_any[i][c] * result[c][r]

                        process[i][r] = substr

                for r in range(0,3) :
                    
                    for c in range(0,3) :
                        
                        result[r][c] = process[r][c]
                
            return result

"""Testing Code"""
