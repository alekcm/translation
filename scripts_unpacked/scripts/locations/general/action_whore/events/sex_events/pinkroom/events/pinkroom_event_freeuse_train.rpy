init python:
    def pinkroom_customer_event_train_sex_sleep_loop_function(forced=False):
        number = numgen(4,8)
        for _ in range(number):
            if forced:
                player.sex_forced(tempname, quest_temp)
            
            if numgen() and not acc.anus:
                player.sex_anal(tempname, quest_temp)
                player.sex_cum(tempname, "anal", quest_temp)
            else:
                player.sex_vag(tempname, quest_temp)
                player.sex_cum(tempname, "inside", quest_temp)
        player.sex_hideaction()

label pinkroom_customer_event_freeuse_train_picker:
    if loc(loc_motel_pinkroom):
        $ tempname = pinkroom_tiedtrain
    else:
        $ tempname = guy_tiedtrain
    $ quest_temp = None
    pcm "This is gonna be a very bad idea..."
    pcm "..."
    pcm "Probably loads of fun as well."
    if loc(loc_motel_pinkroom):
        "I go to the door and leave it slightly ajar then get my bindings out and get to work strapping myself to the bed."
    else:
        "I go over and look for something to tie myself to. Get the straps out and begin locking them up."
    pcm "So much harder doing this alone..."
    if loc(loc_motel_pinkroom):
        pcm "Hope no one comes in while I am getting this ready."
    else:
        pcm "Hope no one comes over while I am getting this ready."
    "Eventually I manage to get all the straps in place. Now it's just a case of waiting..."
    if not player.showing:
        $ renpy.show(renpy.random.choice(["sb_upsidedown pout", "sb_doggy1 body_tied", "sb_onback look_up tied worried"]))
    else:
        $ renpy.show(renpy.random.choice(["sb_doggy1 body_tied", "sb_onback look_up tied worried"]))
    with dissolve
    jump pinkroom_customer_event_train_start





label pinkroom_customer_event_train_start:
    $ tempname = pinkroom_tiedtrain
    pcm "Now I just wait..."
    $ relax(5)
    if renpy.showing("sb_upsidedown") or renpy.showing("sb_doggy1"):
        "I spend some time laying here with my ass in the air until finally it seems like I can hear someone."
    elif renpy.showing("sb_onback"):
        "I spend some time laying here with my legs spread until it finally seems like someone is entering."
    if player.blind:
        "I can't see what they are doing or who they are, but I can hear them walking close to me."
    else:
        if renpy.showing("sb_upsidedown") or renpy.showing("sb_onback"):
            "I see some guy sheepishly enter and look around the room. He looks at me and I just look back at him."
        elif renpy.showing("sb_doggy1"):
            if loc(loc_motel_pinkroom):
                "I can't really see the guy since my arse is pointed towards the door, but I hear him come close to me."
            else:
                "I can't really see the guy since he is coming up behind me, but I hear him come close to me."
    if renpy.showing("sb_doggy1"):
        "I wiggle my arse a bit to give him the right idea. That I want to be fucked like a dirty bitch and am not actually in any trouble."
    else:
        "I think, or at least hope, that because I make no attempt to struggle, he understands that this is all a bit of fun."
    if player.gagged:
        pc "Something."
        tempname.name "What we got 'ere then?"
        pc "Something."
        tempname.name "Don't mind if I do."
        jump pinkroom_customer_event_train_sex_first
    else:
        pc "Oh no... I am stuck. Whatever will poor little me do?"
        tempname.name "Oh?"
        pc "Please don't do terrible things to my naked body."
        if not numgen(0,10):
            if renpy.showing("sb_upsidedown"):
                pc "I hope you aren't one of those types of guys who would take advantage of a naked girl all tied up with her ass in the air."
            elif renpy.showing("sb_doggy1"):
                pc "I hope you aren't one of those types of guys who would take advantage of a naked girl all tied up with her ass out in the open ready to be taken."
            elif renpy.showing("sb_onback"):
                pc "I hope you aren't one of those types of guys who would take advantage of a naked girl all tied up spread eagle ready to have a hot man between her legs."
            if renpy.showing("sb_upsidedown") or renpy.showing("sb_onback"):
                pc "I'm sure you won't give me a spanking until my arse is purple."
            else:
                pc "I'm sure you won't suck on my tits as if you are trying to get milk from them."
            pc "Or stick your hard, throbbing cock inside me and fuck the shit out of me until you fill me with cum."
            pc "Or..."
            tempname.name "Yeah yeah, I get it."
        else:
            tempname.name "Who me? Noooo. I'll untie you. But my clothes will get in the way so gimme a sec to undress."
            pc "Ah good."
        jump pinkroom_customer_event_train_sex_first

label pinkroom_customer_event_train_start_unknown:
    $ tempname = pinkroom_tiedtrain
    $ add_to_list(loc_motel_pinkroom.list, "tied_train")
    $ relax(5)
    if loc(loc_motel_pinkroom):
        "I'm not quite sure how long I end up laying here, but eventually someone enters the room."
    else:
        "I'm not quite sure how long I end up laying here, but eventually someone comes up to me."
    if player.blind:
        "I can't see what they are doing or who they are, but I can hear them walking close to me."
    else:
        if renpy.showing("sb_upsidedown") or renpy.showing("sb_onback"):
            "I see some guy sheepishly enter and look around the room. He looks at me and I just look back at him."
        elif renpy.showing("sb_doggy1"):
            if loc(loc_motel_pinkroom):
                "I can't really see the guy since my arse is pointed towards the door, but I hear him come close to me."
            else:
                "I can't really see the guy since he is comin up behind me, but I hear him come close to me."
    if player.gagged:
        pc "Something."
        tempname.name "What we got 'ere then?"
        pc "Something."
        tempname.name "Don't mind if I do."
        jump pinkroom_customer_event_train_sex_first
    else:
        pc "Err, I am kinda stuck. Can you untie me?"
        if loc(loc_motel_pinkroom):
            tempname.name "Says free use on the door."
        else:
            tempname.name "Aren't you one of those kinda sluts who love this sort of thing?"
        if player.has_perk(perk_freeuse, notif=True):
            if loc(loc_motel_pinkroom):
                pc "It does?"
                tempname.name "It true?"
                pc "Yup!"
                tempname.name "Oh? Okay. Great!"
            else:
                pc "Maybe..."
                tempname.name "Oh? Okay. Great!"
        elif player.has_perk(perk_sucu, notif=True):
            if loc(loc_motel_pinkroom):
                pc "So that's what he did..."
                tempname.name "So, free use?"
                pc "Sure, whatever. Have fun."
            else:
                pc "Sure, whatever. Have fun."
        elif player.has_perk(perk_broken, notif=True):
            if loc(loc_motel_pinkroom):
                pc "Oh? Okay then."
            else:
                pc "Err. I can be, I guess."
            tempname.name "Really?"
            pc "..."

        elif player.has_perk(perk_slut, notif=True):
            if loc(loc_motel_pinkroom):
                pc "It does? Should say \"dirty slut\"."
                tempname.name "Oh?"
            else:
                pc "\"dirty slut\" would be more accurate."
        else:
            if player.selling:
                pc "I got kinda stuck here. Last customer didn't untie me."
            else:
                pc "Ended up in a bit of trouble and kinda ended up stuck."
            tempname.name "..."
            pc "So... gonna untie me?"
            if not numgen(0,5):
                tempname.name "I suppose..."
                pc "Thanks."
                tempname.name "Would have been fun to fuck a cutie like you."
                "Just when I think he might change his mind, he leans over and undoes some of the buckles."
                "I manage to struggle out of them and roll myself over onto a more sitting position."
                pc "Thanks for that."
                tempname.name "No worries."
                pc "..."
                pc "Why are you still standing there?"
                tempname.name "Because you are sexy and naked. Not gonna force myself on a girl but I can still watch you."
                pc "..."
                pc "Well, thanks for not, y'know. Raping me."
                tempname.name "Yeah..."
                pcm "Should I \"reward\" him?"
                menu:
                    "Fuck him as thanks":
                        pc "Err, want to fuck anyway now I am not tied up?"
                        tempname.name "Err..."
                        tempname.name "Yes?"
                        pc "Heh."
                        jump whore_street_sex_sex_picker
                    "No, Clean up and leave":

                        pc "Well, I'm going to clean up now..."
                        tempname.name "Sure, I'll leave you be."
                        if loc(loc_motel_pinkroom):
                            "He heads over to the door, pulling it closed as he leaves."
                        else:
                            "He walks away and heads off to where ever he is going."
                        jump travel
            else:

                tempname.name "Hmm, No. I think I will have some fun with you."
                pc "Ugh..."
    jump pinkroom_customer_event_train_sex_first

label pinkroom_customer_event_train_wakeup_train:
    if not any_image_showing():
        if not player.showing:
            $ renpy.show(renpy.random.choice(["sb_upsidedown pout", "sb_doggy1 body_tied", "sb_onback look_up tied worried"]))
        else:
            $ renpy.show(renpy.random.choice(["sb_doggy1 body_tied", "sb_onback look_up tied worried"]))
    $ if_showing("sb_upsidedown", "vag pain down", "sb_doggy1", "vag body_tied", "sb_onback", "tied worried look_down hump", trans=None)
    $ player.sex_forced(tempname)
    $ player.sex_vag(tempname, quest_temp)
    show screen blackout(50) with dissolve
    pc "Uggh..."
    pc "What the...?"
    "I am tied up and seems someone is fucking me..."
    pcm "What the hell?"
    hide screen blackout
    $ if_showing("sb_upsidedown", "up", "sb_onback", "look_up")
    tempname.name "Sleeping beauty is awake is she?"
    pc "What the hell is going on?"
    tempname.name "Having some fun with you."
    pc "Get off!"
    pcm "Shit, tied up..."
    "I struggle a bit with my bindings and try to get them loose, but doesn't look like I can do anything with them."
    "The guy carries on fucking me regardless and doesn't seem to care I am struggling to get free."
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    tempname.name "Ahhhhh!"
    $ player.sex_cum(tempname, "inside", quest_temp)
    pcm "What the...?"
    pcm "Fuck!"
    $ if_showing("sb_upsidedown", "poke", "sb_doggy1", "poke", "sb_onback", "no_sex")
    $ if_showing("sb_upsidedown", "noman", "sb_doggy1", "noman")
    if loc(loc_motel_pinkroom):
        "He dismounts and heads out the door."
    else:
        "He dismounts, dressed up an walks away."
    pcm "Hopefully with that idiot gone, I can get these things off me."
    if loc(loc_motel_pinkroom):
        "But just as soon as the guy left, another man enters and looks around the room a bit."
    else:
        "But just as soon as the guy left, another man comes up to me with clear intentions."
    jump pinkroom_customer_event_train_sex_first

label pinkroom_customer_event_train_sex_first:


    if player.blind:
        if loc(loc_motel_pinkroom):
            "I hear the guy start walk over to the door, shut it then what sounds like him undressing."
        else:
            "I hear the guy start walk over to me then it sounds like him undressing."
    else:
        if loc(loc_motel_pinkroom):
            "The guy walks over to the door, shuts it then starts taking his clothes off."
        else:
            "The guy walks over to me and starts taking his clothes off."
    if loc(loc_motel_pinkroom):
        tempname.name "Don't need someone disturbing us now do we?"
    else:
        tempname.name "Hopefully no one comes by and disturbs us."
    if player.has_perk([perk_freeuse, perk_sucu, perk_slut], notif=True):
        pc "Planning to do something naughty are you?"
    else:
        pc "Please, untie me."
        if loc(loc_motel_pinkroom):
            tempname.name "Says free use on the door."
            pc "What?"
        tempname.name "You dirty sluts like to play a naughty game."
    $ if_showing("sb_upsidedown", "pout poke", "sb_doggy1", "poke", "sb_onback", "hump")
    tempname.name "Mmmm. Dirty little whore."
    $ if_showing("sb_upsidedown", "vag", "sb_doggy1", "vag")
    $ player.sex_vag(tempname, quest_temp)
    pc "Nnng!"
    if player.has_perk([perk_freeuse, perk_sucu, perk_slut]):
        if renpy.showing("sb_upsidedown"):
            "I end up just laying there with my ass in the air as the guy fucks me as he pleases."
        elif renpy.showing("sb_doggy1"):
            if loc(loc_motel_pinkroom):
                "I end up with my face in the pillow as the guy takes me from behind."
            else:
                "I end up with my face in the dirt as the guy takes me from behind."
        elif renpy.showing("sb_onback"):
            "I end up laying there with the guy between my legs, taking me as he pleases."
        "I should probably pretend to put up a fight, but in reality I don't really care and try to enjoy myself."
    else:
        "The guy ignores my pleading to untie me. My only hope is that once he is done he might take pity on me."
        "So in the end I just save my energy and let him do as he wants."
    $ player.sex_cum(tempname, "inside", quest_temp)
    tempname.name "Ahhh fuck yes!"
    pc "..."
    tempname.name "Haaa... Lovely little slut."
    $ if_showing("sb_upsidedown", "poke", "sb_doggy1", "poke", "sb_onback", "no_sex")
    $ if_showing("sb_upsidedown", "noman", "sb_doggy1", "noman")

    if player.has_perk([perk_freeuse, perk_sucu, perk_slut]):
        pc "..."
        if loc(loc_motel_pinkroom):
            "The guy dresses up and quickly leaves, leaving the door open as he does."
        else:
            "The guy dresses up and quickly leaves with no intention of letting me go."
        pcm "Wonder how many guys it's going to take before someone actually let's me go?"
        pcm "A lot probably..."
    else:
        pc "Gonna untie me now you have had your fun?"
        tempname.name "What? Of course not. I'm sure you can fit more cum inside you and there are plenty of men who will put it there."
        pc "Arse!"
        if loc(loc_motel_pinkroom):
            "The guy just dresses up and leaves without closing the door behind him."
        else:
            "The guy just dresses up and leaves without looking back."
        pcm "Fuck, most of these cunts are going to be like this..."
        if loc(loc_motel_pinkroom):
            "Resigned to my fate, I just close my eyes and hope that one of the people who enter will take pity on me."
        else:
            "Resigned to my fate, I just close my eyes and hope that one of the people who fuck me will take pity on me after and release me."
    $ if_showing("sb_upsidedown", "closed", "sb_onback", "look_closed")
    $ temp_var_1 = 0
    $ temp_var_2 = False
    jump pinkroom_customer_event_train_sex_loop

label pinkroom_customer_event_train_sex_loop:
    $ temp_var_1 += 1
    $ relax(numgen(5,20))
    $ npc_race_picker()
    if player.tired <= 15:
        jump pinkroom_customer_event_train_sex_sleep
    elif temp_var_1 >= 15:
        "At some point I lose count of how many men have fucked me. I am tired and it is all becoming a blur..."
        show screen blackout(50) with dissolve
        pcm "How many more will it be?"
        show screen blackout(100) with dissolve
        jump pinkroom_customer_event_train_sex_instant
    elif temp_var_1 >= 7:
        if not temp_var_2:
            $ temp_var_2 = True
            if player.has_perk([perk_freeuse, perk_sucu, perk_slut]):
                "I start to really relax back and let the guys fuck me without even pretending to want to be released."
                "No doubt eventually someone will take pity on me, until then though I will just enjoy myself."
            else:
                "At this point I don't even bother to beg to be released. I just lay back and prepare to take it."
                "I have no idea how many cocks will fuck me until I am released. But at some point someone will surely help me out."
                "So I just tune out all the fucking and wait for that moment."
            jump pinkroom_customer_event_train_sex_quickloop
    if player.has_perk([perk_freeuse, perk_sucu, perk_slut]):
        if loc(loc_motel_pinkroom):
            "Another guy enters after some time. I make a token effort to pretend I want to be released and as expected he ignores me."
        else:
            "Another guy comes up after some time. I make a token effort to pretend I want to be released and as expected he ignores me."
        "So again I end up taking another cock in me..."
    else:
        if loc(loc_motel_pinkroom):
            "Another guy enters and I try and plead with him to let me go. But of course he ignores me."
        else:
            "Another guy comes up and I try and plead with him to let me go. But of course he ignores me."
        "After he gets naked I no longer even bother to beg him."

    if not player.gagged and numgen():
        pcm "Huh, what is he doing?"
        if numgen():
            $ inv.take(item_ballgag)
            $ player.add_perk(perk_gagged)
        else:
            $ inv.take(item_ballgag_locked)
            $ player.add_perk(perk_gagged_locked)
        pc "Something"
    elif not player.blind and numgen():
        pc "No, don't put that on!"
        $ inv.take(item_blindfold)
        $ player.add_perk(perk_blind)
        pcm "Ugh..."

    jump expression WeightedChoice([
    ("pinkroom_customer_event_train_sex_loop_vag", 100),
    ("pinkroom_customer_event_train_sex_loop_anal", If(not acc.anus, 50, 0)), 
    ("pinkroom_customer_event_train_sex_loop_blow", If(not (player.gagged or renpy.showing("sb_doggy1")), 50, 0)),  
    ("pinkroom_customer_event_train_sex_loop_wank", If(renpy.showing("sb_onback"), 50, 0)), 
    ("pinkroom_customer_event_train_sex_loop_buk", If(renpy.showing("sb_onback"), 50, 0)),
    ])

label pinkroom_customer_event_train_sex_loop_vag:
    $ if_showing("sb_upsidedown", "poke closed pout", "sb_onback", If(numgen(), "look_closed pout hump", "look_closed pout missionary"), "sb_doggy1", "poke")
    "The guy climbs on me and I feel him lining his cock up with my pussy."
    $ player.sex_vag(tempname, quest_temp)
    $ if_showing("sb_upsidedown", "vag", "sb_doggy1", "vag")
    "Nothing I can do about it but take it in me."
    "He keeps fucking me while saying some stuff. But I just tune it out. He isn't going to untie me so I don't much care what he has to say."
    "I just have to accept his cock pushing in and out of me and the guy taking what fun he wants."
    tempname.name "Ahhhhh!"
    $ player.sex_cum(tempname, "inside", quest_temp)
    pc "..."
    $ if_showing("sb_upsidedown", "poke", "sb_doggy1", "poke", "sb_onback", "no_sex")
    $ if_showing("sb_upsidedown", "noman", "sb_doggy1", "noman")
    if loc(loc_motel_pinkroom):
        "He dismounts and heads out the door, of course leaving it open for someone else to join."
    else:
        "He dismounts and heads off no doubt telling other guys they can join."
    jump pinkroom_customer_event_train_sex_loop

label pinkroom_customer_event_train_sex_loop_anal:
    $ if_showing("sb_upsidedown", "poke closed pout", "sb_onback", If(numgen(), "look_closed pout hump", "look_closed pout missionary"), "sb_doggy1", "poke")
    "The guy climbs on me and I feel him lining his cock up with my arsehole."
    $ player.sex_anal(tempname, quest_temp)
    $ if_showing("sb_upsidedown", "ass", "sb_doggy1", "anal")
    "His cock invades my arse and I can do nothing but accept it inside me."
    "He fucks and spanks me while saying some dirty words. But I mostly tune it all out"
    "I just have to accept his cock fucking my arsehole and hope he finished somewhat soon."
    tempname.name "Ahhhhh!"
    $ player.sex_cum(tempname, "anal", quest_temp)
    pc "..."
    $ if_showing("sb_upsidedown", "poke", "sb_doggy1", "poke", "sb_onback", "no_sex")
    $ if_showing("sb_upsidedown", "noman", "sb_doggy1", "noman")
    if loc(loc_motel_pinkroom):
        "He dismounts and heads out the door, of course leaving it open for someone else to join."
    else:
        "He dismounts and heads off no doubt telling other guys they can join."
    jump pinkroom_customer_event_train_sex_loop

label pinkroom_customer_event_train_sex_loop_blow:
    "The guy aims his cock closer to my face. I guess this time round I will be getting fucked in the face."
    $ if_showing("sb_upsidedown", "blow closed", "sb_onback", "facefuck")
    $ player.sex_oral(tempname, quest_temp)
    "He rides my face, using my mouth as just a hole to fuck."
    $ if_showing("sb_upsidedown", "blowdeep", "sb_onback", "facefuck_deep")
    "But that of course it not enough. He has to fuck my throat as well. Making it tough for me to breathe."
    "I just manage to suck in some air through my nose when he pulls out a bit and hope he hurries up."
    tempname.name "Ahhhyes!"
    $ player.sex_cum(tempname, "mouth", quest_temp)
    "I feel him coming down my throat and try my best not to choke on it."
    $ if_showing("sb_upsidedown", "blow closed", "sb_onback", "facefuck")
    $ if_showing("sb_upsidedown", "no_sex", "sb_onback", "no_facefuck")
    if loc(loc_motel_pinkroom):
        "Eventually he leaves, leaving the door open for someone else."
    else:
        "Eventually he leaves and heads off no doubt telling other guys they can join."
    jump pinkroom_customer_event_train_sex_loop

label pinkroom_customer_event_train_sex_loop_wank:
    $ if_showing("sb_onback", If(numgen(), "man_left", "man_right"))
    "The guy climbs onto the bed and starts wanking off."
    "One of the few guys who cont actually try and put anything inside me, but his furious wanking and hands roving over my body let me know he's enjoying himself."
    "It's not long before his cock sounds a lot wetter and I can feel the odd drip from his cock."
    tempname.name "Ahhhhh!"
    $ player.sex_cum(tempname, "face", quest_temp)
    pc "..."
    $ if_showing("sb_onback", "no_man_left no_man_right")
    if loc(loc_motel_pinkroom):
        "He gets off the bed and heads out the door, of course leaving it open for someone else to join."
    else:
        "Eventually he leaves and heads off no doubt telling other guys they can join."
    jump pinkroom_customer_event_train_sex_loop

label pinkroom_customer_event_train_sex_loop_buk:
    $ if_showing("sb_onback", If(numgen(), "man_left", "man_right"))
    "The guy climbs onto the bed and starts wanking off. But it sounds like someone else is also in the room."
    "I realise I am right when I feel some weight on the other side of the bed."
    $ if_showing("sb_onback", "man_left man_right")
    "I hear them both wanking from each ear, neither say anything but both their hands are groping everywhere they can while the other hand works their cock."
    tempname.name "Ahhhhh!"
    $ player.sex_cum(tempname, "face", quest_temp)
    tempname2.name "Yes dirty bitch!"
    $ player.sex_cum(tempname2, "chest", quest_temp)
    "Cum from both sides hit my body and once they are done, they head off to leave."
    $ if_showing("sb_onback", "no_man_left no_man_right")
    if loc(loc_motel_pinkroom):
        "He gets off the bed and heads out the door, of course leaving it open for someone else to join."
    else:
        "Eventually he leaves and heads off no doubt telling other guys they can join."
    jump pinkroom_customer_event_train_sex_loop

label pinkroom_customer_event_train_sex_quickloop:
    if not numgen(0,10):
        jump pinkroom_customer_event_freeuse_train_rescue
    elif numgen(0,4) and not acc.anus:
        $ if_showing("sb_upsidedown", "poke closed pout", "sb_onback", If(numgen(), "look_closed pout hump", "look_closed pout missionary"), "sb_doggy1", "poke")
        pcm "My arse this time is it?"
        $ player.sex_anal(tempname, quest_temp)
        $ if_showing("sb_upsidedown", "ass", "sb_doggy1", "anal")
        "I lay back and get my ass fucked, waiting for him to cum..."
        tempname.name "Ahhhhh!"
        $ player.sex_cum(tempname, "anal", quest_temp)
        $ if_showing("sb_upsidedown", "poke", "sb_doggy1", "poke", "sb_onback", "no_sex")
        $ if_showing("sb_upsidedown", "noman", "sb_doggy1", "noman")
        if loc(loc_motel_pinkroom):
            "He dismounts and heads out the door, of course leaving it open for someone else to join."
        else:
            "He dismounts and heads off no doubt telling other guys they can join."
    else:
        $ if_showing("sb_upsidedown", "poke closed pout", "sb_onback", If(numgen(), "look_closed pout hump", "look_closed pout missionary"), "sb_doggy1", "poke")
        "He lines up his cock with my pussy."
        $ player.sex_vag(tempname, quest_temp)
        $ if_showing("sb_upsidedown", "vag", "sb_doggy1", "vag")
        "And I just lay there and take it."
        tempname.name "Ahhhhh!"
        $ player.sex_cum(tempname, "inside", quest_temp)
        $ if_showing("sb_upsidedown", "poke", "sb_doggy1", "poke", "sb_onback", "no_sex")
        $ if_showing("sb_upsidedown", "noman", "sb_doggy1", "noman")
        if loc(loc_motel_pinkroom):
            "He dismounts and heads out the door, of course leaving it open for someone else to join."
        else:
            "He dismounts and heads off no doubt telling other guys they can join."
    jump pinkroom_customer_event_train_sex_loop

label pinkroom_customer_event_train_sex_instant:
    $ relax(numgen(5,20))
    if not numgen(0,20):
        pause 0.5
        $ player.cheat_bukake()
        $ player.cheat_bukake()
        $ player.sex_hideaction()
        hide screen blackout with dissolve
        jump pinkroom_customer_event_freeuse_train_rescue
    elif not numgen(0,4) and not acc.anus:
        $ player.sex_anal(tempname, quest_temp)
        $ player.sex_cum(tempname, "anal", quest_temp)
    else:
        $ player.sex_vag(tempname, quest_temp)
        if numgen(0, 4):
            $ player.sex_cum(tempname, "inside", quest_temp)
        else:
            $ player.sex_cum(tempname, "pullout", quest_temp)
    jump pinkroom_customer_event_train_sex_instant





label pinkroom_customer_event_train_sex_sleep:
    "I am totally exhausted and can barely even keep my eyes open despite the position I am in."
    show screen blackout(50) with dissolve
    "I start to fade out, despite knowing how much of a bad idea it is."
    show screen blackout(100) with dissolve
    jump pinkroom_customer_event_train_sex_sleep_loop

label pinkroom_customer_event_train_sex_sleep_loop:
    $ pinkroom_customer_event_train_sex_sleep_loop_function()
    $ time_sleep_hour()
    if player.tired >= 20 and not numgen(0, 4):
        jump pinkroom_customer_event_train_sex_sleep_wake
    else:
        jump pinkroom_customer_event_train_sex_sleep_loop

label pinkroom_customer_event_train_sex_sleep_wake:
    $ player.sex_hideaction()
    $ if_showing("sb_upsidedown", "vag up pain", "sb_doggy1", "vag", "sb_onback", "hump worried look_up ah", trans=None)
    hide screen blackout with hpunch
    "I wake with a start and look around to see where I am..."
    pcm "Ah, yeah... I am tied up..."
    "It's not the least shocking to be woke up to a guy fucking me."
    pcm "Haven't been rescued yet, so I guess more waiting..."
    $ if_showing("sb_upsidedown", "closed", "sb_onback", "look_closed")
    $ player.sex_cum(tempname, "inside", quest_temp)
    $ if_showing("sb_upsidedown", "poke", "sb_doggy1", "poke", "sb_onback", "no_sex")
    $ if_showing("sb_upsidedown", "noman", "sb_doggy1", "noman")
    if loc(loc_motel_pinkroom):
        "He dismounts and heads out the door, of course leaving it open for someone else to join."
    else:
        "He dismounts and heads off no doubt telling other guys they can join."
    jump pinkroom_customer_event_train_sex_loop





label pinkroom_customer_event_freeuse_train_rescue:
    if loc(loc_motel_pinkroom):
        jump pinkroom_customer_event_freeuse_train_rescue_pinkroom
    else:
        jump random_event_generic_freeuse_tied_rescue

label pinkroom_customer_event_freeuse_train_rescue_pinkroom:
    if player.blind:
        "I feel some hands on my face and the blindfold coming off."
        $ player.remove_perk(perk_blind)
        $ if_showing("sb_upsidedown", "up pout", "sb_onback", "look_up ah worried")
        show motel_recep at right1
        with dissolve
        motel_recep.name "*Sigh*"
    else:
        $ if_showing("sb_upsidedown", "up pout", "sb_onback", "look_up ah worried")
        show motel_recep at right1
        with dissolve
    motel_recep.name "What you doing here giving out freebies?"
    if player.has_perk(perk_freeuse, notif=True):
        pc "Err... I did this for a customer. They refused to untie me..."
    else:
        pc "I wasn't. Fucker refused to untie me."
    if player.gagged:
        if player.has_perk(perk_gagged_locked):
            "She tries to remove the gag from me but isn't able to."
            motel_recep.name "Dumb whore!"
            "She just then decides to loosen some of the bindings and walks away."
            motel_recep.name "Fuck off out the room or start charging."
            hide motel_recep with dissolve
        else:
            "She reaches over and unclasps the gag and I manage to spit it out."
            $ player.remove_perk(perk_gagged)
            pc "I wasn't giving freebies. Fucker refused to untie me."
            motel_recep.name "..."
            motel_recep.name "You aren't the first whore I've had to rescue like this..."
            "She just then decides to loosen some of the bindings and walks away."
            motel_recep.name "Now fuck off out the room or start charging to be fucked. Taking up space when others could be making money."
            hide motel_recep with dissolve
    else:
        motel_recep.name "..."
        motel_recep.name "You aren't the first whore I've had to rescue like this..."
        "She just then decides to loosen some of the bindings and walks away."
        motel_recep.name "Now fuck off out the room or start charging to be fucked. Taking up space when others could be making money."
        hide motel_recep with dissolve

    "I manage to fumble with the straps and get the rest of them off, then sit myself up on the bed."
    $ renpy.scene()
    with dissolve
    if player.has_perk(perk_sucu, notif=True):
        pcm "Not gonna sleep for a week now though."
        pcm "Worth it..."
    elif player.has_perk(perk_broken, notif=True):
        pcm "..."
        pcm "Was nice to be used again..."
    elif player.has_perk(perk_freeuse, notif=True):
        pcm "Since I am not dead though, that was well worth it."
        pcm "Can't get any more free use than tied up and fucked by so many strangers."
    else:
        pcm "Fucking arse! Leaving me like that."
    pc "..."
    if "temp_outfit" in tab_top:
        "I head over to where I hid my clothes and start to dress."
        $ pc_dress("party")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
