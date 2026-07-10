label school_photo_intro_cheat:
    "*NOTE* This cheat bypasses the start requirements, wait times between shoots and does not check your location. This can lead to some inconsistencies."
    "Starting now..."
    if not school_photo_quest.active:
        jump school_photo_intro_start
    else:
        jump expression "school_photo_intro_stage_" + str(school_photo_intro_quest_stage)









label school_photo_intro_start:
    $ school_photo_quest.activate()
    $ loc_school_darkroom.locked = False
    $ felix.active = False
    show felix at right1 with dissolve
    felix.name "Hey, it's [fname] right?"
    $ player.face_conf()
    pc "Err, yeah. And?"
    felix.name "Great, I've been chatting to [svet.name] and she said I should speak to you. I am [felix.name] by the way."
    $ player.face_neutral()
    pc "[svet.name]? Ok, about what?"
    felix.name "It's about a job. Probably better to have a chat in private if you have time."
    $ player.face_conf()
    pc "A job? Ok..."
    if school_class_hours():
        felix.name "Great, well come and find me in my darkroom after classes."
        $ player.face_neutral()
        pc "Ok."
        hide felix with dissolve
        $ log.assign("Promotional material")
        jump random_event_school_end_picker
    menu:
        "Ok, let's have a chat":
            $ school_photo_intro_quest_stage = 1
            felix.name "Great, follow me."
            $ walk(loc_school_hallway_2f)
            if player.check_nowill():
                $ player.face_worried()
                pc "Err, hold on. In there?"
                felix.name "Yeah, it's my darkroom."
                $ player.face_meek()
                pc "Err, I am going to go..."
                show felix frown
                felix.name "Ah..."
                felix.name "No, it's fine, we can talk out here where it's more public."
                $ player.face_worried()
                pc "..."
            else:
                $ walk(loc_school_darkroom)
                felix.name "Ok, have a seat if you can find one."
            jump school_photo_intro_first_talk
        "Bit busy now, maybe later.":

            felix.name "That's fine, when you have time come to the dark room after classes have ended and we can have a chat."
            $ player.face_neutral()
            pc "Right."
            hide felix with dissolve
            $ log.assign("Promotional material")
            jump travel

label school_photo_intro_first_talk:
    if log.interactive("photo_intro_01"):
        $ walk(loc_school_darkroom)
        pc "Helloooo..."
        show felix at right1 with dissolve
        felix.name "Ah! Yes I'm here."
        felix.name "Glad to see you came to see me."
        pc "Well, you were talking something about a job so I thought I would at least hear you out."
    else:
        pc "So? A job?"
    show felix smile
    felix.name "Yes. Ok, so..."
    felix.name "You know what this place is for right? Err, not the room but the whole place."
    $ player.face_conf()
    pc "Well, acclimatise young people to the shitty new world, or so I was told."
    felix.name "Pretty much. But it's also to provide a safe place for everyone as well. Things are pretty shit out there and it's a lot safer to be hanging out here than anywhere out there."
    $ player.face_neutral()
    pc "Ok..."
    felix.name "So, the head of this place is trying to attract more of the Urchins and Gamines out there to come hang out here. If not attending classes then at least here after classes to keep safe."
    felix.name "But attracting people is not easy. So I have been tasked with essentially making some propaganda material to attract them."
    pc "Ok... I am lost. I have no idea why anyone cares or where I come in."
    felix.name "Why anyone cares? I haven't a clue either. Frankly I don't care myself. What I do care about is I am being paid to promote this stupid idea."
    felix.name "Where you come in is I need a model for any posters or pamphlets I make."
    felix.name "I am thinking pretty girl doing happy looking things might attract some people. You doing sporty stuff or dancing looks like a pretty good place to start."
    felix.name "An all girls dance group doing whatever girly things you do while hanging out might attract other girls looking to hang out. Or guys who want to flirt with a bunch of girls."
    felix.name "I don't care much. The more people I manage to attract with this, the greater chances of me being paid to do more. Me doing more means I need you more. We both get paid."
    felix.name "So? Interested?"
    pc "So photos? You print them as some kind of advertisement for this place. We both get paid?"
    felix.name "Basically."
    pc "What kind of photos?"
    felix.name "First thing I have in mind is something sports related looking like you are having fun. I will put some captions or a small article about how much you enjoy being here to go along with it."
    $ player.face_worried()
    pc "You want to interview me as well?"
    felix.name "Nooo. Waste of time. I will just make up some motivational sounding rubbish. Whatever is fitting."
    $ player.face_neutral()
    pc "Right, so just the photos?"
    felix.name "Yeah, but think it over. I still have other stuff to do so no hurry. Come see me after classes if you are up for it and we will get the ball rolling."
    pc "Ok, sure. How much does it pay?"
    felix.name "Depends on the shoot. £40 or so to start with but hoping more shoots will come up."
    pc "Ok. Well, I'll think it over."
    felix.name "Great. I am normally here when the place is quiet. So evenings or weekends."
    hide felix with dissolve
    $ walk(loc_school_hallway_2f)
    if loc_from == loc_school_darkroom:
        $ player.face_shock()
        $ player.eye = 2
        pcm "Ah! So bright!"
    $ player.face_neutral()
    pcm "Hmmm..."
    if player.sold > 5:
        pcm "Modelling for photos? Guess it's better than fucking guys for money."
    elif player.has_perk(perk_exhibitionist):
        pcm "Modelling for photos? Wonder if it will go nude eventually?"
        pcm "..."
        $ player.face_shy()
        pcm "Of corse it will."
    elif player.check_sex_agree(3):
        pcm "Modelling for photos? Guess there are worse ways to earn a bit of money..."
    else:
        pcm "Modelling for photos in my dance outfit? It's bad enough revealing myself in front of the perverts, but photos?"
    pcm "Ah well. Suppose if I am interested I should go and have another talk with him."
    if not quest_photo_intro.active:
        $ log.assign("Promotional material")
    $ log.markdone("photo_intro_01")
    jump travel

label school_photo_intro_first_shoot_ask:
    $ walk(loc_school_darkroom, trans=False)
    show felix at right1 with dissolve
    pc "Hey."
    felix.name "Hey [name]. So ready to try out some poses for the photos?"
    pc "What was it you wanted again?"
    felix.name "Just some photos of you having fun while doing sporty stuff so I can use the photos in promotional material."
    pc "Hmmm..."
    if player.check_sex_agree(2, exhibitionist=True):
        menu:
            "Sure, let's give it a try":
                jump school_photo_intro_first_shoot
            "Not right now":

                jump school_photo_intro_reject_offer
    else:
        pc "No, I don't think I am ready to have my photos taken right now."
        jump school_photo_intro_reject_offer

label school_photo_intro_first_shoot:
    felix.name "Great, ok. You go and change into your sports outfit while I grab my camera. I will meet you in the gym."
    pc "Ok."
    hide felix
    $ walk(loc_school_locker_girls)
    pause 0.5
    $ photo_clothes_vball_modest()
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ pc_dress_quick("work")
    $ player.set_hair("pony")
    pc "There we go..."
    $ walk(loc_school_gym, trans=False)
    show felix at right1 with dissolve
    pc "How's this?"
    felix.name "Perfect. It's what you all wear right?"
    pc "Most people do yeah. Got it for free before I started coming here and can usually find spares laying around."
    felix.name "Great. Should do the job then."
    felix.name "Ok, take this ball as well. Just some simple poses should do the job for now while we work things out properly."
    show ps_pose_vball
    hide felix
    with dissolve
    $ add_to_list(school_photo_quest.list,"vball")
    felix.name "Big smile."
    "I stand there smiling a huge fake smile while [felix.name] takes photos of me from all different angles. Occasionally he asks me to move my head or shift my body a bit."
    "But all in all, it is a very easy going process and it is starting to feel like easy money."
    $ working(60)
    felix.name "Right, I think I should have enough for now."
    pc "That's it?"
    felix.name "For you, yes. I have to go back and develop the photos and see what ones turned out best."
    pc "Ok, well that was easy."
    hide ps_pose_vball
    show felix at right1
    with dissolve
    felix.name "Glad you think so. Means I should be able to tempt you back another time."
    pc "If you are paying, sure."
    felix.name "Mmm, anyway, here you go. Come back in a few days when I have these all developed and printed."
    pc "Thanks."
    hide felix with dissolve
    $ player.add_money(25)
    $ pc_dress_event("daily", loc_school_locker_girls)
    $ log.markdone("photo_intro_02")
    $ quest_photo_intro.workedtoday = t.day
    jump travel

label school_photo_intro_second_shoot:
    $ walk(loc_school_darkroom)
    pc "Are you here?"
    show felix at right1 with dissolve
    felix.name "Ah hey [name]. Glad to see you back here."
    pc "Sure. How did the photos turn out?"
    felix.name "Good, I already printed out the pamphlets and put them out in the usual places."
    felix.name "You interested in doing more photos? How about this time we do something in your dance outfit?"
    if not player.check_sex_agree(3, exhibitionist=True):
        pc "Bit revealing isn't it?"
        felix.name "Is that a problem? You dance in front of people wearing it."
        pc "Well, yeah..."
        felix.name "Don't worry, you can cover up if it's an issue."
    pc "This one also paid?"
    felix.name "Of course."

    menu:
        "Sure, let's give it a try":
            $ quest_photo_intro.workedtoday = t.day
        "Not right now":

            jump school_photo_intro_reject_offer

    felix.name "Great, ok. You go and change into your dance outfit while I grab my camera. I will meet you in the gym."
    pc "Ok."
    hide felix
    $ walk(loc_school_locker_girls)
    pause 0.5
    $ photo_clothes_dance_modest()
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ pc_dress_quick("work")
    $ player.set_hair()
    pause 0.5
    $ walk(loc_school_gym, trans=False)
    show felix at right1 with dissolve
    pc "Here we go."
    felix.name "Great. Well, same as before. Let's see your best winning smile."
    pc "How should I stand?"
    felix.name "Make it look like you are dancing. But don't actually move since these old cameras don't do too well with motion."
    pc "Ok..."
    show ps_dance
    hide felix
    with dissolve
    $ add_to_list(school_photo_quest.list, ["dance", "dance_modest"])

    pc "Something like this?"
    felix.name "Err, perfect."
    felix.name "Bit more revealing than I realised but should be able to work with it no problem."
    pc "Well, you did ask for the dance outfit."
    felix.name "I did. Just didn't realise how short the skirt was."
    if not c.pants:
        felix.name "And that there was no underwear with the uniform."
    pc "Ah. Yeah when dancing there might as well not even be a skirt. Does nothing to hide anything."
    felix.name "Hmmm. Big smile please."
    show ps_dance vhappy with dissolve
    felix.name "Great."
    "Like before, he moves around in front of me getting photos from all different angles, asking me to shift or adjust my pose depending on the angle."
    felix.name "Brilliant. Ok..."
    pc "That it?"
    felix.name "I think so. These should be more than though."
    pc "Ok."
    hide ps_dance
    $ working(60)
    show felix at right1
    with dissolve
    pc "Back to developing?"
    felix.name "That's right. Come see me in a few days and I should have it all done."
    pc "Mmmm."
    show felix frown
    felix.name "..."
    pc "..."
    felix.name "Err, yes?"
    pc "This tiny skirt doesn't have pockets, but my imaginary ones feel just as light as when I arrived."
    felix.name "Huh?"
    pc "Pay me."
    felix.name "Ahhh."
    show felix smile
    felix.name "Yes, here you go."
    $ player.add_money(25)
    pc "Thanks, see you in a few days."
    felix.name "Mmm."
    hide felix with dissolve
    $ pc_dress_event("daily", loc_school_locker_girls)
    $ log.markdone("photo_intro_04")
    $ quest_photo_intro.workedtoday = t.day
    jump travel

label school_photo_intro_post_second:
    $ walk(loc_school_darkroom)
    $ school_photo_intro_quest_stage = 4
    $ school_photo_date = t.day
    show felix frown at right1
    felix.name "Hey [name]. Come in. Let's have a chat."
    pc "Ok. Everything ok?"
    felix.name "Yeah, the head has given the go ahead to keep working on promotional material so I am guessing there has been more people showing up here than usual."
    pc "Ok, that's good. More money for us then."
    felix.name "Well yes..."
    pc "Hmm. Problem?"
    felix.name "Kind of. I am confused about it. This stuff is costing me more than it usually does and I am trying to work out why."
    pc "What do you mean?"
    felix.name "Well, I've done stuff like this before. When I put the pamphlets out in places like the hospital, market or wherever, I come back weeks later and not a single one has been taken."
    felix.name "These ones though... I have to keep replacing them, which means more printing..."
    pc "So that's bad?"
    felix.name "Well, no. I need to find out why these ones are being taken and not the others. If I can find out why then I might be able to take advantage of it and make even more money."
    if player.has_perk([perk_slut, perk_whore]):
        pc "The degenerates are probably using it as wank material."
        $ add_to_list(quest_photo_intro.conversation_topics, "intro_reason_slut")
    elif player.check_sex_agree(3, exhibitionist=True):
        pc "Pamphlets with a half dressed dancing girl on them. I can't think of a reason why people would make off with them."
        $ add_to_list(quest_photo_intro.conversation_topics, "intro_reason_sex")
    else:
        pc "Can't be my winning smile."
        felix.name "No..."
        $ add_to_list(quest_photo_intro.conversation_topics, "intro_reason_smile")
    felix.name "..."
    felix.name "Err..."
    felix.name "Let me look into this. Come back in a couple of days."
    pc "Err, okay then."
    hide felix
    $ walk(loc_school_hallway_2f)
    pcm "Is he stupid or just naïve?"
    pcm "Oh well."
    $ log.markdone("photo_intro_06")
    $ quest_photo_intro.workedtoday = t.day
    jump travel

label school_photo_intro_post_investigate:
    $ walk(loc_school_darkroom)
    $ school_photo_intro_quest_stage = 5
    $ school_photo_date = t.day
    show felix frown at right1
    felix.name "Ah, [name]. Come in."
    pc "Sure. How was your investigation?"
    felix.name "*Sigh*"
    felix.name "Am I an idiot?"
    pc "Probably."
    if "intro_reason_smile" in quest_photo_intro.conversation_topics:
        felix.name "*Hrmf* Well as you probably guessed, it wasn't your winning smile."
        pc "No? Really? I am shocked!"
    elif "intro_reason_sex" in quest_photo_intro.conversation_topics:
        felix.name "*Hrmf* Well as you hinted at, there was something special in these pamphlets that I didn't have in any of the others."
        pc "Oh? Well don't keep me in suspense. What was it?"
        felix.name "Very funny..."
    else:
        felix.name "*Hrmf*"
        pc "..."
        pc "Well?"
        felix.name "Well what? You were right."

    if player.has_perk([perk_exhibitionist, perk_bimbo, perk_whore, perk_slut, perk_broken]):
        pc "So what now? The photos are already out there for perverts to have fun with."
    else:
        pc "So what now? Not sure how comfortable I feel about my pictures floating around for those perverts."
    felix.name "Hmm, not sure. They are not really doing the job they were intended to so it's kind of pointless to pump more money into printing the pamphlets if they are not reaching the target audience."
    pc "I thought you said the head was happy to let you keep going ahead with making more?"
    felix.name "He is. But if perverts keep taking the pamphlets, then the kids aren't getting their hands on them and not coming here."
    felix.name "So either I have to print more out of my own pocket making it not worth it, or don't print more and not attract anyone new here. Either way it's not good."
    pc "Ok, so then we are both out of a job. Nothing new there..."
    felix.name "I will think of something. I don't want to call it quits so soon. I have invested too much in renovating all this equipment to just throw in the towel because of a bunch of perverts."
    pc "Right. Well good luck with that. Going against people like that is like going against the tide. You will just waste your energy and get swept away in the end anyway."
    felix.name "..."
    felix.name "*Huff*"
    felix.name "You're probably right..."
    hide felix with dissolve
    pc "Err..."
    pc "Ok..."
    pc "Umm..."
    pc "..."
    $ walk(loc_school_hallway_2f)
    pcm "Well, so much for earning some money out of that..."
    $ log.markdone("photo_intro_08")
    $ quest_photo_intro.workedtoday = t.day
    jump travel

label school_photo_intro_return:
    $ player.face_shock()
    show felix at right5 with dissolve
    felix.name "Hey [name]. Got a moment?"
    pc "Ah, sneak up on me like that..."
    $ player.face_neutral()
    pc "Sure I have a moment."
    felix.name "I think I have solved our issue. Come to the dark room when you have time so we can have a chat."
    pc "Ok, sure."
    hide felix with dissolve
    $ log.assign("Photo model")
    jump travel

label school_photo_intro_quest_give:
    $ walk(loc_school_darkroom)
    show felix at right1
    felix.name "Hey [name]. Come in."
    pc "Hi. So, you mentioned you solved \"our\" issue?"
    pcm "Wasn't aware we had an issue..."
    felix.name "Well, solved is a stretch. I found out our problem and how to capitalise on it."
    pc "Ok, so...?"
    felix.name "Well, as you know the problem is people who are not our target audience keep taking our pamphlets for their own \"use\"."
    felix.name "This means we struggle to get the people we want to come here seeing the material. So either we print more or accept defeat."
    pc "Ok, that's what you mentioned before. What changed?"
    felix.name "Here."
    show him_magazine at truecenter with dissolve
    $ player.face_worried()
    pc "Err...Do I need gloves to touch that?"
    $ player.face_shock()
    show felix frown
    felix.name "Not if you don't try to open the pages."
    $ player.face_worried()
    pc "Ok, so you have a dirty mag. I am failing to see..."
    if player.has_perk([perk_exhibitionist, perk_whore], notif=True):
        pc "Ah! I think I see where this is going."
        felix.name "Let me give you my sales pitch before you storm out of here."
        hide him_magazine with dissolve
        $ player.face_neutral()
        pcm "Who's storming anywhere? Sounds a good idea to me."
        pc "Okay then."
    else:
        pc "Ugh..."
        $ player.face_angry()
        pc "Me? Really?"
        show felix smile
        felix.name "Let me give you my sales pitch before you storm out of here."
        hide him_magazine with dissolve
        $ player.face_neutral()
        pc "*Sigh*"
    felix.name "So, these types of magazines were called \"lads mags\". They had general articles on topics that would interest mostly men along with interviews with half dressed women."
    pc "And you want to do the same?"
    felix.name "Similar. I want to create on the surface what is an innocent magazine with articles about [town] or other topics that affect people today."
    felix.name "But..."
    felix.name "I want to sneak in the odd excuse to have photos of... Well, sexy girls. Like the dance set we did before. To people like the head who will be funding this, it's all normal and innocent."
    felix.name "But you and I will know the real selling point is people buying the magazines to look at the girls."
    if player.has_perk([perk_exhibitionist, perk_whore, perk_slut]):
        pc "So you want to sneak in wank material in an otherwise innocent magazine?"
    else:
        pc "So you want to sneak in provocative material for the perverts in an otherwise normal magazine?"
    felix.name "Yes..."
    pc "Selling the magazine?"
    felix.name "Of course!"
    pc "And I am guessing you are speaking to me because you want my photos?"
    felix.name "Yes."
    pc "\"Innocent\" photos? No nudity or anything like that?"
    felix.name "No nudity. The photos must have proper context otherwise the head might shut us down. The dance one for example is perfect. It is your normal dance outfit so why wouldn't we show it in an article to do with dance?"
    felix.name "I tell you what. Go and think it over and if you are interested then come back and see me. If you don't return I will just assume you have refused. No pressure."
    pc "Right..."
    pc "..."
    hide felix
    $ walk(loc_school_hallway_2f)
    if player.has_perk(perk_exhibitionist, notif=True):
        pcm "Sounds like a good idea to me. And a good excuse to show off to the perverts."
        $ player.face_shy()
        pcm "Kind of exciting."
        if player.has_perk(perk_slut, notif=True):
            pcm "Dirty perverts using my photos to wank over..."
            pcm "Mmmm."
            $ player.add_desire_random(20)
            pcm "Makes me horny just thinking about it."
    else:
        pcm "Hmmm, I guess it's a good idea for making money. But with me in the photos...?"
        pcm "I mean they are supposed to be innocent photos. But at the same time not..."
        pcm "Hmmm..."
    $ log.markdone("photo_01")
    $ felix.active = True
    jump travel

label school_photo_intro_quest_camera_shop:
    $ walk(loc_school_darkroom)
    show felix at right1
    $ felix.inv.take(item_polaroid_camera)
    $ felix.inv.take(item_polaroid_blank, 20)
    felix.name "[name]! Good you are here."
    pc "Oh?"
    felix.name "I've been thinking, there isn't always the need to take photos with me."
    pc "Huh?"
    felix.name "I mean I have another camera I fixed up you could buy. Take photos when you are doing your thing and if they are good I can buy them off you."
    if player.has_perk(perk_exhibitionist):
        pc "Ah, you want me to go home and take some mirror nudes?"
        felix.name "What? No!"
        felix.name "Well, I wouldn't complain. They would sell. But no."
    else:
        pc "Want me to take pictures myself while I am out there?"
    felix.name "Pictures of you, friends, the city. Whatever. If it's good I will buy."
    pc "But you are trying to make a dirty mag so I guess more pictures of me?"
    felix.name "Yes. Give it a try and I'll see if there are any worth buying."
    pc "Wait, hold on. You said I can buy the camera? Cheapo! Give it to me."
    felix.name "Err, this stuff is expensive. I'm here trying to make money not give it all away."
    if player.has_perk(perk_exhibitionist):
        pc "I'll take some nudes if you give it to me for free."
        felix.name "Really?"
        pc "Yup ♥"
        felix.name "..."
        felix.name "I'll hold you to that."
        $ felix.inv.take(item_polaroid_camera)
        $ inv.take(item_polaroid_camera)
        $ inv.take(item_polaroid_blank, 5)
        pc "Thanks."
    else:
        pc "Right..."
        call screen inventory_itemshop_screen(felix.inv)
    hide felix with dissolve
    $ log.activate("photo_03", notify=True)
    jump travel

label school_photo_intro_reject_offer:
    felix.name "Ok, well you know where I am if you change your mind."
    pc "Sure."
    hide felix with dissolve
    $ walk(loc_school_hallway_2f)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
