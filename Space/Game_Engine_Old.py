from visual import *
from random import *
from math import *

#-------------------Scene-----------------------------
scene = display(title='The Cannon of Doom',
     x=0, y=0, width=1920, height=1080,
     center=(0,12,0), background=(0.275,.8,1))
scene.range=50
scene.autoscale=0

#----------------Introduction--------------------------
def pause():
     while True:
         rate(30)
         if scene.mouse.events:
             m = scene.mouse.getevent()
             if m.click == 'left': return
         elif scene.kb.keys:
             k = scene.kb.getkey()
             return            
a=text(text='Are you ready \nfor some fun?',
    pos=(-18,12,0), depth=-1, height=5, color=color.orange, material=materials.rough, axis=(1,0,.3)) 
pause()
a.visible = False
del a
b=text(text='Alright, soon you will be \npresented with an earth \nlike enviornment along \nwith a cannon and a moving \ncart.',
    pos=(-40,25,0), depth=-1, height=5, color=color.white, material=materials.bricks, axis=(1,0,.1))
pause()
b.visible = False
del b
c=text(text='Then it is up to you \nto make the basket \ninto the moving cart.',
    pos=(-40,20,0), depth=-1, height=5, color=(205,92,92), material=materials.diffuse, axis=(1,0,.1))
pause()
c.visible = False
del c
d=text(text='The controls are simple. \nClick on your terminal \nwindow and enter the \nrespected values \nwhen prompted.',
    pos=(-40,25,0), depth=-1, height=5, color=color.yellow, material=materials.rough, axis=(1,0,.1))
pause()
d.visible = False
del d
e=text(text='Oh, and remember the fate \nof the universe depends \non it or something.',
    pos=(-40,25,0), depth=-1, height=5, color=(205,92,92),material=materials.diffuse, axis=(1,0,.1))
pause()
e.visible = False
del e

#--------------------Planet-----------------------------
surface =  cylinder(pos=(0,0,0), axis=(0,-1,0), radius=35, material=materials.rough, color=(.42,1,0.25))
ground = cylinder(pos=(0,-1,0), axis=(0,-1,0),   radius=35, material=materials.rough, color=(.7,0.5,0.4))

#--------------------Trees-----------------------------
Tree1 = cylinder(pos=(22,0,20),   axis=(0,7,0), radius=.4, color=(.78,0.5,0.45))
Tree2 = cylinder(pos=(-29,0,5),   axis=(0,7,0), radius=.4, color=(.78,0.5,0.45))
Tree3 = cylinder(pos=(20,0,-5),   axis=(0,7,0), radius=.4, color=(.78,0.5,0.45))
Tree4 = cylinder(pos=(-20,0,-20), axis=(0,7,0), radius=.4, color=(.78,0.5,0.45))
Tree5 = cylinder(pos=(-2,0,-5),   axis=(0,7,0), radius=.4, color=(.78,0.5,0.45))
Tree1_leaves = sphere(pos=(22,7,20),   radius=3, color=(.32,1,0.15))
Tree2_leaves = sphere(pos=(-29,7,5),   radius=3, color=(.32,1,0.15))
Tree3_leaves = sphere(pos=(20,7,-5),   radius=3, color=(.32,1,0.15))
Tree4_leaves = sphere(pos=(-20,7,-20), radius=3, color=(.32,1,0.15))
Tree5_leaves = sphere(pos=(-2,7,-5),   radius=3, color=(.32,1,0.15))

#--------------------Clouds----------------------------
cloud1 = ellipsoid(pos=(-2,25,5), length=3.5, height=3, width=0.5)
cloud2 = ellipsoid(pos=(0,25,5), length=5, height=4, width=0.5)
cloud3 = ellipsoid(pos=(2,25,5), length=3.5, height=3, width=0.5)

cloud4 = ellipsoid(pos=(-20,27,5), length=3.5, height=3, width=0.5)
cloud5 = ellipsoid(pos=(-18,27,5), length=5, height=4, width=0.5)
cloud6 = ellipsoid(pos=(-16,27,5), length=3.5, height=3, width=0.5)

cloud7 = ellipsoid(pos=(16,26,5), length=3.5, height=3, width=0.5)
cloud8 = ellipsoid(pos=(18,26,5), length=5, height=4, width=0.5)
cloud9 = ellipsoid(pos=(20,26,5), length=3.5, height=3, width=0.5)

#----------------------Sun-----------------------------
sun1 = sphere(pos =(47,37,0), radius = 5, color = color.yellow, material = materials.unshaded, opacity = .75)
sun2 = sphere(pos =(47,37,0), radius = 4.9, color = color.yellow, material = materials.emissive)

#---------------------Stripes--------------------------
bands = zeros([16,16,4], float)
for i in range(len(bands)):
    for j in range(len(bands[0])):
        op = 1
        if i % 2 == 0:
            op = 0.3
            col = color.cyan
        else:
            col = [color.blue, color.green, color.red,
                   color.yellow, color.cyan][i//2 % 5]
        bands[i][j] = (col[0], col[1], col[2], op)
stripes = materials.texture(data = bands, mapping = "spherical", interpolate = False)

#---------------------Cannon--------------------------
Cannon = frame()
cr = shapes.circle(radius=1.1, np=64, thickness=0.5)
straight = [(0,0,0),(0,0,-4)]
extrusion(frame=Cannon, pos=straight, shape=cr, color=color.yellow, scale=[(.5,.5), (1,1)])
ar = shapes.arc(radius=1.05, angle1=0, angle2=pi/2)
cr1 = paths.circle(pos= (0,0,-3.93), up=(0,0,-1) , radius=0.05, np=64)
extrusion(frame=Cannon, pos=cr1, shape=ar, material=stripes)
Cannon.pos = (-20,6.25,5)
Cannon.axis = (0,0,-1)

#------------------Cannon Stand------------------------
Cannon_Stand = box(pos=(-23,1,5), length=5, height=2, width=6, material=materials.wood)
sh = Polygon([(0,0),(1.75,0),(2.5,-3),(2.5,-4),(-.5,-3),(0,-4),(0,0)])
l = [(-23.5,6,5.1),(-23.5,6,5.1)]
extrusion(pos=l, shape=sh, material=stripes, color=color.cyan)

#-----------------Basketball Cart------------------------
base_wood =  box(pos=(15,1.65,5), length=8,  height=1, width=4.5, material=materials.wood)
back_wood =  box(pos=(18,5.5,5),  length=.5, height=7, width=4.5, material=materials.wood)
curve1 = curve(pos=[(18,7.5,5), (15.75,7.5,5)], radius=0.05)
ring1 = ring(pos=(14.25,7.5,5), axis=(0,1,0), radius=1.5, thickness=0.1)

#----------------------Wheels---------------------------
cylinder1 = cylinder(pos=(12,0.77,7.5),axis=(0,0,-.5), radius=.8)
cylinder2 = cylinder(pos=(17,0.77,7.5),axis=(0,0,-.5), radius=.8)

#-----------------------Back----------------------------
cylinder3 = cylinder(pos=(12,0.77,3)  ,axis=(0,0,-.5), radius=.8)
cylinder4 = cylinder(pos=(17,0.77,3)  ,axis=(0,0,-.5), radius=.8)
cylinder5 = cylinder(pos=(12,0.77,7.6),axis=(0,0,-.5), radius=.2,   color=(1,0,0.2))
cylinder6 = cylinder(pos=(17,0.77,7.6),axis=(0,0,-.5), radius=.2,   color=(1,0,0.2))
curve2 = curve(pos=[(12,0.77,7.6), (12,1.77,3)],    radius=0.09, color=(1,0,0.2))

cylinder7 = cylinder(pos=(12,0.77,2.9),axis=(0,0,-.5), radius=.2,   color=(1,0,0.2))
cylinder8 = cylinder(pos=(17,0.77,2.9),axis=(0,0,-.5), radius=.2,   color=(1,0,0.2))
curve3 = curve(pos=[(17,0.77,2.9), (17,1.77,7.6)],  radius=0.09, color=(1,0,0.2))

#-------------------The Game Engine--------------------------
while True:
    angle_input = input("Enter the launch angle (in between 0 and 90 degrees): ")
    velocity = input("Enter the initial non-relativistic velocity (in meters/sec): ")
    gravity = input("Enter your gravitational constant (in meters/sec^2): ")
    
    coeff_rest = .9 #The coefficent of resitution chosen for the game. It allows the ball to come to rest after impact with the surface
    coeff_drag = random()#The coeffiecent of drag due to air molecules
    
    radians = (angle_input * pi)/180.0 #converts the angle from degrees into radians
    
#-------------------Cannon Rotation--------------------------    
    Cannon.visible = False #deletes the last rotation of the cannon
    Cannon = frame() #sets up a new cannon
    cr = shapes.circle(radius=1.1, np=64, thickness=0.5)
    straight = [(0,0,0),(0,0,-4)]
    extrusion(frame=Cannon, pos=straight, shape=cr, color=color.yellow, scale=[(.5,.5), (1,1)])
    ar = shapes.arc(radius=1.05, angle1=0, angle2=pi/2)
    cr1 = paths.circle(pos= (0,0,-3.93), up=(0,0,-1) , radius=0.05, np=64)
    extrusion(frame=Cannon, pos=cr1, shape=ar, material=stripes)
    Cannon.pos = (-20,6.25,5)
    Cannon.axis = (0,0,-1)
    Cannon.rotate(angle = -sin(radians), axis = Cannon.axis, origin = Cannon.pos) #rotates the cannon on its origin based upon the user input angle

#------------------Ball Position Etc--------------------------   
    ball = sphere(pos =(Cannon.pos.x + cos(radians),Cannon.pos.y + sin(radians -.5),Cannon.pos.z), radius = 0.5, color = color.orange)
    ball.mass = 2.0
    
    x_velocity = velocity * cos(radians) #converts the velocity into its x-component
    y_velocity = velocity * sin(radians) #converts the velocity into its y-component

    ball.velocity = vector(x_velocity,y_velocity,0) #converts the velocity into a vector
    ball.accel = vector(0,0,0)

#--------------------Cart Variables---------------------------  
    x = randint(1,2) #radomizer used for the next few variables. May unstabilize the code when higher values are used for the paramater.
    
    base_wood.Force = vector(x,0,0)
    base_wood.velocity = vector(x,0,0)
    base_wood.mass = 1

    back_wood.Force = vector(x,0,0)
    back_wood.velocity = vector(x,0,0)
    back_wood.mass = 1

    curve1.Force = vector(x,0,0)
    curve1.velocity = vector(x,0,0)
    curve1.mass = 1

    curve2.Force = vector(x,0,0)
    curve2.velocity = vector(x,0,0)
    curve2.mass = 1

    curve3.Force = vector(x,0,0)
    curve3.velocity = vector(x,0,0)
    curve3.mass = 1

    ring1.Force = vector(x,0,0)
    ring1.velocity = vector(x,0,0)
    ring1.mass = 1

    cylinder1.Force = vector(x,0,0)
    cylinder1.velocity = vector(x,0,0)
    cylinder1.mass = 1

    cylinder2.Force = vector(x,0,0)
    cylinder2.velocity = vector(x,0,0)
    cylinder2.mass = 1

    cylinder3.Force = vector(x,0,0)
    cylinder3.velocity = vector(x,0,0)
    cylinder3.mass = 1

    cylinder4.Force = vector(x,0,0)
    cylinder4.velocity = vector(x,0,0)
    cylinder4.mass = 1

    cylinder5.Force = vector(x,0,0)
    cylinder5.velocity = vector(x,0,0)
    cylinder5.mass = 1

    cylinder6.Force = vector(x,0,0)
    cylinder6.velocity = vector(x,0,0)
    cylinder6.mass = 1

    cylinder7.Force = vector(x,0,0)
    cylinder7.velocity = vector(x,0,0)
    cylinder7.mass = 1

    cylinder8.Force = vector(x,0,0)
    cylinder8.velocity = vector(x,0,0)
    cylinder8.mass = 1
    
# Notice only x-direction matters for the cart as both y and z are set to 0 in all of the cases above.

#------------------Time defination---------------------------
    deltat = 0.01
    t = 0
    t_end = 15
    a = 0 #sets an identifier when the ball bounces back from the Cannon_Stand
    b = 0 #sets an identifier when the ball is higher than the ring1 in both x and y directions
    c = 0
#-------------------The Projectile----------------------------
    while ((t < t_end) & (ball.pos.x < 36)):
        rate(1/0.01) #This rate allows for realtime animation
        t = t + deltat
        ball.F_gravity = vector(0, -ball.mass*gravity, 0)
        ball.F_drag = -coeff_drag * ball.velocity 
        ball.F_net = ball.F_gravity + ball.F_drag #Net force is used due to the presence of drag by the air molecules

        ball.accel = ball.F_net / ball.mass #Non-relativistic assumption, depends on the player to not supply relativistic inputs
        ball.velocity = ball.velocity + ball.accel*deltat #Again non-relativistic situation assumed
        ball.pos = ball.pos + ball.velocity*deltat
        
#----------------Moving Baseketball Cart----------------------
        base_wood.accel = base_wood.Force / base_wood.mass
        base_wood.velocity = base_wood.velocity + base_wood.accel*deltat
        base_wood.pos = base_wood.pos + base_wood.velocity*deltat

        back_wood.accel = back_wood.Force / back_wood.mass
        back_wood.velocity = back_wood.velocity + back_wood.accel*deltat
        back_wood.pos = back_wood.pos + back_wood.velocity*deltat

        curve1.accel = curve1.Force / curve1.mass
        curve1.velocity = curve1.velocity + curve1.accel*deltat
        curve1.pos = curve1.pos + curve1.velocity*deltat

        curve2.accel = curve2.Force / curve2.mass
        curve2.velocity = curve2.velocity + curve2.accel*deltat
        curve2.pos = curve2.pos + curve2.velocity*deltat

        curve3.accel = curve3.Force / curve3.mass
        curve3.velocity = curve3.velocity + curve3.accel*deltat
        curve3.pos = curve3.pos + curve3.velocity*deltat

        ring1.accel = ring1.Force / ring1.mass
        ring1.velocity = ring1.velocity + ring1.accel*deltat
        ring1.pos = ring1.pos + ring1.velocity*deltat

        cylinder1.accel = cylinder1.Force / cylinder1.mass
        cylinder1.velocity = cylinder1.velocity + cylinder1.accel*deltat
        cylinder1.pos = cylinder1.pos + cylinder1.velocity*deltat

        cylinder2.accel = cylinder2.Force / cylinder2.mass
        cylinder2.velocity = cylinder2.velocity + cylinder2.accel*deltat
        cylinder2.pos = cylinder2.pos + cylinder2.velocity*deltat

        cylinder3.accel = cylinder3.Force / cylinder3.mass
        cylinder3.velocity = cylinder3.velocity + cylinder3.accel*deltat
        cylinder3.pos = cylinder3.pos + cylinder3.velocity*deltat

        cylinder4.accel = cylinder4.Force / cylinder4.mass
        cylinder4.velocity = cylinder4.velocity + cylinder4.accel*deltat
        cylinder4.pos = cylinder4.pos + cylinder4.velocity*deltat

        cylinder5.accel = cylinder5.Force / cylinder5.mass
        cylinder5.velocity = cylinder5.velocity + cylinder5.accel*deltat
        cylinder5.pos = cylinder5.pos + cylinder5.velocity*deltat

        cylinder6.accel = cylinder6.Force / cylinder6.mass
        cylinder6.velocity = cylinder6.velocity + cylinder6.accel*deltat
        cylinder6.pos = cylinder6.pos + cylinder6.velocity*deltat

        cylinder7.accel = cylinder7.Force / cylinder7.mass
        cylinder7.velocity = cylinder7.velocity + cylinder7.accel*deltat
        cylinder7.pos = cylinder7.pos + cylinder7.velocity*deltat

        cylinder8.accel = cylinder8.Force / cylinder8.mass
        cylinder8.velocity = cylinder8.velocity + cylinder8.accel*deltat
        cylinder8.pos = cylinder8.pos + cylinder8.velocity*deltat

        
        
        if base_wood.pos.x > 20: #The high value for the postion of the cart
            base_wood.velocity = -base_wood.velocity
            back_wood.velocity = -back_wood.velocity
            curve1.velocity = -curve1.velocity
            curve2.velocity = -curve2.velocity
            curve3.velocity = -curve3.velocity
            ring1.velocity = -ring1.velocity
            cylinder1.velocity = -cylinder1.velocity
            cylinder2.velocity = -cylinder2.velocity
            cylinder3.velocity = -cylinder3.velocity
            cylinder4.velocity = -cylinder4.velocity
            cylinder5.velocity = -cylinder5.velocity
            cylinder6.velocity = -cylinder6.velocity
            cylinder7.velocity = -cylinder7.velocity
            cylinder8.velocity = -cylinder8.velocity
        if base_wood.pos.x < -10: #the low value for the position of the cart
            base_wood.velocity = -base_wood.velocity
            back_wood.velocity = -back_wood.velocity
            curve1.velocity = -curve1.velocity
            curve2.velocity = -curve2.velocity
            curve3.velocity = -curve3.velocity
            ring1.velocity = -ring1.velocity
            cylinder1.velocity = -cylinder1.velocity
            cylinder2.velocity = -cylinder2.velocity
            cylinder3.velocity = -cylinder3.velocity
            cylinder4.velocity = -cylinder4.velocity
            cylinder5.velocity = -cylinder5.velocity
            cylinder6.velocity = -cylinder6.velocity
            cylinder7.velocity = -cylinder7.velocity
            cylinder8.velocity = -cylinder8.velocity
       
#------------------Deflection of the ball---------------------
        if ball.pos.y - ball.radius < surface.pos.y: #When the ball impacts with the surface
            ball.velocity.y = -ball.velocity.y
            ball.velocity.y = ball.velocity.y * coeff_rest
            ball.pos.y = ball.radius
            
        if ((ball.pos.x + ball.radius > base_wood.pos.x - 4) & (ball.pos.y - ball.radius < base_wood.pos.y + .5)): #When the ball impacts with the base_wood of the moving cart
            ball.velocity.y = -ball.velocity.y

        if ((ball.pos.x + ball.radius > back_wood.pos.x + .5) & (ball.pos.y < back_wood.pos.y + 5.5)): #When the ball impacts with the back_wood of the moving cart
            ball.velocity.x = -ball.velocity.x
            
        if ((ball.velocity.x < -1) & (ball.pos.x - ball.radius < Cannon_Stand.pos.x + 2)): #When the ball impacts with the Cannon or the Cannon_Stand. Acts as an invisible force stopping the ball from going behind the cannon stand.
            ball.velocity.x = -ball.velocity.x
            a = 1
            
        if ((ball.pos.y > ring1.pos.y) & (ball.pos.x > ring1.pos.x)): #When the ball above the ring in both x and y directions
            b = 1
            
        if (ball.pos.x -1 > back_wood.pos.x): #When the ball is beyond the back_wood
            c = 1
        
#---------------------Out of Bounds---------------------------
        if ball.pos.x > 34:
            ball.visible = False
            
#-------------------Scoring Mechanism-------------------------
        def score():
            count = 0
            for i in range(1,5):
                if ((a != 1) & (b == 1)& (c != 1) & (ball.pos.x >= ring1.pos.x) & (ball.pos.y <= ring1.pos.y - 3)) : #When the ball makes it through the basket. Although could not figure out how to contain it aorund the area of the basket.
                    count += 1
                    print('''Congratulations! You made the basket and saved the Universe from the wrath
of certain string theorists.'''.format(count))
                    
                    if i == 1:
                        print('''You seem to have mastered this game!
                                Now see if you can do it 5 more times.''') #May represent a buggy nature as explained in the comment above.
                        exit()
        score()
