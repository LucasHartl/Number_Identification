import numpy as np
from tensorflow import keras


class Field:
    def __init__(self):
        self.__model = keras.models.load_model("../Model/output/MNIST-99-Network.h5")
        self.__field = np.zeros([28, 28])

    def write(self, x, y):
        self.__field[y][x] = 1

        if self.__field[y][x+1] != 1:
            self.__field[y][x+1] = 0.5
        if self.__field[y][x-1] != 1:
            self.__field[y][x-1] = 0.5
        if self.__field[y+1][x] != 1:
            self.__field[y + 1][x] = 0.5
        if self.__field[y-1][x] != 1:
            self.__field[y-1][x] = 0.5
        # print(self)

    def init_field(self):
        print("Field initialized")
        self.__field = np.zeros([28, 28])

    def get_forecast(self):
        prediction = self.__model.predict(self.__field.reshape(1, 28, 28, 1))
        # print(prediction)
        # print(np.argmax(prediction))
        return np.argmax(prediction)

    def get_forecast_details(self):
        return self.__model.predict(self.__field.reshape(1, 28, 28, 1))

    def print_model_information(self):
        print(self.__model.summary())

    def __str__(self):
        tmp = ""
        for row in range(28):
            for column in range(28):
                tmp += str(self.__field[row][column])
                tmp += " "
            tmp += "\n"
        return tmp


if __name__ == '__main__':
    field = Field()
    print(field)
    field.print_model_information()
