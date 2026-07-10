layeredimage bg_pub:

    always:
        "bg_pub_scene"

    if robin_here() and (global_random_number % 2) and not renpy.showing("robin"):
        "bg_pub_people_robin_baggy"
    elif robin_here() and not renpy.showing("robin"):
        "bg_pub_people_robin_hoodie"
    if simon_here() and not renpy.showing("simon"):
        "bg_pub_people_simon"
    if t.hour in (20,21,22,23,0):
        "bg_pub_people_farstand"
    if loc_pub.open():
        "bg_pub_people_bar"
    if dani_here() and not renpy.showing("dani"):
        "bg_pub_people_dani"
    if t.hour in (18,19,20,21,22,23,0,1,2):
        "bg_pub_people_sitfar"
    if t.hour in (20,21,22,23,0):
        "bg_pub_people_standmid"
    if t.hour in (20,21,22,23,0):
        "bg_pub_people_standleft"
    if t.hour in (17,18,19,20,21,22,23,0,1,2):
        "bg_pub_people_sitthree"
    if t.hour in (19,20,21,22,23,0):
        "bg_pub_people_standvleft"
    if t.hour in (16,17,18,19,20,21,22,23,0,1,2):
        "bg_pub_people_sitclose"
    if loc_pub.open() and not renpy.showing("trixie"):
        "bg_pub_people_trixie"
    if bob_here():
        "bg_pub_people_bob"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
