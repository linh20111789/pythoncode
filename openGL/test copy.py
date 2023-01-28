import pywavefront
import pyglet

from pyglet.gl import *

def create_object(obj_file):
        # Load the object
    scene = pywavefront.Wavefront(obj_file)

    # Create a list of vertices
    vertices = []
    for mesh in scene.meshes:
        vertices += mesh.vertices

    # Create a list of indices
    indices = []
    for mesh in scene.meshes:
        indices += mesh.indices

    return vertices, indices

def draw_object(vertices, indices):
    # Enable vertex arrays
    glEnableClientState(GL_VERTEX_ARRAY)

    # Set the vertex pointers and draw the triangles
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, indices)

    # Disable vertex arrays
    glDisableClientState(GL_VERTEX_ARRAY)

# Load the object
vertices, indices = create_object('aaaa.obj')

# Create a window
window = pyglet.window.Window()

# Set the drawing function
@window.event
def on_draw():
    # Clear the window
    window.clear()

    # Draw the object
    draw_object(vertices, indices)

# Run the pyglet loop
pyglet.app.run()
