image bg_truckstop_image:
    get_background_filename("truckstop")

layeredimage bg_truckstop_layered:
    always "bg_truckstop_image"

    if t.hour in (10,13,14,16,18,20,22):
        "bg_truckstop_people_manlean"
    if t.hour in (6,7,9,11,12,13,15,17,20,21):
        "bg_truckstop_people_mentalk"
    if (t.hour % 2) == 0:
        "bg_truckstop_people_manwalk"
    if t.hour in (15,16,17,19,20,21,23):
        "bg_truckstop_people_girlstalk"
    if t.hour in (15,16,17,18,21,23,0,1):
        "bg_truckstop_people_bgwhore"

    if kitty_here() and kitty.showing and not renpy.showing("kitty"):
        "bg_truckstop_people_kitty_preg"
    elif kitty_here() and not renpy.showing("kitty"):
        "bg_truckstop_people_kitty"

    if rose_here() and rose.showing and not renpy.showing("rose"):
        "bg_truckstop_people_rose_preg"
    elif rose_here() and not renpy.showing("rose"):
        "bg_truckstop_people_rose"

    if charity_here() and charity.showing and not renpy.showing("charity"):
        "bg_truckstop_people_charity_preg"
    elif charity_here() and not renpy.showing("charity"):
        "bg_truckstop_people_charity"

    if pursy_here() and pursy.showing and not renpy.showing("pursy"):
        "bg_truckstop_people_pursy_preg"
    elif pursy_here() and not renpy.showing("pursy"):
        "bg_truckstop_people_pursy"

    if cass_here() and cass.showing and cass.iswhore and (cass.noon_number % 2) and not renpy.showing("cass"):
        "bg_truckstop_people_cass_skirt_preg"
    elif cass_here() and cass.iswhore and (cass.noon_number % 2) and not renpy.showing("cass"):
        "bg_truckstop_people_cass_skirt"
    elif cass_here() and cass.showing and cass.iswhore and not renpy.showing("cass"):
        "bg_truckstop_people_cass_dress_preg"
    elif cass_here() and cass.iswhore and not renpy.showing("cass"):
        "bg_truckstop_people_cass_dress"

    if mira_here() and mira.showing and not renpy.showing("mira"):
        "bg_truckstop_people_mira_preg"
    elif mira_here() and not renpy.showing("mira"):
        "bg_truckstop_people_mira"

image bg_truckstop:
    "bg_truckstop_layered"
    bg_tint_transform()

image bg_motel_image:
    get_background_filename("motel", winter=False)

layeredimage bg_motel_layered:
    always "bg_motel_image"

    if t.timeofday == "day":
        "bg_motel_people_balcony"
    if t.hour in irange(12,22):
        "bg_motel_people_whore"
    if (t.hour % 2) == 0:
        "bg_motel_people_manloiter"

    if motel_recep_here() and motel_recep.showing and not renpy.showing("motel_recep"):
        "bg_motel_people_recep_preg"
    elif motel_recep_here() and not renpy.showing("motel_recep"):
        "bg_motel_people_recep"

    if kitty_here() and kitty.showing and not renpy.showing("kitty"):
        "bg_motel_people_kitty_preg"
    elif kitty_here() and not renpy.showing("kitty"):
        "bg_motel_people_kitty"

    if rose_here() and rose.showing and not renpy.showing("rose"):
        "bg_motel_people_rose_preg"
    elif rose_here() and not renpy.showing("rose"):
        "bg_motel_people_rose"

    if charity_here() and charity.showing and not renpy.showing("charity"):
        "bg_motel_people_charity_preg"
    elif charity_here() and not renpy.showing("charity"):
        "bg_motel_people_charity"

    if pursy_here() and pursy.showing and not renpy.showing("pursy"):
        "bg_motel_people_pursy_preg"
    elif pursy_here() and not renpy.showing("pursy"):
        "bg_motel_people_pursy"

    if cass_here() and cass.showing and cass.iswhore and (cass.noon_number % 2) and not renpy.showing("cass"):
        "bg_motel_people_cass_skirt_preg"
    elif cass_here() and cass.iswhore and (cass.noon_number % 2) and not renpy.showing("cass"):
        "bg_motel_people_cass_skirt"
    elif cass_here() and cass.showing and cass.iswhore and not renpy.showing("cass"):
        "bg_motel_people_cass_dress_preg"
    elif cass_here() and cass.iswhore and not renpy.showing("cass"):
        "bg_motel_people_cass_dress"

    if mira_here() and mira.showing and not renpy.showing("mira"):
        "bg_motel_people_mira_preg"
    elif mira_here() and not renpy.showing("mira"):
        "bg_motel_people_mira"

    if neighbour_here():
        "bg_motel_people_neigh"

image bg_motel:
    "bg_motel_layered"
    bg_tint_transform()


layeredimage bg_motel_lobby:
    always "bg_motel_lobby_image"
    if motel_recep_here() and not renpy.showing("motel_recep"):
        "bg_motel_lobby_people_recep"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
