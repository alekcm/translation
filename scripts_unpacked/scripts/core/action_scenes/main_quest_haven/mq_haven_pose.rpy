image haven_pose1_spank_layer:
    "haven_pose1_spank"
    opacity_transform(bruise.ass)

image haven_pose1_writing_ass_layer:
    "haven_pose1_writing_ass"
    writing_transform("ass")
image haven_pose1_writing_anus_layer:
    "haven_pose1_writing_anus"
    writing_transform("anus")
image haven_pose1_writing_face_layer:
    "haven_pose1_writing_face"
    writing_transform("face")
image haven_pose1_writing_forehead_layer:
    "haven_pose1_writing_forehead"
    writing_transform("forehead")


layeredimage haven_pose1:

    always:
        "haven_pose1_base"
    always:
        "haven_pose1_spank_layer"
    if writing.ass:
        "haven_pose1_writing_ass_layer"
    if writing.anus:
        "haven_pose1_writing_anus_layer"
    if writing.face:
        "haven_pose1_writing_face_layer"
    if writing.forehead:
        "haven_pose1_writing_forehead_layer"








    if c.top:
        "haven_pose1_topon"
    if c.bottom:
        "haven_pose1_shorts"

    group face auto:
        attribute norm default


    always:
        "haven_pose1_hair"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
