# Library import
import pandas as pd
import os

# Find data
path = []
for root, dir, files in os.walk("C:"):
    if "ARPC2_Spectrin_NND_Analysis.xlsx" in files: # looks for excel file
        path = os.path.join(root, "ARPC2_Spectrin_NND_Analysis.xlsx")
        
if path == []:
    raise Exception("File not found")

# Read ARPC2 data
arpc2 = pd.read_excel(io=path, header=2, usecols='ED,EE', nrows=41)
# Read Spectrin data
spectrin = pd.read_excel(io=path, header=2, usecols='EK:ER', nrows=25) # hardcoded because the function hates assymetrical tables

# Conversion to array
arpc2 = arpc2.to_numpy()
spectrin = spectrin.to_numpy()

# Definition of rectangle class for ease
class rectangle:
    def __init__(self, xtl, ytl, xtr, ytr, xbl, ybl, xbr, ybr):
        self.top_left = [xtl, ytl]
        self.top_right = [xtr, ytr]
        self.bottom_left = [xbl, ybl]
        self.bottom_right = [xbr, ybr]

# Distance to a line segment
def dist(rect_1, rect_2, point): # x3,y3 is the point
    px = rect_2[0]-rect_1[0]
    py = rect_2[1]-rect_1[1]

    norm = px*px + py*py

    u =  ((point[0] - rect_1[0]) * px + (point[1] - rect_1[1]) * py) / float(norm)

    if u > 1:
        u = 1
    elif u < 0:
        u = 0

    x = rect_1[0] + u * px
    y = rect_1[1] + u * py

    dx = x - point[0]
    dy = y - point[1]
    
    dist = (dx*dx + dy*dy)**.5

    return dist

# Array of rectangles
rects = []
for i in range(0, len(spectrin)):
    rects.append(rectangle(spectrin[i][0], spectrin[i][1], spectrin[i][2], spectrin[i][3], spectrin[i][4], 
                           spectrin[i][5], spectrin[i][6], spectrin[i][7]))
# Distance calculation
distances = []
for point in arpc2:
    min_dist = 1E10
    for rect in rects:
        if (rect.top_right[0]>=point[0]) & (point[0]>=rect.top_left[0]):
            if (rect.top_left[1]>=point[1]) & (point[1]>=rect.bottom_left[1]):
                min_dist = 0
                continue
            else:
                check = min(dist(rect.top_left, rect.top_right, point), dist(rect.top_right, rect.bottom_right, point), dist(rect.bottom_right, rect.bottom_left, point), dist(rect.bottom_left, rect.top_left, point))
            if min_dist > check:
                    min_dist = check
            else:
                continue
        else:
            check = min(dist(rect.top_left, rect.top_right, point), dist(rect.top_right, rect.bottom_right, point), dist(rect.bottom_right, rect.bottom_left, point), dist(rect.bottom_left, rect.top_left, point))
        if min_dist > check:
            min_dist = check
        else:
            continue
    distances.append(min_dist)

for i in range(0, len(distances)):
    print(distances[i])