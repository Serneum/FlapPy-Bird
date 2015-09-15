from obstacles.obstacle import Obstacle

class Platform(Obstacle):
    def __init__(self, x, y, width, height, vel_x, color):
        Obstacle.__init__(self, x, y, width, height, vel_x, color)