image robin_cumlick_behind_pc_base_layer:
    "robin_cumlick_behind_pc_base"
    skin_base_colour_transform()
image robin_cumlick_behind_pc_shad_layer:
    "robin_cumlick_behind_pc_shad"
    skin_shad_colour_transform()
image robin_cumlick_behind_pc_writing_anus_layer:
    "robin_cumlick_behind_pc_writing_anus"
    writing_transform("anus")
image robin_cumlick_behind_pc_spank_layer:
    "robin_cumlick_behind_pc_spank"
    opacity_transform(bruise.ass)

image robin_cumlick_behind = LayeredImageProxy("robin_cumlick_behind_layer", Transform(align=(0.7, 0.0)))

layeredimage robin_cumlick_behind_layer:
    always "robin_cumlick_behind_bg"
    always "robin_cumlick_behind_pc_base_layer"
    always "robin_cumlick_behind_pc_shad_layer"
    if writing.anus:
        "robin_cumlick_behind_pc_writing_anus_layer"
    always "robin_cumlick_behind_pc_spank_layer"
    always "robin_cumlick_behind_main"




image robin_cumlick_front_bg_plaster = "robin_cumlick_front_bg_room"
image robin_cumlick_front_bg_layer:
    "robin_cumlick_front_bg_" + loc_cur.loc_type

image robin_cumlick_front_pc_base_layer:
    "robin_cumlick_front_pc_base"
    skin_base_colour_transform()
image robin_cumlick_front_pc_shad_layer:
    "robin_cumlick_front_pc_shad"
    skin_shad_colour_transform()
image robin_cumlick_front_pc_belly_base_layer:
    "robin_cumlick_front_pc_belly_base"
    skin_base_colour_transform()
image robin_cumlick_front_pc_belly_shad_layer:
    "robin_cumlick_front_pc_belly_shad"
    skin_shad_colour_transform()
image robin_cumlick_front_pc_writing_pubic_layer:
    "robin_cumlick_front_pc_writing_pubic"
    writing_transform("pubic")
image robin_cumlick_front_pc_writing_belly_1 = "robin_cumlick_front_pc_writing_belly_0"
image robin_cumlick_front_pc_writing_belly_layer:
    "robin_cumlick_front_pc_writing_belly_" + str(player.pregnancy)
    writing_transform("belly")

image robin_cumlick_front_pc_outfit_bimbo_1 = "robin_cumlick_front_pc_outfit_bimbo_0"
image robin_cumlick_front_pc_outfit_bimbo_2 = "robin_cumlick_front_pc_outfit_bimbo_3"
image robin_cumlick_front_pc_outfit_bimbo_layer:
    "robin_cumlick_front_pc_outfit_bimbo_"  + str(player.pregnancy)

image robin_cumlick_front = LayeredImageProxy("robin_cumlick_front_layer", Transform(align=(0.7, 0.0)))

layeredimage robin_cumlick_front_robin_outfit_bimbo_layer:
    if robin.days_pregnant > (global_pregnancy_length * 0.75):
        "robin_cumlick_front_robin_outfit_bimbo_2"
    elif robin.days_pregnant > (global_pregnancy_length * 0.3):
        "robin_cumlick_front_robin_outfit_bimbo_1"
    else:
        "robin_cumlick_front_robin_outfit_bimbo_0"
layeredimage robin_cumlick_front_robin_outfit_slut_layer:
    if robin.days_pregnant > (global_pregnancy_length * 0.75):
        "robin_cumlick_front_robin_outfit_slut_2"
    elif robin.days_pregnant > (global_pregnancy_length * 0.3):
        "robin_cumlick_front_robin_outfit_slut_1"
    else:
        "robin_cumlick_front_robin_outfit_slut_0"
layeredimage robin_cumlick_front_layer:
    always "robin_cumlick_front_bg_layer"
    always "robin_cumlick_front_pc_base_layer"
    always "robin_cumlick_front_pc_shad_layer"
    if player.pregnancy >= 2:
        "robin_cumlick_front_pc_belly_base_layer"
    if player.pregnancy >= 2:
        "robin_cumlick_front_pc_belly_shad_layer"
    if writing.belly:
        "robin_cumlick_front_pc_writing_belly_layer"
    if writing.pubic:
        "robin_cumlick_front_pc_writing_pubic_layer"

    if c.outfit == 11:
        "robin_cumlick_front_pc_outfit_bimbo_layer"
    elif c.top == 22 and c.bottom == 15:
        "robin_cumlick_front_pc_outfit_slut"

    group robin_body:
        attribute normal default "robin_cumlick_front_robin_base_normal"
        attribute bimbo "robin_cumlick_front_robin_base_bimbo"
        attribute slut "robin_cumlick_front_robin_base_bimbo"
    if robin.days_pregnant > (global_pregnancy_length * 0.75):
        "robin_cumlick_front_robin_belly_2"
    elif robin.days_pregnant > (global_pregnancy_length * 0.3):
        "robin_cumlick_front_robin_belly_1"
    group robin_outfit:
        attribute normal default null
        attribute nude null
        attribute bimbo "robin_cumlick_front_robin_outfit_bimbo_layer"
        attribute slut "robin_cumlick_front_robin_outfit_slut_layer"

    always "robin_cumlick_front_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
