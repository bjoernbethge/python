import bpy
from bpy.utils import register_module, unregister_module
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator

bl_info = {"name": "World", "category": "GL"}

def add_environment(context, filepath):
    try:
        img = bpy.data.images.load(filepath)
    except:
        raise NameError("Cannot load image %s" % realpath)
 
    envtex = bpy.data.textures.new('Environment', type = 'IMAGE')
    envtex.image = img
    context.scene.world.use_sky_real = True
    mtex = context.scene.world.texture_slots.add()
    mtex.texture = envtex
    mtex.use_map_blend = False
    mtex.use_map_horizon = True
    mtex.texture_coords = 'EQUIRECT'

    return {'FINISHED'}

class AddEnvironment(Operator, ImportHelper):
    """Add Environtment Texture"""
    bl_idname = "world_add.environment"
    bl_label = "Add Environtment"
    
    def execute(self, context):
        return add_environment(context, self.filepath)

def menu_func_import(self, context):
    self.layout.operator(AddEnvironment.bl_idname, text="Add Environment")

def register():
    
    register_module(__name__)
    bpy.types.INFO_MT_file.append(menu_func_import)

def unregister():
    
    unregister_module(__name__)
    bpy.types.INFO_MT_file.remove(menu_func_import)

if __name__ == "__main__":
    register()

    # test call
    bpy.ops.world_add.environment('INVOKE_DEFAULT')
