from tkinter import *
from tkinter import messagebox

# Global list for storing all the tasks
tasks_list = []

# Global variable for counting the tasks
counter = 1

def input_error():
    # Check for empty task field
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error", "Task field cannot be empty")
        return False
    return True

def clear_task_number_field():
    # Clear the content of the task number text field
    taskNumberField.delete(0.0, END)

def clear_task_field():
    # Clear the content of the task field entry box
    enterTaskField.delete(0, END)

def insert_task():
    global counter

    # Check for input error
    if not input_error():
        return

    # Get the task string concatenating with a new line character
    content = enterTaskField.get() + "\n"

    # Store the task in the list
    tasks_list.append(content)

    # Insert content of the task entry field to the text area
    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)

    # Increment counter
    counter += 1

    # Clear the content of the task field
    clear_task_field()

def delete_task():
    global counter

    # Handling the empty task error
    if len(tasks_list) == 0:
        messagebox.showerror("No task", "No tasks to delete")
        return

    # Get the task number which is required to delete
    number = taskNumberField.get(1.0, END)

    # Checking for input error when empty input in the task number field
    if number == "\n":
        messagebox.showerror("Input Error", "Task number cannot be empty")
        return
    else:
        task_no = int(number)

    # Function calling for deleting the content of the task number field
    clear_task_number_field()

    # Delete specified task from the list
    tasks_list.pop(task_no - 1)

    # Decrement counter
    counter -= 1

    # Clear the whole content of the text area widget
    TextArea.delete(1.0, END)

    # Rewrite the tasks after deleting one task at a time
    for i in range(len(tasks_list)):
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])

# Driver code
if __name__ == "__main__":

    # Create a GUI window
    gui = Tk()

    # Set the background color of the GUI window
    gui.configure(background="papayawhip")

    # Set the title of the GUI window
    gui.title("ToDo App")

    # Set the configuration of the GUI window
    gui.geometry("700x1000")  # 4 times larger than the original size

    # Create a label: Enter Your Task
    enterTask = Label(gui, text="Enter Your Task", bg="papayawhip", font=("Arial", 25))

    # Create a text entry box for typing the task
    enterTaskField = Entry(gui, font=("Arial", 25))

    # Create a Submit Button
    Submit = Button(gui, text="Submit", fg="black", bg="peachpuff1", font=("Arial", 25), command=insert_task)

    # Create a text area for writing the content
    TextArea = Text(gui, height=10, width=35, font="lucida 25", bg="peachpuff2")

    # Create a label: Delete Task Number
    taskNumber = Label(gui, text="Delete Task Number", bg="peachpuff3", font=("Arial", 25))

    taskNumberField = Text(gui, height=1, width=5, font=("Arial", 25))

    # Create a Delete Button
    delete = Button(gui, text="Delete", fg="black", bg="peachpuff1", font=("Arial", 25), command=delete_task)

    # Grid method is used for placing the widgets at respective positions
    enterTask.grid(row=0, column=2)

    # ipadx attributed set the entry box horizontal size
    enterTaskField.grid(row=1, column=2, ipadx=100)  # 4 times larger than the original size

    Submit.grid(row=2, column=2)

    # padx attributed provide x-axis margin from the root window to the widget
    TextArea.grid(row=3, column=2, padx=20, pady=10, sticky=W)  # Larger padding

    taskNumber.grid(row=4, column=2, pady=10)

    taskNumberField.grid(row=5, column=2)

    # pady attributed provide y-axis margin from the widget
    delete.grid(row=6, column=2, pady=10)

    # Start the GUI
    gui.mainloop()
