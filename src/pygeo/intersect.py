from .objects import Point, Ray, Sphere, Triangle
from numpy import subtract,dot,sqrt,array,all


def intersect(first_object, second_object):
    ...


def _intersect_ray_with_sphere(ray, sphere):
    """ Method to determine intersection of a Ray object and a sphere object.
        Input: ray (of class Ray), sphere (of class Sphere)
        returns:
            0: if there is no intersection
            NumPy array (of objects of Point class): if an intersection exists """
    difference_o_c = subtract(ray._origin,sphere._center)
    nabla = (dot(ray._direction,difference_o_c))**2 - ((dot(difference_o_c,difference_o_c)) - sphere._radius**2)
    if nabla < 0:
        print("Specified ray and sphere do not intersect")
        return None
    elif nabla == 0:
        d = -1*dot(ray._direction,difference_o_c)
        return Point((ray._origin) + (d*ray._direction))
    else:
        d = array([-1*dot(ray._direction,difference_o_c)-sqrt(nabla),-1*dot(ray._direction,difference_o_c)+sqrt(nabla)])
        points = []
        for d in d[d>=0]:
            points.append(Point((ray._origin) + (d*ray._direction)))
        return array(points)
def _intersect_ray_with_triangle(ray, triangle):
    ...
