image pc_body_womb_3_base_layer:
    "pc_body_womb_3_base"
    matrixcolor TintMatrix(get_preg_colour())

layeredimage pc_body_womb_3_layer:
    always "pc_body_womb_3_base_layer"
    always "pc_body_womb_3_col"

image pc_body_womb_3:
    Flatten("pc_body_womb_3_layer")
    matrixcolor OpacityMatrix(0.35)

image pc_body_womb_2_base_layer:
    "pc_body_womb_2_base"
    matrixcolor TintMatrix(get_preg_colour())

layeredimage pc_body_womb_2_layer:
    always "pc_body_womb_2_base_layer"
    always "pc_body_womb_2_col"

image pc_body_womb_2:
    Flatten("pc_body_womb_2_layer")
    matrixcolor OpacityMatrix(0.35)

image pc_body_womb_1_base_layer:
    "pc_body_womb_1_base"
    matrixcolor TintMatrix(get_preg_colour())

layeredimage pc_body_womb_1_layer:
    always "pc_body_womb_1_base_layer"
    always "pc_body_womb_1_col"

image pc_body_womb_1:
    Flatten("pc_body_womb_1_layer")
    matrixcolor OpacityMatrix(0.35)

image pc_body_womb_0:
    "pc_body_womb_0_base"
    matrixcolor OpacityMatrix(0.35)

layeredimage pc_womb:

    if player.pregnancy == 3:
        "pc_body_womb_3"
    elif player.pregnancy == 2:
        "pc_body_womb_2"
    elif player.pregnancy == 1 and player.preg_knows:
        "pc_body_womb_1"
    elif player.preg_knows:
        "pc_body_womb_0"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
