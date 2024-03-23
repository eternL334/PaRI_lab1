import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def get_mask(img, lower, upper):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower, upper)
    return mask

def get_components(img, size=0):
    n, res, stats, centroids = cv.connectedComponentsWithStats(img)
    size_stat = stats[:, -1]
    small, = np.where(size_stat < size)
    img[np.isin(res, small)] = 0
    return n - len(small), img 
    