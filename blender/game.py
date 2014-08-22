from bge import logic, events
from EventHandler import EventHandler

bge.debug = False
handleMouseEvent = EventHandler.handleMouseEvent


class Settings:
    
    show_mouse = False

class Game:
    
    scene = logic.getCurrentScene()
    camera = scene.active_camera
    controller = logic.getCurrentController()
    objects = scene.objects
    
def clickObject():
    
    return Game.camera.getScreenRay(logic.mouse.position[0], logic.mouse.position[1], 100)
    
def handleEvents():
    
    handleMouseEvent('LEFTMOUSE', 'activated', clickObject)
            

def main():
  
  handleEvents()
