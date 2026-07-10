label quest_mira_missing_cass_whore_clothes:
    $ cass.iswhore = True
    pcm "Right, [cass.name] wanted to meet around here. Should I look for her?"
    menu:
        "Look around for her":
            $ NullAction()
        "Not right now":
            pcm "Another time."
            jump travel


    pcm "Hmmm... Where is she?"
    pcm "Well, didn't really plan a time so I guess I'll wait around."
    pcm "..."
    if "cass_knows" in quest_whore.list:
        show cass slut at right1 with dissolve
        cass.name "What do you think?"
        pc "Err... it looks like you are going to do something you might regret."
        cass.name "If this helps find [mira.name] then I won't regret a thing."
        pc "And if it doesn't?"
        cass.name "Then it doesn't matter."
        pc "..."
        pc "Okay then. Let's go."
        if not c.slutty:
            cass.name "Shouldn't you also look the part?"
            pc "I'm already a whore. I'm not trying to fit in with them, I am them."
            cass.name "Right. Just me then."
            pc "Doesn't need to be."
        else:
            pc "You sure you want to do this?"
        show cass angry
        cass.name "Stop [name]! I am doing this so just stop."
        pc "Err, okay then. Sorry."
        show cass neutral
        cass.name "So what do we do?"
        pc "Are you... errr, no. Okay."
        pc "Let's go get the bus."
        hide cass with dissolve
        $ walk(loc_revel)
        show cass slut at right1
        $ walk(loc_busstop_revel)
        cass.name "I'm scared"
        pc "I'm here with you. Will make things a lot easier."
        hide cass with dissolve
        show cass slut at right6
        $ walk(loc_bus_interior)
        pc "Ugh, time to run the gauntlet."
        cass.name "So what do you think we should do?"
        pc "I take you to the highway, introduce you to the girls and find someone to pay for you."
        cass.name "Will that be enough?"
        pc "That's all there is to it. Take money from horny men, make them happy and try not to be killed."
        cass.name "Do I need to ask what they expect from me?"
        pc "They will tell you what they want usually. But you will have to do most things they want."
        if cass.showing:
            pc "You are already pregnant so that's kind of good. Saves money on pills."
        else:
            pc "Probably also want to ask the girls about getting some pills so you don't get knocked up."
        cass.name "..."
        hide cass with dissolve
        $ walk(loc_busstop_truckstop)
        $ walk(loc_truckstop)
        show cass slut at right1 with dissolve
        pc "Ready?"
        cass.name "Give me a moment."
        pc "Take your time."
        "We stand around while [cass.name] tries to gather her nerves. I leave her in peace and just wait for her."
        $ relax(10)
        cass.name "Okay. Let's do this."
        pc "Follow me."
        $ walk(loc_highway)
        pc "Some girls over there. I'll introduce you as my friend. Then we will look for some customers for you."
        show cass at left1
        show rose at right1
        show charity at right2
        with dissolve
        pc "Hey."
        if not c.slutty:
            rose.name "What you want?"
            pc "It's [wname]. Don't treat me like that just because I am not dressed up."
            rose.name "Sorry, didn't recognise you dressed properly."
            rose.name "Who's that you're with?"
        else:
            rose.name "Hey [wname]. Who's that?"
        pc "A friend who needs money. I'm showing her the ropes."
        rose.name "Good luck. It your first time hon?"
        cass.name "Err, yeah. Never done... this before."
        charity.name "She's terrified. Find her an easy one [wname]."
        pc "Trying."
        cass.name "[wname]?"
        pc "Ah yeah. Think of a name for yourself. Helps you separate the real you and what you do here."
        rose.name "Firecunt."
        charity.name "Freckles."
        pc "[cass.wname]."
        rose.name "Milker"
        charity.name "Souleater."
        pc "Souleater? That's not sexy."
        cass.name "[cass.wname] sounds ok."
        pc "Yeah?"
        charity.name "Nice to meet you [cass.wname]."
        cass.name "Hi."
        pc "Look after her when I'm not around would you?"
        rose.name "Sure [wname]."
        pc "Guess I best find someone for her."
        rose.name "Good luck [cass.wname]."
        cass.name "Thanks..."
        hide rose
        hide charity
        show cass at right1
        with dissolve
        cass.name "They seemed... nice..."
        pc "Not everyone here is a junkie bitch."
        cass.name "Guess not."
        pc "Ready to be a whore?"
        cass.name "No choice if I want to find out what happened to [mira.name]."
        cass.name "So what do I do?"
        pc "Stand around looking sexy and available. Make eye contact with any men you see and say \"Hi\" to them if they keep eye contact."
        pc "If they aren't interested then will stop looking. Don't be pushy or you might piss them off."
        cass.name "Right..."
        hide cass
        show cass_pose_whore_1
        with dissolve
        pc "I'll keep an eye on you make sure everything is ok, so don't go too far away."
        cass.name "Okay."
        "I make some distance from [cass.name] and let her try attracting someone. She is very awkward but that doesn't stop her from getting attention."
        "And it isn't long until she attracts someone's interest."
        guy "Hey sweetheart."
        $ male_npc_create_all()
        hide cass_pose_whore_1
        show cass worried slut at left4
        show male_generic at right1
        with dissolve
        cass.name "Err, hi!"
        guy "How about we go somewhere quiet?"
        cass.name "Err, okay... Err..."
        guy "Over there should be fine. Only want something quick."
        cass.name "Err, yes. Okay."
        hide cass
        hide male_generic
        with dissolve
        "I make sure to keep my distance and follow them to make sure nothing bad happens."
        show rose at left1 with dissolve
        rose.name "A ginger with tits like that. She will make a fortune."
        pc "Yeah."
        rose.name "She's going to end up ground into dirt by the shits that come here if she isn't careful."
        pc "Even if she is careful, they will still eat her up."
        show rose at right6 with dissolve
        rose.name "Why did you bring her here? She isn't the whore type."
        pc "Wasn't me. This is all her."
        rose.name "You sure?"
        pc "I tried to talk her out of it. But she has her reasons."
        rose.name "Reasons enough to do this?"
        pc "Reasons enough she would do anything that was needed."
        rose.name "Well, I won't pry. I'll try and look out for her if I see her around."
        pc "Thanks."
        hide rose with dissolve
        "I carry on standing around and keeping an eye out, but don't need to wait long until I can see [cass.name] returning."
        show cass worried slut at right1 with dissolve
        pc "Hey..."
        cass.name "..."
        pc "Want to call it a day and go home?"
        cass.name "Yeah."
        pc "Okay. Let's go."
        show cass at left1
        $ walk(loc_busstop_truckstop)
        "We stand in silence while waiting for the bus. I think about talking to [cass.name] but decide it's probably best to keep quiet."
        $ walk(loc_bus_interior)
        pc "..."
        show cass at right6 with dissolve
        cass.name "That... wasn't very pleasant."
        pc "Something bad happen?"
        cass.name "No. It was fine..."
        cass.name "Just... y'know... I went off with a stranger."
        pc "Yeah..."
        cass.name "Hope I can get used to it."
        pc "Going to carry on?"
        cass.name "Going to take a shower and drink as much beer as I have."
        cass.name "Then probably go back tomorrow..."
        show cass at left1 with dissolve
        hide cass with dissolve
        show cass slut at right1
        $ walk(loc_busstop_residential)
        pc "Stick with the girls around there and it should be ok."
        cass.name "Thanks [name]."
        pc "Don't thank me. I may well have just killed you by taking you there."
        cass.name "..."
        cass.name "Thanks anyway. I won't find [mira.name] by relying on security or anything like that."
        hide cass with dissolve
        pc "See you..."
        pc "*Sigh*"
        pcm "She's going to carry on doing this."
        pcm "..."
        pcm "Suppose I'll just head to the highway area if I am willing to do the same and try to ask about [mira.name]."
    else:


        pcm "Hold on... Is that her in the shop?"
        pcm "*Sigh* What is she getting up to?"
        show cass at right1
        show fun_girl at left4
        $ walk(loc_shop_funwear)
        fun_girl.name "...ing like the smaller one?"
        show cass laugh
        cass.name "Ah [name]! You came?"
        show fun_girl at right3 with dissolve
        fun_girl.name "Perfect, we can have you both try them on."
        show cass neutral
        $ player.face_worried()
        pc "Try on?"
        fun_girl.name "That's right. [cass.name] has been telling me about you girls trying out the highway. I have the perfect outfit for you to try."
        pc "Err, you told her?"
        fun_girl.name "Don't worry darling. Lotta girls from there buy from here. New girls especially."
        fun_girl.name "So c'mon, let's get your asses looking like something worth buying."
        cass.name "I have some clothes for us to try. Although not sure you can call them clothes."
        pc "Right. Okay then..."
        hide fun_girl
        $ walk(loc_changingroom)
        cass.name "I think I got us something suitable. Here, I got this for you."
        $ wardrobe.take(item_top_36, all_notif=True)
        $ wardrobe.take(item_bottom_28, all_notif=True)
        pc "Thanks..."
        pc "Err, this is everything?"
        cass.name "Yeah, should look whore like enough."
        pc "Well, might even be overboard."
        show cass underwear1 with dissolve
        pc "Oh, we just doing it here?"
        cass.name "Come on."
        show cass nude with dissolve
        pc "Okay."
        show cass underwear2 with dissolve
        $ pc_striptease()
        show cass slut with dissolve
        $ quest_mira_missing_kidnap_whore_outfit_set()
        $ quest_mira_missing.work_dress(slow=True)
        pc "No underwear with this getup?"
        cass.name "Err, the girl said it's better without. You will just end up losing them anyway."
        pc "Right. So why do you have underwear on?"
        cass.name "..."
        cass.name "I'm afraid to go without..."
        pc "Err... You want us to go to the highway looking like hookers, pretending to be hookers and it's your knickers that scare you?"
        cass.name "Yes?"
        $ player.face_annoyed()
        pc "You better not be trying to set me up."
        cass.name "Well, I don't really know what I am doing here... I kinda hoped you might."
        if not player.has_perk(perk_whore):
            if player.has_perk(perk_exhibitionist):
                pc "I might like to show off but I am not a whore."
            elif player.has_perk(perk_slut):
                pc "I might like to play around, but I have no idea how this whore stuff goes."
            elif player.has_perk(perk_bimbo):
                pc "Hey, I don't know how this stuff goes. Never done it myself either."
            else:
                pc "How would I know? I don't have a secret highway life or I could have found this stuff out alone."
        else:
            if player.has_perk(perk_gamine):
                pc "I... Okay fair enough. But I am not familiar with this area."
            else:
                pc "Not at the highway, no. People just come up to me and make offers. I have never walked the street."
        pc "Well, I suppose the clothes is a good start. Maybe the girl outside knows what we can do."
        cass.name "Yeah, sounded like she might know something."
        show cass at left1
        show fun_girl at right1
        $ walk(loc_shop_funwear)
        fun_girl.name "Oooh, looking good girls. Don't think you would have issues finding someone like that."
        cass.name "Err, thanks..."
        cass.name "So... Err, we are new to this... What is it we actually do?"
        fun_girl.name "Well, two ways to go about it."
        fun_girl.name "If you still have a bit of cash, can ask for a pink room at the motel. Guys will knock on the door for you."
        fun_girl.name "Motel has fixed prices so people are more willing to go there, but the motel charges a lot for the room."
        fun_girl.name "Or just hang around the truck stop or highway dressed like that. Will have to go to the alleyway to do the job though."
        pc "How dangerous is it?"
        fun_girl.name "Can be a bit. Best to make friends and watch each others backs. Two of you is good, but chat to the other girls and look out for everyone."
        fun_girl.name "Don't be afraid to scream if someone gets violent."
        pc "Ugh, do they get violent a lot?"
        fun_girl.name "Not usually. Most folk are just drunks looking for fun before going home. Are some crazies out there though."
        fun_girl.name "Horny broke junkie, women haters, arseholes looking for an easy target. Some even get off on the rape..."
        fun_girl.name "So be careful out there ok?"
        cass.name "Thanks..."
        fun_girl.name "Hope to see you girls again."
        hide fun_girl
        show cass at right5
        $ walk(loc_revel_backstreet)
        cass.name "So, what do you think?"
        if player.int >= 40 or player.has_perk([perk_whore, perk_gamine]):
            pc "Pink room is no good. We won't make friends in there since we will be alone."
            cass.name "Right, so the streets it is."
        else:
            $ player.face_worried()
            pc "Err..."
            cass.name "I don't know how much the rooms cost but I haven't got that much money."
            pc "Okay, so we wave our arses in the street."
        pc "We getting the bus?"
        cass.name "Dressed like this on the bus..."
        pc "Yup, nightmare. Let's go."
        hide cass with dissolve
        $ walk(loc_revel)
        show cass slut at right1
        $ walk(loc_busstop_revel)
        cass.name "You scared?"
        pc "Me? Nooo. Who would be afraid to hang out near naked where people want to beat you up for fun?"
        hide cass with dissolve
        show cass slut at right6
        $ walk(loc_bus_interior)
        pc "Ugh, time to run the gauntlet."
        cass.name "So what do you think we should do?"
        pc "Err... Not sure... I mean you know where we are headed right?"
        cass.name "Yeah..."
        if player.has_perk([perk_gamine, perk_whore, perk_slut], notif=True):
            pc "To prove to the other girls we are one of them, we aren't getting out of this clean."
            cass.name "What do you mean?"
            pc "I mean we might be pretending to be whores, but the dicks in us won't be pretending."
            cass.name "Oh..."
        elif player.has_perk(perk_bimbo, notif=True):
            pc "We are going to have sex in some smelly alleyway."
            cass.name "You think we might be able to avoid that?"
            pc "Look at us. We look great. People are going to want to do it."
            cass.name "..."
        else:
            pc "Going to be hard to \"pretend\" to be whores."
            cass.name "What do you mean?"
            pc "I mean pretending to be a whore still means heading off with men who want to put their dick in us."
            cass.name "Think we can get away with... not doing that?"
            pc "..."
            pc "No..."
            cass.name "..."
        hide cass with dissolve
        $ walk(loc_busstop_truckstop)
        $ walk(loc_truckstop)
        show cass slut at right1 with dissolve
        pc "Right... So here we are..."
        cass.name "I want to find out what happened to [mira.name]..."
        pc "I know."
        cass.name "If I have to... y'know... then. Then I will..."
        pc "Would make things easier."
        cass.name "What about you?"
        if player.has_perk(perk_sucu, notif=True):
            pc "Don't worry, I am not a stranger to getting dirty."
        elif player.has_perk([perk_gamine, perk_whore], notif=True):
            pc "Well, it's not like I haven't taken money for it before."
        elif player.has_perk(perk_bimbo, notif=True):
            pc "It's what we came here for isn't it?"
        elif player.has_perk(perk_slut, notif=True):
            pc "Not like I haven't got dirty before. I guess it's a small price to pay for [mira.name]. She was my friend too."
        else:
            pc "Well... we are here. I guess we do what we have to..."
        cass.name "Thanks [name]."
        pc "Yeah, say that to my corpse if I get murdered."
        cass.name "Looking at the people round here, they might just consider your corpse a freebie."
        pc "Probably."
        cass.name "So..."
        cass.name "What do you think we should do?"
        cass.name "Do we, like, hang out somewhere specific or something?"
        if player.has_perk([perk_whore, perk_sucu]):
            pc "Look sexy and say \"Hello\" to passing guys."
            pc "I'm guessing they will either ignore us if they aren't interested or ask how much if they are."
            pc "Probably..."
            pc "Not been around here before so just a guess."
        elif kitty.has_met:
            pc "Not too sure, but actually I think I have met that girl over there before. Maybe we can ask her."
            cass.name "Her? Isn't she a whore? Maybe we can ask about [mira.name]?"
            pc "She won't remember me I think. I wasn't dressed like this. But she kinda helped me a little before so hope she is feeling nice again?"
            cass.name "Can try..."
            show cass at left4
            show kitty at right1
            with dissolve
            pc "Err, hey. Kinda new here and trying to figure out what to do."
            kitty.name "And? I'm not your mother. Go away."
            pc "No, but you kinda helped me out before so thought I would ask."
            kitty.name "I don't remember you."
            pc "No... I spent some time in [haven]. You kinda warned me how to keep safe."
            kitty.name "Ah, you stayed there? Where?"
            pc "Where? In some shitty alcove in the shared sleeping area with one eye open."
            kitty.name "Hmmm... Okay then."
            kitty.name "You got a friend here so that's good. Watch each others backs."
            kitty.name "Otherwise you hang around here, make eye contact with people you want to be with and look sexy. Folk who have no interest will ignore you."
            kitty.name "If they keep looking, then you might have a fish on the hook so go talk to them."
            pc "Right. Anything we should be aware of?"
            kitty.name "Don't go with them until you know what they want from you and you set a price."
            kitty.name "Some freaks here want weird shit. Pay to beat you up, want you to shit on 'em or other things. Best avoid 'em. Never worth it."
            kitty.name "You with your friend here so make 'em pay first, give her the money then go off with the guy. Some fucks will kick your ass after and take your money."
            kitty.name "An' don't go nowhere that no one can hear your screamin'. It's how you end up a corpse."
            pc "Err... Corpses common?"
            kitty.name "No. But still something to be careful of."
            pc "Right... Thanks..."
            kitty.name "Stay safe."
            hide kitty
            show cass at right1
            with dissolve
            cass.name "Err, she was helpful?"
            cass.name "She was a bit hostile until you mentioned [haven]. What is that?"
            pc "Ugh, somewhere you don't want to be."
            cass.name "Err... Okay..."
        else:

            pc "Err... No idea really..."
            pc "Stand here looking \"available\" I guess?"
            cass.name "Yeah..."
            cass.name "Right... How do we do that?"
            pc "Say \"hi\" to the guys probably."
            pc "Aren't most guys here for a reason? So we need to just let them know that we are as well."

        pc "So... You ready?"
        cass.name "No."
        cass.name "Not much choice though. Not going to find [mira.name] just waiting at home."
        hide cass
        show cass_pose_whore_1
        with dissolve
        if player.has_perk([perk_whore, perk_sucu]):
            pc "Right then. Suppose all we can do is hope we don't end up with some arsehole."
            cass.name "Yeah..."
        else:
            pc "Shit. Really going through with this?"
            cass.name "The only choice we have."
            pc "Right..."
        "Me and [cass.name] stand around, mostly wondering if we are doing things right. We are both pretty confused about how this whole things works."
        "But it isn't long before we draw some attention."
        guy "Hey sweetheart."
        $ male_npc_create_all()
        hide cass_pose_whore_1
        show cass worried slut at left4
        show male_generic at right1
        with dissolve
        cass.name "Err, hi!"
        guy "How about we go somewhere quiet?"
        cass.name "Err, okay... Err..."
        guy "Over there should be fine. Only want something quick."
        cass.name "Err, yes. Okay."
        hide cass
        hide male_generic
        with dissolve
        "I stand there watching where [cass.name] and her customer went, then go over closer in case something goes wrong."
        $ player.face_worried()
        pcm "Poor [cass.name]. She's going to need a good drink after this."
        "I can somewhat see them in the dark and everything seems ok, so I just stand there watching."
        show rose at right1 with dissolve
        rose.name "Hey, you alone?"
        pc "Err, no. I'm keeping an eye on my friend."
        rose.name "Great, mind keeping a watch for me as well?"
        pc "If I can see you from here, sure."
        rose.name "Thanks!"
        hide rose with dissolve
        "Right, now making sure two people don't end up dead..."
        $ relax(5)
        show male2_generic at right1 with dissolve
        guy "Hey baby. Hows about we have some fun?"
        pc "Sorry mate, I have to keep an eye on some girls."
        guy "Aww c'mon, don't be like that."
        pc "Wait until my friend is back if you want to."
        guy "Ugh, not worth it. I'll find someone else."
        hide male2_generic with dissolve
        pc "..."
        "I hang around for a bit waiting for someone to come back. Now and then a guy comes up and I have to rebuff him."
        $ relax(5)
        show rose at right1 with dissolve
        rose.name "Thanks."
        pc "Done already?"
        rose.name "Yeah, he didn't last long. You still waiting?"
        pc "Yeah."
        rose.name "Not seen you about before."
        pc "No, kinda new."
        rose.name "Okay. Well, they call me \"[rose.wname]\"."
        pc "Err... [name]?"
        rose.name "Yeah, most people round here don't use their proper names. Should think of something for yourself."
        pc "Ah, yeah I should. How about..."
        $ wname = renpy.input("What do you want your whore name to be?", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=12)
        $ wname = wname.strip()
        if wname == "":
            $ wname = "Doxie"
        rose.name "[wname]? Gets the job done. Nice to meet you [wname]. Keep safe."
        pc "You too."
        hide rose with dissolve
        "I carry on standing around, but don't need to wait long until I can see [cass.name] returning."
        show cass worried slut at right1 with dissolve
        pc "Hey..."
        cass.name "..."
        pc "So... I kinda made a new friend..."
        cass.name "Let's go home."
        pc "Err, okay. Let's go."
        show cass at left1
        $ walk(loc_busstop_truckstop)
        "We stand in silence while waiting for the bus. I think about talking to [cass.name] but decide it's probably best to keep quiet."
        $ walk(loc_bus_interior)
        pc "..."
        show cass at right6 with dissolve
        cass.name "That... wasn't very pleasant."
        pc "Something bad happen?"
        cass.name "No. It was fine..."
        cass.name "Just... y'know... I went off with a stranger."
        pc "Yeah..."
        cass.name "Hope I can get used to it."
        pc "Going to carry on?"
        cass.name "Going to take a shower and drink as much beer as I have."
        cass.name "Then probably go back tomorrow..."
        show cass at left1 with dissolve
        hide cass with dissolve
        show cass slut at right1
        $ walk(loc_busstop_residential)
        cass.name "..."
        cass.name "You don't have to if you don't want to."
        pc "What? Go whoring?"
        cass.name "Yeah..."
        pc "How else are we going to find [mira.name]?"
        cass.name "I mean... I didn't even ask if you were okay with it but you helped me anyway."
        cass.name "I'm going to carry on. But if you don't want to deal with this, then I won't be upset."
        cass.name "It... wasn't easy..."
        pc "I bet..."
        cass.name "Right. Well, see you [name]."
        hide cass with dissolve
        pc "See you..."
        pc "*Sigh*"
        pcm "She's going to carry on doing this."
        pcm "..."
        pcm "Suppose I'll just head to the highway area if I am willing to do the same and try to ask about."

    $ log.markdone("mira_missing_07")
    if not quest_whore.active:
        $ log.assign("Street walking")
        $ log.activate("quest_whore_02")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
