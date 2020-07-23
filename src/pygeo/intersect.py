from .objects import Point, Ray, Sphere, Triangle
from numpy import subtract,dot,sqrt,array,all


def intersect(first_object, second_object):
    ...


def _intersect_ray_with_sphere(ray, sphere):
    difference_o_c = subtract(ray._origin,sphere._center)
    nabla = (dot(ray._direction,difference_o_c))**2 - ((dot(difference_o_c,difference_o_c)) - sphere._radius**2)
    if nabla < 0:
        print("Specified ray and sphere do not intersect")
        return None
    elif nabla == 0:
        d = -1*dot(ray._direction,difference_o_c)
        return array([(ray._origin) + (d*ray._direction)])
    else:
        d = array([-1*dot(ray._direction,difference_o_c)-sqrt(nabla),-1*dot(ray._direction,difference_o_c)+sqrt(nabla)])
        points = []
        for d in d[d>=0]:
            points.append((ray._origin) + (d*ray._direction))
        return array(points)
def _intersect_ray_with_triangle(ray, triangle):
    ...
