import cv2
import matplotlib.pyplot as plt
import numpy as np


def resize_image(imagepath,size = (420,640)):
    img = cv2.imread(imagepath)
    resized_image = cv2.resize(img,size)
    return resized_image


def blur_image(imagepath):
    Gaussian = cv2.GaussianBlur(imagepath, (7, 7), 0)
    return Gaussian

def remove_background(imagepath):
    image = cv2.imread(imagepath)
    # Create a mask with the same size as the image
    mask = np.zeros(image.shape[:2], np.uint8)
    # Define the rectangle that contains the foreground object
    rect = (50, 50, image.shape[1] - 100, image.shape[0] - 100)
    # Initialize the foreground and background models for GrabCut
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    # Apply GrabCut algorithm
    cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    # Modify the mask to create a binary mask for the foreground
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    # Create the final image with the background removed
    removed_background = image * mask2[:, :, np.newaxis]
    return removed_background







