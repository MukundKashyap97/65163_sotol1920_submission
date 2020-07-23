import numpy as np


class Point:
    """ Class Point
        Defines a point in 3-dimensional Euclidean space.
        Requires a list/tuple/numpy array as input
        Methods implemented: Addition, Subtraction, Equality"""

    def __init__(self, point):
        self._point = np.array(point, dtype=float)

    def __repr__(self):
        return f"Point({self._point.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._point + other._vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other._vector + self._point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self._point - other._point)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return np.array_equal(other._point, self._point)
        return False


class Vector:
    """ Class Vector.
        Defines a vector in 3-dimensional Euclidean space.
        Requires list/tuple/numpy array as input,
        which defines the components of vector along each coordinate axis.
        Methods implemented: Addition, Subtraction, Equality"""

    def __init__(self, vector):
        self._vector = np.array(vector, dtype=float)

    def __repr__(self):
        return f"Vector({self._vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector + other._vector)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector - other._vector)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False


class Ray:
    """A ray."""
    def __init__(self):
        ...
    def __repr__(self):
        ...
    def __eq__(self, value):
        ...


class Sphere:
    """ Class Sphere
        Requires list/tuple/numpy array (center) and a float/double/string as input (radius)
        Methods implemented: Equality """

    def __init__(self, center, radius):
        self._center = np.array(center,dtype=float)
        self._radius = float(radius)
    def __repr__(self):
        return f"Sphere(Center:{self._center.tolist()}, Radius:{self._radius})"
    def __eq__(self, other):
        if isinstance(other,Sphere):
            flag = False
            if np.array_equal(other._center, self._center) and (other._radius == self._radius):
                flag = True
        return flag

class Triangle:
    """A triangle."""

    ...
