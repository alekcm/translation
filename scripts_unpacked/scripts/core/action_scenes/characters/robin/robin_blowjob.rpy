image robin_blowjob_man_base_layer:
    "robin_blowjob_man_base"
    npc_skin_base_colour_transform()
image robin_blowjob_man_shad_layer:
    "robin_blowjob_man_shad"
    npc_skin_shad_colour_transform()

image robin_blowjob = LayeredImageProxy("robin_blowjob_layered", Transform(align=(0.7, 0.0)))

layeredimage robin_blowjob_layered:
    if loc_cur.loc_type == "tile":
        "robin_blowjob_bg_tile"
    else:
        "robin_blowjob_bg_grass"

    always "robin_blowjob_man_base_layer"
    always "robin_blowjob_man_shad_layer"

    always "robin_blowjob_robin_body"
    if robin_here(dis_beach.locs):
        "robin_blowjob_robin_outfit_swim"
    elif t.wkday in weekdays and t.hour in school_hours:
        "robin_blowjob_robin_outfit_uni"
    elif (global_random_number % 2):
        "robin_blowjob_robin_outfit_baggy"
    else:
        "robin_blowjob_robin_outfit_hoodie"

    if (t.minute % 3) == 0:
        "robin_blowjob_robin_1h"
    elif (t.minute % 3) == 1:
        "robin_blowjob_robin_2h"

    always "robin_blowjob_frame"   
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
