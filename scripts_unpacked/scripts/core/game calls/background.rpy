init python:
    def background_scene():
        renpy.call("background")

label background:
    if t.hour == 5 or t.hour == 20:
        $ timeofday = "dawn"
    elif t.hour > 20 or t.hour < 5:
        $ timeofday = "night"
    else:
        $ timeofday = "day"

    if hide_background_screen == True:
        scene blank
    else:

        if loc_to == "commercial_area":
            if t.hour == 21:
                scene bg_commercial_area_night_open
            else:
                scene expression ("bg_" + loc_to + "_" + timeofday)

        elif loc_to == "trainstation_local_exterior" and t.hour > 20:
            scene bg_trainstation_local_exterior_night_open

        elif loc_to == "park_local_market" and t.hour == 20:
            scene bg_park_local_market_dawn_open

        elif loc_to == "school_hallway":
            if t.day == 6 or t.day == 7:
                if t.hour > 8 and t.hour < 14:
                    scene bg_school_hallway_2a
                else:
                    scene bg_school_hallway_3
            else:
                if t.hour == 8:
                    scene bg_school_hallway_2a
                elif t.hour > 8 and t.hour < 15:
                    scene bg_school_hallway_1
                elif t.hour >= 15 and t.hour < 19:
                    scene bg_school_hallway_2a
                else:
                    scene bg_school_hallway_3

        elif loc_to in district_busstops:
            scene expression ("bg_" + loc_to + "_" + timeofday)

            if t.hour == 7 or t.hour == 9:
                scene bg_busstop_people_busy
            elif t.hour == 8:
                scene bg_busstop_people_full
            elif t.hour > 9 and t.hour < 15:
                scene bg_busstop_people_some
            elif t.hour >= 15 and t.hour < 22:
                scene bg_busstop_people_empty




        elif loc_to in ("commercial_area_mall","stairwell","hallway","kitchen","bathroom","school_gym","school_toilet","school_toilet_boy","school_toilet_girl","school_pool","school_locker_boy","school_locker_girl","school_shower","hospital_waiting"):
            scene expression ("bg_" + loc_to)


        elif loc_to == "pink":
            scene pink
        else:
            scene expression ("bg_" + loc_to + "_" + timeofday)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
