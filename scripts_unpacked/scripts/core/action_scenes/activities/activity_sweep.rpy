

image activity_sweep_bg_beach = "activity_sweep_bg_grass"
image activity_sweep_bg_plaster = "activity_sweep_bg_room"
image activity_sweep_bg_layer:
    "activity_sweep_bg_" + loc_cur.loc_type



image activity_sweep_pc_body_base_layer:
    "activity_sweep_pc_body_base"
    skin_base_colour_transform()
image activity_sweep_pc_body_shad_layer:
    "activity_sweep_pc_body_shad"
    skin_shad_colour_transform()

image activity_sweep = LayeredImageProxy("activity_sweep_layeredimage", Transform(align=(0.7, 0.0)))

layeredimage activity_sweep_layeredimage:
    if loc(loc_pub):
        "activity_sweep_bg_pub"
    else:
        "activity_sweep_bg_layer"

    always "activity_sweep_pc_body_base_layer"
    always "activity_sweep_pc_body_shad_layer"
    if c.outfit == 6:
        "activity_sweep_outfit_pub"
    elif c.outfit == 19:
        "activity_sweep_outfit_dungarees"
    elif c.outfit == 20:
        "activity_sweep_outfit_maid"

    always "activity_sweep_frame"

layeredimage activity_sweep_outfit_pub:
    if c.pants:
        "activity_sweep_pc_outfit_pub_pants"
    if c.socks:
        "activity_sweep_pc_outfit_pub_socks"
    always "activity_sweep_pc_outfit_pub_dress"
layeredimage activity_sweep_outfit_maid:
    if c.pants:
        "activity_sweep_pc_outfit_maid_pants"
    if c.socks:
        "activity_sweep_pc_outfit_maid_socks"
    always "activity_sweep_pc_outfit_maid_dress"
layeredimage activity_sweep_outfit_dungarees:
    if c.gloves:
        "activity_sweep_pc_outfit_dungarees_gloves"
    always "activity_sweep_pc_outfit_dungarees_body"




image activity_broom_bg_grass = "activity_broom_bg_conc"
image activity_broom_bg_layer:
    "activity_broom_bg_" + loc_cur.loc_type

image activity_broom = LayeredImageProxy("activity_broom_layeredimage", Transform(align=(0.7, 0.0)))

layeredimage activity_broom_layeredimage:
    if loc(loc_pub):
        "activity_broom_bg_pub"
    else:
        "activity_broom_bg_layer"
    always "activity_broom_main"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
