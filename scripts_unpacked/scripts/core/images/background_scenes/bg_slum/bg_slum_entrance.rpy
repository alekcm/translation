layeredimage bg_highway_slum_people:
    if t.timeofday == "day":
        "bg_highway_slum_people_mansit"
    if t.hour in irange(12,22):
        "bg_highway_slum_people_girlstalk"
    if (t.hour % 2) == 0:
        "bg_highway_slum_people_trailergirl"
    if t.hour in irange(4,18):
        "bg_highway_slum_people_fishman"
    if t.hour in irange(9,20):
        "bg_highway_slum_people_bgman"
    if t.hour in irange(0,14):
        "bg_highway_slum_people_bggirl" 

    if kitty_here() and kitty.showing and not renpy.showing("kitty"):
        "bg_highway_slum_people_kitty_preg"
    elif kitty_here() and not renpy.showing("kitty"):
        "bg_highway_slum_people_kitty"

    if rose_here() and rose.showing and not renpy.showing("rose"):
        "bg_highway_slum_people_rose_preg"
    elif rose_here() and not renpy.showing("rose"):
        "bg_highway_slum_people_rose"

    if charity_here() and charity.showing and not renpy.showing("charity"):
        "bg_highway_slum_people_chas_preg"
    elif charity_here() and not renpy.showing("charity"):
        "bg_highway_slum_people_chas"

    if pursy_here() and pursy.showing and not renpy.showing("pursy"):
        "bg_highway_slum_people_pursy_preg"
    elif pursy_here() and not renpy.showing("pursy"):
        "bg_highway_slum_people_pursy"

    if cass_here() and cass.showing and cass.iswhore and (cass.noon_number % 2) and not renpy.showing("cass"):
        "bg_highway_slum_people_cass_skirt_preg"
    elif cass_here() and cass.iswhore and (cass.noon_number % 2) and not renpy.showing("cass"):
        "bg_highway_slum_people_cass_skirt"
    elif cass_here() and cass.showing and cass.iswhore and not renpy.showing("cass"):
        "bg_highway_slum_people_cass_dress_preg"
    elif cass_here() and cass.iswhore and not renpy.showing("cass"):
        "bg_highway_slum_people_cass_dress"

    if mira_here() and mira.showing and not renpy.showing("mira"):
        "bg_highway_slum_people_mira_preg"
    elif mira_here() and not renpy.showing("mira"):
        "bg_highway_slum_people_mira"

    if t.hour in irange(8,20) and not renpy.showing("haven_guard1"):
        "bg_highway_slum_people_guard_nice"
    elif not t.hour in irange(8,20) and not renpy.showing("haven_guard2"):
        "bg_highway_slum_people_guard_mean"

image bg_highway_slum_people_image:
    "bg_highway_slum_people"
    bg_tint_transform()

image bg_highway_slum_image:
    get_background_filename("highway_slum", True, False)
    bg_tint_transform()

layeredimage bg_highway_slum:
    always "bg_highway_slum_image"
    always "bg_highway_slum_people_image"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
