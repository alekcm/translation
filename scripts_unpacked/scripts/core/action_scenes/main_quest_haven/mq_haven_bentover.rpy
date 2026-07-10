image haven_bentover_spank_layer:
    "haven_bentover_spank"
    opacity_transform(bruise.ass)

image haven_bentover_pc_writing_anal_layer:
    "haven_bentover_pc_writing_anal"
    writing_transform("ass")
image haven_bentover_pc_writing_whore_layer:
    "haven_bentover_pc_writing_whore"
    writing_transform("forehead")
image haven_bentover_pc_writing_slut_layer:
    "haven_bentover_pc_writing_slut"
    writing_transform("face")

layeredimage haven_bentover_manmast:
    always:
        "haven_bentover_man_larm"
    always:
        "haven_bentover_man_mast"

layeredimage haven_bentover_manpoke:
    always:
        "haven_bentover_man_rarm"
    always:
        "haven_bentover_man_larm"
    always:
        "haven_bentover_man_poke"

layeredimage haven_bentover_maninside:
    always:
        "haven_bentover_man_rarm"
    always:
        "haven_bentover_man_larm"
    always:
        "haven_bentover_man_inside"


layeredimage haven_bentover:

    always:
        "haven_bentover_base"
    always:
        "haven_bentover_spank_layer"
    if writing.ass:
        "haven_bentover_pc_writing_anal_layer"

    if player.cum_locations["cum_vagin"]:
        "haven_bentover_pc_cum_vag"
    if player.cum_locations["cum_vagout"]:
        "haven_bentover_pc_cum_ass"


    if c.top:
        "haven_bentover_pc_top"

    group face:
        attribute ah:
            "haven_bentover_pc_face_ah"
        attribute sad:
            "haven_bentover_pc_face_sad"
        attribute plead default:
            "haven_bentover_pc_face_plead"
        attribute sleep:
            "haven_bentover_pc_face_sleep"
        attribute neutral:
            "haven_bentover_pc_face_neutral"
        attribute happy:
            "haven_bentover_pc_face_happy"
        attribute smile:
            "haven_bentover_pc_face_smile"
        attribute frown:
            "haven_bentover_pc_face_frown"

    if player.beingraped:
        if_not "ah" "haven_bentover_pc_face_tear"
    if player.beingraped:
        if_any "ah" "haven_bentover_pc_face_tearah"

    if writing.forehead:
        "haven_bentover_pc_writing_whore_layer"
    if writing.face:
        "haven_bentover_pc_writing_slut_layer"
    always:
        "haven_bentover_pc_hair"

    if c.bottom:
        "haven_bentover_pc_shorts"

    group man:
        attribute nomanfull:
            null
        attribute noman default:
            "haven_bentover_man_larm"
        attribute mast:
            "haven_bentover_manmast"
        attribute poke:
            "haven_bentover_manpoke"
        attribute inside:
            "haven_bentover_maninside"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
