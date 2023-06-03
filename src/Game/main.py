from lib.RCEngine.BasicClasses import Entity
from lib.Math.Point import Point
from lib.Math.Vector import Vector
from lib.Math.VectorSpace import VectorSpace
from lib.Math.CoordinateSystem import CoordinateSystem


if __name__ == '__main__':
    v1 = Vector(elements=[1, 0, 0])
    v2 = Vector(elements=[0, 1, 0])
    v3 = Vector(elements=[0, 0, 1])
    vs = VectorSpace([v1, v2, v3])
    point = Point(3)

    cs = CoordinateSystem(point, vs)

    ent = Entity.Entity(cs)
    ent.kek = 1
    print(ent.kek)
    print(ent.properties)

