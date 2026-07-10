image robin_prone_man_base_layer:
    "robin_prone_man_base"
    npc_skin_base_colour_transform()
image robin_prone_man_shad_layer:
    "robin_prone_man_shad"
    npc_skin_shad_colour_transform()

image robin_prone = LayeredImageProxy("robin_prone_layered", Transform(align=(0.8, 0.0)))

layeredimage robin_prone_layered:
    always "robin_prone_bg"
    always "robin_prone_man_base_layer"
    always "robin_prone_man_shad_layer"
    always "robin_prone_robin_base"

    group robin_face:
        attribute happy default "robin_prone_robin_face_happy"
        attribute down "robin_prone_robin_face_down"
        attribute front "robin_prone_robin_face_front"

    always "robin_prone_frame"   
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
