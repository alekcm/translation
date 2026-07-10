init python:
    def school_dance_lunch_can_trigger():
        if school_dance_quest.isactive and school_dance_quest_show_count > 1:
            return True 
        else:
            return False

    def school_soccer_lunch_can_trigger():
        if school_soccer_quest.active and all([drake.isactive, nate.isactive, dan.isactive]):
            return True
        else:
            return False

define feminism = Character('Women\'s Studies', color="#ffffff")
define econ = Character('Economics', color="#ffffff")
define history = Character('Plague History', color="#ffffff")
define geog = Character('[town] Geography', color="#ffffff")

default school_plague_history = 0
default school_women_history = 0
default school_econ_history = 0
default school_geography = 0



label school_class_picker:
    if not "school" in tab_top and player.confidence < 60:
        if school.inappropriate == False:
            pcm "I had better change into my school uniform before heading to class."
            $ pc_dress_event("school", [loc_school_hallway, loc_school_gym, loc_school_locker_girls], [loc_school_gym, loc_school_hallway])
        else:
            pcm "I don't have my school uniform on so I might end up in trouble. What should I do?"
            menu:
                "Go to into the school anyway":
                    $ player.add_mood(-10)
                "Go home to change":
                    jump travel


    if school_day == 0 and t.day == 3:
        jump school_class_first_day
    elif school_day == 0:
        jump school_class_first_day_missed
    elif school_day >= 1 and school_met_friend == False:
        jump school_class_meet_friend
    else:
        jump school_class_morning

label school_class_morning_arrive:
    if loc(loc_school_classroom):
        return
    if t.hour == 8:
        $ dialouge = renpy.random.choice([
        "I am early for class but might as well head to the classroom.",
        "I am a bit early for class but might as well go to the classroom and study.",
        "Might as well study before my classes start.",
        "Classes haven't started yet but suppose I might as well hang out in the classroom."
        ])
    elif t.hour == 9:
        $ dialouge = renpy.random.choice([
        "Better head straight to my classroom.",
        "I had better make my way to my classroom",
        "I should head straight to class.",
        ])
    else:
        $ dialouge = renpy.random.choice([
        "I'm late. Better be quiet and not disturb anyone.",
        "Hurry hurry hurry...",
        "Fuck I'm running late.",
        ])
    pcm "[dialouge]"
    pause 0.5
    return

label school_class_morning:
    call school_class_morning_arrive from _call_school_class_morning_arrive_1

    $ walk(loc_school_classroom, trans=False)
    if t.hour in (8,9):
        jump school_class_normal
    else:
        with dissolve
        jump school_class_lesson_picker





label school_class_normal:
    $ rand_choice = WeightedChoice([
    ("school_class_normal_cassmira_1", If (cass.isactive and mira.isactive and not "hospitalised" in mira.list,100,0)), 
    ("school_class_normal_cassmira_2", If (cass.isactive and mira.isactive and not "hospitalised" in mira.list,100,0)), 
    ("school_class_normal_cassmira_3", If (cass.isactive and mira.isactive and not "hospitalised" in mira.list,100,0)), 
    ("school_class_normal_cassmira_4", If (cass.isactive and mira.isactive and not "hospitalised" in mira.list,100,0)), 
    ("school_class_normal_cassmira_5", If (cass.isactive and mira.isactive and not "hospitalised" in mira.list,100,0)), 
    ("school_class_normal_cassmira_6", If (cass.isactive and mira.isactive and not "hospitalised" in mira.list and school_bully_quest_bully_cass_target and not shane.dead,100,0)), 
    ("school_class_normal_cassmira_7", If (cass.isactive and mira.isactive and not "hospitalised" in mira.list,100,0)), 
    ("school_class_normal_cassmira_8", If (cass.isactive and mira.isactive and not "hospitalised" in mira.list,player.allure,0)), 
    ("school_class_normal_cassmira_9", If (cass.isactive and mira.isactive and not "hospitalised" in mira.list,100,0)), 
    ("school_class_normal_cassmira_10", If (cass.isactive and mira.isactive and not "hospitalised" in mira.list and weather_var > 2,100,0)), 
    ("school_class_normal_cassmira_11", If (cass.isactive and mira.isactive and not "hospitalised" in mira.list and "rape" in cass.conversation_topics,500,0)), 
    ("school_class_normal_cassmira_12", If (cass.isactive and mira.isactive and not "hospitalised" in mira.list and "lover" in cass.conversation_topics,500,0)), 
    ("school_class_normal_cassmira_13", If (cass.isactive and mira.isactive and not "hospitalised" in mira.list and "pregnant" in cass.conversation_topics and not cass.showing,1000,0)), 

    ("school_class_normal_nomira_1", If (cass.isactive and not mira.isactive,100,0)),

    ("school_class_normal_nocass_1", If (mira.isactive and not "hospitalised" in mira.list and not cass.isactive,100,0)),
    ("school_class_normal_nocass_2", If (mira.isactive and not "hospitalised" in mira.list and not cass.isactive,100,0)),
    ("school_class_normal_nocass_3", If (mira.isactive and not "hospitalised" in mira.list and not cass.isactive,100,0)),

    ("school_class_normal_soccerboys_1", If (school_soccer_lunch_can_trigger(),nate.lust,0)), 
    ("school_class_normal_soccerboys_2", If (school_soccer_lunch_can_trigger(),100,0)), 
    ("school_class_normal_soccerboys_3", If (school_soccer_lunch_can_trigger() and cass.isactive,100,0)), 
    ("school_class_normal_soccerboys_4", If (school_soccer_lunch_can_trigger(),100,0)), 
    ("school_class_normal_soccerboys_5", If (school_soccer_lunch_can_trigger(),100,0)), 
    ("school_class_normal_soccerboys_6", If (school_soccer_lunch_can_trigger() and drake.sex,drake.lust,0)), 
    ("school_class_normal_soccerboys_7", If (school_soccer_lunch_can_trigger(),100,0)), 
    ("school_class_normal_soccerboys_8", If (school_soccer_lunch_can_trigger(),100,0)), 
    ("school_class_normal_soccerboys_9", If (school_soccer_lunch_can_trigger(),100,0)), 
    ("school_class_normal_soccerboys_10", If (school_soccer_lunch_can_trigger(),100,0)), 

    ("school_class_normal_svetrachel_1", If (school_dance_lunch_can_trigger(),100,0)), 
    ("school_class_normal_svetrachel_2", If (school_dance_lunch_can_trigger(),100,0)), 
    ("school_class_normal_svetrachel_3", If (school_dance_lunch_can_trigger(),100,0)), 
    ("school_class_normal_svetrachel_4", If (school_dance_lunch_can_trigger(),100,0)), 
    ("school_class_normal_svetrachel_5", If (school_dance_lunch_can_trigger() and player.isslut, player.desire * 1.5, 0)), 
    ("school_class_normal_svetrachel_6", If (school_dance_lunch_can_trigger() and not rachel.showing,100,0)), 
    ("school_class_normal_svetrachel_7", If (school_dance_lunch_can_trigger() and weather_var > 2 and player.isslut,300,0)), 
    ("school_class_normal_svetrachel_8", If (school_dance_lunch_can_trigger() and "rape" in rachel.conversation_topics,500,0)), 
    ("school_class_normal_svetrachel_9", If (school_dance_lunch_can_trigger() and "pregnant" in rachel.conversation_topics and not rachel.showing,1000,0)), 
    ("school_class_normal_svetrachel_10", If (school_dance_lunch_can_trigger() and "lover" in rachel.conversation_topics,200,0)), 
    ("school_class_normal_svetrachel_11", If (school_dance_lunch_can_trigger() and "lover" in rachel.conversation_topics,200,0)), 
    ("school_class_normal_svetrachel_12", If (school_dance_lunch_can_trigger() and player.allure > 100,player.allure,0)), 

    ("school_class_normal_anabeldani_1", If (school_dance_lunch_can_trigger() and anabel.isactive and not (anabel.hate or dani.hate),100,0)), 
    ("school_class_normal_anabeldani_2", If (school_dance_lunch_can_trigger() and anabel.isactive and not (anabel.hate or dani.hate),100,0)), 
    ("school_class_normal_anabeldani_3", If (school_dance_lunch_can_trigger() and anabel.isactive and not (anabel.hate or dani.hate),100,0)), 
    ("school_class_normal_anabeldani_4", If (school_dance_lunch_can_trigger() and anabel.isactive and not (anabel.hate or dani.hate),100,0)), 
    ("school_class_normal_anabeldani_5", If (school_dance_lunch_can_trigger() and anabel.isactive and not (anabel.hate or dani.hate),100,0)), 
    ("school_class_normal_anabeldani_6", If (school_dance_lunch_can_trigger() and anabel.isactive and not (anabel.hate or dani.hate) and player.allure>100,player.allure,0)), 
    ("school_class_normal_anabeldani_7", If (school_dance_lunch_can_trigger() and anabel.isactive and not (anabel.hate or dani.hate) and weather_var > 2,300,0)), 
    ("school_class_normal_anabeldani_8", If (school_dance_lunch_can_trigger() and anabel.isactive and not (anabel.hate or dani.hate) and weather_var > 2,300,0)), 
    ("school_class_normal_anabeldani_9", If (school_dance_lunch_can_trigger() and anabel.isactive and not (anabel.hate or dani.hate) and "rape" in dani.conversation_topics,500,0)), 
    ("school_class_normal_anabeldani_10", If (school_dance_lunch_can_trigger() and anabel.isactive and not (anabel.hate or dani.hate) and "rape" in dani.conversation_topics,500,0)), 

    

    ("school_class_normal_felix_1", If (school_photo_quest.isactive and school_photo_intro_quest_complete and felix.isactive,50,0)),
    ("school_class_normal_felix_2", If (school_photo_quest.isactive and school_photo_intro_quest_complete and felix.isactive,50,0)),
    ("school_class_normal_felix_3", If (school_photo_quest.isactive and school_photo_intro_quest_complete and felix.isactive,50,0)),
    ("school_class_normal_felix_4", If (school_photo_quest.isactive and school_photo_intro_quest_complete and felix.isactive,50,0)),


    ("school_class_normal_dani_postdance", If (dani.isactive and "dance_went_alone" in dani.conversation_topics and school_dance_quest_show_count == 9,10000,0)), 


    ])
    jump expression rand_choice





label school_class_normal_end:
    $ player.add_mood(5)
    if t.hour == 8:
        $ relax(60 - t.minute)
    else:
        $ relax(15)
    $ renpy.scene()
    with dissolve
    pcm "Looks like class is starting."
    jump school_class_lesson_picker

label school_class_lesson_picker:
    $ rand_choice = WeightedChoice([
    ("school_plague_history" + str(school_plague_history), If (renpy.has_label("school_plague_history" + str(school_plague_history)),100,0)),
    ("school_women_history" + str(school_women_history), If (renpy.has_label("school_women_history" + str(school_women_history)),100,0)),
    ("school_econ_history" + str(school_econ_history), If (renpy.has_label("school_econ_history" + str(school_econ_history)),100,0)),
    ("school_geography_picker", 100),
    ("school_class_generic_tired", (100 - player.tired)),
    ("school_class_generic_mood", (100 - player.mood)),
    ("school_class_generic_desire", player.check_horny()),
    ("school_class_generic_allure", player.allure / 4),  
    ])
    jump expression rand_choice

label school_class_lesson_end:
    pause 0.5
    $ school_morning()
    $ dialogue = WeightedChoice([
    ("Class is over and I am starving.", If (player.hunger < 40,1,0)),
    ("Ah class is over. I was falling asleep in there.", If (player.tired < 35,1,0)),
    ("Well, that's class over.", 1),
    ("Hmm, that's class done with.", 1),
    ])
    pcm "[dialogue]"
    pause 0.5
    $ walk(loc_school_hallway)
    $ dialogue = WeightedChoice([
    ("Lunch time!", If (player.hunger < 40,1,0)),
    ("Phew. Can relax at last on my lunch break.", If (player.tired < 35,1,0)),
    ("About time the lunch break came.", 1),
    ])
    pcm "[dialogue]"
    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
