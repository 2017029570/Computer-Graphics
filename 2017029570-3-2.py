import glfw
from OpenGL.GL import *
import numpy as np

A = np.array([[1.0,0.,0.],
              [0.,1.0,0.],
              [0.,0.,1.0]])

def render(T):
    
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # draw cooridnate
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0, 255, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()

    # draw triangle
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 255, 255)
    glVertex2fv( (T @ np.array([0.0,0.5,1.0]))[:-1] )
    glVertex2fv( (T @ np.array([0.0,0.0,1.0]))[:-1] )
    glVertex2fv( (T @ np.array([0.5,0.0,1.0]))[:-1] )
    glEnd()

def key_callback(window, key, scancode, action, mods):
    global A
    if key == glfw.KEY_W:
        if action==glfw.PRESS:
            A = np.array([[0.9,0.,0.],
                          [0.,1.0,0.],
                          [0.,0.,1.]]) @ A
            
    elif key == glfw.KEY_E:
        if action==glfw.PRESS:
             A = np.array([[1.1,0.,0.],
                           [0.,1.0,0.],
                           [0.,0.,1.]]) @ A
            
    elif key == glfw.KEY_S:
        if action==glfw.PRESS:
            A = np.array([[np.cos(np.pi/18),-np.sin(np.pi/18),0.],
                          [np.sin(np.pi/18),np.cos(np.pi/18),0.],
                          [0.,0.,1.]]) @ A
            
    elif key == glfw.KEY_D:
        if action==glfw.PRESS:
            A = np.array([[np.cos(-np.pi/18),-np.sin(-np.pi/18),0.],
                          [np.sin(-np.pi/18),np.cos(-np.pi/18),0.],
                          [0.,0.,1.]]) @ A
            

            
    elif key == glfw.KEY_X:
        if action==glfw.PRESS:
            A = np.array([[1.0, -0.1,0.],
                          [0.,1.0,0.],
                          [0.,0.,1.]]) @ A

    elif key == glfw.KEY_C:
        if action==glfw.PRESS:
             A = np.array([[1.0, 0.1,0.],
                          [0.,1.0,0.],
                           [0.,0.,1.]]) @ A

    elif key == glfw.KEY_R:
        if action==glfw.PRESS:
            A = np.array([[1.0,0.,0.],
                          [0.,-1.0,0.],
                          [0.,0.,1.]]) @ A


    elif key == glfw.KEY_1:
        if action==glfw.PRESS:
            A = np.array([[1.0,0.,0.],
                          [0.,1.0,0.],
                          [0.,0.,1.]])



def main():
    global A
    if not glfw.init():
        return
    window = glfw.create_window(480,480,"2D Trans", None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        
        glfw.poll_events()


        render(A)

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
