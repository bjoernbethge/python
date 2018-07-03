import bpy

bl_info = {"name": "Texture", "category": "GL"}

def create_textures(context):
    for image in bpy.data.images:
        if not image.name in [texture.name for texture in bpy.data.textures]:
            tex = bpy.data.textures.new(image.name, type = 'IMAGE')
            tex.image = image
             # Create material
            mat = bpy.data.materials.new(image.name)
         
            # Add texture slot for color texture
            slot = mat.texture_slots.add()
            slot.texture = tex
            slot.use_map_normal = True
			
    
def main(context):
    context.scene.use_nodes = True
    tree = context.scene.node_tree
    links = tree.links
     
    # clear default nodes
    for n in tree.nodes:
        tree.nodes.remove(n)
     
    file_node = tree.nodes.new('CompositorNodeOutputFile')
    file_node.file_slots.remove(file_node.inputs[0])
    y = 0
    for texture in bpy.data.textures:
        if not texture.type in ['IMAGE', 'NONE']:
            viewer_node = tree.nodes.new('CompositorNodeViewer')
            viewer_node.location = 500, y
            name = '%s_viewer' % texture.name
            viewer_node.name = viewer_node.label = name
            
            texture_node = tree.nodes.new('CompositorNodeTexture')
            texture_node.name = texture.name
            texture_node.label = texture.name
            texture_node.texture = texture
            texture_node.location = 0,y
            y -= 300
            
            input = file_node.file_slots.new(texture.name)

            links.new(texture_node.outputs[1], input)
            links.new(texture_node.outputs[1], viewer_node.inputs[0])

    file_node.location = 300, y/2+texture_node.height
        
class TextureOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "image.images_to_texture"
    bl_label = "Images to Textures"

    def execute(self, context):
        create_textures(context)
        return {'FINISHED'}            

class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.object.simple_operator()
