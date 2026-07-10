image rachel_poledance_1 = LayeredImageProxy("rachel_poledance_1_layered", Transform(align=(0.8, 0.0)))

layeredimage rachel_poledance_1_layered:
    if dis(dis_partyhouse):
        "rachel_poledance_1_bg_party"
    else:
        "rachel_poledance_1_bg_party"
    always "rachel_poledance_1_base"
    if rachel.showing:
        "rachel_poledance_1_preg"
    if rachel.showing and not "nude" in rachel.list:
        "rachel_poledance_1_skirt_preg"
    elif not ("nude" in rachel.list or "dream" in rachel.list):
        "rachel_poledance_1_skirt"
    if not ("topless" in rachel.list or "dream" in rachel.list):
        "rachel_poledance_1_top"
    always "rachel_poledance_1_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
