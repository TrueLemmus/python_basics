'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.

'''


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        returned = ""
        for row in self.data:
            for el in row:
                returned += str(el) + " "
            returned += "\n"
        return returned

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                summa = other.data[i][j] + self.data[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.data):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(matrix1)
print(matrix1 + matrix2)
