import sys

def Get_File_Data(filename):
	input_file = open(filename,"r")

	rows = []

	for line in input_file:
		datas = []
		line = line.rstrip('\n')
		
		data_str = line.split(", ")
		for data in data_str:
			datas.append(float(data))

		rows.append(datas)

	input_file.close()
	del input_file, line, datas, data_str, data
	return rows

def Write_to_File(filename, result):
    output_file = open(filename ,'w')
    for i in xrange(0,len(result)):
    	output_file.write(str(result[i]))
    	output_file.write('\n')
    output_file.close()
    del output_file

def Get_Result(datas):
	locations = []
	for i in xrange(1,len(datas)):
		row_locations = []
		for j in xrange(0,len(datas[i])):
			location = int(0)
			if j == 0:
				#		0	1
				#		x
				if datas[i-1][j] < datas[i-1][j+1]:
					min = datas[i-1][j]
				else:
					min = datas[i-1][j+1]
					location = 1
			elif j == (len(datas[i]) - 1):
				#	-1	0
				#		x
				if datas[i-1][j-1] < datas[i-1][j]:
					min = datas[i-1][j-1]
					location = -1
				else:
					min = datas[i-1][j]
			else:
				#	-1	0	1
				#		x

				#Check -1 and 0
				if datas[i-1][j-1] < datas[i-1][j]:
					min = datas[i-1][j-1]
					location = -1
				else:
					min = datas[i-1][j]
				#Check min and 1
				if min > datas[i-1][j+1]:
					min = datas[i-1][j+1]
					location = 1
			datas[i][j] = datas[i][j] + min
			row_locations.append(location)
			del min, location
		locations.append(row_locations)
		del j, row_locations
	del i
	
	result = []
	for i in xrange(0,len(datas)):
		if i == 0:
			row_result = []
			row_result_row = len(datas) - 1
			row_result_col = 0
			for j in xrange(1,len(datas[len(datas) - 1])):
				if datas[row_result_row][row_result_col] > datas[row_result_row][j]:
					row_result_col = j
			del j
			row_result.append(row_result_row)
			row_result.append(row_result_col)
			row_result.append(datas[row_result_row][row_result_col])

			result.append("Min Seam: " + str(row_result[2]))
			result.append(row_result)
			del row_result
		else:
			row = result[i][0] - 1
			col = result[i][1]
			row_result = []
			row_result.append(row)
			row_result.append(col + locations[row][col])
			row_result.append(datas[row][col + locations[row][col]])
			result.append(row_result)
			del row, col, row_result
	return result


print("Input File: " + sys.argv[1] + "\n" + "Output File:" + sys.argv[1].split('.')[0] + "_trace.txt")
result = Get_Result(Get_File_Data(sys.argv[1]))
Write_to_File(sys.argv[1].split('.')[0] + "_trace.txt", result)