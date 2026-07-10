layeredimage pc_lefthand_gloves:


    if c.gloves == 1 and player.prop in larm_beer:
        "pc_gloves_fingerless_larmbeer_base_layer"
    elif c.gloves == 1:
        "pc_gloves_fingerless_larmdown_base_layer"

    elif c.gloves == 2 and player.prop in larm_beer:
        "pc_gloves_sleeve_larmbeer_base_layer"
    elif c.gloves == 2:
        "pc_gloves_sleeve_larmdown_base_layer"




    if c.gloves == 1 and player.prop in larm_beer:
        "pc_gloves_fingerless_larmbeer_lines_layer"
    elif c.gloves == 1:
        "pc_gloves_fingerless_larmdown_lines_layer"

    elif c.gloves == 2 and player.prop in larm_beer:
        "pc_gloves_sleeve_larmbeer_lines_layer"
    elif c.gloves == 2:
        "pc_gloves_sleeve_larmdown_lines_layer"


layeredimage pc_righthand_gloves:

    if c.gloves == 1 and weather_var in (3,4) and outside:
        "pc_gloves_fingerless_rarmumb_base_layer"
    elif c.gloves == 1 and player.prop in rarm_beer:
        "pc_gloves_fingerless_rarmbeer_base_layer"
    elif c.gloves == 1:
        "pc_gloves_fingerless_rarmdown_base_layer"

    elif c.gloves == 2 and weather_var in (3,4) and outside:
        "pc_gloves_sleeve_rarmumb_base_layer"
    elif c.gloves == 2 and player.prop in rarm_beer:
        "pc_gloves_sleeve_rarmbeer_base_layer"
    elif c.gloves == 2:
        "pc_gloves_sleeve_rarmdown_base_layer"




    if c.gloves == 1 and weather_var in (3,4) and outside:
        "pc_gloves_fingerless_rarmumb_lines_layer"
    elif c.gloves == 1 and player.prop in rarm_beer:
        "pc_gloves_fingerless_rarmbeer_lines_layer"
    elif c.gloves == 1:
        "pc_gloves_fingerless_rarmdown_lines_layer"

    elif c.gloves == 2 and weather_var in (3,4) and outside:
        "pc_gloves_sleeve_rarmumb_lines_layer"
    elif c.gloves == 2 and player.prop in rarm_beer:
        "pc_gloves_sleeve_rarmbeer_lines_layer"
    elif c.gloves == 2:
        "pc_gloves_sleeve_rarmdown_lines_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
