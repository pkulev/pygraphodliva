#!/usr/bin/env python

from OpenGLContext import testingcontext  # noqa
from OpenGLContext.arrays import array
from OpenGL.arrays import vbo
from OpenGL.GL import (
    shaders,
    glEnableClientState,
    glDisableClientState,
    glDrawArrays,
    GL_TRIANGLES,
    GL_FRAGMENT_SHADER,
    GL_VERTEX_SHADER,
    GL_VERTEX_ARRAY
)


class TestContext(testingcontext.getInteractive()):
    """Create a simple vertex shader."""

    def __init__(self):
        super(TestContext, self).__init__()
        self.shader = None
        self.vbo = []

    def OnInit(self):
        """Init"""

        vertex = shaders.compileShader(
            """
            #version 120
            void main()
            {
                gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
            }
            """, GL_VERTEX_SHADER)

        fragment = shaders.compileShader(
            """
            #version 120
            void main ()
            {
                gl_FragColor = vec4(0, 1, 0, 1);
            }
            """, GL_FRAGMENT_SHADER)

        self.shader = shaders.compileProgram(vertex, fragment)
        self.vbo = vbo.VBO(
            array([
                [0, 1, 0],
                [-1, -1, 0],
                [1, -1, 0],
                [2, -1, 0],
                [4, -1, 0],
                [4, 1, 0],
                [2, -1, 0],
                [4, 1, 0],
                [2, 1, 0],
            ], 'f')
        )

    def Render(self, mode):
        """Render the geometry for the scene."""

        shaders.glUseProgram(self.shader)
        try:
            self.vbo.bind()
            try:
                glEnableClientState(GL_VERTEX_ARRAY)
                GLVertexPointer(self.vbo)
                glDrawArrays(GL_TRIANGLES, 0, 9)
            finally:
                self.vbo.unbind()
                glDisableClientState(GL_VERTEX_ARRAY)
        finally:
            shaders.glUseProgram(0)

if __name__ == "__main__":
    TestContext.ContextMainLoop()
