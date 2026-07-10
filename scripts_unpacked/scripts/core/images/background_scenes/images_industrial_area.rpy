image bg_industrial:
    get_background_filename("industrial_area")
    bg_tint_transform()

image bg_junk_entrance:
    get_background_filename("junk_entrance")
    bg_tint_transform()

image bg_junk_1:
    get_background_filename("junk_1")
    bg_tint_transform()

image bg_junk_2_scene:
    get_background_filename("junk_2")
    bg_tint_transform()
image bg_junk_2_jaylee_main_layer:
    "bg_junk_2_jaylee_0"
    bg_tint_transform()
image bg_junk_2_jaylee_1_layer:
    "bg_junk_2_jaylee_1"
    bg_tint_transform()
image bg_junk_2_jaylee_2_layer:
    "bg_junk_2_jaylee_2"
    bg_tint_transform()
layeredimage bg_junk_2_jaylee_layered:
    always "bg_junk_2_jaylee_main_layer"
    if jaylee.days_pregnant > (global_pregnancy_length * 0.75):
        "bg_junk_2_jaylee_2"
    elif jaylee.days_pregnant > (global_pregnancy_length * 0.3):
        "bg_junk_2_jaylee_1_layer"
layeredimage bg_junk_2:
    always "bg_junk_2_scene"
    if jaylee_here() and not renpy.showing("jaylee"):
        "bg_junk_2_jaylee_layered"

layeredimage bg_junk_trailer_jaylee_nude:
    if jaylee.days_pregnant > (global_pregnancy_length * 0.3):
        "bg_junk_trailer_jaylee_sit_nude_1"
    else:
        "bg_junk_trailer_jaylee_sit_nude_0"
layeredimage bg_junk_trailer_jaylee_dressed:
    if jaylee.days_pregnant > (global_pregnancy_length * 0.3):    
        "bg_junk_trailer_jaylee_sit_dressed_1"
    else:
        "bg_junk_trailer_jaylee_sit_dressed_0"
layeredimage bg_junk_trailer_jaylee:
    if t.hour in [22,8]:
        "bg_junk_trailer_jaylee_dressed"
    elif t.hour in [23,0,7]:
        "bg_junk_trailer_jaylee_nude"
    else:
        "bg_junk_trailer_jaylee_lay"
layeredimage bg_junk_trailer:
    always "bg_junk_trailer_scene"
    if jaylee_here() and not renpy.showing("jaylee"):
        "bg_junk_trailer_jaylee"

layeredimage bg_junk_trailer_bathroom_jaylee:
    if jaylee.days_pregnant > (global_pregnancy_length * 0.3):
        "bg_junk_trailer_bathroom_jaylee_wash_1"
    else:
        "bg_junk_trailer_bathroom_jaylee_wash_0"
layeredimage bg_junk_trailer_bathroom:
    always "bg_junk_trailer_bathroom_scene"
    if jaylee_here() and not renpy.showing("jaylee"):
        "bg_junk_trailer_bathroom_jaylee"

image bg_junk_office_scene:
    get_background_filename("junk_office")
    bg_tint_transform()
image bg_junk_office_ashon_layer:
    "bg_junk_office_ashon"
    bg_tint_transform()
layeredimage bg_junk_office:
    always "bg_junk_office_scene"
    if ashon_here() and not renpy.showing("ashon"):
        "bg_junk_office_ashon_layer"

image bg_walk_junk_rails:
    get_background_filename("junk_rails")
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
