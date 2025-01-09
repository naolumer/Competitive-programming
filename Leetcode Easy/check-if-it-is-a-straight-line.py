class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]
        xi = coordinates[0][0]      
        yi = coordinates[0][1]

        for i in range(len(coordinates)):
            cur_x = coordinates[i][0]
            cur_y = coordinates[i][1]
            if dx*(cur_y-yi)!=dy*(cur_x-xi):      # checking if it satisfies straight line equation
                return False
        return True