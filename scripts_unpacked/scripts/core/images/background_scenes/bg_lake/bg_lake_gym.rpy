layeredimage bg_beach_gym_people_layer:
    if kaan_here() and not renpy.showing("kaan"):
        "bg_beach_hangout_people_kaan"
    if mateo_here() and not renpy.showing("mateo"):
        "bg_beach_hangout_people_mateo"
    if mason_here() and not renpy.showing("mason") and npc_any_here(exclude=mason):
        "bg_beach_hangout_people_mason_play"
    elif mason_here() and not renpy.showing("mason"):
        "bg_beach_hangout_people_mason_wait"
    if sandy_here() and not renpy.showing("sandy") and people_nude_beach_vball_canplay():
        "bg_beach_hangout_people_sandy_play"
    if rachel_here() and not renpy.showing("rachel"):
        "bg_beach_hangout_people_rachel_base"
    if t.hour in (7,8,9,10,15,16,17) and people_beach():
        "bg_beach_hangout_people_workout"
    if people_beach_vball():
        "bg_beach_hangout_people_vball"

    if erika_here() and not renpy.showing("erika") and people_nude_beach_vball_canplay():
        "bg_beach_hangout_people_erika_nude"
    elif erika_here() and not renpy.showing("erika"):
        "bg_beach_hangout_people_erika"
    if zahra_here() and not renpy.showing("zahra") and people_nude_beach_vball_canplay():
        "bg_beach_hangout_people_zahra_play"
    elif zahra_here() and not renpy.showing("zahra"):
        "bg_beach_hangout_people_zahra"
    if robin_here() and not renpy.showing("robin") and people_nude_beach_vball_canplay():
        "bg_beach_hangout_people_robin_nude"
    elif robin_here() and not renpy.showing("robin"):
        "bg_beach_hangout_people_robin"

image bg_beach_gym_people_image:
    "bg_beach_gym_people_layer"
    bg_tint_transform()

layeredimage bg_beach_gym:
    always "bg_beach_gym_layer"

    always "bg_beach_gym_people_image"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
