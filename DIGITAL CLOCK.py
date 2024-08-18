import tkinter as tk
import time



# Function to update the label text with the current time
def update_time():
    current_time = time.strftime('%H:%M:%S %p')
    clock_label.config(text=current_time)
    root.after(1000, update_time)
# Update every 1000 milliseconds (1 second)


    
# Create the main window
root = tk.Tk()
root.title("Digital Clock")



# Create a label to display the time
clock_label = tk.Label(root, text="", font=("Arial Black", 48, "bold"),
                       background="pink", foreground="white")
clock_label.pack(padx=20, pady=20)



# Start updating the time
update_time()



# Start the Tkinter event loop
root.mainloop()




  
