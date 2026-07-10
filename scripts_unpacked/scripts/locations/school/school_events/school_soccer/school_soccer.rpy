default school_soccer_quest_games_won = 0
default school_soccer_quest_hangout_prompt = False
default school_soccer_quest_play = 0
default school_soccer_quest_talk_topics = {
    
    "rain":False,
    "snow":False,
    "weekend":False,
    "beer":False,
    }
default school_soccer_quest_backentrance = {
    "shown":False,
    "used":False,
    "talk":False,
    }
default school_soccer_quest_boys_know = {
    "pub_work":False,
    "sis_home":False,
    "slut":False,
    "whore":False,
    "raped":False,
    "slave":False,
    "haven":0,
    }
default school_soccer_quest_bully_remove = {
    "asked1":False,
    "asked2":False,
    "accepted":False,
    "vanished":False,
    "vanished_field":False,
    "vanished_date":0,
    "vanished_return":False,
    }
default school_soccer_quest_bully_vanished_stage = 0

default school_soccer_quest_hangout_conv = 1
default school_soccer_quest_hangout_conv_robin = 0
default school_soccer_quest_hangout_conv_robin_sex = 0
default school_soccer_quest_betmatch = {
    "intro":False,
    "can_challenge":False,
    "match_count":0,
    "match_day":0,
    "match_total":0,
    }
default school_soccer_quest_dare_clothes = {
    "under":0,
    "topless":0,
    "nude":0
    }

default school_soccer_quest_dare_pitchsex = {
    "first":False,
    "second":False,
    "third":False,
    }
default school_soccer_quest_dare_preg_warning = False

label school_field_soccer_picker:
    if school_soccer_quest.active == 0:
        $ school_soccer_quest.activate()
        jump school_field_soccer_intro
    else:

        $ player.can_sport(mood=True, returnto="school_field_soccer_watch_sportfail")
        jump school_field_soccer_play_start

label school_field_soccer_watch_sportfail:
    pcm "I guess I could just watch them though."
label school_field_soccer_watch:
    "I decide to head over and hang out with the boys watching them play and having the odd chat whenever one of them is knocked out."
    $ loiter(20, [drake,nate,dan])
    if not school_soccer_playing():
        jump school_field_soccer_play_end_shower
    else:
        jump travel

label school_field_soccer_intro:
    $ school_soccer_quest.activate()
    $ diary_school_soccer_quest = Diary_Class("Boys playing football", "I met a group of boys today on the football field at the academy. They seem friendly enough. Looks like they play football there every day after classes and invited me to play with them. Could be a good way to make some new friends.", right_pic="diary_sideimage_activities_soccer")
    pcm "Looks like a group of boys are playing football. Doesn't look like a proper match though as they are only using one side of the field."
    if robin_here():
        show robin happy at right1 with dissolve
        robin.name "Hey [name]. Joining us?"
        pc "Join? I don't think I even know how to play."
        robin.name "Kick the ball in the goal. Nothing else to know."
        robin.name "Having another girl play would be good."
        if robin.heavy_preg:
            pc "Doesn't look like you are doing much playing."
            robin.name "Well yeah. With the belly I cant. But I can still make fun of them since they play like shit."
            pc "Ha!"
            if player.showing:
                pc "Well, not like I can play either, so I'll probably just insult them with you."
                robin.name "Great!"
        if player.showing:
            pc "Well, not like I can play anyway with this belly. Maybe I'll just watch."
            robin.name "The company would be good when someone get's eliminated."
    else:
        show drake at right1 with dissolve
        drake.name "Hey new girl. You just standing there or do you want to join?"
        $ player.face_surprised()
        pc "Huh? Me?"
        drake.name "Yes you. So..."
        $ player.face_neutral()
        pc "It's [name]."
        drake.name "Sure [name]. So, you joining in?"
        if player.showing:
            pc "With this belly, not sure I can."
            pc "What are the rules though? I can just watch."
        else:
            pc "Join? I don't think I even know how to play."
            drake.name "There is nothing to know. Kick the ball in the net."
            pc "Yeah... But what about the rules?"
        drake.name "This isn't a match and there are no teams. It's called Champion."
        drake.name "Try and score a goal. If you manage to score then you are *in* and you wait for the next round. If you are the last person on the field then you are *out* and have to wait for the match to restart."
        drake.name "Each round one person is *out* until there is only one winner left. He is the Champion."
        $ player.face_happy()
        pc "Or she!"
        drake.name "Can only be a *she* if a *she* joins. So you in? We were about to start a new match so I thought I would invite you."
        $ player.face_neutral()
        pc "Such a gentleman..."
        drake.name "Not really. It's just more fun with more people."
        if player.showing:
            pc "I think I'll just watch for now. Don't want to run around like this."
            drake.name "Sure. You can keep us company when one of us gets kicked out."
            pc "Sounds good."
        else:
            pc "Ok, but I've never played before. Is that ok?"
            drake.name "Yeah it's fine. There are no teams so if you are rubbish then you just get eliminated. No one cares."
            pc "Okay. Sounds good."
            if not "sport" in tab_top:
                drake.name "Change into something better then come and play."
            else:
                drake.name "Come and join when you want."
            pc "Okay."
    $ renpy.scene()
    with dissolve
    $ nate.meet()
    $ dan.meet()
    $ drake.meet()

    jump travel

label school_field_soccer_intro_join:
    pc "Sure, lets play."
    drake.name "Great, then lets go!"
    hide drake
    show activity_soccer
    with dissolve
    call school_field_soccer_play_normal from _call_school_field_soccer_play_normal_1
    jump school_field_soccer_play_end

label school_field_soccer_intro_reject:
    drake.name "No problem. Well we are here after school almost every day. Feel free to join if you want."
    pc "Thanks, I will."
    drake.name "See ya."
    hide drake with dissolve
    "[drake.name] runs off to join his friends and, after a brief chat, they start a new match. I watch them for a few minutes before going about my day."
    $ relax(15)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
