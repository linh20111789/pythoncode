from geometry.parametricGeometry import ParametricGeometry 
from math import sin, cos, pi 

class CylindricalGeometry(ParametricGeometry):

	def __init__(self, radiusTop=1, radiusBottom=1, height=1, radialSegments=32, heightSegments=4, closedTop=True, closedBottom=True):
		def S(u,v):
			return [(v*radiusTop + (1-v)*radiusBottom) * sin(u), 
					height * (v - 0.5),
					(v*radiusTop + (1-v)*radiusBottom) * cos(u) ]	

		super().__init__( 0, 2*pi, radialSegments, 0, 1, heightSegments, S ) 