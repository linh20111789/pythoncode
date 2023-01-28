from core.attribute import Attribute 

class Geometry(object):
	def __init__(self):

		# Store Attribute objects, indexed by name of associated variable in shader.
		# Shader variable associations set up later and stored in vertex array object in Mesh.
		self.attributes = {}

		# number of vertices
		self.vertexCount = None

	def addAttribute(self, dataType, variableName, data):
		self.attributes[variableName] = Attribute (dataType, data)

	def countVertices(self):
	# number of vertices may be calculated from the length of any Attribute object's array of data
		attrib = list( self.attributes.values() )[0]
		self.vertexCount = len( attrib.data ) 