image dani_poledance_1 = LayeredImageProxy("dani_poledance_1_layered", Transform(align=(0.8, 0.0)))

layeredimage dani_poledance_1_layered:
    if dis(dis_partyhouse):
        "dani_poledance_1_bg_party"
    else:
        "dani_poledance_1_bg_party"
    always "dani_poledance_1_base"
    if not ("nude" in dani.list or "dream" in dani.list):
        "dani_poledance_1_skirt"
    if not ("topless" in dani.list or "dream" in dani.list):
        "dani_poledance_1_top"
    always "dani_poledance_1_frame"

image dani_poledance_2 = LayeredImageProxy("dani_poledance_2_layered", Transform(align=(0.8, 0.0)))

layeredimage dani_poledance_2_layered:
    if dis(dis_partyhouse):
        "dani_poledance_2_bg_party"
    else:
        "dani_poledance_2_bg_party"
    always "dani_poledance_2_base"
    if dani.heavy_preg:
        "dani_poledance_2_preg_2"
    elif dani.showing:
        "dani_poledance_2_preg_1"
    if dani.heavy_preg and not ("nude" in dani.list or "dream" in dani.list):
        "dani_poledance_2_skirt_preg_2"
    elif dani.showing and not ("nude" in dani.list or "dream" in dani.list):
        "dani_poledance_2_skirt_preg_1"
    elif not ("nude" in dani.list or "dream" in dani.list):
        "dani_poledance_2_skirt"
    if not ("topless" in dani.list or "dream" in dani.list):
        "dani_poledance_2_top"
    always "dani_poledance_2_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
