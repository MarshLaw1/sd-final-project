import tkinter as tk
from tkinter import messagebox

# Create a new window
window = tk.Tk()
window.title("Car Recommender")

# Create a label widget
label = tk.Label(window, text="Welcome to the Car Recommender! Answer a few questions to find out what type of car you should get.")

# Create a frame to hold the radio buttons for the first question
frame1 = tk.Frame(window)

# Create radio button widgets for the first question
choice1 = tk.StringVar()

option1 = tk.Radiobutton(frame1, text="Do you prefer a car with good gas mileage?", variable=choice1, value="Yes")
option2 = tk.Radiobutton(frame1, text="Do you need a car with a lot of cargo space?", variable=choice1, value="No")

# Define callback function for the first question radio buttons
def question1_callback():
    print("Question 1 answer: ", choice1.get())

# Bind callback function to first question radio buttons
option1.config(command=question1_callback)
option2.config(command=question1_callback)

# Create a frame to hold the radio buttons for the second question
frame2 = tk.Frame(window)

# Create radio button widgets for the second question
choice2 = tk.StringVar()

option3 =tk.Radiobutton(frame2, text="Do you prefer a car with a sporty design?", variable=choice2, value="Yes")
option4 =tk.Radiobutton(frame2, text="Do you prefer a car with a luxurious design?", variable=choice2, value="No")

# Define callback function for the second question radio buttons
def question2_callback():
    print("Question 2 answer: ", choice2.get())

# Bind callback function to second question radio buttons
option3.config(command=question2_callback)
option4.config(command=question2_callback)

# Create a frame to hold the radio buttons for the third question
frame3 = tk.Frame(window)

# Create radio button widgets for the third question
choice3 = tk.StringVar()

option5 =tk.Radiobutton(frame3, text="Do you need a car with all-wheel drive?", variable=choice3, value="Yes")
option6 =tk.Radiobutton(frame3, text="Do you need a car with front-wheel drive?", variable=choice3, value="No")

# Define callback function for the third question radio buttons
def question3_callback():
    print("Question 3 answer: ", choice3.get())

# Bind callback function to third question radio buttons
option5.config(command=question3_callback)
option6.config(command=question3_callback)

# Define callback function for the exit button
def exit_callback():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        window.destroy()

# Function to determine car recommendation based on user's answers
def recommend_car():
    answer1 = choice1.get()
    answer2 = choice2.get()
    answer3 = choice3.get()
    if answer1 == "Yes" and answer2 == "Yes" and answer3 == "Yes":
        messagebox.showinfo("Car Recommender", "You should get a Subaru WRX!")
    elif answer1 == "Yes" and answer2 == "Yes" and answer3 == "No":
        messagebox.showinfo("Car Recommender", "You should get a Mazda MX-5 Miata!")
    elif answer1 == "Yes" and answer2 == "No" and answer3 == "Yes":
        messagebox.showinfo("Car Recommender", "You should get a Subaru Outback!")
    elif answer1 == "Yes" and answer2 == "No" and answer3 == "No":
        messagebox.showinfo("Car Recommender", "You should get a Toyota Corolla!")
    elif answer1 == "No" and answer2 == "Yes" and answer3 == "Yes":
        messagebox.showinfo("Car Recommender", "You should get a Subaru Crosstrek!")
    elif answer1 == "No" and answer2 == "Yes" and answer3 == "No":
        messagebox.showinfo("Car Recommender", "You should get a Honda Odyssey!")
    elif answer1 == "No" and answer2 == "No" and answer3 == "Yes":
        messagebox.showinfo("Car Recommender", "You should get a Honda Civic Type R!")
    elif answer1 == "No" and answer2 == "No" and answer3 == "No":
        messagebox.showinfo("Car Recommender", "You should get a Kia Soul!")

#Create a button widget to submit answers
submit_button = tk.Button(window, text="Submit", command=recommend_car)

#Create a button widget to exit the program
exit_button = tk.Button(window, text="Exit", command=exit_callback)

#Add widgets to window
label.pack(padx=20, pady=10)
option1.pack(side="left", padx=5)
option2.pack(side="left", padx=5)
frame1.pack(padx=20, pady=10)
option3.pack(side="left", padx=5)
option4.pack(side="left", padx=5)
frame2.pack(padx=20, pady=10)
option5.pack(side="left", padx=5)
option6.pack(side="left", padx=5)
frame3.pack(padx=20, pady=10)
submit_button.pack(pady=10)
exit_button.pack(pady=10)

#Run the main loop
window.mainloop()
