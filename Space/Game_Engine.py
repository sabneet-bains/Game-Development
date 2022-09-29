from vpython import *
import numpy
import random

#--------------------------------Constants-------------------------------------

G = 6.67e-11
RP = 6.378e6
MP = 5.972e24
gravity = -9.8
velocity = 10
angle = (45 * pi) / 180
coeff_rest = 0.9
coeff_drag = 0#random.random()
x = random.randint(1, 10)

#----------------------------------Scene---------------------------------------

scene = canvas(title = 'Space Basketball', width = 1688, height = 800,
    center = vector(0, 0, 3*RP), range = 4*RP, autoscale = True)

scene.camera.pos = vector(4*RP, 0, 8*RP)
scene.lights = []

#----------------------------Background Stars-----------------------------------

r = RP*52

for i in numpy.arange(0, 2*pi + 0.5, 0.5):
    for j in numpy.arange(0, pi + 0.5, 0.5):
        sphere(pos = vector(r*sin(j)*cos(i), r*sin(j)*sin(i), r*cos(j)),
            radius = RP/17.5, color = color.white, emissive = True)

#----------------------------------Intro-------------------------------------

intro = text(text = 'A long time ago in a galaxy far,\nfar away....', pos = vector(-RP/3.7, 0, 0), 
        depth = 0, height = RP/7, color = vector(0.41, 0.82, 0.78), emissive = True)

scene.waitfor('click')
for i in range(10):
    rate(25)
    intro.opacity = intro.opacity - 0.1
intro.visible = False

intro2 = text(text = 'SPACE \n BALL', pos = vector(-RP*7.14, RP*1.42, 0), 
        depth = 0, height = RP*2.85, color = vector(0.89, 0.93, 0.56), emissive = True)

for i in range(100):
    rate(25)
    intro2.height = intro2.height*0.99
    intro2.length = intro2.length*0.99
    intro2.pos.x = intro2.pos.x + RP/10
    intro2.pos.y = intro2.pos.y + RP/50

intro3 = text(text = 'Soon, you will be presented', pos = vector(RP*4, -RP*1.42, 0),
    depth = 0, height = RP/7, color = vector(0.89, 0.93, 0.56), emissive = True)
intro4 = text(text = '  with a bizarro planet. Just', pos = vector(RP*4, -RP*1.71, 0), 
    depth = 0, height = RP/7, color = vector(0.89, 0.93, 0.56), emissive = True) 
intro5 = text(text = '         make the basket into', pos = vector(RP*4, -RP*2, 0), 
    depth = 0, height = RP/7, color = vector(0.89, 0.93, 0.56), emissive = True)
intro6 = text(text = '                         the moving cart!', 
    pos = vector(RP*4, -RP*2.28, 0), depth = 0, height = RP/7, color = vector(0.89, 0.93, 0.56),
    emissive = True)

for i in range(400):
    rate(30)
    intro3.pos.y = intro3.pos.y + RP/140
    intro3.length = intro3.length*1.002
    intro3.opacity = intro3.opacity - 0.005
    intro4.pos.y = intro4.pos.y + RP/140
    intro4.length = intro4.length*1.002
    intro4.opacity = intro4.opacity - 0.0033
    intro5.pos.y = intro5.pos.y + RP/140
    intro5.length = intro5.length*1.002
    intro5.opacity = intro5.opacity - 0.0024
    intro6.pos.y = intro6.pos.y + RP/140
    intro6.length = intro6.length*1.002
    intro6.opacity = intro6.opacity - 0.0018

intro3.visible = False
intro4.visible = False
intro5.visible = False
intro6.visible = False

#-------------------------------Closest Star------------------------------------

closest_star = sphere(pos = vector(RP*70, 0, 0), radius = RP*10,
    texture = "https://i.imgur.com/XdRTvzj.jpg", emissive = True)
star_light = distant_light(direction = vector(RP*70, 0, 0), color = color.white)

#-------------------------------Host Planet-------------------------------------

host_planet = sphere(pos = vector(-RP, 0, 0), axis = vector(-200, -5, -500),
    radius = RP, texture = "https://i.imgur.com/Mwsa16j.jpg", emissive = True)
host_planet.mass = MP
host_planet.velocity = vector(0, 0, 0)
host_planet.momentum = host_planet.mass * host_planet.velocity

#-----------------------------Natural Satellite---------------------------------

natural_satellite = sphere(pos = vector(RP*1.1, 0, 0), radius = RP*0.2,
    texture = "https://i.imgur.com/0lAj5pJ.jpg", emissive = True)
natural_satellite.mass = 100
natural_satellite.velocity = vector(0, 5000, 0)
natural_satellite.momentum = natural_satellite.mass * natural_satellite.velocity

#-------------------------------Space Dome---------------------------------------

space_dome = sphere(pos = vector(0, 0, RP*3), axis = vector(0, -RP/35, 0), 
    radius = RP, color = color.cyan, opacity = 0.05, emissive = True)
surface =  cylinder(pos = vector(0, 0, RP*3), axis = vector(0, -RP/35, 0), 
    radius = RP, texture = textures.stucco, color = vector(0.42, 1, 0.25), 
    emissive = False)
ground = cylinder(pos = vector(0, -RP/35, RP*3), axis = vector(0, -RP/17.5, 0), 
    radius = RP, texture = textures.stucco, color = vector(0.7, 0.5, 0.4), 
    emissive = True)
pond = cylinder(pos = vector(0, RP/50, RP*3.5), axis = vector(0, -RP/30, 0), 
    radius = RP/5, texture = textures.stucco, color = vector(0, 0.54, 0.82), 
    emissive = True)
sand = cylinder(pos = vector(0, RP/150, RP*3.5), axis = vector(0, -RP/30, 0), 
    radius = RP/3.8, texture = textures.stucco, color = vector(0.7, 0.5, 0.4), 
    emissive = True)

for k in range(5):
    cone(pos = vector(-RP/2.3 + (k*RP/5), -RP/17.5, RP*2.4), axis = vector(0, -RP/4.4, 0),
        radius = RP/3.8, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
        emissive = True)
    cone(pos = vector(-RP/1.75 + (k*RP/3.5), -RP/17.5, RP*2.6), axis = vector(0, -RP/2.2, 0),
        radius = RP/3.2, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
        emissive = True)
    cone(pos = vector(-RP/1.75 + (k*RP/3.5), -RP/17.5, RP*2.8), axis = vector(0, -RP/2.9, 0),
        radius = RP/4.3, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
        emissive = True)
    cone(pos = vector(-RP/1.75 + (k*RP/3.5), -RP/17.5, RP*3), axis = vector(0, -RP/2, 0),
        radius = RP/3.2, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
        emissive = True)
    cone(pos = vector(-RP/1.5 + (k*RP/3.2), -RP/17.5, RP*3.2), axis = vector(0, -RP/1.6, 0),
        radius = RP/3.4, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
        emissive = True)
    cone(pos = vector(-RP/1.75 + (k*RP/3.6), -RP/17.5, RP*3.4), axis = vector(0, -RP/2, 0),
        radius = RP/3.2, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
        emissive = True)
    cone(pos = vector(-RP/2.1 + (k*RP/4.2), -RP/17.5, RP*3.6), axis = vector(0, -RP/3, 0),
        radius = RP/4.2, texture = textures.stucco, color = vector(0.7, 0.5, 0.4),
        emissive = True)

#----------------------------------Clouds----------------------------------------

cloud_pos = [[-RP/17.5, 0, RP/17.5, -RP/1.75, -RP/2, -RP/2.2, RP/2.2, RP/2, RP/1.75], 
            [RP/10, RP/7, RP/10, RP/10, RP/7, RP/10, RP/10, RP/7, RP/10],
            [RP/11.5, RP/9, RP/11.5, RP/11.5, RP/8.75, RP/11.5, RP/11.5, RP/8.75, RP/11.5]]
z = RP*2.3
for l in range(9):
    if (l == 4):
        z = RP*2.9
    if (l == 7):
        z = RP*3.4
    ellipsoid(pos = vector(cloud_pos[0][l], RP/1.4, z), length = cloud_pos[1][l], 
        height = cloud_pos[2][l], width = RP/7, texture = textures.rough, emissive = True)

#----------------------------------Trees----------------------------------------

tree_pos = [[RP/1.6, -RP/1.7, RP/1.75, -RP/2.3, -RP/17.5], [RP*3.4, RP*3.6, RP*2.7, RP*2.3, RP*2.7]]

for m in range(5):
    cylinder(pos = vector(tree_pos[0][m], 0, tree_pos[1][m]), axis = vector(0, RP/5, 0), 
        radius = RP/87.5, texture = textures.wood_old, emissive = False)
    sphere(pos = vector(tree_pos[0][m], RP/5, tree_pos[1][m]), radius = RP/11.6,
        texture = textures.stucco, color = vector(0.32, 1, 0.15), emissive = True)
    sphere(pos = vector(tree_pos[0][m], RP/3.8, tree_pos[1][m]), radius = RP/10.9,
        texture = textures.stucco, color = vector(0.32, 0.5, 0.15), emissive = True)
    sphere(pos = vector(tree_pos[0][m] + RP/35, RP/4.4, tree_pos[1][m] + RP/35), radius = RP/10,
        texture = textures.stucco, color = vector(0.32, 1, 0.15), emissive = True)
    sphere(pos = vector(tree_pos[0][m] - RP/35, RP/4.4, tree_pos[1][m] - RP/35), radius = RP/10,
        texture = textures.stucco, color = vector(0.32, 1, 0.15), emissive = True)

#--------------------------------Basket Cart------------------------------------

base = box(pos = vector(RP/2.3, RP/23, RP*3), length = RP/4.375, height = RP/35, width = RP/8.75, 
    color = color.orange, emissive = True)
back = box(pos = vector(RP/1.94, RP/6.36, RP*3), length = RP/70, height = RP/5, width = RP/8.75, 
    color = color.orange, emissive = True)
basket = ring(pos = vector(RP/2.45, RP/4.66, RP*3), axis = vector(0, RP/35, 0), radius = RP/23.33, 
    thickness = RP/175, color = color.white, emissive = True)
attachment = cylinder(pos = vector(RP/1.94, RP/4.66, RP*3), axis = vector(-RP/15.55, 0, 0),
    radius = RP/175, color = color.white, emissive = True)
wheel1 = cylinder(pos = vector(RP/2.8, RP/45.45, RP*3.08), axis = vector(0, 0, -RP/70),
    radius = RP/43, color = color.white, emissive = True)
wheel2 = cylinder(pos = vector(RP/2, RP/45.45, RP*3.08), axis = vector(0, 0, -RP/70),
    radius = RP/43, color = color.white, emissive = True)
wheel3 = cylinder(pos = vector(RP/2.8, RP/45.45, RP*2.93), axis = vector(0, 0, -RP/70),
    radius = RP/43, color = color.white, emissive = True)
wheel4 = cylinder(pos = vector(RP/2, RP/45.45, RP*2.93), axis = vector(0, 0, -RP/70),
    radius = RP/43, color = color.white, emissive = True)
axle1 = cylinder(pos = vector(RP/2.8, RP/45.45, RP*3.09), axis = vector(0, 0, -RP/5.5),
    radius = RP/175, color = vector(1, 0, 0.2))
axle2 = cylinder(pos = vector(RP/2, RP/45.45, RP*3.09), axis = vector(0, 0, -RP/5.5),
    radius = RP/175, color = vector(1, 0, 0.2))

cart = compound([base, back, basket, attachment, wheel1, wheel2, wheel3, wheel4,
    axle1, axle2], texture = textures.stucco)
cart.force = vector(x, 0, 0)
cart.velocity = vector(x*50, 0, 0)
cart.mass = 1

#--------------------------------Basketball------------------------------------------

ball = sphere(pos = vector(-RP/1.2 + cos(angle), RP/8 + sin(angle), RP*3), radius = RP/40, color = color.orange, 
    texture = "https://thumbs.dreamstime.com/t/3d-map-basketball-texture-7529012.jpg", emissive = True)

ball.velocity = vector(velocity * cos(angle), velocity * sin(angle), 0)
ball.mass = 2
ball.acceleration = vector(0, 0, 0)

ball.force_gravity = vector(0, ball.mass*gravity, 0)
ball.force_drag = -coeff_drag * ball.velocity 
ball.force_net = ball.force_gravity + ball.force_drag

#------------------------------Game Physics------------------------------------------

# while True:
#     angle_input = float(input('Enter the launch angle (in between 0 and 90 degrees): '))
#     velocity = float(input('Enter the initial non-relativistic velocity (in m/s): '))
#     gravity = float(input('Enter your gravitational constant (in m/s' + u'\u00b2): '))
    
#     coeff_rest = 0.9 # the coefficent of resitution allows the ball to come to rest after impact with the surface
#     coeff_drag = random() # the coeffiecent of drag due to air molecules
    
#     radians = (angle_input * pi) # converts the angle from degrees into radians


t = 0
t_end = 100000
dt = 1

while (t < t_end):
    rate(500)

    r = natural_satellite.pos - host_planet.pos
    F = -G * host_planet.mass * natural_satellite.mass * norm(r) / mag(r)**2

    natural_satellite.momentum = natural_satellite.momentum + F * dt
    natural_satellite.pos = natural_satellite.pos + natural_satellite.momentum*dt / natural_satellite.mass

    host_planet.rotate(angle = 0.002, axis = vector(0,1,0))
    natural_satellite.rotate(angle = 0.001, axis = vector(0,1,0))
    host_planet.rotate(angle = 0.002, axis = vector(0,1,0))

    cart.acceleration = cart.force / cart.mass
    cart.velocity = cart.velocity + cart.acceleration*dt
    cart.pos = cart.pos + cart.velocity*dt

    ball.acceleration = ball.force_net / ball.mass #Non-relativistic assumption, depends on the player to not supply relativistic inputs
    ball.velocity = ball.velocity + ball.acceleration*dt #Again non-relativistic situation assumed
    ball.pos = ball.pos + ball.velocity*dt

    random_angle = random.uniform(0.01, 0.09)

    if cart.pos.x > RP/1.16: # The high value for the postion of the cart
        cart.velocity = -cart.velocity
        cart.rotate(angle = random_angle, axis = vector(0, RP/35, 0))

    if cart.pos.x < -RP/3.5: # the low value for the position of the cart
        cart.velocity = -cart.velocity
        cart.rotate(angle = random_angle, axis = vector(0, -RP/35, 0))

    if ball.pos.y - ball.radius < surface.pos.y: #When the ball impacts with the surface
        ball.velocity.y = -ball.velocity.y
        ball.velocity.y = ball.velocity.y * coeff_rest
        ball.pos.y = ball.radius

    if ((ball.pos.x + ball.radius > base.pos.x - 4) & (ball.pos.y - ball.radius < base.pos.y + 0.5)): #When the ball impacts with the base_wood of the moving cart
            ball.velocity.y = -ball.velocity.y

    if ((ball.pos.x + ball.radius > back.pos.x + 0.5) & (ball.pos.y < back.pos.y + RP/5)):
            ball.velocity.x = -ball.velocity.x
            
    t = t + dt