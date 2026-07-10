label school_class_preg:
    if not loc(loc_school_classroom):
        $ walk(loc_school_classroom)

    $ dialouge = renpy.random.choice([
    "I head into the classroom and take a seat.",
    "I go to the classroom and take an empty seat.",
    "I head inside and find somewhere to sit.",
    ])
    "[dialouge]"
    pause 0.5

    $ rand_choice = WeightedChoice([
    ("school_class_preg_cassmira_1", If (all([cass.has_met, mira.has_met]) and all([cass.isactive, mira.isactive]) and all([cass.showing, mira.showing]),100,0)), 
    ("school_class_preg_cassmira_2", If (all([cass.has_met, mira.has_met]) and all([cass.isactive, mira.isactive]) and all([cass.showing, mira.showing]),100,0)), 
    ("school_class_preg_cassmira_3", If (all([cass.has_met, mira.has_met]) and all([cass.isactive, mira.isactive]) and all([cass.showing, mira.showing]),100,0)), 

    ("school_class_preg_cass_1", If (cass.has_met and cass.isactive and cass.showing,100,0)),
    ("school_class_preg_cass_2", If (cass.has_met and cass.isactive and cass.showing,100,0)),
    ("school_class_preg_cass_3", If (cass.has_met and cass.isactive and cass.showing,100,0)),

    ("school_class_preg_mira_1", If (mira.has_met and mira.isactive and mira.showing,100,0)),
    ("school_class_preg_mira_2", If (mira.has_met and mira.isactive and mira.showing,100,0)),
    ("school_class_preg_mira_3", If (mira.has_met and mira.isactive and mira.showing,100,0)),

    ("school_class_preg_rachel_1", If (rachel.has_met and rachel.showing,100,0)),
    ("school_class_preg_rachel_2", If (rachel.has_met and rachel.showing,100,0)),
    ("school_class_preg_rachel_3", If (rachel.has_met and rachel.showing,100,0)),

    ("school_class_preg_dani_1", If (dani.has_met and dani.showing,100,0)),
    ("school_class_preg_dani_2", If (dani.has_met and dani.showing,100,0)),
    ("school_class_preg_dani_3", If (dani.has_met and dani.showing,100,0)),

    ("school_class_preg_saskia_1", If (saskia.has_met and saskia.showing,100,0)),
    ("school_class_preg_saskia_2", If (saskia.has_met and saskia.showing,100,0)),
    ("school_class_preg_saskia_3", If (saskia.has_met and saskia.showing,100,0)),

    ("school_class_preg_frida_1", If (frida.has_met and frida.showing,100,0)),
    ("school_class_preg_frida_2", If (frida.has_met and frida.showing,100,0)),
    ("school_class_preg_frida_3", If (frida.has_met and frida.showing,100,0)),

    ("school_class_preg_alone", 1),
    ])
    jump expression rand_choice

label school_class_preg_alone:
    "I sit there trying to focus on the class but mostly just daydream."
    jump school_class_preg_end




label school_class_preg_cassmira_1:
    show cass at right1
    show mira at right2
    with dissolve
    cass.name "Not lying about the constipation."
    mira.name "You as well?"
    cass.name "Yeah..."
    jump school_class_preg_end

label school_class_preg_cassmira_2:
    show cass at right1
    show mira at right2
    with dissolve
    cass.name "How do they expect us to work out like this?"
    mira.name "Err... Swimming?"
    cass.name "Well I do already feel like a boat."
    jump school_class_preg_end

label school_class_preg_cassmira_3:
    show cass at right1
    show mira at right2
    with dissolve
    cass.name "...how it's all expected we will go it all again."
    mira.name "Probably will..."
    cass.name "..."
    cass.name "Yeah..."
    jump school_class_preg_end





label school_class_preg_cass_1:
    show cass at right1 with dissolve
    cass.name "Come waddle yourself over here."
    pc "Very funny."
    jump school_class_preg_end

label school_class_preg_cass_2:
    show cass at right1 with dissolve
    pc "Hey."
    cass.name "He..."
    cass.name "Nnng."
    cass.name "I'll be back!"
    hide cass with hpunch
    pc "Nature calls..."
    jump school_class_preg_end

label school_class_preg_cass_3:
    show cass at right1 with dissolve
    cass.name "They say I should glow."
    pc "Radioactive now are you?"
    cass.name "I eat the food here so might be."
    pc "Ha!"
    jump school_class_preg_end





label school_class_preg_mira_1:
    show mira at right1 with dissolve
    mira.name "Actual classes for this thing..."
    pc "Huh?"
    mira.name "They expect it so much they actually have classes for it."
    pc "Well... Look around you."
    mira.name "..."
    jump school_class_preg_end

label school_class_preg_mira_2:
    show mira at right1 with dissolve
    mira.name "Hey [name]..."
    pc "Sounds like you just love it being here."
    mira.name "Don't mind actually. Gets me off my feet."
    pc "Yeah, need more of that."
    mira.name "Yup."
    jump school_class_preg_end

label school_class_preg_mira_3:
    show mira at right1 with dissolve
    mira.name "Maybe I should just go to the beach, lay in the sand."
    pc "I'll join you. Let's go!"
    mira.name "Oh if only."
    jump school_class_preg_end





label school_class_preg_rachel_1:
    show rachel at right1 with dissolve
    rachel.name "Hey preggo buddy!"
    pc "Hey."
    rachel.name "Can I rub your belly?"
    pc "Shoo!"
    jump school_class_preg_end

label school_class_preg_rachel_2:
    show rachel at right1 with dissolve
    rachel.name "Let's go flash our bellies to the boys!"
    pc "That kind of thing is why we are here in the first place."
    rachel.name "And?"
    pc "Err..."
    jump school_class_preg_end

label school_class_preg_rachel_3:
    show rachel at right1 with dissolve
    rachel.name "It was fun when he was putting this here. Not so much now it's getting bigger"
    pc "Wait til you pop."
    rachel.name "What for?"
    pc "Err... It will probably worse than now?"
    rachel.name "You think?"
    pc "..."
    jump school_class_preg_end





label school_class_preg_saskia_1:
    show saskia at right1 with dissolve
    saskia.name "Preggo girls is good usually. Lot of people need their clothes resized."
    saskia.name "Spending most of that time now on my own stuff."
    pc "Right..."
    jump school_class_preg_end

label school_class_preg_saskia_2:
    show saskia at right1 with dissolve
    saskia.name "[name]! Come and see me after and I'll fix you up something nice that fit's with the belly."
    pc "Err, your idea of nice is something I would burst out of even normally."
    saskia.name "Men love a preggo slut. I'll have them all over you."
    pc "Err... Have you seen the belly?"
    saskia.name "Ah. No problems with that already..."
    jump school_class_preg_end

label school_class_preg_saskia_3:
    show saskia at right1 with dissolve
    saskia.name "More guys at the market when you preggo. Swear they come just to look."
    pc "Not like there is any shortage or pregnant girls round here."
    saskia.name "Or perverts."
    pc "Yeah..."
    jump school_class_preg_end





label school_class_preg_frida_1:
    show frida at right1 with dissolve
    frida.name "I got something new your boyfriend will love."
    pc "What boyfriend?"
    frida.name "Whatever one put that in you. You put it up yer arse and it..."
    pc "Nope nope..."
    jump school_class_preg_end

label school_class_preg_frida_2:
    show frida at right1 with dissolve
    frida.name "Y'know [name], some men love it when yer like this."
    pc "I know..."
    frida.name "Ah good. Just make sure to pick the right position."
    pc "Err... Okay..."
    frida.name "Charge them way more if you do that sort of thing."
    jump school_class_preg_end

label school_class_preg_frida_3:
    show frida at right1 with dissolve
    frida.name "Should see [felix.name] with that belly of yours."
    if felix.has_met:
        pc "Yeah, probably end up wanting photos."
        frida.name "Of course."
    else:
        pc "Who's that?"
        frida.name "Ah, not met him yet? You will eventually with that in your belly."
    jump school_class_preg_end





label school_class_preg_dani_1:
    show dani at right1 with dissolve
    dani.name "Think I will stay here for the rest of the day."
    pc "To lazy to get up?"
    dani.name "Yeah..."
    jump school_class_preg_end

label school_class_preg_dani_2:
    show dani at right1 with dissolve
    dani.name "Wonder if people buy milk."
    pc "Err... Actually are there any cows left?"
    dani.name "..."
    pc "What?"
    dani.name "Moooo!"
    jump school_class_preg_end

label school_class_preg_dani_3:
    show dani at right1 with dissolve
    dani.name "I would just go home but I can't be bothered to get up."
    pc "Want me to kick your ass and shoo you away?"
    dani.name "You gonna get off the chair to do that?"
    pc "Ugh! No..."
    jump school_class_preg_end





label school_class_preg_end:
    $ dialogue = renpy.random.choice([
    "...sure to drink lot's of water or else you might find yourself constipated...",
    "...avoid alcohol. Not just just for the babies sake but your own as well. No one needs to be...",
    "...do you a world of good to maintain some exercise and get the blood flowing. You can ask around here for...",
    "...problems, the hospital on Revel will deal with you so don't hesitate. It's also free there for women who...",
    "...a lot of girls in the same situation, so talk with each other and help each other out. It's good to speak to...",
    "...too attached as you may not even get to see or hold the baby. Think of yourself more of a surrogate than the child's mothe...",
    "...find yourself in this situation multiple times. It's not uncommon and don't feel targeted or like one of the unlucky ones. Most of us...",
    "...will usually be fine while working pregnant. It's much more common now than it used to be, especially in the line of work many of you...",
    "...careful on the bus. Makes it harder to get away and might end up bumped around...",
    ])
    feminism "[dialogue]"
    $ player.add_mood(5)
    $ relax(60 - t.minute)
    $ renpy.scene()
    with dissolve
    pause 0.5
    $ school_morning()
    $ dialogue = WeightedChoice([
    ("Class is over and I can't wait to leave.", If (player.hunger < 40,1,0)),
    ("Ah class is over. I was falling asleep in there.", If (player.tired < 35,1,0)),
    ("Well, that's class over.", 1),
    ("Hmm, that's class done with.", 1),
    ])
    pcm "[dialogue]"
    pause 0.5
    $ walk(loc_school_hallway)
    $ dialogue = WeightedChoice([
    ("Home time!", If (player.hunger < 40,1,0)),
    ("Phew. Can relax at last.", If (player.tired < 35,1,0)),
    ("About time classes ended.", 1),
    ])
    pcm "[dialogue]"
    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
