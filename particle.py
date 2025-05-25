import numpy as np
class Particle:
    def __init__(self, position, velocity, acceleration, mass, radius, color, id):
        self.position = np.array(position, dtype=float) #[x, y] ou [x, y, z]
        self.velocity = np.array(velocity, dtype=float) #[vx, vy] ou [vx, vy, vz]
        self.acceleration = np.array(acceleration, dtype=float) #[ax, ay] ou [ax, ay, az]
        self.mass = float(mass)
        self.radius = float(radius)
        self.color = color
        self.id = id


        self.force = np.zeros_like(self.position)
