from pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from pygeo.objects import Ray, Sphere, Triangle
from numpy import array_equal

# intersect


# _intersect_ray_with_sphere
def test__intersect_ray_with_sphere__sphere_center_at_origin__given_tangent_ray__return_true():
    assert array_equal(_intersect_ray_with_sphere(Ray((-3,1,0),(1,0,0)),Sphere((0,0,0),1.0)),[[0,1,0]]) is True

def test__intersect_ray_with_sphere__sphere_center_at_origin__given_ray_that_intersects_at_two_points__return_true():
    assert array_equal(_intersect_ray_with_sphere(Ray((-2,0,0),(1,0,0)),Sphere((0,0,0),1.0)),[[-1,0,0],[1,0,0]]) is True

def test__intersect_ray_with_sphere__sphere_center_at_origin__given_ray_that_intersects_at_no_points__return_true():
    assert (_intersect_ray_with_sphere(Ray((-2,1.5,0),(1,0,0)),Sphere((0,0,0),1.0)) == None)

def test__intersect_ray_with_sphere__sphere_center_at_origin__given_ray_that_originates_inside_sphere__return_true():
    assert array_equal(_intersect_ray_with_sphere(Ray((-0.5,0,0),(1,0,0)),Sphere((0,0,0),1.0)),[[1,0,0]]) is True

def test__intersect_ray_with_sphere__sphere_center_elsewhere__given_tangent_ray__return_true():
    assert array_equal(_intersect_ray_with_sphere(Ray((-3,1,0),(1,0,0)),Sphere((1,1,1),1.0)),[[1,1,0]]) is True

def test__intersect_ray_with_sphere__sphere_center_elsewhere__given_ray_that_intersects_at_two_points__return_true():
    assert array_equal(_intersect_ray_with_sphere(Ray((-2,1,1),(1,0,0)),Sphere((1,1,1),1.0)),[[0,1,1],[2,1,1]]) is True

def test__intersect_ray_with_sphere__sphere_center_elsewhere__given_ray_that_intersects_at_no_points__return_true():
    assert (_intersect_ray_with_sphere(Ray((-2,1.5,0),(1,0,0)),Sphere((1,1,1),1.0)) == None)

def test__intersect_ray_with_sphere__sphere_center_elsewhere__given_ray_that_originates_inside_sphere__return_true():
    assert array_equal(_intersect_ray_with_sphere(Ray((1,1,1),(0,0,1)),Sphere((1,1,1),1.0)),[[1,1,2]]) is True

# _intersect_ray_with_triangle
