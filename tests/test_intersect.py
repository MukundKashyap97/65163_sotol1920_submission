from pygeo.intersect import (
    intersection,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from pygeo.objects import Point, Ray, Sphere, Triangle
from numpy import array_equal

# intersect


# _intersect_ray_with_sphere
def test_intersection__sphere_center_at_origin__given_tangent_ray__return_true():
    assert (intersection(Ray((-3,1,0),(1,0,0)),Sphere((0,0,0),1.0)) == Point([0,1,0]))

def test_intersection__sphere_center_at_origin__given_ray_that_intersects_at_two_points__return_true():
    assert array_equal(intersection(Ray((-2,0,0),(1,0,0)),Sphere((0,0,0),1.0)),[Point([-1,0,0]),Point([1,0,0])]) is True

def test_intersection__sphere_center_at_origin__given_ray_that_intersects_at_no_points__return_true():
    assert (intersection(Ray((-2,1.5,0),(1,0,0)),Sphere((0,0,0),1.0)) == None)

def test_intersection__sphere_center_at_origin__given_ray_that_originates_inside_sphere__return_true():
    assert (intersection(Ray((-0.5,0,0),(1,0,0)),Sphere((0,0,0),1.0))==Point([1,0,0]))

def test_intersection__sphere_center_elsewhere__given_tangent_ray__return_true():
    assert (intersection(Ray((-3,1,0),(1,0,0)),Sphere((1,1,1),1.0))==Point([1,1,0]))

def test_intersection__sphere_center_elsewhere__given_ray_that_intersects_at_two_points__return_true():
    assert array_equal(intersection(Ray((-2,1,1),(1,0,0)),Sphere((1,1,1),1.0)),[Point([0,1,1]),Point([2,1,1])]) is True

def test_intersection__sphere_center_elsewhere__given_ray_that_intersects_at_no_points__return_true():
    assert (intersection(Ray((-2,1.5,0),(1,0,0)),Sphere((1,1,1),1.0)) == None)

def test_intersection__sphere_center_elsewhere__given_ray_that_originates_inside_sphere__return_true():
    assert (intersection(Ray((1,1,1),(0,0,1)),Sphere((1,1,1),1.0))==Point([1,1,2]))

# _intersect_ray_with_triangle
