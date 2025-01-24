import cv2
import numpy as np
import pandas as pd
from PIL import Image
import os
import datetime
import glob

path = 'E:\\Py\\Picture\\*'  # указываем путь с маской * для всех файлов в папке
files_list = glob.glob(path)
for file in files_list:
    image = cv2.imread(file)  # загружаем изображение
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # преобразование в цветовой диапазон серого
    edges = cv2.Canny(gray, 50, 150)  # извлечение контуров с помощью алгоритма Canny
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_of_objects = len(contours)  # кол-во контуров равно общему числу объектов
    current_time = datetime.datetime.now()  # время сканирования
    file_name = os.path.splitext(file)[0]  # имя файла без расширения
    data = {'Time': current_time, 'Filename': file_name, 'Number of objects': num_of_objects}
    # создаем DataFrame
    df = pd.DataFrame(data, index=[0])
    # рисуем зеленые контуры на изображении
    for i in range(len(contours)):
        cv2.drawContours(image, contours, i - 1, (0, 255, 0), 1)
    # сохраняем картинку с контурами в файл
    cv2.imwrite('E:\\Py\\Out\\{}_{}.jpg'.format(file_name, num_of_objects), image)
    df.to_csv('E:\\Py\\Out\\output.csv', mode='a', header=False, index=False)