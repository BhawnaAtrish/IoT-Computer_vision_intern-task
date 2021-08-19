
# BHAWNA ATRISH
# IoT & Computer Vision Intern
# Task #2
# Color Identification in Images

import cv2
from scipy.spatial import KDTree
import webcolors
from webcolors import CSS3_HEX_TO_NAMES,hex_to_rgb,hex_to_name,hex_to_rgb_percent


img=cv2.imread('dfaf.png')
def convert_rgb_to_names(rgb_tuple):
    # a dictionary of all the hex and their respective names in css3
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    cv2.rectangle(img,(0,0),(800,70),(0,0,0),-1)
    cv2.putText(img,str(names[index]),(270,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    cv2.imshow('image', img)
    return f'Colour : {names[index]}'

img = cv2.resize(img,(800,600))
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        b=img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]
        print(convert_rgb_to_names((r,g,b)))

cv2.imshow('image',img)
cv2.setMouseCallback('image',click)
cv2.waitKey(0)
cv2.destroyAllWindows()