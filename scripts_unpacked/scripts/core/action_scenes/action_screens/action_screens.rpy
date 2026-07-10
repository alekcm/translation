image cum_image = im.MatrixColor(("white.png"), im.matrix.tint(0.960, 0.956, 0.937))
image cum_image_pink = im.MatrixColor(("white.png"), im.matrix.tint(0.968, 0.450, 0.831))
image virgin_image = im.MatrixColor(("white.png"), im.matrix.tint(0.431, 0.090, 0.098))
image vagsex_image = im.MatrixColor(("white.png"), im.matrix.tint(0.968, 0.670, 0.905))
image asssex_image = im.MatrixColor(("white.png"), im.matrix.tint(0.596, 0.435, 0.341))

init python:

    def get_sex_cutin(location):
        if renpy.get_showing_tags():
            cutin = renpy.random.choice(["cutin_pen_1 ", "cutin_pen_2 ", "cutin_pen_3 "])
        else:
            
            cutin = "cutin_pen_2 "
        
        for i in ["sb_dpstand", "sb_onbed", "sb_onback", "sb_matingpress"]:
            
            if renpy.showing(i):
                cutin = "cutin_pen_1 "
        
        for i in ["sb_assup", "sb_onbelly", "sb_againstwall2", "sb_againstwall3", "sb_doggy1", "sb_doggy2", "sb_onfours", "sb_standbehind", "sb_table", "sb_lapsit", "sb_layblow", "gh_blow_close", "gh_blow_behind", "sb_standassup", "sb_pressed"]:
            
            if renpy.showing(i):
                cutin = "cutin_pen_2 "
        
        for i in ["sb_dpbed", "sb_ontop", "sb_cowgirl"]:
            
            if renpy.showing(i):
                cutin = "cutin_pen_3 "
                if i == "sb_ontop":
                    attr = renpy.get_attributes("sb_ontop")
                    if "doggy" in attr and (not "lay" in attr or not location == "vag"):
                        cutin = "cutin_pen_2 "
        return cutin

    def sex_pen_popup(location="vag"):
        cutin = get_sex_cutin(location)
        renpy.show_screen("sex_action_image", cutin, location, _layer="fg_screen")

    def sex_cum_popup(location="vag"):
        if location in ["face", "mouth", "ass"]:
            renpy.show_screen("nosex_cum_action_image", "cutin_" + location, _layer="fg_screen")
        else:
            cutin = get_sex_cutin(location)
            renpy.show_screen("sex_cum_action_image", cutin, location, _layer="fg_screen")

init -1:

    transform penetrate_pulse:

        alpha 1
        on show:
            easein 0.2 zoom 1.1
            easein 0.2 zoom 1
            pause 1.5
            easein 0.5 alpha 0

    transform cum_pulse:

        alpha 1
        zoom 0
        linear 0.1 zoom 1.1
        linear 0.6 zoom 1
        pause 0.5
        linear 0.1 zoom 1.1
        linear 0.6 zoom 1
        pause 0.5
        linear 0.1 zoom 1.1
        linear 0.6 zoom 1
        pause 1.5
        easein 0.5 alpha 0

    transform penetrate_impact:
        alpha 1
        on show:
            easein 0.7 alpha 0

    transform spank_fadeout:
        on show:
            alpha 1.0
            anchor (0.5,0.5)
            zoom 0
            parallel:
                easein 0.2 alpha 0
            parallel:
                easein 0.2 zoom 1.2
            parallel:
                easein 0.2 rotate 50

    transform punch_fadeout:
        on show:
            alpha 0.8
            anchor (0.5,0.5)
            parallel:
                easein 0.2 alpha 0
            parallel:
                easein 0.2 zoom 2
            parallel:
                easein 0.2 rotate 80

    transform punch_flash:
        on show:
            alpha 0.5
            parallel:
                easein 0.1 alpha 0

    transform cum_fadeout:

        on show:
            alpha 0.0


            linear 0.2 alpha 0.7
            linear 1.0 alpha 0.0

            linear 0.2 alpha 0.55
            linear 1.0 alpha 0.0

            linear 0.2 alpha 0.4
            linear 1.0 alpha 0.0

    transform penis_insert_fadeout:
        on show:
            alpha 0.0
            linear 0.2 alpha 0.5
            linear 1.2 alpha 0.0

screen spank_bum(xa, ya, zoomamount):
    zorder 6
    frame align (xa, ya) anchor (0.5,0.5) at spank_fadeout:
        background None
        add "spank":
            zoom zoomamount
    timer 0.2 action Hide('spank_bum')

screen punch(xa, ya):
    zorder 6
    frame align (xa,ya) anchor (0.5,0.5) at punch_fadeout:
        background None
        add "punch"
    frame at punch_flash:
        add "cum_image"
    timer 0.2 action Hide ('punch')

screen cum_action(type="none", var=1, show_cutin=True):
    zorder -1
    frame at cum_fadeout:
        background None
        if type == "pink":
            add "cum_image_pink"

        else:
            add "cum_image"


    if type == "pink" and show_cutin:
        frame at penetrate_pulse:
            background None
            add "cutin_orgasm" + str(var) at penetrate_pulse
    timer 5 action Hide('cum_action')






screen sex_action_flash(type="none"):
    zorder -1
    frame at penis_insert_fadeout:
        background None
        if type == "virgin":
            add "virgin_image"
        elif type in ("anal", "ass"):
            add "asssex_image"
        else:
            add "vagsex_image"
    timer 2 action Hide('sex_action_flash')

screen sex_action_image(cutin, location="vag"):
    zorder -2

    add cutin + str(location) at penetrate_pulse

    timer 4 action Hide('sex_action_image', _layer="fg_screen")


screen sex_cum_action_image(cutin, location="vag"):
    zorder -2
    add cutin + str(location) at cum_pulse

    timer 6 action Hide('sex_cum_action_image', _layer="fg_screen")

screen nosex_cum_action_image(cutin):
    zorder -2
    add cutin at cum_pulse

    timer 6 action Hide('nosex_cum_action_image', _layer="fg_screen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
