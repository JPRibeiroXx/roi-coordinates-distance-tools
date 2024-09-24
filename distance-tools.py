# Library import
import pandas as pd
import tkinter
from tkinter import filedialog

# Find data
tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
print("Select the CSV file containing the coordinates of the set of points")
point_filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

print("Select the CSV file containing the coordinates of the ROI corners")
rect_filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

# Read point data
points = pd.read_csv(point_filename)
# Read rectangle data
roi = pd.read_csv(rect_filename)

# Conversion to array
points = points.to_numpy()
roi = roi.to_numpy()

# Definition of rectangle class for ease
class rectangle:
    def __init__(self, rect):
        self.top_left = [rect[0], rect[1]]
        self.top_right = [rect[2], rect[3]]
        self.bottom_left = [rect[4], rect[5]]
        self.bottom_right = [rect[6], rect[7]]

# Distance to a line segment
def dist(rect_1, rect_2, point): # rect_1 and rect_2 correspond to corners of a rectangle forming a line segment of its perimeter
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
for i in range(0, len(roi)):
    rects.append(rectangle(roi[i]))
    
# Distance calculation
distances = []
for point in points:
    min_dist = 1E10
    for rect in rects:
        if (rect.top_right[0]>=point[0]) & (point[0]>=rect.top_left[0]): # check if x coordinate is in bounds
            if (rect.top_left[1]>=point[1]) & (point[1]>=rect.bottom_left[1]):  # check if y coordinate is in bounds
                min_dist = 0 # if yes, distance is 0 as the point is inside the rectangle
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
    distances.append([point[0], point[1], min_dist])

# File output
output = pd.DataFrame(distances, columns = ['x', 'y', 'Distance'])
print("Select save location and name for output CSV file")
output_path = tkinter.filedialog.asksaveasfilename(filetypes=[("CSV files", "*.csv")])
output.to_csv(output_path+'.csv', index = False)
