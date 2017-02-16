import os
import sys
if(sys.version_info[0]<3):
    from Tkinter import *
else:
    from tkinter import *
import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15

#create an ADS1015 ADC (12-bit) instance.
adc = Adafruit_ADS1x15.ADS1015()


#Define names according to scematic, the numbers referres to GPIO number
CAN_120_term = 13
CAN_Traffic = 5
CAN_Error = 16
Yellow = 12
Logging_active = 6
Plus30_General = 26
SW_CAN_term = 21
Info_If_Sim = 20
Info_If_Read = 18
Ubat_control = 4
Start_Stop_Log =19
CAN_transmit = 17  #this GPIO must be pulled down to allow transmit of CAN traffic

#Setup GPIOs

#Outputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(CAN_120_term, GPIO.OUT)
GPIO.setup(CAN_Traffic, GPIO.OUT)
GPIO.setup(CAN_Error, GPIO.OUT)
GPIO.setup(Yellow, GPIO.OUT)
GPIO.setup(Logging_active, GPIO.OUT)
GPIO.setup(Plus30_General, GPIO.OUT)
GPIO.setup(Info_If_Sim, GPIO.OUT)
GPIO.setup(Ubat_control, GPIO.OUT)
GPIO.setup(CAN_transmit, GPIO.OUT)

#Inputs
GPIO.setup(SW_CAN_term, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Info_If_Read, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Start_Stop_Log, GPIO.IN, pull_up_down=GPIO.PUD_UP)


	
def button_state(input_state):
	if (GPIO.input(input_state) == 1):
		return ("HIGH")
	else:
		return ("LOW")

	
	
class App(Frame):
	
    def __init__(self, master):
        frame = Frame(master)
        self.master = master
        frame.pack()
        self.check_var = BooleanVar()
        check = Checkbutton(frame, text='CAN_120_Ohm', 
                 command=self.update,
                 variable=self.check_var, onvalue=True, offvalue=False)
        check.grid(row=1)
        
        label = Label(frame, text='SW_CAN_Term switch', fg="green", font=("Helvetica", 12))
        label.grid(row=2)
        self.reading_label1 = Label(frame, text='12.44', font=("Helvetica", 12))
        self.reading_label1.grid(row=3)
     #   self.update_reading()
        
        label = Label(frame, text='Info_If_Read', fg="red", font=("Helvetica", 12))
        label.grid(row=4)
        self.reading_label2 = Label(frame, text='12.34', font=("Helvetica", 12))
        self.reading_label2.grid(row=5)
    #    self.update_reading()
        
        label = Label(frame, text='Start_Stop_Log', fg="blue", font=("Helvetica", 12))
        label.grid(row=6)
        self.reading_label3 = Label(frame, text='12.34', font=("Helvetica", 12))
        self.reading_label3.grid(row=7)
        
        label = Label(frame, text='TGW Voltage', fg="orange", font=("Helvetica", 12))
        label.grid(row=8)
        self.reading_label4 = Label(frame, text='12.34', font=("Helvetica", 12))
        self.reading_label4.grid(row=9)
        
        label = Label(frame, text='TGW current', fg="orange", font=("Helvetica", 12))
        label.grid(row=10)
        self.reading_labelcurrent= Label(frame, text='12.34', font=("Helvetica", 12))
        self.reading_labelcurrent.grid(row=11)
        
        label = Label(frame, text='ch3 voltage', fg="orange", font=("Helvetica", 12))
        label.grid(row=12)
        self.reading_label5= Label(frame, text='12.34', font=("Helvetica", 12))
        self.reading_label5.grid(row=13)
        
        label = Label(frame, text='+30_General current', fg="orange", font=("Helvetica", 12))
        label.grid(row=14)
        self.reading_label6= Label(frame, text='12.34', font=("Helvetica", 12))
        self.reading_label6.grid(row=15)
     
        self.update_reading()
        
    
       
	
	button = Button(root, text='CAN_Traffic', width=25,
	command=lambda: self.my_func(CAN_Traffic))
	button.pack()
	
	button1 = Button(root, text='CAN_Error', width=25,
	command=lambda: self.my_func(CAN_Error))
	button1.pack()
	
	button2 = Button(root, text='Yellow', width=25,
	command=lambda: self.my_func(Yellow))
	button2.pack()
	
	button3 = Button(root, text='Logging_active', width=25,
	command=lambda: self.my_func(Logging_active))
	button3.pack()
	
	button4 = Button(root, text='Plus30General', width=25,
	command=lambda: self.my_func(Plus30_General))
	button4.pack()  
	
	button5 = Button(root, text='Info_If_Sim', width=25,
	command=lambda: self.my_func(Info_If_Sim))
	button5.pack()  
	
	button6 = Button(root, text='Ubat_control', width=25,
	command=lambda: self.my_func(Ubat_control))
	button6.pack()  
	
	button7 = Button(root, text='Activate Tx CAN', width=25,
	command=lambda: self.my_func(CAN_transmit))
	button7.pack()  
	
	button8 = Button(root, text='Send vehicle mode running', width=25,
	command=lambda: os.system("cansend can0 10FF1FDF#FFF37F6FFF0CFFFF"))
	button8.pack()
	
	button9 = Button(root, text='shut down CAN controller', width=25,
	command=lambda: os.system("sudo ifconfig can0 down"))
	button9.pack()
	
	button10 = Button(root, text='start CAN controller 500k baud', width=25,
	command=lambda: os.system("sudo ifconfig can0 up"))
	button10.pack()
	
	

	#Updates label with the reading of an GPIO input		
    def update_reading(self):
        self.reading_label1.configure(text=button_state(SW_CAN_term))
        self.reading_label2.configure(text=button_state(Info_If_Read))
        self.reading_label3.configure(text=button_state(Start_Stop_Log))
        self.reading_label4.configure(text='{:.2f}'.format(adc.read_adc(1, gain=1)*10.9834/500.))
        self.reading_labelcurrent.configure(text='{:.2f}'.format(adc.read_adc(0, gain=1)/2))
        self.reading_label5.configure(text='{:.2f}'.format(adc.read_adc(3, gain=1)*10.9834/500.))
        self.reading_label6.configure(text='{:.2f}'.format(adc.read_adc(2, gain=1)/2))
        self.master.after(500, self.update_reading)
        
	#function used by checkbox
    def update(self):
        GPIO.output(CAN_120_term, self.check_var.get())
        
   
       
	#Function to handle every button press
    def my_func(self,knapp):
		if(GPIO.input(knapp) == 1):
			GPIO.output(knapp, False)
		else:
			GPIO.output(knapp, True)


root = Tk()
root.wm_title('LOBSTER HW test interface')
app = App(root)
root.geometry("400x700+0+0")
root.mainloop()
GPIO.cleanup()
