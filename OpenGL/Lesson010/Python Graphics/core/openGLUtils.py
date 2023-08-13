from OpenGL import GL

# static methods to load/compile OpenGL shaders
#  and link to create GPU programs

class OpenGLUtils(object):

    @staticmethod
    def initializeShader(shaderCode, shaderType):

        # specify OpenGL version and requirements
        shaderCode = "#version 330 \n" + shaderCode

        # create empty shader object and return reference value
        shaderRef = GL.glCreateShader(shaderType)
        # store source code in shader
        GL.glShaderSource(shaderRef, shaderCode)
        # compile source code stored in shader
        GL.glCompileShader(shaderRef)

        # query whether compilation was successful
        compileSuccess = GL.glGetShaderiv(shaderRef, GL.GL_COMPILE_STATUS)
        if not compileSuccess:
            # retrieve error message
            errorMessage = GL.glGetShaderInfoLog(shaderRef)
            # free memory used to store shader program
            GL.glDeleteShader(shaderRef)
            # convert byte string to character string
            errorMessage = "\n" + errorMessage.decode("utf-8")
            # raise exception, halt program, print error message
            raise Exception(errorMessage)

        # compilation was successful
        return shaderRef
    
    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):

        # compile shaders and store references
        vertexShaderRef = OpenGLUtils.initializeShader(vertexShaderCode, GL.GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtils.initializeShader(fragmentShaderCode, GL.GL_FRAGMENT_SHADER)

        # create program object and store reference
        programRef = GL.glCreateProgram()

        # attach previously compiled shaders
        GL.glAttachShader(programRef, vertexShaderRef)
        GL.glAttachShader(programRef, fragmentShaderRef)

        # link vertex shader to fragment shader
        GL.glLinkProgram(programRef)

        # query if linking was successful
        linkSuccess = GL.glGetProgramiv(programRef, GL.GL_LINK_STATUS)
        if not linkSuccess:
            # retrieve error message
            errorMessage = GL.glGetProgramInfoLog(programRef)
            # free memory used to store program
            GL.glDeleteProgram(programRef)
            # convert byte string to character string
            errorMessage = "\n" + errorMessage.decode("utf-8")
            # raise exception, halt program, print error message
            raise Exception(errorMessage)
        
        # linking was successful, return program reference
        return programRef
    