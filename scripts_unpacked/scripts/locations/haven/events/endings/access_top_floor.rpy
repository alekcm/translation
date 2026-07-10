init python:
    def haven_nohide():
        if ("flooded" in main_quest_05.list or "set_fire" in main_quest_05.list) and "hidden" in main_quest_05.list and haven_time_nohide():
            return True
        elif not ("flooded" in main_quest_05.list or "set_fire" in main_quest_05.list) and haven_time_nohide():
            return True
        else:
            return False

screen haven_hallway_3f_screen():
    zorder 1
    if t.hour == 5 or t.hour == 20:
        $ timeofday = "dawn"
    elif t.hour > 20 or t.hour < 5:
        $ timeofday = "night"
    else:
        $ timeofday = "day"


    if not temp_var_10:
        imagebutton auto ("bg_haven_hallway_3f_doorblocked_layer_%s") focus_mask True action Jump ("haven_access_top_floor_doorblocked")
    imagebutton auto ("bg_haven_hallway_3f_doorguard_layer_%s") focus_mask True action Jump ("haven_access_top_floor_doorguard")
    imagebutton auto ("bg_haven_hallway_3f_doormain_layer_%s") focus_mask True action Jump ("haven_access_top_floor_doormain")
    if not temp_var_11:
        imagebutton auto ("bg_haven_hallway_3f_hole_layer_%s") focus_mask True action Jump ("haven_access_top_floor_hole")
    imagebutton auto ("bg_haven_hallway_3f_vent_layer_%s") focus_mask True action Jump ("haven_access_top_floor_vent")
    if not temp_var_12:
        imagebutton auto ("bg_haven_hallway_3f_woodjunk_layer_%s") focus_mask True action Jump ("haven_access_top_floor_woodjunk")



label haven_access_top_floor:

    $ walk(loc_haven_toplanding)
    $ player.face_worried()
    $ log.markdone("mq_05_guard")
    pcm "..."
    pcm "Ok... I managed to get up here, but now what?"
    pcm "Need to find [alex.name] and ask him where [ant.name] is. Doubt he would take too kindly to me just walking up and asking."

    if "flooded" in main_quest_05.list:
        pcm "Especially not after I just flooded his building. He doesn't know it was me but he might figure it out."
    elif "set_fire" in main_quest_05.list:
        pcm "Especially not after I just set fire to his building. He doesn't know it was me but he might figure it out."
    else:
        pcm "At least I haven't done anything so far to piss him off though. He might be a bit more open to communication than if I had."

    pcm "Ok, looks like the floor layout is the same as the ones below. So I am guessing his office will be off the hallway."
    $ walk(loc_haven_hallway_3f)
    pcm "Yes! It's the same. Somewhat..."
    pcm "Ok. Where do I go?"
    if "flooded" in main_quest_05.list or "set_fire" in main_quest_05.list:
        pcm "Huh?"
        if "flooded" in main_quest_05.list:
            havmuff "...the entire first floor. Getting the pipe blocked now but s'gonna take a while to..."
        elif "set_fire" in main_quest_05.list:
            havmuff "...from the showers in buckets. Need to make sure there's no flare up though so we are..."
        pcm "Those voices are coming from the room at the end of the hall. Sounds like they are telling someone what is going on downstairs."
        pcm "That has got to be [alex.fname] [alex.sname] they are talking to. So his office is at the end of the hall."
    else:
        if player.int >= 40:
            pcm "Judging by the layout of the lower floors, it is likely that [alex.fname] [alex.sname]'s office is at the end of the hall there."

    pcm "Think I have only two choices. Find somewhere to hide out until night time and try to catch [alex.fname] [alex.sname] while the place is a graveyard."
    pcm "Or I just head to him right now and hope he is reasonable or that I can convince him."
    if "flooded" in main_quest_05.list:
        pcm "Considering I flooded his building, the chance of him being reasonable is slim..."
    elif "set_fire" in main_quest_05.list:
        pcm "Considering I set fire to his building, the chance of him being reasonable is slim..."
    if "flooded" in main_quest_05.list or "set_fire" in main_quest_05.list:
        pcm "But better hurry and decide. Won't be long until someone comes here and sees me."
    $ reset_temp_vars()
    $ temp_var_1 = 0

label haven_access_top_floor_choices:
    if not "hidden" in main_quest_05.list and temp_var_1 >= 3 and ("flooded" in main_quest_05.list or "set_fire" in main_quest_05.list):
        pcm "Fuck, took too long... I can hear them coming over."
        pcm "What do I do what do I do..."
        show haven_guard2 at right1 with hpunch
        havguard "Hey! The fuck are you doing up here?"
        pc "Err..."
        havguard "Come 'ere!"
        jump haven_caught_and_beaten
    call screen haven_hallway_3f_screen

label haven_access_top_floor_doorblocked:
    $ temp_var_1 += 1
    $ temp_var_10 = True
    if "hidden" in main_quest_05.list:
        pcm "No need to worry about what's in there"
    else:
        pcm "Might be able to get in there if I pull the wood off. But it's pointless since I don't have the time and I couldn't put the wood back to stay hidden."
    jump haven_access_top_floor_choices

label haven_access_top_floor_doorguard:
    $ temp_var_1 += 1
    if haven_nohide():
        pcm "Hmmm..."
        pcm "Without even having to go inside, I can tell this probably isn't the right room."
        pcm "With all the snoring going on inside, this is probably where the guards sleep. I can't imagine the boss bunking with the hired help."
        jump haven_access_top_floor_choices

    if "flooded" in main_quest_05.list or "set_fire" in main_quest_05.list:
        pcm "Hmmm, looks like the guards sleep in here. Not a good place to be hiding out."
        if temp_var_1 >= 3:
            $ player.face_worried()
            pcm "Fuck, I can hear people coming. Shit shit!"
            pcm "No choice but to hide in here anyway."
            $ walk(loc_haven_guardroom)
            $ player.face_worried()
            pcm "Errr..."
            pcm "Under the bed..."
            jump haven_access_top_floor_choices_guardroom_hide
        else:
            pcm "Probably best I find somewhere else to hide."
            jump haven_access_top_floor_choices
    else:
        $ walk(loc_haven_guardroom)
        pcm "Fuck! Its's packed in here. Better leave before someone..."
        show haven_guard2 at right1 with dissolve
        havguard "Hey!"
        pcm "Fuck!"
        havguard "Don't just stand there with the door open letting all the cold in. Get your arse in here."
        havguard "Hold on, what you doin 'ere anyway? Who let you up here?"
        if player.has_perk([perk_sucu], notif=True):
            $ player.face_happy()
            pc "Room full of burly men and little old me? Take a guess."
            $ player.face_neutral()
            havguard "Err..."
            havguard "Ok... Nice."
            havguard "Come in come in."
            $ havguardw = Character('Haven guard', color="#ffffff")
            jump haven_whore_ending_catcher

        elif player.has_perk([perk_whore, perk_slut, perk_gamine], notif=True) or player.check_sex_agree(4):
            pcm "Damn, I am not getting out of this situation very easily..."
            menu:
                "Pretend to be a whore":
                    $ player.face_happy()
                    pc "I thought I was expected. I was asked to come here to help relieve stress."
                    if not player.iswhore:
                        pcm "Damn. Sounding like an actual whore saying that."
                    $ player.face_neutral()
                    havguard "Err..."
                    havguard "Ok... Nice."
                    havguard "Come in come in."
                    $ havguardw = Character('Haven guard', color="#ffffff")
                    jump haven_whore_ending_catcher
                "Get out of here":

                    $ NullAction()

        pc "Err, I got lost..."
        hide haven_guard2
        $ walk(loc_haven_hallway_3f)
        "I turn around and quickly leave, but have absolutely nowhere to go."
        pcm "Fuck what do I do..."
        pcm "Gate downstairs is locked. Only chance is the ho..."
        "Before I can even contemplate fully what to do, I am grabbed by the guard and pushed to the floor."
        show haven_guard2 at right5 with hpunch
        $ player.punch()
        jump haven_caught_and_beaten


label haven_access_top_floor_doormain:
    $ temp_var_1 += 1
    if haven_nohide():
        jump haven_access_top_floor_night_office

    elif player.int >= 40:
        pcm "This is no doubt [alex.fname] [alex.sname]'s office. Do I really want to just be strolling right in?"
        menu:
            "Yes, go right in":
                jump haven_access_top_floor_day_office_enter
            "No, look for another option":

                jump haven_access_top_floor_choices
    else:
        pcm "Let's have a look..."
        jump haven_access_top_floor_day_office_enter


label haven_access_top_floor_hole:
    $ temp_var_1 += 1
    $ temp_var_11 = True
    if t.hour in dark:
        pcm "Just blackness out there. I can't see a thing."
    else:
        pcm "Pretty high up..."
        pcm "Not that I would like to, but in case of an emergency, I could survive the fall. Doubt I will be walking away from it afterwards though."
        $ add_to_list(main_quest_05.list, "survive_fall")
    jump haven_access_top_floor_choices

label haven_access_top_floor_vent:
    $ temp_var_1 += 1
    if haven_nohide():
        pcm "A vent to the other room. Not something I need to be dealing with right now."
        jump haven_access_top_floor_choices
    elif inv.qty(item_haven_crowbar):
        if havenvent.vsex > 0:
            $ player.face_angry()
            pcm "No fucking chance! Not after last time!"
            jump haven_access_top_floor_choices
        else:
            pcm "Might be able to use this tool to pry the vent and squeeze into that blocked off room to wait. Will take me some time to do it though so better be quick."
            menu:
                "Pry the vent.":
                    jump haven_access_top_floor_choices_vent

                    "There will be a fitness check and you will try and pry the vent. Too many failures will get you caught but it should be somewhat easy to do."
                "Look for another option":
                    jump haven_access_top_floor_choices
    else:
        pcm "Looks like it leads into the blocked off room there. But not a lot I can do with my bare hands."
        jump haven_access_top_floor_choices

label haven_access_top_floor_woodjunk:
    $ temp_var_1 += 1
    $ temp_var_12 = True
    pcm "Just some junk, probably for repairs. Doesn't look like there is anything here that can help me."
    jump haven_access_top_floor_choices



label haven_access_top_floor_choices_guardroom_hide:
    show haven_underbed at right with dissolve
    pcm "Fuck, this is not a good place to be hiding."
    pcm "What the hell am I going to do? Going to end up stuck under here at this rate."
    pcm "Ugh, no choice but to stay hidden until I am able to sneak out and try to see [alex.fname] [alex.sname]..."
    jump haven_access_top_floor_choices_guardroom_hide_repeat

label haven_access_top_floor_choices_guardroom_hide_repeat:
    $ working(60)
    if player.check_fight(2, can_spray=False, notif=False):
        if haven_time_nohide():
            pcm "Ok... These guys have been snoring for a bit already so now might be a good time to try and sneak out of here."
            hide haven_underbed with dissolve
            pcm "Quietly..."
            $ walk(loc_haven_hallway_3f)
            pcm "Almost..."
            pcm "..."
            pcm "Ok, no one seems to have noticed me. So now I guess I should try and meet [alex.fname] [alex.sname]."
            $ add_to_list(main_quest_05.list, "hidden")
            jump haven_access_top_floor_night_office
        else:
            $ dialouge = renpy.random.choice([
            "Come on...",
            "Just a little longer...",
            "A bit more...",
            "Don't get caught now...",
            ])
            pcm "[dialouge]"
            jump haven_access_top_floor_choices_guardroom_hide_repeat
    else:
        $ havguardw = Character('Haven guard', color="#ffffff")
        havguard "Huh?"
        havguard "Why is there someone hiding under your bed?"
        pcm "FUCK FUCK FUCK!!"
        hide haven_underbed with hpunch
        "I try to rush out from under the bed and make a run for it but as I crawl out I feel a foot press on my back."
        pc "Ung! Get off!"
        havguard "What the hell you doing here?"
        if c.exposed:
            havguard "And why are you naked?"
        havguard "Who has been sneaking whores in here guys? You can't just leave them lying around up here!"
        pc "Wait what? No sorry I didn't mean..."
        $ player.punch()
        havguard "Shut up! How did you get up here anyway? Who let you in?"
        pc "No stop don't!"
        havguard "Well, no point in sending you down just yet I suppose. Might as well put you to use."
        pc "What?"
        pcm "Fuck! They want to use me..."
        if not player.check_nowill:

            menu:
                "Try to run away":
                    pcm "Need to get out of here..."
                    with hpunch
                    pcm "Nnng."
                    with hpunch
                    pc "Fuck."
                    havguard "Stop that."
                    $ player.punch()
                    pc "Ahhh!"
                    with hpunch
                    havguard "Stop!"
                    jump haven_caught_and_beaten
                "Don't resist":

                    $ NullAction()

        pcm "..."
        pcm "*SOB*"
        pcm "I have no choice..."
        jump haven_whore_ending

label haven_access_top_floor_choices_vent:
    pcm "Ok... Let's give this a go."
    with vpunch
    show haven_vent at right2 with dissolve
    pcm "Quick before I get caught."
    pcm "Uff! Come on... Get in..."
    $ walk(loc_haven_ventroom)
    pcm "Yes!"
    hide haven_vent with dissolve
    pcm "Ok... now I just hide out here and wait."
    if haven_time_nohide():
        pcm "Better hang out here for a couple of hours until things calm down, then head on out while people are sleeping."
        "I hang around in the darkness trying to keep as silent as possible while listening out for anything going on outside."
        $ working(120)
    else:
        pcm "Ok, now just to wait until things are quiet and most people in this place are sleeping."
        "I hang around in the darkness trying to keep as silent as possible while listening out for anything going on outside."
        $ time_working_to(1,12)
    pcm "..."
    if player.tired < 10:
        pcm "Uff, so tired..."
    pcm "Not heard anything going on outside for ages and it has been night time for quite a while. Now might be a good time to get out of here and confront [alex.fname] [alex.sname]."
    show haven_vent at right2 with dissolve
    pcm "Hup, here we go..."
    $ walk(loc_haven_hallway_3f)
    hide haven_vent with dissolve
    if player.int >= 40:
        pcm "Ok, his office seems like the one at the end of the hall. Hope that's also where he sleeps"
    else:
        pcm "Ok... Now where should I go?"
    $ add_to_list(main_quest_05.list, "hidden")
    jump haven_access_top_floor_choices
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
