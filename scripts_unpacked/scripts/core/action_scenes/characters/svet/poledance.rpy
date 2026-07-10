image svet_poledance_1 = LayeredImageProxy("svet_poledance_1_layered", Transform(align=(0.8, 0.0)))

layeredimage svet_poledance_1_layered:
    if dis(dis_partyhouse):
        "svet_poledance_1_bg_party"
    else:
        "svet_poledance_1_bg_party"
    always "svet_poledance_1_base"
    if svet.showing:
        "svet_poledance_1_preg"
    if svet.showing and not ("nude" in svet.list or "dream" in svet.list):
        "svet_poledance_1_skirt_preg"
    elif not ("nude" in svet.list or "dream" in svet.list):
        "svet_poledance_1_skirt"
    if not ("topless" in svet.list or "dream" in svet.list):
        "svet_poledance_1_top"
    always "svet_poledance_1_frame"

image svet_poledance_2 = LayeredImageProxy("svet_poledance_2_layered", Transform(align=(0.8, 0.0)))

layeredimage svet_poledance_2_layered:
    if dis(dis_partyhouse):
        "svet_poledance_2_bg_party"
    else:
        "svet_poledance_2_bg_party"
    always "svet_poledance_2_base"
    if svet.showing:
        "svet_poledance_2_preg"
    if svet.showing and not ("nude" in svet.list or "dream" in svet.list):
        "svet_poledance_2_skirt_preg"
    elif not ("nude" in svet.list or "dream" in svet.list):
        "svet_poledance_2_skirt"
    if not ("topless" in svet.list or "dream" in svet.list):
        "svet_poledance_2_top"
    always "svet_poledance_2_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
