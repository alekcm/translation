label school_class_normal_svetrachel:
    $ rand_choice = WeightedChoice([
    ("school_class_normal_svetrachel_1", 100),
    ("school_class_normal_svetrachel_2", 100),
    ("school_class_normal_svetrachel_3", 100),
    ("school_class_normal_svetrachel_4", 100),
    ("school_class_normal_svetrachel_5", If(player.mood < 30, 100, 0)),
    ("school_class_normal_svetrachel_6", If ( not rachel.showing, 100, 0)),
    ("school_class_normal_svetrachel_7", If (weather_var > 2 and player.isslut,100,0)),
    ("school_class_normal_svetrachel_8", If ("rape" in rachel.conversation_topics,300,0)),
    ("school_class_normal_svetrachel_9", If ("pregnant" in rachel.conversation_topics and not rachel.showing,1000,0)),  
    ("school_class_normal_svetrachel_10", If ("lover" in rachel.conversation_topics,100,0)),
    ("school_class_normal_svetrachel_11", If ("lover" in rachel.conversation_topics,100,0)),
    ("school_class_normal_svetrachel_12", If (player.allure > 100,100,0)),
    ])
    jump expression rand_choice

label school_class_normal_svetrachel_1:
    show rachel at right1 with dissolve
    pc "Morning."
    rachel.name "So... We are alone."
    pc "Err, yeah?"
    rachel.name "Are you fucking one of those boys?"

    if player.check_nowill():
        $ player.face_shock()
        pc "Ssshhhh. Don't say such things so loud."
    else:
        $ player.face_shy()
        pc "Errr..."
    if school_soccer_quest.sex:
        if player.isslut and drake.sex and dan.sex and nate.sex:
            pc "Come here..."
            rachel.name "Oh?"
            show rachel at right6 with dissolve
            pc "I am fucking all of them."
            show rachel happy
            pc "I drink with them at night and let them take turns."
            rachel.name "Ooooohh!!!"
            rachel.name "Haha. Good for you."
            rachel.name "Maybe I should join."
            pc "They would love that."
            jump school_class_normal_end
        elif player.check_nowill():
            pc "..."
        else:
            pc "Wouldn't you like to know."
        show rachel happy
        rachel.name "Ahhh!"
        pc "Shhhhhh!!!"
        rachel.name "Okay ok."
    else:
        pc "Nooooo."
        rachel.name "Not yet? Ok."
        rachel.name "Give it time."
    jump school_class_normal_end

label school_class_normal_svetrachel_2:
    show svet worried at right1
    show rachel at right2
    with dissolve
    svet.name "... getting the bus?"
    rachel.name "You lot complain too much. It's not as bad as you make out."
    pc "It's not?"
    rachel.name "Some harmless fun in the morning."
    svet.name "Err..."
    pc "Harmless?"
    show rachel happy
    rachel.name "You should try it. Perks you right up in the morning."
    pc "..."
    jump school_class_normal_end

label school_class_normal_svetrachel_3:
    show svet at right1 with dissolve
    pc "Morning."
    svet.name "Morning [name]."
    show rachel worried at right2 with dissolve
    rachel.name "Uggghh. Morning."
    pc "Late night?"
    rachel.name "Ugh. The noise outside on the street last night. Like a gang of elephants partying."
    pc "Oh? I would love to see that."
    rachel.name "Uggghhhhhh..."
    jump school_class_normal_end

label school_class_normal_svetrachel_4:
    show svet at right1
    show rachel at right2
    with dissolve
    rachel.name "... he was nice."
    pc "Morning. [rachel.name] making new friends again?"
    svet.name "As always."
    rachel.name "C'mon, people are friendly if you give them a chance."
    svet.name "Yeah, if you say so."
    jump school_class_normal_end

label school_class_normal_svetrachel_5:
    show rachel at right1 with dissolve
    pc "Morning."
    rachel.name "Morning [name]. Up for some fun?"
    pc "Huh?"
    rachel.name "I was teasing some boy this morning and he's waiting for me in the toilets."
    pc "Err. Okay?"
    rachel.name "Looking at your face though, looks like you could do with the fun more than me."
    pc "Err..."
    if player.check_sex_agree(5):
        menu:
            "Sure. I could do with the fun":
                rachel.name "Have fun."
                pc "Yeah... The boys toilet?"
                rachel.name "Yeah."
                pcm "Hmmm."
                hide rachel
                $ walk(loc_school_hallway)
                pause 0.5
                $ walk(loc_school_toilet)
                pcm "Hope no one notices me."
                $ walk(loc_school_toilet_boys)
                guy "Err. Hey?"
                pc "Hey, [rachel.name] couldn't make it so I am here instead."
                guy "Oh? Well that's fine."
                pc "So... Want to have some fun?"
                guy "Of course!"
                $ rand_choice = renpy.random.choice([
                "school_rep_sex_blowjob",
                "school_rep_sex_handjob",
                ])
                jump expression rand_choice
            "No thanks":

                $ NullAction()
    rachel.name "Okay then. Well, see ya."
    hide rachel with dissolve
    pc "Yeah... See you."
    jump school_class_normal_end

label school_class_normal_svetrachel_6:
    show svet at right1
    show rachel at right2
    with dissolve
    svet.name "...wind up pregnant if you keep messing about like that."
    pc "Morning."
    if player.pregnancy >= 2:
        svet.name "Like [name] here."
        pc "Like me what?"
        svet.name "[rachel.name] is going about getting a fat belly just like you."
        rachel.name "Stop worrying [svet.nname]. Anyway, I bet it can be fun."
        svet.name "*Sigh*"
    else:
        pc "Playing it risky?"
        rachel.name "Stop worrying you two. It'll be fine."
        svet.name "Yeah. Until it's not..."
    jump school_class_normal_end

label school_class_normal_svetrachel_7:
    show rachel at right1 with dissolve
    pc "Morning."
    rachel.name "Morning. You seen [svet.nname]?"
    pc "No, didn't see her. Why?"
    rachel.name "..."
    show rachel happy at right6 with dissolve
    rachel.name "She will get mad at me if she hears this."
    pc "Oh?"
    rachel.name "It was raining today so I got the bus."
    rachel.name "Well, you know what it's like. Some guy putting his hand up my skirt and rubbing me."
    $ player.face_worried()
    pc "Yeah morning bus is like that. Why would [svet.nname] be mad for that?"
    rachel.name "Well, he was wanking with one hand and touching me with the other. So I pressed myself against his cock."
    $ player.face_neutral()
    pc "Oooh?"
    rachel.name "He slipped my knickers down a bit and pressed his cock between my legs."
    $ player.face_happy()
    pc "You let him fuck you on the bus?"
    rachel.name "I can still feel him leaking out of me now."
    $ player.face_laugh()
    pc "Oh you dirty whore."
    rachel.name "Right?"
    jump school_class_normal_end

label school_class_normal_svetrachel_8:
    show rachel worried at right1 with dissolve
    pc "Morning."
    pc "You okay?"
    rachel.name "Not really."
    pc "Err. Want to talk about it?"
    show rachel angry
    rachel.name "*Huff* I was walking home last night and cut through the park."
    pc "Hmmm..."
    rachel.name "Some fucker pulled me in the bushes and had his way with me."
    $ player.face_worried()
    pc "Ah. Sorry..."
    show rachel worried
    rachel.name "It's fine. Not like it hasn't happened to everyone in here."
    pc "Mmmm..."
    $ remove_from_list(rachel.conversation_topics, "rape")
    jump school_class_normal_end

label school_class_normal_svetrachel_9:
    show rachel at right1 with dissolve
    pc "Morning."
    rachel.name "Ugh. Morning [name]."
    pc "That good of a morning?"
    rachel.name "I think [svet.nname] was right."
    pc "About what?"
    rachel.name "About me playing with fire."
    pc "Err. Ok. Still no idea what you mean."
    rachel.name "I felt all nauseous and puked this morning. Pretty sure I'm preggo."
    pc "Oh? Congratulations?"
    rachel.name "Yeah... Thanks."
    $ remove_from_list(rachel.conversation_topics, "pregnant")
    if rachel.pregnant_who in [drake,nate,dan]:
        $ add_to_list(rachel.conversation_topics, "pregnant_" + rachel.pregnant_who._original_name)
    jump school_class_normal_end

label school_class_normal_svetrachel_10:
    show rachel at right1 with dissolve
    pc "Morning."
    show rachel happy at right6
    pc "Err..."
    rachel.name "I had a date."
    pc "Ooh?"
    rachel.name "I think I have bite marks on my ass."
    pc "What?"
    rachel.name "It was amazing."
    pc "Err. Ok. Great?"
    $ remove_from_list(rachel.conversation_topics, "lover")

    jump school_class_normal_end

label school_class_normal_svetrachel_11:
    show svet at right1
    show rachel happy at right2
    with dissolve
    svet.name "...tell me you invited him back?"
    rachel.name "Damn right I did. I didn't sleep any last night."
    svet.name "Ugh [rachel.name]..."
    rachel.name "I didn't even shower. I'm still all smelly from him."
    svet.name "Ugh..."
    if player.isslut:
        $ player.face_happy()
        pc "Nice!"
        rachel.name "Right?!"
        svet.name "Not you too..."
    $ remove_from_list(rachel.conversation_topics, "lover")
    jump school_class_normal_end

label school_class_normal_svetrachel_12:
    show rachel at right1 with dissolve
    rachel.name "Ah you're here?"
    pc "Good morning to you too."
    show rachel at right6 with dissolve:
        xzoom -1
    rachel.name "Come with me."
    pc "Err. Okay..."
    $ walk(loc_school_hallway)
    pc "Where are we..."
    rachel.name "Ssshhhh..."
    $ walk(loc_school_toilet)
    rachel.name "..."
    rachel.name "No one here...?"
    pc "What are we..."
    rachel.name "Now. Quick."
    $ walk(loc_school_toilet_boys, trans=False)
    $ player.face_shock()
    with hpunch
    pc "Wha..."
    pc "What are we doing in here?"
    $ player.face_normal()
    show rachel happy with dissolve:
        xzoom 1
    rachel.name "Someone I have been fooling around with fancies you."
    pc "Ok. And?"
    if player.isslut:
        rachel.name "I told him you are a huge slut and would let him fuck you."
    elif player.iswhore:
        rachel.name "I told him I could arrange a freebie with you."
    elif player.has_perk(perk_preg_want):
        rachel.name "I told him as long as he tries to knock you up, you'd let him do what he wants."
    else:
        rachel.name "And I told him I would bring you here to have fun with him."
    if not player.check_sex_agree(4):
        $ player.face_shock()
        pc "Whaa??? What the hell?"
        hide rachel
        $ walk(loc_school_toilet, trans=False)
        $ player.face_worried()
        with hpunch
        pc "Christ. Setting me up like that."
        pc "*Sigh*"
        jump travel
    $ player.face_shy()
    pc "What? Seriously?"
    rachel.name "Yeah, he's in the cubicle. Wanna fuck him?"
    menu:
        "Sure. Let's have some fun":
            rachel.name "Heh, enjoy you two. I'll go back to class."
            pc "Right..."
            hide rachel with dissolve
            guy "Hey."
            pc "Hey. Ready for some fun?"
            guy "With you? Fuck yes I am!"
            $ rand_choice = renpy.random.choice([
            "school_rep_sex_blowjob",
            "school_rep_sex_handjob",
            ])
            jump expression rand_choice
        "What? No way":
            pc "Sorry. Your friend is on his own."
            rachel.name "Aww. Well whatever. You head in and I'll catch up."
            pc "Right."
            hide rachel
            $ walk(loc_school_toilet)
            pc "Didn't expect that."
            jump travel


label school_class_normal_anabeldani:


    $ rand_choice = WeightedChoice([
    ("school_class_normal_anabeldani_1", 1),
    ("school_class_normal_anabeldani_2", 1),
    ("school_class_normal_anabeldani_3", 1),
    ("school_class_normal_anabeldani_4", If(not anabel_here(), 1, 0)),
    ("school_class_normal_anabeldani_5", 1),
    ("school_class_normal_anabeldani_6", If (player.allure>100,1,0)),
    ("school_class_normal_anabeldani_7", If (weather_var > 2,1,0)),
    ("school_class_normal_anabeldani_8", If (weather_var > 2,1,0)),
    ("school_class_normal_anabeldani_9", If ("rape" in dani.conversation_topics,1,0)),
    ("school_class_normal_anabeldani_10", If ("rape" in dani.conversation_topics,1,0)),
    ])
    jump expression rand_choice

label school_class_normal_anabeldani_1:
    show anabel happy at right1
    show dani happy at right2
    with dissolve
    anabel.name "...and couldn't even carry on I was laughing so much."
    pc "Morning."
    dani.name "Morning [name]. What did they do after that?"
    anabel.name "What could they do?"
    dani.name "Mmmm."
    jump school_class_normal_end

label school_class_normal_anabeldani_2:
    show anabel at right1
    show dani at right2
    with dissolve
    dani.name "...for the rest of the month."
    anabel.name "Yeah I guess. Morning [name]."
    pc "Morning."
    dani.name "Well, no different to any other month."
    pc "Err. Period?"
    dani.name "Noo! Rent."
    pc "Ah."
    jump school_class_normal_end

label school_class_normal_anabeldani_3:
    show anabel at right1
    show dani at right2
    with dissolve
    dani.name "...that guy that was flirting with you?"
    pc "Morning. [anabel.nname] found a boyfriend?"
    anabel.name "No way! Just some guy trying to hit on me."
    pc "Oh? And?"
    anabel.name "And what?"
    pc "And and?"
    anabel.name "Ugh, you two. I'm not going to meet him again."
    dani.name "[anabel.nname] is too shy by the looks of it."
    jump school_class_normal_end

label school_class_normal_anabeldani_4:
    show dani at right1 with dissolve
    pc "Morning."
    dani.name "Hey [name]."
    pc "No [anabel.nname] today?"
    dani.name "No, not seen her today yet."
    pc "Spending time with a boyfriend?"
    dani.name "Ha, if only."
    jump school_class_normal_end

label school_class_normal_anabeldani_5:
    show anabel at right1 with dissolve
    pc "Morning."
    anabel.name "Hey [name]. Morning."
    pc "You ok? Your face is all red."
    anabel.name "Ah!"
    pc "Hmmm..."
    $ player.face_happy()
    pc "Someone caught your eye?"
    anabel.name "No, nothing like that."
    pc "Don't be shy. Point him out to me. I might be able to introduce the two of you."
    show dani at right2
    dani.name "Morning. [anabel.nname] found someone?"
    anabel.name "Don't you start as well."
    jump school_class_normal_end

label school_class_normal_anabeldani_6:
    show anabel at right1
    show dani at right2
    with dissolve
    pc "Morning."
    dani.name "Morning [name]."
    anabel.name "Morning. Don't you get a bit much attention dressed like that?"
    if player.has_perk(perk_exhibitionist):
        pc "Yeah. I like the attention."
    else:
        pc "Huh? I could wear a potato sack and these perverts would still be perverts."
        pc "So I wear what I like."
    anabel.name "Wish I had your confidence."
    show dani happy
    dani.name "Don't need confidence when you have those huge things..."
    if player.breasts == 3:
        dani.name "Both of you. I am surrounded by breast monsters!"
    show anabel angry
    anabel.name "[dani.fname]!"
    jump school_class_normal_end

label school_class_normal_anabeldani_7:
    show anabel at right1 with dissolve
    pc "Morning."
    anabel.name "Morning [name]."
    show dani worried at right2 with dissolve
    dani.name "Morning."
    anabel.name "Hey. Everything ok?"
    dani.name "Ugh yeah. Weather is shit so I got the bus."
    anabel.name "Ah. Need to borrow some knickers?"
    dani.name "Probably. I'll go to the toilet and clean up a bit..."
    anabel.name "I'll come with. See you in a bit [name]"
    hide dani
    hide anabel
    with dissolve
    if player.isslut:
        pcm "Maybe I should be getting the bus more often."
    jump school_class_normal_end

label school_class_normal_anabeldani_8:
    show dani at right1
    show anabel worried at right2
    with dissolve
    anabel.name "...just dealing with it since they were only groping."
    pc "Morning. More bus adventures?"
    anabel.name "Are there any other types of adventure in this kind of weather. I swear my breasts are all bruised now."
    dani.name "Well, good you are wearing trousers I guess."
    anabel.name "It wasn't long before they were getting tugged down. Spend most of the ride with some guy trying to put his fingers in me."
    dani.name "Ugh..."
    if player.isslut:
        $ player.add_desire(15)
        pcm "Is it wrong of me to be getting turned on by this?"
    jump school_class_normal_end

label school_class_normal_anabeldani_9:
    show anabel at right1 with dissolve
    pc "Morning."
    anabel.name "Morning [name]."
    pc "Looks like you..."
    $ dani.have_sex(busgroper, forced=True)
    show dani worried at right2
    dani.name "Anyone able to give me some underwear?"
    anabel.name "Err, I think so. Everything ok?"
    dani.name "Ugh... Yeah it's fine. I let someone on the bus get away with too much on the way here."
    anabel.name "Shit. He didn't manage to go too far did he?"
    dani.name "Spent most of the ride \"too far\"..."
    anabel.name "Err... Do you need to shower first or just new underwear?"
    dani.name "..."
    dani.name "Shower..."
    hide dani
    hide anabel
    with dissolve
    pc "..."
    if player.isslut:
        $ player.add_desire(15)
        if player.desire > 85:
            pc "Wish someone would go too far with me..."
    $ remove_from_list(dani.conversation_topics, "rape")
    jump school_class_normal_end

label school_class_normal_anabeldani_10:
    show anabel at right1 with dissolve
    pc "Morning."
    anabel.name "Morning [name]."
    pc "Looks like you..."
    show dani worried at right2
    dani.name "Morning."
    pc "Hey."
    anabel.name "You okay?"
    dani.name "Not really. I wen't out last night and had a few too many."
    anabel.name "Oh? Good for you."
    dani.name "Well, it was fine until it wasn't. Wound up a bit too drunk and couldn't make it home so fell asleep in some bushes."
    anabel.name "Oh? That's not good."
    dani.name "It wasn't. Woke up to my dress hitched up to my armpits and my body all sore."
    anabel.name "..."
    dani.name "Probably going to have to take a test..."
    $ remove_from_list(dani.conversation_topics,"rape")
    jump school_class_normal_end

label school_class_normal_dani_postdance:
    show dani at right1 with dissolve
    pc "Morning."
    dani.name "Morning [name]."
    call dani_postdance_company_conv from _call_dani_postdance_company_conv_1
    jump school_class_normal_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
