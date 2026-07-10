default hide_peoplescreen = False















screen people_screen():

    zorder 1
    if t.hour == 5 or t.hour == 20:
        $ timeofday = "dawn"
    elif t.hour > 20 or t.hour < 5:
        $ timeofday = "night"
    else:
        $ timeofday = "day"


































    if main_quest_05.active == 1:
        if loc_to == "haven_lounge" and not (renpy.get_screen("say") or renpy.get_screen("choice") or _windows_hidden or renpy.get_screen("qlog")):
            if main_quest_05.missionvar6["found_toolbox"] == True and main_quest_05.missionvar6["took_stool"] == False and not haven_time_danger():
                imagebutton auto "bg_haven_lounge_stoolns_layer_%s" focus_mask True action Jump ("haven_storage_stool")
            if main_quest_05.missionvar6["took_fluid"] == False and haven_time_empty():
                imagebutton auto "bg_haven_lounge_fluid_%s" focus_mask True action Jump ("haven_lounge_fluid")

        if loc_to == "haven_room1" and not (renpy.get_screen("say") or renpy.get_screen("choice") or _windows_hidden or renpy.get_screen("qlog")):
            if t.timeofday == "night":
                imagebutton auto ("bg_haven_room1_peephole_light_layer_%s") focus_mask True action Jump ("haven_room1_peek")
            elif main_quest_05.missionvar6["found_peephole"] == True:
                imagebutton auto ("bg_haven_room1_peephole_layer_%s") focus_mask True action Jump ("haven_room1_peek")

        if loc_to == "haven_landing" and loc_haven_landing.dict["gate_open"] == False and not (renpy.get_screen("say") or renpy.get_screen("choice") or _windows_hidden or renpy.get_screen("qlog")):
            imagebutton auto ("bg_haven_landing_gatelocked_layer_%s") focus_mask True action Jump ("haven_landing_3f_arrival")

        if loc_to == "haven_utilities" and not (renpy.get_screen("say") or renpy.get_screen("choice") or _windows_hidden or renpy.get_screen("qlog")):
            if main_quest_05.missionvar11["firestart"] == False or (main_quest_05.missionvar11["firestart"] == True and main_quest_05.missionvar11["firecheck_done"] == True):
                for i in ("boiler", "bigpipe", "bluepipes", "cables", "ceilingpipe", "cutoff", "elebox", "fire", "gas", "redpipes", "trash", "vents"):
                    if not main_quest_05.missionvar10[i]:
                        imagebutton auto ("bg_haven_utilities_" + i + "_layer_%s") focus_mask True action Jump ("haven_utilities_" + i)


        if loc_to == "haven_storage" and not (renpy.get_screen("say") or renpy.get_screen("choice") or _windows_hidden or renpy.get_screen("qlog")):
            for i in ("beer1", "beer2", "boxclose", "cardboard1", "cardboard2", "crate1", "crate2", "debris", "ele", "shelf", "vent", "wood"):
                if main_quest_05.missionvar12[i] == False:
                    imagebutton auto ("bg_haven_storage_" + i + "_%s") focus_mask True action Jump ("haven_storage_" + i)

            if main_quest_05.missionvar12["vent_isopen"] == True and main_quest_05.missionvar12["vent_quest"] < 2:
                imagebutton auto ("bg_haven_storage_ventopen_%s") focus_mask True action Jump ("haven_storage_ventopen")
            if main_quest_05.missionvar6["took_toolbox"] == False:
                imagebutton auto ("bg_haven_storage_toolbox_%s") focus_mask True action Jump ("haven_storage_toolbox")


        if (loc_to == "haven_bedroom" and main_quest_05.missionvar13["bedroom_prompt"] == True and haven_time_empty()) and not (renpy.get_screen("say") or renpy.get_screen("choice") or _windows_hidden or renpy.get_screen("qlog")):
            for i in ("bedbag1", "bedbag2", "bedbag3", "bedbag4", "bedcorner", "beddoor", "bedfar", "bedright"):
                if main_quest_05.missionvar13[i] == False:
                    imagebutton auto ("bg_haven_bedroom_" + i + "_layer_%s") focus_mask True action Jump ("haven_bedroom_" + i)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
