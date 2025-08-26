class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        max_diagonal = 0
        max_area = 0
        val = []

        for length,width in dimensions:
            curr_dia = sqrt(length*length + width*width )
            curr_area = length*width

            if curr_dia > max_diagonal: 
                max_diagonal = curr_dia
                max_area = curr_area
            elif curr_dia == max_diagonal:
                max_area = max(max_area, curr_area)

            
        return max_area
