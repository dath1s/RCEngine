from lib.Math.VectorSpace import VectorSpace
from lib.RCEngine.BasicClasses.Game import *
from lib.EventSystem import EventSystem
from lib.RCEngine.BasicClasses.EntityList import EntityList
from config.globals import *

if __name__ == '__main__':
    cs = CoordinateSystem(Point(elements=[0, 0, 0]),
                          VectorSpace(
                              [Vector(elements=[1, 0, 0]), Vector(elements=[0, 1, 0]), Vector(elements=[0, 0, 1])]))

    game = Game(cs)
    camera = game.Camera()(
        position=Point(elements=[1, 1, -80]),
        fov=fov, vfov=None,
        draw_dist=draw_dist,
        look_at=Point(elements=[1, 1, 1])
    )

    event_system = EventSystem()

    event_system.add("move")
    event_system.add("rotate_h")
    event_system.add("rotate_v")

    event_system.handle("move", camera.move)
    event_system.handle("rotate_h", camera.planar_rotate)
    event_system.handle("rotate_v", camera.set_direction)

    game.entities = EntityList()
    game.es = event_system

    hyper_ellipsoid = game.HyperEllipsoid()(
        pos=Point(elements=[1, 1, -8]),
        dir=Vector(elements=[1, 1, 0]),
        semiaxes=[0.5, 0.5, 0.5]
    )
    game.entities.append(hyper_ellipsoid)

    canvas = game.Canvas()(canvas_h, canvas_v)
    console = game.Console()

    console.draw(canvas, console)
