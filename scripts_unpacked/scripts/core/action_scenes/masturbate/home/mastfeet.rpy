

image mastfeet_base_1 = im.MatrixColor(("action/masturbate/home/feet/mastfeet_base.webp"), im.matrix.tint(0.976, 0.827, 0.729))
image mastfeet_shad_1 = im.MatrixColor(("action/masturbate/home/feet/mastfeet_shad.webp"), im.matrix.tint(0.945, 0.682, 0.556))



image mastfeet_base_2 = im.MatrixColor(("action/masturbate/home/feet/mastfeet_base.webp"), im.matrix.tint(0.894, 0.709, 0.607))
image mastfeet_shad_2 = im.MatrixColor(("action/masturbate/home/feet/mastfeet_shad.webp"), im.matrix.tint(0.752, 0.525, 0.447))



image mastfeet_base_3 = im.MatrixColor(("action/masturbate/home/feet/mastfeet_base.webp"), im.matrix.tint(0.658, 0.427, 0.309))
image mastfeet_shad_3 = im.MatrixColor(("action/masturbate/home/feet/mastfeet_shad.webp"), im.matrix.tint(0.462, 0.235, 0.141))



image mastfeet_base_4 = im.MatrixColor(("action/masturbate/home/feet/mastfeet_base.webp"), im.matrix.tint(0.694, 0.505, 0.388))
image mastfeet_shad_4 = im.MatrixColor(("action/masturbate/home/feet/mastfeet_shad.webp"), im.matrix.tint(0.533, 0.329, 0.231))



image mastfeet_base_5 = im.MatrixColor(("action/masturbate/home/feet/mastfeet_base.webp"), im.matrix.tint(0.996, 0.901, 0.717))
image mastfeet_shad_5 = im.MatrixColor(("action/masturbate/home/feet/mastfeet_shad.webp"), im.matrix.tint(0.996, 0.729, 0.501))


image mastfeet_base_layer:
    "mastfeet_base_" + str(player.race)
image mastfeet_shad_layer:
    "mastfeet_shad_" + str(player.race)


image mastfeet_vag_1 = im.MatrixColor(("action/masturbate/home/feet/mastfeet_vag.webp"), im.matrix.tint(0.996, 0.6, 0.533))
image mastfeet_vag_2 = im.MatrixColor(("action/masturbate/home/feet/mastfeet_vag.webp"), im.matrix.tint(0.713, 0.454, 0.364))
image mastfeet_vag_3 = im.MatrixColor(("action/masturbate/home/feet/mastfeet_vag.webp"), im.matrix.tint(0.392, 0.207, 0.129))
image mastfeet_vag_4 = im.MatrixColor(("action/masturbate/home/feet/mastfeet_vag.webp"), im.matrix.tint(0.501, 0.266, 0.152))
image mastfeet_vag_5 = im.MatrixColor(("action/masturbate/home/feet/mastfeet_vag.webp"), im.matrix.tint(0.996, 0.6, 0.533))

image mastfeet_vag_layer:
    "mastfeet_vag_" + str(player.race)


image mastfeet_nails_black = im.MatrixColor(("action/masturbate/home/feet/mastfeet_nails.webp"), im.matrix.tint(0.25, 0.25, 0.3))
image mastfeet_nails_white = im.MatrixColor(("action/masturbate/home/feet/mastfeet_nails.webp"), im.matrix.tint(0.898, 0.949, 1))
image mastfeet_nails_blue = im.MatrixColor(("action/masturbate/home/feet/mastfeet_nails.webp"), im.matrix.tint(0.352, 0.529, 0.635))
image mastfeet_nails_brown = im.MatrixColor(("action/masturbate/home/feet/mastfeet_nails.webp"), im.matrix.tint(0.713, 0.619, 0.478))
image mastfeet_nails_green = im.MatrixColor(("action/masturbate/home/feet/mastfeet_nails.webp"), im.matrix.tint(0.286, 0.360, 0.125))
image mastfeet_nails_orange = im.MatrixColor(("action/masturbate/home/feet/mastfeet_nails.webp"), im.matrix.tint(0.968, 0.454, 0.101))
image mastfeet_nails_pink = im.MatrixColor(("action/masturbate/home/feet/mastfeet_nails.webp"), im.matrix.tint(1, 0.411, 0.705))
image mastfeet_nails_purple = im.MatrixColor(("action/masturbate/home/feet/mastfeet_nails.webp"), im.matrix.tint(0.392, 0.098, 0.615))
image mastfeet_nails_red = im.MatrixColor(("action/masturbate/home/feet/mastfeet_nails.webp"), im.matrix.tint(0.411, 0.180, 0.239))
image mastfeet_nails_sky = im.MatrixColor(("action/masturbate/home/feet/mastfeet_nails.webp"), im.matrix.tint(0.682, 0.811, 0.933))
image mastfeet_nails_yellow = im.MatrixColor(("action/masturbate/home/feet/mastfeet_nails.webp"), im.matrix.tint(0.929, 0.827, 0.207))
image mastfeet_nails_grey = im.MatrixColor(("action/masturbate/home/feet/mastfeet_nails.webp"), im.matrix.tint(0.474, 0.474, 0.505))
image mastfeet_nails_navy = im.MatrixColor(("action/masturbate/home/feet/mastfeet_nails.webp"), im.matrix.tint(0.129, 0.184, 0.250))
image mastfeet_nails_magenta = im.MatrixColor(("action/masturbate/home/feet/mastfeet_nails.webp"), im.matrix.tint(0.662, 0.168, 0.623))
image mastfeet_nails_lime = im.MatrixColor(("action/masturbate/home/feet/mastfeet_nails.webp"), im.matrix.tint(0.364, 0.662, 0.062))

image mastfeet_nails_layer:
    ("mastfeet_nails_" + str(acc.nails_primary_colour))



layeredimage mastfeet:

    always:
        "mastfeet_bg"

    always:
        "mastfeet_base_layer"
    always:
        "mastfeet_shad_layer"

    if acc.nails == 1:
        "mastfeet_nails_layer"
    always:
        "mastfeet_vag_layer"

    always:
        "mastfeet_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
