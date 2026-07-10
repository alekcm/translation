






image cutin1_bg_layer:
    "cutin1_bg"
    matrixcolor OpacityMatrix(0.6)
image cutin_avatar_breasts = LayeredImageProxy("pc", Transform(crop=(0, 260, 500, 300), align = (0.4, 0.5), zoom = (3.0)))

image cutin_avatar_breasts_mask:
    AlphaMask("cutin_avatar_breasts", "cutin1_bg")

layeredimage cutin_gropeb_test:
    always "cutin1_bg_layer"
    always "cutin_avatar_breasts_mask" align (0.2, 0.0)
    always "cutin1_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
