#Write OOP classes to handle the following scenarios:
#A user can create and view 2D coordinates
#A user can find out the distance between 2 coordinates
#A user can find find the distance of a coordinate from origin
#A user can check if a point lies on a given line
#A user can find the distance between a given 2D point and a given line


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"Point({self.x},{self.y})"  
    def euclidean_distance(self,other):
        return ((self.x-other.x)**2 +(self.y-other.y)**2)**0.5
    def distance_from_origin(self):
        return self.euclidean_distance(Point(0,0))
         
    
p1=Point(0,0)
p2=Point(10,10)
print(p1.distance_from_origin() )
