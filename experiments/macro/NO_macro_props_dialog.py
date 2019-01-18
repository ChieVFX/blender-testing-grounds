import bpy

class OpA(bpy.types.Operator):
    bl_idname = "tezt.op_a"
    bl_label = "Hello"
    bl_options = {'INTERNAL'}

    def execute(self, context):
        print("EXECUTE A")
        return {"FINISHED"}
        
class OpProps(bpy.types.Operator):
    bl_idname = "tezt.op_props"
    bl_label = "World"
    bl_options = {'INTERNAL', 'REGISTER', 'UNDO'}

    f_value : bpy.props.FloatProperty()

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        print("EXECUTE PROPS {}".format(self.f_value))
        return {"FINISHED"}
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'f_value', text="F_VAL")
    
class MacroOp(bpy.types.Macro):
    bl_idname = "tezt.macro"
    bl_label = "TEZT"

classes = [
    OpA,
    OpProps,
    MacroOp
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    
    MacroOp.define("TEZT_OT_op_a")
    MacroOp.define("TEZT_OT_op_props")
    MacroOp.define("TEZT_OT_op_a")
    MacroOp.define("OBJECT_OT_select_all")


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)