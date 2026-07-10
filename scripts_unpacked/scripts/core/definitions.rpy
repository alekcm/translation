


init python:




    def dialogue_catcher_talk(event, interact=True, **kwargs):
        global test_what
        
        test_what = store._last_raw_what
        if not interact:
            return
        if event == "begin":
            dialogue_catcher_first_times()
            if player.has_perk([perk_gagged, perk_gagged_locked]):
                dialogue_catcher_gagged()
            elif player.having_sex and player.beingraped:
                dialogue_catcher_forced() 
            elif player.having_sex and "mouth" in player.sex_holes: 
                dialogue_catcher_suckspeak()
            else:
                dialogue_catcher_speak_clean()

    def dialogue_catcher_think(event, interact=True, **kwargs):
        global test_what
        
        test_what = store._last_raw_what
        if not interact:
            return
        if event == "begin":
            dialogue_catcher_think_clean()

    def dialogue_catcher_talk_npc_end(event, interact=True, **kwargs):
        if event == "end":
            
            if player.has_perk(perk_blackout) and not numgen(0,40):
                dialogue_catcher_drunk(event)

    def dialogue_catcher_talk_end(event, interact=True, **kwargs):
        if event == "end":
            if player.having_sex and not player.beingraped:
                player.having_sex_time()
            if player.has_perk(perk_blackout) and not numgen(0,40):
                dialogue_catcher_drunk(event)
            if not player.having_sex and player.desire > 300 and numgen(0, 2000) < (player.desire - 300):
                dialogue_catcher_horny(event)
            if player.having_sex and player.beingraped and not numgen(0, 10) and player.has_perk(perk_freeuse):
                dialogue_catcher_having_sex_forced_pretend(event)
            if player.having_sex and player.beingraped and not numgen(0, 10) and not player.has_perk(perk_freeuse):
                dialogue_catcher_having_sex_forced(event)
            if player.having_sex and player.selling and player.has_perk(perk_whore) and not numgen(0, 10):
                dialogue_catcher_having_sex_sold(event)
            if player.having_sex and player.selling and not player.has_perk([perk_whore, perk_bimbo, perk_gamine, perk_numb, perk_broken]) and not numgen(0, 10):
                dialogue_catcher_having_sex_sold_regret(event)

    def dialogue_catcher_bimbo(what):
        global test_what
        test_what = bimbofy(test_what)
        renpy.call("dialogue_catcher_event_bimbo")

    def dialogue_catcher_gagged():
        renpy.call("dialogue_catcher_event_gagged")
    def dialogue_catcher_suckspeak():
        renpy.call("dialogue_catcher_event_blowjob")
    def dialogue_catcher_speak_clean():
        renpy.call("dialogue_catcher_event_speak")
    def dialogue_catcher_think_clean():
        renpy.call("dialogue_catcher_event_think")
    def dialogue_catcher_forced():
        renpy.call("dialogue_catcher_event_forced")

    def dialogue_catcher_first_times():
        
        for i in ["hsex", "osex", "vsex", "asex", "swallow", "facial", "creamvag", "creamanal", "assault", "rape", "soldprice"]:
            if getattr(player, i) and not i in sex_first_time_dict:
                add_to_list(sex_first_time_dict, i)
                renpy.call("first_time_" + i)

    def dialogue_catcher_drunk(event, interact=True, **kwargs):
        renpy.show_screen("text_char_speak", text=rlist.drunk_dialogue)

    def dialogue_catcher_horny(event, interact=True, **kwargs):
        renpy.show_screen("text_char_speak", text=rlist.horny_dialogue)

    def dialogue_catcher_having_sex(event, interact=True, **kwargs):
        renpy.show_screen("text_char_speak", text=rlist.having_sex_dialogue)

    def dialogue_catcher_having_sex_forced(event, interact=True, **kwargs):
        renpy.show_screen("text_char_speak", text=rlist.having_sex_forced_dialogue)

    def dialogue_catcher_having_sex_forced_pretend(event, interact=True, **kwargs):
        renpy.show_screen("text_char_speak", text=rlist.having_sex_forced_freeuse_dialogue)

    def dialogue_catcher_having_sex_sold(event, interact=True, **kwargs):
        renpy.show_screen("text_char_speak", text=rlist.having_sex_sold_dialogue)

    def dialogue_catcher_having_sex_sold_regret(event, interact=True, **kwargs):
        renpy.show_screen("text_char_speak", text=rlist.having_sex_sold_regret_dialogue)



label dialogue_catcher_event_gagged:
    $ player.eye = renpy.random.choice([1,2,3,6])
    $ player.brow = renpy.random.choice([1,2,3,4])
    pcg "[rlist.gagged_dialogue]"
    return

label dialogue_catcher_event_blowjob:
    pcc "[rlist.blowjob_muffle]"
    return
label dialogue_catcher_event_bimbo:
    pcg "[test_what] BIMBO BIMBO."
    return

label dialogue_catcher_event_speak:
    $ test_what = dialogue_edit(test_what)
    pcc "[test_what]"
    return

label dialogue_catcher_event_think:
    $ test_what = dialogue_edit(test_what)
    pcmc "[test_what]"
    return

label dialogue_catcher_event_npc:
    $ test_what = dialogue_edit(test_what)
    pcmc "[test_what]"
    return

label dialogue_catcher_event_forced:
    pcc "[rlist.having_sex_forced]"
    return
















default cheats = 0
default danger_content = False
default danger_day_limit = True
default force_return = False





default tf_age = 0
default tf_weight = 0
default tf_gay = False
default tf_virgin = True




define district_home = ("bedroom", "bathroom", "common", "hallway", "kitchen")
define district_residential = ("residential_area", "residential_area_kiosk", "busstop_residential_area")
define district_commercial = ("commercial_area", "commercial_area_mall", "busstop_commercial_area")
define district_school_exterior = ("school_exterior", "busstop_school_exterior")
define district_school_interior = ("school_classroom", "school_hallway", "school_cafe", "school_gym", "school_field", "school_locker_girl", "school_locker_boy", "school_toilet", "school_toilet_boy", "school_toilet_girl", "school_locker_old", "school_field_back")
define district_highway = ("highway_local", "highway_local_motel", "busstop_highway_local")
define district_trainstation = ("revel", "trainstation_local_exterior", "trainstation_local_platform", "busstop_trainstation_exterior", "trainstation_local_pub", "trainstation_local_pub_toilet_girls", "trainstation_local_pub_toilet_boys", "commercial_area_mall_fitting")
define district_market = ("park_local_market", "filler")
define district_park = ("park_local", "park_local_community_centre")
define district_hospital = ("hospital_exterior", "hospital_reception")
define district_busstop_location = ("revel", "residential_area", "commercial_area", "school_exterior", "park_local", "highway_local", "truckstop", "checkpoint", "industrial_area", "lake_entrance")
define district_busstops = ("busstop_residential_area", "busstop_commercial_area", "busstop_school_exterior", "busstop_revel", "busstop_lake_entrance", "busstop_highway_local", "busstop_checkpoint", "busstop_industrial_area", "busstop_truckstop", "busstop_park_local")
define district_haven = ("haven_exterior", "haven_hallway_1f", "haven_hallway_2f", "haven_hallway_3f", "haven_lobby", "haven_landing", "haven_bedroom", "haven_bed", "haven_shower", "haven_shower_stall", "haven_room1", "haven_room2", "haven_room3", "haven_lounge", "haven_storage", "haven_utilities", "haven_office", "haven_guardroom")
define district_minor_locations = ("alley", "bushes", "school_locker_old")

define weekends = ("Saturday", "Sunday")
define weekend = ("Saturday", "Sunday")
define weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
define weekday = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
define morning = (6,7,8,9,10,11)
define afternoon = (12,13,14,15,16,17,18,19)
define evening = (20,21,22)
define night = (23,0,1,2,3,4,5)
define workhours = (8,9,10,11,12,13,14,15,16,17,18)
define work_hours = workhours
define schoolhours = (8,9,10,11,12,13)
define school_hours = schoolhours

define rushhour = (8,9,16,17,18)
define dark = [0,1,2,3,4,21,22,23]
define dawn = [5,20]
define light = (6,7,8,9,10,11,12,13,14,15,16,17,18,19)
default calander_holiday = ""

default npc_all = []
default npc_unique = []
default npc_girls = []
default npc_girls_pregnant = []
default npc_girls_whore = []




default hide_background_screen = False
define background_image_screen = ""
default timeofday = "day"










define gui.dialogue_text_outlines = [ (2, "#00000080", 0, 0) ]
define gui.name_text_outlines = [ (2, "#00000080", 0, 0) ]






default wardrobe_tutorial = False


define me = Character('Me', color="#ffffff", callback=name_callback, cb_name="pc", image="pc")
define mem = Character('Me', who_color="#ffffff", what_color='#b3b3b3', what_prefix='(-', what_suffix='-)', callback=name_callback, cb_name="pc", image="pc")
default fname = "Samantha"
default sname = "Bangtail"
default name = "Sammy"
default wname = "Doxie"
define pc = Character('[name]', color="#ffffff", callback=[dialogue_catcher_talk, name_callback], cb_name="pc", image="pc")
define pcm = Character('[name]', who_color="#ffffff", what_color='#b3b3b3', what_prefix='(-', what_suffix='-)', callback=[dialogue_catcher_think, name_callback], cb_name="pc", image="pc")
define pcg = Character('[name]', color="#ffffff",callback=[name_callback], cb_name="pc", image="pc")
define pcc = Character('[name]', color="#ffffff",callback=[dialogue_catcher_talk_end, name_callback], cb_name="pc", image="pc")
define pcmc = Character('[name]', who_color="#ffffff", what_color='#b3b3b3', what_prefix='(-', what_suffix='-)', callback=[name_callback], cb_name="pc", image="pc")
default tempname = ""
default tempname2 = ""
default tempname3 = ""

define nadia = Character('Nadia', color="#ffffff")
define nadianame = "Nadia Pallavi"

default event_end_interrupt_label = ""




define emile.name = Character('Emilie', color="#ffffff")
define sism = Character('Emilie', color="#ffffff")








define headt = Character('Head teacher', color="#ffffff")

define carlson = Character('Miss Carlson', color="#ffffff")
define oneil = Character('Mr O\'Neill', color="#ffffff")
define abbott = Character('Mr Abbott', color="#ffffff")





define swimteach = Character('Swimming coach', color="#ffffff")
define sportteach = Character('Sports coach', color="#ffffff")

define brad = Character('Brad', color="#ffffff")







define jaz = Character('Jaz', color="#ffffff")



define woman = Character('Woman', color="#ffffff")
define man = Character('Man', color="#ffffff")
define thug = Character('Thug', color="#ffffff")
define stranger = Character('Stranger', color="#ffffff")
define strangew = Character('Strange Woman', color="#ffffff")
define stranger1 = Character('Stranger 1', color="#ffffff")
define stranger2 = Character('Stranger 2', color="#ffffff")
define stranger3 = Character('Stranger 3', color="#ffffff")
define stranger4 = Character('Stranger 4', color="#ffffff")
define cuteguy = Character('Cute Guy', color="#ffffff")
define cuteboy = Character('Cute Boy', color="#ffffff")
define handsomeguy = Character('Handsome Guy', color="#ffffff")
define cutegirl = Character('Cute Girl', color="#ffffff")
define sexygirl = Character('Sexy Girl', color="#ffffff")

define girl = Character('Girl', color="#ffffff")
define girl1 = Character('Girl 1', color="#ffffff")
define girl2 = Character('Girl 2', color="#ffffff")
define guy = Character('Guy', color="#ffffff")
define guy1 = Character('Guy 1', color="#ffffff")
define guy2 = Character('Guy 2', color="#ffffff")


define patron = Character('Patron', color="#c8ffc8")
define drunk = Character('Drunk Guy', color="#ffffff")
define drunkard = Character('Drundard', color="#ffffff")
define pervert = Character('Pervert', color="#ffffff")
define handsy = Character('Handsy Man', color="#ffffff")
define lecher = Character('Lecherous Man', color="#ffffff")
define groper = Character('Groper', color="#ffffff")




define town = "Blaston"
define haven = "Haven"
define dancet = "Sweet Girls"
define school = "Name of the School"





define pc_cash = 0
define cashcard = 0












define bus_travel_time = 0
define bus_travel_loc = ""





default loc_fromfrom = []
default loc_from = []
default loc_to = ["stairwell"]
default loc_home = True
default loc_want = ""
default outside = False

default visited_park = False
default visited_market = False
default visited_highway = False
default visited_motel = False
default visited_hospital = False
default visited_trainstation = False
default visited_revel = False
default visited_lake = False
default visited_truckstop = False
default visited_checkpoint = False
default visited_industrial_area = False

default explored_park = False
default explored_commercial_area = False
default explored_residential_area = False
default explored_market = False

default unlocked_police = False
default unlocked_pub = False
default unlocked_club = False
default unlocked_strip_club = False
default unlocked_porn_studio = False
default unlocked_photostudio = False
default unlocked_perv_club = False
default unlocked_highway_homeless = False
default unlocked_highway_dealers = False
default unlocked_highway_hookers = False

default cosmetic_surgery_tutorial = True




define totalMinutes = 60
define talk_counter = "blocked"
define talk_counter_what = ""





default go_sleep_prompt = False
default late_warning = False
default late_final_warning = False
default shower_warning = False
default lust_blocker = False


define temp_var_1 = False
define temp_var_2 = False
define temp_var_3 = False
define temp_var_4 = False
define temp_var_5 = False
define temp_var_6 = False
define temp_var_7 = False
define temp_var_8 = False
define temp_var_9 = False
define temp_var_10 = False
define temp_var_11 = False
define temp_var_12 = False
define temp_var_13 = False
define temp_var_14 = False
define temp_var_15 = False
define temp_var_16 = False
define temp_var_17 = False
define temp_var_18 = False
define temp_var_19 = False




default cheat_pregnancy_enabled = True
default cheat_fetish_cumflation = False
default cheat_fetish_preg_fantasy = False
default global_pregnancy_length = 42

default global_random_number = 0

default global_random_hour_number = 0
default global_random_noon_number = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
