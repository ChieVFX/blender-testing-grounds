import bpy
        
def _set_dirty(self, context):
    bpy.ops.tezt.op_a('EXEC_DEFAULT')
    
class OpA(bpy.types.Operator):
    bl_idname = "tezt.op_a"
    bl_label = "Hello"
    bl_options = {'INTERNAL'}

    def execute(self, context):
        print("EXECUTE A")
        return {'FINISHED'}

class OpProps(bpy.types.Operator):
    bl_idname = "tezt.op_props"
    bl_label = "TEZZT"
    bl_options = {'REGISTER', 'UNDO'}

    f_value : bpy.props.FloatProperty(update=_set_dirty)

    def execute(self, context):
        print("EXECUTE PROPS  {}".format(self.f_value))
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        # return wm.invoke_props_dialog(self)
        return self.execute(context)
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'f_value', text="F_VAL")

classes = [
    OpA,
    OpProps,
]

def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)