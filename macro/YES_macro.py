import bpy

class OpA(bpy.types.Operator):
    bl_idname = "tezt.op_a"
    bl_label = "Hello"
    bl_options = {'INTERNAL'}

    def execute(self, context):
        print("EXECUTE A")
        return {"FINISHED"}
        
class OpB(bpy.types.Operator):
    bl_idname = "tezt.op_b"
    bl_label = "World"
    bl_options = {'INTERNAL'}

    def execute(self, context):
        print("EXECUTE B")
        return {"FINISHED"}
    
class MacroOp(bpy.types.Macro):
    bl_idname = "tezt.macro"
    bl_label = "TEZT"

classes = [
    OpA,
    OpB,
    MacroOp
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    
    MacroOp.define("TEZT_OT_op_a")
    MacroOp.define("TEZT_OT_op_b")
    MacroOp.define("OBJECT_OT_select_all")


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)