from xml.etree import ElementTree as xml

class XMLGenerator(object):

	def __init__(self):
	
		self.root = None
		
	def create_root(self, element_name):
	
		self.root = xml.Element(element_name)
		
	def sub (self, parent, element_name, *args):
	
		if(args): 
	
			return xml.SubElement(parent, element_name, args[0])
			
		else:
		
			return xml.SubElement(parent, element_name)
			
	def write(self, filepath):
	
		xml.ElementTree(self.root).write(filepath, encoding="UTF-8",  xml_declaration=True)
		
if __name__ == "__main__":

	XMLGenerator()
