import os
import cv2
import numpy as np
import pandas as pd
from PIL import Image
import glob
import datetime

path = 'E:\\Py\\Picture\\*.jpg'  # указываем путь с маской * для всех файлов в папке .jpg
files_list = glob.glob(path)
for file in files_list:
    image = cv2.imread(os.path.join(path, file))  # загружаем изображение
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_of_objects = len(contours)
    current_time = datetime.datetime.now()
    file_name = os.path.splitext(file)[0]
    #contours_image = np.zeros(image.shape[:2], dtype=np.uint8)
    for i in range(len(contours)):
        cv2.drawContours(image, contours, i - 1, (0, 255, 0), 2)  # рисуем зеленые контуры на изображении
    cv2.imwrite('E:\\Py\\Out\\{}.jpg'.format(file_name), image)
    data = {'Time': current_time, 'Filename': file_name, 'Number of objects': num_of_objects}
    df = pd.DataFrame(data, index=[0])  # создаем DataFrame
    df.to_csv('E:\\Py\\Out\\output.csv', mode='a', header=False, index=False)