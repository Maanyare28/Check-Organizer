import shutil
import os
from tkinter import *
from tkinter import filedialog

# Function to upload a file and save it to a temporary location
def openFile():
    global file_path
    file_path = filedialog.askopenfilename()
    file_name = os.path.basename(file_path)
    shutil.copy(file_path, f"./temp/{file_name}")
    print(f"File '{file_name}' uploaded successfully.")

# Function to sort the file based on its type
def sortFile():
    check_type = check_type_entry.get()
    file_name = os.path.basename(file_path)
    
    if check_type == "1099":
        target_folder = "./1099"
    elif check_type == "food":
        target_folder = "./food"
    elif check_type == "gas":
        target_folder = "./gas"
    elif check_type == "payments":
        target_folder = "./payments"
    elif check_type == "other":
        target_folder = "./others"
    else:
        print("Error: Unknown check type")
        return
    
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    shutil.move(f"./temp/{file_name}", f"{target_folder}/{file_name}")
    print(f"File '{file_name}' sorted to {target_folder} folder.")

# Create necessary directories
if not os.path.exists('./temp'):
    os.makedirs('./temp')

# Create the main window
window = Tk()

# Upload button
upload_button = Button(window, text="Upload Check", command=openFile)
upload_button.pack()

# Entry for check type
check_type_entry = Entry(window)
check_type_entry.pack()
check_type_entry.insert(0, "Enter check type here")

# Sort button
sort_button = Button(window, text="Sort Check", command=sortFile)
sort_button.pack()

# Run the Tkinter event loop
window.mainloop()
