init python:
    def shower_scene(outfit="none", hair="none", say_what="I have a shower."):
        
        shower_scene_start(outfit, hair)
        shower_scene_wash(say_what)
        shower_scene_end(outfit, hair)

    def shower_scene_start(outfit="daily", hair="none"): 
        pc_strip_tops()
        acc_shower()
        renpy.pause(0.5)
        pc_strip()
        if not player.hair_style == "haven":
            player.hair_style = "loose"
        renpy.pause(0.5)
        if loc_cur in (loc_school_locker_boys, loc_school_locker_girls, loc_school_locker_old):
            walk(loc_school_locker_shower)
            renpy.pause(0.5)

    def shower_scene_wash(say_what="I have a shower."): 
        
        renpy.scene()
        renpy.show(renpy.random.choice(["shower", "shower_back"]))  
        renpy.with_statement(dissolve)
        player.shower()
        _window_show(auto=True)
        
        if say_what:
            renpy.say(None,say_what)
        renpy.scene()
        renpy.with_statement(dissolve)

    def shower_scene_end(outfit="daily", hair="none"):
        if loc_cur.get_district() == dis_home:
            outfit = "home"
        if loc_cur == loc_school_locker_shower:
            walk(loc_from)
            renpy.pause(0.5)
        pc_dress_slow(outfit)
        acc_shower_dress()
        if not player.hair_style == "haven":
            player.set_hair(hair)
        if makeup_shower_toggle and not acc.makeup_on:
            acc.makeup_on = True
            renpy.say(None,"I apply some makeup.")
            relax(15)

label shower_scene:
    call shower_scene_start from _call_shower_scene_start
    call shower_scene_wash from _call_shower_scene_wash
    call shower_scene_end from _call_shower_scene_end
    return

label shower_scene_start:
    $ pc_strip_tops()
    $ acc_shower()
    pause 0.5
    $ pc_strip()
    if not player.hair_style == "haven":
        $ player.hair_style = "loose"
    pause 0.5
    if loc_cur in (loc_school_locker_boys, loc_school_locker_girls, loc_school_locker_old):
        $ walk(loc_school_locker_shower)
        pause 0.5


    return

label shower_scene_wash:
    $ renpy.show(renpy.random.choice(["shower", "shower_back"]))
    $ renpy.with_statement(dissolve)
    $ player.shower()
    if loc_cur == loc_school_locker_shower and loc_from == loc_school_locker_girls and school_people_present():
        call random_event_school_girls_shower from _call_random_event_school_girls_shower
    elif loc_cur == loc_school_locker_shower and loc_cur == loc_school_locker_old:
        jump random_event_school_old_shower
    else:
        "I have a shower."

    $ renpy.hide("shower")
    $ renpy.hide("shower_back")
    $ renpy.with_statement(dissolve)
    return

label shower_scene_end:
    if loc(loc_school_locker_shower):
        $ walk(loc_from)
        pause 0.5
    if loc_cur.home_location or dis(dis_home):
        $ pc_dress_quick("home")
    elif loc_from == loc_motel_pinkroom or loc(loc_motel_pinkroom):
        $ pc_set_temp_outfit()
    else:
        if t.timeofday == "night":
            $ pc_dress_quick("party")
        else:
            $ pc_dress_quick("daily")
    $ acc_shower_dress()

    if not player.hair_style == "haven":
        $ player.set_hair()
    if makeup_shower_toggle and not acc.makeup_on:
        $ acc.makeup_on = True
        "I apply some makeup."
        $ relax(15)
    return

label makeup_apply:
    if acc.makeup_on == False:
        $ acc.makeup_on = True
        "I apply some makeup."
        $ relax(15)
    else:
        $ acc.makeup_on = False
        "I wash the makeup from my face."
        $ relax(15)

    jump travel

label makeup_apply_call:
    if makeup_shower_toggle and not acc.makeup_on:
        $ acc.makeup_on = True
        "I apply some makeup."
        $ relax(15)
    return

label shower_event:
    call shower_scene_start from _call_shower_scene_start_1
    call shower_scene_wash from _call_shower_scene_wash_1
    call shower_scene_end from _call_shower_scene_end_1
    jump travel

label shower_event_call:
    call shower_scene_start from _call_shower_scene_start_2
    call shower_scene_wash from _call_shower_scene_wash_2
    call shower_scene_end from _call_shower_scene_end_2
    return

label hair_event:
    if player.hair_neck == 1:
        pc "My hair is too short to style."
    elif "sport" in tab_top:
        pc "I prefer it up while exercising so it doesn't get in my face."
    elif "home" in tab_top:
        pc "I don't want to have my hair up while I am at home relaxing."
    elif "swim" in tab_top:
        pc "My hair will get all over the place and stick to my face if I don't have it tied up."
    jump travel

define makeup_shower_toggle = False
label makeup_toggle_shower_event_set:
    if makeup_shower_toggle:
        pcm "Guess I will stop putting makeup on after the shower."
    else:
        pcm "I should put makeup on after I have a shower."
    $ makeup_shower_toggle = not makeup_shower_toggle
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
