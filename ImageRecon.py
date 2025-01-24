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
    folder_path = os.path.join(os.getcwd(), 'images')  # change this path to your images folder (relative)
    save_folder = os.path.join(os.getcwd(), 'out')  # change this path for saving counted images and csv file (relative)
    os.makedirs(save_folder, exist_ok=True)

    img_list = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if
                f[-3:].lower() == 'jpg']  # create list of jpg files in the folder

    with open(os.path.join(save_folder, 'output.csv'), 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for img in img_list:
            count = count_objects(img)
            img_cnt, cnt = save_img_with_cnt(img)

            if cnt > 0:
                cv2.imwrite(os.path.join(save_folder, os.path.basename(img)),
                            img_cnt)  # save image with counted contours
            writer.writerow([os.path.basename(img), count])  # write to csv file

    print('Выполнено, все объекты найдены!')


if __name__ == '__main__':
    main()