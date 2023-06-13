from lib.Math.VectorSpace import VectorSpace
from lib.RCEngine.BasicClasses.Game import *
from lib.RCEngine.BasicClasses.EntityList import EntityList
from config.globals import *

if __name__ == '__main__':
    # Создание системы координат
    cs = CoordinateSystem(Point(elements=[0, 0, 0]),
                          VectorSpace(
                              [Vector(elements=[1, 0, 0]), Vector(elements=[0, 1, 0]), Vector(elements=[0, 0, 1])]))
    # Инициализация игры
    game = Game(cs)
    # Инициализация игры
    camera = game.Camera()(
        position=Point(elements=[1, 1, -80]),
        fov=fov, vfov=None,
        draw_dist=draw_dist,
        look_at=Point(elements=[1, 1, 1])
    )

    game.entities = EntityList()

    # Инициализация игрового объекта
    hyper_ellipsoid = game.HyperEllipsoid()(
        pos=Point(elements=[1, 1, -8]),
        dir=Vector(elements=[1, 1, 0]),
        semiaxes=[0.5, 0.5, 0.5]
    )
    game.entities.append(hyper_ellipsoid)

    canvas = game.Canvas()(canvas_h, canvas_v)
    console = game.Console()

    # запуск игры
    console.draw(canvas, console)
