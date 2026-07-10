init python:
    class District(object):
        def __init__(self, name, hub, danger, locs, npc_desc="", locked=False, map_enabled=True, sub_districts=[]):
            self._npc_desc = npc_desc 
            self.name = name
            self._hub = hub
            self._danger = danger
            self._locs = locs
            self.locked = locked
            self.map_enabled = map_enabled
            self.sub_districts = sub_districts
            self.parent_district = None
            self._whore_locations = []
            self.add_whore_locations()
            
            self.add_sub_district_locs()
            self.add_locations()
        
        @property
        def unlocked(self):
            return not self.locked
        
        @property
        def npc_desc(self):
            
            try:
                value = self._npc_desc
            except AttributeError:
                self._npc_desc = ""
            
            if self._npc_desc:
                return self._npc_desc
            else:
                return self.name
        
        
        @property
        def danger(self):
            danger = self._danger
            if t.timeofday == "night":
                danger = danger * 2
            elif t.timeofday == "dawn":
                danger = danger * 1.4
            
            if loc_cur.population == 0:
                danger = 0
            elif loc_cur.population == 2:
                danger = danger * 0.3
            return int(danger)
        
        @property
        def busstop(self):
            return globals()[self._hub[:4] + "busstop_" + self._hub[4:]]
        
        
        @property
        def hub(self):
            return globals()[self._hub]
        
        @property
        def whore_locations(self):
            loc_list = []
            for i in self._whore_locations:
                add_to_list(loc_list, globals()[i])
            return loc_list
        
        @property
        def locs(self):
            loc_list = []
            for i in self._locs:
                add_to_list(loc_list, globals()[i])
            return loc_list
        
        @property
        def locs_no_sub(self):
            loc_list = self.locs
            if self.sub_districts:
                for i in self.sub_districts:
                    for q in i.locs:
                        if q in loc_list:
                            remove_from_list(loc_list, q)
            return loc_list
        
        def add_locations(self):
            for i in self._locs:
                globals()[i].district = self
        
        def add_sub_district_locs(self):
            if self.sub_districts:
                for i in self.sub_districts:
                    for q in i._locs:
                        add_to_list(self._locs, q)
        
        def add_whore_locations(self):
            for i in self._locs:
                if globals()[i].can_whore:
                    add_to_list(self._whore_locations, i)

    class Location(object):
        def __init__(self, desc, name, outside=True, loc_type="conc", population=2, locked=False, isolate_loc="loc_alley", busstop="", force_outfit=[], forbid_outfit=["swim", "home"], forbid_exposed=True, mens_room=False, can_whore=False, can_loiter=False, can_eat=False, can_sleep=False, can_scavenge=True, can_gloryhole=False, drinking_location=False, home_location=False, opening_hours=[], block_actions=False, events=True):
            self.desc = desc 
            self.name = name 
            
            self.district = None 
            self.visited = False
            self.explored = False
            self.locked = locked 
            
            self.force_outfit = force_outfit 
            self.forbid_outfit = forbid_outfit 
            self.forbid_exposed = forbid_exposed 
            
            self.mens_room = mens_room 
            
            self.home_location = home_location
            self.drinking_location = drinking_location 
            self.man_amount = 0 
            self.outside = outside 
            self._population = population 
            self.opening_hours = opening_hours
            self.loc_type = loc_type 
            
            
            self._isolate_loc = isolate_loc 
            
            self.can_whore = can_whore
            self.can_loiter = can_loiter
            self.can_eat = can_eat
            self.can_sleep = can_sleep
            self.can_scavenge = can_scavenge
            self.can_gloryhole = can_gloryhole
            self.has_gloryhole = False 
            self.events = events
            self.block_actions = block_actions
            self.scav_last = -500 
            self.clean_last = -500 
            self.set_list()
            
            self.dict = {}
            self.list = []
        
        @property
        def unlocked(self):
            return not self.locked
        
        @property
        def population(self):
            if self.closed():
                return 0
            if t.timeofday == "night" and self._population == 2:
                return 1
            else:
                return self._population
        
        @property
        def scav_recent(self):
            if t.minutes_total - self.scav_last > 90:
                return False
            else:
                return True
        
        
        @property
        def bg_name(self):
            return self.name.replace("loc_", "", 1)
        
        @property
        def isolate_loc(self):
            return globals()[self._isolate_loc]  
        
        @property
        def inside(self):
            return not self.outside
        
        def set_list(self):
            global loc_list, loc_list_all
            add_to_list(loc_list, self.name)
            add_to_list(loc_list_all, self)
        
        def get_district(self):
            if self.district.sub_districts:
                for i in self.district.sub_districts:
                    for q in i.locs:
                        if self == q:
                            return i
            return self.district
        
        def closed(self):
            return not self.open()
        
        def open(self):
            if self.locked:
                return False
            elif self.opening_hours:
                if t.hour in self.opening_hours:
                    return True
                else:
                    return False
            else:
                return True
        @property
        def opening_hours_display(self):
            if not self.opening_hours:
                return "open all day"
            open = str(self.opening_hours[0])
            if open == "12":
                open = "noon"
            close = str(self.opening_hours[-1] + 1)
            if close == "24":
                close = "midnight"
            return "\"" + open + " - " + close + "\""
        
        def clean_recent(self, mins_since=240):
            if t.minutes_total - self.clean_last > mins_since:
                return False
            else:
                return True
        
        def man_degrade(self):
            
            if self.man_amount and not self == loc_cur:
                self.man_amount -= numgen(0,3)
                if self.man_amount < 0:
                    self.man_amount = 0

    def travel_bus():
        global dis_cur, dis_from
        relax(25)
        dis_from = dis_cur
        dis_cur = loc_want.district

    def travel_walk(location, time_amount=2, arrival=False, trans=True, loc_cur_block=False, outfit_block=False):
        global loc_cur, loc_from, loc_fromfrom, loc_want, dis_cur, dis_from, speaking_char
        refresh_avatar()
        loc_want = location 
        
        for i in irange(0,8): 
            renpy.hide_screen('notif_popup_' + str(i))
        
        if loc_cur == location: 
            return
        
        
        
        speaking_char = None
        if arrival:
            
            arrival_blocker(location) 
        
        if not outfit_block and not location == "":
            check_force_outfit(location)  
        
        tamount = float(time_amount)
        
        if not loc_cur == location:
            
            loc_fromfrom = loc_from
            loc_from = loc_cur
            loc_cur = location
        
        if not (loc_cur.district == dis_misc and dis_cur == location.district):
            if not (location.district == dis_bus_interior or location.district == dis_walk):
                dis_from = dis_cur
            dis_cur = loc_cur.district
            music_location_play()
        
        if location in dis_walk.locs and loc_from in dis_walk.locs and time_amount == 2:
            tamount = float(15)
        
        hunger = tamount / 10
        allure = tamount / 15 * player.allure / 80
        if player.pregnancy == 2:
            stotal = tamount / 15 * 1.5
            t.minute = int(tamount * 1.5)
        elif player.pregnancy == 3:
            stotal = tamount / 15 * 2
            t.minute = int(tamount * 2)
        else:
            stotal = tamount / 15
            t.minute = int(tamount)
        
        
        player.add_hygiene(hunger * 0.7)
        player.add_hunger(hunger)
        player.add_tired(-stotal)
        player.add_mood(-stotal)
        player.add_desire(allure)
        if player.hygiene <= 20:
            player.add_mood(-stotal)
        player.sex_hideaction()
        
        if location == loc_beach_water:
            
            player.shower()
        
        
        
        
        if arrival:
            renpy.jump("travel_arrival")
        if trans:
            if trans == True:
                renpy.with_statement(dissolve)
            else:
                renpy.with_statement(trans)
        refresh_avatar()


    def check_if_isolated(location=None):
        global loc_cur
        if location == None:
            location = loc_cur
        
        if location.district == dis_misc or location.population == 0:
            return True
        else:
            return False

    def travel_isolate(trans=True):
        if not check_if_isolated():
            travel_walk(loc_cur.isolate_loc, trans=trans)

    def travel_whore_location():
        if loc_cur.get_district().whore_locations:
            location = renpy.random.choice(loc_cur.get_district().whore_locations)
        elif dis_cur.whore_locations:
            location = renpy.random.choice(dis_cur.whore_locations)
        else:
            renpy.say(pc, "Event failed")
        travel_walk(location)

    def travel_loiter_location():
        if renpy.has_label(loc_cur.get_district().name + "_loiter_tombola"):
            renpy.jump(loc_cur.get_district().name + "_loiter_tombola")
        if renpy.has_label(dis_cur.name + "_loiter_tombola"):
            renpy.jump(dis_cur.name + "_loiter_tombola")
        
        
        
        if loc_cur.can_loiter:
            return
        if loc_cur in dis_misc.locs:
            travel_walk(loc_from)   
        
        loiter_list = []
        if dis_cur == loc_cur.get_district():
            for i in dis_cur.locs_no_sub: 
                if i.can_loiter and not (i.locked or i.closed()):  
                    add_to_list(loiter_list, i)
        else:
            for i in loc_cur.get_district().locs:
                if i.can_loiter and can_loiter(i):
                    add_to_list(loiter_list, i)
        
        if loiter_list:
            travel_walk(renpy.random.choice(loiter_list))
        elif cheats:
            renpy.say("", "DEBUG. Loiter list couldn't find anywhere to loiter, this shouldn't happen so needs fixing. This is a crash prevention override.") 

    def travel_sleep_location():
        if loc_cur in dis_misc.locs:
            return
        
        sleep_list = []
        if dis_cur == loc_cur.get_district():
            for i in dis_cur.locs_no_sub:
                if i.can_sleep:
                    add_to_list(sleep_list, i)
        else:
            for i in loc_cur.get_district().locs:
                if i.can_sleep:
                    add_to_list(sleep_list, i)
        if not sleep_list == []:
            location = renpy.random.choice(sleep_list)
            travel_walk(location)  

    def travel_dump_location():
        
        locations = [loc_highway, loc_junk_2, loc_park, loc_beach_rocks, loc_truckstop]
        for i in locations[:]:
            if (not i.visited or i.district.locked) or (i.force_outfit and not tab_top in i.force_outfit):
                locations.remove(i)
        if not locations:
            locations = [loc_truckstop]
            loc_truckstop.visited = True
        walk(renpy.random.choice(locations), trans=False)
        travel_isolate(trans=False)

    def travel_hangout_location():
        
        location = None
        if dis(dis_residential):
            location = loc_park_gazebo
        elif dis(dis_beach):
            location = loc_beach_pier
        elif dis(dis_lake):
            location = loc_pier
        elif dis(dis_school):
            location = loc_school_library
        elif dis(dis_truckstop):
            location = loc_truckstop_truck_1
        elif dis(dis_motel):
            location = loc_motel_room2
        
        if location== None or location.locked:
            travel_isolate()
        else:
            walk(location)

    def travel_toilet_girls(check=False):
        
        travel = False
        if dis(dis_home):
            travel = loc_bathroom
        elif loc_motel_room.open() and dis(dis_motel):
            travel = loc_motel_shower
        else:
            for i in dis_cur.locs:
                if "toilet_girls" in i.name and not "stall" in i.name and i.open():
                    travel = i
        if check:
            return travel 
        
        elif travel:
            
            walk(travel)

    def get_isolate_return_locs():
        if check_if_isolated(): 
            if not check_if_isolated(loc_from):
                return loc_from
            elif not check_if_isolated(loc_fromfrom):
                return loc_fromfrom
            elif not check_if_isolated(dis_cur.hub):
                return dis_cur.hub
            else:
                
                return dis_from.hub
        
        else:
            return loc_cur      








    def action_swap_actions_method():
        global action_act_var, action_mirror_var, action_wardrobe_var
        if action_act_var:
            action_act_var = False
        else:
            action_act_var = loc_cur
        
        action_mirror_var=False
        action_wardrobe_var=False

    def check_force_outfit(location):
        global tab_top
        if location.force_outfit:
            if not (re.sub('[0-9]', '', tab_top) in (location.force_outfit, "temp_outfit", "work") or pc_lost_clothes()): 
                renpy.jump("force_outfit_" + location.force_outfit)

    def location_closed():
        if loc_cur.opening_hours and not t.hour in loc_cur.opening_hours:
            if renpy.has_label(loc_cur.name + "_closed"):
                renpy.jump(loc_cur.name + "_closed")
            elif renpy.has_label(dis_cur.name + "_closed"):
                renpy.jump(dis_cur.name + "_closed")
            else:
                renpy.jump("location_generic_closed_eject")

    def school_class_add_button(loc):
        if school_class_morning_active() and loc == loc_school_classroom:
            return True
        elif school_class_lunch_active() and loc == loc_school_cafe:
            return True
        elif school_class_gym_active() and loc == loc_school_gym:
            return True
        else:
            return False

    def pc_actions_disabled():
        if block_action_bar_because_naked():
            return True
        elif log.interactive("mq_05_b"):
            
            return True
        elif log.interactive("quest_homeless_start_01") or log.interactive("quest_homeless_start_02"):
            
            return True
        elif loc_cur in (loc_haven_shower_stall, loc_haven_utilities, loc_haven_cell):
            return True
        elif not loc_cur.explored and renpy.has_label(loc_cur.name + "_explore"):
            return True
        elif block_action_bar_because_bitch():
            return True
        elif dis(dis_partyhouse) and school_dance_at_party():
            return True
        else:
            return False

    def loc(location=None, from_check=False):
        if location is None:
            return loc_cur.name
        
        if not isinstance(location, list):
            location = [location]
        
        for i in location:
            if loc_cur == i or (from_check and loc_from == i):
                return True
        
        return False

    def dis(location=None, from_check=False):
        if location is None:
            return dis_cur.name
        
        if not isinstance(location, list):
            location = [location]
        
        for i in location:
            if loc_cur in i.locs or (from_check and loc_from in i.locs):
                return True
        
        return False

    def can_loiter(location):
        if location.open() and location.visited and not location.locked:
            return True
        else:
            return False

    def get_opposite_gender_room(location=None):
        if not location:
            location = loc_cur
        name = location.name
        if "girls" in name:
            cur = "girls"
            opp= "boys"
        elif "boys" in name:
            cur = "boys"
            opp= "girls"
        else:
            return False
        name = name.replace(cur, opp)
        if name in globals():
            return globals()[name]
        return None

























    def get_people_images_can_show(who, location, location2=False):
        
        if who.has_met and not who.hate:
            
            if who._original_name.lower() + "_here" in globals():
                
                if (globals()[who._original_name.lower() + "_here"](location) or (location2 and globals()[who._original_name.lower() + "_here"](location2))):
                    
                    if not isinstance(globals()[who._original_name.lower() + "_here"](class_loc=True), District) or isinstance((location2 and globals()[who._original_name.lower() + "_here"](class_loc=True)), District):
                        
                        if renpy.loadable("images/ui/location_people/loc_badge_" + who._original_name.lower() + ".webp"):
                            
                            return True
        return False

    def get_people_images(location, location2=False):
        list_of_images = []
        
        for i in npc_unique:
            if get_people_images_can_show(i, location, location2):
                list_of_images.append("loc_badge_" + i._original_name.lower()) 
        
        
        
        
        
        
        
        if len(list_of_images) > 4:
            while len(list_of_images) > 3:
                list_of_images.pop()
            list_of_images.append("loc_badge_plus")
        return list_of_images

    def block_action_bar_because_naked():
        if c.inappropriate:
            
            
            if dis(dis_home):
                
                return False
            elif loc_cur.home_location:
                
                return False
            elif dis(dis_beach):
                
                return False
            elif dis(dis_haven):
                
                return False
            elif dis(dis_partyhouse):
                
                return False
            elif loc(loc_pink):
                
                return False
            elif any(substring for substring in ["toilet", "bathroom", "shower", "locker", "bedroom", "trailer", "changingroom", "bedroom"] if substring in loc_cur.name):
                
                return False
            elif player.has_perk(perk_whore) and dis(dis_truckstop):
                
                return False
            elif loc([loc_motel_pinkroom, loc_motel_room]):
                
                return False
            elif rachel_here(dis_school.locs) and rachel_exhib_stripping_show() and dis(dis_school) and not school_open_hours() and not loc([loc_school,loc_school_secret_entrance]):
                
                return False
            elif "exhibitionist_asked" in school_soccer_quest.conversation_topics and dis(dis_school) and loc_cur.outside and not loc(loc_school):
                
                return False
            elif school_soccer_dare_should_undress() and dis(dis_school) and loc_cur.outside and not loc([loc_school,loc_school_secret_entrance]):
                
                return False
            elif loc(loc_school_field_back): 
                return False
            elif "office_pi" in loc_cur.name:
                
                return False
            elif dis(dis_hospital) and not loc_cur.outside:
                
                return False
            
            
            else:
                return True
        return False

    def block_action_bar_because_bitch():
        if wolfgang_can_play() and quest_wolfgang.active:
            return True
        else:
            return False

    def block_bus_button():
        if dis(dis_partyhouse) and school_dance_at_party():
            return True

    def show_search_clothes_button():
        if loc_cur.home_location:
            return False
        elif dis(dis_home_area) and not loc_kitchen.locked:
            return False
        elif loc_cur.name.endswith("shower") or loc_cur.name.endswith("bathroom") or loc_cur.name.endswith("girls"):
            return False
        elif loc(loc_motel_pinkroom):
            return False
        elif c.exposed:
            return True
        else:
            return False

define action_mirror_var = False
define action_act_var = False
define action_wardrobe_var = False
define action_npc_var = False
define action_shower_var = False
define action_misc_var = False
define action_bed_var = False

image loc_button_idle:
    "loc_button_hover"
    matrixcolor TintMatrix("#b23f73")
image loc_button_left_idle:
    "loc_button_left_hover"
    matrixcolor TintMatrix("#b23f73")
image loc_button_right_idle:
    "loc_button_right_hover"
    matrixcolor TintMatrix("#b23f73")
image action_button_idle:
    "action_button_hover"
    matrixcolor TintMatrix("#b23f73")
image action_button_grey:
    "action_button_hover"
    matrixcolor TintMatrix("#777777")
image action_button_rect_idle:
    "action_button_rect_hover"
    matrixcolor TintMatrix("#b23f73")
image action_button_arrow_idle:
    "action_button_arrow_hover"
    matrixcolor TintMatrix("#b23f73")

screen travel_but_text(text, stat_image=False):
    frame anchor (0.0, 0.5) pos (555,928) xysize (500,50) at text_hov_fade:
        background None
        has hbox
        $ first = text[:1].upper()
        $ rest = text[1:].upper()
        text "[text]" style "hover_font_style" size 36 yalign 0.5



        if stat_image:
            frame xysize (10,1)
            if isinstance(stat_image, list):
                for i in stat_image:

                    add i yalign 0.5
                    frame xysize (10,1)
            else:
                add stat_image yalign 0.5

screen travel_button_people(location, location2=None):
    hbox:
        for icon in get_people_images(location, location2):
            add icon pos (-5,-10)


screen travel_button(location, jump_loc="", desc="", icon_image=None, locked=False, ignore_locked=False):
    if not location.locked or ignore_locked:
        if desc == "":
            $ desc = location.desc
        if (dis_cur == dis_haven and not location.visited) and not loc_cur in [loc_haven_cell]:
            $ desc = "Investigate"


        $ icon = location.name
        if icon_image:
            $ icon = icon_image

        elif renpy.loadable("images/ui/location/" + location.name + "_" + t.timeofday + ".webp"):
            $ icon = location.name + "_" + t.timeofday
        elif renpy.loadable("images/ui/location/" + location.name + ".webp"):
            $ icon = location.name
        else:
            $ icon = "loc_placeholder"




        if (location.closed() or locked) and not ignore_locked:
            frame padding (0,0) xysize (146,83) background None:

                add icon pos (3,2) matrixcolor SaturationMatrix(0)
                text desc size 22 font "BRLNSB.TTF" pos (5,5, 136, 73) color "#6b6b6b"
                add "but_locked" pos (3,2)

                $ jump_loc = "location_closed"
                if renpy.has_label(location.name + "_closed"):
                    $ jump_loc = location.name + "_closed"

                imagebutton auto "loc_button_%s":
                    action [Hide ("travel_but_text"), Jump(jump_loc)],



        else:
            frame padding (0,0) xysize (146,83) background None:

                if loc_cur == location:
                    add icon pos (3,2) matrixcolor SaturationMatrix(0)
                    add "but_locked" pos (3,2)
                    add "loc_button_idle"
                else:
                    if dis_cur == dis_haven and not location.visited:
                        add icon pos (3,2) matrixcolor SaturationMatrix(0)
                        add "but_question" pos (3,2)
                    else:
                        add icon pos (3,2)
                        if school_class_add_button(location):
                            add "but_class" pos (3,2)
                    text desc size 22 font "BRLNSB.TTF" pos (5,5, 136, 73) color "#dbdbdb"
                    imagebutton auto "loc_button_%s":
                        action [Hide ("travel_but_text"), If(jump_loc == "", Function(travel_walk, location, arrival=True), Jump(jump_loc))],


                use travel_button_people(location)

transform travel_button_split_test_rotate():
    anchor (0, 0) rotate -70
screen travel_button_split(location1, location2, jump_loc1="", jump_loc2="", desc1="", desc2=""):
    if not (location1.locked or loc_cur == location1):
        if "toilet" in location1.name:
            $ desc = "Toilets"
        elif "locker" in location1.name:
            $ desc = "Lockers"
        else:
            $ desc = ""
        $ icon = location2.name
        if renpy.loadable("images/ui/location/" + location2.name + "_" + t.timeofday + ".webp"):
            $ icon = location2.name + "_" + t.timeofday
        frame padding (0,0) xysize (146,83) background None:


            add icon pos (3,2)

            imagebutton auto "loc_button_left_%s":
                action [Hide ("travel_but_text"), If(jump_loc1 == "", Function(travel_walk, location1, arrival=True), Jump(jump_loc1))],


            imagebutton auto "loc_button_right_%s":
                align (1.0, 0.0)
                action [Hide ("travel_but_text"), If(jump_loc2 == "", Function(travel_walk, location2, arrival=True), Jump(jump_loc2))],


            text "Boys" size 22 font "BRLNSB.TTF" pos (5,15, 136, 73) color "#527ac1" at travel_button_split_test_rotate
            text "Girls" size 22 font "BRLNSB.TTF" pos (80,15, 136, 73) color "#c057b7" at travel_button_split_test_rotate

            use travel_button_people(location1)
            use travel_button_people(location2)





screen action_button(picture, desc, jump_loc, stat_image=False):
    frame padding (0,0) xysize (61,61) background None:
        add "action_" + picture anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "action_button_%s":
            action [Hide ("travel_but_text"), Jump(jump_loc)],
            hovered Show("travel_but_text", text=desc, stat_image=stat_image),
            unhovered Hide("travel_but_text")

screen action_button_explore():
    frame padding (0,0) xysize (61,61) background None:
        add "action_walk" anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "action_button_%s":
            action [Hide ("travel_but_text"),SetVariable("loc_cur.explored", True), Jump(loc_cur.name + "_explore")],
            hovered Show("travel_but_text", text="Explore the area"),
            unhovered Hide("travel_but_text")

screen action_button_wardrobe_quick():
    if not dis_cur in [dis_haven]:
        frame padding (0,0) xysize (61,61) background None:
            add "action_wardrobe" anchor (0.5,0.5) align (0.5,0.5)
            imagebutton auto "action_button_%s":
                action [Hide("travel_but_text"), SetVariable("action_wardrobe_var", If(action_wardrobe_var, False, loc_cur.name))]
                hovered Show("travel_but_text", text="Change outfit quickly")
                unhovered Hide("travel_but_text")
            if action_wardrobe_var:
                use action_button_wardrobe_quick_expanded()

screen action_button_wardrobe_quick_expanded():
    $ amount = 0
    for i in ["school", "daily", "party", "sport", "swim", "home"]:
        if not (tab_top == i or i in loc_cur.forbid_outfit):
            $ amount = amount - 65
            frame padding (0,0) xysize (61,61) pos (0, amount) background None:
                add "action_outfit_" + i anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_%s":
                    action [Hide ("travel_but_text"), Jump("clothes_quickchange_" + i)]
                    hovered Show("travel_but_text", text="Change into " + i + " outfit")
                    unhovered Hide("travel_but_text")

screen action_button_mirror():
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("mirror", If(acc.makeup_on, "Remove makeup", "Apply makeup"), "makeup_apply")
        if action_mirror_var:
            frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                $ amount_total += amount
                add "action_comb" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_%s":
                    action [Hide ("travel_but_text"), Function (hair_cycle_front), Function(refresh_avatar)]
                    hovered Show("travel_but_text", text="Style fringe")
                    unhovered Hide("travel_but_text")
            if not player.hair_neck == 1:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    add "action_hair" anchor (0.5,0.5) align (0.5,0.5)
                    imagebutton auto "action_button_%s":
                        action [Hide ("travel_but_text"), Function (hair_cycle), Function(refresh_avatar)]
                        hovered Show("travel_but_text", text="Do hair")
                        unhovered Hide("travel_but_text")
        else:
            use action_button_expand_arrow("action_mirror_var")

screen action_button_wardrobe():
    frame padding (0,0) xysize (61,61) background None:
        add "action_wardrobe" anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "action_button_%s":
            action [
                Hide ("travel_but_text"),   
                SetVariable("tab_left", If(c.outfit, "outfit", "top")), 
                
                Show("wardrobe_screen"), 
                Hide("travel_screen"),
                SetVariable("tab_top_enter", tab_top),
                Function(pc_remove_bad_clothes),
                If(tab_top in ["work", "temp"], Function(pc_set_outfit, If(t.timeofday == "day", "daily", "party"))),
                Function(set_wardrobe_colours), 
                Function(pc_dress)
                ],
            hovered Show("travel_but_text", text="Open my wardrobe"),
            unhovered Hide("travel_but_text")

screen action_button_loiter():
    $ amount_total = -65
    $ amount = -65
    default expand_button = False
    frame padding (0,0) xysize (61,61) background None:
        use action_button("wait", "Hang out", "loiter_jump")
        showif expand_button:
            if inv.qty(item_cigs):
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    add "action_smoke" anchor (0.5,0.5) align (0.5,0.5)
                    imagebutton auto "action_button_%s":
                        action [Hide ("travel_but_text"), SetVariable("item_inv_call", True), Jump("item_cigs_action")],
                        hovered Show("travel_but_text", text="Smoke a cig"),
                        unhovered Hide("travel_but_text")

            if inv.qty(item_beer) or inv.qty(item_brew):
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    add "action_beer" anchor (0.5,0.5) align (0.5,0.5)
                    imagebutton auto "action_button_%s":
                        action [Hide ("travel_but_text"), SetVariable("item_inv_call", True), SetVariable("item_inv_call", True), Jump(If(inv.qty(item_beer), "item_beer_action", "item_brew_action"))],
                        hovered Show("travel_but_text", text="Drink beer"),
                        unhovered Hide("travel_but_text")

            if inv.qty(item_joy):
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    add "action_joy" anchor (0.5,0.5) align (0.5,0.5)
                    imagebutton auto "action_button_%s":
                        action [Hide ("travel_but_text"), SetVariable("item_inv_call", True), SetVariable("item_inv_call", True), Jump("item_joy_action")],
                        hovered Show("travel_but_text", text="Eat a Joy"),
                        unhovered Hide("travel_but_text")

        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_passout():
    $ amount_total = -65
    $ amount = -65
    default expand_button = False
    frame padding (0,0) xysize (61,61) background None:
        use action_button("sleep", "Sleep somewhere", "action_sleep_jump")
        showif expand_button:
            if inv.qty(item_energydrink):
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    add "action_edrink" anchor (0.5,0.5) align (0.5,0.5)
                    imagebutton auto "action_button_%s":
                        action [Hide ("travel_but_text"), SetVariable("item_inv_call", True), Jump("item_energydrink_action")],
                        hovered Show("travel_but_text", text="Drink Energy drink"),
                        unhovered Hide("travel_but_text")

            if inv.qty(item_wakeup):
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    add "action_wakeup" anchor (0.5,0.5) align (0.5,0.5)
                    imagebutton auto "action_button_%s":
                        action [Hide ("travel_but_text"), SetVariable("item_inv_call", True), SetVariable("item_inv_call", True), Jump("item_wakeup_action")],
                        hovered Show("travel_but_text", text="take Wakeup"),
                        unhovered Hide("travel_but_text")

        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_scav():
    $ amount_total = -65
    $ amount = -65
    default expand_button = False
    frame padding (0,0) xysize (61,61) background None:
        if not loc_cur.scav_recent:
            use action_button("search", "Scavenge", "scav_jump")
        else:
            use action_button("search_wait", "Scavenge", "scav_jump")
        showif expand_button:
            if show_search_clothes_button():
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    add "action_search_clothes" anchor (0.5,0.5) align (0.5,0.5)
                    imagebutton auto "action_button_%s":
                        action [Hide ("travel_but_text"), Jump("scav_clothes_jump")],
                        hovered Show("travel_but_text", text="Search for clothes"),
                        unhovered Hide("travel_but_text")

        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_shower():
    $ amount_total = -65
    $ amount = -65
    default expand_button = False
    frame padding (0,0) xysize (61,61) background None:
        use action_button("shower", "Have a shower", "shower_event")
        showif expand_button:
            if player.desire >= 80:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("heart", "\"Warm\" shower", "shower_masturbate", stat_image=["mood_vhappy", "heart_1"])
            frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                $ amount_total += amount
                use action_button("makeup", "Auto makeup", "makeup_toggle_shower_event_set")

        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_bed():
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("sleep", "Go to sleep", "bed_sleep", stat_image="sleep_green")
        if action_bed_var:
            frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                $ amount_total += amount
                use action_button("relax", "Have a nap", "bed_nap", stat_image="sleep_green")
            if player.desire >= 80:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("heart", "Masturbate", "bedroom_masturbate", stat_image=["mood_vhappy", "heart_1"])
        else:
            use action_button_expand_arrow("action_bed_var")

screen action_button_pub_work():
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("work", "Start work", "pub_waitress_picker")
        if action_misc_var:
            frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                $ amount_total += amount
                use action_button("pants", If(pub_waitress.dict["wear_pants"], "Go commando", "Wear knickers"), "pub_waitress_work_pants_picker")
            frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                $ amount_total += amount
                use action_button("socks", If(pub_waitress.dict["wear_socks"], "Bare legs", "Wear socks"), "pub_waitress_work_socks_picker")
        else:
            use action_button_expand_arrow("action_misc_var")

screen action_button_soccer_back():
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("talk", "Talk to the boys", "school_field_soccer_hangout")
        if action_misc_var:
            if school_soccer_quest_betmatch["can_challenge"]:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("soccer", "Play a dare match", "school_field_soccer_darematch_challenge")
            if school_soccer_cansex():
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("heart", "Offer myself", "school_field_soccer_sex_offer_picker")
            frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                $ amount_total += amount
                use action_button("beer", If("stop_drinking" in loc_school_field_back.list, "Carry on drinking", "Stop drinking"), "school_field_soccer_drinking_toggle")

        else:
            use action_button_expand_arrow("action_misc_var")

screen action_button_whore():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        if player.has_perk(perk_freeuse):
            use action_button("heart", "Offer myself", "whore_street_start_setter")
        else:
            use action_button("whore", "Whore", "whore_street_start_setter")
        showif expand_button == True:
            frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                $ amount_total += amount
                use action_button("buy", If(player.has_perk(perk_freeuse), "Start charging", "Stop charging"), "whore_street_freeuse_toggle")
        showif expand_button == False:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action SetLocalVariable("expand_button", True)
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_pinkroom():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("whore", "Advertise myself", "pinkroom_advertise_start")
        showif expand_button:
            if "first_time" in loc_motel_pinkroom.list:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("heart", If(loc_motel_pinkroom.dict["sex_groups"], "Reject groups", "Accept groups"), "pinkroom_groups_picker")
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("heart", If(loc_motel_pinkroom.dict["sex_extreme"], "Reject extreme sex", "Accept extreme sex"), "pinkroom_extreme_picker")
                if "tied_train" in loc_motel_pinkroom.list and player.has_perk([perk_freeuse, perk_sucu, perk_broken]):
                    frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                        $ amount_total += amount
                        use action_button("train", "Freeuse train", "pinkroom_customer_event_freeuse_train_picker")

        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_expand_arrow(action_var):
    frame padding (0,0) xysize (61,25) pos (0,-20) background None:
        add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
            action [SetVariable(str(action_var), If(globals()[action_var], False, loc_cur.name))]
            hovered Show("travel_but_text", text="More actions")
            unhovered Hide("travel_but_text")

screen local_button_expand_arrow():
    frame padding (0,0) xysize (61,25) pos (0,-20) background None:
        add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
            action SetLocalVariable("expand_button", True)
            hovered Show("travel_but_text", text="More actions")
            unhovered Hide("travel_but_text")

screen action_button_shop(what_inv, desc):
    frame padding (0,0) xysize (61,61) background None:
        add "action_shop" anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "action_button_%s":
            action [
                Function (wardrobe_copy_tab, tab_top, "shop"),
                Function (tab_clothes, "shop"), 
                Hide("travel_screen"), 
                Show("wardrobe_screen", what_inv=what_inv, shop=True), 
                SetVariable("tab_top_enter", tab_top),
                Hide("travel_but_text"),
                ]
            hovered Show("travel_but_text", text=desc),
            unhovered Hide("travel_but_text")

screen action_button_item_shop(what_inv, desc):
    frame padding (0,0) xysize (61,61) background None:
        add "action_shop" anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "action_button_%s":
            action [
                Hide("travel_screen"), 
                Show("inventory_itemshop_screen", what_inv=what_inv), 
                Hide("travel_but_text"),
                ]
            hovered Show("travel_but_text", text=desc),
            unhovered Hide("travel_but_text")

screen travel_worldmap_but():
    frame padding (0,0) xysize (146,83) background None:
        if not loc_cur.district.map_enabled or block_bus_button():
            add "loc_bus_" + t.timeofday pos (3,2) matrixcolor SaturationMatrix(0)
            text "Bus stop" size 22 font "BRLNSB.TTF" pos (5,5, 136, 73) color "#6b6b6b"
            add "but_locked" pos (3,2)
            add "loc_button_idle"
        else:
            add "loc_bus_" + t.timeofday pos (3,2)
            if not loc_cur.district.hub.visited:
                add "but_question" pos (3,2)
            else:
                add "but_bus" pos (3,2)
            text "Bus stop" size 22 font "BRLNSB.TTF" pos (5,5, 136, 73) color "#dbdbdb"
            imagebutton auto "loc_button_%s":
                action [Hide("travel_but_text"), If(not loc_cur.district.hub.visited, Jump("map_screen_unknown_busstop"), Jump("map_screen"))],



screen action_swap_actions():
    frame padding (0,0) xysize (30,61) background None:
        add "action_swap"
        imagebutton auto "action_button_rect_%s":


            if action_act_var:
                action [Show ("travel_but_text", text="Swap to self actions"), Function (action_swap_actions_method)]
                hovered Show("travel_but_text", text="Swap to area actions")
            else:
                action [Show ("travel_but_text", text="Swap to area actions"), Function (action_swap_actions_method)]
                hovered Show("travel_but_text", text="Swap to self actions")
            unhovered Hide("travel_but_text")

screen action_button_perversions():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("lips", "Perversions", "action_perversion_picker_tombola")
        showif expand_button:

            if perversion_can_trigger_mast():
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("heart", "Masturbate", "action_mast_event_start")



            if perversion_can_trigger_flirt():
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("lips", "Flirt", "action_perversion_flirt_start")

            elif perversion_can_trigger_preg():
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("insem", "Get pregnant", "action_perversion_flirt_preg_start")


            if perversion_can_trigger_exhib():
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("streak", "Strip clothes", "action_strip_event_tombola")


            if perversion_can_trigger_train():
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("train", "Freeuse train", "action_perversion_freeusetrain_start")



            if perversion_can_trigger_bitch():
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("bitch", "Wear bitch collar", "action_perversion_wolfgang_wear_collar")

            elif acc.choker == 6 and quest_wolfgang.isactive():
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("nobitch", "Remove bitch collar", "action_perversion_wolfgang_remove_collar")


        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen travel_screen_pc_actions():
    if not pc_actions_disabled():
        use action_button_loiter()
        if player.tired < 15:
            use action_button_passout()



        if quest_scav.active:
            use action_button_scav()
        elif show_search_clothes_button():
            use action_button("search_clothes", "Search for clothes", "scav_clothes_jump")

        if perversion_can_trigger_any():
            use action_button_perversions()

        if quest_whore.active:
            if log.interactive("mira_missing_08") and not player.has_perk([perk_whore, perk_gamine]):
                use action_button("whore", "Pretend to whore", "whore_street_mira_quest_start_setter")
            else:
                use action_button_whore()
        if player.milky:
            use action_button("milk", "Milk myself", "item_breastpump_action_jump")

screen travel_screen_actions():


    if block_action_bar_because_bitch():
        use action_button("howl", "Howl", "wolfgang_action_howl")
        if tab_top == "temp_outfit":
            use action_button("search_clothes", "Dress up and leave", "wolfgang_action_dress_and_leave")

    elif block_action_bar_because_naked():
        use action_button("search_clothes", If(tab_top == "temp_outfit", "Dress up", "Search for clothes"), "scav_clothes_jump")

    else:
        if not loc_cur.explored and renpy.has_label(loc_cur.name + "_explore"):
            use action_button_explore()

        elif dis_cur == dis_residential:
            if loc_cur == loc_bedroom:
                use action_button_wardrobe()
                use action_button_bed()

            elif loc_cur == loc_bathroom:
                use action_button_mirror()
                use action_button_shower()

            elif loc_cur == loc_kitchen:
                if emile_here():
                    use action_button("talk", "Talk to " + emile.setname, "emile_tutorial_info")
                if player.hunger <= 40:
                    use action_button("eat", "Have something to eat", "kitchen_eat_alone", stat_image="mood_vhappy")

            elif loc_cur == loc_common:
                use action_button("tv", "Watch TV", "common_tv", stat_image="mood_vhappy")
                use action_button("run", "Exercise", "common_sport", stat_image="body_5")
                if emile_here():
                    use action_button("talk", "Talk to " + emile.setname, "emile_tutorial_info")




            elif loc(loc_stairwell):
                if log.interactive("quest_rent_b") and not loc_stairwell.clean_recent() and t.timeofday == "day" and not (loc_kitchen.locked or oskar.dead):

                    use action_button("clean", "Clean around the house", "action_clean_start")
                if loc_kitchen.locked and not "kickedout_window_entry" in robin.list:
                    use action_button("look", "Knock on window", "robin_talk_kickedout_window")
                if loc_office_ll.closed() and loc_kitchen.locked and not "pc_broke_in" in loc_office_ll.list:
                    use action_button("break", "Break into office", "oskar_office_breakin_action")

            elif loc(loc_bedroom_dani):
                if not dani.hate:
                    if loc_bedroom_dani.home_location:
                        use action_button_wardrobe()
                        use action_button_bed()
                        use action_button("wash", "Have a wash", "action_wash")

            elif loc(loc_office_ll):
                if not oskar_here() and (oskar.hate or oskar.rape) and oskar.sex > 5 and not oskar.dead and inv.qty(item_beer_poison) >= 4:
                    use action_button("skull", "Leave poison beer", "oskar_poison_event")

            elif loc_cur == loc_park:
                use action_button("run", "Go for a run", "action_exercise_run")
            elif loc_cur in [loc_park_toilet_boys, loc_park_toilet_girls]:
                use action_button_mirror()
                use action_button("wash", "Have a wash", "action_wash")

            elif loc_cur == loc_residential:
                use action_button("shop", "Corner shop", "loc_shop_corner_arrive")

                if cheats:
                    use action_button("shop", "Item debug shop", "item_debug_shop_label")

        elif dis_cur == dis_school:

            if loc(loc_school_hallway):
                if school_class_morning_active():
                    use action_button("study", "Attend class", "school_class_picker")
                if school_class_lunch_active():
                    use action_button("eat", "Have lunch", "school_class_lunch")
                if school_class_gym_active():
                    use action_button("outfit_sport", "Attend gym class", "school_class_gym_picker")

            elif loc(loc_school_classroom):
                if school_class_morning_active():
                    use action_button("study", "Attend class", "school_class_picker")

            elif loc_cur in [loc_school_toilet_boys, loc_school_toilet_girls]:
                use action_button_mirror()
                use action_button("wash", "Have a wash", "action_wash")

            elif loc_cur in [loc_school_locker_boys, loc_school_locker_girls, loc_school_locker_old]:
                use action_button_wardrobe()
                use action_button_mirror()
                use action_button_shower()

            elif loc_cur == loc_school_gym:
                if school_dance_intro:
                    if "show_stripping" in rachel.list and t.timeofday == "night":
                        use action_button("dance", If(rachel_here(loc_school_gym), "Dance with " + rachel.name.name, "Dance naked"), "school_gym_dance_nude_picker")
                    else:
                        use action_button("dance", If(school_dance_girls_present(), "Dance with the girls", "Practice dance alone"), "school_gym_dance_exercise_picker")
                if school_dance_event_active():
                    use action_button("dance", "Join girl's for event", "school_dance_show_ask")
                if school_class_gym_active():
                    use action_button("outfit_sport", "Attend gym class", "school_class_gym_picker")

            elif loc_cur == loc_school_pool:
                use action_button("swim", "Swim laps", "school_pool_swim")

            elif loc_cur == loc_school_cafe:
                if school_class_lunch_active():
                    use action_button("eat", "Have lunch", "school_class_lunch")
                elif player.hunger <= 40:
                    use action_button("eat", "Have a snack", "school_cafe_eat")

            elif loc_cur == loc_school_field:
                if school_soccer_playing():
                    if not school_soccer_quest.active:
                        use action_button("look", "Watch the boys play", "school_field_soccer_picker")
                    else:
                        use action_button("soccer", "Play with the boys", "school_field_soccer_picker")
                        use action_button("look", "Hang out with the boys", "school_field_soccer_watch")
                else:
                    use action_button("run", "Go for a run", "action_exercise_run")

            elif loc_cur == loc_school_field_back:
                if school_soccer_hangingout():
                    use action_button_soccer_back()
                    if "soccer_sex_robin" in robin.list and not robin_here(loc_school_field_back):
                        use action_button("look", "Spy on " + robin.setname, "school_field_soccer_sex_robin_spy")

            elif loc_cur == loc_school_sewroom:
                if saskia_frida_here():
                    if shop_needle.open:
                        use action_button("shop", "Buy clothes", "neddle_girls_shop")
                        use action_button("shop", "Sell junk", "neddle_girls_junk")
                    if all([saskia_here(), frida_here()]):
                        use action_button("talk", "Talk to the girls", "saskia_frida_talk_picker")
                    elif saskia_here():
                        use action_button("talk", "Talk to " + saskia.setname, "saskia_frida_talk_picker")
                    elif frida_here() and frida_here():
                        use action_button("talk", "Talk to " + frida.setname, "saskia_frida_talk_picker")
                    if log.interactive("quest_robinslut_01") and shop_needle.open:
                        use action_button("quest", "Look for clothes for " + str(robin.setname), "robin_talk_sexobject_neddle_buy")

            elif loc(loc_school_darkroom):
                if felix_here():
                    use action_button_npc_felix()

            elif loc(loc_school_library):
                use action_button("study", "Study", "school_library_study")
                use action_button("relax", "Relax", "loc_school_library_loiter")

        elif dis_cur == dis_lake:
            if loc_cur == loc_boardwalk:
                if t.hour in irange(8,20):
                    use action_button("shop", If(sandy.has_met, "Buy swimwear", "Check kiosks"), "boardwalk_bikini_kiosk")
                    if sandy.has_met:
                        use action_button("shop", "Seashell kiosk", "boardwalk_shell_kiosk")
                        use action_button("flyer", "Hand out flyers", "action_flyer_start")

            elif loc_cur == loc_pier:
                use action_button("relax", "Watch the waves", "loc_pier_relax")
                use action_button("run", "Jump off", "loc_pier_jetty_jump")

            elif loc_cur in [loc_beach_locker_girls, loc_beach_locker_boys]:
                use action_button_wardrobe()
                use action_button_mirror()
                use action_button_shower()

            elif loc(loc_beach_hangout):
                if not t.timeofday == "night" and weather_var <= 2:
                    use action_button("relax", "Relax in the sand", "loc_beach_relax")

            elif loc(loc_beach_fire):
                if people_beach_firepit():
                    use action_button("relax", "Hangout by the fire", "loc_fire_relax")

            elif loc_cur == loc_beach_gym:
                if t.hour in irange(9,18) and people_beach():
                    use action_button("vball", "Join volleyball", "action_exercise_vball")
                elif people_nude_beach_vball():
                    use action_button("vball", "Join nude volleyball", "action_exercise_vball")
                else:
                    use action_button("run", "Go for a run", "action_exercise_run")

            elif loc(loc_beach_rocks):
                if lake_dealer.has_met and lake_dealer_here():
                    use action_button_npc_lake_dealer()

        elif dis_cur == dis_revel:
            if loc_cur == loc_revel:
                if main_quest_02.stage == 2 and t.hour in (20,21,22,23):
                    use action_button("quest", "Apply chalk mark", "main_quest_02_meet")

            if loc(loc_revel_backstreet):
                if log.completed("Becoming the Fixer") and not "intro" in loc_office_pi.list and loc_revel_backstreet_stairwell.locked:
                    use action_button("look", "Investigte P.I. office", "loc_office_pi_discover")
                if log.interactive("mira_missing_07") and t.hour in (20,21,22,23):
                    use action_button("quest", "Look for " + cass.setname, "quest_mira_missing_cass_whore_clothes")
                if (log.interactive("quest_dancevip_01") or log.interactive("quest_dancevip_04")) and t.hour == 21 and t.wkday == "Saturday":
                    use action_button("quest", "Meet with the girls", "dance_party_start_picker")
                elif t.wkday == "Sunday" and t.hour < 6 and any([dani_here(), rachel_here(), svet_here(), anabel_here()]) and (log.interactive("quest_dancevip_03") or log.interactive("quest_dancevip_04")):
                    use action_button("talk", "Say goodnight", "dance_party_ending_goodbye")


            elif loc(loc_shop_funwear):
                use action_button("shop", "Funwear shop", "funwear_shop")
                if log.interactive("quest_flyers_01") and "funwear_start" in quest_flyers.list:
                    use action_button("flyer", "Hand out flyers", "action_flyer_start")
                if log.interactive("quest_robinslut_01"):
                    use action_button("quest", "Look for clothes for " + str(robin.setname), "robin_talk_sexobject_funwear_buy")

            elif loc(loc_shop_tattoo):
                use action_button("shop", "Speak to the beautician", "shop_tattoo_speak")

            elif loc(loc_office_pi_back):
                use action_button_wardrobe()
                use action_button_bed()
                use action_button("wash", "Have a wash", "action_wash")

            elif loc_cur == loc_mall:
                use action_button_shop(shop_test, "Test shop")

            elif loc_cur == loc_market:
                if t.hour in workhours:
                    use action_button("walk", "Wander round the stalls", "market_wander")
                if log.interactive("quest_flyers_01") and t.hour in workhours:
                    use action_button("flyer", "Hand out flyers", "action_flyer_start")
                if log.interactive("mq_05_prep_b") and not loc_market_stall_needle.visited and t.hour in workhours:
                    use action_button("quest", "Look for the clothing stall", "main_quest_05_market")

                if "sexobject_clothes_market_thoughts" in robin.list and log.interactive("quest_robinslut_01") and t.hour in workhours:
                    use action_button("quest", "Look for clothes for " + str(robin.setname), "robin_talk_sexobject_market_buy")


            elif loc(loc_market_stall_needle):
                if any([saskia_here(), frida_here()]):
                    use action_button("shop", "Buy clothes", "neddle_girls_shop")
                    use action_button("shop", "Sell junk", "neddle_girls_junk")
                    if all([saskia_here(), frida_here()]):
                        use action_button("talk", "Talk to the girls", "saskia_frida_talk_picker")
                    elif saskia_here():
                        use action_button("talk", "Talk to " + saskia.setname, "saskia_frida_talk_picker")
                    elif frida_here() and frida_here():
                        use action_button("talk", "Talk to " + frida.setname, "saskia_frida_talk_picker")
                if log.interactive("mq_05_prep_b"):
                    use action_button("quest", "Ask about package", "main_quest_05_market")

            elif loc(loc_market_stall_milk) and hucow_here():
                use action_button("shop", "Buy supplies", "market_stall_milkstand_shop")
                use action_button("shop", "Sell milk", "market_stall_milkstand_junk")
                if log.interactive("quest_flyers_01") and "milkmaid_start" in quest_flyers.list:
                    use action_button("flyer", "Hand out flyers", "action_flyer_start")

            elif loc_cur == loc_pub:
                if not pub_waitress.active:
                    use action_button("work", "Ask for work", "pub_waitress_picker")
                elif pub_waitress.can_work() and not pub_waitress.timesworked:
                    use action_button("work", "Start work", "pub_waitress_picker")
                use action_button("beer", "Hang out", "pub_drink_start", stat_image="badge_mood")

                if not pub_waitress.can_work() and pub_waitress.active and not loc_pub.clean_recent():
                    use action_button("clean", "Clean the pub", "action_clean_start")


                if log.interactive("mq_01_b"):

                    use action_button("quest", "Look for the reporter", "main_quest_01_reporter1")

            elif loc_cur in [loc_pub_toilet_girls, loc_pub_toilet_boys]:
                use action_button_mirror()
                use action_button("wash", "Have a wash", "action_wash")

            elif loc_cur == loc_pub_changingroom:
                use action_button_wardrobe()
                use action_button_mirror()
                use action_button("buy", "Buy uniform", "pub_waitress_shop")
                if pub_waitress.can_work() and pub_waitress.timesworked:
                    use action_button_pub_work()


            elif loc_cur == loc_hospital_lobby:
                use action_button("talk", "Speak to receptionist", "hospital_waiting_reception")



            elif dis(dis_partyhouse):
                if school_dance_at_party() and not t.hour == 4:
                    if loc(loc_party_stage):
                        use action_button("dance", "Solo dance", "dance_party_solo_dance")

                    if not quest_dancevip.dict["wine_amount"]:
                        use action_button("wine", "Refill wine", "dance_party_drink_topup")
                    else:
                        use action_button("wine", "Take a sip", "dance_party_drink_drink")

                if loc([loc_party_bedroom1, loc_party_bedroom2, loc_party_bedroom3, loc_party_bedroom4]):
                    use action_button_wardrobe()
                    use action_button_bed()

        elif dis_cur == dis_checkpoint:

            if loc_cur == loc_checkpoint_guardpost:
                use action_button("talk", "Chat with the guard", "loc_checkpoint_guardpost_chat")

            if loc_cur == loc_checkpoint_lobby:
                use action_button("talk", "Talk to " + paige.fullname, "checkpoint_lobby_reception_speak")

            elif loc_cur == loc_industrial:
                if log.interactive("mq_05_prep_a"):
                    use action_button("quest", "Look for the mechanics", "main_quest_05_mechanic")

            elif loc_cur == loc_mechanic:
                use action_button("talk", "Talk to " + ali.setname, "mechanic_ali_talk")

            elif loc_cur == loc_mechanic_office:
                use action_button("talk", "Talk to " + dez.setname, "mechanic_dez_talk")
                use action_button("shop", "Sell electronics", "mechanic_dez_sell")

            elif loc_cur == loc_junk_office:
                if ashon_here():
                    use action_button("shop", "Sell junk", "junkyard_ash_sell")
                    if "shop_open" in ashon.conversation_topics:
                        use action_button("shop", "Buy junk", "junkyard_ash_shop")
                    if log.interactive("mq_05_prep_c"):
                        use action_button("quest", "Pick up package", "main_quest_05_junkyard")

            elif loc_cur == loc_junk_trailer:
                use action_button_wardrobe()
                use action_button_bed()

            elif loc_cur == loc_junk_trailer_bathroom:
                use action_button_mirror()
                if not jaylee_here():
                    use action_button_shower()

        elif dis_cur == dis_truckstop:

            if loc(loc_motel):
                if quest_cleaner.active and "cleaner_unlocked" in loc_motel_lobby.list:
                    use action_button("clean", "Clean the motel", "action_clean_start")


            elif loc(loc_motel_lobby):
                use action_button("talk", "Speak to the receptionist", "motel_receptionist_talk")
                if shop_motel.open:
                    use action_button("buy", "Buy things", "motel_receptionist_talk_shop")
                if log.interactive("quest_flyers_01") and "motel_offer" in quest_flyers.list:
                    use action_button("flyer", "Hand out flyers", "action_flyer_start")

            elif loc(loc_motel_room):
                use action_button_wardrobe()
                use action_button_bed()

            elif loc(loc_motel_pinkroom):
                use action_button_pinkroom()
                use action_button_wardrobe()

            elif loc(loc_motel_shower):
                use action_button_mirror()
                use action_button_shower()

            elif loc(loc_highway_slum_still):
                use action_button("shop", "Buy booze", "slum_havenvik_shop")
                use action_button("shop", "Sell junk", "slum_havenvik_sell")

            elif loc(loc_highway_slum):
                if log.interactive("quest_homeless_01") or log.interactive("quest_homeless_start_02"):
                    use action_button("look", "Investigate house", "slum_home_find")

            elif loc(loc_highway_slum_home):
                use action_button_wardrobe()
                use action_button_bed()
                use action_button_mirror()
                use action_button_shower()

            if loc([loc_truckstop, loc_highway, loc_motel]):
                if not quest_whore.active and (player.has_perk([perk_gamine, perk_whore, perk_sucu, perk_broken]) or not loc_highway_slum_home.locked) and not t.timeofday == "day":
                    use action_button("look", "Look at the whores", "action_whore_discover_first")

        elif dis_cur == dis_haven and log.completed("mq_05_b"):

            if loc_cur == loc_haven_bedroom:
                if log.interactive("mq_05_sprinklers") and not "checked_sprinkler" in loc_cur.list:
                    use action_button("sprinkler", "Check sprinklers", "haven_check_sprinklers")
                if haven_time_empty():
                    use action_button("search", "Search beds", "loc_haven_bedroom_scavenge")

            elif loc_cur == loc_haven_bed:
                use action_button("sleep", "Have a nap", "haven_bed_sleep")
                if haven_time_safe():
                    use action_button("listen", "Eavesdrop on the girls", "haven_bed_listen_chainstart")

            elif loc_cur == loc_haven_shower:
                use action_button("shower", "Head into the showers", "haven_shower_stall_arrival")

            elif loc_cur == loc_haven_shower_stall:
                use action_button("listen", "Eavesdrop", "haven_shower_stall_listen")

            elif loc_cur == loc_haven_utilities:
                if not (log.interactive("mq_05_pipesbreak") or  log.interactive("mq_05_sprinklers")):
                    use action_button("look", "Investigate area", "haven_utilities_investigate_picker")
                if log.interactive("mq_05_pipesbreak"):
                    use action_button("break", "Pry the pipes", "haven_utilities_pipes_break")

            elif loc_cur == loc_haven_room1:
                if haven_can_set_fire():
                    use action_button("fire", "Set a fire", "haven_set_fire")
                if log.interactive("mq_05_sprinklers") and not "checked_sprinkler" in loc_cur.list:
                    use action_button("sprinkler", "Check sprinklers", "haven_check_sprinklers")
                if "found_peephole" in loc_haven_room1.list:
                    use action_button("look", "Check peephole", "haven_room1_peek")
                elif t.hour in dark:
                    use action_button("question", "Investigate light", "haven_room1_peek")

            elif loc_cur == loc_haven_landing:
                if haven_guard_smoking() and inv.qty(item_haven_crowbar):
                    use action_button("break", "Pry the gate", "haven_landing_3f_pry")
                else:
                    use action_button("talk", "Talk to the guard", "haven_landing_3f_arrival")

            elif loc_cur == loc_haven_room2:
                use action_button("listen", "Eavesdrop", "haven_room2_listen_chainstart")
                if log.interactive("mq_05_sprinklers") and not "checked_sprinkler" in loc_cur.list:
                    use action_button("sprinkler", "Check sprinklers", "haven_check_sprinklers")
                if haven_can_set_fire():
                    use action_button("fire", "Set a fire", "haven_set_fire")

            elif loc_cur == loc_haven_room3:
                if havengateguard.inv.qty(item_haven_lighter) and inv.qty(item_haven_crowbar) and haven_guard_hours():
                    use action_button("look", "Wait for guard to smoke", "haven_room3_wait")
                if haven_can_set_fire():
                    use action_button("fire", "Set a fire", "haven_set_fire")
                if log.interactive("mq_05_sprinklers") and not "checked_sprinkler" in loc_cur.list:
                    use action_button("sprinkler", "Check sprinklers", "haven_check_sprinklers")

            elif loc_cur == loc_haven_lounge:
                if t.timeofday == "night":
                    use action_button("relax", "Hang out by the fire", "haven_lounge_fire_hangout")
                if haven_can_set_fire():
                    use action_button("fire", "Set a fire", "haven_set_fire")
                if log.interactive("mq_05_sprinklers") and not "checked_sprinkler" in loc_cur.list:
                    use action_button("sprinkler", "Check sprinklers", "haven_check_sprinklers")
                if "searched_toolbox" in loc_haven_storage.list and not "took_toolbox" in loc_haven_storage.list:
                    use action_button("look", "Look for something to stand on", "haven_storage_stool")

            elif loc_cur == loc_haven_storage:
                if not loc_haven_storage.explored:
                    use action_button("look", "Look around", "haven_storage_investigate")
                elif not "searched_all" in loc_haven_storage.list:
                    use action_button("search", "Scavenge", "scav_jump")
                if "searched_toolbox" in loc_haven_storage.list and not "took_toolbox" in loc_haven_storage.list:
                    use action_button("look", "Investigate toolbox", "haven_storage_toolbox")
                if "searched_vent" in loc_haven_storage.list and inv.qty(item_haven_crowbar) and not "vent_climbedin" in loc_haven_storage.list:
                    use action_button("look", "Investigate vent", "haven_storage_vent_picker")
                if log.interactive("mq_05_sprinklers") and not "checked_sprinkler" in loc_cur.list:
                    use action_button("sprinkler", "Check sprinklers", "haven_check_sprinklers")
                if haven_can_set_fire():
                    use action_button("fire", "Set a fire", "haven_set_fire")

            elif loc_cur == loc_haven_cell:
                if "checked_done" in loc_haven_cell.list:
                    use action_button("relax", "Lay down", "haven_sold_ending_bed_rep")
                    use action_button("shower", "Shower", "haven_sold_ending_shower_rep")
                    use action_button("look", "Look around", "haven_sold_ending_look_rep")
                else:
                    use action_button("look", "Look around", "haven_sold_ending_check_picker")

        if dis_cur == dis_dev or loc_cur == loc_pink:
            use action_button_wardrobe()
            use action_button_mirror()

        if loc_cur == loc_gloryhole_stall:
            use action_button("wait", "Knock and wait", "gloryhole_wait")
        elif loc_cur.has_gloryhole:
            use action_button("gloryhole", "Use the gloryhole", "gloryhole_enter")
        elif loc_cur.can_gloryhole and log.interactive("quest_gloryhole"):
            use action_button("gloryhole", "Make a gloryhole", "gloryhole_make_picker")

        use travel_screen_talk_actions()

screen travel_screen_talk_actions():



    if dis(dis_partyhouse) and (anabel_here() or (dani_here() and not dani.hate) or svet_here() or rachel_here()):
        use action_button("talk", "Chit chat", "random_event_picker_dance_party_talk_tombola_direct")

    if robin_here():
        if not (loc(loc_school_field_back) or (loc(loc_school_field) and not robin.heavy_preg) or (t.hour == 12 and loc(loc_school_cafe)) or loc(loc_pub) or ("soccer_sex_robin" in robin.list and dis(dis_school)) or loc(loc_bathroom)):
            use action_button_npc_robin()

    if cass_here() or mira_here():
        if not (t.hour == 12 and loc(loc_school_cafe)):
            if cass_here() and mira_here():
                use action_button_npc_cass_mira()
            elif cass_here():
                if not cass_here(loc_revel_backstreet):
                    use action_button_npc_cass()
            elif mira_here():
                if not (mira_here(loc_school_field_back) or ("saw_at_academy" in mira.list and dis(dis_school))):
                    use action_button_npc_mira()

    if rachel_here() or svet_here():
        if not ((t.hour == 12 and loc(loc_school_cafe)) or school_dance_trope_present() or loc(loc_revel_backstreet) or dis(dis_partyhouse)):
            if rachel_here() and svet_here():
                use action_button("talk", "Talk to " + svet.nname + " and " + rachel.fname, "svet_rachel_talk_test")
            elif rachel_here():
                if not ((rachel_exhib_stripping_hide() and loc(loc_school_gym)) or loc(loc_beach_gym) or rachel_here(loc_school_field_back)):
                    use action_button_npc_rachel()
            elif svet_here():
                use action_button("talk", "Talk to " + svet.setname, "svet_talk_picker")

    if dani_here() or anabel_here():
        if anabel_here() and anabel.hate:
            if not "blocked_talking" in anabel.list:
                use action_button("talk", "Talk to " + anabel.nname, "anabel_talk_reject_talking")

        elif not ((t.hour == 12 and loc(loc_school_cafe)) or school_dance_trope_present() or loc(loc_revel_backstreet) or dis(dis_partyhouse)):
            if dani_here() and anabel_here():
                use action_button("talk", "Talk to " + dani.nname + " and " + anabel.nname, "dani_anabel_talk_picker")
            elif dani_here() and not (loc(loc_pub) or dani.hate):
                use action_button_npc_dani()
            elif anabel_here():
                use action_button_npc_anabel()

    if jaylee_here():
        if jaylee_here(loc_junk_trailer_bathroom):
            use action_button("shower", "Shower with " + jaylee.setname, "shower_event_jaylee")
        else:
            use action_button_npc_jaylee()

    if simon_here():
        if loc_office_pi.visited:

            use action_button_npc_simon()

    if oskar_here():
        if not robin_here():
            use action_button_npc_oskar()

    if kitty_here() and kitty.has_met:
        use action_button_npc_kitty()

screen travel_screen_locs():


    if loc_cur == loc_gloryhole_stall:
        use travel_button(loc_from, "gloryhole_dress_leave", "Dress and leave")

    elif loc_cur in dis_misc.locs and not loc_from in dis_misc.locs:
        if loc_from.open():
            use travel_button(loc_from)
        elif not dis_cur is dis_misc:
            use travel_button(dis_cur.hub)
        else:
            use travel_button(dis_from.hub)

    elif dis_cur == dis_residential:


        if dis(dis_home) and not loc_kitchen.locked:
            use travel_button(loc_stairwell)
            use travel_button(loc_kitchen)
            use travel_button(loc_bedroom)
            use travel_button(loc_bathroom)
            use travel_button(loc_common)
            if robin.has_met:
                use travel_button(loc_bedroom_robin, If(robin_here(loc_bedroom_robin) and t.time_from_to(00.00, 06.00) and not robin.can_sex, "robin_bedroom_asleep", If(oskar_here(loc_bedroom_robin), "robin_oskar_sex_catch_picker", "")), icon_image=If(robin_here(loc_bedroom_robin) and not t.time_from_to(00.00, 06.00), "loc_bedroom_robin_light", "loc_bedroom_robin_dark"))

        elif loc(loc_bedroom_robin):
            if loc_kitchen.locked and "kickedout_window_entry" in robin.list:
                use travel_button(loc_stairwell)

        elif loc_cur == loc_stairwell:
            use travel_button(loc_kitchen)
            if loc_kitchen.locked and "kickedout_window_entry" in robin.list:
                use travel_button(loc_bedroom_robin, jump_loc=If(robin_here(dis_home), "", "robin_talk_kickedout_window_locked"), icon_image=If(robin_here(loc_bedroom_robin) and not t.time_from_to(00.00, 06.00), "loc_bedroom_robin_light", "loc_bedroom_robin_dark"))

            use travel_button(loc_office_ll, If(robin_here(loc_office_ll), "robin_oskar_sex_catch_picker", 
            If(loc_kitchen.locked and loc_office_ll.open(), "oskar_office_enter_reject", "")), icon_image=If(loc_office_ll.open(), "loc_office_ll_light", "loc_office_ll_dark"))



            use travel_button(loc_bedroom_dani, jump_loc="dani_bedroom_checks")
            use travel_button(loc_residential)

        elif loc(loc_office_ll):
            use travel_button(loc_stairwell)
            use travel_button(loc_office_ll_back)

        elif loc(loc_bedroom_dani):
            use travel_button(loc_stairwell)

        elif loc_cur == loc_residential:

            use travel_button(loc_stairwell)

            use travel_button(loc_park)

        elif loc(loc_park):
            use travel_button(loc_residential)
            if loc_park.explored:
                use travel_button(loc_park_field)
                use travel_button(loc_park_gazebo)


        elif loc(loc_park_toilet):
            use travel_button(loc_park_path)
            use travel_button_split(loc_park_toilet_boys, loc_park_toilet_girls)
            use travel_button(loc_park_gazebo)

        elif loc([loc_park_toilet_boys, loc_park_toilet_girls]):
            use travel_button(loc_park_toilet)

        elif loc(loc_park_path):
            use travel_button(loc_park_field)
            use travel_button(loc_walk_park_forest)
            use travel_button(loc_park_toilet)

        elif loc(loc_park_gazebo):
            use travel_button(loc_park_toilet)
            use travel_button(loc_walk_park_shrubs)
            use travel_button(loc_park)

        elif loc(loc_park_field):
            use travel_button(loc_park)
            use travel_button(loc_park_path)

        elif loc(loc_walk_park_shrubs):
            use travel_button(loc_park_gazebo)
            use travel_button(loc_walk_lake_shrubs)

        else:
            use travel_button(dis_residential.hub)

    elif dis_cur == dis_school:
        if loc_cur == loc_school:
            if t.day > 2:
                use travel_button(loc_school_hallway, jump_loc=If(t.time_from_to(20.00, 07.59) and loc_school_secret_entrance.visited, "loc_school_use_back", ""))
            use travel_button(loc_school_secret_entrance)

        elif loc_cur == loc_school_hallway:
            use travel_button(loc_school, jump_loc=If(t.time_from_to(20.00, 07.59) and loc_school_secret_entrance.visited, "loc_school_use_back", ""))
            use travel_button(loc_school_hallway_2f)
            use travel_button(loc_school_classroom)
            use travel_button(loc_school_cafe)
            use travel_button(loc_school_gym)
            use travel_button(loc_school_field)
            use travel_button_split(loc_school_toilet_boys, loc_school_toilet_girls, jump_loc1="school_toilet_boy_arrival")



        elif loc_cur in [loc_school_classroom, loc_school_cafe, loc_school_toilet_girls, loc_school_toilet_boys]:
            use travel_button(loc_school_hallway)

        elif loc_cur == loc_school_gym:
            use travel_button(loc_school_hallway)
            use travel_button(loc_school_field)
            use travel_button_split(loc_school_locker_boys, loc_school_locker_girls, jump_loc1="school_locker_boy_arrival")

        elif loc_cur == loc_school_hallway_2f:
            use travel_button(loc_school_hallway)
            use travel_button(loc_school_library)
            use travel_button(loc_school_sewroom, jump_loc=If(not (saskia_here(loc_school_sewroom) or frida_here(loc_school_sewroom)), "loc_school_sewroom_locked", ""))
            use travel_button(loc_school_darkroom, jump_loc=If(not log.interactive("photo_03"), "school_darkroom_arrival", ""))




        elif loc([loc_school_sewroom, loc_school_library, loc_school_chem, loc_school_darkroom]):
            use travel_button(loc_school_hallway_2f)

        elif loc_cur == loc_school_field:
            use travel_button(loc_school_hallway, jump_loc=If(rachel_exhib_stripping_show() and not c.nude, "rachel_talk_exhib_strip_enter_school", ""))
            use travel_button(loc_school_gym, jump_loc=If(rachel_exhib_stripping_show() and not c.nude, "rachel_talk_exhib_strip_enter_school", ""))
            use travel_button(loc_school_locker_old)
            use travel_button(loc_school_field_back, If(school_soccer_hangingout(),"school_field_soccer_hangout", ""))
            if not loc_school_secret_entrance.locked:
                use travel_button(loc_school_secret_entrance)

        elif loc_cur == loc_school_field_back:

            use travel_button(loc_school_field)
            use travel_button(loc_school_locker_old)

        elif loc_cur == loc_school_pool:
            use travel_button_split(loc_school_locker_boys, loc_school_locker_girls)

        elif loc_cur == [loc_school_darkroom, loc_school_photostudio, loc_school_photo_changingroom]:
            use travel_button(loc_school_hallway_2f)
            use travel_button(loc_school_darkroom, jump_loc="school_photo_quest_picker")
            use travel_button(loc_school_photostudio)
            use travel_button(loc_school_photo_changingroom)

        elif loc_cur in [loc_school_locker_boys, loc_school_locker_girls]:
            use travel_button(loc_school_gym)


        elif loc_cur == loc_school_locker_old:
            use travel_button(loc_school_field)
            use travel_button(loc_school_field_back, If(school_soccer_hangingout(),"school_field_soccer_hangout", ""))

        elif loc(loc_school_secret_entrance):
            use travel_button(loc_school)
            use travel_button(loc_school_field)
            use travel_button(loc_walk_school_forest)

        else:
            use travel_button(dis_school.hub)

    elif dis_cur == dis_lake:

        if loc_cur == loc_lake:
            use travel_button_split(loc_beach_locker_boys, loc_beach_locker_girls)
            use travel_button(loc_boardwalk)
            use travel_button(loc_walk_lake_shrubs)


        elif loc_cur == loc_boardwalk:
            use travel_button(loc_lake)
            use travel_button(loc_pier)

        elif loc_cur == loc_pier:
            use travel_button(loc_boardwalk)

        elif loc_cur in [loc_beach_locker_girls, loc_beach_locker_boys]:
            use travel_button(loc_lake)
            use travel_button(loc_beach_hangout)

        elif loc_cur == loc_beach_hangout:
            use travel_button_split(loc_beach_locker_boys, loc_beach_locker_girls)
            use travel_button(loc_beach_gym)
            use travel_button(loc_beach_fire)
            use travel_button(loc_beach_water)

        elif loc_cur == loc_beach_fire:
            use travel_button(loc_beach_hangout)
            use travel_button(loc_beach_pier)
            use travel_button(loc_beach_water)

        elif loc_cur == loc_beach_pier:
            use travel_button(loc_beach_fire)
            use travel_button(loc_beach_water)

        elif loc_cur == loc_beach_gym:
            use travel_button(loc_beach_rocks)
            use travel_button(loc_beach_hangout)
            use travel_button(loc_beach_water)

        elif loc_cur == loc_beach_rocks:

            use travel_button(loc_beach_gym)
            use travel_button(loc_beach_water)

        elif loc_cur == loc_beach_secluded:
            use travel_button(loc_beach_rocks)
            use travel_button(loc_beach_water)

        elif loc_cur == loc_beach_water:
            use travel_button(loc_from)

        else:
            use travel_button(dis_lake.hub)

    elif dis_cur == dis_revel:

        if loc_cur == loc_revel:
            if loc_revel.explored:
                use travel_button(loc_market)
                use travel_button(loc_pub)
                use travel_button(loc_revel_backstreet)
                use travel_button(loc_hospital_entrance)

        elif loc(loc_revel_backstreet):
            use travel_button(loc_revel)
            if loc_revel_backstreet.explored:
                use travel_button(loc_shop_funwear)
                use travel_button(loc_shop_tattoo)
                use travel_button(loc_revel_backstreet_stairwell)

        elif loc(loc_revel_backstreet_stairwell):
            use travel_button(loc_revel_backstreet)
            if log.completed("Becoming the Fixer"):
                use travel_button(loc_office_pi, jump_loc=If("intro" in loc_office_pi.list, If(loc_office_pi.visited, "", "loc_office_pi_enter_firsttime"), "loc_office_pi_discover"), icon_image=If(simon_here(loc_office_pi), "loc_office_pi_light", "loc_office_pi_dark"), locked=If("has_key" in loc_office_pi.list, False, If(simon_here(loc_office_pi), False, True)))





            if quest_dancevip.active:
                use travel_button(loc_party_main, jump_loc=If(school_dance_at_party() and not t.hour == 4, "dance_party_start_late_picker", "loc_party_main_locked"), desc="Party house", locked=If(school_dance_at_party(), False, True))

        elif loc(loc_office_pi):
            use travel_button(loc_revel_backstreet_stairwell)
            use travel_button(loc_office_pi_back, icon_image=If(simon_here(loc_office_pi_back), "loc_office_pi_back_light", "loc_office_pi_back_dark"))

        elif loc(loc_office_pi_back):
            use travel_button(loc_office_pi, icon_image=If(simon_here(loc_office_pi), "loc_office_pi_light", "loc_office_pi_dark"))

        elif loc([loc_shop_funwear, loc_shop_tattoo]):
            use travel_button(loc_revel_backstreet)

        elif loc_cur == loc_hospital_entrance:
            use travel_button(loc_revel)
            use travel_button(loc_hospital_lobby)

        elif loc_cur == loc_hospital_lobby:
            use travel_button(loc_hospital_entrance)

        elif loc_cur == loc_pub:
            use travel_button(loc_revel)
            use travel_button_split(loc_pub_toilet_boys, loc_pub_toilet_girls)
            use travel_button(loc_pub_changingroom)

        elif loc_cur in [loc_pub_toilet_girls, loc_pub_toilet_boys, loc_pub_changingroom]:
            use travel_button(loc_pub)

        elif loc(loc_pub_toilet_girls_stall):
            use travel_button(loc_pub_toilet_girls)

        elif loc_cur == loc_commercial:
            use travel_button(loc_revel)
            use travel_button(loc_mall)
            use travel_button(loc_market)

        elif loc(loc_mall):
            use travel_button(loc_commercial)

        elif loc(loc_market):
            use travel_button(loc_revel)
            if loc_market.explored:
                if shop_needle.open:
                    use travel_button(loc_market_stall_needle)
                if shop_milk.open:
                    use travel_button(loc_market_stall_milk)


        elif loc([loc_market_stall_needle, loc_market_stall_milk]):
            use travel_button(loc_market)

        elif dis(dis_partyhouse):
            if not school_dance_at_party():
                if loc(loc_party_main):
                    use travel_button(loc_revel_backstreet_stairwell)
                    use travel_button(loc_party_bedroom1)
                else:
                    use travel_button(loc_party_main)
            else:
                use travel_button(loc_party_kitchen)
                use travel_button(loc_party_main)
                use travel_button(loc_party_stage)
                use travel_button(loc_party_hall)
                use travel_button(loc_party_terrace)

        else:
            use travel_button(dis_revel.hub)

    elif dis_cur == dis_truckstop:

        if loc_cur == loc_truckstop:

            use travel_button(loc_motel)
            use travel_button(loc_highway)

        elif loc_cur == loc_diner:
            use travel_button(loc_truckstop)
            use travel_button(loc_diner_toilet_girls)
            use travel_button(loc_diner_toilet_boys)
            use travel_button(loc_diner_changingroom)

        elif loc_cur in [loc_diner_toilet_girls, loc_diner_toilet_boys, loc_diner_changingroom]:
            use travel_button(loc_diner)

        elif loc_cur == loc_motel:
            use travel_button(loc_truckstop)
            use travel_button(loc_motel_lobby)

            use travel_button(loc_motel_room)
            use travel_button(loc_motel_pinkroom)

        elif loc_cur in [loc_motel_lobby, loc_motel_pool]:
            use travel_button(loc_motel)

        elif loc([loc_motel_room, loc_motel_pinkroom2, loc_motel_room2]):
            use travel_button(loc_motel)
            use travel_button(loc_motel_shower)

        elif loc(loc_motel_pinkroom):
            use travel_button(loc_motel, jump_loc="pinkroom_leave")
            use travel_button(loc_motel_shower)

        elif loc(loc_motel_shower):
            use travel_button(loc_from, ignore_locked=True)

        elif loc(loc_highway):
            use travel_button(loc_truckstop)
            use travel_button(loc_highway_slum)

        elif loc(loc_highway_slum):
            use travel_button(loc_highway)
            use travel_button(loc_highway_slum_street)
            use travel_button(loc_walk_slum_pipe)

        elif loc(loc_highway_slum_street):
            use travel_button(loc_highway_slum)
            use travel_button(loc_highway_slum_still)
            use travel_button(loc_highway_slum_home)

        elif loc(loc_highway_slum_still):
            use travel_button(loc_highway_slum_street)

        elif loc(loc_highway_slum_home):
            use travel_button(loc_highway_slum_street)

        else:
            use travel_button(dis_truckstop.hub)

    elif dis_cur == dis_checkpoint:
        if loc_cur == loc_checkpoint:
            use travel_button(loc_industrial)
            use travel_button(loc_junk_entrance)
            use travel_button(loc_checkpoint_lobby)


        elif loc_cur == loc_checkpoint_guardpost:
            use travel_button(loc_checkpoint)





        elif loc_cur == loc_junk_entrance:
            use travel_button(loc_checkpoint)
            use travel_button(loc_junk_office)

        elif loc_cur == loc_junk_office:
            use travel_button(loc_junk_entrance)
            use travel_button(loc_junk_1)
            use travel_button(loc_junk_2)

        elif loc(loc_junk_1):
            use travel_button(loc_junk_office)
            use travel_button(loc_walk_junk_rails)

        elif loc(loc_junk_2):
            use travel_button(loc_junk_office)
            use travel_button(loc_junk_trailer)

        elif loc_cur == loc_junk_trailer:
            use travel_button(loc_junk_2)
            use travel_button(loc_junk_trailer_bathroom)

        elif loc_cur == loc_junk_trailer_bathroom:
            use travel_button(loc_junk_trailer)

        elif loc_cur == loc_mechanic:
            use travel_button(loc_industrial)
            use travel_button(loc_mechanic_office)

        elif loc_cur == loc_mechanic_office:
            use travel_button(loc_mechanic)

        elif loc_cur == loc_checkpoint_lobby:
            use travel_button(loc_checkpoint)
            use travel_button(loc_checkpoint_office)
            use travel_button(loc_checkpoint_office_empty)

        elif loc_cur in [loc_checkpoint_office, loc_checkpoint_office_empty]:
            use travel_button(loc_checkpoint_lobby)

        else:
            use travel_button(dis_checkpoint.hub)

    elif dis(dis_walk):


        if loc(loc_walk_slum_pipe):
            use travel_button(loc_highway_slum)
            use travel_button(loc_walk_junk_rails)

        elif loc(loc_walk_junk_rails):
            use travel_button(loc_junk_1)
            use travel_button(loc_walk_slum_pipe)


        elif loc(loc_walk_park_forest):
            use travel_button(loc_park_path)
            use travel_button(loc_walk_school_forest)

        elif loc(loc_walk_school_forest):
            use travel_button(loc_school_secret_entrance)
            use travel_button(loc_walk_park_forest)


        elif loc(loc_walk_park_shrubs):
            use travel_button(loc_park_gazebo)
            use travel_button(loc_walk_lake_shrubs)

        elif loc(loc_walk_lake_shrubs):
            use travel_button(loc_walk_park_shrubs)
            use travel_button(loc_lake)

    elif dis_cur == dis_haven:
        if loc_cur == loc_haven_exterior:
            if not loc_haven_exterior.locked:
                use travel_button(loc_highway)
            use travel_button(loc_haven_lobby)

        elif loc_cur == loc_haven_lobby:
            use travel_button(loc_haven_exterior, "haven_ending_leave_intel", "Leave Haven")
            use travel_button(loc_haven_hallway_1f)
            use travel_button(loc_haven_landing)

        elif loc_cur == loc_haven_hallway_1f:
            use travel_button(loc_haven_lobby)
            use travel_button(loc_haven_bedroom)
            use travel_button(loc_haven_shower)
            use travel_button(loc_haven_room1)

        elif loc_cur == loc_haven_bedroom:
            use travel_button(loc_haven_hallway_1f)
            use travel_button(loc_haven_bed)

        elif loc_cur == loc_haven_bed:
            use travel_button(loc_haven_bedroom)

        elif loc_cur == loc_haven_shower:
            use travel_button(loc_haven_hallway_1f)
            if log.interactive("mq_05_b") and not loc_haven_utilities.visited:
                use travel_button(loc_haven_utilities, "haven_shower_stall_arrival")

        elif loc_cur == loc_haven_shower_stall:
            use travel_button(loc_haven_shower, "haven_shower_dress", "Dress and leave")
            use travel_button(loc_haven_utilities, "haven_utilities_arrival_checks")

        elif loc_cur == loc_haven_utilities:
            use travel_button(loc_haven_shower_stall, "haven_shower_stall_arrival")

        elif loc_cur == loc_haven_room1:
            use travel_button(loc_haven_hallway_1f)

        elif loc_cur == loc_haven_landing:
            use travel_button(loc_haven_lobby)
            use travel_button(loc_haven_hallway_2f)
            use travel_button(loc_haven_hallway_3f, "loc_haven_hallway_3f_visit")

        elif loc_cur == loc_haven_hallway_2f:
            use travel_button(loc_haven_landing)
            use travel_button(loc_haven_room2)
            use travel_button(loc_haven_lounge)
            use travel_button(loc_haven_room3)

        elif loc_cur in [loc_haven_room2, loc_haven_room3]:
            use travel_button(loc_haven_hallway_2f)

        elif loc_cur == loc_haven_lounge:
            use travel_button(loc_haven_hallway_2f)
            use travel_button(loc_haven_storage)

        elif loc_cur == loc_haven_storage:
            use travel_button(loc_haven_lounge)

        elif loc_cur == loc_haven_cell:
            if "checked_done" in loc_haven_cell.list:
                use travel_button(loc_haven_cell_dummy, "haven_sold_ending_check_door_rep", "Check the door")
            elif not "checked_door" in loc_haven_cell.list:
                use travel_button(loc_haven_cell_dummy, "haven_sold_ending_check_door", "Check the door")
            else:
                use travel_button(loc_haven_cell, "haven_sold_ending_check_door", "Check the door")


screen travel_screen():
    zorder 0
    add "map_travel_frame" pos (517,871)
    hbox anchor (0.0,1.0) align (0.23,0.97) spacing 4:

        use travel_worldmap_but()
        frame xysize (50,1) background None
        use travel_screen_locs()

    hbox pos (655, 845) spacing 4:
        use travel_screen_actions()
    hbox pos (980, 845) spacing 4:
        use travel_screen_pc_actions()

default loc_list = []
default loc_list_all = []
label location_call:





    $ loc_list = []

    $ loc_bedroom = Location("Bedroom", "loc_bedroom", outside=False, population=0, forbid_outfit=["swim"], forbid_exposed=False, loc_type="room", can_loiter=True, home_location=True)
    $ loc_kitchen = Location("Kitchen", "loc_kitchen", outside=False, population=0, forbid_outfit=["swim"], forbid_exposed=False, loc_type="plaster", can_loiter=True, can_eat=True)
    $ loc_common = Location("Common room", "loc_common", outside=False, population=0, forbid_outfit=["swim"], forbid_exposed=False, loc_type="plaster", can_loiter=True)
    $ loc_bathroom = Location("Bathroom", "loc_bathroom", outside=False, population=0, forbid_outfit=["swim"], forbid_exposed=False, loc_type="tile")
    $ loc_hallway = Location("Hallway", "loc_hallway", outside=False, population=0, forbid_outfit=["swim"], forbid_exposed=False, loc_type="plaster")

    $ loc_bedroom_robin = Location("Robin's bedroom", "loc_bedroom_robin", outside=False, population=0, forbid_outfit=["swim"], forbid_exposed=False, loc_type="room")

    $ dis_home = District("dis_home", "loc_kitchen", 0, loc_list, npc_desc="Somewhere at home.")

    $ loc_list = []
    $ loc_stairwell = Location("Building courtyard", "loc_stairwell", loc_type="grass", events=False)
    $ loc_office_ll = Location("Landlord's office", "loc_office_ll", outside=False, population=0, opening_hours=[8,9,10,11,12,13,14,15,16,17,18], events=False)
    $ loc_office_ll_back = Location("Landlord's office back room", "loc_office_ll_back", outside=False, population=0, opening_hours=[8,9,10,11,12,13,14,15,16,17,18], events=False, locked=True)


    $ dis_home_area = District("dis_home_area", "loc_stairwell", 0, loc_list, npc_desc="Around the home area.")


    $ loc_list = []
    $ loc_park = Location("Blaston park", "loc_park", can_whore=True, loc_type="grass", isolate_loc="loc_bushes", can_loiter=True, can_eat=True, can_sleep=True)
    $ loc_park_toilet = Location("Blaston park toilets", "loc_park_toilet", events=False)
    $ loc_park_toilet_boys = Location("Boys toilet", "loc_park_toilet_boys", loc_type="tile", outside=False, mens_room=True, events=False, can_gloryhole=True)
    $ loc_park_toilet_girls = Location("Girls toilet", "loc_park_toilet_girls", loc_type="tile", outside=False, events=False, can_gloryhole=True)
    $ loc_park_toilet_girls_stall = Location("Women's toilet stall", "loc_park_toilet_girls_stall", outside=False, population=1, loc_type="tile", can_gloryhole=True)
    $ loc_park_path = Location("Park scenic path", "loc_park_path", can_whore=True, loc_type="grass", population=1, isolate_loc="loc_bushes")
    $ loc_park_gazebo = Location("Park gazebo", "loc_park_gazebo", can_whore=True, loc_type="grass", population=1, isolate_loc="loc_bushes")
    $ loc_park_field = Location("Park grassy field", "loc_park_field", loc_type="grass", population=1, isolate_loc="loc_bushes")


    $ dis_park = District("dis_park", "loc_park", 30, loc_list, npc_desc="At the park.")

    $ loc_list = []
    $ loc_residential = Location("Home street", "loc_residential", can_whore=True)
    $ loc_shop_corner = Location("Corner shop", "loc_shop_corner", loc_type="plaster", isolate_loc="loc_alley", outside=True, population=0, opening_hours=irange(8, 19), events=False)

    $ loc_bedroom_dani = Location("Dani's bedroom", "loc_bedroom_dani", outside=False, population=0, events=False, locked=True, loc_type="room")

    $ loc_busstop_residential = Location("Bus stop", "loc_busstop_residential", events=False)
    $ dis_residential = District("dis_residential", "loc_residential", 20, loc_list, sub_districts=[dis_home, dis_home_area, dis_park])




    $ loc_list = []

    $ loc_beach_pier = Location("Under the pier", "loc_beach_pier", force_outfit="swim", forbid_exposed=False, can_whore=True, loc_type="beach", isolate_loc="loc_beach_pier", can_sleep=True)
    $ loc_beach_fire = Location("Beach firepit", "loc_beach_fire", force_outfit="swim", forbid_exposed=False, can_whore=True, loc_type="beach", isolate_loc="loc_beach_pier", can_loiter=True)
    $ loc_beach_hangout = Location("Beach hangout", "loc_beach_hangout", force_outfit="swim", forbid_exposed=False, can_whore=True, loc_type="beach", isolate_loc="loc_beach_locker_girls", can_loiter=True)
    $ loc_beach_gym = Location("Beach workout area", "loc_beach_gym", force_outfit="swim", forbid_exposed=False, can_whore=True, loc_type="beach", isolate_loc="loc_beach_pier")
    $ loc_beach_rocks = Location("Rocky beach", "loc_beach_rocks", force_outfit="swim", forbid_exposed=False, can_whore=True, loc_type="beach", isolate_loc="loc_beach_rocks")
    $ loc_beach_secluded = Location("Secluded beach", "loc_beach_secluded", force_outfit="swim", forbid_exposed=False, can_whore=True, loc_type="beach", isolate_loc="loc_beach_secluded")

    $ loc_beach_water = Location("In the water", "loc_beach_water", force_outfit="swim", forbid_exposed=False, can_whore=True, loc_type="beach", isolate_loc="loc_beach_pier", events=False)

    $ dis_beach = District("dis_beach", "loc_beach", 60, loc_list, npc_desc="At the beach somewhere.")

    $ loc_list = []
    $ loc_lake = Location("Lake", "loc_lake")

    $ loc_beach_locker_boys = Location("Boys changing room", "loc_beach_locker_boys", outside=False, loc_type="tile", mens_room=True, events=False, can_gloryhole=True)
    $ loc_beach_locker_girls = Location("Girls changing room", "loc_beach_locker_girls", outside=False, loc_type="tile", events=False, can_gloryhole=True)
    $ loc_beach_locker_girls_stall = Location("Beach changing cabin", "loc_beach_locker_girls_stall", outside=False, loc_type="tile", events=False, can_gloryhole=True)

    $ loc_boardwalk = Location("Boardwalk", "loc_boardwalk", can_whore=True, can_loiter=True, can_eat=True, can_sleep=True, isolate_loc="loc_beach_locker_girls")
    $ loc_pier = Location("Pier", "loc_pier", can_loiter=True, isolate_loc="loc_beach_locker_girls")

    $ loc_busstop_lake = Location("Bus stop", "loc_busstop_lake", events=False)
    $ dis_lake = District("dis_lake", "loc_lake", 40, loc_list, sub_districts=[dis_beach], npc_desc="Around the lake area.")




    $ loc_list = []
    $ loc_school = Location("School entrance", "loc_school", can_whore=True, loc_type="plaster", can_sleep=True, isolate_loc="loc_bushes")

    $ loc_school_hallway = Location("School hallway", "loc_school_hallway", outside=False, opening_hours=irange(8,20), loc_type="plaster", isolate_loc="loc_school_toilet_girls")
    $ loc_school_hallway_2f = Location("School hallway 2f", "loc_school_hallway_2f", outside=False, opening_hours=irange(8,20), loc_type="plaster", isolate_loc="loc_school_toilet_girls")
    $ loc_school_classroom = Location("Classroom", "loc_school_classroom", outside=False, opening_hours=irange(8,20), loc_type="plaster", isolate_loc="loc_school_toilet_girls")
    $ loc_school_cafe = Location("Cafeteria", "loc_school_cafe", outside=False, opening_hours=irange(8,20), loc_type="plaster", can_loiter=True, can_eat=True, isolate_loc="loc_school_toilet_girls")
    $ loc_school_gym = Location("Gymnasium", "loc_school_gym", outside=False, opening_hours=irange(8,20), loc_type="plaster", isolate_loc="loc_school_locker_girls")
    $ loc_school_pool = Location("Swimming pool", "loc_school_pool", outside=False, force_outfit="swim", opening_hours=irange(8,20), loc_type="tile", isolate_loc="loc_school_locker_girls")
    $ loc_school_field = Location("Soccer pitch", "loc_school_field", opening_hours=irange(8,20), loc_type="grass", can_loiter=True, can_sleep=True, isolate_loc="loc_bushes")
    $ loc_school_field_back = Location("Behind the old lockers", "loc_school_field_back", locked=True, opening_hours=irange(8,20), isolate_loc="loc_bushes", drinking_location=True)
    $ loc_school_locker_girls = Location("Girls locker room", "loc_school_locker_girls", outside=False, population=1, opening_hours=irange(8,20), loc_type="tile", isolate_loc="loc_school_locker_girls")
    $ loc_school_locker_boys = Location("Boys locker room", "loc_school_locker_boys", outside=False, population=1, opening_hours=irange(8,20), loc_type="tile", mens_room=True, isolate_loc="loc_school_locker_boys")
    $ loc_school_locker_shower = Location("School shower", "loc_school_locker_shower", outside=False, population=1, opening_hours=irange(8,20), loc_type="tile", isolate_loc="loc_school_locker_shower")
    $ loc_school_locker_old = Location("Old locker room", "loc_school_locker_old", outside=False, locked=True, population=0, opening_hours=irange(8,20), loc_type="tile", isolate_loc="loc_school_locker_old")
    $ loc_school_toilet = Location("Toilet entrance", "loc_school_toilet", outside=False, opening_hours=irange(8,20), loc_type="plaster", isolate_loc="loc_school_toilet_girls")
    $ loc_school_toilet_girls = Location("Girls toilet", "loc_school_toilet_girls", outside=False, population=1, opening_hours=irange(8,20), loc_type="tile", isolate_loc="loc_school_toilet_girls_stall", can_gloryhole=True)
    $ loc_school_toilet_girls_stall = Location("Girls toilet stall", "loc_school_toilet_girls_stall", outside=False, population=0, opening_hours=irange(8,20), loc_type="tile", isolate_loc="loc_school_toilet_girls_stall", can_gloryhole=True)
    $ loc_school_toilet_boys = Location("Boys toilet", "loc_school_toilet_boys", outside=False, population=1, opening_hours=irange(8,20), loc_type="tile", mens_room=True, isolate_loc="loc_school_toilet_boys_stall", can_gloryhole=True)
    $ loc_school_toilet_boys_stall = Location("Boys toilet stall", "loc_school_toilet_boys_stall", outside=False, population=0, opening_hours=irange(8,20), loc_type="tile", mens_room=True, isolate_loc="loc_school_toilet_boys_stall", can_gloryhole=True)
    $ loc_school_darkroom = Location("Photo darkroom", "loc_school_darkroom", outside=False, locked=True, events=False, opening_hours=irange(15,20), loc_type="plaster", isolate_loc="loc_school_toilet_girls")
    $ loc_school_photo_changingroom = Location("Studio dressing room", "loc_school_photo_changingroom", outside=False, opening_hours=irange(8,20), loc_type="plaster")
    $ loc_school_photostudio = Location("Photo studio", "loc_school_photostudio", outside=False, opening_hours=irange(8,20), loc_type="plaster")
    $ loc_school_sewroom = Location("Clothing club", "loc_school_sewroom", outside=False, opening_hours=irange(8,20), loc_type="plaster", isolate_loc="loc_school_toilet_girls", events=False)
    $ loc_school_chem = Location("Chemestry lab", "loc_school_chem", outside=False, opening_hours=irange(8,20), loc_type="plaster", isolate_loc="loc_school_toilet_girls", events=False)
    $ loc_school_library = Location("Library", "loc_school_library", outside=False, opening_hours=irange(8,20), loc_type="plaster", can_loiter=True, isolate_loc="loc_school_toilet_girls", events=False)
    $ loc_school_secret_entrance = Location("School secret entrance", "loc_school_secret_entrance", loc_type="grass", isolate_loc="loc_school_secret_entrance", locked=True, events=False)

    $ loc_busstop_school = Location("Bus stop", "loc_busstop_school", isolate_loc="loc_bushes")
    $ dis_school = District("dis_school", "loc_school", 40, loc_list, npc_desc="At the academy somewhere.")






    $ loc_list = []
    $ loc_pub = Location("The Pub", "loc_pub", outside=False, opening_hours=[11,12,13,14,15,16,17,18,19,20,21,22,23,0,1,2], loc_type="plaster", can_loiter=True, isolate_loc="loc_pub_toilet_girls", drinking_location=True)
    $ loc_pub_toilet_girls = Location("Women's toilet", "loc_pub_toilet_girls", outside=False, population=1, opening_hours=[11,12,13,14,15,16,17,18,19,20,21,22,23,0,1,2], loc_type="tile", can_gloryhole=True)
    $ loc_pub_toilet_girls_stall = Location("Women's toilet stall", "loc_pub_toilet_girls_stall", outside=False, population=1, opening_hours=[11,12,13,14,15,16,17,18,19,20,21,22,23,0,1,2], loc_type="tile", can_gloryhole=True)
    $ loc_pub_toilet_boys = Location("Men's toilet", "loc_pub_toilet_boys", outside=False, population=1, opening_hours=[11,12,13,14,15,16,17,18,19,20,21,22,23,0,1,2], loc_type="tile", mens_room=True, can_gloryhole=True)
    $ loc_pub_changingroom = Location("Pub back room", "loc_pub_changingroom", outside=False, locked=True, population=0, opening_hours=[11,12,13,14,15,16,17,18,19,20,21,22,23,0,1,2], loc_type="plaster", events=False)

    $ dis_pub = District("dis_pub", "loc_pub", 40, loc_list, npc_desc="At the pub.")


    $ loc_list = []
    $ loc_hospital_entrance = Location("Mercy hospital", "loc_hospital_entrance", loc_type="plaster", events=False)
    $ loc_hospital_lobby = Location("Hospital reception", "loc_hospital_lobby", loc_type="plaster", events=False, outside=False)
    $ loc_hospital_ward = Location("Hospital ward", "loc_hospital_ward", loc_type="plaster", events=False, outside=False)
    $ loc_hospital_psy = Location("Psychologists office", "loc_hospital_psy", loc_type="plaster", events=False, outside=False)
    $ loc_hospital_office = Location("Office room", "loc_hospital_office", loc_type="plaster", events=False, outside=False)

    $ dis_hospital = District("dis_hospital", "loc_hospital_lobby", 40, loc_list, npc_desc="At the hospital.")


    $ loc_list = []
    $ loc_commercial = Location("High street", "loc_commercial", can_whore=True, can_loiter=True, can_sleep=True)
    $ loc_mall = Location("Mall", "loc_mall", outside=False, opening_hours=irange(8,22), loc_type="tile", can_loiter=True)
    $ loc_mall_shop_clothing = Location("Clothing shop", "loc_mall_shop_clothing", outside=False, opening_hours=irange(8,22), loc_type="plaster")
    $ loc_mall_shop_cosmetics = Location("Cosmetics shop", "loc_mall_shop_cosmetics", outside=False, opening_hours=irange(8,22), loc_type="plaster")
    $ loc_mall_changingroom = Location("Changing room", "loc_mall_changingroom", outside=False, opening_hours=irange(8,22), loc_type="plaster")
    $ loc_market = Location("Outdoor market", "loc_market", can_whore=True, can_loiter=True, can_eat=True, can_sleep=True)
    $ loc_market_stall_needle = Location("Needle girls stall", "loc_market_stall_needle", can_loiter=True)
    $ loc_market_stall_milk = Location("Milkmaid stall", "loc_market_stall_milk")
    $ dis_commercial = District("dis_commercial", "loc_commercial", 40, loc_list, npc_desc="Around the shopping area.")


    $ loc_list = []
    $ loc_party_main = Location("Main room", "loc_party_main", loc_type="room", population=0, outside=False, events=False, drinking_location=True, locked=True)
    $ loc_party_kitchen = Location("Kitchen", "loc_party_kitchen", loc_type="tile", population=0, outside=False, events=False, drinking_location=True)
    $ loc_party_bedroom1 = Location("Main bedroom", "loc_party_bedroom1", loc_type="room", population=0, outside=False, events=False, drinking_location=True)
    $ loc_party_bedroom2 = Location("Small bedroom", "loc_party_bedroom2", loc_type="room", population=0, outside=False, events=False, drinking_location=True)
    $ loc_party_bedroom3 = Location("Main bedroom", "loc_party_bedroom3", loc_type="room", population=0, outside=False, events=False)
    $ loc_party_bedroom4 = Location("Small bedroom", "loc_party_bedroom4", loc_type="room", population=0, outside=False, events=False)
    $ loc_party_terrace = Location("Terrace", "loc_party_terrace", loc_type="room", population=0, outside=False, events=False, drinking_location=True)
    $ loc_party_entrance = Location("Building entrance", "loc_party_entrance", loc_type="plaster", population=0, outside=False, events=False, drinking_location=True)
    $ loc_party_stage = Location("Stage", "loc_party_stage", loc_type="room", population=0, outside=False, events=False)
    $ loc_party_hall = Location("Hallway", "loc_party_hall", loc_type="plaster", population=0, outside=False, events=False)

    $ dis_partyhouse = District("dis_partyhouse", "loc_party_main", 0, loc_list, npc_desc="At the private party house.")

    $ loc_list = []
    $ loc_revel = Location("Revel street", "loc_revel", can_whore=True, can_sleep=True)
    $ loc_revel_backstreet = Location("Revel backstreet", "loc_revel_backstreet", can_whore=True, can_sleep=True, can_eat=True)
    $ loc_revel_backstreet_stairwell = Location("Appartment block", "loc_revel_backstreet_stairwell", events=False, outside=False, loc_type="plaster", locked=True)
    $ loc_shop_tattoo = Location("Beauty salon", "loc_shop_tattoo", outside=False, opening_hours=irange(12,23), loc_type="plaster", events=False)
    $ loc_shop_funwear = Location("Funwear shop", "loc_shop_funwear", outside=False, opening_hours=irange(12,23), loc_type="plaster", events=False)
    $ loc_busstop_revel = Location("Bus stop", "loc_busstop_revel")
    $ loc_office_pi = Location("Private Investigator", "loc_office_pi", outside=False, opening_hours=irange(12,23), loc_type="room", events=False)
    $ loc_office_pi_back = Location("P.I. back room", "loc_office_pi_back", outside=False, loc_type="room", events=False, locked=True, home_location=True)

    $ dis_revel = District("dis_revel", "loc_revel", 40, loc_list, sub_districts=[dis_pub, dis_hospital, dis_commercial, dis_partyhouse], npc_desc="Revel street somewhere.")





    $ loc_list = []
    $ loc_diner = Location("Truck stop diner", "loc_diner", loc_type="plaster", can_eat=True, locked=True)
    $ loc_diner_toilet_girls = Location("Women's toilet", "loc_diner_toilet_girls", loc_type="tile", can_gloryhole=True, locked=True)
    $ loc_diner_toilet_boys = Location("Men's toilet", "loc_diner_toilet_boys", loc_type="tile", can_gloryhole=True, locked=True)
    $ loc_diner_changingroom = Location("Diner changingroom", "loc_diner_changingroom", loc_type="plaster", locked=True)

    $ dis_diner = District("dis_diner", "loc_diner", 40, loc_list)

    $ loc_list = []
    $ loc_motel = Location("Motel", "loc_motel", loc_type="plaster", can_whore=True)
    $ loc_motel_lobby = Location("Motel lobby", "loc_motel_lobby", loc_type="plaster", outside=False, events=False, population=0)
    $ loc_motel_pool = Location("Motel pool", "loc_motel_pool", loc_type="plaster")
    $ loc_motel_room = Location("Motel room", "loc_motel_room", outside=False, locked=True, loc_type="room", population=0, events=False, home_location=True)
    $ loc_motel_pinkroom = Location("Motel pink room", "loc_motel_pinkroom", outside=False, locked=True, loc_type="room", population=0, events=False)
    $ loc_motel_shower = Location("Motel shower", "loc_motel_shower", outside=False, loc_type="tile", population=0, events=False)

    $ loc_motel_pinkroom2 = Location("Motel pink room", "loc_motel_pinkroom2", outside=False, locked=True, loc_type="room", population=0, events=False)
    $ loc_motel_room2 = Location("Motel room", "loc_motel_room2", outside=False, locked=True, loc_type="room", population=0, events=False)

    $ dis_motel = District("dis_motel", "loc_motel", 40, loc_list, npc_desc="The Motel somewhere.")

    $ loc_list = []
    $ loc_highway_slum = Location("Highway slum", "loc_highway_slum", can_sleep=True)
    $ loc_highway_slum_street = Location("Slum row", "loc_highway_slum_street", can_sleep=True)
    $ loc_highway_slum_still = Location("Slum still", "loc_highway_slum_still", outside=False, population=0, events=False, loc_type="room", opening_hours=(15,16,17,18,19,20,21,22,23,0,1,2,3))
    $ loc_highway_slum_home = Location("Slum home", "loc_highway_slum_home", can_sleep=True, outside=False, events=False, population=0, loc_type="room", home_location=True, locked=True)

    $ dis_slum = District("dis_slum", "loc_highway_slum", 80, loc_list,npc_desc="In the slums.")

    $ loc_list = []
    $ loc_truckstop = Location("Truck stop", "loc_truckstop", can_whore=True, can_loiter=True, can_sleep=True, isolate_loc="loc_truckstop_truck_1")
    $ loc_highway = Location("Highway overpass", "loc_highway", can_whore=True, can_loiter=True)

    $ loc_busstop_truckstop = Location("Bus stop", "loc_busstop_truckstop")

    $ dis_truckstop = District("dis_truckstop","loc_truckstop", 60, loc_list, sub_districts=[dis_diner, dis_motel, dis_slum], npc_desc="Somewhere around the truck stop.")




    $ loc_list = []

    $ loc_checkpoint_lobby = Location("Security building lobby", "loc_checkpoint_lobby", outside=False, locked=True, loc_type="plaster", events=False)
    $ loc_checkpoint_office = Location("Security office", "loc_checkpoint_office", outside=False, loc_type="plaster", events=False)
    $ loc_checkpoint_office_empty = Location("Security office", "loc_checkpoint_office_empty", outside=False, locked=True, loc_type="plaster", events=False)

    $ dis_security = District("dis_security", "loc_checkpoint_lobby", 0, loc_list)

    $ loc_list = []
    $ loc_junk_entrance = Location("Scrapyard entrance", "loc_junk_entrance", loc_type="plaster", isolate_loc="loc_walk_junk_rails")
    $ loc_junk_office = Location("Scavver office", "loc_junk_office", loc_type="plaster", locked=True, isolate_loc="loc_walk_junk_rails")
    $ loc_junk_1 = Location("Abandoned trainline", "loc_junk_1", can_sleep=True, can_whore=True, isolate_loc="loc_walk_junk_rails")
    $ loc_junk_2 = Location("Car graveyard", "loc_junk_2", can_sleep=True, isolate_loc="loc_walk_junk_rails")
    $ loc_junk_trailer = Location("Trailer home", "loc_junk_trailer", outside=False, loc_type="room", locked=True, population=0, can_loiter=True, isolate_loc="loc_walk_junk_rails", home_location=True)
    $ loc_junk_trailer_bathroom = Location("Trailer bathroom", "loc_junk_trailer_bathroom", outside=False, loc_type="room", population=0, isolate_loc="loc_walk_junk_rails")

    $ dis_junkyard = District("dis_junkyard", "loc_junk_entrance", 50, loc_list, npc_desc="At the junkyard.")

    $ loc_list = []

    $ loc_mechanic = Location("Maintenance area", "loc_mechanic", events=False, locked=True)
    $ loc_mechanic_office = Location("Maintenance office", "loc_mechanic_office", loc_type="plaster", events=False)

    $ dis_mechanic = District("dis_mechanic", "loc_mechanic", 0, loc_list)

    $ loc_list = []
    $ loc_industrial = Location("Industrial area", "loc_industrial", can_loiter=True, can_eat=True)

    $ dis_industrial = District("dis_industrial", "loc_industrial", 20, loc_list, sub_districts=[dis_mechanic])

    $ loc_checkpoint = Location("Security checkpoint", "loc_checkpoint", can_loiter=True)
    $ loc_checkpoint_guardpost = Location("Security guardpost", "loc_checkpoint_guardpost", events=False)

    $ loc_busstop_checkpoint = Location("Bus stop", "loc_busstop_checkpoint")
    $ dis_checkpoint = District("dis_checkpoint","loc_checkpoint", 30, loc_list, sub_districts=[dis_security, dis_junkyard, dis_industrial], npc_desc="At the security checkpoint.")









    $ loc_list = []


    $ loc_changingroom = Location("Changing room", "loc_changingroom", outside=False, population=0, loc_type="plaster")
    $ loc_gloryhole_stall = Location("Toilet stall", "loc_gloryhole_stall", outside=False, population=0, loc_type="tile", isolate_loc="loc_gloryhole_stall", can_gloryhole=True)


    $ loc_alley = Location("Backalley", "loc_alley", population=0)
    $ loc_bushes = Location("Bushes", "loc_bushes", loc_type="grass", population=0)
    $ loc_cupboard = Location("Empty room", "loc_cupboard", loc_type="plaster", population=0 )
    $ loc_rocks = Location("Behind some rocks", "loc_rocks", loc_type="beach", population=0)
    $ loc_school_field_back_isolate = Location("Behind lockers", "loc_school_field_back_isolate", loc_type="grass", population=0)

    $ loc_flat1 = Location("Some guys flat", "loc_flat1", loc_type="room", population=0, outside=False, events=False)
    $ loc_flat2 = Location("Some guys flat", "loc_flat2", loc_type="room", population=0, outside=False, events=False)
    $ loc_flat3 = Location("Some guys flat", "loc_flat3", loc_type="room", population=0, outside=False, events=False)
    $ loc_flat4 = Location("Some guys flat", "loc_flat4", loc_type="room", population=0, outside=False, events=False)
    $ loc_flat5 = Location("Some guys flat", "loc_flat5", loc_type="room", population=0, outside=False, events=False)

    $ loc_truckstop_truck_1 = Location("Between the trucks", "loc_truckstop_truck_1", loc_type="conc", population=0, events=False, isolate_loc="loc_lorry")
    $ loc_truckstop_truck_2 = Location("Between the trucks", "loc_truckstop_truck_2", loc_type="conc", population=0, events=False, isolate_loc="loc_lorry_1")
    $ loc_truckstop_truck_3 = Location("Between the trucks", "loc_truckstop_truck_3", loc_type="conc", population=0, events=False, isolate_loc="loc_lorry_1")
    $ loc_truckstop_truck_4 = Location("Between the trucks", "loc_truckstop_truck_4", loc_type="conc", population=0, events=False, isolate_loc="loc_lorry_2")
    $ loc_truckstop_truck_5 = Location("Between the trucks", "loc_truckstop_truck_5", loc_type="conc", population=0, events=False, isolate_loc="loc_lorry_2")







    $ loc_slumtent = Location("Some guys tent", "loc_slumtent", loc_type="room", population=0, outside=False, events=False)

    $ loc_lorry = Location("Back of a lorry", "loc_lorry", loc_type="room", population=0, outside=False, events=False)
    $ loc_lorry_1 = Location("Back of a lorry", "loc_lorry_1", loc_type="room", population=0, outside=False, events=False)
    $ loc_lorry_2 = Location("Back of a lorry", "loc_lorry_2", loc_type="room", population=0, outside=False, events=False)


    $ loc_homeless_start_1 = Location("Bushes", "loc_homeless_start_1", loc_type="grass", population=0, events=False)
    $ loc_homeless_start_2 = Location("Bushes", "loc_homeless_start_2", loc_type="grass", population=0, events=False)
    $ loc_homeless_start_3 = Location("Bushes", "loc_homeless_start_3", loc_type="grass", population=0, events=False)
    $ loc_homeless_start_4 = Location("Bushes", "loc_homeless_start_4", loc_type="grass", population=0, events=False)
    $ loc_homeless_start_5 = Location("Bushes", "loc_homeless_start_5", loc_type="grass", population=0, events=False)


    $ dis_misc = District("dis_misc", "loc_alley", 30, loc_list, map_enabled=False)




    $ loc_list = []
    $ loc_bus_interior = Location("On the bus", "loc_bus_interior", outside=False)
    $ dis_bus_interior = District("dis_bus_interior", "loc_bus_interior", 30, loc_list, map_enabled=False)




    $ loc_list = []

    $ loc_walk_junk_rails = Location("Abandoned rails", "loc_walk_junk_rails", loc_type="grass", locked=True, population=0)
    $ loc_walk_slum_pipe = Location("Sewer pipe", "loc_walk_slum_pipe", loc_type="plaster", locked=True, population=0, outside=False)
    $ loc_walk_park_forest = Location("Muddy path", "loc_walk_park_forest", loc_type="grass", locked=True, population=0)
    $ loc_walk_school_forest = Location("Field trees", "loc_walk_school_forest", loc_type="grass", locked=True, population=0)
    $ loc_walk_park_shrubs = Location("Shrubbery", "loc_walk_park_shrubs", loc_type="grass", locked=True, population=0)
    $ loc_walk_lake_shrubs = Location("Sparse bushes", "loc_walk_lake_shrubs", loc_type="grass", locked=True, population=0)

    $ dis_walk = District("dis_walk", "loc_walk_junk_rails", 80, loc_list, map_enabled=False)




    $ loc_list = []
    $ loc_haven_exterior = Location("Haven courtyard", "loc_haven_exterior")
    $ loc_haven_lobby = Location("Lobby", "loc_haven_lobby", outside=False, isolate_loc="loc_haven_room1")
    $ loc_haven_landing = Location("Landing", "loc_haven_landing", outside=False, isolate_loc="loc_haven_room3")

    $ loc_haven_hallway_1f = Location("1st floor hallway", "loc_haven_hallway_1f", outside=False, isolate_loc="loc_haven_room1")
    $ loc_haven_hallway_2f = Location("2nd floor hallway", "loc_haven_hallway_2f", outside=False, isolate_loc="loc_haven_room2")
    $ loc_haven_hallway_3f = Location("3rd floor hallway", "loc_haven_hallway_3f", outside=False, isolate_loc="loc_haven_guardroom", population=1)

    $ loc_haven_bedroom = Location("Sleeping area", "loc_haven_bedroom", outside=False, can_loiter=True, can_whore=True, isolate_loc="loc_haven_room1", loc_type="plaster")
    $ loc_haven_bed = Location("My sleeping corner", "loc_haven_bed", outside=False, can_scavenge=False, isolate_loc="loc_haven_room1", loc_type="room")
    $ loc_haven_shower = Location("Communal showers", "loc_haven_shower", outside=False, can_scavenge=False, isolate_loc="loc_haven_room1", block_actions=True)
    $ loc_haven_shower_stall = Location("Shower stall", "loc_haven_shower_stall", outside=False, can_scavenge=False, block_actions=True, isolate_loc="loc_haven_utilities")
    $ loc_haven_utilities = Location("Utility room", "loc_haven_utilities", outside=False, block_actions=True, population=1, isolate_loc="loc_haven_utilities")
    $ loc_haven_lounge = Location("Lounge", "loc_haven_lounge", outside=False, can_loiter=True, can_whore=True, isolate_loc="loc_haven_storage")
    $ loc_haven_storage = Location("Storage room", "loc_haven_storage", outside=False, population=1, isolate_loc="loc_haven_storage")

    $ loc_haven_room1 = Location("Dark and damp room", "loc_haven_room1", outside=False, isolate_loc="loc_haven_room1", population=1)
    $ loc_haven_room2 = Location("Noisy room", "loc_haven_room2", outside=False, isolate_loc="loc_haven_room2", population=1)
    $ loc_haven_room3 = Location("Dangerous room", "loc_haven_room3", outside=False, isolate_loc="loc_haven_room3", population=1)

    $ loc_haven_office = Location("[alex.nname]'s office", "loc_haven_office", outside=False, isolate_loc="loc_haven_guardroom", population=1)
    $ loc_haven_toplanding = Location("Top floor landing", "loc_haven_toplanding", outside=False, isolate_loc="loc_haven_guardroom", population=1)
    $ loc_haven_guardroom = Location("Guard barracks", "loc_haven_guardroom", outside=False, loc_type="plaster", isolate_loc="loc_haven_guardroom", population=1)
    $ loc_haven_ventroom = Location("Abandoned room", "loc_haven_ventroom", outside=False, isolate_loc="loc_haven_guardroom", population=1)

    $ loc_haven_cell = Location("My cell", "loc_haven_cell", outside=False, loc_type="plaster")
    $ loc_haven_cell_dummy = Location("My cell", "loc_haven_cell", outside=False, loc_type="plaster")

    $ dis_haven = District("dis_haven", "loc_haven_exterior", 100, loc_list, map_enabled=False, npc_desc="Somewhere in Haven.")





    $ loc_list = []
    $ loc_pink = Location("Pink", "loc_pink", outside=False)

    $ dis_dev = District("dis_dev", "loc_pink", 100, loc_list, map_enabled=False)




    $ loc_list = []



    $ loc_cur = loc_bedroom
    $ loc_from = loc_bedroom
    $ loc_fromfrom = loc_bedroom

    $ dis_cur = dis_residential
    $ dis_from = dis_residential

    $ loc_want = loc_bedroom

    $ districts = [dis_residential, dis_lake, dis_school, dis_revel, dis_checkpoint, dis_truckstop]
    $ busstops = [loc_busstop_residential, loc_busstop_lake, loc_busstop_school, loc_busstop_revel, loc_busstop_checkpoint, loc_busstop_truckstop]


    return

label loiter_jump:
    $ travel_loiter_location()
    if renpy.has_label(loc_cur.name + "_loiter"):
        jump expression loc_cur.name + "_loiter"
    "I have nothing in the area I can do so I just relax a bit where I am and kill some time."

label loiter_end:
    $ loiter()
    jump travel_arrival

label change_clothes:
    "This button will make Sammy find somewhere to change."
    "She will go to some alleyway or bushes to swap her clothes"
    "She will only be able to choose the outfit such as daily, party etc and not open the full wardrobe."
    "Of course events can trigger here where someone catches her or something."
    jump travel_arrival



label whore_jump:
    if renpy.has_label(loc_cur.name + "_whore"):
        jump expression loc_cur.name + "_whore"
    elif renpy.has_label(loc_cur.get_district().name + "_whore"):
        jump expression loc_cur.get_district().name + "_whore"
    else:
        "No whore event for this location. I need to add one."
        "Advertise yourself."
        "Once the whire storyline is unlocked and Sammy has accepted herself as a whore, she can actively advertise herself at any location."
    jump travel_arrival

label location_generic_closed_eject:
    pcm "This place is closing. I had better leave."
    $ travel_walk(loc_cur.district.hub)
    jump travel


label location_closed:
    "Generic location closed message."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
