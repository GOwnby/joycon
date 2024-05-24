# Libraries needed to install: 
# pip install tk 
# pip install pyserial
# pip install matplotlib (python3 -m pip install matplotlib -- command if pip PATH is Python 2.x)
# pip install Pillow (python3 -m pip install Pillow)
import sys # Package used to exit the application properly
import os # Package used to navigate folders correctly
import tkinter as tk # Package used for creating GUI window
from PIL import ImageTk, Image # Package used to add Image to GUI
import matplotlib.backends.backend_tkagg # Package used to add Plot Graph to GUI
import matplotlib.figure # Package used to add Plot Graph to GUI
import ArduinoConnect # Package used for connecting to the Arduino
import math

# Run the above functions to get the COM port the Arduino is connected to
serialConnection = ArduinoConnect.findArduino()

# Create tkinter window for GUI
window = tk.Tk()
# Name the window and set the geometry of the window to fill the screen
window.title("A-10 Warthog")
window.geometry("1920x1080")

# Load the OU Logo
img = ImageTk.PhotoImage(Image.open(os.path.dirname(os.path.dirname(os.path.realpath(__file__) ) ) + os.sep + "media" + os.sep + "OUlogo.png") )
panel = tk.Label(window, image=img)
panel.pack(side="top", fill="none", expand="no") # Add the Logo to the top of the GUI

# Create a Figure to hold the First Joystick Position Plot
joystickFigure1 = matplotlib.figure.Figure(figsize=(5,5), dpi=100)
# Add the Figure to a Canvas Frame within the Window
canvasPlot1 = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(joystickFigure1, window)
canvasPlot1.get_tk_widget().pack(side='left')

# Add a Frame Filler for padding between the canvas plot and Digital Input Buttons
frameFillA = tk.Frame(width="100")
frameFillA.pack(side="left")

# Add a Frame to hold the Digital Input Buttons
frameA = tk.Frame()
frameA.pack(side="left")

# Create a Figure to hold the Second Joystick Position Plot
joystickFigure2 = matplotlib.figure.Figure(figsize=(5,5), dpi=100)
# Add the Figure to a Canvas Frame within the Window
canvasPlot2 = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(joystickFigure2, window)
canvasPlot2.get_tk_widget().pack(side='right')

# Add a Frame Filler for padding between the canvas plot and Digital Output Buttons
frameFillB = tk.Frame(width="100")
frameFillB.pack(side="right")

# Add a Frame to hold the Digital Output Buttons
frameB = tk.Frame()
frameB.pack(side="right")

# Functions to send characters to the Arduino specifying which Digital Output should be turned on
def turnOnLED1():
    serialConnection.write(b"1")
def turnOnLED2():
    serialConnection.write(b"2")
def turnOnLED3():
    serialConnection.write(b"3")
def turnOnLED4():
    serialConnection.write(b"4")
def turnOnLED5():
    serialConnection.write(b"5")
def turnOnLED6():
    serialConnection.write(b"6")
def turnOnLED7():
    serialConnection.write(b"7")
def turnOnLED8():
    serialConnection.write(b"8")
def turnOnLED9():
    serialConnection.write(b"9")
def turnOnLED10():
    serialConnection.write(b"q")
def turnOnLED11():
    serialConnection.write(b"w")
def turnOnLED12():
    serialConnection.write(b"e")
def turnOnLED13():
    serialConnection.write(b"r")
def turnOnLED14():
    serialConnection.write(b"t")
def turnOnLED15():
    serialConnection.write(b"y")
def turnOnLED16():
    serialConnection.write(b"u")

# Add all the Digital Input buttons to Frame A
buttonB1I = tk.Button(frameA, text='Digital Input 1')
buttonB1I.pack()
buttonB2I = tk.Button(frameA, text='Digital Input 2')
buttonB2I.pack()
buttonB3I = tk.Button(frameA, text='Digital Input 3')
buttonB3I.pack()
buttonB4I = tk.Button(frameA, text='Digital Input 4')
buttonB4I.pack()
buttonB5I = tk.Button(frameA, text='Digital Input 5')
buttonB5I.pack()
buttonB6I = tk.Button(frameA, text='Digital Input 6')
buttonB6I.pack()
buttonB7I = tk.Button(frameA, text='Digital Input 7')
buttonB7I.pack()
buttonB8I = tk.Button(frameA, text='Digital Input 8')
buttonB8I.pack()
buttonB9I = tk.Button(frameA, text='Digital Input 9')
buttonB9I.pack()
buttonB10I = tk.Button(frameA, text='Digital Input 10')
buttonB10I.pack()
buttonB11I = tk.Button(frameA, text='Digital Input 11')
buttonB11I.pack()
buttonB12I = tk.Button(frameA, text='Digital Input 12')
buttonB12I.pack()
buttonB13I = tk.Button(frameA, text='Digital Input 13')
buttonB13I.pack()
buttonB14I = tk.Button(frameA, text='Digital Input 14')
buttonB14I.pack()
buttonB15I = tk.Button(frameA, text='Digital Input 15')
buttonB15I.pack()
buttonB16I = tk.Button(frameA, text='Digital Input 16')
buttonB16I.pack()

# Add all the Digital Output buttons to Frame B and attach the command corresponding to each Digital Output
buttonB1O = tk.Button(frameB, text='Digital Output 1', command=turnOnLED1)
buttonB1O.pack()
buttonB2O = tk.Button(frameB, text='Digital Output 2', command=turnOnLED2)
buttonB2O.pack()
buttonB3O = tk.Button(frameB, text='Digital Output 3', command=turnOnLED3)
buttonB3O.pack()
buttonB4O = tk.Button(frameB, text='Digital Output 4', command=turnOnLED4)
buttonB4O.pack()
buttonB5O = tk.Button(frameB, text='Digital Output 5', command=turnOnLED5)
buttonB5O.pack()
buttonB6O = tk.Button(frameB, text='Digital Output 6', command=turnOnLED6)
buttonB6O.pack()
buttonB7O = tk.Button(frameB, text='Digital Output 7', command=turnOnLED7)
buttonB7O.pack()
buttonB8O = tk.Button(frameB, text='Digital Output 8', command=turnOnLED8)
buttonB8O.pack()
buttonB9O = tk.Button(frameB, text='Digital Output 9', command=turnOnLED9)
buttonB9O.pack()
buttonB10O = tk.Button(frameB, text='Digital Output 10', command=turnOnLED10)
buttonB10O.pack()
buttonB11O = tk.Button(frameB, text='Digital Output 11', command=turnOnLED11)
buttonB11O.pack()
buttonB12O = tk.Button(frameB, text='Digital Output 12', command=turnOnLED12)
buttonB12O.pack()
buttonB13O = tk.Button(frameB, text='Digital Output 13', command=turnOnLED13)
buttonB13O.pack()
buttonB14O = tk.Button(frameB, text='Digital Output 14', command=turnOnLED14)
buttonB14O.pack()
buttonB15O = tk.Button(frameB, text='Digital Output 15', command=turnOnLED15)
buttonB15O.pack()
buttonB16O = tk.Button(frameB, text='Digital Output 16', command=turnOnLED16)
buttonB16O.pack()

# Sliders are used to measure the potentiometers and are placed in the middle of the screen between the packed Frames
# Add a Frame Filler for padding between the top of the logo and the sliders
fillFrameC = tk.Frame(height="200")
fillFrameC.pack()

# Add each Slider Scale to the GUI 
sliderS1 = tk.Scale(window, from_=0, to=5)
sliderS1.pack()

sliderS2 = tk.Scale(window, from_=0, to=5)
sliderS2.pack()

sliderS3 = tk.Scale(window, from_=0, to=5)
sliderS3.pack()

sliderS4 = tk.Scale(window, from_=0, to=5)
sliderS4.pack()

# A function that asks the user if they would like to quit the program when they try to close the program
def on_closing():
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

# Attach the closing function to the window
window.protocol("WM_DELETE_WINDOW", on_closing)

# Start the Main Loop that refreshes the values of Inputs and Outputs on the GUI
while 1:
    # Read in data in the order that it was printed
    # Read in the serial data corresponding to both Joysticks
    serialDataX1 = float(serialConnection.readline().decode('ascii')) # Joystick 1 X-axis
    serialDataY1 = float(serialConnection.readline().decode('ascii')) # Joystick 1 Y-axis
    serialDataX2 = float(serialConnection.readline().decode('ascii')) # Joystick 2 X-axis
    serialDataY2 = float(serialConnection.readline().decode('ascii')) # Joystick 2 Y-axis
    # Read in the serial data corresponding to each Potentiometer
    serialDataPot1 = float(serialConnection.readline().decode('ascii')) # Potentiometer 1
    serialDataPot2 = float(serialConnection.readline().decode('ascii')) # Potentiometer 2
    serialDataPot3 = float(serialConnection.readline().decode('ascii')) # Potentiometer 3
    serialDataPot4 = float(serialConnection.readline().decode('ascii')) # Potentiometer 4
    # Read in the serial data corresponding to each Digital Input Button
    serialDataB1 = float(serialConnection.readline().decode('ascii')) # Button 1 Digital Input
    serialDataB2 = float(serialConnection.readline().decode('ascii')) # Button 2 Digital Input
    serialDataB3 = float(serialConnection.readline().decode('ascii')) # Button 3 Digital Input
    serialDataB4 = float(serialConnection.readline().decode('ascii')) # Button 4 Digital Input
    serialDataB5 = float(serialConnection.readline().decode('ascii')) # Button 5 Digital Input
    serialDataB6 = float(serialConnection.readline().decode('ascii')) # Button 6 Digital Input
    serialDataB7 = float(serialConnection.readline().decode('ascii')) # Button 7 Digital Input
    serialDataB8 = float(serialConnection.readline().decode('ascii')) # Button 8 Digital Input
    serialDataB9 = float(serialConnection.readline().decode('ascii')) # Button 9 Digital Input
    serialDataB10 = float(serialConnection.readline().decode('ascii')) # Button 10 Digital Input
    serialDataB11 = float(serialConnection.readline().decode('ascii')) # Button 11 Digital Input
    serialDataB12 = float(serialConnection.readline().decode('ascii')) # Button 12 Digital Input
    serialDataB13 = float(serialConnection.readline().decode('ascii')) # Button 13 Digital Input
    serialDataB14 = float(serialConnection.readline().decode('ascii')) # Button 14 Digital Input
    serialDataB15 = float(serialConnection.readline().decode('ascii')) # Button 15 Digital Input
    serialDataB16 = float(serialConnection.readline().decode('ascii')) # Button 16 Digital Input

    # Decode the range from 0V to 5V to a -1.0 to +1.0 axis range for Joystick 1
    # Values greater than 2.5 are positive, values less than 2.5 are negative
    if serialDataX1 >= 2.5:
        positionX1 = (serialDataX1 - 2.5) * 0.4 # Adjust to a range of 0 to 1
    elif serialDataX1 < 2.5:
        positionX1 = (2.5 - serialDataX1) * -0.4 # Adjust to a range of 0 to 1

    if serialDataY1 >= 2.5:
        positionY1 = (serialDataY1 - 2.5) * 0.4 # Adjust to a range of 0 to 1
    elif serialDataY1 < 2.5:
        positionY1 = (2.5 - serialDataY1) * -0.4 # Adjust to a range of 0 to 1

    # Decode the range from 0V to 5V to a -1.0 to +1.0 axis range for Joystick 2
    # Values greater than 2.5 are positive, values less than 2.5 are negative
    if serialDataX2 >= 2.5:
        positionX2 = (serialDataX2 - 2.5) * 0.4 # Adjust to a range of 0 to 1
    elif serialDataX2 < 2.5:
        positionX2 = (2.5 - serialDataX2) * -0.4 # Adjust to a range of 0 to 1

    if serialDataY2 >= 2.5:
        positionY2 = (serialDataY2 - 2.5) * 0.4 # Adjust to a range of 0 to 1
    elif serialDataY2 < 2.5:
        positionY2 = (2.5 - serialDataY2) * -0.4 # Adjust to a range of 0 to 1

    # Print the plot to the Tkinter GUI by adding a plot to the Figure within the Canvas within the Window
    joystickPlot1 = joystickFigure1.add_subplot(111)
    joystickPlot1.scatter(float(positionX1), -1.0 * float(positionY1)) # Flip the orientation of the y-axis for this joystick
    # Set the Axis range
    joystickPlot1.set_xlim(-1, 1)
    joystickPlot1.set_ylim(-1, 1)

    # Draw updated values to the plot
    canvasPlot1.draw()

    # Run all waiting GUI events for the Canvas Frame holding the Joystick Figure within the Window before moving forward in the loop
    canvasPlot1.flush_events()

    # Print the plot to the Tkinter GUI by adding a plot to the Figure within the Canvas within the Window
    joystickPlot2 = joystickFigure2.add_subplot(111)
    joystickPlot2.scatter(float(positionX2), -1.0 * float(positionY2)) # Flip the orientation of the y-axis for this joystick
    # Set the Axis range
    joystickPlot2.set_xlim(-1, 1)
    joystickPlot2.set_ylim(-1, 1)

    # Draw updated values to the plot
    canvasPlot2.draw()

    # Run all waiting GUI events for the Canvas Frame holding the Joystick Figure within the Window before moving forward in the loop
    canvasPlot2.flush_events()

    # Check which Digital Output buttons have been clicked by the user on the GUI and invoke the command attached to the button
    try:
        if buttonB1O['relief'] == "sunken":
            buttonB1O.invoke()

        if buttonB2O['relief'] == "sunken":
            buttonB2O.invoke()

        if buttonB3O['relief'] == "sunken":
            buttonB3O.invoke()

        if buttonB4O['relief'] == "sunken":
            buttonB4O.invoke()

        if buttonB5O['relief'] == "sunken":
            buttonB5O.invoke()

        if buttonB6O['relief'] == "sunken":
            buttonB6O.invoke()

        if buttonB7O['relief'] == "sunken":
            buttonB7O.invoke()

        if buttonB8O['relief'] == "sunken":
            buttonB8O.invoke()

        if buttonB9O['relief'] == "sunken":
            buttonB9O.invoke()

        if buttonB10O['relief'] == "sunken":
            buttonB10O.invoke()
      
        if buttonB11O['relief'] == "sunken":
            buttonB11O.invoke()

        if buttonB12O['relief'] == "sunken":
            buttonB12O.invoke()

        if buttonB13O['relief'] == "sunken":
            buttonB13O.invoke()

        if buttonB14O['relief'] == "sunken":
            buttonB14O.invoke()

        if buttonB15O['relief'] == "sunken":
            buttonB15O.invoke()

        if buttonB16O['relief'] == "sunken":
            buttonB16O.invoke()
    except Exception:
        pass
    
    # Set the value of the Sliders after the Potentiometer data has been read
    try:
        sliderS1.set(int(serialDataPot1))
        sliderS2.set(int(serialDataPot2))
        sliderS3.set(int(serialDataPot3))
        sliderS4.set(int(serialDataPot4))
    except Exception:
        pass

    # Set the value of the Digital Input Buttons after the Digital Input data has been read
    try:
        if math.isclose(serialDataB1, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB1I.config(relief="sunken")

        if math.isclose(serialDataB1, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB1I.config(relief="raised")

        if math.isclose(serialDataB2, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB2I.config(relief="sunken")

        if math.isclose(serialDataB2, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB2I.config(relief="raised")

        if math.isclose(serialDataB3, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB3I.config(relief="sunken")

        if math.isclose(serialDataB3, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB3I.config(relief="raised")

        if math.isclose(serialDataB4, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB4I.config(relief="sunken")

        if math.isclose(serialDataB4, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB4I.config(relief="raised")

        if math.isclose(serialDataB5, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB5I.config(relief="sunken")

        if math.isclose(serialDataB5, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB5I.config(relief="raised")

        if math.isclose(serialDataB6, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB6I.config(relief="sunken")

        if math.isclose(serialDataB6, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB6I.config(relief="raised")

        if math.isclose(serialDataB7, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB7I.config(relief="sunken")

        if math.isclose(serialDataB7, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB7I.config(relief="raised")

        if math.isclose(serialDataB8, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB8I.config(relief="sunken")

        if math.isclose(serialDataB8, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB8I.config(relief="raised")

        if math.isclose(serialDataB9, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB9I.config(relief="sunken")

        if math.isclose(serialDataB9, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB9I.config(relief="raised")

        if math.isclose(serialDataB10, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB10I.config(relief="sunken")

        if math.isclose(serialDataB10, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB10I.config(relief="raised")

        if math.isclose(serialDataB11, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB11I.config(relief="sunken")

        if math.isclose(serialDataB11, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB11I.config(relief="raised")

        if math.isclose(serialDataB12, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB12I.config(relief="sunken")

        if math.isclose(serialDataB12, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB12I.config(relief="raised")

        if math.isclose(serialDataB13, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB13I.config(relief="sunken")

        if math.isclose(serialDataB13, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB13I.config(relief="raised")

        if math.isclose(serialDataB14, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB14I.config(relief="sunken")

        if math.isclose(serialDataB14, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB14I.config(relief="raised")

        if math.isclose(serialDataB15, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB15I.config(relief="sunken")

        if math.isclose(serialDataB15, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB15I.config(relief="raised")

        if math.isclose(serialDataB16, 1.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB16I.config(relief="sunken")

        if math.isclose(serialDataB16, 0.0, rel_tol=1e-09, abs_tol=0.0):
            buttonB16I.config(relief="raised")
    except Exception:
        pass

    # Update the Window to show our changed Frames
    window.update()

    # Clear the plots from the Tkinter GUI to prepare to write new Frames
    try:
        joystickFigure1.clear()
        joystickFigure2.clear()
    except Exception: # If the plots on the Frame cannot be found/destroyed it is because the application was closed mid-loop (they are gone already)
        sys.exit(0)
