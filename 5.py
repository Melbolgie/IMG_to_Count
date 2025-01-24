import cv2
import os
import csv


def count_objects(img):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # преобразование в цветовой диапазон серого
    edges = cv2.Canny(gray, 50, 150)  # извлечение контуров с помощью алгоритма Canny
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return len(contours)


def save_img_with_cnt(img):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # преобразование в цветовой диапазон серого
    edges = cv2.Canny(gray, 50, 150)  # извлечение контуров с помощью алгоритма Canny
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = len(contours)

    if cnt > 0:
        img_cnt = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    else:
        img_cnt = img

    return img_cnt, cnt


def main():
    folder_path = r'E:\\Py\\Picture\\'  # change the path to your folder with images
    save_folder = r'E:\\Py\\Out\\'  # change this path for saving counted images and csv file
    os.makedirs(save_folder, exist_ok=True)

    img_list = [f for f in os.listdir(folder_path) if f[-3:].lower() == 'jpg']  # create list of jpg files in the folder

    with open(os.path.join(save_folder, r'E:\\Py\\Out\\output.csv'), 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for img in img_list:
            img_path = os.path.join(folder_path, img)
            count = count_objects(img_path)
            img_cnt, cnt = save_img_with_cnt(img_path)

            if cnt > 0:
                cv2.imwrite(os.path.join(save_folder, f'{os.path.splitext(img)[0]}.jpg'),
                            img_cnt)  # save image with counted contours
            writer.writerow([img, count])  # write to csv file

    print('Выполнено, все объекты найдены!')


if __name__ == '__main__':
    main()
