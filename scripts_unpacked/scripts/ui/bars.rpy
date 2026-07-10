style bar_style:
    right_bar "bar_empty.png"
    thumb "bar_thumb.png"
    thumb_offset 0
    xysize (300, 30)








screen bars:
    style_group "pref"
    frame xsize (430):
        has vbox spacing 6

        frame xysize (300, 60):
            style_group "pref"
            has hbox
            label _("MIND")

        frame:
            style_group "pref"
            has hbox
            bar value player.desire range 100
            label _("Desire")
        frame xysize (300, 60):
            style_group "pref"
            has hbox
            label _("Tiredness")
            bar value player.tired range 100
        frame xysize (300, 60):
            style_group "pref"
            has hbox
            label _("Willpower")
            bar value player.will range 100
        frame xysize (300, 60):
            style_group "pref"
            has hbox
            label _("Corruption")
            bar value player.corrupt range 100


        frame xysize (300, 60):
            style_group "pref"
            has hbox
            label _("BODY")

        frame xysize (300, 60):
            style_group "pref"
            has hbox
            label _("Fitness")
            bar value player.fitness range 100 xysize (300, 30)
        frame xysize (300, 60):
            style_group "pref"
            has hbox
            label _("Looks")
            bar value player.looks range 100 xysize (300, 30)
        frame xysize (300, 60):
            style_group "pref"
            has hbox
            label _("Health")
            bar value player.health range 100
        frame xysize (300, 60):
            style_group "pref"
            has hbox
            label _("Stamina")
            bar value player.stamina range 100
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
