import tkinter as tk
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

        def wool(self):
            return f"{self.name},says woof"
dog1=Dog("German Shepard",10)
dog2=Dog("Husky",8)
older_dog=dog1 if dog1.age>dog2.age else dog2

class DogGUI(tk.Tk):
    def __init__(self):
        super().__init__
        self.title("Dog Infomation")
        self.geometry("300x200")
        self.display_dog_info()

    def display_dog_info(self):
        label1 = tk.Lable(self, "Dog1: {dog1.name},{dog1.age} years old")
        label1.pack()
        label2 = tk.Label(self, text=f"Dog 2: {dog2.name}, {dog2.age} years old")
        label2.pack()
        older_dog_label=tk.label(self,text=f"the older dog is {older_dog_label}")
        older_dog_label.pack()
        woof_button = tk.Button(self, text="Make the oldest dog woof", command=self.woof)
        woof_button.pack()

    def woof (self):
        result = older_dog.woof()
        woof_label =  tk.Label(self, text=result)
        woof_label.pack()


# Instantiate the DogGUI class

app = DogGUI()
app.mainloop()