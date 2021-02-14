import tkinter as tk
from tkinter import messagebox
import numpy as np
from Field import Field


class UI:
    def __init__(self):
        self.__window = tk.Tk()
        self.__window.title("Number Identification!")
        self.__window.rowconfigure(4)
        self.__window.columnconfigure(2)

        self.__field = Field()
        self.__lbl_forecast = tk.Label(self.__window, text="Identified Number:  ", font=("Arial", 14), pady=10, padx=10)
        self.__lbl_forecast.grid(row=0, column=0, columnspan=2)

        self.__btn_identify = tk.Button(self.__window, text="Identify", command=self.identify, pady=10, padx=10)
        self.__btn_identify.grid(row=1, column=1, sticky="nsew")

        self.__btn_delete = tk.Button(self.__window, text="Delete", command=self.delete, pady=10, padx=10)
        self.__btn_delete.grid(row=2, column=1, sticky="nsew")

        self.__btn_close = tk.Button(self.__window, text="Close", command=self.close, pady=10, padx=10)
        self.__btn_close.grid(row=3, column=1, sticky="nsew")

        self.__canvas = tk.Canvas(self.__window, width=150, height=150, borderwidth=1, highlightthickness=1, bg="white")
        self.__canvas.grid(row=1, column=0, rowspan=3, sticky="nsew")
        self.__coordinates = (0, 0)
        self.__canvas.bind("<ButtonPress-1>", self.on_button_down)
        self.__canvas.bind("<B1-Motion>", self.on_move)

    def close(self):
        print("CLOSE")
        self.__window.destroy()

    def identify(self):
        print("IDENTIFY")
        prediction = self.__field.get_forecast_details()
        tmp = ""
        for entry in prediction[0]:
            tmp += str(np.where(prediction[0] == entry)[0])
            tmp += ":\t"
            tmp += "{:.2f}".format(entry * 100)
            tmp += "%\n"
        messagebox.showinfo("Details", str(tmp))
        self.__lbl_forecast.config(text="Identified Number: {}".format(self.__field.get_forecast()))

    def delete(self):
        print("DELETE")
        self.__canvas.delete("all")
        self.__field.init_field()

    def on_button_down(self, event):
        self.__coordinates = (event.x, event.y)
        self.write_to_field(event)

    def on_move(self, event):
        self.__canvas.create_line((self.__coordinates[0], self.__coordinates[1], event.x, event.y))
        self.__coordinates = (event.x, event.y)
        self.write_to_field(event)
        self.__lbl_forecast.config(text="Identified Number: {}".format(self.__field.get_forecast()))

    def write_to_field(self, event):
        if event.x < 0 or event.x > 150 or \
                event.y < 0 or event.y > 150:
            return

        x, y = event.x, event.y
        x, y = self.map_value(x, 0, 150, 0, 27), self.map_value(y, 0, 150, 0, 27)
        self.__field.write(x, y)

    @staticmethod
    def map_value(value, min_old, max_old, min_new, max_new):
        return int((value - min_old) * (max_new - min_new) / (max_old - min_old) + min_new)

    def run(self):
        self.__window.mainloop()


if __name__ == '__main__':
    UI().run()
