from core.object3D import Object3D 

class MovementRig3(Object3D):

	def __init__(self, unitsPerSecond=5, degreesPerSecond=30):

		# initialize base Object3D; controls movement 
		# and turn left/right
		super().__init__()

		# initialize attached Object3D; controls look up/down
		self.lookAttachment = Object3D()
		self.children = [ self.lookAttachment ]
		self.lookAttachment.parent = self

		# control rate of movement
		self.unitsPerSecond  = unitsPerSecond
		self.degreesPerSecond = degreesPerSecond

		# customizable key mappings 
		#  defaults: WASDRF (move), QE (turn), UO (look) 
		self.KEY_MOVE_FORWARDS = "w" 
		self.KEY_MOVE_BACKWARDS = "s" 
		self.KEY_MOVE_LEFT = "a" 
		self.KEY_MOVE_RIGHT  = "d" 

		self.KEY_MOVE_UP = "i" 
		self.KEY_MOVE_DOWN = "k" 

		self.KEY_YAW_LEFT = "left" 
		self.KEY_YAW_RIGHT  = "right" 

		self.KEY_PITCH_UP = "up" 
		self.KEY_PITCH_DOWN = "down" 

		self.KEY_ROLL_LEFT = ","
		self.KEY_ROLL_RIGHT = "."

	# adding and removing objects applies to look attachment;
	#  override functions from Object3D class 
	def add(self, child):
		self.lookAttachment.add(child)

	def remove(self, child):
		self.lookAttachment.remove(child) 

	def update(self, inputObject, deltaTime): 
		moveAmount = self.unitsPerSecond * deltaTime
		rotateAmount = self.degreesPerSecond * (3.1415926 / 180) * deltaTime
		if inputObject.isKeyPressed(self. KEY_MOVE_FORWARDS):
			self.translate( 0, 0, -moveAmount )
		if inputObject.isKeyPressed(self. KEY_MOVE_BACKWARDS):
			self.translate( 0, 0, moveAmount )
		if inputObject.isKeyPressed(self.KEY_MOVE_LEFT):
			self.translate( -moveAmount, 0, 0 )
		if inputObject.isKeyPressed(self.KEY_MOVE_RIGHT):
			self.translate( moveAmount, 0, 0 )
		if inputObject.isKeyPressed(self.KEY_MOVE_UP):
			self.translate( 0, moveAmount, 0 )
		if inputObject.isKeyPressed(self.KEY_MOVE_DOWN):
			self.translate( 0, -moveAmount, 0 )
		if inputObject.isKeyPressed(self.KEY_YAW_RIGHT):
			self.rotateY( -rotateAmount )
		if inputObject.isKeyPressed(self.KEY_YAW_LEFT):
			self.rotateY( rotateAmount )
		if inputObject.isKeyPressed(self.KEY_PITCH_UP):
			self.lookAttachment.rotateX( rotateAmount )
		if inputObject.isKeyPressed(self.KEY_PITCH_DOWN):
			self.lookAttachment.rotateX( -rotateAmount ) 
		if inputObject.isKeyPressed(self.KEY_ROLL_LEFT):
			self.lookAttachment.rotateZ( rotateAmount )
		if inputObject.isKeyPressed(self.KEY_ROLL_RIGHT):
			self.lookAttachment.rotateZ( -rotateAmount ) 
		