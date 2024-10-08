# TODO:
# format design
# vector calculation
# components
# 2x2 input slide withing matrix_frame
# single matrix with respective functions input
# other functionality

# imports
import customtkinter as ctk
import CTkMessagebox as ctkmb
import Main

sOutput : str = ""

class Gui() :
    
    # inheritance
    def __init__(self, root) -> None:
        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    # When the user closes the GUI window, the on_closing method is triggered, 
    # which destroys the window and stops the execution of the code
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
        tk_iA11.set(0)
        tk_iA12.set(0)
        tk_iA13.set(0)
        tk_iA21.set(0)
        tk_iA22.set(0)
        tk_iA23.set(0)
        tk_iA31.set(0)
        tk_iA32.set(0)
        tk_iA33.set(0)
        tk_iB11.set(0)
        tk_iB12.set(0)
        tk_iB13.set(0)
        tk_iB21.set(0)
        tk_iB22.set(0)
        tk_iB23.set(0)
        tk_iB31.set(0)
        tk_iB32.set(0)
        tk_iB33.set(0)
        EntryOutput.delete("1.0","1000.0")

    # backend function
    def user_input_matrix_a() -> None :
        """
        Sets global matrix B to user input
        """
        global matrix_a
        matrix_a = [[iA11, iA12, iA13],[iA21, iA22, iA23],[iA31, iA32, iA33],]
    
    # backend function
    def user_input_matrix_b() -> None : 
        """
        Sets global matrix A to user input
        """
        global matrix_b
        matrix_b = [[iB11, iB12, iB13],[iB21, iB22, iB23],[iB31, iB32, iB33],]

    # backend function relies on user input in the matrix panel
    def Store() -> None :
        # A
        global iA11
        iA11 = A_R1C1.get()
        try : iA11 = float(iA11)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            A_R1C1.focus()
            print(f"Error data type : {VE}")
            return
        global iA12
        iA12 = A_R1C2.get()
        try : iA12 = float(iA12)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            A_R1C2.focus()
            print(f"Error data type : {VE}")
            return
        global iA13
        iA13 = A_R1C3.get()
        try : iA13 = float(iA13)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            A_R1C3.focus()
            print(f"Error data type : {VE}")
            return
        global iA21
        iA21 = A_R2C1.get()
        try : iA21 = float(iA21)    
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            A_R2C1.focus()
            print(f"Error data type : {VE}")
            return
        global iA22
        iA22 = A_R2C2.get()
        try : iA22 = float(iA22)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            A_R2C2.focus()
            print(f"Error data type : {VE}")
            return
        global iA23
        iA23 = A_R2C3.get()
        try : iA23 = float(iA23)  
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            A_R2C3.focus()
            print(f"Error data type : {VE}")
            return
        global iA31
        iA31 = A_R3C1.get()
        try : iA31 = float(iA31)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            A_R3C1.focus()
            print(f"Error data type : {VE}")
            return
        global iA32
        iA32 = A_R3C2.get()
        try : iA32 = float(iA32)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            A_R3C2.focus()
            print(f"Error data type : {VE}")
            return
        global iA33
        iA33 = A_R3C3.get()
        try : iA33 = float(iA33)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            A_R3C3.focus()
            print(f"Error data type : {VE}")
            return
        # B
        global iB11
        iB11 = B_R1C1.get()
        try : iB11 = float(iB11)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            B_R1C1.focus()
            print(f"Error data type : {VE}")
            return
        global iB12
        iB12 = B_R1C2.get()
        try : iB12 = float(iB12)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            B_R1C2.focus()
            print(f"Error data type : {VE}")
            return
        global iB13
        iB13 = B_R1C3.get()
        try : iB13 = float(iB13)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            B_R1C3.focus()
            print(f"Error data type : {VE}")
            return
        global iB21
        iB21 = B_R2C1.get()
        try : iB21 = float(iB21)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            B_R2C1.focus()
            print(f"Error data type : {VE}")
            return
        global iB22
        iB22 = B_R2C2.get()
        try : iB22 = float(iB22)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            B_R2C2.focus()
            print(f"Error data type : {VE}")
            return
        global iB23
        iB23 = B_R2C3.get()
        try : iB23 = float(iB23)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            B_R2C3.focus()
            print(f"Error data type : {VE}")
            return
        global iB31
        iB31 = B_R3C1.get()
        try : iB31 = float(iB31)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            B_R3C1.focus()
            print(f"Error data type : {VE}")
            return
        global iB32
        iB32 = B_R3C2.get()
        try : iB32 = float(iB32)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            B_R3C2.focus()
            print(f"Error data type : {VE}")
            return
        global iB33
        iB33 = B_R3C3.get()
        try : iB33 = float(iB33)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "Please ensure there are no empty spaces and all inputs are integers or floats", option_1= "OK", justify = "center", option_focus = 1)
            B_R3C3.focus()
            print(f"Error data type : {VE}")
            return
        Gui.user_input_matrix_a()
        Gui.user_input_matrix_b()

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
        try : x : str = str(x)
        except ValueError as VE :
            ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = "A conversion error has occured.{VE}", option_1= "OK", justify = "center", option_focus = 1)
            print(f"A conversion error has occurred, {VE}")
            return
        x : str = str(x)
        EntryOutput.delete("1.0","1000.0")
        EntryOutput.insert("1.0", x)
                
    def decimals() -> None :
        # A
        # iA11
        if iA11 % 1 == 0 : tk_iA11.set(f"{iA11:.0f}")
        else : tk_iA11.set(f"{iA11:.2f}")
        # iA12
        if iA12 % 1 == 0 : tk_iA12.set(f"{iA12:.0f}")
        else : tk_iA12.set(f"{iA12:.2f}")
        # iA13
        if iA13 % 1 == 0 : tk_iA13.set(f"{iA13:.0f}")
        else : tk_iA13.set(f"{iA13:.2f}")
        # iA21
        if iA21 % 1 == 0 : tk_iA21.set(f"{iA21:.0f}")
        else : tk_iA21.set(f"{iA21:.2f}")
        # iA22
        if iA22 % 1 == 0 : tk_iA22.set(f"{iA22:.0f}")
        else : tk_iA22.set(f"{iA22:.2f}")
        # iA23
        if iA23 % 1 == 0 : tk_iA23.set(f"{iA23:.0f}")
        else : tk_iA23.set(f"{iA23:.2f}")
        # iA31
        if iA31 % 1 == 0 : tk_iA31.set(f"{iA31:.0f}")
        else : tk_iA31.set(f"{iA31:.2f}")
        # iA32
        if iA32 % 1 == 0 : tk_iA32.set(f"{iA32:.0f}")
        else : tk_iA32.set(f"{iA32:.2f}") 
        # iA33
        if iA33 % 1 == 0 : tk_iA33.set(f"{iA33:.0f}")
        else : tk_iA33.set(f"{iA33:.2f}")
    # B
        # iB11
        if iB11 % 1 == 0 : tk_iB11.set(f"{iB11:.0f}")
        else : tk_iB11.set(f"{iB11:.2f}")
        # iB12
        if iB12 % 1 == 0 :tk_iB12.set(f"{iB12:.0f}")
        else : tk_iB12.set(f"{iB12:.2f}")
        # iB13
        if iB13 % 1 == 0 :tk_iB13.set(f"{iB13:.0f}")
        else : tk_iB13.set(f"{iB13:.2f}")
        # iB21
        if iB21 % 1 == 0 :tk_iB21.set(f"{iB21:.0f}")
        else : tk_iB21.set(f"{iB21:.2f}")
        # iB22
        if iB22 % 1 == 0 :tk_iB22.set(f"{iB22:.0f}")
        else : tk_iB22.set(f"{iB22:.2f}")
        # iB23
        if iB23 % 1 == 0 :tk_iB23.set(f"{iB23:.0f}")
        else : tk_iB23.set(f"{iB23:.2f}")
        # iB31
        if iB31 % 1 == 0 :tk_iB31.set(f"{iB31:.0f}")
        else : tk_iB31.set(f"{iB31:.2f}")
        # iB32
        if iB32 % 1 == 0 :tk_iB32.set(f"{iB32:.0f}")
        else : tk_iB32.set(f"{iB32:.2f}")
        # iB33
        if iB33 % 1 == 0 :tk_iB33.set(f"{iB33:.0f}")
        else : tk_iB33.set(f"{iB33:.2f}")
            
    def Addition() -> None :
        Gui.Store()
        Gui.Output(Main.main.addition_a_b(matrix_a, matrix_b))
    
    def Subtraction() -> None :
        Gui.Store()
        Gui.Output(Main.main.subtraction_a_b(matrix_a, matrix_b))
    
    def Multiplication() -> None : 
        Gui.Store()
        Gui.Output(Main.main.multiplication_ab(matrix_a, matrix_b))
    
    def Power() -> None : 
        Gui.Store()
        AorB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "Matrix Power",icon = "info", message = "Please select matrix A or B to perform calculation", option_1= "A", option_2= "B", justify = "center")
        choice : str = AorB.get()
        if choice == "A" :
            dialog = ctk.CTkInputDialog(title = "Matrix Power", text = "Please enter the power value, an integer")
            power : int = (dialog.get_input())
            try : power = int(power)
            except ValueError as VE :
                ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = f"Please enter an integer.{VE}", option_1= "OK", justify = "center", option_focus = 1)
                return
            print(power)
            if power or power == 0 : Gui.Output(Main.Advanced.Power(matrix_a, power))
        if choice == "B" :
            dialog = ctk.CTkInputDialog(title = "Matrix Power", text = "Please enter the power value, an integer")
            power : int = (dialog.get_input())
            try : power = int(power)
            except ValueError as VE :
                ErrorMB = ctkmb.CTkMessagebox(master = root , width = 150, height = 100, title = "ERROR",icon = "cancel" , message = f"Please enter an integer.{VE}", option_1= "OK", justify = "center", option_focus = 1)
                return
            if power or power == 0 : Gui.Output(Main.Advanced.Power(matrix_b, power))
    
    def DetA() -> None : 
        Gui.Store()
        Gui.OutAny(Main.Advanced.Determinant(matrix_a))
    
    def DetB() -> None :
        Gui.Store()
        Gui.OutAny(Main.Advanced.Determinant(matrix_b))

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

# Tkinter variables, also have to be declared after root initialization
# A
tk_iA11 : ctk.DoubleVar = ctk.DoubleVar()
iA11 : float = float(tk_iA11.get())
tk_iA12 : ctk.DoubleVar = ctk.DoubleVar()
iA12 : float = float(tk_iA11.get())
tk_iA13 : ctk.DoubleVar = ctk.DoubleVar()
iA13 : float = float(tk_iA13.get())
tk_iA21 : ctk.DoubleVar = ctk.DoubleVar()
iA21 : float = float(tk_iA21.get())
tk_iA22 : ctk.DoubleVar = ctk.DoubleVar()
iA22 : float = float(tk_iA22.get())
tk_iA23 : ctk.DoubleVar = ctk.DoubleVar()
iA23 : float = float(tk_iA23.get())
tk_iA31 : ctk.DoubleVar = ctk.DoubleVar()
iA31 : float = float(tk_iA31.get())
tk_iA32 : ctk.DoubleVar = ctk.DoubleVar()
iA32 : float = float(tk_iA32.get())
tk_iA33 : ctk.DoubleVar = ctk.DoubleVar()
iA33 : float = float(tk_iA33.get())
# B
tk_iB11 : ctk.DoubleVar = ctk.DoubleVar()
iB11 : float = float(tk_iB11.get())
tk_iB12 : ctk.DoubleVar = ctk.DoubleVar()
iB12 : float = float(tk_iB11.get())
tk_iB13 : ctk.DoubleVar = ctk.DoubleVar()
iB13 : float = float(tk_iB13.get())
tk_iB21 : ctk.DoubleVar = ctk.DoubleVar()
iB21 : float = float(tk_iB21.get())
tk_iB22 : ctk.DoubleVar = ctk.DoubleVar()
iB22 : float = float(tk_iB22.get())
tk_iB23 : ctk.DoubleVar = ctk.DoubleVar()
iB23 : float = float(tk_iB23.get())
tk_iB31 : ctk.DoubleVar = ctk.DoubleVar()
iB31 : float = float(tk_iB31.get())
tk_iB32 : ctk.DoubleVar = ctk.DoubleVar()
iB32 : float = float(tk_iB32.get())
tk_iB33 : ctk.DoubleVar = ctk.DoubleVar()
iB33 : float = float(tk_iB33.get())

# matrix variables
matrix_a : list[list[float]] = [[iA11, iA12, iA13],[iA21, iA22, iA23],[iA31, iA32, iA33]]
matrix_b : list[list[float]] = [[iB11, iB12, iB13],[iB21, iB22, iB23],[iB31, iB32, iB33]]

# fonts
cfontbtn = ctk.CTkFont("capilary", 18, weight = "bold")
cfont = ctk.CTkFont("capilary", 16, weight = "bold")
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

# main buttons
btnAddition = ctk.CTkButton(master = main_frame, corner_radius = 12, font = cfontbtn, text = "Addition", fg_color = "dodgerblue4", command = lambda : Gui.Addition())
btnAddition.grid(row = 1, column = 1, sticky = "nesw", padx = 35, pady = 20)
btnSubtraction = ctk.CTkButton(master = main_frame, corner_radius = 12, font = cfontbtn, text = "Subtraction", fg_color = "dodgerblue4", command = lambda : Gui.Subtraction())
btnSubtraction.grid(row = 2, column = 1, sticky = "nesw", padx = 35, pady = 20)
btnMultiplication = ctk.CTkButton(master = main_frame, corner_radius = 12, font = cfontbtn, text = "Multiplication", fg_color = "dodgerblue4", command = lambda : Gui.Multiplication())
btnMultiplication.grid(row = 3, column = 1, sticky = "nesw", padx = 35, pady = 20)
btnPower = ctk.CTkButton(master = main_frame, corner_radius = 12, font = cfontbtn, text = "Power", fg_color = "dodgerblue4", command = lambda : Gui.Power())
btnPower.grid(row = 4, column = 1, sticky = "nesw", padx = 35, pady = 20)
btnDeterminantA = ctk.CTkButton(master = main_frame, corner_radius = 12, font = cfontbtn, text = "Determinant of A", fg_color = "dodgerblue4", command = lambda : Gui.DetA())
btnDeterminantA.grid(row = 5, column = 1, sticky = "nesw", padx = 35, pady = 20)
btnDeterminantB = ctk.CTkButton(master = main_frame, corner_radius = 12, font = cfontbtn, text = "Determinant of B", fg_color = "dodgerblue4", command = lambda : Gui.DetB())
btnDeterminantB.grid(row = 6, column = 1, sticky = "nesw", padx = 35, pady = 20)

# btnCalculateVectors = ctk.CTkButton(master = main_frame, corner_radius = 12, font = cfontbtn, text = "Calculate components")
# btnCalculateVectors.grid(row = 7, column = 1, sticky = "nesw", padx = 35, pady = 20)

# output
# change row to 3 and rowspan to 3 when redoing GUI, Reminder that it creates 3 rows for 3 sections of components
EntryOutput = ctk.CTkTextbox(master = main_frame, font = ctk.CTkFont("capilary", 28, "bold"), corner_radius = 10)
EntryOutput.grid(column = 2, row = 2, rowspan = 4, sticky = "nsew")

# for the frame where matrixes will be placed
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
    
A_R1C1 = ctk.CTkEntry(master = frame_a, textvariable = tk_iA11, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R1C1.grid(row = 0, column = 0, padx = 5, pady = 10)
A_R1C2 = ctk.CTkEntry(master = frame_a, textvariable = tk_iA12, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R1C2.grid(row = 0, column = 1, padx = 5, pady = 5)
A_R1C3 = ctk.CTkEntry(master = frame_a, textvariable = tk_iA13, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R1C3.grid(row = 0, column = 2, padx = 5, pady = 5)
A_R2C1 = ctk.CTkEntry(master = frame_a, textvariable = tk_iA21, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R2C1.grid(row = 1, column = 0, padx = 5, pady = 5)
A_R2C2 = ctk.CTkEntry(master = frame_a, textvariable = tk_iA22, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R2C2.grid(row = 1, column = 1, padx = 5, pady = 5)
A_R2C3 = ctk.CTkEntry(master = frame_a, textvariable = tk_iA23, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R2C3.grid(row = 1, column = 2, padx = 5, pady = 5)
A_R3C1 = ctk.CTkEntry(master = frame_a, textvariable = tk_iA31, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R3C1.grid(row = 2, column = 0, padx = 5, pady = 10)
A_R3C2 = ctk.CTkEntry(master = frame_a, textvariable = tk_iA32, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
A_R3C2.grid(row = 2, column = 1, padx = 5, pady = 5)
A_R3C3 = ctk.CTkEntry(master = frame_a, textvariable = tk_iA33, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
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
    
B_R1C1 = ctk.CTkEntry(master = frame_b, textvariable = tk_iB11, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R1C1.grid(row = 0, column = 0, padx = 5, pady = 10)
B_R1C2 = ctk.CTkEntry(master = frame_b, textvariable = tk_iB12, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R1C2.grid(row = 0, column = 1, padx = 5, pady = 5)
B_R1C3 = ctk.CTkEntry(master = frame_b, textvariable = tk_iB13, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R1C3.grid(row = 0, column = 2, padx = 5, pady = 5)
B_R2C1 = ctk.CTkEntry(master = frame_b, textvariable = tk_iB21, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R2C1.grid(row = 1, column = 0, padx = 5, pady = 5)
B_R2C2 = ctk.CTkEntry(master = frame_b, textvariable = tk_iB22, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R2C2.grid(row = 1, column = 1, padx = 5, pady = 5)
B_R2C3 = ctk.CTkEntry(master = frame_b, textvariable = tk_iB23, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R2C3.grid(row = 1, column = 2, padx = 5, pady = 5)
B_R3C1 = ctk.CTkEntry(master = frame_b, textvariable = tk_iB31, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R3C1.grid(row = 2, column = 0, padx = 5, pady = 10)
B_R3C2 = ctk.CTkEntry(master = frame_b, textvariable = tk_iB32, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R3C2.grid(row = 2, column = 1, padx = 5, pady = 5)
B_R3C3 = ctk.CTkEntry(master = frame_b, textvariable = tk_iB33, corner_radius = 0, height = 35, width = 35, justify="center", font = cfont)
B_R3C3.grid(row = 2, column = 2, padx = 5, pady = 5)

# button clear
button_clear_matrixes = ctk.CTkButton(master = frame_matrix, text = "Clear", fg_color = "dodgerblue4", command = lambda : Gui.button_clear(), height = 35)
button_clear_matrixes.grid(row = 9, column = 0, sticky = "nesw", padx = 15, pady = 15)

# may remove in a later stage
Gui.decimals()

root.mainloop()