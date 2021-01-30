import numpy as np
import random as rnd

def matrix_abs(n,m):
    arr = np.random.randint(-50, 100, size=(n, m))#рандом
    print(arr)
    arr = np.array(arr) # преобразование к массиву нампай
    arrt = arr.transpose()  # транспонируем матрицу для более быстрой работы
    arrta = np.abs(arrt) #ищем абсолютные
    sums = np.sum(arrta, axis=1) #находим сумму
    row_idx = np.argmax(sums)
    el = np.max(arrt[row_idx])#находим максимальный
    saver(el,arr)
    print(el)
#Комментарий!
def saver(element,array):#Метод сохранения в файл
    with open("final.npy","wb") as f:
        np.save(f,element)
        np.save(f,array)

if __name__ == "__main__":
    while True:
        m=int(input("Vvod M :"))
        n=int(input("Vvod N :"))
        matrix_abs(n,m)
#more comments!!!!!!!