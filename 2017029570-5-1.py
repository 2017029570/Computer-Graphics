import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

T = np.array([0.5,0.])

def render(M):
    global T
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    glBegin(GL_LINES)
    glColor3ub(255,0,0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0,255,0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()

    glColor3ub(255,255,255)

    glBegin(GL_POINTS)
    glVertex2fv(M @ (T+T))
    
    glEnd()

    glBegin(GL_LINES)
    glVertex2fv([0.,0.])
    glVertex2fv(M @ T)
    
    glEnd()

def main():

    if not glfw.init():
        return
    window = glfw.create_window(480,480,"2017029570-5-1", None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
   
    glfw.swap_interval(1)
    
    while not glfw.window_should_close(window):
        
        glfw.poll_events()
        t = glfw.get_time()

        M = np.array([[np.cos(t), -np.sin(t)],
                      [np.sin(t), np.cos(t)]])

        render(M)

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
    

