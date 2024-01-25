import maya.cmds as cmds

selected = cmds.ls(sl=1)

if len(selected) < 2:
    cmds.error("Please select 2 obj!")

obj_1 = selected[0]
obj_2 = selected[1]
print(obj_1,obj_2)

history_1 = cmds.listHistory(obj_1)
blendShapeNode_1 = cmds.ls( history_1, type='blendShape')
if len(blendShapeNode_1) == 0:
    cmds.error("first object do not have blendShape")
blendShapeNames_1 = cmds.listAttr(blendShapeNode_1[0]+'.w', m=True)

history_2 = cmds.listHistory(obj_2)
blendShapeNode_2 = cmds.ls( history_2, type='blendShape')

if len(blendShapeNode_2) == 0:
    cmds.error("second object do not have blendShape")
    
blendShapeNames_2 = cmds.listAttr(blendShapeNode_2[0]+'.w', m=True)

if len(blendShapeNames_1) != len(blendShapeNames_2):
    cmds.warning("They do not have same amount of blendShapes!")
    
set1 = set(blendShapeNames_1)
set2 = set(blendShapeNames_2)
intersection = list(set1 & set2)


while intersection:
    bs = intersection.pop()
    cmds.connectAttr(blendShapeNode_1[0]+".{0}".format(bs), blendShapeNode_2[0]+".{0}".format(bs), f=True)
    
cmds.confirmDialog(title="Process Status", message="Process Finished", button=['OK'])


