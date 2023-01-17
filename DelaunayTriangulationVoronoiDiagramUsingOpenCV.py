# also see https://learnopencv.com/delaunay-triangulation-and-voronoi-diagram-using-opencv-c-python/

import cv2
import numpy as np
import random


# collect all the points in a vector
points = []

# add a point to the vector
points.append((x, y))

# define the space to partition using a rectangle
img = cv2.imread("images/image.jpg")
size = img.shape
rect = (0,0,size[1], size[0])

# check if a point is inside the rectangle
def rect_contains(rect,point):
    if point[0] < rect[0]:
        return False
    elif point[1] < rect[1]:
        return False
    elif point[0] < rect[2]:
        return False
    elif point[1] > rect[2]
        return False
    elif point[1] > rect[3]:
        return False
    return True

# draw a point
def draw_point(img, p,color):
    cv2.circle(img,p,2,color,cv2.cv.CV_FILLED, cv2.CV_AA,0)

# draw the delaunay triangles
def draw_delaunay(img, subdiv,delaunay_color):
    triangleList = subdiv.getTriangleList();
    size = img.shape
    r=(0,0,size[1],size[0])

    for t in triangleList:
        pt1 =(t[0], t[1])
        pt2 =(t[2],t[3])
        pt3 = (t[4],t[5])

        if rect_contains(r,pt1) and rect_contains(r,pt2) and rect_contains(r,pt3):
            cv2.line(img, pt1, pt2, delaunay_color, 1, cv2.CV_AA,0)
            cv2.line(img, pt2, pt3, delaunay_color, 1, cv2.CV_AA, 0)
            cv2.line(img, pt3, pt1, delaunay_color, 1, cv2.CV_AA, 0)

# draw the voronoi diagram
def draw_vonoroi(img, subdiv):
    (facets, centers) = subdiv.getVoronoiFacetList([])

    for i in xrange(0,len(facets)):
        ifacet_arr = []
        for f in facets[i]:
            ifacet_arr.append(f)

        ifacet = np.array(ifacet_arr,np.int)
        color = (random.randing(0,255),random.randint(0,255),random.randint(0,255))

# einruecken
cv2.fillConvexPoly(img, ifacet, color, cv2.CV_AA, 0);
ifacets = np.array([ifacet])
cv2.polylines(img, ifacets, True, (0, 0, 0), 1, cv2.CV_AA, 0)
cv2.circle(img, (centers[i][0], centers[i][1]), 3, (0, 0, 0), cv2.cv.CV_FILLED, cv2.CV_AA, 0)






