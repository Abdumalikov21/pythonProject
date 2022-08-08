from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

oyna = Ursina()
osmon_texture = load_texture('assets/skybox.png')


class Voxel(Button):
    def init(self, position=(0, 0, 0)):
        super().init__(
            position=position,
            model='cube',
            origin_y=0.5,
            texture='white_cube',
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5,
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)
        elif key == 'right mouse down':
            destroy(self)

        def init(self):
            super().init(
                parent=scene)

class osmon(Entity):
        model = 'sphere'
        texture = osmon_texture
        double_sided = True


for x in range(20):
    for z in range(20):
        voxel = Voxel(position=(x, 0, z))

scale = 150
oyinchi = FirstPersonController()
osmon = osmon()
oyna.run()
