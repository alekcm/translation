image jaylee_ontop_pc_body_vag_layer:
    "jaylee_ontop_pc_body_vag"
    vagina_colour_transform()
image jaylee_ontop_pc_body_base_layer:
    "jaylee_ontop_pc_body_base"
    skin_base_colour_transform()
image jaylee_ontop_pc_body_shad_layer:
    "jaylee_ontop_pc_body_shad"
    skin_shad_colour_transform()

image jaylee_ontop_pc_writing_ass_layer:
    "jaylee_ontop_pc_writing_ass"
    writing_transform("ass")
image jaylee_ontop_pc_writing_anus_layer:
    "jaylee_ontop_pc_writing_anus"
    writing_transform("anus")

image jaylee_ontop_pc_phair_layer:
    "jaylee_ontop_pc_phair"
    phair_colour_transform()

image jaylee_ontop = LayeredImageProxy("jaylee_ontop_layered", Transform(align=(0.8, 0.0)))

layeredimage jaylee_ontop_layered:
    always "jaylee_ontop_bg"

    always "jaylee_ontop_pc_body_base_layer"
    always "jaylee_ontop_pc_body_shad_layer"
    always "jaylee_ontop_pc_body_vag_layer"

    if writing.ass:
        "jaylee_ontop_pc_writing_ass_layer"
    if writing.anus:
        "jaylee_ontop_pc_writing_anus_layer"
    if acc.anus:
        "jaylee_ontop_pc_plug"
    if player.phair:
        "jaylee_ontop_pc_phair_layer"

    always "jaylee_ontop_jaylee"
    always "jaylee_ontop_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
