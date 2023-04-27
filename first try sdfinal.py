import tkinter as tk

class Car:
    def __init__(self, make, model, color, year, price):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price

class CarInventory:
    def __init__(self):
        self.cars = [
            Car('Toyota', 'Camry', 'Red', 2019, 20000),
            Car('Honda', 'Civic', 'Blue', 2020, 22000),
            Car('Ford', 'F-150', 'Black', 2021, 40000),
            Car('Chevrolet', 'Corvette', 'Yellow', 2022, 60000),
            Car('BMW', 'M5', 'White', 2020, 70000)
        ]

class CarFinder:
    def __init__(self, inventory):
        self.inventory = inventory
        self.filtered_cars = self.inventory.cars.copy()

    def filter_cars(self, make=None, model=None, color=None, year=None, price=None):
        self.filtered_cars = self.inventory.cars.copy()
        if make:
            self.filtered_cars = [car for car in self.filtered_cars if car.make == make]
        if model:
            self.filtered_cars = [car for car in self.filtered_cars if car.model == model]
        if color:
            self.filtered_cars = [car for car in self.filtered_cars if car.color == color]
        if year:
            self.filtered_cars = [car for car in self.filtered_cars if car.year == year]
        if price:
            self.filtered_cars = [car for car in self.filtered_cars if car.price <= price]

class CarGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Car Finder')
        self.current_car_list = []

        # Create frames for questions and results
        self.question_frame = tk.Frame(self.window)
        self.question_frame.pack()
        self.result_frame = tk.Frame(self.window)
        self.result_frame.pack()

        # Create questions
        self.make_question = tk.Label(self.question_frame, text='Make:')
        self.make_question.grid(row=0, column=0)
        self.make_entry = tk.Entry(self.question_frame)
        self.make_entry.grid(row=0, column=1)

        self.model_question = tk.Label(self.question_frame, text='Model:')
        self.model_question.grid(row=1, column=0)
        self.model_entry = tk.Entry(self.question_frame)
        self.model_entry.grid(row=1, column=1)

        self.color_question = tk.Label(self.question_frame, text='Color:')
        self.color_question.grid(row=2, column=0)
        self.color_entry = tk.Entry(self.question_frame)
        self.color_entry.grid(row=2, column=1)

        self.year_question = tk.Label(self.question_frame, text='Year:')
        self.year_question.grid(row=3, column=0)
        self.year_entry = tk.Entry(self.question_frame)
        self.year_entry.grid(row=3, column=1)

        self.price_question = tk.Label(self.question_frame, text='Price:')
        self.price_question.grid(row=4, column=0)
        self.price_entry = tk.Entry(self.question_frame)
        self.price_entry.grid(row=4, column=1)

        self.submit_button = tk.Button(self.question_frame, text='Submit', command=self.filter_cars)
        self.submit_button.grid(row=5, column=0)

        # Create results
