# TODO:
# format design
# vector calculation
# components
# 2x2 input slide withing matrix_frame
# single matrix with respective functions input
# other functionality
# enable float datatypes, and return values of functions should all return rounded in format .2f



# imports
import customtkinter as ctk
import CTkMessagebox as ctkmb
import Main



# GLOBALS

iA11 : int = 0
iA12 : int = 0
iA13 : int = 0
iA21 : int = 0
iA22 : int = 0
iA23 : int = 0
iA31 : int = 0
iA32 : int = 0
iA33 : int = 0

iB11 : int = 0
iB12 : int = 0
iB13 : int = 0
iB21 : int = 0
iB22 : int = 0
iB23 : int = 0
iB31 : int = 0
iB32 : int = 0
iB33 : int = 0

matrix_a : list[list[int]] =[
                                [iA11, iA12, iA13],
                                [iA21, iA22, iA23],
                                [iA31, iA32, iA33]
                            ]

matrix_b : list[list[int]] =[
                                [iB11, iB12, iB13],
                                [iB21, iB22, iB23],
                                [iB31, iB32, iB33]
                            ]

sOutput : str = ""

class Gui() : 
    
    # inheritance
    def __init__(self, root) -> None:
        self.root = root
         
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    # When the user closes the GUI window, the on_closing method is triggered, 
    # which destroys the window and stops the execution of the code
    # this could be seen as a memory leak?
    
    # closing
    def on_closing(self) : 
        
        self.root.destroy()
        quit()
    
    # clears all entries in the matrix panel
    def button_clear() -> None :
        
        """
        Defines the function of clearing all boxes for the matrixes, \n
        will be used to initialise the command = button_clear for button_clear_matrixes
        """
        
        A_R1C1.delete(0, 1000)
        A_R1C1.insert(0,"0")
        
        A_R1C2.delete(0, 1000)
        A_R1C2.insert(0,"0")
        
        A_R1C3.delete(0, 1000)
        A_R1C3.insert(0,"0")
        
        
        A_R2C1.delete(0, 1000)
        A_R2C1.insert(0,"0")
        
        A_R2C2.delete(0, 1000)
        A_R2C2.insert(0,"0")
        
        A_R2C3.delete(0, 1000)
        A_R2C3.insert(0,"0")
        
        
        A_R3C1.delete(0, 1000)
        A_R3C1.insert(0,"0")
        
        A_R3C2.delete(0, 1000)
        A_R3C2.insert(0,"0")
        
        A_R3C3.delete(0, 1000)
        A_R3C3.insert(0,"0")
        
        
        
        B_R1C1.delete(0, 1000)
        B_R1C1.insert(0,"0")
        
        B_R1C2.delete(0, 1000)
        B_R1C2.insert(0,"0")
        
        B_R1C3.delete(0, 1000)
        B_R1C3.insert(0,"0")
        
        
        B_R2C1.delete(0, 1000)
        B_R2C1.insert(0,"0")
        
        B_R2C2.delete(0, 1000)
        B_R2C2.insert(0,"0")
        
        B_R2C3.delete(0, 1000)
        B_R2C3.insert(0,"0")
        
        
        B_R3C1.delete(0, 1000)
        B_R3C1.insert(0,"0")
        
        B_R3C2.delete(0, 1000)
        B_R3C2.insert(0,"0")
        
        B_R3C3.delete(0, 1000)
        B_R3C3.insert(0,"0")
        
        global iA11
        iA11 = 0
        
        global iA12
        iA12 = 0
        
        global iA13
        iA13 = 0
        
        global iA21
        iA21 = 0
        
        global iA22
        iA22 = 0
        
        global iA23
        iA23 = 0
        
        global iA31
        iA31 = 0
        
        global iA32
        iA32 = 0
        
        global iA33
        iA33 = 0


        global iB11
        iB11 = 0
        
        global iB12
        iB12 = 0
        
        global iB13
        iB13 = 0
        
        global iB21
        iB21 = 0
        
        global iB22
        iB22 = 0
        
        global iB23
        iB23 = 0
        
        global iB31
        iB31 = 0
        
        global iB32
        iB32 = 0
        
        global iB33
        iB33 = 0
        
        btnAddition._state = "disabled"
        btnSubtraction._state = "disabled"
        btnDeterminantA._state = "disabled"
        btnDeterminantB._state = "disabled"
        btnPower._state = "disabled"
        btnMultiplication._state = "disabled"
        
        btnAddition.configure(fg_color = "grey15")
        btnSubtraction.configure(fg_color = "grey15")
        btnDeterminantA.configure(fg_color = "grey15")
        btnDeterminantB.configure(fg_color = "grey15")
        btnPower.configure(fg_color = "grey15")
        btnMultiplication.configure(fg_color = "grey15")

    # backend function
    def user_input_matrix_a() -> None :
        
        """
        Allows the user to input the first matrix that calculations will be done on.
        
        Returns:
            list[list[int]] : Returns a 3 Dimensional matrix of type integer
        """

        global matrix_a
    
        matrix_a  = [
                    [iA11,
                     iA12,
                     iA13],
                    [iA21,
                     iA22,
                     iA23],
                    [iA31,
                     iA32,
                     iA33],
                    ]
    
    # backend function
    def user_input_matrix_b() -> None : 
    
        """
        Allows the user to input the second matrix that calculations will be done on.

        Returns:
            list[list[int]] : Returns a 3 Dimensional matrix of type integer
        """
    
        global matrix_b
    
        matrix_b  = [
                    [iB11,
                     iB12,
                     iB13],
                    [iB21,
                     iB22,
                     iB23],
                    [iB31,
                     iB32,
                     iB33],
                    ]

    # backend function relies on user input in the matrix panel
    def store() -> None :
        
        # A
        
        global iA11
        iA11 = A_R1C1.get()
        
        try :
            
            iA11 = int(iA11)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            A_R1C1.focus()
            print(f"Error data type : {VE}")
            return
        
        global iA12
        iA12 = A_R1C2.get()
        
        try :
            
            iA12 = int(iA12)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            A_R1C2.focus()
            print(f"Error data type : {VE}")
            return
        
        global iA13
        iA13 = A_R1C3.get()
        
        try :
            
            iA13 = int(iA13)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            A_R1C3.focus()
            print(f"Error data type : {VE}")
            return
        
        global iA21
        iA21 = A_R2C1.get()
        
        try :
            
            iA21 = int(iA21)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            A_R2C1.focus()
            print(f"Error data type : {VE}")
            return
        
        global iA22
        iA22 = A_R2C2.get()
        
        try :
            
            iA22 = int(iA22)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            A_R2C2.focus()
            print(f"Error data type : {VE}")
            return
        
        global iA23
        iA23 = A_R2C3.get()
        
        try :
            
            iA23 = int(iA23)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            A_R2C3.focus()
            print(f"Error data type : {VE}")
            return
        
        global iA31
        iA31 = A_R3C1.get()
        
        try :
            
            iA31 = int(iA31)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            A_R3C1.focus()
            print(f"Error data type : {VE}")
            return
        
        global iA32
        iA32 = A_R3C2.get()
        
        try :
            
            iA32 = int(iA32)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            A_R3C2.focus()
            print(f"Error data type : {VE}")
            return

        global iA33
        iA33 = A_R3C3.get()
        
        try :
            
            iA33 = int(iA33)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            A_R3C3.focus()
            print(f"Error data type : {VE}")
            return
        
        
        
        # B
        
        global iB11
        iB11 = B_R1C1.get()
        
        try :
            
            iB11 = int(iB11)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            B_R1C1.focus()
            print(f"Error data type : {VE}")
            return
        
        global iB12
        iB12 = B_R1C2.get()
        
        try :
            
            iB12 = int(iB12)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            B_R1C2.focus()
            print(f"Error data type : {VE}")
            return
        
        global iB13
        iB13 = B_R1C3.get()
        
        try :
            
            iB13 = int(iB13)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            B_R1C3.focus()
            print(f"Error data type : {VE}")
            return
        
        global iB21
        iB21 = B_R2C1.get()
        
        try :
            
            iB21 = int(iB21)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            B_R2C1.focus()
            print(f"Error data type : {VE}")
            return
        
        global iB22
        iB22 = B_R2C2.get()
        
        try :
            
            iB22 = int(iB22)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            B_R2C2.focus()
            print(f"Error data type : {VE}")
            return
        
        global iB23
        iB23 = B_R2C3.get()
        
        try :
            
            iB23 = int(iB23)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            B_R2C3.focus()
            print(f"Error data type : {VE}")
            return
        
        global iB31
        iB31 = B_R3C1.get()
        
        try :
            
            iB31 = int(iB31)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            B_R3C1.focus()
            print(f"Error data type : {VE}")
            return
        
        global iB32
        iB32 = B_R3C2.get()
        
        try :
            
            iB32 = int(iB32)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            B_R3C2.focus()
            print(f"Error data type : {VE}")
            return

        global iB33
        iB33 = B_R3C3.get()
        
        try :
            
            iB33 = int(iB33)
            
        except ValueError as VE :
            
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers", option_1= "OK", justify = "center", option_focus = 1)
            B_R3C3.focus()
            print(f"Error data type : {VE}")
            return
        
        Gui.user_input_matrix_a()
        Gui.user_input_matrix_b()
        
        btnAddition._state = "enabled"
        btnSubtraction._state = "enabled"
        btnDeterminantA._state = "enabled"
        btnDeterminantB._state = "enabled"
        btnPower._state = "enabled"
        btnMultiplication._state = "enabled"
        
        btnAddition.configure(fg_color = "dodgerblue4")
        btnSubtraction.configure(fg_color = "dodgerblue4")
        btnDeterminantA.configure(fg_color = "dodgerblue4")
        btnDeterminantB.configure(fg_color = "dodgerblue4")
        btnPower.configure(fg_color = "dodgerblue4")
        btnMultiplication.configure(fg_color = "dodgerblue4")

    # front end function
    def Output(matrix_type : list[list[str]] = list[list[str]]) -> None :

        """
        Outputs an input of type list[list[str]] to the Output ctk.Output
        """

        EntryOutput.delete("1.0", "1000.0")
        EntryOutput.insert("1.0", f"\n\n\n{Main.main.convert_matrix_to_string(matrix_type)}")
    
    # front end function
    def OutAny(x : any = any) -> None :
        
        """
        Outputs any given data into the output box
        """
        
        try :
            x : str = str(x)
            
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "A conversion error has occured.{VE}", option_1= "OK", justify = "center", option_focus = 1)
            print(f"A conversion error has occurred, {VE}")
            return

        x : str = str(x)
        
        EntryOutput.delete("1.0","1000.0")
        EntryOutput.insert("1.0", x)
    
    # front end function of the Main.Advanced.Power() function
    def Power() -> None :
        
        AorB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "Matrix Power",icon = "info", message = "Please select matrix A or B to perform calculation", option_1= "A", option_2= "B", justify = "center")
        
        choice : str = AorB.get()
        
        if choice == "A" :
            
            dialog = ctk.CTkInputDialog(title = "Matrix Power", text = "Please enter the power value, an integer")
            power : int = (dialog.get_input())
            
            try :
                power = int(power)
                
            except ValueError as VE :
                ErrorMB = ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = f"Please enter an integer.{VE}", option_1= "OK", justify = "center", option_focus = 1)
                return
                
            print(power)
                
            if power or power == 0:
                
                Gui.Output(Main.Advanced.Power(matrix_a, power))
            
            
            
        if choice == "B" :
            
            dialog = ctk.CTkInputDialog(title = "Matrix Power", text = "Please enter the power value, an integer")
            power : int = (dialog.get_input())
            
            try :
                power = int(power)
                
            except ValueError as VE :
                ErrorMB = ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = f"Please enter an integer.{VE}", option_1= "OK", justify = "center", option_focus = 1)
                return
            
            if power or power == 0:
                
                Gui.Output(Main.Advanced.Power(matrix_b, power))

"""
# GUI is relatively scalable, but poorly implemented
# disabled for debugging
# root.resizable(width = False, height = False)
"""

# system config

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")



# root window

root = ctk.CTk()
root.geometry("1100x640")
root.title("Matrix Calculator")



# fonts

# custom font for buttons
cfontbtn = ctk.CTkFont("capilary", 18, weight = "bold")

# custom font for inputs of matrix variables
cfont = ctk.CTkFont("capilary", 16, weight = "bold")

# custom font for labels
cfontmlabel = ctk.CTkFont("capilary", 20, weight = "bold")


# root frame

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=8)
root.grid_rowconfigure(0, weight=1)



# frame for main components

main_frame = ctk.CTkFrame(master = root, corner_radius = 25)
main_frame.grid(row = 0, column = 1, sticky = "nesw", padx = 30, pady = 25)



# columns

main_frame.grid_columnconfigure(1, weight = 1, pad = 40)
main_frame.grid_columnconfigure(2, weight = 3, pad = 40)
main_frame.grid_columnconfigure(3, weight = 3, pad = 40)



# rows

main_frame.grid_rowconfigure(1, weight = 1, pad = 30)
main_frame.grid_rowconfigure(2, weight = 1, pad = 30)
main_frame.grid_rowconfigure(3, weight = 1, pad = 30)
main_frame.grid_rowconfigure(4, weight = 1, pad = 30)
main_frame.grid_rowconfigure(5, weight = 1, pad = 30)
main_frame.grid_rowconfigure(6, weight = 1, pad = 30)
main_frame.grid_rowconfigure(7, weight = 1, pad = 30)

# main buttons



btnAddition = ctk.CTkButton(master = main_frame, corner_radius = 12, font = cfontbtn, text = "Addition", fg_color = "dodgerblue4", command = lambda : Gui.Output(Main.main.addition_a_b(matrix_a, matrix_b)))
btnAddition.grid(row = 1, column = 1, sticky = "nesw", padx = 35, pady = 20)
# btnAddition._state = "disabled"

btnSubtraction = ctk.CTkButton(master = main_frame, corner_radius = 12, font = cfontbtn, text = "Subtraction", fg_color = "dodgerblue4", command = lambda : Gui.Output(Main.main.subtraction_a_b(matrix_a, matrix_b)))
btnSubtraction.grid(row = 2, column = 1, sticky = "nesw", padx = 35, pady = 20)
# btnSubtraction._state = "disabled"

btnMultiplication = ctk.CTkButton(master = main_frame, corner_radius = 12, font = cfontbtn, text = "Multiplication", fg_color = "dodgerblue4", command = lambda : Gui.Output(Main.main.multiplication_ab(matrix_a, matrix_b)))
btnMultiplication.grid(row = 3, column = 1, sticky = "nesw", padx = 35, pady = 20)
# btnMultiplication._state = "disabled"

btnPower = ctk.CTkButton(master = main_frame, corner_radius = 12, font = cfontbtn, text = "Power", fg_color = "dodgerblue4", command = lambda : Gui.Power())
btnPower.grid(row = 4, column = 1, sticky = "nesw", padx = 35, pady = 20)
# btnPower._state = "disabled"

btnDeterminantA = ctk.CTkButton(master = main_frame, corner_radius = 12, font = cfontbtn, text = "Determinant of A", fg_color = "dodgerblue4", command = lambda : Gui.OutAny(Main.Advanced.Determinant(matrix_a)))
btnDeterminantA.grid(row = 5, column = 1, sticky = "nesw", padx = 35, pady = 20)
# btnDeterminantA._state = "disabled"

btnDeterminantB = ctk.CTkButton(master = main_frame, corner_radius = 12, font = cfontbtn, text = "Determinant of B", fg_color = "dodgerblue4", command = lambda : Gui.OutAny(Main.Advanced.Determinant(matrix_b)))
btnDeterminantB.grid(row = 6, column = 1, sticky = "nesw", padx = 35, pady = 20)
# btnDeterminantB._state = "disabled"

# btnCalculateVectors = ctk.CTkButton(master = main_frame, corner_radius = 12, font = cfontbtn, text = "Calculate components")
# btnCalculateVectors.grid(row = 7, column = 1, sticky = "nesw", padx = 35, pady = 20)

# output

# change row to 3 and rowspan to 3 when redoing GUI
EntryOutput = ctk.CTkTextbox(master = main_frame, font = ctk.CTkFont("capilary", 28, "bold"), corner_radius = 10)
EntryOutput.grid(column = 2, row = 2, rowspan = 4, sticky = "nsew")



# for the frame where matrixes will be placed

# frame create

frame_matrix = ctk.CTkFrame(master = root, width = 300,height = 580 , corner_radius = 0)
frame_matrix.grid(row = 0, column = 0, rowspan = 4, sticky = "nswe")



# columns
    
frame_matrix.grid_columnconfigure(0, weight = 1)
    
  
    
# rows
    
frame_matrix.grid_rowconfigure(0, weight = 2, pad = 40)
frame_matrix.grid_rowconfigure(1, weight = 1)
frame_matrix.grid_rowconfigure(2, weight = 4, pad = 80)
frame_matrix.grid_rowconfigure(3, weight = 3)
frame_matrix.grid_rowconfigure(4, weight = 1)
frame_matrix.grid_rowconfigure(5, weight = 1)
frame_matrix.grid_rowconfigure(6, weight = 1)
frame_matrix.grid_rowconfigure(7, weight = 4, pad = 80)
frame_matrix.grid_rowconfigure(8, weight = 1)
frame_matrix.grid_rowconfigure(9, weight = 1)
frame_matrix.grid_rowconfigure(10, weight = 0)   
    
    
    
# label Matrix A
    
matrix_label_a = ctk.CTkLabel(master = frame_matrix, text = "Matrix A", font = cfontmlabel)
matrix_label_a.grid(row = 0, column = 0, sticky = "we")
    
    
    
# frame For A
    
frame_a = ctk.CTkFrame(master = frame_matrix, width = 160, height = 160, corner_radius = 10)
frame_a.grid(row = 2, column = 0, sticky = "nesw", padx = 15, pady = 15)
    
    
    
# row and column configuration A
    
frame_a.grid_rowconfigure(0, weight = 1)
frame_a.grid_rowconfigure(1, weight = 1)
frame_a.grid_rowconfigure(2, weight = 1)
    
frame_a.grid_columnconfigure(0, weight = 1)
frame_a.grid_columnconfigure(1, weight = 1)
frame_a.grid_columnconfigure(2, weight = 1)
    
A_R1C1 = ctk.CTkEntry(master = frame_a, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R1C1.grid(row = 0, column = 0, padx = 5, pady = 10)
    
A_R1C2 = ctk.CTkEntry(master = frame_a, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R1C2.grid(row = 0, column = 1, padx = 5, pady = 5)
    
A_R1C3 = ctk.CTkEntry(master = frame_a, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R1C3.grid(row = 0, column = 2, padx = 5, pady = 5)
    
    
A_R2C1 = ctk.CTkEntry(master = frame_a, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R2C1.grid(row = 1, column = 0, padx = 5, pady = 5)
    
A_R2C2 = ctk.CTkEntry(master = frame_a, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R2C2.grid(row = 1, column = 1, padx = 5, pady = 5)
    
A_R2C3 = ctk.CTkEntry(master = frame_a, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R2C3.grid(row = 1, column = 2, padx = 5, pady = 5)
    
    
A_R3C1 = ctk.CTkEntry(master = frame_a, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R3C1.grid(row = 2, column = 0, padx = 5, pady = 10)
    
A_R3C2 = ctk.CTkEntry(master = frame_a, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R3C2.grid(row = 2, column = 1, padx = 5, pady = 5)
    
A_R3C3 = ctk.CTkEntry(master = frame_a, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R3C3.grid(row = 2, column = 2, padx = 5, pady = 5)
    
    
    
# label Matrix B
    
matrix_label_b = ctk.CTkLabel(master = frame_matrix, text = "Matrix B", font = cfontmlabel)
matrix_label_b.grid(row = 6, column = 0, sticky = "wne")
    
    
    
# frame For B
    
frame_b = ctk.CTkFrame(master = frame_matrix, width = 160, height = 160, corner_radius = 10)
frame_b.grid(row = 7, column = 0, sticky = "nesw", padx = 15, pady = 25)    



# row and column configuration B

frame_b.grid_rowconfigure(0, weight = 1)
frame_b.grid_rowconfigure(1, weight = 1)
frame_b.grid_rowconfigure(2, weight = 1)

frame_b.grid_columnconfigure(0, weight = 1)
frame_b.grid_columnconfigure(1, weight = 1)
frame_b.grid_columnconfigure(2, weight = 1)
    
B_R1C1 = ctk.CTkEntry(master = frame_b, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R1C1.grid(row = 0, column = 0, padx = 5, pady = 10)

B_R1C2 = ctk.CTkEntry(master = frame_b, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R1C2.grid(row = 0, column = 1, padx = 5, pady = 5)

B_R1C3 = ctk.CTkEntry(master = frame_b, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R1C3.grid(row = 0, column = 2, padx = 5, pady = 5)


B_R2C1 = ctk.CTkEntry(master = frame_b, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R2C1.grid(row = 1, column = 0, padx = 5, pady = 5)

B_R2C2 = ctk.CTkEntry(master = frame_b, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R2C2.grid(row = 1, column = 1, padx = 5, pady = 5)

B_R2C3 = ctk.CTkEntry(master = frame_b, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R2C3.grid(row = 1, column = 2, padx = 5, pady = 5)


B_R3C1 = ctk.CTkEntry(master = frame_b, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R3C1.grid(row = 2, column = 0, padx = 5, pady = 10)
    
B_R3C2 = ctk.CTkEntry(master = frame_b, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R3C2.grid(row = 2, column = 1, padx = 5, pady = 5)

B_R3C3 = ctk.CTkEntry(master = frame_b, placeholder_text = "0", corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R3C3.grid(row = 2, column = 2, padx = 5, pady = 5)



# button store
    
button_store_matrixes = ctk.CTkButton(master = frame_matrix, text = "Store", height = 50, fg_color = "dodgerblue4", command = lambda : Gui.store())
button_store_matrixes.grid(row = 8, column = 0, sticky = "nesw", padx = 15, pady = 10)



# button clear
    
button_clear_matrixes = ctk.CTkButton(master = frame_matrix, text = "Clear", fg_color = "dodgerblue4", command = lambda : Gui.button_clear(), height = 35)
button_clear_matrixes.grid(row = 9, column = 0, sticky = "nesw", padx = 15, pady = 15)

# Gui.user_input_int_only(1)

root.mainloop()