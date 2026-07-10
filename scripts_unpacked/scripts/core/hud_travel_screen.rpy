init python:








    def loc_button(but, desc, round, jumploc):
        if t.hour == 5 or t.hour == 20:
            timeof = "dawn"
        elif t.hour > 20 or t.hour < 5:
            timeof = "night"
        else:
            timeof = "day"
        if renpy.loadable("images/map_icons/locations/but_" + but + round + "_" + timeof + "_idle.webp"):
            renpy.ui.imagebutton(auto=("map_icons/locations/but_" + but + round + "_" + timeof + "_%s.webp"), action=[Hide ("text_hov2"), Jump (If(jumploc=="",but + "_arrival", jumploc))], hovered=Show("text_hov2", text=desc), unhovered=Hide("text_hov2"))
            return True
        else:
            renpy.ui.imagebutton(auto=("map_icons/locations/but_" + but + round + "_%s.webp"), action=[Hide ("text_hov2"), Jump (If(jumploc=="",but + "_arrival", jumploc))], hovered=Show("text_hov2", text=desc), unhovered=Hide("text_hov2"))
            return False

    def loc_button_frame(desc, jumploc, round=False):
        if round:
            suffix = "round"
        else:
            suffix = "square"
        renpy.ui.imagebutton(auto=("but_" + suffix + "_%s"),
        action=[Hide ("text_hov2"), Jump (jumploc)],
        hovered=Show("text_hov2", text=desc),
        unhovered=Hide("text_hov2"))


    def poi_button(but, desc, x,y, jumploc):
        renpy.ui.imagebutton(auto=("poi_" + but + "_%s"), action=[Hide ("text_hov"), Jump (jumploc)], pos=(x,y), hovered=Show("text_hov", text=desc, posi=(x,y)), unhovered=Hide("text_hov"))

    def poi_wardrobe(x,y):
        renpy.ui.imagebutton(auto=("poi_wardrobe_%s"), action=[Hide ("text_hov"), SetVariable("tab_left", "top"), Show("wardrobe_screen"), Hide("travel_screen")], pos=(x,y), hovered=Show("text_hov", text="Open your wardrobe", posi=(x,y)), unhovered=Hide("text_hov"))
    def poi_accessories(x,y):
        renpy.ui.imagebutton(auto=("poi_jewel_%s"), action=[Hide ("text_hov"), SetVariable("tab_left", "glasses"), Show("acc_screen"), Hide("travel_screen")], pos=(x,y), hovered=Show("text_hov", text="Open your jewellery box", posi=(x,y)), unhovered=Hide("text_hov"))

    def poi_mirror(x,y):
        renpy.ui.imagebutton(auto=("poi_wardrobe_%s"), action=[Hide ("text_hov"), Hide ("tab_left", "top"), Show("wardrobe_screen"), Hide("travel_screen")], pos=(x,y), hovered=Show("text_hov", text="Open your wardrobe", posi=(x,y)), unhovered=Hide("text_hov"))
    def poi_makeup(x,y):
        if acc.makeup_on == True:
            renpy.ui.imagebutton(auto=("poi_makeup_%s"), action=[Hide ("text_hov"), Jump ("makeup_apply")], pos=(x,y), hovered=Show("text_hov", text="Wash off makeup", posi=(x,y)), unhovered=Hide("text_hov"))
        else:
            renpy.ui.imagebutton(auto=("poi_makeup_%s"), action=[Hide ("text_hov"), Jump ("makeup_apply")], pos=(x,y), hovered=Show("text_hov", text="Apply makeup", posi=(x,y)), unhovered=Hide("text_hov"))
    def poi_cycle_hair(x,y):
        renpy.ui.imagebutton(auto=("poi_hairback_%s"), action=[Hide ("text_hov"), Function (hair_cycle)], pos=(x,y), hovered=Show("text_hov", text="Do hair", posi=(x,y)), unhovered=Hide("text_hov"))
    def poi_cycle_hair_front(x,y):
        renpy.ui.imagebutton(auto=("poi_comb_%s"), action=[Hide ("text_hov"), Function (hair_cycle_front)], pos=(x,y), hovered=Show("text_hov", text="Style fringe", posi=(x,y)), unhovered=Hide("text_hov"))
    def poi_screen_button_mirror_function(x,y):
        renpy.show_screen("travel_screen_button_mirror_expanded",x,y)
        renpy.hide_screen("travel_screen_button_mirror")

    def school_class_add_button(loc):
        if school_class_morning_active() and loc == "school_classroom":
            return True
        elif school_class_lunch_active() and loc == "school_cafe":
            return True
        elif school_class_gym_active() and loc == "school_gym":
            return True
        else:
            return False


screen text_hov(text, posi):

    frame anchor (0.37,1.0) pos (posi) xsize 350 at text_hov_fade:
        background None
        text "[text]" style "hover_font_style" size 25 xalign 0.5

screen text_hov2(text):
    zorder 3
    frame anchor (0, 1) xalign (0.23) yalign (0.85):
        background None
        text "[text]" style "hover_font_style" size 30

screen travel_screen_button_interior_lock(loc, jumploc, description, timeofday=False):
    if timeofday:
        $ timeimage = loc + "_day"
        $ timeimage1 = loc + "_" + t.timeofday
    else:
        $ timeimage = loc
        $ timeimage1 = loc
    frame padding (0,0) xysize (150,84) background None:
        if loc_to == loc:
            add "but_" + timeimage matrixcolor SaturationMatrix(0)
            add "but_locked"
            add "but_round_idle"
        else:
            add "but_" + timeimage1
            if school_class_add_button(loc):
                add "but_class"
            $ loc_button_frame(description, jumploc, True)

screen travel_screen_button_interior_locked(loc, jumploc, description, timeofday=False):
    if timeofday:
        $ timeimage = loc + "_day"
    else:
        $ timeimage = loc
    frame padding (0,0) xysize (150,84) background None:

        add "but_" + timeimage matrixcolor SaturationMatrix(0)
        add "but_locked"
        $ loc_button_frame(description, jumploc, True)

screen travel_screen_button_tint(loc, jumploc, description, is_round=False):
    frame padding (0,0) xysize (150,84) background None:
        add "but_" + loc matrixcolor TintMatrix(get_button_outside_colour())
        $ loc_button_frame(description, jumploc, is_round)

screen travel_screen_button_notime(loc, jumploc, description, is_round=False):
    frame padding (0,0) xysize (150,84) background None:
        add "but_" + loc
        $ loc_button_frame(description, jumploc, is_round)

screen travel_screen_button_time(loc, jumploc, description, is_round=False):
    frame padding (0,0) xysize (150,84) background None:
        add "but_" + loc + "_" + t.timeofday
        $ loc_button_frame(description, jumploc, is_round)


screen travel_screen_button_mirror(x, y):

    if mirror_var == False:
        imagebutton auto "poi_mirror_%s":
            action [Hide("text_hov"), SetVariable("mirror_var", loc_to)]
            pos (x,y)
            hovered Show("text_hov", text="Use mirror", posi=(x,y))
            unhovered Hide("text_hov")
    else:
        use travel_screen_button_mirror_expanded(x, y)

screen travel_screen_button_mirror_expanded(x, y):
    $ amount = 70
    $ poi_cycle_hair_front(x,y-amount)
    if not player.hair_neck == 1:
        $ poi_cycle_hair(x+amount,y)
    $ poi_makeup(x-amount,y)



screen travel_screen_a():

    zorder 0
    add "ui/bottom_travel_small.png" xanchor 0.0 yanchor 0.0 xalign 1.0 yalign 1.0

    hbox anchor (0.0,1.0) align (0.23,0.97):





        if loc_to in district_home:

            use travel_screen_button_notime("stairwell", "leave_house_checks", "Building stairwell", True)

            use travel_screen_button_interior_lock("hallway", "hallway_arrival", "Hallway")
            use travel_screen_button_interior_lock("bedroom", "bedroom_arrival", "My bedroom", True)
            use travel_screen_button_interior_lock("bathroom", "bathroom_arrival", "Bathroom")
            use travel_screen_button_interior_lock("kitchen", "kitchen_arrival", "Kitchen")
            use travel_screen_button_interior_lock("common", "common_arrival", "Livingroom", True)

        elif loc_to == "stairwell":
            use travel_screen_button_notime("hallway", "hallway_arrival", "Go home", True)
            if t.hour in night and late_final_warning == False:
                use travel_screen_button_time("residential_area", "stairwell_late", "Neighbourhood", True)
            else:
                use travel_screen_button_time("residential_area", "residential_area_arrival", "Neighbourhood", True)





        elif loc_to == "school_exterior":
            use travel_screen_button_time("lake_entrance", "lake_entrance_arrival", "Lake")
            use travel_screen_button_time("residential_area", "residential_area_arrival", "Neighbourhood")

            if school_open_hours():
                if not calander_holiday == "":
                    use travel_screen_button_interior_locked("school_hallway", "school_hallway_locked_holiday", "School hallways")

                else:
                    use travel_screen_button_notime("school_hallway", "school_hallway_arrival", "School hallway", True)









            else:
                if school_soccer_quest_backentrance["shown"]:
                    use travel_screen_button_interior_lock("school_field", "school_field_secret_entrance", "Secret entrance", True)
                else:
                    use travel_screen_button_interior_locked("school_hallway", "school_hallway_locked", "School hallways")


        elif loc_to in ("school_hallway", "school_gym", "school_field", "school_cafe", "school_toilet", "school_classroom", "school_darkroom"):

            use travel_screen_button_time("school_exterior", "school_exterior_arrival", "School entrance", True)

            if school_open_hours():
                use travel_screen_button_interior_lock("school_hallway", "school_hallway_arrival", "School hallways")
                use travel_screen_button_interior_lock("school_classroom", If(school_class_morning_active(),"school_class_picker","school_classroom_arrival"), If(school_class_morning_active(),"Attend class","School classroom"), True)
                use travel_screen_button_interior_lock("school_cafe", If(school_class_lunch_active(), "school_class_lunch","school_cafe_arrival"), "School cafeteria", True)
                use travel_screen_button_interior_lock("school_gym", If(school_class_gym_active(),"school_class_gym_picker","school_gym_arrival"), If(school_class_gym_active(),"Attend gym class","Gymnasium"))
                use travel_screen_button_interior_lock("school_field", "school_field_arrival", "School field", True)
                use travel_screen_button_interior_lock("school_locker", "school_locker_girl_arrival", "Girls locker room and pool")
                use travel_screen_button_interior_lock("school_toilet", "school_toilet_arrival", "Toilets")
                if school_photo_quest.active:
                    use travel_screen_button_interior_lock("school_darkroom", "school_photo_quest_picker", "Darkroom")
            else:
                use travel_screen_button_interior_lock("school_field", "school_field_arrival", "School field", True)
                use travel_screen_button_interior_lock("school_locker_old", "school_locker_old_arrival", "Abandoned locker room")


        elif loc_to == "school_field_back":
            use travel_screen_button_interior_lock("school_locker_old", "school_locker_old_arrival", "Abandoned locker room")
            use travel_screen_button_interior_lock("school_field", "school_field_arrival", "School field", True)

        elif loc_to == "school_pool":
            use travel_screen_button_interior_lock("school_locker", "school_locker_girl_arrival", "Girls locker room")

        elif loc_to == "school_toilet_boy" or loc_to == "school_toilet_girl":
            use travel_screen_button_interior_lock("school_toilet", "school_toilet_arrival", "Leave the toilets")


        elif loc_to == "school_locker_girl" or loc_to == "school_locker_boy":
            if school_open_hours():
                use travel_screen_button_interior_lock("school_gym", "leave_school_changingroom_checks_gym", "Gymnasium")
                use travel_screen_button_interior_lock("school_field", "leave_school_changingroom_checks_field", "School field", True)
                use travel_screen_button_interior_lock("school_pool", "leave_school_changingroom_checks_pool", "Swimming pool")
            else:
                use travel_screen_button_interior_lock("school_field", "leave_school_changingroom_checks_field", "School field", True)
        elif loc_to == "school_locker_old":
            use travel_screen_button_interior_lock("school_field", "leave_school_changingroom_checks_field", "School field", True)




        elif loc_to == "residential_area":
            use travel_screen_button_time("school_exterior", "school_exterior_arrival", "School entrance")
            use travel_screen_button_time("park_local", "park_local_arrival", "Park")
            if t.hour == 21:
                use travel_screen_button_notime("commercial_area_open", "commercial_area_arrival", "Shopping centre")
            else:
                use travel_screen_button_time("commercial_area", "commercial_area_arrival", "Shopping centre")
            use travel_screen_button_notime("stairwell", "stairwell_arrival", "Home stairwell", True)




        elif loc_to == "lake_entrance":
            use travel_screen_button_time("school_exterior", "school_exterior_arrival", "School entrance")
            use travel_screen_button_time("park_local", "park_local_arrival", "Park")




        elif loc_to == "commercial_area":
            use travel_screen_button_time("residential_area", "residential_area_arrival", "Neighbourhood")
            use travel_screen_button_time("revel", "revel_arrival", "Revel street")
            use travel_screen_button_time("highway_local", "highway_local_arrival", "Highway underpass")
            if t.hour >= 8 and t.hour <= 21:
                use travel_screen_button_notime("commercial_area_mall", "commercial_area_mall_arrival", "Mall", True)
            else:
                use travel_screen_button_interior_locked("commercial_area_mall", "commercial_area_mall_locked", "Mall")
            use travel_screen_button_time("park_local_market", "park_local_market_arrival", "Outdoor market", True)

        elif loc_to in ("commercial_area_mall", "park_local_market"):
            if t.hour == 21:
                use travel_screen_button_notime("commercial_area_open", "commercial_area_arrival", "Shopping centre")
            else:
                use travel_screen_button_time("commercial_area", "commercial_area_arrival", "Shopping centre")







        elif loc_to == "park_local":
            use travel_screen_button_time("lake_entrance", "lake_entrance_arrival", "Lake")
            use travel_screen_button_time("residential_area", "residential_area_arrival", "Neighbourhood")
            use travel_screen_button_time("revel", "revel_arrival", "Revel street")






        elif loc_to == "revel":
            use travel_screen_button_time("park_local", "park_local_arrival", "Park")
            if t.hour == 21:
                use travel_screen_button_notime("commercial_area_open", "commercial_area_arrival", "Shopping centre")
            else:
                use travel_screen_button_time("commercial_area", "commercial_area_arrival", "Shopping centre")
            use travel_screen_button_time("truckstop", "truckstop_arrival", "Truckstop")
            use travel_screen_button_time("hospital_exterior", "hospital_exterior_arrival", "Hospital", True)

            if t.hour in pub_open_hours:
                use travel_screen_button_notime("trainstation_local_pub", "trainstation_local_pub_arrival", "Cock and Goose Pub", True)
            else:
                use travel_screen_button_interior_locked("trainstation_local_pub", "trainstation_local_pub_closed", "Cock and Goose Pub")






        elif loc_to == "trainstation_local_pub":
            use travel_screen_button_time("revel", "revel_arrival", "Leave the pub", True)







        elif loc_to == "hospital_exterior":
            use travel_screen_button_time("revel", "revel_arrival", "Revel street", True)
            use travel_screen_button_notime("hospital_waiting", "hospital_waiting_arrival", "Hospital reception", True)

        elif loc_to == "hospital_waiting":
            use travel_screen_button_time("hospital_exterior", "hospital_exterior_arrival", "Hospital", True)





        elif loc_to == "highway_local":
            if t.hour == 21:
                use travel_screen_button_notime("commercial_area_open", "commercial_area_arrival", "Shopping centre")
            else:
                use travel_screen_button_time("commercial_area", "commercial_area_arrival", "Shopping centre")
            use travel_screen_button_time("truckstop", "truckstop_arrival", "Truckstop")
            use travel_screen_button_time("industrial_area", "industrial_area_arrival", "Factory area")





        elif loc_to == "truckstop":
            use travel_screen_button_time("revel", "revel_arrival", "Revel street")
            use travel_screen_button_time("highway_local", "highway_local_arrival", "Highway underpass")
            use travel_screen_button_time("checkpoint", "checkpoint_arrival", "Security checkpoint")





        elif loc_to == "checkpoint":
            use travel_screen_button_time("truckstop", "truckstop_arrival", "Truckstop")
            use travel_screen_button_time("industrial_area", "industrial_area_arrival", "Factory area")
            if unlocked_police:
                use travel_screen_button_notime("checkpoint_lobby", "checkpoint_lobby_arrival", "Enter the Police station")

        elif loc_to == "checkpoint_lobby":
            use travel_screen_button_time("checkpoint", "checkpoint_arrival", "Security checkpoint", True)





        elif loc_to == "industrial_area":
            use travel_screen_button_time("highway_local", "highway_local_arrival", "Highway underpass")
            use travel_screen_button_time("checkpoint", "checkpoint_arrival", "Security checkpoint")





        elif loc_to in district_minor_locations:
            use travel_screen_button_notime("return", loc_from + "_arrival", "Go back", True)




        elif loc_to in district_busstops:
            use travel_screen_button_notime("return", loc_from + "_arrival", "Leave the bus stop", True)

        if loc_to in district_busstop_location:
            $ loc_button("busstop", "Bus stop", "", "busstop")













        if loc_to == "haven_exterior":
            if main_quest_05.active == 1:
                if main_quest_05.missionvar18["exit_open"] == True:
                    use travel_screen_button_time("highway_local", "highway_local_arrival", "Highway underpass", True)
            else:
                use travel_screen_button_time("highway_local", "highway_local_arrival", "Highway underpass", True)

            if main_quest_05.active == 1:
                use travel_screen_button_notime("unknown", "haven_lobby_arrival", "Enter Haven", True)
            else:
                use travel_screen_button_tint("haven_lobby", "haven_lobby_arrival", "Enter Haven", True)



        elif loc_to == "haven_lobby":
            if main_quest_05.active == 1:
                if main_quest_05.missionvar18["exit_open"] == True:
                    use travel_screen_button_time("haven_exterior", "haven_ending_leave_intel", "Leave Haven", True)
            else:
                use travel_screen_button_time("haven_exterior", "haven_exterior_arrival", "Leave Haven", True)

            use travel_screen_button_tint("haven_hallway_1f", "haven_hallway_1f_arrival", "1st floor hallway", True)
            use travel_screen_button_tint("haven_landing", "haven_landing_arrival", "Stairs to the 2nd floor landing", True)

        elif loc_to == "haven_hallway_1f":

            use travel_screen_button_tint("haven_lobby", "haven_lobby_arrival", "Entrance area", True)

            if main_quest_05.missionvar1["bedroom"]:
                use travel_screen_button_tint("haven_bedroom", "haven_bedroom_arrival", "Sleeping area", True)
            else:
                use travel_screen_button_notime("unknown", "haven_bedroom_arrival", "?????", True)

            if main_quest_05.missionvar1["shower"]:
                use travel_screen_button_tint("haven_shower", "haven_shower_arrival", "Shower room", True)
            else:
                use travel_screen_button_notime("unknown", "haven_shower_arrival", "?????", True)

            if main_quest_05.missionvar1["room1"]:
                use travel_screen_button_tint("haven_room1", "haven_room1_arrival", "Dark and damp room", True)
            else:
                use travel_screen_button_notime("unknown", "haven_room1_arrival", "?????", True)

        elif loc_to == "haven_bedroom":
            use travel_screen_button_tint("haven_hallway_1f", "haven_hallway_1f_arrival", "1st floor hallway", True)
            use travel_screen_button_tint("haven_bed", "haven_bed_arrival", "Your sleeping corner", True)

        elif loc_to == "haven_bed":
            use travel_screen_button_tint("haven_bedroom", "haven_bedroom_arrival", "Sleeping area", True)

        elif loc_to == "haven_shower":

            use travel_screen_button_tint("haven_hallway_1f", "haven_hallway_1f_arrival", "1st floor hallway", True)

            if main_quest_05.missionvar2["shower_warning"]:
                use travel_screen_button_tint("haven_shower_stall", "haven_shower_stall_propt", "Head into the showers", True)
            elif main_quest_05.missionvar1["utilities"]:
                use travel_screen_button_tint("haven_utilities", "haven_shower_stall_arrival", "Maintenance room", True)
            else:
                use travel_screen_button_notime("unknown", "haven_shower_stall_arrival", "?????", True)

        elif loc_to == "haven_shower_stall":
            use travel_screen_button_tint("haven_shower", "haven_shower_dress", "Get dressed and leave", True)
            use travel_screen_button_tint("haven_utilities", "haven_utilities_arrival_checks", "Sneak into the maintenance room", True)

        elif loc_to == "haven_utilities":
            use travel_screen_button_tint("haven_shower_stall", "haven_shower_stall_arrival", "Shower stalls", True)



        elif loc_to == "haven_room1":
            use travel_screen_button_tint("haven_hallway_1f", "haven_hallway_1f_arrival", "1st floor hallway", True)

        elif loc_to == "haven_landing":
            use travel_screen_button_tint("haven_hallway_2f", "haven_hallway_2f_arrival", "Second floor hallway", True)
            use travel_screen_button_tint("haven_lobby", "haven_lobby_arrival", "Stairs to the 1st floor lobby", True)

        elif loc_to == "haven_hallway_2f":
            use travel_screen_button_tint("haven_landing", "haven_landing_arrival", "2nd floor landing", True)
            if main_quest_05.missionvar1["room2"]:
                use travel_screen_button_tint("haven_room2", "haven_room2_arrival", "Noisy room", True)
            else:
                use travel_screen_button_notime("unknown", "haven_room2_arrival", "?????", True)
            if main_quest_05.missionvar1["lounge"]:
                use travel_screen_button_time("haven_lounge", "haven_lounge_arrival", "Lounge", True)
            else:
                use travel_screen_button_notime("unknown", "haven_lounge_arrival", "?????", True)
            if main_quest_05.missionvar1["room3"]:
                use travel_screen_button_tint("haven_room3", "haven_room3_arrival", "Dangerous room", True)
            else:
                use travel_screen_button_notime("unknown", "haven_room3_arrival", "?????", True)


        elif loc_to in ("haven_room2", "haven_room3"):
            use travel_screen_button_tint("haven_hallway_2f", "haven_hallway_2f_arrival", "Second floor hallway", True)

        elif loc_to == "haven_lounge":
            use travel_screen_button_tint("haven_hallway_2f", "haven_hallway_2f_arrival", "Second floor hallway", True)
            if main_quest_05.missionvar1["storage"]:
                use travel_screen_button_notime("haven_storage", "haven_storage_arrival", "Storage room", True)
            else:
                use travel_screen_button_notime("unknown", "haven_storage_arrival", "?????", True)

        elif loc_to == "haven_storage":
            use travel_screen_button_time("haven_lounge", "haven_lounge_arrival", "Lounge", True)

        elif loc_to == "haven_cell":
            if main_quest_05.missionvar14["checked_done"]:
                use travel_screen_button_notime("unknown", "haven_sold_ending_check_door_rep", "Door", True)
            else:
                use travel_screen_button_notime("unknown", "haven_sold_ending_check_door", "Door", True)










    if loc_to == "bathroom":
        use travel_screen_button_mirror(1600, 276)



        $ poi_button("shower", "Have a shower", 1141, 456, "shower_event")
        if player.desire >= 80:
            $ poi_button("heart", "Have a \"warm\" shower", 1041, 456, "shower_masturbate")

    elif loc_to == "kitchen":
        $ poi_button("beer", "Have a beer", 1700, 500, "kitchen_beer")
        if player.hunger <= 30:
            $ poi_button("food", "Have something to eat", 950, 670, "kitchen_eat_alone")


    elif loc_to == "common":
        $ poi_button("tv", "Watch TV", 1580, 585, "common_tv")
        $ poi_button("run", "Exercise", 900, 660, "common_sport")

    elif loc_to == "bedroom":
        $ poi_wardrobe(1045,526)
        $ poi_accessories(1045,426)
        $ poi_button("sleep", "Go to sleep", 1605, 666, "bedroom_sleep")
        $ poi_button("relax", "Have a nap", 1505, 666, "bedroom_nap")
        if player.desire >= 80:
            $ poi_button("heart", "Masturbate", 1405, 666, "bedroom_masturbate")






    elif loc_to == "school_toilet":
        $ poi_button("door", "Boys toilet", 637, 524, "school_toilet_boy_arrival")
        $ poi_button("door", "Girls toilet", 1447, 524, "school_toilet_girl_arrival")

    elif loc_to == "school_toilet_girl":
        use travel_screen_button_mirror(850, 450)

    elif loc_to == "school_toilet_boy":

        use travel_screen_button_mirror(1020, 450)


    elif loc_to == "school_field":

        if school_soccer_playing():
            if not school_soccer_quest.active:
                $ poi_button("soccer", "Watch the boys play", 720,700, "school_field_soccer_picker")
            else:
                $ poi_button("soccer", "Play with the boys", 1075,700, "school_field_soccer_picker")
                $ poi_button("look", "Hang out with the boys", 1220,700, "school_field_soccer_watch")

        else:
            $ poi_button("run", "Go for a run", 1075,700, "school_field_run")

        if school_soccer_hangingout() and school_soccer_quest_hangout_prompt:
            $ poi_button("talk", "Talk to the boys", 1520,570, "school_field_back_arrival")

    elif loc_to== "school_field_back":
        if school_soccer_hangingout():
            $ poi_button("talk", "Talk to the boys", 1020,570-70, "school_field_soccer_hangout")
            if school_soccer_quest_betmatch["can_challenge"]:
                $ poi_button("soccer", "Play a dare match", 1020-70,570, "school_field_soccer_darematch_challenge")
            if school_soccer_cansex():
                $ poi_button("heart", "Offer myself", 1020+70,570, "school_field_soccer_sex_offer_picker")

    elif loc_to == "school_pool":
        $ poi_button("swim", "Swim laps", 565, 691, "school_pool_swim")

    elif loc_to == "school_gym":
        if school_dance_intro == True:
            if school_dance_trope_present() and school_dance_quest_on_team == True:
                $ poi_button("dance", "Dance with the troupe", 965, 691, "school_gym_dance_exercise_picker")
            elif school_dance_girls_present():
                $ poi_button("dance", "Dance with the girls", 965, 691, "school_gym_dance_exercise_picker")
            else:
                $ poi_button("dance", "Practice dance alone", 965, 691, "school_gym_dance_exercise_picker")

    elif loc_to in  ("school_locker_girl", "school_locker_boy", "school_locker_old"):
        if player.desire >= 80:
            $ poi_button("heart", "Have a \"warm\" shower", 1640, 563, "shower_masturbate")
        $ poi_button("shower", "Take a shower", 1540, 563, "shower_event")
        use travel_screen_button_mirror(1350, 563)
        $ poi_wardrobe(877, 473)











    elif loc_to == "commercial_area_mall":
        imagebutton auto "map_icons/poi/poi_map_%s.png":
            action [Show("mall_screen"), Hide("travel_screen"), Hide("text_hov")]
            pos (888,325)
            hovered Show("text_hov", text="Shop directory", posi=(888,325))
            unhovered Hide("text_hov")






    elif loc_to == "park_local":
        if explored_park == False:
            $ poi_button("walk", "Explore the park", 1182, 619, "park_local_walk_first")

        else:
            $ poi_button("walk", "Walk around the park", 1182, 619, "park_local_walk")
            $ poi_button("run", "Go for a run", 800, 585, "park_local_jog")

            if player.tired <= 20:
                $ poi_button("sleep", "Take a nap", 1719, 700, "park_local_nap")
            else:
                if weather_var in (1,2):
                    $ poi_button("relax", "Relax in the park", 1719, 700, "park_local_relax")






    elif loc_to == "park_local_market":
        if explored_market == False:
            $ poi_button("walk", "Explore the market", 840, 620, "park_local_market_explore")

        else:
            if t.hour in workhours and market_flyer.active == 0:
                $ poi_button("work", "Speak to [dan]", 840, 620, "park_local_market_flyer_intro")

            elif t.hour in market_flyer.starttime and t.wkday in market_flyer.workdays:
                $ poi_button("work", "Hand out flyers", 840, 620, "park_local_market_flyer")








    elif loc_to == "revel":


        if main_quest_02.stage == 2 and t.hour in (20,21,22,23):

            $ poi_button("question", "Apply chalk mark", 1682, 576, "main_quest_02_meet")





    elif loc_to == "trainstation_local_pub":
        if pub_waitress.active == 0:
            $ poi_button("work", "Ask for work", 1680, 580, "pub_waitress_picker")
        else:
            if t.hour in pub_waitress.starttime and t.wkday in pub_waitress.workdays:
                $ poi_button("work", "Start work", 1680, 580, "pub_waitress_picker")

        $ poi_button("beer", "Get a beer", 1580, 580, "pub_drink")

        if main_quest_01.stage == 1:

            $ poi_button("question", "Find the reporter", 1480, 580, "main_quest_01_reporter1")





    elif loc_to == "hospital_waiting":
        $ poi_button("question", "Speak to receptionist", 1719, 700, "hospital_waiting_reception")













    elif main_quest_05.active == 1:



        if loc_to == "haven_bed":
            if main_quest_05.stage == 3:
                $ poi_button("sleep", "Have a nap", 920, 600, "haven_bed_sleep")
                if haven_time_safe():
                    $ poi_button("listen", "Eavesdrop on the girls", 1650, 600, "haven_bed_listen_chainstart")


        elif loc_to == "haven_bedroom":


            if haven_show_sprinkler() and main_quest_05.missionvar11["sprinkler_bed"] == False:
                imagebutton auto "poi_firesprinkler_%s":
                    action [Hide("text_hov"), SetDict(main_quest_05.missionvar11, "sprinkler_bed", True), Jump ("haven_check_sprinklers")]
                    pos (1200, 150)
                    hovered Show("text_hov", text="Check sprinklers", posi=(1200, 150))
                    unhovered Hide("text_hov")

        elif loc_to == "haven_shower_stall":
            $ poi_button("listen", "Eavesdrop", 1719, 700, "haven_shower_stall_listen")

        elif loc_to == "haven_room1":
            if haven_can_set_fire():
                $ poi_button("fire", "Set a fire", 1719, 500, "haven_set_fire")
            if haven_show_sprinkler() and main_quest_05.missionvar11["sprinkler_room1"] == False:
                imagebutton auto "poi_firesprinkler_%s":
                    action [Hide("text_hov"), SetDict(main_quest_05.missionvar11, "sprinkler_room1", True), Jump ("haven_check_sprinklers")]
                    pos (1200, 150)
                    hovered Show("text_hov", text="Check sprinklers", posi=(1200, 150))
                    unhovered Hide("text_hov")

        elif loc_to == "haven_room2":
            if main_quest_05.stage == 3:
                $ poi_button("listen", "Eavesdrop", 1650, 600, "haven_room2_listen_chainstart")
            if haven_can_set_fire():
                $ poi_button("fire", "Set a fire", 1719, 500, "haven_set_fire")
            if haven_show_sprinkler() and main_quest_05.missionvar11["sprinkler_room2"] == False:
                imagebutton auto "poi_firesprinkler_%s":
                    action [Hide("text_hov"), SetDict(main_quest_05.missionvar11, "sprinkler_room2", True), Jump ("haven_check_sprinklers")]
                    pos (1200, 150)
                    hovered Show("text_hov", text="Check sprinklers", posi=(1200, 150))
                    unhovered Hide("text_hov")

        elif loc_to == "haven_room3":
            if havengateguard.inv.qty(item_haven_lighter) and  inv.qty(item_tool) and t.hour in main_quest_05.missionvar4["guard_hours"]:
                $ poi_button("look", "Wait for guard to smoke", 1719, 700, "haven_room3_wait")
            if haven_can_set_fire():
                $ poi_button("fire", "Set a fire", 1719, 500, "haven_set_fire")
            if haven_show_sprinkler() and main_quest_05.missionvar11["sprinkler_room3"] == False:
                imagebutton auto "poi_firesprinkler_%s":
                    action [Hide("text_hov"), SetDict(main_quest_05.missionvar11, "sprinkler_room3", True), Jump ("haven_check_sprinklers")]
                    pos (1200, 150)
                    hovered Show("text_hov", text="Check sprinklers", posi=(1200, 150))
                    unhovered Hide("text_hov")

        elif loc_to == "haven_lounge":
            if haven_can_set_fire():
                $ poi_button("fire", "Set a fire", 1719, 500, "haven_set_fire")
            if haven_show_sprinkler() and main_quest_05.missionvar11["sprinkler_lounge"] == False:
                imagebutton auto "poi_firesprinkler_%s":
                    action [Hide("text_hov"), SetDict(main_quest_05.missionvar11, "sprinkler_lounge", True), Jump ("haven_check_sprinklers")]
                    pos (1200, 150)
                    hovered Show("text_hov", text="Check sprinklers", posi=(1200, 150))
                    unhovered Hide("text_hov")

        elif loc_to == "haven_storage":
            if haven_can_set_fire():
                $ poi_button("fire", "Set a fire", 1719, 500, "haven_set_fire")

        elif loc_to == "haven_hallway_1f":
            if haven_show_sprinkler() and main_quest_05.missionvar11["sprinkler_1f"] == False:
                imagebutton auto "poi_firesprinkler_%s":
                    action [Hide("text_hov"), SetDict(main_quest_05.missionvar11, "sprinkler_1f", True), Jump ("haven_check_sprinklers")]
                    pos (1200, 150)
                    hovered Show("text_hov", text="Check sprinklers", posi=(1200, 150))
                    unhovered Hide("text_hov")

        elif loc_to == "haven_hallway_2f":
            if haven_show_sprinkler() and main_quest_05.missionvar11["sprinkler_2f"] == False:
                imagebutton auto "poi_firesprinkler_%s":
                    action [Hide("text_hov"), SetDict(main_quest_05.missionvar11, "sprinkler_2f", True), Jump ("haven_check_sprinklers")]
                    pos (1200, 150)
                    hovered Show("text_hov", text="Check sprinklers", posi=(1200, 150))
                    unhovered Hide("text_hov")





        elif loc_to == "haven_cell" and main_quest_05.missionvar14["checked_done"]:
            $ poi_button("relax", "Lay down", 1480, 780, "haven_sold_ending_bed_rep")
            $ poi_button("shower", "Shower", 540, 400, "haven_sold_ending_shower_rep")
            $ poi_button("look", "Look around", 1100, 400, "haven_sold_ending_look_rep")







    if loc_to in district_busstops:
        add "busstop_map" xalign 0.8 yalign 0.5

        if loc_to == "busstop_school_exterior":
            add "map_icons/markers/busstop_marker_here_idle.webp" pos (600, 350)
        else:
            imagebutton auto "map_icons/markers/busstop_marker_school_%s.webp":
                action [Hide("text_hov"), SetVariable ("bus_travel_loc", "school_exterior"), Jump ("busstop_bus_test")]
                pos (600, 350)
                hovered Show("text_hov", text="School", posi=(600, 350))
                unhovered Hide("text_hov")

        if loc_to == "busstop_residential_area":
            add "map_icons/markers/busstop_marker_here_idle.webp" pos (800, 350)
        else:
            imagebutton auto "map_icons/markers/busstop_marker_residential_%s.webp":
                action [Hide("text_hov"), SetVariable ("bus_travel_loc", "residential_area"), Jump ("busstop_bus_test")]
                pos (800, 350)
                hovered Show("text_hov", text="Home neighbourhood", posi=(800, 350))
                unhovered Hide("text_hov")

        if loc_to == "busstop_commercial_area":
            add "map_icons/markers/busstop_marker_here_idle.webp" pos (1000, 350)
        else:
            imagebutton auto "map_icons/markers/busstop_marker_commercial_%s.webp":
                action [Hide("text_hov"), SetVariable ("bus_travel_loc", "commercial_area"), Jump ("busstop_bus_test")]
                pos (1000, 350)
                hovered Show("text_hov", text="Shopping centre", posi=(1000, 350))
                unhovered Hide("text_hov")

        if loc_to == "busstop_highway_local":
            add "map_icons/markers/busstop_marker_here_idle.webp" pos (1200, 350)
        else:
            imagebutton auto "map_icons/markers/busstop_marker_highway_%s.webp":
                action [Hide("text_hov"), SetVariable ("bus_travel_loc", "highway_local"), Jump ("busstop_bus_test")]
                pos (1200, 350)
                hovered Show("text_hov", text="Highway", posi=(1200, 350))
                unhovered Hide("text_hov")

        if loc_to == "busstop_industrial_area":
            add "map_icons/markers/busstop_marker_here_idle.webp" pos (1400, 350)
        else:
            imagebutton auto "map_icons/markers/busstop_marker_industrial_%s.webp":
                action [Hide("text_hov"), SetVariable ("bus_travel_loc", "industrial_area"), Jump ("busstop_bus_test")]
                pos (1400, 350)
                hovered Show("text_hov", text="Factory area", posi=(1400, 350))
                unhovered Hide("text_hov")




        if loc_to == "busstop_lake_entrance":
            add "map_icons/markers/busstop_marker_here_idle.webp" pos (600, 565)
        else:
            imagebutton auto "map_icons/markers/busstop_marker_lake_%s.webp":
                action [Hide("text_hov"), SetVariable ("bus_travel_loc", "lake_entrance"), Jump ("busstop_bus_test")]
                pos (600, 565)
                hovered Show("text_hov", text="Lake", posi=(600, 565))
                unhovered Hide("text_hov")

        if loc_to == "busstop_park_local":
            add "map_icons/markers/busstop_marker_here_idle.webp" pos (800, 565)
        else:
            imagebutton auto "map_icons/markers/busstop_marker_park_%s.webp":
                action [Hide("text_hov"), SetVariable ("bus_travel_loc", "park_local"), Jump ("busstop_bus_test")]
                pos (800, 565)
                hovered Show("text_hov", text="Park", posi=(800, 565))
                unhovered Hide("text_hov")

        if loc_to == "busstop_revel":
            add "map_icons/markers/busstop_marker_here_idle.webp" pos (1000, 565)
        else:
            imagebutton auto "map_icons/markers/busstop_marker_revel_%s.webp":
                action [Hide("text_hov"), SetVariable ("bus_travel_loc", "revel"), Jump ("busstop_bus_test")]
                pos (1000, 565)
                hovered Show("text_hov", text="Revel street", posi=(1000, 565))
                unhovered Hide("text_hov")

        if loc_to == "busstop_truckstop":
            add "map_icons/markers/busstop_marker_here_idle.webp" pos (1200, 565)
        else:
            imagebutton auto "map_icons/markers/busstop_marker_truckstop_%s.webp":
                action [Hide("text_hov"), SetVariable ("bus_travel_loc", "truckstop"), Jump ("busstop_bus_test")]
                pos (1200, 565)
                hovered Show("text_hov", text="Highway truckstop", posi=(1200, 565))
                unhovered Hide("text_hov")

        if loc_to == "busstop_checkpoint":
            add "map_icons/markers/busstop_marker_here_idle.webp" pos (1400, 565)
        else:
            imagebutton auto "map_icons/markers/busstop_marker_checkpoint_%s.webp":
                action [Hide("text_hov"), SetVariable ("bus_travel_loc", "checkpoint"), Jump ("busstop_bus_test")]
                pos (1400, 565)
                hovered Show("text_hov", text="Highway checkpoint", posi=(1400, 565))
                unhovered Hide("text_hov")

    elif loc_to == "pink":
        $ poi_wardrobe(1045,526)
        $ poi_accessories(1045,426)
        $ poi_button("sleep", "Go to sleep", 1605, 666, "bedroom_sleep")
        $ poi_button("relax", "Have a nap", 1455, 666, "bedroom_nap")
        imagebutton auto "map_icons/poi/poi_map_%s.png" xalign 0.5 yalign 0.3 action Hide("travel_screen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
