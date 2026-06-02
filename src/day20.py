import re
from math import sqrt
from itertools import combinations


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __rmul__(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def norm(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


class Particle:
    def __init__(self, id, initial_position, velocity, acceleration):
        self.id = id
        self.initial_position = initial_position
        self.velocity = velocity
        self.acceleration = acceleration

    def position(self, t):
        return self.initial_position + (t * self.velocity) + (t*(t + 1)/ 2 * self.acceleration)
    
    def collision_times(self, other):
        # x = at² + bt + c
        a = (self.acceleration.x - other.acceleration.x) / 2
        b = self.velocity.x - other.velocity.x + (self.acceleration.x - other.acceleration.x) / 2
        c = self.initial_position.x - other.initial_position.x
        delta = b**2 - 4 * a * c

        collisions = []

        if a != 0:
            if delta >= 0:
                t1 = round((-b + sqrt(delta)) / (2 * a))
                if self.position(t1) == other.position(t1) and t1 >= 0:
                    collisions.append(t1)

                t2 = round((-b - sqrt(delta)) / (2 * a))
                if self.position(t2) == other.position(t2) and t2 >= 0:
                    collisions.append(t2)        
        elif b != 0:
            t = round(-c/b)
            if self.position(t) == other.position(t) and t >= 0:
                collisions.append(t)
        elif self.initial_position == other.initial_position:
            collisions.append(0)
        
        return tuple(collisions)



def part1(input_file):
    min_distance = float("+inf")
    best_particle = None

    with open(input_file, 'r') as f:
        for particle_id, line in enumerate(f):
            particle_data = tuple(map(lambda it : tuple(map(int, it)), re.findall("<(-*[0-9]+),(-*[0-9]+),(-*[0-9]+)>", line)))

            particle = Particle(particle_id, Vector3(*particle_data[0]), Vector3(*particle_data[1]), Vector3(*particle_data[2]))
            distance = particle.position(10**6).norm()

            if distance < min_distance:
                min_distance = distance
                best_particle = particle_id

    return best_particle


def part2(input_file):
    particles = set()
    with open(input_file, 'r') as f:
        for particle_id, line in enumerate(f):
            particle_data = tuple(map(lambda it : tuple(map(int, it)), re.findall("<(-*[0-9]+),(-*[0-9]+),(-*[0-9]+)>", line)))
            particles.add(Particle(particle_id, Vector3(*particle_data[0]), Vector3(*particle_data[1]), Vector3(*particle_data[2])))
    
    collisions = []
    for p1, p2 in combinations(particles, 2):
        for collision_time in p1.collision_times(p2):
            collisions.append((collision_time, p1.id, p2.id))
    collisions.sort()
    
    deleted_particles = set()
    particles_to_be_deleted = set()
    current_time = 0
    while collisions:
        time, p1, p2 = collisions.pop(0)

        if time != current_time:
            deleted_particles.update(particles_to_be_deleted)
            particles_to_be_deleted.clear()
            current_time = time

        if p1 in deleted_particles or p2 in deleted_particles:
            continue

        particles_to_be_deleted.add(p1)
        particles_to_be_deleted.add(p2)

    deleted_particles.update(particles_to_be_deleted)

    return len(particles) - len(deleted_particles)


print(part1("input\\day20.txt"))
print(part2("input\\day20.txt"))