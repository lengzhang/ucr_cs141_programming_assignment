import sys

class Point :
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val

    def __repr__(self):
        return "(%.2f, %.2f)" % (self.x, self.y)

def Read_Points_From_Command_Line_File():
    points = []
    number_of_args = len(sys.argv)
    file = open(sys.argv[1],"r")

    for line in file:
        line.strip()
        x_y = line.split(" ")
        points.append(Point(float(x_y[0]),float(x_y[1])))

    return points

def Write_to_File(filename, s):
    output = open(filename ,'w')
    output.write(str(s))
    output.write('\n')

def Sort_by_x(points):
    for i in range(0,len(points)-1):
        for j in range(i+1,len(points)):
            if float(points[i].x) > float(points[j].x):
                temp = points[i]
                points[i] = points[j]
                points[j] = temp
    return points

def Sort_by_y(points):
    for i in range(0,len(points)-1):
        for j in range(i+1,len(points)):
            if float(points[i].y) > float(points[j].y):
                temp = points[i]
                points[i] = points[j]
                points[j] = temp
    return points

def Brute_Force(points):
    min_distance = 0;
    for i in range(0,len(points)-1):
        for j in range(i+1, len(points)):
            distances = ( (points[i].x - points[j].x) ** 2 + (points[i].y - points[j].y) ** 2 ) ** 0.5
            if i == 0 and j == 1:
                min_distance = distances
            else:
                if min_distance > distances:
                    min_distance = distances
    return min_distance

def Divide_and_Conquer(points):
    # Step 1:   Find a value mid_x for which exactly half the points have x_i < mid_x, and half have x_i > mid_x.
    #           On this basis, split the points into two groups L and R.
    mid_x = (points[0].x + points[len(points) - 1].x) / 2
    #if (len(points) % 2) == 0:
    #    mid_x = (points[(len(points) / 2) - 1].x + points[len(points) / 2].x) / 2
    #else:
    #    mid_x = (points[len(points) // 2].x + points[(len(points) // 2) + 1].x) / 2
    points_L = []
    points_R = []
    for i in range(0,len(points)):
        if points[i].x < mid_x:
            points_L.append(points[i])
        else:
            points_R.append(points[i])
    # Step 2:   Recursively n_d the closest pair in L and in R. Say these pairs are p_L1 and p_L2 in L and
    #           p_R1 and q_R2 in R, with distances d_L and d_R respectively. Let d be the smaller of these
    #           two distances.
    d_L = Brute_Force(points_L)
    d_R = Brute_Force(points_R)
    d = 0
    if d_L > d_R:
        d = d_R
    else:
        d = d_L
    # Step 3:   It remains to be seen whether there is a point in L and a point in R that are less than distance d
    #           apart from each other. To this end, discard all points with x_i < x - d or x_i > x + d and sort the
    #           remaining points by their y-coordinate.
    new_points = []
    for i in range(0,len(points)):
        if points[i].x >= (mid_x - d) and points[i].x <= (mid_x + d):
            new_points.append(points[i])
    # Step 4:   Case 1 - Less than 2 points with x_i < x - d or x_i > x + d in new_points
    #                    return the minimized distance between d_L and d_R
    if len(new_points) < 2:
        return d
    #           Case 2 - More than 1 points with x_i < x - d or x_i > x + d in new_points
    #                    Sort new_points and list, and for each point, compute its distance
    #                    to the subsequent points in the list.
    #                    Return the minimized distance.
    else:
        new_points = Sort_by_y(new_points)
        d_M = Brute_Force(new_points)
        if d_M > d:
            return d
        else:
            return d_M

import timeit
points = Read_Points_From_Command_Line_File()
points = Sort_by_x(points)

#Brute Force
start_BF = timeit.default_timer()
min_distance_by_BF = Brute_Force(points)
stop_BF = timeit.default_timer()
BF_time = float(stop_BF - start_BF)

#Divide and Conquer
start_DC = timeit.default_timer()
min_distance_by_DC = Divide_and_Conquer(points)
stop_DC = timeit.default_timer()
DC_time = float(stop_DC - start_DC)

print("Brute Force time: " + str(BF_time))
print("Divide and Conquer time: " + str(DC_time))

Write_to_File(sys.argv[1].split('.')[0] + "_distance.txt", min_distance_by_DC)
