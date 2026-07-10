label patch_haven_endings:

    $ player.isbroken = False
    $ blood = BodyPaint()
    if main_quest_05.active > 0 and loc_to in district_haven:

        $ main_quest_05.missionvar5 = {"survive_fall":False, "hidden":False, "nohide":[23,0,1,2,3,4,5,6], "time_over":False}
        $ main_quest_05.missionvar18["burnt_building"] = False
        $ main_quest_05.missionvar18["caught_settingfire"] = False
        $ main_quest_05.missionvar18["guard_sex"] = False
        $ main_quest_05.missionvar18["guard_vsex"] = False

        $ main_quest_05.missionvar14 = {"defiance":0, "checked_door":False, "checked_bedframe":False, "checked_mattress":False, "checked_graf":False, "checked_shower":False, "checked_toilet":False, "checked_toiletpaper":False, "checked_wall":False, "checked_counter":0, "checked_done":False, "training_stage":0, "training_time":0, "training_rebel":0}

        define havguard1 = Character('Haven guard 1', color="#ffffff")
        define havguard2 = Character('Haven guard 2', color="#ffffff")
        define havguard3 = Character('Haven guard 3', color="#ffffff")
        image havguard1 = ("shadm")
        image havguard2 = ("shadm")
        define havengateguard.name = Character('Haven gate guard', color="#ffffff")
        define havenmeanguard.name = Character('Haven mean guard', color="#ffffff")

        define havguardw = Character('Haven guard', color="#ffffff")

        $ havenguardgb = Npc(fname="Haven", sname="Guard", pregname="I am carrying the child of one of the guards from Haven from when they had group sex with me.", virginname="My virginity was taken while I was passed around and gang fucked by the guards in Haven.")
        $ havengateguard = Npc(fname="Haven", sname="gate guard", pregname="I am carrying the child of the gate guard from Haven.", virginname="I gave my virginity to the gate guard in Haven.")


    $ renpy.block_rollback()
    return

label patch_post_haven:
    if main_quest_05.active == 0:
        call main_quest_05_preperation_vars from _call_main_quest_05_preperation_vars
    else:
        $ havengateguard = Npc(fname="Haven", sname="gate guard", pregname="I am carrying the child of the gate guard from Haven.", virginname="I gave my virginity to the gate guard in Haven.")
    $ player.cum_locations = {
    "cum_mouth" : 0,
    "cum_face" : 0,
    "cum_chest" : 0,
    "cum_belly" : 0,
    "cum_vagout" : 0,
    "cum_vagin" : 0,
    "cum_assout" : 0,
    "cum_assin" : 0,
    }
    $ player.cycle_conditions = {
    "length_mens" : 5,
    "length_foll" : 9,
    "length_ovulate" : 5,
    "length_lut" : 10,
    "length_no_cycle" : 28,

    "count_stage" : 0, 
    "count_cycle" : 14,

    "stage" : "mens",

    "chance_mens" : 99,
    "chance_foll" : 20,
    "chance_ovulate" : 5,
    "chance_lut" : 35,
    "chance_no_cycle" : 35, 

    "chance_base" : 1
    }
    $ t._hourcheck = 1

    $ acc.eyeliner = 1
    $ acc.eyeliner_primary_colour = "black"
    $ acc.eyeliner_secondary_colour = "black"
    $ accbak = Accessories()
    $ pub_waitress.pub_waitress_clothes()
    $ renpy.block_rollback()
    return

label patch_post_haven_update:
    if main_quest_05.active <= 1 and not loc_to in district_haven:
        call main_quest_05_preperation_vars from _call_main_quest_05_preperation_vars_2
    else:
        $ main_quest_05.missionvar4["guard_gone"] = False
    $ shop = Clothes(0, 0, 0, 0, 0, 0, 0, 0, 0)
    $ shop.outfit_colours("crimson","pink","crimson","pink","crimson","pink","crimson","pink","crimson","pink","crimson","pink","pink","crimson")
    return

label patch_school_update:
    $ school_soccer_quest = QuestClass()
    $ school_dance_quest = QuestClass()
    $ school_bully_quest = QuestClass()


    $ c._slutty = False
    $ school._slutty = False
    $ daily._slutty = False
    $ party._slutty = False
    $ sport._slutty = False
    $ swim._slutty = False
    $ home._slutty = False
    $ work._slutty = False
    $ shop._slutty = False




    $ svet = Npc(fname="Svetlana", sname="Makarava", nname="Svet")
    $ rachel = Npc(fname="Rachel", sname="Taylor")
    $ anabel = Npc(fname="Anabel", sname="Desmond")
    $ dani = Npc(fname="Danielle", sname="Rabel", nname="Dani")

    $ drake = Npc(fname="Drake", sname="Singer")
    $ nate = Npc(fname="Nate", sname="Taylor")
    $ dan = Npc(fname="Dan", sname="Bloom")

    $ shane = Npc(fname="Shane", sname="Simmons")
    $ marcus = Npc(fname="Marcus", sname="Andal")
    $ josh = Npc(fname="Josh", sname="Orich")


    $ player.hair_style = "loose"
    $ player.hair_style_default = "loose"

    $ player.soldrequest = 0
    $ schoolguy = Npc(fname="Guy from school", pregname="I am carrying the child of some random guy from school", virginname="some random guy from school")

    if player.hair_neck == 5:
        $ player.hair_neck = 3
    if loc_to in district_haven:
        $ player.hair_style = "haven"


    return

label patch_school_pt2_update:

    $ school_newfriend_quest = QuestClass()
    $ school_photo_quest = QuestClass()
    $ writing = BodyPaint()
    $ class_updater(Npc,("vsex","preg","hand"), 0)
    $ class_updater(BodyPaint,("forehead","special","pubic","anus"), 0)
    $ player.rainbow = 0
    $ class_updater(QuestClass,("vsex","creamed","preg","sold", "hand"), 0)
    $ c.pokenips_check()

    $ c.shirt_body = 1
    $ c.shirt_collar = 1

    $ felix = Npc(fname="Felix", sname="Vincenzo")
    $ class_updater(Clothes,("cansee_breasts","cansee_vagina","cansee_ass","cansee_bra","cansee_pants","clothed","underwear","nude"), False)
    $ player.preg_father_class = nosex
    $ class_updater(Npc,("vvirgin_know","preg_current","preg_knows"), False)
    $ player.want_pullout = True
    $ player.have_pullout = True
    return

label patch_school_pt3_update:
    if game_version < "0.2.35.08":
        $ class_updater(Npc,("seen_breasts", "seen_vagina","seen_ass"), False)

    if game_version < "0.2.35.10":
        $ class_updater(Npc,("_nname", "_skinbase","_skinshad"), "")

        $ shane._skinbase=(0.901, 0.666, 0.572)
        $ shane._skinshad=(0.831, 0.537, 0.454)
        $ marcus._skinbase=(0.752, 0.607, 0.549)
        $ marcus._skinshad=(0.682, 0.498, 0.447)

        $ drake._skinbase = (0.929, 0.756, 0.670)
        $ drake._skinshad = (0.886, 0.611, 0.498)

        $ nate._skinbase = (0.901, 0.666, 0.576)
        $ nate._skinshad = (0.827, 0.537, 0.458)

        $ dan._skinbase = (0.929, 0.725, 0.670)
        $ dan._skinshad = (0.705, 0.537, 0.478)
    if game_version < "0.2.35.14":
        $ player.cum_locations['cum_hand'] = 0
    if game_version < "0.2.35.15":
        $ shanewhore = Npc(fname="Shane", sname="Simmons", pregname="I am carrying the child of someone who had sex with me while [shane.name] was selling me.", virginname="some guy who paid [shane.name] to make me have sex with him.")

    if game_version < "0.2.35.16":
        $ class_updater(Npc,("is_female","is_pregnant", "iswhore"), False)
        $ cass = Npc(fname="Cassidy", sname="O'Reilly", nname="Cass", is_female=True)
        $ mira = Npc(fname="Mira", sname="Bhatti", is_female=True, iswhore=True)
        $ punter = Npc(fname="Punter", sname="", pregname="I am carrying the child of one of some punter", virginname="some random punter")
        $ lover = Npc(fname="Lover", pregname="")

        $ (svet.is_female, dani.is_female, anabel.is_female, rachel.is_female, emile.is_female, betty.is_female) = (True, True, True, True, True, True)
        $ player.beingraped = False

        $ class_list_creator(Npc, "npc_all")
        $ class_list_creator(Npc, "npc_girls", "is_female", True)
        $ class_list_creator(Npc, "npc_girls_whore", "iswhore", True)

        python:
            for i in npc_girls:
                i.pregnant_who = ""
                i.days_pregnant = 0
                i.sex_who = {}

    if game_version < "0.2.35.19":
        python:
            for i in npc_all:
                i._cum_last = 0
    if game_version < "0.2.35.22":
        python:
            for i in npc_all:
                i.active = True
                i.conversation_topics = []
    if game_version < "0.2.35.23":
        if school_dance_quest_show_count:
            $ school_dance_quest.activate()

    if game_version < "0.2.35.24":
        $ player.mood_queue = []

    if game_version < "0.2.35.28":
        $ player._desire = 0.0
        $ player._tired = 80.0
        $ player._mood = 80.0
        $ player._confidence = 35.0
        $ player._fitness = 35.0
        $ player._int = 15.0
        $ player._allure = 0.0
        $ player._drunk = 0.0
        $ player._high = 0.0
    if game_version < "0.2.35.30":
        python:
            for i in npc_girls:
                if i.pregnant_who == "":
                    i.pregnant_who = nosex
    if game_version < "0.2.35.31":
        python:
            for i in npc_all:
                i.last_spoke_to = 0

    if game_version < "0.2.35.31":
        $ class_updater(QuestClass,("conversation_topics", "list","dict"), [])

    if game_version < "0.2.35.37":
        $ fix_clothes()

    if game_version < "0.2.35.38":
        python:
            for i in npc_all:
                i.iswhore = False
                if i in npc_girls_whore:
                    i.iswhore = True

    if game_version < "0.2.35.39":
        $ parkpervert_dani = Npc(fname="Pervert", sname="", pregname="I am carrying the child of a pervert in the park who I let fuck me in the bushes", virginname="some random pervert who fucked me in the bushes")

    if game_version < "0.2.35.40":
        $ temp_outfit = Clothes(0, 0, 0, 0, 0, 0, 0, 0, 0)
    if game_version < "0.2.35.41":
        $ busgroper = Npc(fname="Bus", sname="groper", pregname="I am carrying the child of a pervert from the bus", virginname="some random pervert who I let fuck me on the bus")
    if game_version < "0.2.35.42":
        $ class_updater(BodyPaint,"ass_counter", 0)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
