###################################################
# [Practice] Matrix Stack
import glfw
from OpenGL.GL import *
import numpy as np
from OpenGL.GLU import *

gCamAng = 0

def render():
    # enable depth test (we'll see details later)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # use orthogonal projection (we'll see details later)
    glOrtho(-2,2, -2,2, -1,1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # rotate "camera" position to see this 3D space better (we'll see details later)
    #gluLookAt(.1*np.sin(camAng),.1, .1*np.cos(camAng), 0,0,0, 0,1,0)

    drawFrame()
    t = glfw.get_time()

    # blue base transformation
    glPushMatrix()
    glTranslatef(np.sin(t), 0, 0)

    # blue base drawing
    glPushMatrix()
    glScalef(.2, .2, .2)
    glColor3ub(0, 0, 255)
    drawBox()
    glPopMatrix()

    #green line
    glPushMatrix()
    glTranslatef(0,0.6,0.005)
    
    glPushMatrix()
    glScalef(0.005, 0.6,0.6)
    glColor3ub(0,255,0)
    drawBox()
    glPopMatrix()
    glPopMatrix()

    # green line with red arm
    glPushMatrix()
    glTranslatef(0,0,0)
    glRotatef(t*(180/np.pi),0,0,1)
    glTranslatef(0.5,.6,.01)

    glPushMatrix()
    glScalef(0.005,0.6,0.6)
    drawBox()
    glPopMatrix()

    # red line 
    glPushMatrix()
    glTranslate(.6,-0.6,0)
    glRotatef(90,0,0,1)

    glPushMatrix()
    glScalef(0.005,0.6,0.6)
    glColor3ub(255,0,0)
    drawBox()
    glPopMatrix()
    glPopMatrix()
    
    glPopMatrix()
    
    # red arm transformation
    glPushMatrix()
    glRotatef(t*(180/np.pi), 0, 0, 1)
    glTranslatef(.5, 0, .01)


    # red arm drawing
    glPushMatrix()
    glScalef(.5, .1, .1)
    glColor3ub(255, 0, 0)
    drawBox()

    glPopMatrix()

    # green base transformation
    glPushMatrix()
    glTranslatef(.5,0,0.1)
    glRotatef(t*(180/np.pi), 0, 0, 1)


    # green base drawing
    glPushMatrix()
    glScalef(.2,.2,.2)
    glColor3ub(0,255,0)
    drawBox()
    glPopMatrix()

    #green line
    glPushMatrix()
    glTranslatef(0,0.6,0)
    
    glPushMatrix()
    glScalef(0.005,0.6,0.6)
    drawBox()
    glPopMatrix()

    # red line
    glPushMatrix()
    glTranslatef(0.6,-0.6,0.1)
    glRotatef(90,0,0,1)
    

    glPushMatrix()
    glScalef(0.005,0.6,0.6)
    glColor3ub(255,0,0)
    drawBox()
    glPopMatrix()

    glPopMatrix()

    
    
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()


def drawBox():
    glBegin(GL_QUADS)
    glVertex3fv(np.array([1,1,0.]))
    glVertex3fv(np.array([-1,1,0.]))
    glVertex3fv(np.array([-1,-1,0.]))
    glVertex3fv(np.array([1,-1,0.]))
    glEnd()

def drawFrame():
    # draw coordinate: x in red, y in green, z in blue
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([1.,0.,0.]))
    glColor3ub(0, 255, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([0.,1.,0.]))
    glColor3ub(0, 0, 255)
    glVertex3fv(np.array([0.,0.,0]))
    glVertex3fv(np.array([0.,0.,1.]))
    glEnd()


def main():
    if not glfw.init():
        return
    window = glfw.create_window(480,480,"2017029570-7-1", None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)

    glfw.swap_interval(1)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()


