init python:
    avatar_bool_1 = False
    avatar_bool_2 = False
    def refresh_clothes():
        global avatar_bool_1, avatar_bool_2
        avatar_bool_2 = not avatar_bool_1

screen pc_avatar_image:

    if avatar_bool_1 != avatar_bool_2:
        $ renpy.restart_interaction
        $ avatar_bool_2 = avatar_bool_1
    zorder 1

    if c.bra:
        if c.bra == 1:
            add "fcup_layer"
        elif c.bra == 2:
            add "sport1_layer"
        elif c.bra == 3:
            add "sport2_layer"
        elif c.bra == 4:
            add "strapless_layer"
        elif c.bra == 5:
            add "shelf_layer"
        elif c.bra == 6:
            add "open_bra_layer"
        elif c.bra == 7:
            add "stringfront_layer"
        elif c.bra == 8:
            add "wrap_bra_layer"
        elif c.bra == 9:
            add "frilly_bra_layer"
        elif c.bra == 10:
            add "triangle_bra_layer"
        elif c.bra == 11:
            add "simple_bra_layer"
        elif c.bra == 12:
            add "half_bra_layer"

    if player.pregnancy == 1 or player.isfat:
        add "body_preg_base"
    elif player.pregnancy == 2:
        add "body_preg_base"
    elif player.pregnancy == 3:
        add "body_preg_base"
    if player.pregnancy == 1 or player.isfat:
        add "body_preg_shad"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
