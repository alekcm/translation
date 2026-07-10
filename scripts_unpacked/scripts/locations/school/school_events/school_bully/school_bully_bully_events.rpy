label school_bully_resist_event_1:
    show shane at right1
    shane.name "Ah look, it's the little whore."
    $ player.face_annoyed()
    pc "Tsk."
    hide shane with dissolve
    jump random_event_school_end_picker

label school_bully_resist_event_2:
    show shane at right1
    shane.name "Hey little bitch, how's the punters been treating you?"
    $ player.face_annoyed()
    pc "Tsk."
    hide shane with dissolve
    jump random_event_school_end_picker

label school_bully_resist_event_3:
    show shane at right1
    shane.name "Why are you even here? There are no classes on how to whore yourself out."
    $ player.face_annoyed()
    if player.iswhore:
        pcm "Still need to learn how to count money..."
    else:
        pc "..."
    hide shane with dissolve
    jump random_event_school_end_picker

label school_bully_resist_event_4:
    show marcus at right1
    show shane at right3
    shane.name "Wassa dumb bitch like you doing here anyway? Everyone knows you are just going to sell yourself in the end."
    $ player.face_annoyed()
    pc "*Sigh*"
    hide shane
    hide marcus
    with dissolve
    jump random_event_school_end_picker

label school_bully_resist_event_5:
    show marcus at right1
    show shane at right3
    marcus.name "Look who it is."
    shane.name "Ah the dumb whore. What you her..."
    $ player.face_annoyed()
    pc "Yeah yeah, not interested."
    hide shane
    hide marcus
    with dissolve
    jump random_event_school_end_picker

label school_bully_resist_event_6:
    show shane at right1
    shane.name "Well look at..."
    $ player.face_annoyed()
    pc "Yeah yeah."
    hide shane
    jump random_event_school_end_picker

label school_bully_resist_event_7:
    show shane at right1
    shane.name "Bitch!"
    $ player.face_annoyed()
    pc "*Sigh*"
    jump random_event_school_end_picker

label school_bully_resist_event_8:
    show shane at right5
    shane.name "Here cunt!"
    $ player.punch()
    pc "Ah fuck!"
    $ player.face_angry()
    hide shane with dissolve
    pc "You arsehole!"
    jump random_event_school_end_picker

label school_bully_resist_event_9:
    show shane at right1
    shane.name "Maybe we should have some fun with your friend with the giant tits."
    $ player.face_annoyed()
    pc "*Sigh*"
    jump random_event_school_end_picker

label school_bully_resist_event_10:
    show shane at right1
    shane.name "How's the ginger milk tits doing?"
    $ player.face_annoyed()
    pc "*Sigh*"
    jump random_event_school_end_picker

label school_bully_bully_event_1:
    $ school_bully_adv_bully_stage(1)

    $ rand_choice = WeightedChoice([
    ("school_bully_bully_event_1_1", 1),
    ("school_bully_bully_event_1_2", If (c.ass, 1, 0)),
    ("school_bully_bully_event_1_3", If (c.braless, 1, 0)),
    ("school_bully_bully_event_1_4", If (c.skirt, 1, 0)),
    ("school_bully_bully_event_1_5", If (c.clevage, 1, 0)),
    ("school_bully_bully_event_1_6", If (acc.makeup_on, 1, 0)),
    ("school_bully_bully_event_1_7", If (c.ass and c.skirt, 1, 0)),
    ("school_bully_bully_event_1_8", If (c.skirt and c.pantsless, 1, 0)),
    ("school_bully_bully_event_1_9", If (player.isfat or player.pregnancy == 1, 1, 0)),
    ("school_bully_bully_event_1_10", If (player.pregnancy > 1, 1, 0)),
    ("school_bully_bully_event_1_11", If (player.allure > 100, 1, 0)),
    ("school_bully_bully_event_1_12", If (c.slutty, 1, 0)),
    ("school_bully_bully_event_1_13", If (school_met_friend, 1, 0)),
    ("school_bully_bully_event_1_14", If (school_met_friend, 1, 0)),
    ])
    show marcus at right1
    show shane at right3
    jump expression rand_choice

label school_bully_bully_event_1_1:
    shane.name "Sup bitch?"
    jump school_bully_bully_event_1_end

label school_bully_bully_event_1_2:
    shane.name "Damn, look at the little whore's ass!"
    jump school_bully_bully_event_1_end

label school_bully_bully_event_1_3:
    shane.name "Damn, look at her tits bounce!"
    jump school_bully_bully_event_1_end

label school_bully_bully_event_1_4:
    shane.name "Lift that skirt up for us you dirty whore."
    jump school_bully_bully_event_1_end

label school_bully_bully_event_1_5:
    shane.name "Look at the whore flashing her tits to everyone."
    jump school_bully_bully_event_1_end

label school_bully_bully_event_1_6:
    shane.name "Thank fuck she is wearing makeup. Looking at her face can make us puke."
    jump school_bully_bully_event_1_end

label school_bully_bully_event_1_7:
    shane.name "Showing off your ass in that tight skirt? Want people to know you are up for getting fucked in the toilets?"
    if c.pantsless:
        marcus.name "Not even got anything under it either."
        shane.name "Damn you're right. Didn't even notice. She's a proper whore."
    elif c.thong:
        marcus.name "Nice little thong up her arse as well."
        shane.name "Damn you're right. Didn't even notice."
    jump school_bully_bully_event_1_end

label school_bully_bully_event_1_8:
    shane.name "You see that?"
    marcus.name "Yeah. Bitch ain't even got any pants on."
    shane.name "Whore wants someone to lift her skirt up and give her a good fucking."
    jump school_bully_bully_event_1_end

label school_bully_bully_event_1_9:
    shane.name "Careful, earthquake."
    marcus.name "Don't worry, it's just the fat bitch"
    jump school_bully_bully_event_1_end

label school_bully_bully_event_1_10:
    marcus.name "Look, the preggo bitch."
    shane.name "Yeah, fucking whore!"
    jump school_bully_bully_event_1_end

label school_bully_bully_event_1_11:
    shane.name "All dressed up for hanging round the highway?"
    marcus.name "Might pay you a visit. What time you normally there?"
    jump school_bully_bully_event_1_end

label school_bully_bully_event_1_12:
    shane.name "Dressed like that I think I might have to take you in the toilets and give you what you are asking for."
    jump school_bully_bully_event_1_end

label school_bully_bully_event_1_13:
    shane.name "Having fun with that ginger with the giant tits?"
    pc "Huh?"
    shane.name "Might have to pay her a visit as well."
    jump school_bully_bully_event_1_end

label school_bully_bully_event_1_14:
    shane.name "Who's your friend with the melon tits? Might have to go milk the bitch."
    jump school_bully_bully_event_1_end

label school_bully_bully_event_1_end:
    if renpy.showing("shane") or renpy.showing("marcus"):
        hide shane
        hide marcus
        with dissolve
    $ player.face_worried()
    pcm "Ugh."
    $ player.add_mood(-3)
    jump random_event_school_end_picker



label school_bully_bully_event_2:
    $ school_bully_adv_bully_stage(2)

    $ rand_choice = WeightedChoice([
    ("school_bully_bully_event_2_1", 1),
    ("school_bully_bully_event_2_2", If (c.ass, 1, 0)),
    ("school_bully_bully_event_2_3", If (c.braless, 1, 0)),
    ("school_bully_bully_event_2_4", If (c.skirt, 1, 0)),
    ("school_bully_bully_event_2_5", If (c.clevage, 1, 0)),
    ("school_bully_bully_event_2_6", If (acc.makeup_on, 1, 0)),
    ("school_bully_bully_event_2_7", If (c.ass and c.skirt, 1, 0)),
    ("school_bully_bully_event_2_8", If (c.skirt and c.pantsless, 1, 0)),
    ("school_bully_bully_event_2_9", If (player.isfat or player.pregnancy == 1, 1, 0)),
    ("school_bully_bully_event_2_10", If (player.pregnancy > 1, 1, 0)),
    ("school_bully_bully_event_2_11", If (player.allure > 100, 1, 0)),
    ("school_bully_bully_event_2_12", If (c.slutty, 1, 0)),
    ("school_bully_cass_event_9", 1),
    ])
    jump expression rand_choice

label school_bully_bully_event_2_1:
    show shane at right6
    pause 0.5
    $ player.punch()
    pc "Ugh fuck!"
    shane.name "Sorry, hand slipped."
    jump school_bully_bully_event_2_end

label school_bully_bully_event_2_2:
    show marcus at right1
    show shane at right3
    shane.name "Damn, look at the little whore's ass!"
    $ player.spank()
    shane.name "Keep walking bitch, I wanna see you shake it."
    jump school_bully_bully_event_2_end

label school_bully_bully_event_2_3:
    show marcus at right1
    show shane at right3
    shane.name "Damn, look at her tits bounce! Gonna have to get a better look at them when you are bouncing on my cock."
    jump school_bully_bully_event_2_end

label school_bully_bully_event_2_4:
    show marcus at right1
    show shane at right3
    shane.name "Lift that skirt up for us you dirty whore."
    $ player.spank()
    $ player.face_angry()
    pc "Oi!"
    jump school_bully_bully_event_2_end

label school_bully_bully_event_2_5:
    show marcus at right1
    show shane at right3
    shane.name "Look at that. Going to stick my face between those tits soon."
    jump school_bully_bully_event_2_end

label school_bully_bully_event_2_6:
    show marcus at right1
    show shane at right3
    shane.name "Better make sure to fuck you in an alley like a proper whore. Don't want all that shit on your face dirtying up my bed."
    jump school_bully_bully_event_2_end

label school_bully_bully_event_2_7:
    show marcus at right1
    show shane at right3
    shane.name "Showing off your ass in that tight skirt? Want people to know you are up for getting fucked in the toilets?"
    $ player.spank()
    jump school_bully_bully_event_2_end

label school_bully_bully_event_2_8:
    pause 0.5
    show shane at right6
    $ c.bottom = 0
    $ player.face_shock()
    with vpunch
    pc "Ah fuck!"
    $ pc_dress()
    $ player.face_angry()
    pc "The hell?"
    show marcus smile at right1 with dissolve
    show shane smile with dissolve:
        xzoom -1
    shane.name "Told you, nothing under."
    marcus.name "Fuck. Should take her to the locker room and give her what she wants."
    jump school_bully_bully_event_2_end

label school_bully_bully_event_2_9:
    show marcus at right1
    show shane at right3
    shane.name "Careful, earthquake."
    marcus.name "Don't worry, it's just the fat bitch"
    $ player.punch()
    jump school_bully_bully_event_2_end

label school_bully_bully_event_2_10:
    show marcus at right1
    show shane at right3
    marcus.name "If you wanted to be a breeder bitch, I'll take you in the toilets like the dirty whore you are."
    jump school_bully_bully_event_2_end

label school_bully_bully_event_2_11:
    show shane at right6
    pause 0.5
    $ player.punch()
    pause 0.3
    pc "Ah! Fuck!"
    shane.name "Wonder if the perverts at the highway are still willing to pay for you if you are all bruised?"
    jump school_bully_bully_event_2_end

label school_bully_bully_event_2_12:

    show shane at right6
    pause 0.5
    $ player.spank()
    pause 0.3
    shane.name "Come to the toilets slut and I'll give you the fucking you are asking for."
    jump school_bully_bully_event_2_end

label school_bully_bully_event_2_end:
    if renpy.showing("shane") or renpy.showing("marcus"):
        hide shane
        hide marcus
        with dissolve
    $ player.face_worried()
    pcm "Ugh. Fucking shits."
    $ player.add_mood(-5)
    jump random_event_school_end_picker




label school_bully_bully_event_3:
    $ school_bully_adv_bully_stage(3)

    $ rand_choice = WeightedChoice([
    ("school_bully_bully_event_3_1", 1),
    ("school_bully_bully_event_3_2", If (c.slutty or player.allure > 100, 1,0)),
    ("school_bully_bully_event_3_3", If (player.mood > 60, 1,0)),
    ("school_bully_bully_event_3_4", 1),
    ("school_bully_bully_event_3_5", If (player.tired <= 30, 1, 0)),
    ("school_bully_bully_event_3_6", If (player.isfat or player.pregnancy == 1, 1, 0)),
    ("school_bully_bully_event_3_7", If (c.ass, 1, 0)),
    ("school_bully_cass_event_9", 1),
    ])
    jump expression rand_choice

label school_bully_bully_event_3_1:
    show shane at right6
    shane.name "Outta the way whore!"
    $ player.punch()
    pc "Ugh fuck!"
    jump school_bully_bully_event_3_end

label school_bully_bully_event_3_2:
    show marcus at right1
    show shane at right3
    marcus.name "Look at the whore."
    shane.name "Should take the bitch somewhere and take all her clothes."
    jump school_bully_bully_event_3_end

label school_bully_bully_event_3_3:
    show marcus at right1
    show shane at right3
    shane.name "The bitch looks happy. What, you and your dance whores finally got gangbanged by the idiots playing football?"
    jump school_bully_bully_event_3_end

label school_bully_bully_event_3_4:
    show marcus at right1
    show shane at right3
    shane.name "What do you think? Tie the bitch up in the locker room and let people take turns on her?"
    marcus.name "The whore would probably thank us for it."
    jump school_bully_bully_event_3_end

label school_bully_bully_event_3_5:
    show marcus at right1
    show shane at right3
    shane.name "Looks like the bitch was up all night taking cocks on the highway."
    marcus.name "Probably. Bet she is too dumb to even get the money from them."
    jump school_bully_bully_event_3_end

label school_bully_bully_event_3_6:
    show marcus at right1
    show shane at right3
    shane.name "People on the highway pay to fuck a fat whore like you?"
    jump school_bully_bully_event_3_end

label school_bully_bully_event_3_7:
    show marcus at right1
    show shane at right3
    shane.name "Look at that arse. Should take her in the toilet and ass fuck her 'til she screams."
    marcus.name "Bitch like her would be screaming for more. Arse has probably had more cocks in it than I have had warm meals."
    jump school_bully_bully_event_3_end

label school_bully_bully_event_3_end:
    if renpy.showing("shane") or renpy.showing("marcus"):
        hide shane
        hide marcus
        with dissolve
    $ player.face_worried()
    pcm "Ugh. Cunts."
    $ player.add_mood(-5)
    jump random_event_school_end_picker

label school_bully_bully_event_4:
    $ school_bully_adv_bully_stage(4)

    $ rand_choice = WeightedChoice([
    ("school_bully_bully_event_4_1", 1),
    ("school_bully_bully_event_4_2", If (loc_cur == loc_school_hallway, 1,0)),
    ("school_bully_bully_event_4_3", 1),
    ("school_bully_bully_event_4_4", 1),
    ("school_bully_bully_event_4_5", 1),
    ("school_bully_bully_event_4_6", If (player.isfat or player.pregnancy == 1, 1, 0)),
    ("school_bully_bully_event_4_7", If (c.ass, 1, 0)),
    ("school_bully_bully_event_4_8", 1),
    ("school_bully_bully_event_5_6", If (inv.qty(item_beer_poison) >= 4, 10, 0)),
    ])
    jump expression rand_choice

label school_bully_bully_event_4_1:
    pause 0.5
    $ player.grope_breasts()
    $ player.face_shock()
    pc "Wha..."
    pc "Get off!"
    $ player.grope_end()
    with hpunch
    shane.name "Nice!"
    jump school_bully_bully_event_4_end

label school_bully_bully_event_4_2:
    pause 0.5
    $ walk(loc_school_toilet_boys)
    show marcus at right1
    show shane at right3
    with hpunch
    $ player.face_shock()
    pc "Ah what are you doing?"
    shane.name "Show me your tits."
    $ player.face_worried()
    pc "What?"
    shane.name "Come on, show em to us."
    $ player.face_meek()
    marcus.name "Hurry up or someone will come in and you will have to show them too."
    pc "..."
    $ pc_strip_upper(slow=True)
    show marcus smile
    show shane smile
    shane.name "Good whore."
    marcus.name "Heh."
    shane.name "C'mon, before someone catches us."
    hide shane
    hide marcus
    with dissolve
    $ player.face_normal()
    pc "..."
    $ pc_dress()
    jump school_bully_bully_event_4_end

label school_bully_bully_event_4_3:
    pause 0.5
    show marcus smile at right6
    $ c.bottom = 0
    with vpunch
    pc "Fuck!"
    marcus.name "Got her!"
    hide shane with dissolve
    $ pc_dress()
    pc "Fuck..."
    jump school_bully_bully_event_4_end

label school_bully_bully_event_4_4:
    pause 0.5
    show marcus at right6
    $ player.grope()
    $ player.face_shock()
    pc "Ah!"
    pc "Get off!"
    $ player.grope_end()
    with vpunch
    show shane at right1 with dissolve
    shane.name "Get a feel?"
    show marcus at right6 with dissolve:
        xzoom -1
    marcus.name "Heh yeah."
    jump school_bully_bully_event_4_end

label school_bully_bully_event_4_5:
    pause 0.5
    show shane at right6
    $ player.punch()
    pc "Ahh!"
    shane.name "One for me."
    hide shane with dissolve
    show marcus at right6
    $ player.punch()
    marcus.name "And one for me!"
    hide marcus with dissolve
    shane.name "Haha!"
    pc "Fucking shits!"
    jump school_bully_bully_event_4_end

label school_bully_bully_event_4_6:
    pause 0.5
    show shane at right6
    show marcus at right4
    $ player.spank()
    $ player.face_shock()
    pc "AH!"
    shane.name "Piggy!"
    $ player.spank()
    pc "Stop it!"
    $ player.spank()
    pc "I said stop!"
    shane.name "Ok"
    $ player.punch()
    marcus.name "Heh."
    jump school_bully_bully_event_4_end

label school_bully_bully_event_4_7:
    pause 0.5
    $ player.grope_hips()
    $ player.face_shock()
    pc "Wha..."
    pc "Get off!"
    $ player.grope_end()
    with hpunch
    shane.name "Nice!"
    jump school_bully_bully_event_4_end

label school_bully_bully_event_4_8:
    show shane at right6
    show marcus at right4
    shane.name "How much do people on the highway pay to fuck you?"
    pc "What? I don't..."
    shane.name "I am wondering how much I can make from selling you to the pricks that come to this school."
    shane.name "These pussies probably ain't ever seen a girl naked before. So can sell you to them and make some money."
    pc "What? No!"
    shane.name "Ain't asking for your permission. I am asking how much a whore sells for at the highway. Can easily charge these shits more."
    marcus.name "What? These shits don't have any money. If they did they will be working and not hanging round here all day."
    shane.name "You think so?"
    marcus.name "Any money they can pay for this whore ain't worth our time."
    shane.name "..."
    shane.name "Fuck! Thought I could sell this bitch and make something out of it."
    marcus.name "Na, not with these wimps. Come on, this bitch ain't worth our time."
    hide shane
    hide marcus
    with dissolve
    pcm "Fucking shits!"
    jump random_event_school_end_picker

label school_bully_bully_event_4_end:
    if renpy.showing("shane") or renpy.showing("marcus"):
        hide shane
        hide marcus
        with dissolve
    pcm "Arseholes."
    jump random_event_school_end_picker

label school_bully_bully_event_5:
    $ school_bully_adv_bully_stage(5)

    $ rand_choice = WeightedChoice([
    ("school_bully_bully_event_5_1", 1),
    ("school_bully_bully_event_5_2", 1),
    ("school_bully_bully_event_5_3", 1),
    ("school_bully_bully_event_5_4", If (not writing.forehead, 1, 0)),
    ("school_bully_bully_event_5_5", If (not writing.face, 1, 0)),
    ("school_bully_bully_event_5_6", 1),
    ("school_bully_bully_event_5_6", If (inv.qty(item_beer_poison) >= 4, 10, 0)),
    ])
    jump expression rand_choice

label school_bully_bully_event_5_1:
    call school_bully_bully_event_isolate from _call_school_bully_bully_event_isolate
    shane.name "Let me see what you got here."
    $ player.face_shock()
    $ player.grope()
    with hpunch
    pc "Wha? Hey!"
    shane.name "Can see why the guys on the highway like to pay her."
    $ player.grope()
    pc "What are you doing?"
    shane.name "Shut up."
    $ player.face_meek()
    pc "Stop touching me."
    $ player.grope()
    shane.name "Not bad down here either. Wouldn't pay for the slut though."
    marcus.name "Why bother. Just take the bitch."
    shane.name "Heh, next time."
    $ player.grope_end()
    pause 0.5
    $ player.spank()
    pause 0.5
    shane.name "Come on, lets go."
    hide shane
    hide marcus
    with dissolve
    pcm "Fucking shits!"
    jump random_event_school_end_picker

label school_bully_bully_event_5_2:
    call school_bully_bully_event_isolate from _call_school_bully_bully_event_isolate_1
    shane.name "You like fucking the teachers?"
    pc "What?"
    shane.name "I asked if you like fucking the teachers?"
    pc "I don't do anything like that."
    $ player.punch()
    pc "Ugg!"
    shane.name "Wrong answer."
    shane.name "Do you like fucking the teachers?"
    pc "Yes..."
    shane.name "What? Say it!"
    pc "Yes I like fucking the teachers."
    marcus.name "Haha. Bitch!"
    shane.name "Come on, lets go."
    hide shane
    hide marcus
    with dissolve
    pcm "Fucking shits!"
    jump random_event_school_end_picker

label school_bully_bully_event_5_3:
    call school_bully_bully_event_isolate from _call_school_bully_bully_event_isolate_2
    shane.name "Bet you want to suck on our cocks don't you?"
    pc "What? No!"
    shane.name "Coming here with us. You want us to put you on your knees and put our cocks in your mouth?"
    pc "No."
    marcus.name "No? Prefer it if we fuck your pussy then?"
    shane.name "Yeah little slut like her isn't satisfied with just her mouth. Probably wants one of us in her pussy and the other fucking her arse."
    marcus.name "Oh is that right bitch? Want both of us to fuck you together?"
    marcus.name "Na ain't into that. Prefer to fuck you alone. If you want guys rubbing dicks then go to the faggots on the football pitch."
    shane.name "They probably too busy fucking each other to bother with this bitch. It's why she wants us."
    shane.name "Next time I'll have you choking on my cock."
    marcus.name "Haha."
    shane.name "Come on, lets go."
    hide shane
    hide marcus
    with dissolve
    pcm "Fucking shits!"
    jump random_event_school_end_picker

label school_bully_bully_event_5_4:
    call school_bully_bully_event_isolate from _call_school_bully_bully_event_isolate_3
    shane.name "Come here. I'm gonna make sure everyone knows what a whore you are."
    pc "What?"
    shane.name "Shut up!"
    $ player.face_worried()
    pc "..."
    $ writing.add_writing("forehead", "perm")
    shane.name "There, now there is no hiding what you are."
    marcus.name "Haha."
    shane.name "Come on, lets go."
    hide shane
    hide marcus
    with dissolve
    pcm "Fucking shits!"
    jump random_event_school_end_picker

label school_bully_bully_event_5_5:
    call school_bully_bully_event_isolate from _call_school_bully_bully_event_isolate_4
    shane.name "Come here. I'm gonna make sure everyone knows just how cock hungry you are."
    pc "What?"
    shane.name "Shut up!"
    $ player.face_worried()
    pc "..."
    $ writing.add_writing("face", "perm")
    shane.name "There, now there is no hiding what you are."
    marcus.name "Haha."
    shane.name "Come on, lets go."
    hide shane
    hide marcus
    with dissolve
    pcm "Fucking shits!"
    jump random_event_school_end_picker

label school_bully_bully_event_5_6:
    call school_bully_bully_event_isolate from _call_school_bully_bully_event_isolate_12
    shane.name "What you got on you?"
    pc "Huh?"
    show shane at right6 with hpunch
    $ player.mug(bully=True)
    pc "Ahh!"
    $ player.mug(bully=True)
    pc "Stop!"
    $ player.grope_end()
    shane.name "Thanks bitch."
    jump random_event_school_end_picker

label school_bully_bully_event_6:
    $ school_bully_adv_bully_stage(6)

    $ rand_choice = WeightedChoice([
    ("school_bully_bully_event_6_1", 4),
    ("school_bully_bully_event_6_2", If (c.pants, 1, 0)),
    ("school_bully_bully_event_6_3", If (c.skirt and c.pants == 0, 1, 0)),
    ("school_bully_bully_event_5_6", If (inv.qty(item_beer_poison) >= 4, 10, 0)),
    
    
    
    ])
    jump expression rand_choice

label school_bully_bully_event_6_1:
    call school_bully_bully_event_isolate from _call_school_bully_bully_event_isolate_5
    call school_bully_bully_event_force_strip from _call_school_bully_bully_event_force_strip
    $ rand_choice = WeightedChoice([
    ("school_bully_bully_event_6_1_1", 1),
    ("school_bully_bully_event_6_1_2", 1),
    ("school_bully_bully_event_6_1_3", 1),
    ("school_bully_bully_event_6_1_4", 1),
    ])
    jump expression rand_choice

label school_bully_bully_event_6_1_1:
    $ player.spank()
    pc "Ah!"
    marcus.name "Haha."
    shane.name "Bitch probably likes it. Come on, let's leave the whore."
    hide shane
    hide marcus
    with dissolve
    pc "..."
    pcm "Arseholes."
    $ pc_dress_slow()
    jump random_event_school_end_picker

label school_bully_bully_event_6_1_2:
    $ player.grope()
    $ player.face_shock()
    pc "Hey, what are you doing?"
    shane.name "Getting a feel of these."
    $ player.face_meek()
    $ player.grope()
    pc "Stop it. Someone might come in and see."
    shane.name "Bet you would like that. Getting watched while I feel you up."
    pc "No!"
    $ player.grope_end()
    shane.name "Heh. Come on, let's go."
    marcus.name "What, that's it?"
    shane.name "Yeah. I'll fuck her when we have more time."
    hide shane
    hide marcus
    with dissolve
    pc "..."
    pcm "Arseholes."
    $ pc_dress_slow()
    jump random_event_school_end_picker

label school_bully_bully_event_6_1_3:
    $ player.grope_ass()
    $ player.face_shock()
    pc "Hey, what are you doing?"
    if player.desire > 60:
        shane.name "Fuck, looks like you were looking forward to this. Bitch is already wet."
        marcus.name "Whore like her is used to being dragged off alone and bent over so is prepared for it I bet."
    else:
        shane.name "Seeing how used your shitty cunt is. Making good money from this I bet."
    $ player.face_meek()
    pc "Stop it. Someone might come in and see."
    shane.name "Bet you would like that. Getting watched while I feel you up."
    pc "No!"
    $ player.grope_end()
    shane.name "Heh. Come on, let's go."
    marcus.name "What, that's it?"
    shane.name "Yeah. I'll fuck her when we have more time."
    hide shane
    hide marcus
    with dissolve
    pc "..."
    pcm "Arseholes."
    $ pc_dress_slow()
    jump random_event_school_end_picker

label school_bully_bully_event_6_1_4:
    shane.name "Turn around."
    pc "What? What for?"
    shane.name "Show us your arse."
    pc "..."
    show sb_pose_lookback worried frown with dissolve
    shane.name "Not bad. Can see why people would pay to fuck you."
    if player.check_nowill():
        pc "..."
    else:
        pc "People don't pay me."
        shane.name "Just give it away for free do you?"
        pc "*Sigh*"
    shane.name "Heh. Come on, let's go."
    marcus.name "What, that's it?"
    shane.name "Yeah. I'll fuck her when we have more time."
    hide shane
    hide marcus
    hide sb_pose_lookback
    with dissolve
    pc "..."
    pcm "Arseholes."
    $ pc_dress_slow()
    jump random_event_school_end_picker

label school_bully_bully_event_6_2:
    call school_bully_bully_event_isolate from _call_school_bully_bully_event_isolate_6
    shane.name "Take off your underwear."
    pc "What? Why?"
    shane.name "Shut up and give them to me."
    $ player.face_meek()
    pc "..."
    shane.name "Come on!"
    pc "Ok..."
    if not c.can_access_pants():
        $ pc_strip_lower(slow=True)
    $ wardrobe.drop(globals()["item_pants_" + str(getattr(globals()[tab_top], "pants"))])
    pc "Here."
    shane.name "Good. I'll be keeping these. You can walk around flashing that arse all day."
    marcus.name "Heh. Slut will probably like it."
    shane.name "Come on, let's go."
    hide shane
    hide marcus
    with dissolve
    pcm "Shit..."
    $ pc_dress_slow()
    jump random_event_school_end_picker

label school_bully_bully_event_6_3:
    call school_bully_bully_event_isolate from _call_school_bully_bully_event_isolate_7
    shane.name "Show us what you got under your skirt."
    pc "What...?"
    shane.name "Come on. Give us a show!"
    $ player.face_meek()
    pc "..."
    marcus.name "Stop wasting time."
    pc "..."
    $ pc_strip_lower(slow=True)
    pc "Happy?"
    if player.phair > 0:
        marcus.name "Hairy little bitch ain't she?"
    else:
        marcus.name "Look. Shaved for her customers."
    shane.name "Heh. Come on, let's get out of here."
    hide shane
    hide marcus
    with dissolve
    pc "..."
    pc "Ugh. Shits that they are."
    $ pc_dress_slow()
    jump random_event_school_end_picker

label school_bully_bully_event_7:
    $ school_bully_adv_bully_stage(7)
    call school_bully_bully_event_isolate from _call_school_bully_bully_event_isolate_8

    $ tempname = school_pick_bully_lust()

    call school_bully_bully_event_force_strip from _call_school_bully_bully_event_force_strip_1

    jump school_bully_sex_forced_hand

label school_bully_bully_event_8:
    $ school_bully_adv_bully_stage(8)
    call school_bully_bully_event_isolate from _call_school_bully_bully_event_isolate_9

    $ tempname = school_pick_bully_lust()

    call school_bully_bully_event_force_strip from _call_school_bully_bully_event_force_strip_2

    jump school_bully_sex_forced_blow

label school_bully_bully_event_9:
    $ school_bully_adv_bully_stage(9)
    call school_bully_bully_event_isolate from _call_school_bully_bully_event_isolate_10

    $ tempname = school_pick_bully_lust()

    call school_bully_bully_event_force_strip from _call_school_bully_bully_event_force_strip_3

    jump school_bully_sex_forced_sex_intro

label school_bully_bully_event_10:
    $ school_bully_adv_bully_stage(10)

    call school_bully_bully_event_isolate from _call_school_bully_bully_event_isolate_11

    $ tempname = school_pick_bully_lust()

    call school_bully_bully_event_force_strip from _call_school_bully_bully_event_force_strip_4

    jump school_bully_sex_forced_sold_intro

label school_bully_bully_event_isolate:
    if loc_cur in (loc_school_locker_boys, loc_school_toilet_boys):
        show marcus at right1
        show shane at right3
        shane.name "Look what we have here."
        $ player.face_worried()
        marcus.name "The little whore came to have some fun."
        if not player.check_nowill():
            $ player.face_annoyed()
            pc "*Tsk*"
            pcm "Fuck heads!"
            $ walk(loc_from)
            jump random_event_school_end_picker
        pc "Err, no..."
        pc "I..."
        shane.name "Get over here."
        pc "Hey"
        return

    show marcus at right1
    show shane at right3
    with dissolve
    shane.name "There's the little whore."
    $ player.face_worried()
    pc "Wha? What do you want?"

    if loc_cur == loc_hallway:
        pause 0.5
        $ walk(loc_school_toilet_boys)
        $ player.face_shock()
        with hpunch
        shane.name "Get in there."
        pc "Hey!"
        return

    elif loc_cur.outside and not weather_var >= 2:
        pause 0.5
        $ walk(loc_bushes)
        $ player.face_shock()
        with hpunch
        shane.name "Get over here."
        pc "Hey!"
        return

    shane.name "Come with us."

    if school_bully_quest_bully_event_stage >= 9:
        pcm "Fuck. Again?"
        pc "*Sigh*"
    else:
        pc "What for?"
        shane.name "Shut up and come here."

    pause 0.5

    if loc_cur in (loc_school_classroom, "school_hallway"):
        $ walk(loc_school_toilet_boys)
    elif outside and not weather_var >= 2:
        $ walk(loc_bushes)
    else:
        $ walk(loc_school_locker_boys)
    $ player.face_worried()
    pause 0.5
    pc "Why are you taking me here?"
    return








label school_bully_cass_event_1:
    $ player.face_worried()
    show cass worried at right1
    show shane at right2:
        xzoom -1
    $ dialouge = renpy.random.choice([
    "Milk tits bitch.",
    "Empty headed whore!",
    "Look at you.",
    "Dumb cunt!",
    ])
    shane.name "[dialouge]"
    show cass cry with hpunch
    shane.name "Heh."
    hide shane with dissolve
    cass.name "*SOB*"
    hide cass with dissolve
    pc "..."
    jump random_event_school_end_picker

label school_bully_cass_event_2:
    show cass cry at right1
    cass.name "*SOB*"
    hide cass with dissolve
    pcm "Was it those arseholes...?"
    jump random_event_school_end_picker

label school_bully_cass_event_3:
    show cass cry at right1
    pc "Ah hey... Err... You ok?"
    show cass worried
    cass.name "Yeah..."
    cass.name "It's ok..."
    hide cass with dissolve
    pcm "..."
    jump random_event_school_end_picker

label school_bully_cass_event_4:
    $ player.face_worried()
    show cass worried at right1:
        xzoom -1
    show shane smile at right2:
        xzoom -1
    pause 0.2
    $ dialouge = renpy.random.choice([
    "Huh, why is she with that arsehole?",
    "...",
    "Fuck... She being troubled as well...",
    "Shit... She's with that cunt...",
    ])
    pcm "[dialouge]"
    hide cass
    hide shane
    with dissolve
    pcm "Fuck. He took her to the toilets..."
    pcm "Can't take me there any more so he targets [cass.nname]?"
    pcm "..."
    $ walk(loc_school_toilet_boys)
    $ rand_choice = renpy.random.choice([
    "school_bully_cass_event_4_grope",
    "school_bully_cass_event_4_blow",
    "school_bully_cass_event_4_sex",
    ])
    call expression rand_choice from _call_expression_7

    pcm "Better leave before she sees me. I don't want to make her feel more humiliated than she already does."
    $ renpy.scene()
    with dissolve
    $ walk(loc_school_hallway)
    if "poisoned" in shane.list:
        $ player.face_annoyed()
        $ dialouge = renpy.random.choice([
        "Hopefully those drinks they stole will kick in soon.",
        "Those drinks need to work faster...",
        "Hurry up and die you cunt",
        "Die you piece of shit.",
        ])
        pcm "[dialouge]"
    else:
        $ player.face_worried()
        $ dialouge = renpy.random.choice([
        "I really need to find some way to help her out.",
        "I guess I knew this would happen...",
        "Do I really have to just let this carry on?",
        "Isn't there something I can do?",
        ])
        pcm "[dialouge]"
        $ player.face_angry()
        pcm "*Tsk* Arseholes!"
        $ player.add_mood(-10)
    jump random_event_school_end_picker

label school_bully_cass_event_4_grope:
    $ player.face_shock()
    show cass_bully_grope
    with dissolve
    pcm "Fuck, his hands are all over her..."
    pcm "Not sure why I came in here, not like I can do anything."
    pcm "Fuck."
    return
label school_bully_cass_event_4_blow:
    $ player.face_shock()
    show cass_bully_blow
    with dissolve
    pcm "Ah shit..."
    pcm "Does she really have to do this?"
    pcm "Ugh, if she doesn't want her face all purple I guess so..."
    return
label school_bully_cass_event_4_sex:
    $ player.face_shock()
    show cass_bully_sex
    with dissolve
    pcm "Oh no... [cass.nname]..."
    pcm "With these arseholes?"
    pcm "Fuck..."
    return

label school_bully_cass_event_5:
    show cass cry at right1
    pc "Ah hey..."
    show cass worried
    cass.name "..."
    pc "Sorry..."
    cass.name "It's not like you did anything. Don't worry..."
    hide cass with dissolve
    pcm "..."
    jump random_event_school_end_picker

label school_bully_cass_event_6:
    show shane happy at right
    $ player.face_worried()
    $ randomnum = renpy.random.randint(1, 4)
    if randomnum == 1:
        shane.name "Can't mess with you any more. But that redhead bitch is making a nice replacement. Fun times fucking that bitch."
    elif randomnum == 2:
        shane.name "How's it feel knowing I'm fucking your friend?"
    elif randomnum == 3:
        shane.name "Mmm. That redhead bitch is tasty. She tell you how we fuck her in the toilets?"
    else:
        shane.name "Gave that milk tits friend of your's a good fucking. She tell you?"
    $ player.face_angry()
    pc "Tsk. Cunt!"
    shane.name "Heh!"
    $ remove_from_list(shane.conversation_topics, cass.name)
    hide shane with dissolve
    jump random_event_school_end_picker


label school_bully_cass_event_7:
    show marcus smile at right1
    $ player.face_worried()
    $ randomnum = renpy.random.randint(1, 4)
    if randomnum == 1:
        marcus.name "Mmm. That cunt friend of yours is doing a better job than you did. She doesn't say anything when we fuck her in the toilets."
    elif randomnum == 2:
        marcus.name "How long you think it will be 'til I make your milk tits friend all fat?"
    elif randomnum == 3:
        marcus.name "Your friend tell you how I fucked her in the toilets?"
    else:
        marcus.name "Won't be long 'til I put something extra in your friends belly. Real milk tits then."
    $ player.face_angry()
    pc "Tsk. Cunt!"
    marcus.name "Heh!"
    $ remove_from_list(marcus.conversation_topics, cass.name)
    hide marcus with dissolve
    jump random_event_school_end_picker

label school_bully_cass_event_8:
    $ player.face_worried()
    show shane happy at right1
    show marcus smile at right2
    cass.pregnant_who.name "You see the fat belly I gave your friend?"
    pc "That was you shits?"
    cass.pregnant_who.name "Damn right. Been making sure she gets it nice and deep."
    $ player.face_annoyed()
    pc "Ugh!"
    hide shane
    hide marcus
    with dissolve
    $ remove_from_list(cass.pregnant_who.conversation_topics, "pregnant")
    jump random_event_school_end_picker

label school_bully_cass_event_9:
    $ temp_var_1 = False
    if inv.qty(item_beer_poison) >= 4:
        $ temp_var_1 = True
    $ player.mug(bully=True)
    pc "Ah fuck!"
    show shane at right1 with dissolve
    $ player.grope_end()
    shane.name "Thanks bitch!"
    hide shane with dissolve
    if temp_var_1:
        $ player.face_angry()
        pcm "Yeah go thank yourself by drinking the poison, cunt!"
    jump random_event_school_end_picker





label school_bully_poisoned_event_1:
    $ player.face_worried()
    show shane happy at right1
    show marcus smile at right2
    with dissolve
    shane.name "It's the dumb bitch."
    marcus.name "Heh, you..."
    show shane frown
    shane.name "Ubbb!"
    hide shane with hpunch
    show marcus frown
    marcus.name "Fuck."
    hide marcus with dissolve
    jump school_bully_poisoned_event_end

label school_bully_poisoned_event_2:
    $ player.face_shock()
    show shane frown at right1 with hpunch
    shane.name "Out the way bitch."
    shane.name "Ubbb!"
    hide shane with hpunch
    jump school_bully_poisoned_event_end

label school_bully_poisoned_event_3:
    show shane at right1
    show marcus at left4
    with dissolve
    marcus.name "Maybe we should go to that place on revel?"
    shane.name "The fuck they gonna do?"
    marcus.name "Dunno, but this ain't looking good..."
    hide shane
    hide marcus
    with dissolve
    pcm "Heh..."
    jump school_bully_poisoned_event_end

label school_bully_poisoned_event_4:
    show shane frown at right1 with dissolve
    shane.name "Uhhhhh..."
    shane.name "The fuck you looking at?"
    hide shane with dissolve
    jump school_bully_poisoned_event_end

label school_bully_poisoned_event_end:
    if renpy.showing("shane") or renpy.showing("marcus"):
        hide shane
        hide marcus
        with dissolve
    $ player.face_annoyed()
    $ dialouge = renpy.random.choice([
    "Fuck off cunts.",
    "Have fun with those beers did you?",
    "Die!",
    "Yeah, won't be mouthing off much longer.",
    ])
    pcm "[dialouge]"
    jump random_event_school_end_picker

label school_bully_removed_event_1:
    pcm "Hmm, not seen those two arseholes around for a while. Place feels a lot more peaceful than it used to."
    jump random_event_school_end_picker
label school_bully_removed_event_2:
    pcm "Hmm, normally would have seen the cunt duo by now..."
    pcm "Hope those fuckers don't come back."
    jump random_event_school_end_picker
label school_bully_removed_event_3:
    girl1 "...seen them for a while."
    girl2 "Thank fuck. Hope those shits tried it with someone they shouldn't have an ended up face down somewhere."
    girl1 "Mmmm."
    jump random_event_school_end_picker
label school_bully_removed_event_4:
    pcm "It's not perfect, but this place is so much nicer without seeing the fuckwits around."
    jump random_event_school_end_picker
label school_bully_removed_event_5:
    pcm "Not seen the cunts around for a bit. Maybe that poison did the job."
    jump random_event_school_end_picker
label school_bully_removed_event_6:
    girl1 "They were sick as hell and now they stopped showing up."
    girl2 "Good. Hope the fuckers are dead."
    jump random_event_school_end_picker


label school_bully_removed_event_chain_0:
    $ school_soccer_quest_bully_vanished_stage += 1
    girl1 "...and security was here today. You see them?"
    girl2 "No. What are they doing here?"
    girl1 "Remember those two shits that used to cause trouble?"
    girl2 "Yeah, how could I forget them. They been strung up by security or something?"
    girl1 "No, apparently they haven't been home for ages. Some security guy came here and asked about..."
    jump random_event_school_end_picker

label school_bully_removed_event_chain_1:
    $ school_soccer_quest_bully_vanished_stage += 1
    girl1 "...asking about that [shane.name] and the other idiot."
    girl2 "The head was? What does he care?"
    girl1 "No idea. He gave up when anyone he asked just commented they were glad they were gone."
    girl2 "*Tsk* Of course everyone is. Those two were a cancer to this place..."
    jump random_event_school_end_picker

label school_bully_removed_event_chain_2:
    $ school_soccer_quest_bully_vanished_stage += 1
    girl1 "...heard about them?"
    girl2 "Why would I care about them?"
    girl1 "This is good. So apparently some wild foxes dug them up."
    girl2 "What? Dug them up?"
    girl1 "Hah, yeah. They were dead and buried."
    girl2 "Wow..."
    jump random_event_school_end_picker

label school_bully_removed_event_chain_3:
    $ school_soccer_quest_bully_vanished_stage += 1
    girl1 "...about them again."
    girl2 "And?"
    girl1 "Everyone they asked just commented how happy they were. All smiles an happiness at the news."
    girl2 "How did security react?"
    girl1 "Think he got the message that they are not worth looking into. He ended up just relaxing in the cafeteria for the rest of the day before leaving."
    girl2 "Hah, that's great..."
    jump random_event_school_end_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
