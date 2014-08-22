import bge as bge
class EventHandler():
	"""class EvenHandler 
	
	"""
	def __init__( self ):

		self.keyboard = bge.logic.keyboard
		self.mouse = bge.logic.mouse
		self.events = bge.events
		self.debug = bge.debug
		
		if self.debug:
			print("EventHandler started")
	
	def getStatus( self, status ):
	
		if status == 1:
			status = "activated"
		elif status == 2:
			status = "active"
		elif status == 3:
			status = "deactivated"
	
		return status
	
	def getCharacter( self, event ):
		
		return self.events.EventToCharacter(event,0)
	
	def getString( self, event ):
		
		return self.events.EventToString(event)
	
	def mouseEvents(self):
	
		return self.mouse.active_events.items()
		
	def keyEvents(self):
	
		return self.keyboard.active_events.items()
	
	def handleKeyEvent( self, string_event, string_status, callback, args=[] ):
	
		for event in self.keyEvents():

			event_string = self.getString( event[0] )
			
			event_status = self.getStatus(event[1])
			
			if event_status == string_status and event_string == string_event:
			
					if self.debug:

						print( event_string, event_status )
					
					try:
					
						callback(*args)
						
					except:
					
						callback()
					
					return
	
	def handleMouseEvent(self, string_event, string_status, callback, args=[]):
		
		for event in self.mouseEvents():
		
			event_string = self.getString(event[0])
			
			event_status = self.getStatus(event[1])
			
			if event_status == string_status and event_string == string_event:
			
					if self.debug:

						print( event_string, event_status )
					
					try:
					
						callback(*args)
						
					except:
					
						callback()
					
					return
			
	def onKey(self, key_char, callback, args=[]):
	
		for event in self.keyEvents():
			
			if self.getStatus(event[1]) == 'activated':
				
				self.handleEvents( event, key_char, callback, args )
					
	def onKeyPress(self, key_char, callback, args=[]):
	
		for event in self.keyEvents():
			
			if self.getStatus(event[1]) == 'active':
			
				self.handleEvents( event, key_char, callback, args )
	
	def onKeyRelease(self, key_char, callback, args=[]):
	
		for event in self.keyEvents():
			
			if self.getStatus(event[1]) == 'deactivated':
			
				self.handleEvents( event, key_char, callback, args )
			
	def handleEvents(self, event, key_char, callback, args=[]):
	
		event_char = self.getCharacter( event[0] )
				
		if event_char == key_char:
		
			try:
			
				callback(*args)
				
			except:
			
				callback()
			
			return
    
if __name__ == "__main__":
    
    EventHandler()