image anabel_poledance_1 = LayeredImageProxy("anabel_poledance_1_layered", Transform(align=(0.8, 0.0)))

layeredimage anabel_poledance_1_layered:
    if dis(dis_partyhouse):
        "anabel_poledance_1_bg_party"
    else:
        "anabel_poledance_1_bg_party"
    always "anabel_poledance_1_base"
    if anabel.showing:
        "anabel_poledance_1_preg"
    if anabel.showing and not ("nude" in anabel.list or "dream" in anabel.list):
        "anabel_poledance_1_skirt_preg"
    elif not ("nude" in anabel.list or "dream" in anabel.list):
        "anabel_poledance_1_skirt"
    if not ("topless" in anabel.list or "dream" in anabel.list):
        "anabel_poledance_1_top"
    always "anabel_poledance_1_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
