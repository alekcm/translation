init python:
    def haven_sold_passtime(amount):
        for _ in range(amount):
            for _ in range(20):
                haven_sold_sex()
            
            t.pass_time(1, False)
        player.shower()
        player._confidence = 0.0
        player._mood = 25.0
        player._tired = 60.0
        player.face_normal()

    def haven_sold_sex():
        randomnum = renpy.random.randint(0, 10)
        player.sex_forced(havenbrothel, main_quest_05)
        if randomnum <= 7:
            randomnum = renpy.random.randint(0, 5)
            if randomnum == 0:
                player.sex_anal(havenbrothel, main_quest_05)
                randomnum = renpy.random.randint(0, 3)
                if randomnum == 0:
                    player.sex_cum(havenbrothel, "anal", main_quest_05)
                else:
                    player.sex_cum(havenbrothel, "ass", main_quest_05)
            else:
                player.sex_vag(havenbrothel, main_quest_05)
                randomnum = renpy.random.randint(0, 5)
                if randomnum == 0:
                    player.sex_cum(havenbrothel, "ass", main_quest_05)
                elif randomnum == 1:
                    player.sex_cum(havenbrothel, "pullout", main_quest_05)
                else:
                    player.sex_cum(havenbrothel, "inside", main_quest_05)
        else:
            randomnum = renpy.random.randint(0, 1)
            
            
            if randomnum == 1:
                player.sex_hand(havenbrothel, main_quest_05)
                player.sex_cum(havenbrothel, "face", main_quest_05) 
            else:
                player.sex_oral(havenbrothel, main_quest_05)
                player.sex_cum(havenbrothel, "mouth", main_quest_05) 
        player.sex_hideaction()

label haven_sold_ending_check_door_rep:
    $ rand_choice = renpy.random.choice([
    "haven_sold_ending_door_rep_1",
    "haven_sold_ending_door_rep_2",
    "haven_sold_ending_door_rep_3",
    "haven_sold_ending_door_rep_4",
    "haven_sold_ending_door_rep_5",
    "haven_sold_ending_door_rep_6",
    "haven_sold_ending_door_rep_7",
    "haven_sold_ending_door_rep_8",
    "haven_sold_ending_door_rep_9",

    ])
    jump expression rand_choice

label haven_sold_ending_door_rep_1:
    pcm "Would be impossible to get through there..."
    pcm "Come on [tucker.sname]. Where are your goons?"
    jump haven_sold_ending_check_door_rep_end
label haven_sold_ending_door_rep_2:
    pcm "Doubt I could make a run for it when someone comes in."
    pcm "Just have to hope someone is coming to get me out of here."
    jump haven_sold_ending_check_door_rep_end
label haven_sold_ending_door_rep_3:
    pcm "Why would somewhere have a door like that?"
    pcm "It's as if this place had police cells before the pandemic made most places get abandoned."
    jump haven_sold_ending_check_door_rep_end
label haven_sold_ending_door_rep_4:
    pcm "Solid metal with a food hatch."
    pcm "Why would somewhere have such doors?"
    jump haven_sold_ending_check_door_rep_end
label haven_sold_ending_door_rep_5:
    pcm "Can hear some faint noises from outside but the door is pretty soundproof."
    pcm "Wonder what kind of place this is."
    jump haven_sold_ending_check_door_rep_end
label haven_sold_ending_door_rep_6:
    pcm "How many more rooms like this do they have?"
    pcm "Hope there aren't other idiots like me all lined up along a corridor."
    jump haven_sold_ending_check_door_rep_end
label haven_sold_ending_door_rep_7:
    pcm "Already tried shoulder charging the door and I will break long before that door ever does..."
    jump haven_sold_ending_check_door_rep_end
label haven_sold_ending_door_rep_8:
    pcm "Open. Oooopen. Fuck come on [tucker.sname]. Where are you?"
    jump haven_sold_ending_check_door_rep_end
label haven_sold_ending_door_rep_9:
    pcm "Come on [emile.name]. Send someone through the door..."
    jump haven_sold_ending_check_door_rep_end

label haven_sold_ending_check_door_rep_end:
    $ working(60)
    pcm "Ugh, shouldn't stand here just staring at the door..."
    jump haven_sold_ending_check_rep_join

label haven_sold_ending_shower_rep:
    show shower with dissolve

    if player.is_dirty():
        pcm "Better clean up or else I will get beaten again..."
    else:
        pcm "Not really dirty but don't want to risk another beating..."
    $ player.shower()
    $ acc.makeup_on = False
    $ working(20)
    hide shower with dissolve
    jump haven_sold_ending_check_rep_join

label haven_sold_ending_bed_rep:
    if player.pregnancy >= 2:
        show haven_lament_open with dissolve
    else:
        $ randomnum = renpy.random.randint(1, 2)
        if randomnum == 1:
            show haven_lament with dissolve
        else:
            show haven_lament_open with dissolve
    $ rand_choice = renpy.random.choice([
    "haven_sold_ending_bed_rep_1",
    "haven_sold_ending_bed_rep_2",
    "haven_sold_ending_bed_rep_3",
    "haven_sold_ending_bed_rep_4",
    "haven_sold_ending_bed_rep_5",
    "haven_sold_ending_bed_rep_6",
    "haven_sold_ending_bed_rep_7",
    "haven_sold_ending_bed_rep_8",
    "haven_sold_ending_bed_rep_9",

    ])
    jump expression rand_choice

label haven_sold_ending_bed_rep_1:
    pcm "*SOB*"
    pcm "Not sure how much of this I can take..."
    jump haven_sold_ending_bed_rep_end

label haven_sold_ending_bed_rep_2:
    pc "..."
    pcm "Please hurry..."
    pcm "It is horrible here [emile.name]..."
    jump haven_sold_ending_bed_rep_end

label haven_sold_ending_bed_rep_3:
    pcm "..."
    pc "*SOB*"
    pc "*Sniff*"
    pcm "Let me out of here..."
    jump haven_sold_ending_bed_rep_end

label haven_sold_ending_bed_rep_4:
    pc "..."
    pcm "Maybe if I hit him back..."
    pcm "Then he will..."
    pc "*SOB*"
    jump haven_sold_ending_bed_rep_end

label haven_sold_ending_bed_rep_5:
    pc "..."
    pcm "I need to try and be strong. Someone will come for me."
    pcm "They have to..."
    pcm "..."
    pcm "Please come..."
    jump haven_sold_ending_bed_rep_end

label haven_sold_ending_bed_rep_6:
    pc "..."
    pcm "You won't leave me here will you [emile.name]?"
    pcm "..."
    jump haven_sold_ending_bed_rep_end

label haven_sold_ending_bed_rep_7:
    pc "..."
    pcm "I had the plug..."
    pcm "They gave it to me for this reason."
    pcm "Any moment they should be coming for me."
    pcm "..."
    pcm "Any moment..."
    jump haven_sold_ending_bed_rep_end

label haven_sold_ending_bed_rep_8:
    pc "..."
    pcm "Please hurry..."
    pcm "It is horrible here [emile.name]..."
    jump haven_sold_ending_bed_rep_end

label haven_sold_ending_bed_rep_9:
    pc "..."
    pcm "Please hurry..."
    pcm "It is horrible here [emile.name]..."
    jump haven_sold_ending_bed_rep_end

label haven_sold_ending_bed_rep_end:
    if player.tired <= 30:
        hide haven_lament
        hide haven_lament_open
        with dissolve
        pc "..."
        pc "So tired..."
        show haven_lament_sleep with dissolve
        pause 0.5
        show screen blackout(100) with Dissolve(1)
        $ time_sleep(230)
        pause 1
        hide haven_lament_sleep
        hide screen blackout with dissolve
        if player.pregnancy >= 2:
            show haven_lament_open with dissolve
        else:
            $ randomnum = renpy.random.randint(1, 2)
            if randomnum == 1:
                show haven_lament with dissolve
            else:
                show haven_lament_open with dissolve
        pc "Huh?"
        pcm "Oh..."
        pcm "Fuck. Still in this place..."
    else:


        $ working(120)

    hide haven_lament
    hide haven_lament_open
    with dissolve
    jump haven_sold_ending_check_rep_join





label haven_sold_ending_look_rep:
    jump expression renpy.random.choice([
    "haven_sold_ending_look_rep_1",
    "haven_sold_ending_look_rep_2",
    "haven_sold_ending_look_rep_3",
    "haven_sold_ending_look_rep_4",
    "haven_sold_ending_look_rep_5",
    "haven_sold_ending_look_rep_6",
    "haven_sold_ending_look_rep_7",
    "haven_sold_ending_look_rep_8",
    "haven_sold_ending_look_rep_9",
    ])

label haven_sold_ending_look_rep_1:
    pcm "Nothing to do but just pace around the room..."
    jump haven_sold_ending_look_rep_end
label haven_sold_ending_look_rep_2:
    pcm "Wish I could read the faded writing on the walls. Give me something to do other than pacing around."
    jump haven_sold_ending_look_rep_end
label haven_sold_ending_look_rep_3:
    pcm "Toilet still there. Bricks still where the bricks are supposed to be..."
    jump haven_sold_ending_look_rep_end
label haven_sold_ending_look_rep_4:
    pcm "1... 2... 3... Turn... 1... 2... 3..."
    jump haven_sold_ending_look_rep_end
label haven_sold_ending_look_rep_5:
    pcm "Shower head has 38 holes for the water to come out of..."
    jump haven_sold_ending_look_rep_end
label haven_sold_ending_look_rep_6:
    pcm "Toilet goes *flush* then *gurgle* followed by *blub blub blub*"
    jump haven_sold_ending_look_rep_end
label haven_sold_ending_look_rep_7:
    pcm "No more nails to bite..."
    jump haven_sold_ending_look_rep_end
label haven_sold_ending_look_rep_8:
    pcm "*Buzzzzzzzz* *Buuuuzzzzzz* Hello light. *Buuuzzzzzzz*"
    jump haven_sold_ending_look_rep_end
label haven_sold_ending_look_rep_9:
    pcm "And we go left and then we go right and then we go left..."
    jump haven_sold_ending_look_rep_end

label haven_sold_ending_look_rep_end:
    $ working(120)
    pcm "Ugh..."
    jump haven_sold_ending_check_rep_join

label haven_sold_ending_check_rep_join:
    if haventrainer.spoke_to_hours_ago > 3 and numgen(0,2):
        jump expression "haven_sold_ending_training_" + str(loc_haven_cell.dict["training_stage"])
    else:
        jump travel

label haven_sold_ending_birth_call:
    if player.days_pregnant > global_pregnancy_length:
        hide screen blackout with dissolve
        $ player.face_pain()
        pcm "Nnnng!"
        pcm "Fuck it's coming."
        show screen blackout(100) with dissolve
        $ player.give_birth()
        $ player.set_fitness(25)
        return
    else:
        return

label haven_sold_ending_hospital_birth_call:
    if player.days_pregnant > global_pregnancy_length:
        show nurse at right1
        show nikolas at right3
        $ walk(loc_hospital_ward)
        $ player.face_pain()
        hide screen blackout with dissolve
        pc "Ahhh I can feel it, it is coming!"
        nurse.name "Breathe, deep breaths..."
        pc "Ahhhhhh!"
        show screen blackout(100) with dissolve
        hide nurse
        hide nikolas
        $ player.give_birth()
        $ t.pass_time(6)

        return
    else:
        return



label haven_sold_ending:
    $ havenbrothel = Npc(fname="Brothel", sname="client", pregname="I am carrying the child of someone who had sex with me while I was trapped in the underground brothel.", virginname="some random")
    $ renpy.stop_predict("images/locations/haven/screen_office/*.webp")

    show haven_guard3 with hpunch
    havguard "Come 'ere!"
    $ player.face_worried()
    pc "Shit!"
    with hpunch
    pc "Get... Off!"
    $ renpy.scene()
    show screen hooded(_layer="fg_screen") with hpunch
    pc "Ahhhhhh! Mmmffffffff!!"
    pcm "Fuck, can't get them off me."
    with vpunch
    "No matter how much I struggle, I am unable to wrest myself away from the people holding me."
    pcm "Fuck fuck! Just wearing myself out. Need to wait for a good time to do a runner."
    "I am dragged around for a while and then bundled into some kind of small area not even big enough to kick my legs out."
    pcm "Where am I?"
    pcm "Shit, this is getting worse by the moment..."
    pcm "Huh, everything is vibrating? Fuck am I in a car or something?"
    pcm "Can't be. No cars any more. So where the fuck an I?"
    with hpunch
    pcm "Need to get out!"
    with hpunch
    pcm "Shit, can't get any leverage with my arms and legs tied up."
    with vpunch
    pcm "..."
    pcm "*Sigh* Nothing I can do..."
    pcm "Hope [tucker.name] and [emile.name] are able to track me and I didn't go around with this in my arse only to get kidnapped anyway."
    pcm "If I can't get out of here I just need to hold out until they come."
    "The ride carries on for some time and I just lay there trying to keep my energy in the hopes of making it out of here when I arrive to where every they are taking me."
    pcm "Been bouncing around for a while. How far is the place? Even if I'm just in a cart it must be pretty far from [haven]."
    "My ride does eventually come to a stop, but I am given no chance to try and escape and are instead dragged away and lead somewhere else."
    pcm "Where are they taking me?"
    pcm "No wind and it stinks in here, so we are inside. But no idea where."
    "I am given one last push and then just... left alone."
    pcm "Huh?"
    pcm "No one holding me or pushing me? What's going on now?"






    $ renpy.scene()
    $ npc_race = 1
    $ walk(loc_haven_cell, 120)
    $ player.face_shock()
    $ renpy.hide_screen("hooded", layer="fg_screen")
    show haven_guardcell
    with hpunch
    pc "Ah!"
    haventrainer.name "Welcome to your new home."
    $ player.face_worried()
    pc "What? Home?"
    if not c.exposed:
        jump haven_sold_ending_cont0
    else:
        haventrainer.name "Get those bits of metal out of you."
        pc "..."
        pc "Why?"
        $ player.punch()
        haventrainer.name "Don't ask questions. Do it!"
        $ player.face_meek()
        pc "..."
        $ player.punch()
        pc "Ahhh!"
        haventrainer.name "Don't just stand there. Off!"
        pc "Okay ok..."
        pause 0.5
        $ acc_strip()
        jump haven_sold_ending_cont2

label haven_sold_ending_cont0:
    haventrainer.name "Undress."
    pc "What? Why?"
    haventrainer.name "Don't ask questions unless you want a beating. Undress, now!"
    pcm "This is not looking good..."
    $ player.punch()
    pc "Ahhh fuck. What did you do that for?"
    haventrainer.name "I told you to undress."
    if player.check_nowill():
        jump haven_sold_ending_cont1

    pc "..."
    $ player.punch()
    pc "Ahhh shit stop!"
    haventrainer.name "Undress."
    if player.check_nowill:
        jump haven_sold_ending_cont1
    pc "Wait, what is goi..."
    $ player.punch()
    pc "Ahhh!"
    $ player.punch()
    pc "!!!"
    $ player.face_cry()
    $ player.punch()
    pc "Stop stop!"
    pc "*SOB"
    jump haven_sold_ending_cont1

label haven_sold_ending_cont1:
    $ player.face_meek()
    pcm "..."
    $ c.top = 0
    pcm "Shit, I am not getting out of this am I?"
    $ c.bottom = 0
    $ c.pants = 0
    pcm "Damn [tucker.sname] better hurry..."
    haventrainer.name "Everything. Take out the piercings as well."
    pc "..."
    $ pc_strip()
    $ acc_strip()
label haven_sold_ending_cont2:
    haventrainer.name "Now get over there. Clean yourself up."
    $ player.face_worried()
    pc "What? Why?"
    $ player.face_meek()
    "He steps forward and I realise he is going to hit me, so I quickly rush under the shower."
    pcm "Fuck. Didn't think it could be worse than Haven. I need to be careful in here or I will end up looking like a corpse."
    show shower with dissolve
    $ player.shower()
    $ acc.makeup_on = False
    pcm "I just need to play for time. The tracker will lead them here."
    pcm "Just stay here washing. Nothing to worry about..."
    haventrainer.name "Hurry up!"
    hide shower with hpunch
    pc "Ah!"
    haventrainer.name "Come here. Let's see what you are made of."
    show haven_gangbang_plug at right with hpunch
    pcm "Fuck!"
    haventrainer.name "Hmmm."
    show haven_gangbang_plug plugpull with dissolve
    haventrainer.name "Won't be needing this anymore. But good you came prepared."
    show haven_gangbang_plug noplug with dissolve
    haventrainer.name "Still a nice body and these bruises should heal."
    $ player.spank()
    pc "Ah!"
    $ player.face_worried()
    if writing.check_writing("tattoo"):
        haventrainer.name "The writing is a tattoo? Already looking like someone ready for this place."
        if isinstance(writing.ass, dict) and "tattoo" in writing.ass:
            haventrainer.name "And a counter for who fucked you? Christ!"
            if writing.ass_counter == 0:
                haventrainer.name "No one put their mark on you yet though. Don't worry, we will change that."
            elif writing.ass_counter > 100:
                haventrainer.name "How many is that? Fucking hell. Over 100 has given it to ya. You gonna love this place."
            elif writing.ass_counter > 10:
                haventrainer.name "Decent numbers I suppose."
            else:
                haventrainer.name "We will get those numbers up soon enough."
    haventrainer.name "Come on, up you get!"
    hide haven_gangbang_plug with dissolve
    haventrainer.name "Get some rest. Things are going to get busy for you soon so take the chance while you can."
    pc "What do you mean? Why busy?"
    haventrainer.name "*Hrmf*"
    hide haven_guardcell with dissolve
    pcm "What the hell..."
    pcm "..."
    $ player.face_cry()
    pcm "Fuck. What am I supposed to do..."
    pcm "I should look around a bit and see if I can get out of here."
    $ loc_haven_cell.dict["checked_counter"] = 0
    $ haven_complete_questlog(slave=True)
    jump travel

label haven_sold_ending_check_picker:


    $ loc_haven_cell.dict["checked_counter"] += 1
    jump expression WeightedChoice([
    ("haven_sold_ending_check_bedframe", If(not "checked_bedframe" in loc_haven_cell.list, 1,0)),
    ("haven_sold_ending_check_mattress", If(not "checked_mattress" in loc_haven_cell.list, 1,0)),
    ("haven_sold_ending_check_graf", If(not "checked_graf" in loc_haven_cell.list, 1,0)),
    ("haven_sold_ending_check_shower", If(not "checked_shower" in loc_haven_cell.list, 1,0)),
    ("haven_sold_ending_check_toilet", If(not "checked_toilet" in loc_haven_cell.list, 1,0)),
    ("haven_sold_ending_check_toiletpaper", If(not "checked_toiletpaper" in loc_haven_cell.list, 1,0)),
    ("haven_sold_ending_check_wall", If(not "checked_wall" in loc_haven_cell.list, 1,0)),
    ])

label haven_sold_ending_check_bedframe:
    $ add_to_list(loc_haven_cell.list, "checked_bedframe")
    pcm "Hmm. May be able to pull apart some of this metal from the bed and make a weapon out of it."
    pause 0.5
    with hpunch
    pc "Ung!"
    pcm "..."
    pcm "Bolted to the floor..."
    pcm "What the fuck kind of place has the beds bolted to the floor?"
    pcm "Well, will take some time to try and break this apart for a weapon. I should look around some more."
    jump haven_sold_ending_check_end

label haven_sold_ending_check_mattress:
    $ add_to_list(loc_haven_cell.list, "checked_mattress")
    pcm "This..."
    pcm "Is not a clean mattress..."
    pcm "Hmm, nothing under it or around it. Not a spring mattress so can't pull out the metal springs to use for something."
    pcm "Can't feel any cuts where someone might have slipped something inside... But doesn't mean there isn't one."
    pcm "I should look around more before spending time looking for something hidden."
    jump haven_sold_ending_check_end

label haven_sold_ending_check_graf:
    $ add_to_list(loc_haven_cell.list, "checked_graf")
    pcm "Some markings etched into the wall..."
    pcm "Looks like someone was marking the days..."
    pcm "Whoever it was only made it to 24. Wonder what happened after that?"
    pcm "Some other writing as well but I can't make out what it says. Hmmm."
    pcm "Well, I should look around more for some way to escape so I don't have to start counting my days."
    jump haven_sold_ending_check_end

label haven_sold_ending_check_shower:
    $ add_to_list(loc_haven_cell.list, "checked_shower")
    pcm "Already showered so I know it works and is stone cold. Not sure how I might use it as a way to escape."
    pcm "Could turn it on and block the drain to try and flood the place. But not sure how that will do anything other than get me beaten up."
    pcm "Try and pull it off the wall? Hmm, again that would just get me beaten..."
    pcm "I will look around some more."
    jump haven_sold_ending_check_end

label haven_sold_ending_check_toilet:
    $ add_to_list(loc_haven_cell.list, "checked_toilet")
    pcm "Metal toilet with no seat like you would see in prison movies."
    pcm "Doubt I am pulling that off the wall. Thought not sure where that would get me, assuming I am even strong enough."
    pcm "Ugh, I should look around some more."
    jump haven_sold_ending_check_end

label haven_sold_ending_check_toiletpaper:
    $ add_to_list(loc_haven_cell.list, "checked_toiletpaper")
    pcm "Toilet paper..."
    pcm "Might be able to use it to jam the lock like you read about in books. Haven't a clue how I would go about that though."
    pcm "Could also plug the drain to the shower. Not that it would do me much good..."
    pcm "*Sigh* I need to find something else."
    jump haven_sold_ending_check_end

label haven_sold_ending_check_wall:
    $ add_to_list(loc_haven_cell.list, "checked_wall")
    pcm "Looks sturdy. I can see the brick pattern under the plaster so it's not some flimsy wall that I could break through."
    pcm "No windows or any serious cracks that I can see..."
    pcm "I should give it a try anyway."
    pause 0.5
    $ player.face_pain()
    with hpunch
    pc "Ugh!"
    $ player.face_cry()
    pcm "Not getting through the wall. It is solid."
    pcm "Light on the ceiling is recessed as well so not able to hang from it and pull it from the ceiling or something..."
    pcm "I need to find a better option to get out of here."
    jump haven_sold_ending_check_end

label haven_sold_ending_check_door:
    $ add_to_list(loc_haven_cell.list, "checked_door")
    pcm "The door is made of metal. No chance am I going to be able to break it down."
    pcm "Looks like this place was built ages ago and not something made since the pandemic. Why would there be cells like this in [town]? There wasn't a prison or anything."
    pcm "Anyway, not making it through the door while it's locked so better find some other way out of here."
    jump travel

label haven_sold_ending_check_end:
    if loc_haven_cell.dict["checked_counter"] >= 5:
        $ add_to_list(loc_haven_cell.list, "checked_done")
        jump haven_sold_ending_check_cont
    else:
        jump travel

label haven_sold_ending_check_cont:
    pcm "Huh, someone unlocking the door?"
    show haven_guardcell with dissolve
    pc "What do you want?"
    $ player.punch()
    pc "Ah fuck!"
    haventrainer.name "Don't ask questions."
    haventrainer.name "Get on the bed."
    pc "What? Wh..."
    $ player.punch()
    pc "Ah okay ok!"
    $ player.face_meek()
    "I follow him to the bed as he is taking his clothes off and I realise what he wants from me."
    if player.check_nowill():
        $ NullAction()
    else:
        $ player.face_shock()
        pc "Wait hold on, what the fu..."
        $ player.punch()
        pc "AHhhh!"
        pc "Why?"
        haventrainer.name "Don't ask questions and just do as you are told."
        $ player.face_meek()
        pc "..."
        pause 0.5
        $ player.punch()
        pc "Ahhh! What was that for?"
        haventrainer.name "To make sure you remember."
    pcm "Fuck..."
    show haven_fish at right with dissolve
    pcm "Fuck, come on damn [emile.name]. Get me the fuck out of here!"
    show haven_fish sex with dissolve
    pc "*SOB*"
    $ player.sex_forced(haventrainer, main_quest_05)
    $ player.sex_vag(haventrainer, main_quest_05)
    $ player.face_cry()
    with hpunch
    pc "Ahhhh!"
    with hpunch
    haventrainer.name "Get used to it girl. Gonna be a lot more soon."
    pcm "..."
    pc "*SOB*"
    with hpunch
    haventrainer.name "Got a lot of work ahead of us."
    pc "*SOB*"
    $ player.sex_cum(haventrainer, "inside", main_quest_05)
    haventrainer.name "Haaaaaa!!!"
    pc "*SOB*"
    haventrainer.name "Mmmmm, gonna be fun breaking you in."
    pc "*SOB*"
    show haven_fish nosex with dissolve
    haventrainer.name "Make sure you are clean when I come round next time."
    hide haven_fish with dissolve
    pc "..."
    $ player.punch()
    pc "Ahhhh whyy??"
    haventrainer.name "It's what will happen if I find you dirty in here."
    pc "*SOB*"
    hide haven_guardcell with dissolve
    pc "..."
    $ player.face_wail()
    pc "WAaaaahhhhhhhh..."
    $ player.face_cry()
    pc "*SOB* *SOB*"
    pc "*Sniff*"
    show haven_fish at right with dissolve
    pc "..."
    pcm "Help me [emile.name]..."
    hide haven_fish with dissolve
    show haven_lament_sleep at right3 with dissolve
    pause 1
    show screen blackout(100) with Dissolve(1)
    pause 1
    $ time_sleep(230)
    hide screen blackout with Dissolve(1)
    hide haven_lament_sleep with dissolve
    show haven_lament with dissolve
    pcm "Huh?"
    pcm "..."
    pc "*SOB*"
    pcm "Wasn't a bad dream..."
    hide haven_lament with dissolve
    $ loc_haven_cell.dict["training_stage"] = 0
    $ loc_haven_cell.dict["training_rebel"] = 0
    jump travel



label haven_sold_ending_training_0:
    $ loc_haven_cell.dict["training_stage"] += 1
    $ player.face_worried()
    pcm "Keys! Someone is coming in the room."
    show haven_underbed at right with dissolve
    pcm "Fuck. No way is he going to think I ran away."
    haventrainer.name "*Sigh*"
    $ player.face_shock()
    hide haven_underbed
    show haven_guardcell
    with hpunch
    haventrainer.name "Wrong choice."
    $ player.punch()
    pause 0.5
    $ player.punch()
    pc "Ahhh!"
    $ player.punch()
    pc "Please stop!"
    $ player.face_cry()
    pc "I'm sorry! I'm sorry!!"
    haventrainer.name "Hrmf!"

    if player.is_dirty():
        call expression "haven_sold_ending_training_shower_punish_" + str(loc_haven_cell.dict["training_rebel"]) from _call_expression_4

    haventrainer.name "Get on the bed."
    pc "..."
    haventrainer.name "Do I need to ask again?"
    pc "No!"
    show haven_fish at right with dissolve
    pcm "Fucking bastard!"
    pc "*SOB*"
    haventrainer.name "Good girl."
    pc "..."
    show haven_fish sex with dissolve
    pcm "Ugh..."
    $ player.sex_forced(haventrainer, main_quest_05)
    $ player.sex_vag(haventrainer, main_quest_05)
    with hpunch
    pc "Ahhh."
    haventrainer.name "Don't worry. I will make a slut out of you and make you beg for more cock."
    pcm "Please get me out of here..."
    with hpunch
    pc "Hnnng!"
    with hpunch
    pc "You are being too rough."
    haventrainer.name "Get used to it."
    pc "It hurts."
    haventrainer.name "If you want it to end sooner then you need to make me cum."
    pc "..."
    haventrainer.name "Or you can do the work yourself."
    pc "..."
    with hpunch
    pc "Huuug."
    haventrainer.name "Want me to stop?"
    pc "Yes!"
    haventrainer.name "Then ask me to cum."
    pc "Huh?"
    with hpunch
    pc "Ngg!"
    haventrainer.name "Ask me to cum."
    pc "Please cum."
    haventrainer.name "What?"
    with hpunch
    pc "This hurts. Please finish."
    haventrainer.name "Finish where?"
    pc "Where ever you want. Just hurry."
    with hpunch
    haventrainer.name "Tell me where. Want it in your pussy?"
    pc "Yes, just stop."
    haventrainer.name "Say it. Say you want me to cum in your pussy."
    pc "*SOB*"
    haventrainer.name "Say it!"
    pc "I want you to cum in my pussy..."
    haventrainer.name "Ok."
    with hpunch
    pause 0.5
    with hpunch
    pause 0.5
    $ player.sex_cum(haventrainer, "inside", main_quest_05)
    with hpunch
    haventrainer.name "Haaaaaaaa!"
    pc "Nnnng!"
    haventrainer.name "Haaaa."
    haventrainer.name "..."
    haventrainer.name "There we go. Stopped fucking you and came in your pussy."
    show haven_fish nosex with dissolve
    haventrainer.name "Better now?"
    pc "..."
    haventrainer.name "I asked you a question."
    pc "Yes. Better."
    haventrainer.name "And what do you say after someone does something nice for you?"
    pc "I... Don't know..."
    haventrainer.name "You say thank you."
    pc "..."
    haventrainer.name "Say it."
    pc "..."
    pc "Thank you..."
    haventrainer.name "Good."
    hide haven_fish with dissolve
    haventrainer.name "Now, if I come in here again and find you under the bed then we will have some trouble. Understand?"
    pc "Yes..."
    haventrainer.name "Yes what?"
    pc "I understand."
    haventrainer.name "Hrmf."
    hide haven_guardcell with dissolve
    pc "..."
    $ player.face_wail()
    pc "Whaaaaaaaa!!!!!"
    pc "*Sniff* *Sniff*"
    $ player.face_normal()
    pcm "Please hurry and find me..."

    jump travel

label haven_sold_ending_training_1:
    $ loc_haven_cell.dict["training_stage"] += 1
    pcm "Fuck! He's coming back."
    pcm "..."
    pcm "Nothing I can do about it..."
    show haven_guardcell with dissolve
    haventrainer.name "Glad to see I didn't have to fish you out from under the bed."
    $ player.face_meek()
    pc "..."

    if player.is_dirty():
        call expression "haven_sold_ending_training_shower_punish_" + str(loc_haven_cell.dict["training_rebel"]) from _call_expression_5

    haventrainer.name "On the bed, legs open."
    pc "..."
    show haven_fish at right with dissolve
    pc "..."
    pc "Ok..."
    pc "What do you want?"
    haventrainer.name "You tell me that."
    pc "Huh?"
    haventrainer.name "What do you want?"
    pc "I..."
    pc "I want to be left alone."
    haventrainer.name "Ok, so for that to happen, you will have to satisfy me so I leave."
    pc "..."
    haventrainer.name "Now, I don't like damaging such pretty girls like you. It's a huge waste. I would much prefer to fuck them."
    haventrainer.name "So..."
    haventrainer.name "What will it be?"
    $ player.face_shock()
    pc "Please dont hit me again!"
    haventrainer.name "Okay then."
    $ player.face_normal()
    haventrainer.name "So then what should I do instead?"
    pc "..."
    pc "Sex..."
    haventrainer.name "What?"
    pc "Sex."
    haventrainer.name "Full sentences girl! What do you want?"
    pc "*SOB*"
    pc "..."
    pc "I want you to have sex with me and not hit me."
    haventrainer.name "Okay then. I can do that."
    haventrainer.name "Want me to fuck you gently or want it rough?"
    pc "Gently!"
    haventrainer.name "Ok."
    show haven_fish sex with dissolve
    haventrainer.name "If you cooperate, I will be gentle."
    $ player.sex_vag(havenbrothel, main_quest_05)
    pc "Ngg."
    pc "..."
    haventrainer.name "Like it like this?"
    pc "..."
    haventrainer.name "I can go faster if you want."
    pc "No! This is ok..."
    haventrainer.name "Okay then. So you like it like this?"
    pc "Yes. Stay like this."
    pc "*SOB*"
    haventrainer.name "Crying does you no good. I told you before, want it to end then you need to get me off."
    haventrainer.name "You need to pretend you are enjoying."
    pc "..."
    haventrainer.name "Don't worry, I don't expect you to do that now. But I do expect you to ask me to cum."
    pc "..."
    haventrainer.name "No? Well your choice."
    haventrainer.name "If you won't do the work, then I will."
    with hpunch
    haventrainer.name "Ah much better."
    with hpunch
    pause 0.5
    with hpunch
    pc "Ah too rough!"
    haventrainer.name "Is it?"
    pc "Yes!"
    haventrainer.name "Then you should take control."
    pc "*SOB*"
    pc "Hurry up and finish."
    haventrainer.name "Cum."
    pc "Huh?"
    haventrainer.name "Hurry up and \"cum\". Use the correct words."
    pc "Hurry up and cum..."
    haventrainer.name "In your pussy?"
    pc "Yes."
    haventrainer.name "Where?"
    pc "In my pussy. Hurry and cum in my pussy."
    haventrainer.name "Can't refuse an offer like that."
    with hpunch
    pc "Ahhh."
    with hpunch
    pc "Too much!"
    with hpunch
    pc "Ahhhhh!"
    with hpunch
    pc "*SOB*"
    haventrainer.name "Ahhhhh."
    $ player.sex_cum(havenbrothel, "inside", main_quest_05)
    haventrainer.name "Ahhh yes!"
    haventrainer.name "Mmmmmmmm."
    pc "*SOB*"
    show haven_fish nosex with dissolve
    pc "Why did you do that?"
    haventrainer.name "Hmmm? You asked me to hurry up so I did. Can't have it both ways. So if you want it to always be gentle then you need to do it yourself."
    if loc_haven_cell.dict["training_rebel"] == 0:
        haventrainer.name "If you keep being a good girl, then next time I will bring something nice for you to help your situation."
        pc "Nice?"
        haventrainer.name "Must be boring alone in here. So will bring something to cheer you up."
    else:
        haventrainer.name "Now clean yourself up. You know what will happen if I come in here again and find you all dirty."
        pc "..."
        pc "Yes..."
    hide haven_fish with dissolve
    haventrainer.name "Now, it is at this point you will say goodbye."
    $ player.face_happy()
    pc "What? I can go?"
    haventrainer.name "Are you an idiot? You say goodbye to me who is leaving."
    $ player.face_meek()
    pc "Oh..."
    haventrainer.name "So?"
    $ player.face_normal()
    pc "Goodbye..."
    haventrainer.name "Good enough for now."
    hide haven_guardcell with dissolve
    pcm "..."
    pcm "[tucker.sname] you bastard! Why aren't you here yet?"
    pcm "How much more of this do I have to go through?"

    jump travel

label haven_sold_ending_training_2:
    $ loc_haven_cell.dict["training_stage"] += 1
    pcm "Fuck! He's coming again."
    pcm "..."
    pcm "*SOB*"
    show haven_guardcell with dissolve
    haventrainer.name "..."
    if player.is_dirty():
        call expression "haven_sold_ending_training_shower_punish_" + str(loc_haven_cell.dict["training_rebel"]) from _call_expression_6
    haventrainer.name "Here, take this."
    pc "..."
    pc "What is it?"
    haventrainer.name "Strong alcohol. Put some on your wounds to clean them, drink the rest."
    pc "..."
    pc "Why are you giving me this?"
    haventrainer.name "Bad girls get punished while good girls get rewarded. From now on, if you are a good girl you will be given nicer food to eat and alcohol to wash it down with."
    haventrainer.name "Be a bad girl and you will get the fist."
    haventrainer.name "I don't like hitting people. So let's work together to get you nice food and alcohol shall we?"
    haventrainer.name "I don't like seeing your skin more purple than white."
    haventrainer.name "So drink it up and have a nice long sleep. Might also give some time for those bruises to heal a bit."
    hide haven_guardcell with dissolve
    pc "..."
    pc "*SOB*"
    pc "..."
    pcm "It's alcohol...?"
    pcm "Well, won't be poison since no point in that. They would just beat me to death if they wanted to kill me."
    pcm "So much fucking pain..."
    if bruise.special:
        pcm "Better put some of this on my eye first."
        $ player.face_pain()
        with hpunch
        pc "FUUUUCCCCKKKKKK!!"
        pcm "FUCK!"
        pcm "Ow ow ow ow ow"
        pcm "Fuck, that hurt much more than I thought it would..."
        pcm "Drink!"
    pcm "Here goes..."
    $ player.add_drunk(40)
    $ player.vodka()
    pc "Bleh."
    pc "..."
    $ player.vodka()
    pcm "Ugh, it's horrible..."
    $ player.vodka()
    pcm "Phew..."
    pc "Ugggghhhhh..."
    pcm "Shouldn't... Drink... So... Much..."
    pcm "Spiiiiiiinnniingggg..."
    $ player.eye = 3
    show haven_lament_sleep with dissolve
    pc "Uuuuhhhhhhh..."
    show screen blackout(100) with Dissolve(1)
    $ time_sleep(400)
    $ player.add_drunk(-100)
    $ bruise.special = 0
    pause 1
    show screen blackout(50) with Dissolve(1)
    pc "Uhhhhhh..."
    $ player.face_normal()
    hide screen blackout with dissolve
    pc "..."
    pcm "Still in this place..."
    pcm "What the hell is taking them so long to come?"
    hide haven_lament_sleep with dissolve
    show haven_lament with dissolve
    pcm "Been far too long since I arrived here. Days?"
    pcm "They should have found me by now..."
    pcm "Are they not coming?"
    pcm "No, [emile.name] wouldn't leave me here."
    pcm "..."
    pcm "Better shower before he comes in here again..."
    hide haven_lament with dissolve
    pcm "Bastard will beat me again if I am smelling of booze."
    show shower with dissolve
    $ player.shower()
    $ acc.makeup_on = False
    pcm "Fuck..."
    $ player.face_cry()
    pc "*SOB*"
    $ relax(20)
    hide shower with dissolve
    $ player.face_normal()
    pcm "..."
    pcm "Now what?"

    jump travel

label haven_sold_ending_training_shower_punish_0:
    $ loc_haven_cell.dict["training_rebel"] += 1
    haventrainer.name "Why didn't you take a shower?"
    pc "Huh?"
    haventrainer.name "I told you to be clean when I returned."
    $ player.face_meek()
    pc "..."
    haventrainer.name "Well?"
    $ player.face_normal()
    pc "I..."
    pc "Err..."
    $ player.face_meek()
    pc "..."
    $ player.punch()
    pc "Ahhh!"
    $ player.punch()
    pc "Sorry! I won't do it again!"
    $ player.punch()
    pc "Ahhh haaaaa aaaaaaa!"
    $ player.punch()
    haventrainer.name "What won't you do again?"
    pc "*SOB*"
    haventrainer.name "I asked you a question."
    pc "I won't be dirty."
    haventrainer.name "Good."
    haventrainer.name "Go shower."
    pc "*SOB*"
    show shower with dissolve
    $ player.shower()
    $ acc.makeup_on = False
    pcm "Fuck..."
    pc "*SOB*"
    $ working(20)
    hide shower with dissolve
    pc "..."
    $ player.face_wail()
    pc "Whaaaaa!!!"
    $ player.face_normal()
    pc "*Sniff*"
    haventrainer.name "Come here."

    return

label haven_sold_ending_training_shower_punish_1:
    $ loc_haven_cell.dict["training_rebel"] += 1
    haventrainer.name "And again you haven't taken a shower. Seems like you just don't listen."
    $ player.face_shock()
    pc "No please don't..."
    $ player.punch()
    pc "Ahhh"
    $ player.punch()
    pc "No please wai-"
    $ player.punch()
    pc "Awwwwwaaaaaaa!"
    $ player.punch()
    pc "Ukkkk!"
    $ player.punch()
    pc "Awwwwaaaaaaa nooooooo..."
    $ player.face_wail()
    pc "Awwwwaaa haaaaaa haaaaaa waaaaaaa!!!"
    pc "Sorry please I'm sorry."
    haventrainer.name "Get in the shower."
    pc "Yes!"
    show shower with dissolve
    $ player.shower()
    $ acc.makeup_on = False
    pc "Ahhh haaaa it hurts!"
    pc "The water hurts!"
    haventrainer.name "That's your own fault. Make sure to clean up properly."
    $ working(20)
    hide shower with dissolve
    pc "Whaaaaa!!!"
    $ player.face_normal()
    pc "*Sniff*"
    haventrainer.name "Come here."
    pc "Uhh huh..."
    return

label haven_sold_ending_training_shower_punish_2:
    $ loc_haven_cell.dict["training_rebel"] += 1
    haventrainer.name "You disapoint me..."
    $ player.face_meek()
    pc "..."
    haventrainer.name "Now I am sure you heard me when I told you to be clean."
    haventrainer.name "And I am sure you remember the beatings you got the last time you ignored me."
    haventrainer.name "So I can only assume you are doing this on purpose."
    haventrainer.name "Am I right?"
    pc "..."
    haventrainer.name "Let me tell you something."
    haventrainer.name "In this place, there are a few things we don't necessarily need you to have. This is just a small room after all."
    haventrainer.name "So things like eyes, feet or even legs are not really something you will make much use of."
    haventrainer.name "Not a big issue fucking a blind girl. Not ideal but we more use for a blind girl and a disobedient one."
    haventrainer.name "Still mess around and we will just remove your legs for you. People quite enjoy raping a girl who is that vulnerable."
    haventrainer.name "Worst comes to worst, we will allow someone to have you who gets off on beating girls as they fuck them. If you are going to end up a corpse, might as well have someone pay us to make you one."
    haventrainer.name "So, this is your final warning. Next time you disobey, I will remove your eyes."
    $ player.face_wail()
    pc "Whaaaaaaaa!"
    $ player.face_cry()
    pc "*SOB*"
    haventrainer.name "That is next time though. What should I do this time?"
    pc "Please don't."
    haventrainer.name "It is your actions that brought us here. You had clear instructions and failed to follow them."
    pc "Please! It won't happen again!"
    haventrainer.name "It has happened again. This is your third warning."
    haventrainer.name "So..."
    pc "No please don't..."
    $ player.punch()
    pc "Ahhh"
    $ player.punch()
    pc "No please wai-"
    $ player.punch()
    pc "Awwwwwaaaaaaa!"
    $ player.punch()
    pc "Ukkkk!"
    $ player.punch()
    pc "Awwwwaaaaaaa nooooooo..."
    $ player.punch()
    pc "Uggg!"
    $ player.punch()
    pause 0.3
    show screen blackout(100)
    hide haven_guardcell
    $ bruise.special = "haven"
    $ blood.special = "haven"

    show screen blackout(75) with dissolve
    pc "Ugggg..."
    show screen blackout(100) with dissolve
    pause 1
    show screen blackout(75) with dissolve
    pc "Aaaaaaaaaa..."
    show screen blackout(100) with dissolve
    $ player.shower()
    $ blood.special = 0
    show haven_lament_sleep
    show screen blackout(75) with dissolve
    pc "Ugggghhhh..."
    pc "Huh?"
    $ player.face_shock()
    hide screen blackout
    hide haven_lament_sleep
    with hpunch
    pc "Ow ow ow ow ow ow..."
    pcm "Fuck it hurts!"
    $ player.face_cry()
    pcm "Why..."
    show haven_guardcell with dissolve
    pc "Ah!"
    pc "No please no more!"
    pc "Please please please!"
    haventrainer.name "Going to be a good girl?"
    pc "Yes I promise!"
    haventrainer.name "Really?"
    pc "I am sorry!"
    haventrainer.name "What for?"
    pc "For not showering."
    haventrainer.name "For disobeying me!"
    haventrainer.name "When I tell you to do something, you do it."
    haventrainer.name "Understand?"
    pc "Yes I do."
    haventrainer.name "So, will you disobey again?"
    pc "No."
    haventrainer.name "Let me hear you say it."
    pc "I won't disobey you again."
    haventrainer.name "Good."
    return

label haven_sold_ending_training_3:
    $ loc_haven_cell.dict["training_stage"] += 1
    pcm "Shit, he's coming in again."
    show haven_guardcell with dissolve
    haventrainer.name "..."
    pc "..."
    haventrainer.name "..."
    haventrainer.name "Got something to say?"
    $ player.face_meek()
    pcm "What does he want from me now?"
    pc "No..."
    haventrainer.name "\"Welcome\""
    pc "What?"
    haventrainer.name "When someone comes in that door, no matter who it is I expect you to welcome them into your room."
    pc "..."
    pc "Ok..."
    haventrainer.name "So?"
    pc "..."
    pc "Welcome...?"
    haventrainer.name "Good enough for now. Next time I expect more enthusiasm."
    haventrainer.name "Did you enjoy the alcohol I brought?"
    pc "..."
    pc "Yes."
    haventrainer.name "Thought so. You were out like a light after drinking it."
    pc "You were watching?"
    haventrainer.name "No, this room is your private place. But I did come and check on you and saw you passed out."
    pc "..."
    haventrainer.name "Now, I am leaving so what do you say?"
    pc "Goodbye."
    haventrainer.name "Hrmf."
    hide haven_guardcell with dissolve
    pc "..."

    jump travel

label haven_sold_ending_training_4:
    $ loc_haven_cell.dict["training_stage"] += 1
    pcm "I can hear him at the door."
    show haven_guardcell with dissolve
    haventrainer.name "..."
    pc "..."
    haventrainer.name "I came in here with this food and more alcohol for you."
    pc "Really?"
    haventrainer.name "Yes. But looks like someone else will be eating and drinking it."
    pc "What? Why?"
    haventrainer.name "Didn't I tell you to welcome anyone who comes through that door?"
    $ player.face_meek()
    pc "..."
    haventrainer.name "Well?"
    pc "Yes you did."
    haventrainer.name "And did you welcome me?"
    pc "..."
    $ player.face_shock()
    haventrainer.name "Stop hesitating and answer!"
    pc "Ah."
    $ player.face_meek()
    pc "No I didn't."
    haventrainer.name "No you didn't. So it will be someone else enjoying this."
    haventrainer.name "I am leaving."
    pc "..."
    pc "Goodbye..."
    haventrainer.name "Oh?"
    haventrainer.name "Well done."
    hide haven_guardcell with dissolve
    pc "..."

    jump travel

label haven_sold_ending_training_5:
    $ loc_haven_cell.dict["training_stage"] += 1
    pcm "He's coming again."
    show haven_guardcell with dissolve
    pc "Welcome."
    haventrainer.name "Thank you."
    haventrainer.name "Here you go. Something to eat and drink."
    pc "Thank you..."
    haventrainer.name "Hmmm."
    pc "Ah, goodbye."
    hide haven_guardcell with dissolve
    pc "..."
    pcm "Fuck. Got to do tricks like a dog..."
    with hpunch
    $ player.face_angry()
    pcm "WHY THE FUCK IS NO ONE COMING TO RESCUE ME!!!!"
    pc "..."
    $ player.face_cry()
    pc "*SOB*"
    $ player.vodka()
    pc "Bleh."
    pc "..."
    $ player.vodka()
    pcm "Phew..."

    jump travel

label haven_sold_ending_training_6:
    $ loc_haven_cell.dict["training_stage"] += 1
    pcm "He's here..."
    show haven_guardcell with dissolve
    pc "Welcome."
    haventrainer.name "Thank you."
    haventrainer.name "Have something more for you to drink. Here."
    pc "Thank you..."
    haventrainer.name "Drink up."
    pc "Now?"
    haventrainer.name "You will want to have that in you for what comes next."
    pc "What? I didn't do anything wrong!"
    haventrainer.name "No you didn't. That's why you are getting good food and drinks."
    $ player.face_meek()
    pc "You want to fuck me...?"
    haventrainer.name "No, I want you to fuck me."
    pc "Oh?"
    pc "..."
    $ player.vodka()
    pc "Phew..."
    pc "..."
    $ player.vodka()
    pc "Ugh..."
    pc "..."
    haventrainer.name "Ready?"
    pc "..."
    $ player.face_normal()
    pc "Can I wait until it kicks in?"
    haventrainer.name "It will kick in while we are getting ready."
    haventrainer.name "I am going to lay on the bed and you will do all the work. The faster you make me cum the faster I leave. So do a good job."
    pc "..."
    haventrainer.name "Come on, get on."
    pc "Ok..."
    show haven_gangbang penisup noplug at right with dissolve
    haventrainer.name "Good girl."
    pc "..."
    pc "Now what?"
    haventrainer.name "Up to you. I can lay here all day playing with your tits. If that's what you want then good job."
    pc "..."
    pcm "I really am going to have to fuck him to get rid of him..."
    pc "..."
    $ player.sex_vag(havenbrothel, main_quest_05)
    show haven_gangbang penisvag with dissolve
    haventrainer.name "Mmmm that's better."
    pcm "Just ride him and hopefully he doesn't last too long."
    haventrainer.name "Should consider showing your tits off while riding. Easier to get off when I have something nice to look at."
    haventrainer.name "Also makes my cock go in deeper. Gives you the chance to give longer strokes and make me cum faster."
    pc "..."
    hide haven_gangbang
    show haven_cowgirl stern
    with dissolve
    pc "Like this?"
    haventrainer.name "Much better."
    haventrainer.name "Ride with deep strides."
    pc "Hmmmm."
    pc "Why are you telling me this?"
    haventrainer.name "To make you better at this."
    pc "What for?"
    haventrainer.name "Think you are the only one who gets punished?"
    pcm "Huh?"
    haventrainer.name "In future, consider a smile or dirty words. Telling someone how much you love their cock will get them to the point quicker."
    pc "..."
    haventrainer.name "Mmmm, but being this deep is nice."
    with hpunch
    pc "Ahh."
    with hpunch
    pc "Now it is you that's moving."
    haventrainer.name "Won't always be able to get your way."
    with hpunch
    $ player.sex_cum(havenbrothel, "inside", main_quest_05)
    haventrainer.name "Ahhhhhh!"
    hide haven_cowgirl
    show haven_gangbang penisvag noplug at right
    with dissolve
    haventrainer.name "Ahhhh haaaaaa..."
    haventrainer.name "That was good."
    pc "Was it?"
    haventrainer.name "Yes. Keep this up and you will always have nice food and something to drink."
    pcm "Fuck."
    pc "Ok..."
    hide haven_gangbang with dissolve
    haventrainer.name "Make sure to clean up."
    pc "..."
    pc "Goodye."
    haventrainer.name "Hmmm."
    hide haven_guardcell with dissolve
    pcm "Fuck fuck..."
    pc "..."

    jump haven_sold_ending_shower_rep

label haven_sold_ending_training_7:
    $ loc_haven_cell.dict["training_stage"] += 1
    pcm "He's coming in again..."
    show haven_guardcell with dissolve
    pc "Welcome."
    haventrainer.name "Good. Try again with a smile. Even if it's a fake one."
    $ player.face_meek()
    pcm "Going to get beaten at some point if I don't try..."
    pc "..."
    $ player.face_happy()
    pc "Welcome."
    haventrainer.name "Better."
    $ player.face_normal()
    haventrainer.name "Here, something more to drink."
    haventrainer.name "And something extra. It's a bit better than the shitty booze."
    pc "Thank you."
    haventrainer.name "Mmmm."
    pc "Goodbye."
    haventrainer.name "Smile."
    $ player.face_happy()
    pc "Goodbye."
    haventrainer.name "Mm"
    hide haven_guardcell with dissolve
    $ player.face_normal()
    pc "..."
    $ player.vodka()
    pcm "Some Joy as well?"
    $ player.add_perk(perk_joy, hours=4)
    $ player.add_mood(200)
    pcm "Wash it down..."
    $ player.vodka()
    pc "Uggghh!"
    pcm "Stuff tastes like shit..."
    $ player.vodka()
    pc "Ubbbb."
    pc "Whoooo!"
    pc "Too much..."
    show haven_lament_sleep with dissolve
    $ player.eye = 3
    pcm "Ugggg. Too much too much..."
    show screen blackout(100) with Dissolve(1)
    show screen blackout(100) with Dissolve(1)
    pause 1
    $ time_sleep(230)
    hide screen blackout with Dissolve(1)
    hide haven_lament_sleep with dissolve
    $ player.face_normal()
    show haven_lament with dissolve
    pcm "Huh?"
    pcm "..."
    hide haven_lament with dissolve

    jump haven_sold_ending_shower_rep

label haven_sold_ending_training_8:
    $ loc_haven_cell.dict["training_stage"] += 1
    pcm "I hear the keys."
    show haven_guardcell with dissolve
    pc "Welcome."
    haventrainer.name "The smile?"
    $ player.face_happy()
    pc "Welcome."
    haventrainer.name "Thank you. I have brought someone for you to keep company."
    $ player.face_conf()
    pc "Huh what?"
    haventrainer.name "Just like with me. Sit on him and make him happy."
    $ player.face_worried()
    pc "What no nononono no please."
    haventrainer.name "You know what happens if you refuse. Just get this done as quick as you can and be done with it."
    pc "But I-"
    haventrainer.name "You know what happens if you refuse."
    $ player.face_meek()
    pc "..."
    haventrainer.name "Good. Lay on the bed."
    pc "..."
    show haven_fish nosex at right with dissolve
    haventrainer.name "Great, I'll send him in."
    pc "..."
    havenbrothel.fullname "What's this? She is all beaten up."
    haventrainer.name "And don't make it any worse. I will be outside."
    hide haven_guardcell
    pcm "Fuck!"
    havenbrothel.fullname "Whatever."
    show haven_fish sex with dissolve
    pcm "Fuck. Nothing I can do..."
    with hpunch
    $ player.sex_vag(havenbrothel, main_quest_05)
    pc "Nnng."
    havenbrothel.fullname "Mmm, tasty little whore."
    with hpunch
    pcm "Ow ow."
    with hpunch
    pcm "Why is this happening..."
    with hpunch
    pcm "..."
    with hpunch
    pcm "Please hurry..."
    pcm "..."
    with hpunch
    $ player.sex_cum(havenbrothel, "inside", main_quest_05)
    havenbrothel.fullname "Ahhhhhhh!!!"
    pcm "Hurry..."
    pcm "Shut up talking and go away..."
    havenbrothel.fullname "...little whores need a good..."
    pcm "Go away go away!"
    show haven_fish nosex with dissolve
    pcm "..."
    pcm "Go away..."
    pcm "Please come and save me [emile.name]..."
    hide haven_fish
    show haven_guardcell
    with hpunch
    haventrainer.name "Snap out of it!"
    pc "Wha?"
    haventrainer.name "I said good job. Here, have these drinks and some joy to calm you down."
    pc "..."
    haventrainer.name "Oh? Don't want them? Okay then I w-"
    pc "Yes I want them."
    haventrainer.name "Ok, so what do you say?"
    pc "Thank you!"
    haventrainer.name "Hrmf. Enjoy them and shower before you pass out."
    pc "I will. Goodbye."
    hide haven_guardcell with dissolve
    $ player.vodka()
    $ player.add_perk(perk_joy, hours=4)
    $ player.add_mood(200)
    pc "Ugh."
    pc "..."
    pcm "Can't believe that happened..."
    $ player.vodka()
    pc "Ubb."
    pc "..."
    show shower with dissolve

    if player.is_dirty():
        pcm "Better clean up or else I will get beaten again..."
    else:
        pcm "Not really dirty but don't want to risk another beating..."
    $ player.shower()
    $ acc.makeup_on = False
    $ working(20)
    hide shower with dissolve
    pcm "That really happened..."

    jump haven_sold_ending_bed_rep

label haven_sold_ending_training_9:
    $ loc_haven_cell.dict["training_stage"] += 1
    pcm "He's coming here again..."
    show haven_guardcell with dissolve
    $ player.face_happy()
    pc "Welcome."
    haventrainer.name "Good job."
    $ player.face_normal()
    haventrainer.name "Here. Something for you to drink."
    pc "Thank you."
    haventrainer.name "Don't save it. Drink it up and shower. The next time that door opens it won't be me coming in."
    pc "What?"
    haventrainer.name "There will be someone else for you to make feel welcome. Remember to smile and to help them get off as quickly as possible to get it over with."
    $ player.face_meek()
    pc "Ok..."
    haventrainer.name "And take these. It will make everything easier."
    pc "..."
    pc "Thanks..."
    haventrainer.name "Mmm."
    $ player.face_normal()
    pc "Goodbye."
    hide haven_guardcell with dissolve
    pcm "Fuck!"
    pcm "I just have to get through this and hold out for [tucker.name] and [emile.name] to come for me..."
    pcm "Hurry the fuck up!"
    $ player.vodka()
    pc "Bleh."
    pcm "Some Joy and what looks like Lebo..."
    $ player.add_perk(perk_joy, hours=4)
    $ player.add_mood(200)
    $ player.add_perk(perk_lebo, hours=4)
    $ player.add_desire(1000)
    pcm "Going to need this to be able to suffer my next visitor."
    show shower with dissolve
    pcm "Ugh. Keep clean for these shits..."
    $ player.shower()
    $ acc.makeup_on = False
    $ working(20)
    hide shower with dissolve
    pcm "Ok..."
    $ player.vodka()
    pc "Phew..."

    jump travel

label haven_sold_ending_training_10:
    pcm "Shit. I hear the door."
    $ male_npc_create_all()
    show male_generic at right1 with dissolve
    $ player.face_happy()
    pc "Welcome."
    pcm "Fuck fuck."
    havenbrothel.fullname "Mmm. Come here. Get on top."
    pcm "Shit. So he's just here to have sex with me?"
    pc "Ok."
    hide male_generic
    show haven_gangbang penisup noplug at right
    with dissolve
    havenbrothel.fullname "Girls here are supposed to be dirty little sluts. But hear you are new so I will go easy on you."
    pc "Yeah. I am new..."
    pcm "What the fuck There are other girls here?"
    $ player.sex_vag(havenbrothel, main_quest_05)
    show haven_gangbang penisvag with hpunch
    pc "Ahhh!"
    havenbrothel.fullname "Mmmm like that do you?"
    pcm "Fuck no it hurts."
    pc "Yes I do."
    with hpunch
    havenbrothel.fullname "Need to learn to lie better."
    havenbrothel.fullname "Ride me like the little slut you are."
    pc "Ok..."
    hide haven_gangbang
    show haven_cowgirl
    with dissolve
    pc "Like this?"
    havenbrothel.fullname "Mmm much better. Sexy tits you have."
    with hpunch
    pause 0.5
    with hpunch
    pause 0.5
    with hpunch
    havenbrothel.fullname "Mmmm, quiet type or just shy? Might wanna learn to talk some to entertain your guests."
    pc "I... Am new here..."
    pcm "Can't tell him I was kidnapped and forced here. Will end up dead for sure."
    with hpunch
    havenbrothel.fullname "Haaaa well your not doing too bad..."
    havenbrothel.fullname "Ahhh yesss."
    with hpunch
    havenbrothel.fullname "Ahhhhhhh fucckkkk!"
    with hpunch
    $ player.sex_cum(havenbrothel, "inside", main_quest_05)
    havenbrothel.fullname "Fuck yes take it!!"
    pc "Mmmmm give it to me..."
    havenbrothel.fullname "Haaaa. Nice. You will make it far in here."
    pcm "Yeah fucking right!"
    havenbrothel.fullname "Mmmm. I am done. Get up."
    pc "Ok."
    hide haven_cowgirl with dissolve
    pc "Hope you had fun. Goodbye."
    pcm "Fuck!"
    havenbrothel.fullname "Mmm, I did."
    hide shadm with dissolve
    pc "..."
    $ player.face_cry()
    pc "*SOB*"
    show shower with dissolve
    pc "..."
    pcm "Better clean up before he the guard comes back and beats me up..."
    $ player.shower()
    $ acc.makeup_on = False
    $ working(20)
    hide shower with dissolve
    pc "..."
    show haven_guardcell with dissolve
    haventrainer.name "..."
    $ player.face_happy()
    pc "Welcome."
    haventrainer.name "Good job."
    $ player.face_normal()
    pc "..."
    haventrainer.name "Here, have something nice to eat and drink then get some sleep. Things will be busier from here on."
    pc "What?"
    haventrainer.name "Don't worry. Be a good girl and everything will be ok."
    pc "..."
    $ player.face_happy()
    pc "Goodbye."
    haventrainer.name "Mmm, sleep well."
    hide haven_guardcell with dissolve
    $ player.face_normal()
    pcm "Fuck. Busier?"
    $ player.face_cry()
    pc "*SOB*"
    pcm "They will be here any moment. Come on [emile.name]..."
    $ player.vodka()
    pc "Ughhhh."
    pc "..."
    show haven_lament_sleep with dissolve
    pause 1
    show screen blackout(100) with Dissolve(1)
    $ time_sleep(230)
    pause 1

    hide screen blackout with Dissolve(1)



    pause 1



    hide haven_lament_sleep with dissolve
    pause 0.5


    "The new day brings much of the same and men come, have their way with me and leave. Sometimes they are rough and sometimes not. But it's clear that they see me only as is a body to please them."
    show haven_fish sex at right with dissolve
    pcm "[emile.name] will come. It will be over soon..."
    pcm "Just need to wait..."
    hide haven_fish
    show haven_lament at right2
    with dissolve
    pcm "They know where I am. Just a matter of time..."



    show screen blackout(100) with dissolve
    $ haven_sold_passtime(1)
    pause 0.5
    call haven_sold_ending_birth_call from _call_haven_sold_ending_birth_call
    $ player.face_worried()
    hide screen blackout with dissolve

    pcm "They won't forget about me..."
    $ haven_sold_passtime(1)
    show haven_fish sex at right
    hide haven_lament
    with dissolve
    pcm "It's only been a week. They probably still think I am in Haven. They will notice soon."
    pcm "Sure, I wasn't supposed to be in there that long so they will notice..."
    $ haven_sold_passtime(1)
    show haven_gangbang noplug at right
    hide haven_fish
    with dissolve
    pcm "Any moment they will come. It won't be much longer..."



    show screen blackout(100) with dissolve
    pause 0.5
    call haven_sold_ending_birth_call from _call_haven_sold_ending_birth_call_1
    show haven_lament_open at right2
    hide haven_gangbang
    $ haven_sold_passtime(1)
    $ player.face_worried()
    hide screen blackout with dissolve

    pcm "Come on..."
    pcm "Come through the door and get me out of here..."
    hide haven_lament_open
    show haven_cowgirl stern
    with dissolve
    pcm "Please [emile.name]..."
    pcm "*SOB*"
    pcm "Please don't leave me here."



    show screen blackout(100) with dissolve
    pause 0.5
    hide haven_cowgirl
    call haven_sold_ending_birth_call from _call_haven_sold_ending_birth_call_2
    show haven_lament at right2
    $ haven_sold_passtime(5)
    $ player.face_worried()
    pause 0.5
    hide screen blackout with dissolve


    pcm "Why aren't they here yet?"
    pcm "Please, don't forget about me..."
    hide haven_lament
    show haven_fish sex at right
    with dissolve
    pcm "I am not sure how much more of this I can take."

    show screen blackout(100) with dissolve
    pause 0.5
    hide haven_fish
    call haven_sold_ending_birth_call from _call_haven_sold_ending_birth_call_3
    show haven_lament at right2
    $ haven_sold_passtime(5)
    $ player.face_worried()
    pause 0.5
    hide screen blackout with dissolve

    pcm "..."
    pcm "They gave up on me..."
    pcm "It's been weeks..."
    pcm "No one is coming..."
    $ player.face_cry()
    pcm "*SOB*"
    pc "*SOB SOB*"




    show screen blackout(100) with dissolve
    hide haven_lament
    call haven_sold_ending_birth_call from _call_haven_sold_ending_birth_call_4
    show haven_lament_open at right2

    $ haven_sold_passtime(5)
    pause 0.5

    $ player.face_normal()
    $ player.face_worried()
    hide screen blackout with dissolve

    pcm "No way I am getting through the door..."
    pcm "Only time it is open is when someone is coming in. I could rush them and try and get out."
    pcm "*Sigh* No way I am strong enough to push past them. It would just get me a beating."
    pc "*SOB*"
    pcm "Maybe if he beats me bad enough, they will have to take me to a hospital."
    pcm "..."
    pcm "Yeah right. Probably just let me die in here."
    pcm "..."
    pcm "Might be my only way out..."


    show screen blackout(100) with dissolve
    hide haven_lament
    call haven_sold_ending_birth_call from _call_haven_sold_ending_birth_call_5

    show haven_fish sex at right

    $ haven_sold_passtime(5)
    pause 0.5
    $ player.face_normal()
    $ player.face_worried()
    hide screen blackout with dissolve

    pcm "If I just bite him in the face."
    pcm "Maybe he will kill me..."
    pcm "Maybe..."
    pc "*SOB*"
    pcm "I can't..."



    show screen blackout(100) with dissolve
    hide haven_fish
    call haven_sold_ending_birth_call from _call_haven_sold_ending_birth_call_6
    show haven_cowgirl stern

    $ haven_sold_passtime(5)
    pause 0.5
    $ player.face_normal()
    $ player.face_worried()
    hide screen blackout with dissolve

    pcm "Just do as they say and they don't hit me."
    pcm "They also give me sweets if I make someone happy..."
    show haven_cowgirl happy with dissolve
    pc "You like it when I do this?"
    $ player.sex_cum(unknown, "inside", main_quest_05)
    pc "Ah yes you do!"






    show screen blackout(100) with dissolve
    hide haven_cowgirl
    call haven_sold_ending_birth_call from _call_haven_sold_ending_birth_call_7
    show haven_spitroast at right

    $ haven_sold_passtime(5)
    pause 0.5
    hide screen blackout with dissolve


    pcm "At least they feed me and don't hit me anymore."
    pcm "As long as I do what I am told."
    pcm "It's not too bad..."
    show haven_gangbang noblow down noplug at right
    hide haven_spitroast
    with dissolve
    pcm "It's ok. I can make them happy."
    show haven_gangbang manblow blow with dissolve
    mem "It is why I am here. I can be happy as well."
    mem "Just make them happy and they will be nice to me."
    mem "They will be good to me and not beat me."
    show haven_gangbang anal with dissolve
    mem "It's why I am here. I am good at pleasing them."
    mem "They like me so why shouldn't I?"
    show screen blackout(100) with dissolve
    hide haven_gangbang
    call haven_sold_ending_birth_call from _call_haven_sold_ending_birth_call_8
    show haven_spitroast at right
    $ haven_sold_passtime(5)
    hide screen blackout with dissolve
    me "Mmffff."
    me "So good. Ah yes fuck me! Love me!"
    show haven_gangbang noblow down noplug at right
    hide haven_spitroast
    with dissolve
    me "Ah fuck yes. Give it to me!"
    $ player.spank()
    $ player.face_happy()
    me "Mmm, harder."
    $ player.spank()
    me "Harder!"
    $ player.spank()
    me "HARDER!"
    $ player.spank()
    $ player.sex_cum(unknown,"self")
    $ player.face_orgasm()
    me "Fuck YES!"


    show screen blackout(100) with dissolve
    hide haven_gangbang
    call haven_sold_ending_birth_call from _call_haven_sold_ending_birth_call_9
    show haven_cowgirl
    $ haven_sold_passtime(10)
    hide screen blackout with dissolve

    me "Ah you are so big you sexy beast!"
    me "I love it! How much it fills me up!"
    havenbrothel.fullname "Ah you like it do you?"
    me "Fuck yes. Give it to me."
    havenbrothel.fullname "You fat bitch. Take it all the way."







    show screen blackout(100) with dissolve
    hide haven_cowgirl
    call haven_sold_ending_birth_call from _call_haven_sold_ending_birth_call_10
    show haven_lament_open at right2
    $ haven_sold_passtime(10)
    hide screen blackout with dissolve

    mem "Who will be next?"
    mem "Come on, open the door and love me."
    mem "I am here for you waiting."

    show screen blackout(100) with dissolve
    pause 0.5
    hide haven_lament_open
    call haven_sold_ending_birth_call from _call_haven_sold_ending_birth_call_11
    $ haven_sold_passtime(10)
    hide screen blackout with dissolve


    mem "Need to make sure to stay washed. So many people to love me so I will get dirty."
    hide haven_lament with dissolve
    show shower with dissolve
    mem "They like me clean. So need to wash."
    mem "Wash me, please me, wash me, please me."
    hide shower with dissolve
    mem "..."
    show haven_lament_open at right2 with dissolve
    mem "Why are you making me wait?"

    show screen blackout(100) with dissolve
    call haven_sold_ending_birth_call from _call_haven_sold_ending_birth_call_12
    pause 0.5
    hide screen blackout with dissolve

    mem "Lot of noise outside today. Must be busy."
    mem "Sounds like a party."
    hide haven_lament_open
    show police_gen mask at right1
    show police_gen2 mask at right3
    with dissolve

    $ player.face_happy()
    me "Ah, come in. ♥"
    police.name "[fname]?"
    $ player.face_happy()
    me "I can be. What should I call you?"
    police.name "Are you [fname] [sname]?"
    me "I will be what you want. ♥"
    police.name "*Radio* [cam.name]. We think we found her, but it's not good."
    cam.name "*Radio* Just get her out of there!"
    me "Ok, so are you going to undress or do you want me to do it for you?"
    police.name "Come with us."
    $ player.face_worried()
    me "Err. No. I can't leave the room. We will have fun here."
    police.name "Quickly [fname]! Come with us!"
    $ player.face_shock()
    with hpunch
    me "No! Get off me! AHHHHAHHAHAHA!!! STOPPP!!!!!"
    police.name "Fuck!"
    police.name "Shut her up!"
    show screen hooded(_layer="master") with hpunch
    me "Ahhhhhh! Mmmffffffff!!"
    with hpunch
    me "Not allowed to leave!!"
    with hpunch
    havmuff "...not cooperative..."
    havmuff "...sedation..."
    me "GET OFF GET OFF GET OFF GET OFF!!!"
    me "Get off... Get... oooofffff..."

    show screen blackout(50) with dissolve
    me "Get..."
    me "Oooooffff..."
    show screen blackout(100) with dissolve
    pause 1
    $ renpy.hide_screen("hooded", layer="master")
    hide police_gen
    hide police_gen2


    $ c.outfit = 1
    $ walk(loc_hospital_ward)
    $ t.pass_time(1)
    $ player.set_tired(50)
    $ player.set_mood(30)
    $ player.face_normal()
    $ player.eye = 3
    $ player.mouth = 8
    show nikolas at right1
    show tucker at right4:
        xzoom -1
    show screen blackout(75) with dissolve
    nik.name "...physically, but we can't be sure about..."
    show screen blackout(100) with dissolve
    $ t.pass_time(1)
    $ player.eye = 3
    $ player.mouth = 8
    hide tucker
    show emile suitshirt worried at right4:
        xzoom -1
    pause 0.5

    show screen blackout(75) with dissolve
    nik.name "...observation it's impossible to tell..."
    show screen blackout(100) with dissolve
    $ t.pass_time(1)
    $ player.eye = 3
    $ player.mouth = 8
    pause 0.5
    hide emile
    show nurse at right1
    show nikolas at right3

    show screen blackout(50) with dissolve
    me "Ugghhh..."
    nurse.name "Here we go. Gently now."
    show screen blackout (75) with dissolve
    $ player.eye = 2
    show screen blackout(50) with dissolve
    me "Uuuuggggg..."
    nurse.name "Gently..."
    $ player.face_shock()
    hide screen blackout with hpunch
    me "Where am I???"
    nurse.name "You are..."
    me "No no no no no!"
    me "No please why am I here?"
    me "Where is my room!?"
    nik.name "Sedate her! Quickly!"
    nurse.name "Yes!"
    me "No no please no!"
    me "Nooooo..."
    show screen blackout(50) with dissolve
    $ player.eye = 3
    me "Not... allowed..."
    show screen blackout(100) with dissolve
    pause 0.5
    $ t.pass_time(1)
    $ player.eye = 3
    $ player.mouth = 8
    pause 0.5


    show screen blackout(75) with dissolve
    me "Uwwwaaa..."
    $ player.eye = 2
    nik.name "That's right, just a little bit."
    show screen blackout(50) with dissolve
    me "Uhhhhh... Where am I?"
    nurse.name "You are in a hospital. You are safe now."
    me "Safe?"
    me "Wait? Where is my room? Why am I here?"
    show screen blackout(25) with dissolve
    nurse.name "It's alright. Everything is ok. You don't have to go back there anymore."
    me "What? Why not? I can't go back?"
    hide screen blackout with dissolve
    nurse.name "You are here now and your sister is waiting for you."
    me "Who?"
    nurse.name "[emile.name]. She is here for you. She misses you."
    me "..."
    me "[emile.name]?"
    nurse.name "Yes. She missed you ver..."
    $ player.face_worried()
    me "[emile.name] didn't come for me!"
    with hpunch
    $ player.face_shock()
    me "NONONO NO NO NO!!!"
    me "GO AWAY!!"
    nik.name "*Sigh* Sed..."
    nurse.name "Yes [nik.name]."
    show screen blackout(50) with dissolve
    $ player.eye = 3
    me "Did... n't... come..."
    show screen blackout(100) with dissolve
    pause 0.5
    $ t.pass_time(5)
    $ player.face_normal()
    hide nikolas
    call haven_sold_ending_hospital_birth_call from _call_haven_sold_ending_hospital_birth_call
    show nurse at right4

    hide screen blackout with dissolve
    nurse.name "...good care of here. And when you are feeling up to it we can..."
    show screen blackout(100) with dissolve
    hide nurse
    show brooker at right1
    $ t.pass_time(6)
    $ walk(loc_hospital_psy)
    $ player.mouth = 8
    hide screen blackout with dissolve
    psy.name "...at all to be ashamed of. No one could have..."
    show screen blackout(100) with dissolve
    $ t.pass_time(2)
    $ walk(loc_hospital_ward)
    show emile at right4
    hide brooker
    hide screen blackout with dissolve
    emile.name "...and when the car came, it ended up running over his foot instead of..."
    show screen blackout(100) with dissolve
    hide emile
    $ t.pass_time(10)
    call haven_sold_ending_hospital_birth_call from _call_haven_sold_ending_hospital_birth_call_1
    $ player.add_mood(30)
    $ player.add_tired(50)
    $ walk(loc_hospital_office)
    show tucker at right1
    hide nurse
    hide nikolas
    $ player.face_worried()
    hide screen blackout with dissolve
    tucker.name "...was unable to track your precise location due to the tracker being removed. But fortunately they didn't know what it was so threw all your belongings away in tip nearby."
    tucker.name "So we knew you were somewhere close, but not what building. We couldn't just go kicking doors down to find you because that might get the rats to run somewhere else."
    tucker.name "So had no choice but to observe the whole area and look for suspicious activity..."
    show screen blackout(100) with dissolve

    hide tucker
    $ t.pass_time(5)
    call haven_sold_ending_hospital_birth_call from _call_haven_sold_ending_hospital_birth_call_2
    $ tattoo.chest = 0
    $ tattoo.ass = 0
    $ player.eye_liner = 1
    show brooker at right1



    $ walk(loc_hospital_psy)
    $ player.face_normal()
    hide screen blackout with dissolve
    psy.name "Won't be long until we will be sending you home. How do you feel about that?"
    pc "Dunno. Might be good to get some fresh air."
    psy.name "How do you feel about [emile.name] joining you where you live?"
    $ player.face_meek()
    pc "..."
    pc "Okay I suppose..."
    psy.name "Do you still hold resentment towards her for not being able to come for you?"
    pc "..."
    pc "Probably."
    pc "I know there wasn't much she or [tucker.name] could have done."
    pc "Doesn't make it much easier though."
    psy.name "I see."
    psy.name "You do understand why we want [emile.name] with you right?"
    pc "To stop me from killing myself if I decide to?"
    psy.name "Not quite how I would put it. She will be there to help you adjust back into a normal routine and to help out where you might need."
    pc "And to keep an eye on me."
    psy.name "It is for your own wellbeing."
    pc "Yeah, I'm sure the men in my cell would have said the same thing if they thought it would make it easier to trick me."
    psy.name "We only want what's best."
    pc "Then maybe you should stop using the same words as the people who harmed me..."

    show screen blackout(100) with dissolve
    $ t.pass_time(1)
    call haven_sold_ending_hospital_birth_call from _call_haven_sold_ending_hospital_birth_call_3
    pause 0.5
    $ player.face_normal()
    $ player.mouth = 8
    hide screen blackout with dissolve

    psy.name "...you think you will be up for a talk with [tucker.name]? A quick debrief on the mission before you leave to go home?"
    pc "There isn't a lot to tell him, so it should be fine. Prefer to get it over with now than come back here afterwards."
    psy.name "Ok, well when you think you are up to it, I will arrange a time..."


    show screen blackout(100) with dissolve
    $ t.pass_time(3)


    hide brooker
    call haven_sold_ending_hospital_birth_call from _call_haven_sold_ending_hospital_birth_call_4
    show tucker at right1
    $ walk(loc_hospital_office)
    hide screen blackout with dissolve


    tucker.name "...if you are not up to it, we can arrange..."
    pc "I would prefer it if we got it over with."
    tucker.name "Ok, as you wish. So I will cut right to the chase. Were you able to find out [ant.name]'s location?"
    pc "Sort of. He was never at [haven]. It seems he approached [alex.fname] [alex.sname] for something. Drug related I think. Production of something that [alex.fname] [alex.sname] thought would be harmful to the people of [haven] anyway."
    pc "[alex.fname] [alex.sname] had no interest in it and cast [ant.name] out of [haven] long before I even arrived."
    tucker.name "Were you able to find out where he went."
    pc "Possibly. Something about \"The Twins\". He went to whoever or whatever they are. Pretty sure a \"who\" since [alex.fname] [alex.sname] said I should speak to them."
    tucker.name "Hmm, ok. Well that should be enough to get the ball rolling anyway. So I'll call an end to this and you can go and relax..."
    show screen blackout(100) with dissolve

    hide tucker

    $ walk(loc_hospital_ward)

    $ player.add_money((main_quest_05.reward * 15) + main_quest_05.reward_counter)
    $ inv_transfer(inv_backup, inv)
    $ inv.drop([item_haven_crowbar, item_haven_intel, item_haven_lighter, item_haven_fluid], 50)

    $ player.hair_style = "loose"


    $ pc_set_outfit("daily")
    $ pc_dress()
    show emile suitvest at right1
    pause 0.5
    hide screen blackout with dissolve
    emile.name "Got everything?"
    pc "Think so."
    emile.name "Great. Let's go."
    pause 0.5
    $ walk(loc_hospital_entrance)
    emile.name "This the first time you have been outside?"
    pc "No, I walked around the backyard and carpark. No cars there anymore so it was always empty."
    emile.name "Ok, well if you are feeling overwhelmed, tell me and we can have a rest."
    pc "Mmm."
    show emile neutral
    emile.name "Ok..."
    $ walk(loc_hospital_entrance)
    pc "Brings back memories actually."
    emile.name "What does?"
    pc "Leaving the hospital again with you."
    emile.name "Ah."
    $ player.face_meek()
    pc "..."
    pc "Can't really have anything good anymore can we?"
    emile.name "Huh?"
    $ player.face_worried()
    pc "Twice I have left this hospital with something horrible behind me..."
    pc "Won't be the last time though will it?"
    show emile worried
    emile.name "I..."
    hide emile
    $ walk(loc_market)
    pc "..."
    show emile suitvest at right1 with dissolve
    emile.name "Why such a rush?"
    pc "The weather is different."
    emile.name "It is?"
    if t.month == "Winter":
        pc "Snow is everywhere now. Wasn't anything like this when I walked to [haven]."
    elif t.month == "Autumn":
        pc "The trees are starting to loose their leaves. I remember walking to [haven] in the snow."
    elif t.month == "Spring":
        pc "Was a nice Summers day when I walked to [haven]. Now it looks like winter has just ended."
    else:
        pc "The leaves had already been falling when I walked to [haven] and now It is a nice Summers day."
    emile.name "Ah..."
    $ player.face_meek()
    pc "..."
    $ player.face_normal()
    pc "Ok..."
    $ walk(loc_revel)
    $ player.face_worried()
    pc "..."
    pc "Not going in there again are we?"
    emile.name "No, let's get you home."
    pc "Actually been a while. Why do I still have a place there?"
    emile.name "I have been living there while you were away. It is closer to where I was living before so I could get to and from The Institute quicker."
    $ player.face_meek()
    pc "Oh..."
    pc "Ok..."
    $ walk(loc_residential)
    emile.name "You ok?"
    pc "*Sigh*"
    pc "Yeah I suppose."
    $ walk(loc_stairwell)
    pc "..."
    emile.name "Let's head inside."
    $ walk(loc_kitchen)
    pause 0.5
    $ walk(loc_bedroom)
    pcm "Mostly looks the same I suppose."
    emile.name "I hope you don't mind too much."
    pc "Mind what?"
    emile.name "Us staying together."
    pcm "Not much choice in the matter even if I did mind."
    emile.name "Not a lot of room, but I think we can make do."
    pc "Yeah..."
    emile.name "..."
    pc "..."
    emile.name "Ok... Then I will let you get comfortable."
    emile.name "..."
    emile.name "If you want to talk, I will be here."
    pc "Ok."
    hide emile with dissolve
    pcm "What am I even supposed to do?"
    pcm "*Sigh* Maybe I should go for a walk or something instead of just hanging around here."
    pcm "Get away from [emile.name] for a bit at least."
    $ add_to_list(main_quest_05.list, "slave")
    $ player.add_perk(perk_whore)
    $ player.add_perk(perk_broken)
    $ player.add_perk(perk_joy_addict, days=5)
    $ player.add_perk(perk_alcoholic, days=7)
    $ player.preg_desire = 0
    $ player.check_preg_desire()
    $ player.description_sex()
    $ player.add_tired(60)
    $ player.add_mood(30)
    $ player.add_conf(-100)
    $ player.remove_fitness(100)
    $ player.remove_int(100)
    $ log.markdone("mq_05_slave_a")
    $ rent_pay(rent_total_owed(), cash=False, notif=False)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
