image dance_gropeass_bg_layer:
    "dance_gropeass_bg"
    desire_colour_transform()

image dance_gropeass_body_base_layer:
    "dance_gropeass_body_base"
    skin_base_colour_transform()
image dance_gropeass_body_shad_layer:
    "dance_gropeass_body_shad"
    skin_shad_colour_transform()
image dance_gropeass_body_skirtshad_layer:
    "dance_gropeass_body_skirtshad"
    skin_shad_colour_transform(0.5)



image dance_gropeass_pants1_layer:
    "dance_gropeass_pants1"
    pants_primary_colour_transform()
image dance_gropeass_pants2_layer:
    "dance_gropeass_pants2"
    pants_primary_colour_transform()
image dance_gropeass_skirt_norm_layer:
    "dance_gropeass_skirt_norm"
    bottom_primary_colour_transform()
image dance_gropeass_skirt_grope_layer:
    "dance_gropeass_skirt_grope"
    bottom_primary_colour_transform()
image dance_gropeass_tights_layer:
    "dance_gropeass_tights"
    socks_primary_colour_transform()

layeredimage dance_gropeass:

    always:
        "dance_gropeass_bg_layer"

    group man:
        attribute grope:
            "dance_gropeass_man_side"
        attribute finger:
            "dance_gropeass_man_side"
        attribute mast:
            "dance_gropeass_man_side"



    always:
        "dance_gropeass_body_base_layer"
    group skirt:
        attribute skirton:
            "dance_gropeass_body_skirtshad_layer"
    always:
        "dance_gropeass_body_shad_layer"

    if player.cum_locations["cum_vagin"]:
        "dance_gropeass_cumin"
    if player.cum_locations["cum_vagout"] or player.cum_locations["cum_assout"]:
        "dance_gropeass_cumout"

    if c.pants > 0 and c.thong:
        "dance_gropeass_pants2_layer"
    elif c.pants > 0:
        "dance_gropeass_pants1_layer"

    if c.socks > 0:
        "dance_gropeass_tights_layer"




    group skirt:
        attribute skirton default if_any ["grope", "finger"]:
            "dance_gropeass_skirt_grope_layer"
        attribute skirton default if_not ["grope", "finger"]:
            "dance_gropeass_skirt_norm_layer"
        attribute skirtoff:
            null


    group man:
        attribute grope:
            "dance_gropeass_man_side_grope"
        attribute finger:
            "dance_gropeass_man_side_finger"
        attribute mast:
            "dance_gropeass_man_side_mast"
        attribute rub:
            "dance_gropeass_man_pen_rub"
        attribute pokemast:
            "dance_gropeass_man_pen_pokemast"
        attribute poke:
            "dance_gropeass_man_pen_poke"
        attribute inside:
            "dance_gropeass_man_pen_inside"

    always:
        "dance_gropeass_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
