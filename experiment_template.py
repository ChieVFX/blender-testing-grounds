#DO NOT CHANGE!
#THIS FILE IS FOR COPY-PASTE INTO "experiment.py" ONLY!

import bpy

#insert your code here: classes, funcs

#this operator is just to get you started
class OpTezt(bpy.types.Operator):
    bl_idname = "tezt.op_tezt"
    bl_label = "TEZZT"

    def execute(self, context):
        return {"FINISHED"}

#remember to add your class here:
classes = [
    OpTezt,
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    
    #insert your code here

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    
    #possibly insert your code here

if __name__ == '__main__':
    register()