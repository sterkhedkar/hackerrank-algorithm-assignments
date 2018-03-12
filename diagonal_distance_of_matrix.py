import math

def get_diagonal_distance(matrix):
    distance = 0
    for index, element in enumerate(matrix):
        left = element[index]
        right = element[len(element) - index - 1]
        # print "Left\t\tRight"
        # print left,"\t\t",right
        distance += left - right
    return int(math.fabs(distance))



### Driver code
input_matrix = [
    [-10,2,3,10],
    [4,0,0,9],
    [7,0,0,0],
    [0,2,4,-10]
]

distance = get_diagonal_distance(input_matrix)
print "\nThe Distance Between the Diagonals of a Matrix: ", distance,"\n\n"