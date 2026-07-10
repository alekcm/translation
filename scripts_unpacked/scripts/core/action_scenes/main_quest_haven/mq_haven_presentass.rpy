image haven_presentass_pc_spank_layer:
    "haven_presentass_pc_spank"
    opacity_transform(bruise.ass)

image haven_presentass_pc_writing_whore_layer:
    "haven_presentass_pc_writing_whore"
    writing_transform("forehead")
image haven_presentass_pc_writing_slut_layer:
    "haven_presentass_pc_writing_slut"
    writing_transform("face")
image haven_presentass_pc_writing_fuckme_layer:
    "haven_presentass_pc_writing_fuckme"
    writing_transform("lleg")
image haven_presentass_pc_writing_anal_layer:
    "haven_presentass_pc_writing_anal"
    writing_transform("ass")
image haven_presentass_pc_writing_counter_layer:
    "haven_presentass_pc_writing_counter"
    writing_transform("anus")

layeredimage haven_presentass:
    if loc_cur.loc_type == "room":
        "haven_presentass_bg_bunk"
    elif loc_cur.loc_type == "plaster":
        "haven_presentass_bg_bed"
    else:
        "haven_presentass_bg_boxes"

    group pc auto:
        attribute lookback default

    always:
        "haven_presentass_pc_ass"

    group man auto:
        attribute inside:
            "haven_presentass_man_inside_shad"
        attribute poke:
            "haven_presentass_man_poke_shad"





    always:
        "haven_presentass_pc_spank_layer"

    if writing.forehead:
        if_any "lookback" "haven_presentass_pc_writing_whore_layer"
    if writing.face:
        if_any "lookback" "haven_presentass_pc_writing_slut_layer"
    if writing.lleg:
        "haven_presentass_pc_writing_fuckme"
    if writing.anus:
        "haven_presentass_pc_writing_anal"
    if writing.ass:
        "haven_presentass_pc_writing_counter"

    if player.cum_locations["cum_vagin"]:
        "haven_presentass_pc_cumin"
    if player.cum_locations["cum_vagout"]:
        "haven_presentass_pc_cumass"


    group man auto:
        attribute inside:
            "haven_presentass_man_inside"
        attribute poke:
            "haven_presentass_man_poke"
        attribute mast:
            "haven_presentass_man_mast"
        attribute noman default:
            null

    always:
        "haven_presentass_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
