#DO NOT CHANGE!
#THIS FILE CONTAINS SNIPPETS! FOR COPY-PASTE ONLY!
import bpy


class OpTezt(bpy.types.Operator):
    bl_idname = "tezt.op_tezt"
    bl_label = "TEZZT"

    def execute(self, context):
        return {"FINISHED"}
        

class OpTeztModal(bpy.types.Operator):
    bl_idname = "tezt.op_tezt_m"
    bl_label = "TEZZT_M"

    def execute(self, context):
        #insert you code here
        return {"FINISHED"}
    
    def modal(self, context, event):
        if event in ['ESC', 'RIGHTMOUSE']:
            return {'CANCELLED'}
        
        if event in ['ENTER', 'LEFTMOUSE']:
            return self.execute(context)

        #insert you code here
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        #insert you code here
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}


class OpTeztPopup(bpy.types.Operator):
    bl_idname = "tezt.op_tezt_p"
    bl_label = "TEZZT_P"
    bl_options = {'REGISTER', 'UNDO'}

    #insert props here

    def execute(self, context):
        #insert you code here
        return {"FINISHED"}

    def invoke(self, context, event):
        #insert you code here
        return context.window_manager.invoke_props_popup(self, event)
    
    def draw(self, context):
        pass
        

class OpTeztDialog(bpy.types.Operator):
    bl_idname = "tezt.op_tezt_p"
    bl_label = "TEZZT_P"
    bl_options = {'REGISTER', 'UNDO'}

    #insert props here

    def execute(self, context):
        #insert you code here
        return {"FINISHED"}

    def invoke(self, context, event):
        #insert you code here
        return context.window_manager.invoke_props_dialog(self, event)

    def draw(self, context):
        pass