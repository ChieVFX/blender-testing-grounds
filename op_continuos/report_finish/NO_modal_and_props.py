import bpy
        
class OpModal(bpy.types.Operator):
    bl_idname = "tezt.op_modal"
    bl_label = "TEZZT"
    # bl_options = {'INTERNAL'}
    bl_options = {'REGISTER', 'UNDO'}

    f_prop = bpy.props.FloatProperty()

    def invoke(self, context, event):
        wm = context.window_manager
        wm.modal_handler_add(self)

        return wm.invoke_props_popup(self, event)

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

classes = [
    OpModal,
]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)