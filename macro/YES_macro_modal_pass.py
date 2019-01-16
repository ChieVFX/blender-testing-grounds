import bpy

class OpA(bpy.types.Operator):
    bl_idname = "tezt.op_a"
    bl_label = "Hello"
    bl_options = {'INTERNAL'}

    def execute(self, context):
        print("EXECUTE A")
        return {"FINISHED"}
        
class OpModal(bpy.types.Operator):
    bl_idname = "tezt.op_modal"
    bl_label = "World"
    bl_options = {'INTERNAL'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.modal_handler_add(self)

        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if (event.type in {'RIGHTMOUSE', 'ESC'}):
            return {'CANCELLED'}
            
        if (event.type in {'ENTER', 'LEFTMOUSE'}):
            return self.execute(context)
        
        print('MODAL')

        return {'PASS_THROUGH'}

    def execute(self, context):
        print("MODAL EXECUTE")
        return {"FINISHED"}
    
class MacroOp(bpy.types.Macro):
    bl_idname = "tezt.macro"
    bl_label = "TEZT"

classes = [
    OpA,
    OpModal,
    MacroOp
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    
    MacroOp.define("TEZT_OT_op_a")
    MacroOp.define("TEZT_OT_op_modal")
    MacroOp.define("TEZT_OT_op_a")

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)