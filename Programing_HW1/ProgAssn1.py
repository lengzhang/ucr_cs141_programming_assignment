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


list = Read_Points_From_Command_Line_File()
print list
Write_to_File("output.txt", list)
