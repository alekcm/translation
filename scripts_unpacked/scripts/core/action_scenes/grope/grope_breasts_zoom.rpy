init -1:
    transform grope_popup_breasts_1_transform:
        xpos 400 ypos 400
        on show:
            alpha 0
            linear 0.1 zoom 1.8 alpha 1.0
            linear 0.2 zoom 1.5
            pause 1.6
            linear 0.5 alpha 0.0
    transform grope_popup_breasts_2_transform:
        xpos 400 ypos 500
        on show:
            alpha 0
            linear 0.1 zoom 1.8 alpha 1.0
            linear 0.2 zoom 1.5
            pause 1.6
            linear 0.5 alpha 0.0
    transform grope_popup_hips_1_transform:
        xpos 400 ypos 700
        on show:
            alpha 0
            linear 0.1 zoom 1.8 alpha 1.0
            linear 0.2 zoom 1.5
            pause 1.6
            linear 0.5 alpha 0.0
    transform grope_popup_hips_2_transform:
        xpos 400 ypos 800
        on show:
            alpha 0
            linear 0.1 zoom 1.8 alpha 1.0
            linear 0.2 zoom 1.5
            pause 1.6
            linear 0.5 alpha 0.0




screen grope_popup_breasts_1():
    modal False
    zorder 1
    frame at grope_popup_breasts_1_transform:
        background None
        add "grope_popup_breasts_1_image"
    timer 2 action Hide ('grope_popup_breasts_1')

screen grope_popup_breasts_2():
    modal False
    zorder 1
    frame at grope_popup_breasts_2_transform:
        background None
        add "grope_popup_breasts_2_image"
    timer 2 action Hide ('grope_popup_breasts_2')

image grope_popup_breasts_crop = Crop((105, 315, 600, 150), "pc")

image grope_popup_breasts_1_image = LayeredImageProxy("grope_popup_breasts_1_layered", Transform(anchor=(0.05, 0.8)))
image grope_popup_breasts_2_image = LayeredImageProxy("grope_popup_breasts_2_layered", Transform(anchor=(0.05, 0.2)))

layeredimage grope_popup_breasts_1_layered:
    always "grope_popup_bg"
    always "grope_popup_breasts_crop" align (0.09, 0.02)
    always "grope_popup_frame_1"

layeredimage grope_popup_breasts_2_layered:
    always "grope_popup_bg"
    always "grope_popup_breasts_crop" align (0.09, 0.02)
    always "grope_popup_frame_2"





screen grope_popup_hips_1():
    modal False
    zorder 1
    frame at grope_popup_hips_1_transform:
        background None
        add "grope_popup_hips_1_image"
    timer 2 action Hide ('grope_popup_hips_1')

screen grope_popup_hips_2():
    modal False
    zorder 1
    frame at grope_popup_hips_2_transform:
        background None
        add "grope_popup_hips_2_image"
    timer 2 action Hide ('grope_popup_hips_2')

image grope_popup_hips_crop = Crop((80, 570, 600, 150), "pc")

image grope_popup_hips_1_image = LayeredImageProxy("grope_popup_hips_1_layered", Transform(anchor=(0.05, 0.8)))
image grope_popup_hips_2_image = LayeredImageProxy("grope_popup_hips_2_layered", Transform(anchor=(0.05, 0.2)))

layeredimage grope_popup_hips_1_layered:
    always "grope_popup_bg"
    always "grope_popup_hips_crop" align (0.09, 0.02)
    always "grope_popup_frame_1"

layeredimage grope_popup_hips_2_layered:
    always "grope_popup_bg"
    always "grope_popup_hips_crop" align (0.09, 0.02)
    always "grope_popup_frame_2"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
