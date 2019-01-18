import bpy

class OpA(bpy.types.Operator):
    bl_idname = "tezt.op_a"
    bl_label = "Hello"
    bl_options = {'INTERNAL'}

    def execute(self, context):
        print("EXECUTE A")
        return {"FINISHED"}
        
class OpModalDraw(bpy.types.Operator):
    bl_idname = "tezt.op_modal_draw"
    bl_label = "World"
    bl_options = {'INTERNAL'}

    f_value : bpy.props.FloatProperty()

    def invoke(self, context, event):
        wm = context.window_manager
        wm.modal_handler_add(self)

        self._handle = bpy.types.SpaceView3D.draw_handler_add(self.)

        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if (event.type in {'RIGHTMOUSE', 'ESC'}):
            return self.execute(context)
            
        if (event.type in {'ENTER', 'LEFTMOUSE'}):
            return self.execute(context)
        
        print('MODAL')

        return {'RUNNING_MODAL'}

    def execute(self, context):
        print("MODAL EXECUTE")
        return {"FINISHED"}
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "f_value", text="F_VAL")
    
class MacroOp(bpy.types.Macro):
    bl_idname = "tezt.macro"
    bl_label = "TEZT"

classes = [
    OpA,
    OpModalDraw,
    MacroOp
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    
    MacroOp.define("TEZT_OT_op_a")
    MacroOp.define("TEZT_OT_op_modal_draw")
    MacroOp.define("TEZT_OT_op_a")

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)