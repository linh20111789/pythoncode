from core.base  import Base 
from core.renderer import Renderer 
from core.scene import Scene 
from core.camera  import Camera 
from core.mesh  import Mesh 
from core.texture import Texture 

from geometry.boxGeometry  import BoxGeometry 
from geometry.rectangleGeometry import RectangleGeometry
from geometry.sphereGeometry import SphereGeometry

from material.pointMaterial import PointMaterial
from material.lineMaterial import LineMaterial
from material.surfaceMaterial import SurfaceMaterial
from material.textureMaterial import TextureMaterial 

from geometry.geometry  import Geometry 
from material.material  import Material 

from extras.movementRig import MovementRig
from extras.movementRig3 import MovementRig3 

# render a basic scene 
class Test(Base):

	def initialize(self):

		self.renderer = Renderer()
		self.scene = Scene()
		self.camera  = Camera()
		
		self.camera.setPosition( [0,2,10] )

		geometry = BoxGeometry()
		material = SurfaceMaterial( {"useVertexColors": True} )

		self.mesh = Mesh( geometry, material )
		self.scene.add( self.mesh )

		self.rig = MovementRig()
		self.rig.add( self.mesh ) 
		self.scene.add( self.rig ) 

		self.rig3 = MovementRig3() 
		self.rig3.add( self.camera ) 
		self.scene.add( self.rig3 ) 
		self.rig3.setPosition( [0, 1, 4] )  

		skyGeometry = SphereGeometry(radius=100) 
		skyMaterial = TextureMaterial( Texture("images/sky.jfif") ) 
		sky = Mesh( skyGeometry, skyMaterial ) 
		self.scene.add( sky ) 
		
		grassGeometry = RectangleGeometry(width=500, height=500)  
		grassMaterial = TextureMaterial( Texture("images/grass.jfif"), {"repeatUV": [50,50]} ) 
		grass = Mesh( grassGeometry, grassMaterial ) 
		grass.rotateX(-3.14/2) 
		self.scene.add( grass ) 

	def update(self):

		self.rig.update( self.input, self.deltaTime )

		self.rig3.update( self.input, self.deltaTime )

		self.renderer.render( self.scene, self.camera ) 

# instantiate this class and run the program 
Test( screenSize=[800,600] ).run() 