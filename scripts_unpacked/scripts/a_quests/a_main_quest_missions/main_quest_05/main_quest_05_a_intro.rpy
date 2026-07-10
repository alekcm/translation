label main_quest_05_cheatjump:
    "This is the cheat to jump directly to the start of the Haven mission."
    "If you pressed the button by mistake, then roll back now as this cannot be undone later."
    "NOTE**** There may be an error caused by the questlog because you bypassed parts of the game. Press IGNORE and it will be fine."
    if player.fitness < 40:
        "You do not meet the minimum fitness requirement so it will be boosted to 30"
        $ player._fitness = 42
        $ player.add_fitness()
    if not main_quest_05.stage == 1:

        $ main_quest_05.activate()
    "Have fun."
    jump main_quest_05_main_start

label main_quest_05_intro:
    $ walk(loc_hospital_office, trans=False)
    if not main_quest_05.stage == 1:

        $ main_quest_05.activate()
    show tucker at right1 with dissolve
    $ log.markdone("mq_04_f")
    tucker.name "Come in [fname]."
    tucker.name "As I am sure you have guessed. We are ready to move forward with tracking down [ant.fullname]."
    $ player.face_happy()
    pc "I am fine thank you. How are you?"
    $ player.face_neutral()
    tucker.name "I have had a couple of people keeping an eye out on the building for a few days now and we think we have come up with a somewhat viable plan."
    pc "Thanks for asking, the kids are doing well. Wife is going on at me for spending too much time at work though."
    $ player.eye = 2
    pc "Starting to suspect I am having an affair with the secretary."
    $ player.eye = 1
    pc "But that's fine, as long as she suspects my secretary she won't realise I am actually having an affair with her sister."
    tucker.name "..."
    $ player.face_worried()
    pc "She almost caught us last week when she came home early. I had to confess I was secretly trying on her knickers and not that they were left behind by her sister."
    $ player.face_shame()
    pc "She thinks it's kinky. Now she makes me wear her pants every day. I almost broke down and confessed to the affair when she brought out a bright pink thong for me to wear."
    tucker.name "Hello [fname]. How are you?"
    $ player.face_normal()
    $ player.face_happy()
    pc "I am great [tucker.name]. Yourself?"
    $ player.face_normal()
    tucker.name "I am wonderful!"
    tucker.name "Now, we have arranged most of the details for you. We have a new legend set up for you but we need some clothes and equipment to go with it."
    tucker.name "We could do it ourselves, but I think this is a good opportunity for you to get in touch with some of the other people that will be helping us out in future."
    pc "Oh?"
    tucker.name "At the market there is a stall that makes and repairs clothes. Go there and pick up the outfit you will be wearing for entering Haven."
    pc "A cheap whore's outfit I assume?"
    tucker.name "No, that will draw too much attention. Just something a typical Gamine might wear."
    tucker.name "I also need you to collect a tracking device from the guys at the junk yard near the checkpoint and head over to the mechanic shop nearby for some other equipment."
    tucker.name "Just bring it all back here and we should be ready to go."
    pc "Right, okay then."
    hide tucker
    $ walk(loc_hospital_lobby)
    $ log.assign("Preparing for a Curse")
    $ log.activate("mq_05_prep_b")
    $ log.activate("mq_05_prep_c")
    pcm "Right, okay then. To the market for some clothes, the junk yard for a tracker and to the mechanics for... Something."
    pcm "Nice and easy."
    jump travel

label main_quest_05_mechanic:
    if not t.hour in workhours:
        pcm "It's late, I should look around when it's going to be open so I make sure it's the right place."
        jump travel
    pcm "Hmm, one of these buildings should be it."
    pcm "Err, this looks like the right place."
    $ walk(loc_mechanic)
    pcm "..."
    pc "Helloooo..."
    pcm "..."
    show ali worried at right1 with dissolve
    ali.name "Yes?"
    pc "I was sent by [tucker.name] to pick up a package."
    if c.slutty:
        show ali angry
        ali.name "*Tsk*"
        ali.name "Speak to [dez.nname] in back."
        hide ali with dissolve
        pcm "Right..."
        show dez at right1
        $ walk(loc_mechanic_office)
        pc "Hi, I am here to pick up a package for [tucker.name]."
        dez.name "Was expectin' his goons to show up. Not expecting the like of you."
        pc "No need for goons to get a package."
        dez.name "Good. Don't need the oafs from over there come stompin' round here. Better you come next time."
        pc "Not sure there will be a next time. But sure."
        dez.name "Well, package is there all ready for ya."
        pc "Thanks."
        pc "Who pissed in the girls pants over there?"
    else:

        show ali neutral
        ali.name "Right. It's in back with [dez.nname]."
        pc "Thanks."
        ali.name "Don't get close to him."
        pc "Huh? He your boyfriend?"
        ali.name "Ugh. He's a creep. Make sure you can see his hands."
        pc "Oh?"
        pc "Thanks."
        hide ali
        $ walk(loc_mechanic_office)
        pc "Hi, picking up a package. It should be ready for me."
        show dez at right1 with dissolve
        dez.nname "You? Was expectin' one of [tucker.name]'s goons to show up. Not expecting the like of you."
        pc "No need for goons to get a package."
        dez.nname "Good. Don't need the oafs from over there come stompin' round here. Better you come next time."
        pc "Not sure there will be a next time."
        dez.nname "Well, package is there all ready for ya."
        pc "Thanks."
        pc "..."
        pc "So what's going on with the girl out there?"

    dez.name "[ali.nname]? Startin' to realise the world is shit. Can't come to terms with it."
    if player.has_perk([perk_gamine, perk_whore, perk_slut], notif=True) or player.check_int(3):
        pc "..."
        pc "Or just realising the people in it are shit?"
        dez.nname "What you sayin'?"
        pc "She's pretty and your her boss. Taking advantage of her?"
        dez.nname "Not like that. I coulda got better people in for the job. She offered herself up if I give the job."
        dez.nname "I give the job and get no offer. She aint bad mechanic so I can keep her. But better people to have if she's not giving me fun."
        dez.nname "I just let her know this and now she is pissed."
    else:
        pc "Yeah, her and everyone else."
        dez.nname "Mmm."
    pc "Right..."
    pc "Whatever. I'll take the package and leave you to it."
    $ inv.take(item_haven_package)
    dez.nname "Come back if you need something."
    pc "Sure."
    hide dez
    $ walk(loc_mechanic)
    pcm "Those two are just trouble brewing. Wonder if I should try and do something about it..."
    $ walk(loc_industrial)
    $ log.markdone("mq_05_prep_a")
    if log.interactive("mq_05_prep_c") and log.interactive("mq_05_prep_b"):
        pcm "Whatever. The junk yard and the market are my next stops."
    elif log.interactive("mq_05_prep_c"):
        pcm "Whatever. Off to the junk yard to get a tracker."
    elif log.interactive("mq_05_prep_b"):
        pcm "Whatever. Off to the market to get my clothes."
    $ loc_mechanic.locked = False
    jump travel

label main_quest_05_junkyard:
    if not t.hour in workhours:
        if ashon.has_met:
            pcm "[ashon.name] won't be here til tomorrow. I'll have to come back."
        else:
            pcm "It's a bit late so no one here. I'll have to come back tomorrow."
        jump travel
    show ashon at right1 with dissolve
    if ashon.inv.value_junk() > 20:
        pc "Hey [ashon.nname]. I am to pick some stuff up for you."
        ashon.name "Oh? They sending you? Didn't know you worked for \"them\"."
        pc "They pay and I need money."
        ashon.name "Ain't that the truth."
        ashon.name "Well, one [jaylee.name] special."
        pc "From [jaylee.name]?"
        ashon.name "Yup."
        pc "Right..."
    else:
        pc "Hi. I'm here to collect a package."
        ashon.name "You are? What you picking up?"
        pc "Err, you should have already got it ready. It's what I was told anyway."
        ashon.name "Yeah, got a lot of stuff here. What is it?"
        pc "A tracker?"
        ashon.name "..."
        pc "I think..."
        ashon.name "Just checking. Lot of thieves tryin' their luck and you don't look like the typical goon he sends."
        pc "Ah. Well, yeah. Kinda the point."
        ashon.name "Here you go."
    $ inv.take(item_haven_package)
    pc "Thanks."
    hide ashon with dissolve
    $ log.markdone("mq_05_prep_c")
    if log.interactive("mq_05_prep_a") and log.interactive("mq_05_prep_b"):
        pcm "Ok, now to the mechanics and the market."
    elif log.interactive("mq_05_prep_a"):
        pcm "Ok, now to the mechanics to pick up... I'm not sure what actually. [tucker.name] didn't say."
    elif log.interactive("mq_05_prep_b"):
        pcm "Ok, now to the market to pick up my clothes."
    jump travel

label main_quest_05_market:
    if not t.hour in workhours:
        pcm "Market is closed so need to come back tomorrow to pick up the package."
        jump travel
    if not loc(loc_market_stall_needle):
        pcm "Let's see..."
        pcm "..."
        pcm "There we go..."
        $ walk(loc_market_stall_needle)
    show frida at right1 with dissolve
    if frida.has_met:
        pc "Oh?"
        frida.name "Hey [name]."
        pc "Hey."
        frida.name "Just come to say hello?"
        pc "Ah. Actually here to pick up a package. Just didn't know it would be from you."
        frida.name "No one else around here fixing up clothes. It going to be you wearing this stuff?"
        pc "Yeah..."
        pc "Please tell me it's not that bad."
        frida.name "What do you mean?"
        pc "Ah nothing. No matter."
        if felix.has_met:
            frida.name "[felix.name] would love some shots of you wearing it though."
            pc "Ugh, so it is bad?"
            frida.name "Ha, I'm just teasing."
        frida.name "[saskia.nname]! Our dear [name] wants her stuff."
        show saskia at right2 with dissolve
        saskia.name "Oh. For you?"
        saskia.name "Well, she can pull it off."
        pc "C'mon."
        frida.name "Anyone behind her is going to have a fun time."
        saskia.name "[tucker.name] is going to love it."
        frida.name "Didn't think he was into this sort of thing. But you never know with people like him."
        saskia.name "Likes the gamine look?"
        frida.name "Maybe he likes them vulnerable?"
        saskia.name "\"Oh no [tucker.name]! Whatever is a poor girl like me to do. I sure do hope some grumpy git doesn't get all handsy.\""
        frida.name "Hahaha!"
        pc "Ugh..."
        saskia.name "Come back wearing it and show it to us."
        pc "Yeah yeah, damn clowns."
        $ inv.take(item_haven_package)
        frida.name "Have fun."
        hide frida
        hide saskia
        with dissolve
    else:
        pc "Hi. I'm here to pick up a package for..."
        frida.name "Oh wow! [saskia.nname]! [tucker.name]'s girl showed up herself!"
        show saskia at right2 with dissolve
        saskia.name "Really? Didn't know he went for girls as young as you."
        $ player.face_worried()
        if c.slutty:
            frida.name "Or as bold."
        elif player.breasts == 3:
            frida.name "Likes them big it looks like."
        $ player.face_worried()
        pc "Err..."
        pc "Not quite sure he's like that."
        frida.name "Dressing his girl up in this stuff. I think he is."
        if c.slutty:
            frida.name "Not sure why though. What you have now is way more revealing."
        pc "It's not... Ugh. Never mind. Do you have it?"
        $ player.face_neutral()
        saskia.name "Sure do. Have fun with it."
        $ inv.take(item_haven_package)
        frida.name "Come back and tell us how it went. Might give you something else to entertain that grump."
        saskia.name "Maybe he will actually crack a smile."
        frida.name "Yeah right. Him? He was born with a scowl."
        pcm "No argument there."
        pc "Ok, well..."
        saskia.name "So the gamine look?"
        frida.name "Maybe he likes them vulnerable?"
        saskia.name "\"Oh no [tucker.name]! Whatever is a poor girl like me to do. I sure do hope some grumpy git doesn't get all handsy.\""
        frida.name "Hahaha!"
        hide frida
        hide saskia
        with dissolve
        pcm "Okay then..."
        pcm "Leave those weirdos alone..."
    $ log.markdone("mq_05_prep_b")
    if log.interactive("mq_05_prep_c") and log.interactive("mq_05_prep_a"):
        pcm "The junk yard and the mechanics are my next stops. Close together so can do them one after the other."
    elif log.interactive("mq_05_prep_c"):
        pcm "Picking up the tracker from the junk yard is my last stop."
    elif log.interactive("mq_05_prep_a"):
        pcm "Picking up stuff from the mechanics is my last stop."
    jump travel

label main_quest_05_main_start:
    show tucker at right1
    $ walk(loc_hospital_office)
    $ log.markdone("mq_05_prep_d")
    tucker.name "Good to see you miss [sname]. Everything to..."
    pc "So I hear you like your girls young and vulnerable."
    tucker.name "*Sigh*"
    pc "Maybe I should come here with a responsible adult. Supervised meetings and all that."
    pc "Does The Institute have an HR department? I think I will need to speak to someone."
    tucker.name "So you have picked up your outfit?"
    pc "Making me play dress up is harassment. I need to lodge a complaint. The girls at the market will be on my side."
    tucker.name "So I am to assume that is a \"yes\"?"
    pc "They had some words about your proclivities."
    tucker.name "Then we have everything we need to proceed."
    pc "Here you go."
    $ inv.drop(item_haven_package, 10)
    $ log.assign("Haven")
    if player.pregnancy >= 2 or player.preg_knows:
        tucker.name "Your pregnancy poses a problem though. We will need to wait until it has run it's course before proceeding with the mission."
        tucker.name "Come and see me once you have given birth and slimmed down a bit, then we can move forward."
        pc "Ok, I'll come back later."
        tucker.name "I look forward to it"
        hide tucker with dissolve
        $ walk(loc_hospital_lobby)
        jump travel
    elif player.fitness < 30 or player.pregnancy:
        tucker.name "But it looks like you haven't been following [nik.name]'s guidance about exercising. The people where we are sending you are seriously underfed and in your current state you will stand out far too much."
        tucker.name "So come and see me once you have shed some weight and we can start things off."
        pc "Ok, I'll come back later."
        tucker.name "I look forward to it"
        hide tucker with dissolve
        $ walk(loc_hospital_lobby)
        jump travel

    tucker.name "All we need now is your go ahead and we can start. Keep in mind you might be away for a week or more."
    tucker.name "You should probably think it over and return when you are fully ready to take on this mission."
    menu:
        "I am ready now. Let's get started.":
            $ log.markdone("mq_05_a")
            jump main_quest_05_preperation
        "I have some things I would like to sort out first.":

            tucker.name "Ok, I'll be waiting."
            hide tucker with dissolve
            $ walk(loc_hospital_lobby)
            jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
