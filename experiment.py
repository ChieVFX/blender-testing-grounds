import bpy

class OpTeztPopup(bpy.types.Operator):
    bl_idname = "tezt.op_tezt_p"
    bl_label = "TEZZT_P"
    bl_options = {'REGISTER', 'UNDO'}

    location_x : bpy.props.FloatProperty()

    def execute(self, context):
        d1 = str(context.object.matrix_world)
        context.object.location[0] = self.location_x
        
        #throw everything, something might stick:
        context.scene.update()
        bpy.context.scene.update()
        
        d2 = str(context.object.matrix_world)
        debug = "{} ::: {}".format(d1, d2)
        print(debug)
        op : bpy.types.Operator = self
        op.report({'INFO'}, debug)
        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)

classes = [
    OpTeztPopup
]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == '__main__':
    register()