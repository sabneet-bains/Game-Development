from vpython import *
import numpy as np
import random

#--------------------------------Constants-------------------------------------

G_CONSTANT = 6.674e-11
P_RADIUS = 6.378e6
P_MASS = 5.972e24
P_GRAVITY = -9.81
VELOCITY = 10.0
ANGLE = (45.0 * pi) / 180.0
COEFF_REST = 0.9
COEFF_DRAG = 0.0 # random.random()
x = random.randint(1, 10)

#----------------------------------Scene---------------------------------------

scene = canvas(title = 'Space Basketball', width = 1688, height = 800,
        center = vector(0, 0, 3*P_RADIUS), range = 4*P_RADIUS, autoscale = True)

scene.camera.pos = vector(4*P_RADIUS, 0, 8*P_RADIUS)
scene.lights = []

#----------------------------Background Stars-----------------------------------

S_RADIUS = P_RADIUS*52

for i in np.arange(0, 2*pi + 0.5, 0.5):
    for j in np.arange(0, pi + 0.5, 0.5):
        sphere(pos = vector(S_RADIUS*sin(j)*cos(i), S_RADIUS*sin(j)*sin(i), S_RADIUS*cos(j)),
               radius = P_RADIUS/17.5, color = color.white, emissive = True)

#----------------------------------Intro-------------------------------------

intro = text(text = 'A long time ago in a galaxy far,\nfar away....',
             pos = vector(-P_RADIUS/3.7, 0, 0), depth = 0, height = P_RADIUS/7,
             color = vector(0.41, 0.82, 0.78), emissive = True)

scene.waitfor('click')
for i in range(10):
    rate(25)
    intro.opacity = intro.opacity - 0.1
intro.visible = False

intro2 = text(text = 'SPACE \n BALL', pos = vector(-P_RADIUS*7.14, P_RADIUS*1.42, 0),
        depth = 0, height = P_RADIUS*2.85, color = vector(0.89, 0.93, 0.56), emissive = True)

for i in range(100):
    rate(25)
    intro2.height = intro2.height*0.99
    intro2.length = intro2.length*0.99
    intro2.pos.x = intro2.pos.x + P_RADIUS/10
    intro2.pos.y = intro2.pos.y + P_RADIUS/50

intro3 = text(text = 'Soon, you will be presented', pos = vector(P_RADIUS*4, -P_RADIUS*1.42, 0),
    depth = 0, height = P_RADIUS/7, color = vector(0.89, 0.93, 0.56), emissive = True)
intro4 = text(text = '  with a bizarro planet. Just', pos = vector(P_RADIUS*4, -P_RADIUS*1.71, 0),
    depth = 0, height = P_RADIUS/7, color = vector(0.89, 0.93, 0.56), emissive = True)
intro5 = text(text = '         make the basket into', pos = vector(P_RADIUS*4, -P_RADIUS*2, 0),
    depth = 0, height = P_RADIUS/7, color = vector(0.89, 0.93, 0.56), emissive = True)
intro6 = text(text = '                         the moving cart!', pos = vector(P_RADIUS*4, -P_RADIUS*2.28, 0),
    depth = 0, height = P_RADIUS/7, color = vector(0.89, 0.93, 0.56), emissive = True)

for i in range(400):
    rate(30)
    intro3.pos.y = intro3.pos.y + P_RADIUS/140
    intro3.length = intro3.length*1.002
    intro3.opacity = intro3.opacity - 0.005
    intro4.pos.y = intro4.pos.y + P_RADIUS/140
    intro4.length = intro4.length*1.002
    intro4.opacity = intro4.opacity - 0.0033
    intro5.pos.y = intro5.pos.y + P_RADIUS/140
    intro5.length = intro5.length*1.002
    intro5.opacity = intro5.opacity - 0.0024
    intro6.pos.y = intro6.pos.y + P_RADIUS/140
    intro6.length = intro6.length*1.002
    intro6.opacity = intro6.opacity - 0.0018

intro3.visible = False
intro4.visible = False
intro5.visible = False
intro6.visible = False

#-------------------------------Closest Star------------------------------------

closest_star = sphere(pos = vector(P_RADIUS*70, 0, 0), radius = P_RADIUS*10,
    texture = "https://i.imgur.com/XdRTvzj.jpg", emissive = True)
star_light = distant_light(direction = vector(P_RADIUS*70, 0, 0), color = color.white)

#-------------------------------Host Planet-------------------------------------

host_planet = sphere(pos = vector(-P_RADIUS, 0, 0), axis = vector(-200, -5, -500),
    radius = P_RADIUS, texture = "https://i.imgur.com/Mwsa16j.jpg", emissive = True)
host_planet.mass = P_MASS
host_planet.velocity = vector(0, 0, 0)
host_planet.momentum = host_planet.mass * host_planet.velocity

#-----------------------------Natural Satellite---------------------------------

natural_satellite = sphere(pos = vector(P_RADIUS*1.1, 0, 0), radius = P_RADIUS*0.2,
    texture = "https://i.imgur.com/0lAj5pJ.jpg", emissive = True)
natural_satellite.mass = 100
natural_satellite.velocity = vector(0, 5000, 0)
natural_satellite.momentum = natural_satellite.mass * natural_satellite.velocity

#-------------------------------Space Dome---------------------------------------

space_dome = sphere(pos = vector(0, 0, P_RADIUS*3), axis = vector(0, -P_RADIUS/35, 0),
    radius = P_RADIUS, color = color.cyan, opacity = 0.05, emissive = True)
surface =  cylinder(pos = vector(0, 0, P_RADIUS*3), axis = vector(0, -P_RADIUS/35, 0),
    radius = P_RADIUS, texture = textures.stucco, color = vector(0.42, 1, 0.25),
    emissive = False)
ground = cylinder(pos = vector(0, -P_RADIUS/35, P_RADIUS*3), axis = vector(0, -P_RADIUS/17.5, 0),
    radius = P_RADIUS, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
    emissive = True)
pond = cylinder(pos = vector(0, P_RADIUS/50, P_RADIUS*3.5), axis = vector(0, -P_RADIUS/30, 0),
    radius = P_RADIUS/5, texture = textures.stucco, color = vector(0, 0.54, 0.82),
    emissive = True)
sand = cylinder(pos = vector(0, P_RADIUS/150, P_RADIUS*3.5), axis = vector(0, -P_RADIUS/30, 0),
    radius = P_RADIUS/3.8, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
    emissive = True)

for k in range(5):
    cone(pos = vector(-P_RADIUS/2.3 + (k*P_RADIUS/5), -P_RADIUS/17.5, P_RADIUS*2.4), axis = vector(0, -P_RADIUS/4.4, 0),
        radius = P_RADIUS/3.8, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
        emissive = True)
    cone(pos = vector(-P_RADIUS/1.75 + (k*P_RADIUS/3.5), -P_RADIUS/17.5, P_RADIUS*2.6), axis = vector(0, -P_RADIUS/2.2, 0),
        radius = P_RADIUS/3.2, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
        emissive = True)
    cone(pos = vector(-P_RADIUS/1.75 + (k*P_RADIUS/3.5), -P_RADIUS/17.5, P_RADIUS*2.8), axis = vector(0, -P_RADIUS/2.9, 0),
        radius = P_RADIUS/4.3, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
        emissive = True)
    cone(pos = vector(-P_RADIUS/1.75 + (k*P_RADIUS/3.5), -P_RADIUS/17.5, P_RADIUS*3), axis = vector(0, -P_RADIUS/2, 0),
        radius = P_RADIUS/3.2, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
        emissive = True)
    cone(pos = vector(-P_RADIUS/1.5 + (k*P_RADIUS/3.2), -P_RADIUS/17.5, P_RADIUS*3.2), axis = vector(0, -P_RADIUS/1.6, 0),
        radius = P_RADIUS/3.4, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
        emissive = True)
    cone(pos = vector(-P_RADIUS/1.75 + (k*P_RADIUS/3.6), -P_RADIUS/17.5, P_RADIUS*3.4), axis = vector(0, -P_RADIUS/2, 0),
        radius = P_RADIUS/3.2, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
        emissive = True)
    cone(pos = vector(-P_RADIUS/2.1 + (k*P_RADIUS/4.2), -P_RADIUS/17.5, P_RADIUS*3.6), axis = vector(0, -P_RADIUS/3, 0),
        radius = P_RADIUS/4.2, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
        emissive = True)

#----------------------------------Clouds----------------------------------------

cloud_pos = [[-P_RADIUS/17.5, 0, P_RADIUS/17.5, -P_RADIUS/1.75, -P_RADIUS/2, -P_RADIUS/2.2, P_RADIUS/2.2, P_RADIUS/2, P_RADIUS/1.75],
            [P_RADIUS/10, P_RADIUS/7, P_RADIUS/10, P_RADIUS/10, P_RADIUS/7, P_RADIUS/10, P_RADIUS/10, P_RADIUS/7, P_RADIUS/10],
            [P_RADIUS/11.5, P_RADIUS/9, P_RADIUS/11.5, P_RADIUS/11.5, P_RADIUS/8.75, P_RADIUS/11.5, P_RADIUS/11.5, P_RADIUS/8.75, P_RADIUS/11.5]]

cloud_size = P_RADIUS*2.3
for l in range(9):
    if l == 4:
        cloud_size = P_RADIUS*2.9
    if l == 7:
        cloud_size = P_RADIUS*3.4
    ellipsoid(pos = vector(cloud_pos[0][l], P_RADIUS/1.4, cloud_size), length = cloud_pos[1][l],
        height = cloud_pos[2][l], width = P_RADIUS/7, texture = textures.rough, emissive = True)

#----------------------------------Trees----------------------------------------

tree_pos = [[P_RADIUS/1.6, -P_RADIUS/1.7, P_RADIUS/1.75, -P_RADIUS/2.3, -P_RADIUS/17.5], [P_RADIUS*3.4, P_RADIUS*3.6, P_RADIUS*2.7, P_RADIUS*2.3, P_RADIUS*2.7]]

for m in range(5):
    cylinder(pos = vector(tree_pos[0][m], 0, tree_pos[1][m]), axis = vector(0, P_RADIUS/5, 0),
        radius = P_RADIUS/87.5, texture = textures.wood_old, emissive = False)
    sphere(pos = vector(tree_pos[0][m], P_RADIUS/5, tree_pos[1][m]), radius = P_RADIUS/11.6,
        texture = textures.stucco, color = vector(0.32, 1, 0.15), emissive = True)
    sphere(pos = vector(tree_pos[0][m], P_RADIUS/3.8, tree_pos[1][m]), radius = P_RADIUS/10.9,
        texture = textures.stucco, color = vector(0.32, 0.5, 0.15), emissive = True)
    sphere(pos = vector(tree_pos[0][m] + P_RADIUS/35, P_RADIUS/4.4, tree_pos[1][m] + P_RADIUS/35), radius = P_RADIUS/10,
        texture = textures.stucco, color = vector(0.32, 1, 0.15), emissive = True)
    sphere(pos = vector(tree_pos[0][m] - P_RADIUS/35, P_RADIUS/4.4, tree_pos[1][m] - P_RADIUS/35), radius = P_RADIUS/10,
        texture = textures.stucco, color = vector(0.32, 1, 0.15), emissive = True)

#--------------------------------Basket Cart------------------------------------

base = box(pos = vector(P_RADIUS/2.3, P_RADIUS/23, P_RADIUS*3), length = P_RADIUS/4.375, height = P_RADIUS/35, width = P_RADIUS/8.75,
    color = color.orange, emissive = True)
back = box(pos = vector(P_RADIUS/1.94, P_RADIUS/6.36, P_RADIUS*3), length = P_RADIUS/70, height = P_RADIUS/5, width = P_RADIUS/8.75,
    color = color.orange, emissive = True)
basket = ring(pos = vector(P_RADIUS/2.45, P_RADIUS/4.66, P_RADIUS*3), axis = vector(0, P_RADIUS/35, 0), radius = P_RADIUS/23.33,
    thickness = P_RADIUS/175, color = color.white, emissive = True)
attachment = cylinder(pos = vector(P_RADIUS/1.94, P_RADIUS/4.66, P_RADIUS*3), axis = vector(-P_RADIUS/15.55, 0, 0),
    radius = P_RADIUS/175, color = color.white, emissive = True)
wheel1 = cylinder(pos = vector(P_RADIUS/2.8, P_RADIUS/45.45, P_RADIUS*3.08), axis = vector(0, 0, -P_RADIUS/70),
    radius = P_RADIUS/43, color = color.white, emissive = True)
wheel2 = cylinder(pos = vector(P_RADIUS/2, P_RADIUS/45.45, P_RADIUS*3.08), axis = vector(0, 0, -P_RADIUS/70),
    radius = P_RADIUS/43, color = color.white, emissive = True)
wheel3 = cylinder(pos = vector(P_RADIUS/2.8, P_RADIUS/45.45, P_RADIUS*2.93), axis = vector(0, 0, -P_RADIUS/70),
    radius = P_RADIUS/43, color = color.white, emissive = True)
wheel4 = cylinder(pos = vector(P_RADIUS/2, P_RADIUS/45.45, P_RADIUS*2.93), axis = vector(0, 0, -P_RADIUS/70),
    radius = P_RADIUS/43, color = color.white, emissive = True)
axle1 = cylinder(pos = vector(P_RADIUS/2.8, P_RADIUS/45.45, P_RADIUS*3.09), axis = vector(0, 0, -P_RADIUS/5.5),
    radius = P_RADIUS/175, color = vector(1, 0, 0.2))
axle2 = cylinder(pos = vector(P_RADIUS/2, P_RADIUS/45.45, P_RADIUS*3.09), axis = vector(0, 0, -P_RADIUS/5.5),
    radius = P_RADIUS/175, color = vector(1, 0, 0.2))

cart = compound([base, back, basket, attachment, wheel1, wheel2, wheel3, wheel4,
    axle1, axle2], texture = textures.stucco)
cart.force = vector(x, 0, 0)
cart.velocity = vector(x*50, 0, 0)
cart.mass = 1

#--------------------------------Basketball------------------------------------------

ball = sphere(pos = vector(-P_RADIUS/1.2 + cos(ANGLE), P_RADIUS/8 + sin(ANGLE), P_RADIUS*3), radius = P_RADIUS/40, color = color.orange,
              texture = "https://thumbs.dreamstime.com/t/3d-map-basketball-texture-7529012.jpg", emissive = True)

ball.velocity = vector(VELOCITY * cos(ANGLE), VELOCITY * sin(ANGLE), 0)
ball.mass = 2
ball.acceleration = vector(0, 0, 0)

ball.force_GRAVITY = vector(0, ball.mass*P_GRAVITY, 0)
ball.force_drag = -COEFF_DRAG * ball.velocity
ball.force_net = ball.force_GRAVITY + ball.force_drag

#------------------------------Game Physics------------------------------------------

# Interactivity
#
# while True:
#     ANGLE_input = float(input('Enter the launch ANGLE (in between 0 and 90 degrees): '))
#     VELOCITY = float(input('Enter the initial non-relativistic VELOCITY (in m/s): '))
#     P_GRAVITY = float(input('Enter your gravitational constant (in m/s' + u'\u00b2): '))

#     COEFF_REST = 0.9 # the coefficent of resitution allows the ball to come to rest after impact with the surface
#     COEFF_DRAG = random() # the coeffiecent of drag due to air molecules

#     radians = (ANGLE_input * pi) # converts the ANGLE from degrees into radians


t = 0
dt = 1

while t < 100000:
    rate(500)

    S_RADIUS = natural_satellite.pos - host_planet.pos
    F = -G_CONSTANT * host_planet.mass * natural_satellite.mass * norm(S_RADIUS) / mag(S_RADIUS)**2

    natural_satellite.momentum = natural_satellite.momentum + F * dt
    natural_satellite.pos = natural_satellite.pos + natural_satellite.momentum*dt / natural_satellite.mass

    host_planet.rotate(angle = 0.002, axis = vector(0,1,0))
    natural_satellite.rotate(angle = 0.001, axis = vector(0,1,0))
    host_planet.rotate(angle = 0.002, axis = vector(0,1,0))

    cart.acceleration = cart.force / cart.mass
    cart.velocity = cart.velocity + cart.acceleration*dt
    cart.pos = cart.pos + cart.velocity*dt

    ball.acceleration = ball.force_net / ball.mass # Non-relativistic assumption, depends on the player to not supply relativistic inputs
    ball.velocity = ball.velocity + ball.acceleration*dt # Again non-relativistic situation assumed
    ball.pos = ball.pos + ball.velocity*dt

    random_ANGLE = random.uniform(0.01, 0.09)

    # The high value for the postion of the cart
    if cart.pos.x > P_RADIUS/1.16:
        cart.velocity = -cart.velocity
        cart.rotate(angle = random_ANGLE, axis = vector(0, P_RADIUS/35, 0))

    # The low value for the position of the cart
    if cart.pos.x < -P_RADIUS/3.5:
        cart.velocity = -cart.velocity
        cart.rotate(angle = random_ANGLE, axis = vector(0, -P_RADIUS/35, 0))

    # When the ball impacts with the surface
    if ball.pos.y - ball.radius < surface.pos.y:
        ball.velocity.y = -ball.velocity.y
        ball.velocity.y = ball.velocity.y * COEFF_REST
        ball.pos.y = ball.radius

    # When the ball impacts with the base_wood of the moving cart
    if (ball.pos.x + ball.radius > base.pos.x - 4) & (ball.pos.y - ball.radius < base.pos.y + 0.5):
        ball.velocity.y = -ball.velocity.y

    if (ball.pos.x + ball.radius > back.pos.x + 0.5) & (ball.pos.y < back.pos.y + P_RADIUS/5):
        ball.velocity.x = -ball.velocity.x

    t = t + dt
