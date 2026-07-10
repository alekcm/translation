image activity_pubdrink_pc_base_layer:
    "activity_pubdrink_pc_base"
    skin_base_colour_transform()
image activity_pubdrink_pc_shad_layer:
    "activity_pubdrink_pc_shad"
    skin_shad_colour_transform()
image activity_pubdrink_pc_outfit_general_layer:
    "activity_pubdrink_pc_outfit_general"
    outfit_primary_colour_transform()

image activity_pubdrink = LayeredImageProxy("activity_pubdrink_layered", Transform(align=(0.8, 0.0)))

layeredimage activity_pubdrink_layered:
    always "activity_pubdrink_bg"
    always "activity_pubdrink_pc_base_layer"
    always "activity_pubdrink_pc_shad_layer"
    if c.top == 22 and c.bottom == 15:
        "activity_pubdrink_pc_outfit_slut"
    else:
        "activity_pubdrink_pc_outfit_general_layer"
    always "activity_pubdrink_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
