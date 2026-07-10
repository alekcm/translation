define grope_self = "normal"

screen grope_self_screen(xp, yp):
    add "grope_self":

        at transform:
            align (xp, yp)
image grope_self_a = LayeredImageProxy("grope_self", Transform(align=(0.5, 0.2)))

layeredimage grope_self:

    always:
        "grope_self_bg"

    group actionscene:
        attribute test1:
            "grope_self_back_loop_test1"
        attribute test2:
            "grope_self_back_loop_test2"
        attribute slowa:
            "grope_self_back_loop_slow"
        attribute normal:
            "grope_self_back_loop_normal"
        attribute fast:
            "grope_self_back_loop_fast"






        attribute test1:
            "grope_self_front_loop_test1"
        attribute test2:
            "grope_self_front_loop_test2"
        attribute slowa:
            "grope_self_front_loop_slow"
        attribute normal:
            "grope_self_front_loop_normal"
        attribute fast:
            "grope_self_front_loop_fast"






    always:
        "grope_self_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
