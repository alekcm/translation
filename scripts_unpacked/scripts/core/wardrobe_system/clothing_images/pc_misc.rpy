image pregband:
    "pc_misc_pregband_" + str(player.pregnancy)
    matrixcolor TintMatrix(clothing_colours["black"])


image mask_ballgag_lips_layered:
    "pc_mask_ballgag_lips"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
layeredimage pc_mask_ballgag_layer:
    always "mask_ballgag_lips_layered"
    always "pc_misc_ballgag"
layeredimage pc_mask_ballgag_red_layer:
    always "mask_ballgag_lips_layered"
    always "pc_misc_ballgag_red"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
