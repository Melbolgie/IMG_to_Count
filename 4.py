import cv2
import numpy as np
import os
import csv
from glob import glob


def find_contours(image, threshold):
    # Blur the image and convert it to grayscale
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to the grayscale image
    ret, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    # Find contours in the image
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    return cnts


def create_copy_and_save_image(path, name, countour):
    # Create a copy of the original image and draw contours on it
    img = cv2.imread(path)
    img_contour = img.copy()
    cv2.drawContours(img_contour, countour, -1, (0, 255, 0), 3)

    # Save the image with contours
    name = 'contours_' + name
    cv2.imwrite('E:\\Py\\Out\\' + name, img_contour)


def write_csv(data):
    file_name = "E:\\Py\\Out\\output.csv"

    # Check if the file exists and create it otherwise
    if not os.path.isfile(file_name):
        with open(file_name, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Number of objects'])

    # Write the data in the file
    with open(file_name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([data[0], data[1]])


def main():
    path = "E:\\Py\\Picture\\*"  # Replace with your folder name

    for filename in glob(path):
        image = cv2.imread(filename)
        cnts = find_contours(image, threshold=150)
        count = len(cnts)

        if count:
            create_copy_and_save_image(filename, os.path.basename(filename), cnts)
            write_csv([os.path.basename(filename), count])


if __name__ == '__main__':
    main()
