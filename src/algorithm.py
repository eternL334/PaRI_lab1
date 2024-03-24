import numpy as np
import cv2 as cv

def get_mask(img, lower, upper):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue_mask = cv.inRange(hsv[:, :, 0], int(lower[0]), int(upper[0]))
    saturation_mask = cv.inRange(hsv[:, :, 1], int(lower[1]), int(upper[1]))
    value_mask = cv.inRange(hsv[:, :, 2], int(lower[2]), int(upper[2]))
    mask = cv.inRange(hsv, lower, upper)
    return mask, hue_mask, saturation_mask, value_mask

def get_components(img, size=0):
    n, res, stats, centroids = cv.connectedComponentsWithStats(img)
    size_stat = stats[:, -1]
    small, = np.where(size_stat < size)
    img[np.isin(res, small)] = 0
    return n - len(small), img 
    