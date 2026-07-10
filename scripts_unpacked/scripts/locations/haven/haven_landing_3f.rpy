label haven_landing_3f_arrival:

    if not haven_guard_hours():
        if havenmeanguard.has_met:
            pcm "It's that guard who is an arse. I shouldn't try and speak to him."
        else:
            show haven_guard2 at right1 with dissolve
            havenmeanguard.name "Sod off. Not allowed up ere."
            $ player.face_worried()
            pc "Sorry."
            hide haven_guard2 with dissolve
            if not havengateguard.has_met:
                pcm "Well he seems like a cunt. Maybe I can wait until another guard is on shift and see if he is any nicer."
            else:
                pcm "I should probably avoid him and stick to talking to the nice guard."
        $ player.face_normal()
        jump travel
    else:

        if haven_guard_smoking():
            jump haven_landing_3f_guard
        elif havengateguard.has_met and havengateguard.spoke_to_hours_ago <= 2 and not "asked_lighter" in havengateguard.conversation_topics:
            pcm "I shouldn't seem too eager to speak to him or else he might get suspicious. I should come back after a few hours."
            jump travel

        elif "rejected_sex" in havengateguard.conversation_topics and haven_days() >= 5:


            pcm "I am not making much progress on getting up there any other way. Should I take him up on his earlier offer to stay with him?"
            menu:
                "No, speak to him normally":
                    jump haven_landing_3f_guard
                "Maybe I should":

                    jump haven_landing_3f_sex
        else:

            jump haven_landing_3f_guard



label haven_landing_3f_guard:
    if not havengateguard.has_met:
        $ havengateguard.dict["times_spoke"] = 0
        show haven_guard1 at right1 with dissolve
        havengateguard.name "Sorry love, not allowed up here."
        pc "Err, no problem. I'm just walking around killing time."
        havengateguard.name "Mmm."
        hide haven_guard1 with dissolve
        pcm "Doesn't look like he will leave very easily but he isn't some pro security guard so there must be something I can do to dislodge him."
        pcm "If I could kick up some kind of ruckus, he and his cronies upstairs would no doubt come down to see what's going on."
        pcm "Would have to be a pretty big commotion though. I can't expect them to come running if I just start screaming. Needs to be something that could threaten [alex.name] or this building."
        pcm "Suppose I could also try to sweet talk him and see how that goes."
        $ log.activate("mq_05_guard", notify=True)
        jump travel

    elif havengateguard.dict["times_spoke"] < 5:


        if havengateguard.dict["times_spoke"] == 0:
            $ havengateguard.dict["times_spoke"] += 1
            pcm "For now I should just chat with him and see if an opportunity to get upstairs comes up. Just be casual and nice."
            show haven_guard1 at right1 with dissolve
            pc "Must be bored stiff sitting there all day like that."
            havengateguard.name "Tell me about it. Can hardly feel my arse when I go back upstairs after my shift."
            pc "No breaks to stretch your legs?"
            havengateguard.name "Pfft, yeah right."
            "I spend the next few minutes having a chat with the guard."
            $ relax(5)
            havengateguard.name "Anyway, I should get back to it. Don't want to look like I spend all day chatting with pretty girls."
            pc "Sure, have fun."
            hide haven_guard1 with dissolve
            jump travel

        elif havengateguard.dict["times_spoke"] == 1:
            $ havengateguard.dict["times_spoke"] += 1
            show haven_guard1 at right1 with dissolve
            pc "Hey, how's things?"
            havengateguard.name "Same as. Sittin here as always and hoping my brain doesn't turn to mush from boredom."
            pc "Boredom? What's there to be bored about when you can watch the rats running by or count the cockroaches?"
            havengateguard.name "Maybe I should start catching the rats and sell them grilled. Make a bit of extra cash."
            pc "With a cockroach sauce."
            havengateguard.name "Mmm, that will get them downstairs salivating."
            "I joke around with the guard a little more before letting him get back to his duties."
            pc "See you round."
            hide haven_guard1 with dissolve
            jump travel

        elif havengateguard.dict["times_spoke"] == 2:
            $ havengateguard.dict["times_spoke"] += 1
            show haven_guard1 at right1 with dissolve
            pc "How's business?"
            havengateguard.name "Terrible, the rats aren't as easy to catch as you might think."
            pc "That's quitters talk."
            havengateguard.name "Yeah well sitting down all day is easier anyway."
            pc "Well, keep your guard up. Now you have provoked the rats they might come for revenge."
            havengateguard.name "I'll be ready."
            havengateguard.name "Hey, tell me. What you doing round these parts anyway?"
            pcm "Hmmm, what should I tell him?"
            pc "Looking for my brother. Heard he might have come here after he needed to get away from some people."
            havengateguard.name "Not seen him yet I guess."
            pc "Mmm, and can't even ask around much because who knows what name he had at the time. So have to ask for a guy with patchy skin."
            pcm "Fuck, was that too forward?"
            havengateguard.name "Well, good luck anyway."
            pc "Thanks."
            hide haven_guard1 with dissolve
            pcm "No reaction from him. Maybe for the best."
            jump travel
        elif havengateguard.dict["times_spoke"] == 3:
            jump haven_intel_13

        elif havengateguard.dict["times_spoke"] == 4:
            $ havengateguard.dict["times_spoke"] += 1
            show haven_guard1 at right1 with dissolve
            havengateguard.name "Still here? Looks like you'll be a while at this rate."
            pc "Well, not got anything better to do. So I just enjoy the lovely building and the fresh air the holes in the walls provide."
            havengateguard.name "Careful in the winter or you'll wake with a mouthful of snow."
            pc "Sleeping here, that would be one of the better things to wake with a mouthful of."
            havengateguard.name "Hah, true. Guess the zoo animals can get a bit pushy sometimes?"
            pc "You could put it that way."
            havengateguard.name "Well, keep safe."
            pc "You too."
            hide haven_guard1 with dissolve
            jump travel

    elif not "offered_sex" in havengateguard.conversation_topics:
        $ add_to_list(havengateguard.conversation_topics, "offered_sex")
        show haven_guard1 at right1 with dissolve
        havengateguard.name "Keeping safe?"
        pc "As best I can."
        havengateguard.name "Why not come up and stay with me? Will get you out of the zoo. Fewer rats as well."
        pc "Hmm, isn't that just swapping the zoo animals trying to put their cock in me to you putting yours in me?"
        havengateguard.name "I have a nicer bed and sometimes warm food."
        pc "Oh, you should become a salesman with a pitch like that."
        havengateguard.name "Well, not really trying to sell you on it. Just putting the offer out there."
        pc "Heh, I'll think about it."
        hide haven_guard1 with dissolve
        pcm "..."
        pcm "Not really the best of offers in the world, but it will get me past the gate..."
        if player.iswhore:
            pcm "Whored myself out for worse offers though and it would make it nice and simple getting up there."
        elif player.vvirgin:
            pcm "He is cute so could be worse ways to give up my virginity. Two birds with one stone."
        else:
            pcm "Am I really willing to go that far though?"
        jump travel

    elif "offered_sex" in havengateguard.conversation_topics and not "rejected_sex" in havengateguard.conversation_topics:
        show haven_guard1 at right1 with dissolve
        havengateguard.name "And my day gets a little brighter."
        pc "Trying the sweet talk now are we?"
        havengateguard.name "Not really. When you are sitting here all day then some company makes the day go by faster."
        pc "I bet."
        havengateguard.name "Speaking of, will you keep me company at night as well?"
        if player.has_perk([perk_sucu, perk_slut, perk_whore, perk_gamine, perk_bimbo], notif=True):
            pc "Is the bed really that much better?"
            havengateguard.name "Well, it's a bed. Don't remember seeing one of those downstairs last I was there."
            menu:
                "Sure, I'll keep it warm for you.":
                    $ log.markdone("mq_05_upstairs")
                    $ havguardw = Character('Haven gate guard', color="#ffffff")
                    pcm "Fucking him will get me upstairs pretty easily. Just have to hope I'm not biting off more than I can chew..."
                    havengateguard.name "Great. Hold on I'll open up."
                    havengateguard.name "Been a while since we've had someone upstairs."
                    pcm "\"We've had\"??"
                    pcm "Fuck..."

                    jump haven_landing_3f_sexcont
                "Na, I will stick to fending off the animals":

                    havengateguard.name "No worries. But for someone as cute as you, the offer still stands."
                    pc "I'll keep that in mind."
                    hide haven_guard1 with dissolve
                    pcm "Still need to find a way upstairs though."
                    $ add_to_list(havengateguard.conversation_topics, "rejected_sex")
                    jump travel

        pc "Sorry, you are cute an all. But whoring isn't really my thing."
        havengateguard.name "I knew that from the start. If I wanted a whore I would just go downstairs."
        havengateguard.name "Wanted us to keep each other company 'til you decide to move on since you seem quite nice. It's a change from what this place usually drags in."
        if player.check_sex_agree(4):

            pcm "Hmm, well he is kinda nice..."
            pcm "Should I enjoy some time with him?"
            menu:
                "Spend time with him":
                    pc "that... might be nice."
                    havengateguard.name "Yeah? Wow ok. Hold on..."
                    jump haven_landing_3f_sexcont
                "No, leave him alone":


                    $ NullAction()


        pc "That's sweet, but no thanks."
        havengateguard.name "No worries. But for someone as cute as you, the offer still stands."
        pc "I'll keep that in mind."
        hide haven_guard1 with dissolve
        pcm "Still need to find a way upstairs though."
        $ add_to_list(havengateguard.conversation_topics, "rejected_sex")
        jump travel

    elif not "asked_lighter" in havengateguard.conversation_topics:
        $ add_to_list(havengateguard.conversation_topics, "asked_lighter")
        show haven_guard1 at right1 with dissolve
        havengateguard.name "You don't happen to have a light do you? Someone made off with mine and I don't wanna keep going upstairs and asking for one or else they know I am not at my post."
        if inv.qty(item_haven_lighter):
            menu:
                "Sure, here you go.":
                    jump haven_landing_3f_pry_intro
                "No I don't":


                    $ NullAction()


        pc "No I don't, sorry."
        havengateguard.name "No? Shame. Wonder where I can get one from..."
        havengateguard.name "If you come across one, send it my way would you?"
        pc "Sure."
        hide haven_guard1 with dissolve
        jump travel

    elif "asked_lighter" in havengateguard.conversation_topics and not havengateguard.inv.qty(item_haven_lighter):
        show haven_guard1 at right1 with dissolve
        havengateguard.name "Not managed to get your hands on a lighter since last time I asked?"
        menu:
            "Yes, here is one." if inv.qty(item_haven_lighter):
                jump haven_landing_3f_pry_intro
            "No I haven't":

                havengateguard.name "Ah that's a shame. Well if you get your hands on one, give it to me will ya?"
                pc "Sure."
                hide haven_guard1 with dissolve
                jump travel

    elif havengateguard.inv.qty(item_haven_lighter):
        show haven_guard1 at right1 with dissolve
        pc "Hey."
        havengateguard.name "Back again? How's things?"
        $ relax(15)
        "I hang around having a bit of a chat with the guard to pass the time before heading off."
        if haven_guard_smoking():
            havengateguard.name "I'm gonna pop for a smoke. Back in a bit."
        else:
            pc "See you round."
        hide haven_guard1 with dissolve
        jump travel

label haven_landing_3f_pry_intro:
    $ inv.give(item_haven_lighter, havengateguard.inv)
    havengateguard.name "Ah nice, cheers."
    havengateguard.name "Err..."
    havengateguard.name "Ah fuck it, the gate is locked so it will be fine."
    $ havengateguard.active = False
    hide haven_guard1 with dissolve
    pcm "Looks like he is heading for the lounge to smoke."
    pcm "Right, let's have a look at this gate..."
    pcm "Can't just climb over it so need to go through it somehow."
    with hpunch
    "I give the gate a bit of a shake to see how sturdy it is."
    pcm "Gate itself seems pretty solid. Easiest way would probably to try and pry it directly from the walls since the building is falling apart. No doubt the walls are ready to give way."
    pcm "But that would cause a huge mess and I would be noticed right away..."
    pcm "No choice but to try and pry the bars apart enough to squeeze though or aim for the lock."
    pcm "Well, right now I just need to see how long he will take to have a smoke."
    $ walk(loc_haven_room3)
    pcm "..."
    $ stroll(10)
    "I hang around in the room waiting to hear him pass, all the while hoping some pervert doesn't notice me and try to join."
    pcm "There he goes. About 10 minutes. Need to keep that in mind when I next see him leave his post."
    $ loc_haven_landing.dict["gate_pry"] = 0
    $ havengateguard.active = True
    jump travel



label haven_landing_3f_pry:
    if loc_haven_landing.dict["gate_pry"] == 0:
        $ loc_haven_landing.dict["gate_pry"] += 1
        "I wedge the tool wherever it can find purchase and try to wiggle it around hoping to see where anything might be loose, which would be a good place to start."
        pcm "..."
        $ player.face_worried()
        pcm "What was that?"
        pause 0.5
        $ walk(loc_haven_room3)
        $ player.face_worried()
        pcm "..."
        pcm "Seems like it was nothing. Fuck, I can't be jumping at shadows while doing this."
        $ exercise(20)
        jump travel
    elif loc_haven_landing.dict["gate_pry"] == 1:
        $ loc_haven_landing.dict["gate_pry"] += 1
        pcm "Ok, let's try again."
        "Again I hook it where ever it can grip and start wiggling the tool around."
        pcm "Hmm, looks like the lock is just a latch. If I can pry the gate open it might still be able to shut again. Then no one will notice it was opened."
        $ exercise(20)
        pcm "Better stop for now since I have been here a while"
        jump travel
    elif loc_haven_landing.dict["gate_pry"] == 2:
        $ loc_haven_landing.dict["gate_pry"] += 1
        "I try to wedge the tool between the lock and the frame but it doesn't go in easy since I have so little leverage."
        pcm "Come on you damn door."
        pcm "..."
        $ exercise(20)
        $ player.face_worried()
        pcm "Fuck, footsteps behind me"
        "I slip the tool back in my shorts and try to look inconspicuous."
        show haven_guard1 at right1 with dissolve
        havengateguard.name "Hey [name]. Was smoking."
        $ player.face_happy()
        pc "Yeah thought as much so I just waited."
        havengateguard.name "Ah missing me that much were you?"
        $ player.face_neutral()
        pc "Well, not a lot else to do round here. And you are about the only one who doesn't try to get me naked in an empty room."
        havengateguard.name "Hmm, I wouldn't refuse that."
        pc "Ok, the only one who doesn't try to force me into an empty room."
        havengateguard.name "Hmmmm. Didn't realise that was an option. I could give it a try."
        pc "No, you wouldn't."
        "I flash him an innocent smile as I walk away."
        hide haven_guard1
        $ walk(loc_haven_room3)
        pcm "Fuck, he almost caught me."
        pcm "..."
        pcm "Ah, what am I doing in here? If he saw me come in here he might think it was an invitation."
        $ walk(loc_haven_lounge)
        jump travel
    elif loc_haven_landing.dict["gate_pry"] == 3:
        $ loc_haven_landing.dict["gate_pry"] += 1
        pcm "Right, I need to wedge this in a lot deeper so I can get some leverage."
        $ stroll(20)
        $ player.face_grit()
        with hpunch
        with vpunch
        pc "Shit!"
        $ walk(loc_haven_hallway_2f)
        pcm "Wasn't me..."
        jump travel
    elif loc_haven_landing.dict["gate_pry"] == 4:
        $ loc_haven_landing.dict["gate_pry"] += 1
        pcm "Silent as a mouse..."
        pcm "No one can hear me..."
        pcm "Like a ninja..."
        $ stroll(20)
        pcm "This is harder than I thought."
        $ walk(loc_haven_hallway_2f)
        pcm "Too aggressive and I make a load of noise, too timid and I can't get the bar in deep enough to gain any leverage."
        jump travel
    elif loc_haven_landing.dict["gate_pry"] == 5:
        $ loc_haven_landing.dict["gate_pry"] += 1
        pcm "Right, fuck it. This time I am just jamming it in there and to hell with the noise."
        $ player.face_grit()
        with hpunch
        with vpunch
        pcm "Shit, ok. O-pen you damn gate!"
        pcm "Yes, that's it that's it."
        $ stroll(20)
        pcm "..."
        pcm "Voices?"
        $ walk(loc_haven_hallway_2f)
        pcm "Yes, almost had it. Next time I am going to open that baby."
    else:
        $ loc_haven_landing.dict["gate_pry"] += 1
        pcm "Ok, jam it in there and put all my weight behind it."
        $ player.face_grit()
        with hpunch
        with vpunch
        pcm "And pull!"
        with hpunch
        with vpunch
        $ loc_haven_landing.dict["gate_open"] = True
        pcm "YES! Got it!"
        "I open the gate a bit and slip through to the other side."
        pcm "Ok, I need to close it so it doesn't look like someone broke in. Gonna make it hard to get back out though."
        pcm "I'll have to cross that bridge when I get there."
        $ loc_haven_landing.dict["gate_open"] = False
        "I shut the gate and scamper upstairs."
        $ add_to_list(main_quest_05.list, "gate_pry")
        jump haven_access_top_floor


    hide haven_guard1 with dissolve
    jump travel

label haven_landing_3f_sex:
    $ havguardw = Character('Haven gate guard', color="#ffffff")
    show haven_guard1 at right1 with dissolve
    pc "Hey, your offer still good?"
    havengateguard.name "What offer?"
    pc "To stay with you instead of with the fleas downstairs."
    havengateguard.name "Err, yeah sure. Hold on..."
    pcm "He seems far too eager..."

label haven_landing_3f_sexcont:
    $ loc_haven_landing.dict["gate_open"] = True
    havengateguard.name "Here we go. Come on up."
    pc "Ok..."
    $ walk(loc_haven_toplanding)
    pcm "Hope I made the right choice here..."
    $ walk(loc_haven_hallway_3f)
    pcm "Looks just as depressing here than it does downstairs. Thought things would be nicer since it's only for [alex.nname]'s goons."
    pcm "Not many places to go... Got two doors at the end and this blocked one. So [alex.nname] must be in one of the door's at the end."
    havengateguard.name "Here, this way."
    pcm "Ok. Well if he is inviting me in there then that must mean [alex.nname] is in the other room."
    $ walk(loc_haven_guardroom)
    havengateguard.name "Here we are. Home sweet home."
    pc "Errm..."
    pcm "Looks just like downstairs..."
    if player.vvirgin or player.vsex + player.asex < 10:
        jump haven_virginsex_ending
    else:
        jump haven_whore_ending
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
