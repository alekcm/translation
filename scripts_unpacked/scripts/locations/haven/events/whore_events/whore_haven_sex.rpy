label haven_sex_repeatable_start:
    $ haven_whore_pay()
    $ player.sex_sold(havenman, 0, main_quest_05)
    if not loc_cur == loc_haven_bed:
        pc "Let's go to my bunk."
        $ walk(loc_haven_bed)

    $ dialouge = renpy.random.choice([
    "Whores here are much nicer than those highway bitches.",
    "Mmm, sexy little thing. Come here.",
    "Not seen you round 'ere before. Much nicer than the usual lot.",
    "Love the easy girls round this place."
    ])
    hav "[dialouge]"
    $ renpy.scene()
    with dissolve
    jump expression WeightedChoice([
    ("haven_sex_repeatable_grope", 100),
    ("haven_sex_repeatable_kiss", 100),
    ("haven_sex_repeatable_blow", 50),
    ("haven_sex_repeatable_sex_picker", 25),
    ])





label haven_sex_repeatable_grope:
    show haven_grope grope happy with dissolve
    $ dialouge = renpy.random.choice([
    "Ooh? Like them do you?",
    "Mmm, like my tits?",
    "Oh? Straight to it then?",
    "Not wasting any time are you?"
    ])
    pc "[dialouge]"
    $ player.grope(hands=False, steal=True)
    $ dialouge = renpy.random.choice([
    "Pierced? So sexy.",
    "Feel just as nice as they look.",
    "Sexy little girl.",
    "So nice. I knew you were the right one to pay."
    ])
    hav "[dialouge]"
    pc "Oh?"
    $ player.grope(hands=False, steal=True)
    $ dialouge = renpy.random.choice([
    "Well, you can have more than my tits",
    "Wait til you see the rest of me.",
    "Got more than just nice tits.",
    ])
    pc "[dialouge]"
    jump expression WeightedChoice([
    ("haven_sex_repeatable_blow", 100),
    ("haven_sex_repeatable_wank", 100),
    ])

label haven_sex_repeatable_kiss:
    show haven_kiss with dissolve
    pc "Mmmf."
    $ player.grope(hands=False, steal=True)
    $ dialouge = renpy.random.choice([
    "Paying for romance are you?",
    "People don't usually pay for kissing.",
    "Not what I expected when you wanted to pay for some time.",
    ])
    pc "[dialouge]"
    $ dialouge = renpy.random.choice([
    "I have time so we can go slow.",
    "No need to rush to it.",
    "Some warm up first is nice.",
    ])
    hav "[dialouge]"
    $ player.grope(hands=False, steal=True)
    pc "Mmmff."
    "I mostly stand there and let him do what he wants. His tongue is invading my mouth while his hands roam all over my body."
    $ player.grope(hands=False, steal=True)
    "It's a good job people in [haven] have pretty good hygiene otherwise this might be disgusting. But as it is it feels ok."
    "I can even close my eyes and imagine I am not being paid to do this and it's all for fun."
    pc "*MWA*"
    $ player.grope(hands=False, steal=True)
    pcm "Think that's enough kissing. Not gonna get him off like this."
    pc "Want something a bit more?"
    jump expression WeightedChoice([
    ("haven_sex_repeatable_blow", 100),
    ("haven_sex_repeatable_wank", 100),
    ])

label haven_sex_repeatable_wank:
    $ player.sex_hand(havenman, main_quest_05)
    $ renpy.scene()
    show haven_grope grope mast penis
    with dissolve
    pc "Like this?"
    hav "Mmmm..."
    $ player.grope(hands=False, steal=True)
    $ dialouge = renpy.random.choice([
    "Like looking at my tits while I wank you?",
    "Bet you love it. A whore wanking you off while you play with her tits.",
    "Tits in your hand and your cock in mine. Bet you love it.",
    ])
    pc "[dialouge]"
    "I stand there wanking him off while he ogles me and paws at my breasts."
    $ player.grope(hands=False, steal=True)
    "His cock is hard and warm in my hand and feels kinda nice. His groping starts to get much more primal the more I wank him."
    jump expression WeightedChoice([
    ("haven_sex_repeatable_wank_cum", 100),
    ("haven_sex_repeatable_blow_catcher", 100),
    ])

label haven_sex_repeatable_wank_cum:
    pc "Having fun?"
    hav "Ughh!"
    pc "Oh?"
    pcm "He's about to cum. I should go faster to finish him off."
    "I start to furiously wank his cock and I can feel precum leaking out of it."
    pc "Oh, Come on, let's see it."
    hav "Nnnng!"
    $ player.sex_cum(havenman, "hand", main_quest_05)
    pc "Oooh, here it is..."
    hav "Haaaaaaa!"
    hav "Mmmmmm."
    show haven_grope hold nopenis with dissolve
    pc "Someone enjoyed themself."
    hav "Sure did."
    jump haven_sex_repeatable_end

label haven_sex_repeatable_blow_catcher:
    hav "Haaa. Let me feel you sucking on it."
    pc "Oh?"
    jump haven_sex_repeatable_blow
label haven_sex_repeatable_blow:
    $ player.sex_oral(havenman, main_quest_05)
    $ renpy.scene()
    show haven_blow wait
    with dissolve
    "I get down on my knees and take a good look at his cock in front of my face"
    if not numgen(0,3):
        show haven_blow cum with dissolve
        show haven_blow lookup with dissolve
    show haven_blow wait happy with dissolve
    pc "Much bigger up close."
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        show haven_blow cum with dissolve
        show haven_blow 2h with dissolve
    elif randomnum == 2:
        show haven_blow cum with dissolve
        show haven_blow 1h with dissolve
    else:
        show haven_blow ballsuck with dissolve
    hav "Ahh yes!"
    if player.check_horny(extreme=True):
        pc "Mmmmmm."
    $ dialouge = renpy.random.choice([
    "This is what makes whores here the best.",
    "Girls here know just what we want.",
    "Mmm, nothing better than a whores lips round yer cock.",
    ])
    hav "[dialouge]"
    if player.check_horny(extreme=True):
        pc "♥"
    hav "Bet you love this just as much as I do."
    show haven_blow wait with dissolve
    $ dialouge = renpy.random.choice([
    "Could be worse.",
    "It's what makes Haven girls the best right?",
    "I like to make an impression.",
    ])
    pc "[dialouge]"
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        show haven_blow cum with dissolve
        show haven_blow 2h with dissolve
    elif randomnum == 2:
        show haven_blow cum with dissolve
        show haven_blow 1h with dissolve
    else:
        show haven_blow ballsuck with dissolve
    if weightgen(10, 100):
        jump haven_sex_repeatable_sex_cum_bj_catcher
    else:
        hav "Fuck! I think I want to put my cock somewhere warmer."
        show haven_blow wait with dissolve
        pc "Oh?"
        pc "Come here."
        hide haven_blow with dissolve
        jump haven_sex_repeatable_sex_picker

label haven_sex_repeatable_sex_picker:
    $ c.top = 0
    $ c.bottom = 0
    $ c.pants = 0
    jump expression WeightedChoice([
    ("haven_sex_repeatable_sex_onback", 100),
    ("haven_sex_repeatable_sex_cowgirl", 100),
    ("haven_sex_repeatable_sex_bentover", 100),
    ])





label haven_sex_repeatable_sex_onback:
    "I lay on the bed and beckon the guy over to join me."
    show haven_onback at right with dissolve
    pc "Like what you see?"
    show haven_onback mast up with dissolve
    $ dialouge = renpy.random.choice([
    "Fucking amazing. I'm gonna have fun with you.",
    "Such a sexy girl. Best one I've had I think.",
    "Just asking for it aren't ya?",
    ])
    hav "[dialouge]"
    pc "Mmmm."
    if not numgen(0,6):
        jump haven_sex_repeatable_sex_cum_premature
    show haven_onback poke oh with dissolve
    $ dialouge = renpy.random.choice([
    "Not sure I've had someone as sexy as you on the end of my cock before.",
    "Such a sexy girl. Best one I've had I think.",
    "Girl as sexy as you. Think I'll have to make this a regular thing.",
    ])
    hav "[dialouge]"
    $ player.sex_vag(havenman, main_quest_05)
    show haven_onback sex ag with dissolve
    pc "Ooooh fuck!"
    hav "Ahhh so nice and warm."
    "He holds onto my thighs and pulls himself deep into me. He has no rhythm and it's almost like an animal having sex with me."
    "I guess it's not something he has done too often and so just goes at it as best he can."
    "He no doubt won't last very long at this rate."
    hav "Fuck yes!"
    pc "Ooohh!"
    $ player.sex_cum_location_offer(
    difficulty=3, 
    cum_want="haven_sex_repeatable_sex_cum_want", 
    cum_notwant="haven_sex_repeatable_sex_cum_notwant", 
    cum_pullout="haven_sex_repeatable_sex_cum_pullout",
    cum_pullout_bj="haven_sex_repeatable_sex_cum_bj",  
    cum_pullout_poke="haven_sex_repeatable_sex_cum_poke",
    cum_bj="haven_sex_repeatable_sex_cum_bj",    
    
    block_anal_check=True
    )





label haven_sex_repeatable_sex_cowgirl:
    "I lay the guy down on my bunk and straddle him."
    show haven_gangbang penisup at right with dissolve
    $ dialouge = renpy.random.choice([
    "Like my tits in your face?",
    "Keeping you very warm like this.",
    "Tits in your face and something hard poking me. What could be better?",
    ])
    pc "[dialouge]"
    "I rub myself up and down his cock getting myself ready and his cock slick with my juices."
    hav "Mmmm."
    if not numgen(0,6):
        jump haven_sex_repeatable_sex_cum_premature
    $ player.spank()
    $ dialouge = renpy.random.choice([
    "Not sure I've had someone as sexy as you on top of me before.",
    "Such a sexy girl. Best one I've had I think.",
    "Girl as sexy as you. Think I'll have to make this a regular thing.",
    ])
    hav "[dialouge]"
    $ player.sex_vag(havenman, main_quest_05)
    show haven_gangbang penisvag with dissolve
    pc "Ooooh fuck!"
    hav "Ahhh so nice and warm."
    "I ride back and forth while he gropes at my tits. He just lays there and let's me do most of the work."
    if numgen():
        $ renpy.scene()
        show haven_cowgirl happy
        with dissolve
        "I sit up and play with my tits while bouncing up and down. He holds on to me grunting and pawing at my thighs."
    else:
        "I look him in the eyes as I ride him. His face contorting with pleasure and moans escaping his mouth."
    "He is perfectly content with letting me do all the work so I ride at quite a fast pace. Mostly to get him off quicker but also for my own pleasure."
    $ player.spank()
    "He no doubt won't last very long at this rate."
    hav "Fuck yes!"
    pc "Ooohh!"
    $ player.sex_cum_location_offer(
    difficulty=0, 
    cum_want="haven_sex_repeatable_sex_cum_want", 
    cum_notwant="haven_sex_repeatable_sex_cum_want", 
    cum_pullout="haven_sex_repeatable_sex_cum_pullout",
    block_anal_check=True
    )





label haven_sex_repeatable_sex_bentover:
    "I bend over on my bunk and present myself to him."
    show haven_presentass at right with dissolve
    pc "How do I look?"
    show haven_presentass mast with dissolve
    hav "Fuck. Like a good whore."
    pc "Mmmm."
    if not numgen(0,6):
        jump haven_sex_repeatable_sex_cum_premature
    show haven_presentass poke with dissolve
    $ player.spank()
    $ dialouge = renpy.random.choice([
    "Not sure I've had someone as sexy as you on the end of my cock before.",
    "Such a sexy girl. Best one I've had I think.",
    "Girl as sexy as you. Think I'll have to make this a regular thing.",
    ])
    hav "[dialouge]"
    $ player.sex_vag(havenman, main_quest_05)
    show haven_presentass inside lookdown with dissolve
    pc "Ooooh fuck!"
    hav "Ahhh so nice and warm."
    "He grips onto my ass and aggressively trusts into me. He has no rhythm and it's almost like an animal having sex with me."
    "I guess it's not something he has done too often and so just goes at it as best he can."
    $ player.spank()
    "He no doubt won't last very long at this rate."
    hav "Fuck yes!"
    pc "Ooohh!"
    $ player.sex_cum_location_offer(
    difficulty=3, 
    cum_want="haven_sex_repeatable_sex_cum_want", 
    cum_notwant="haven_sex_repeatable_sex_cum_notwant", 
    cum_pullout="haven_sex_repeatable_sex_cum_pullout",
    cum_pullout_bj="haven_sex_repeatable_sex_cum_bj",  
    cum_pullout_poke="haven_sex_repeatable_sex_cum_poke",
    cum_bj="haven_sex_repeatable_sex_cum_bj",    
    
    block_anal_check=True
    )





label haven_sex_repeatable_sex_cum_want:
    pc "Ah fuck keep going! Keep fucking me!"
    hav "Ahhh!"
    hav "Yes!"
    $ player.sex_cum(havenman, "inside", main_quest_05)
    hav "Ahhhhhhhh!"
    pc "Oooh yes. I can feel it!"
    pc "Mmm..."
    hav "Fuck. That was nice."
    $ if_showing(
    "haven_onback", "poke down",
    "haven_presentass", "poke lookback",
    )
    pc "Like it did you?"
    hav "*Phew*"
    jump haven_sex_repeatable_end

label haven_sex_repeatable_sex_cum_notwant:
    pc "Ah fuck not inside!"
    hav "Ahhh!"
    hav "Yes!"
    $ player.sex_cum(havenman, "inside", main_quest_05)
    hav "Ahhhhhhhh!"
    pc "Fuck not inside. I don't need a baby!"
    hav "Fuck. That was nice."
    $ if_showing(
    "haven_onback", "poke down",
    "haven_presentass", "poke lookback",
    )
    pc "Pull out next time!"
    hav "*Phew*"
    jump haven_sex_repeatable_end

label haven_sex_repeatable_sex_cum_poke:
    $ if_showing(
    "haven_onback", "poke down worried",
    "haven_presentass", "poke lookback",
    )
    jump haven_sex_repeatable_sex_cum_notwant

label haven_sex_repeatable_sex_cum_pullout:
    pc "Ah fuck cum on my arse!"
    hav "Ahhh!"
    if renpy.showing("haven_cowgirl"):
        $ renpy.scene()
        show haven_gangbang penisup at right
        with dissolve
    else:
        $ if_showing(
        "haven_onback", "poke",
        "haven_presentass", "poke lookback",
        )
        $ if_showing(
        "haven_onback", "mast down",
        "haven_presentass", "mast",
        "haven_gangbang", "penisup",
        )
    hav "Yes!"
    $ player.sex_cum(havenman, "pullout", main_quest_05)
    hav "Ahhhhhhhh!"
    pc "Oooh yes. I can feel it!"
    pc "Mmm..."
    hav "Fuck. That was nice."
    show haven_presentass lookback with dissolve
    pc "Like it did you?"
    hav "*Phew*"
    jump haven_sex_repeatable_end

label haven_sex_repeatable_sex_cum_bj:
    $ renpy.scene()
    with dissolve
    pc "Use my mouth."
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        show haven_blow cum with dissolve
        show haven_blow 2h with dissolve
    elif randomnum == 2:
        show haven_blow cum with dissolve
        show haven_blow 1h with dissolve
    else:
        show haven_blow ballsuck with dissolve
    jump haven_sex_repeatable_sex_cum_bj_catcher

label haven_sex_repeatable_sex_cum_bj_catcher:
    hav "Haaaa."
    pc "*Hyuk*"
    hav "Ah yes here it comes!"
    show haven_blow cum with dissolve
    havenvik.name "Fuck yes!"
    $ player.sex_cum(havenman, "mouth", main_quest_05)
    hav "Ahhh yes yeeeeessss."
    hav "Take it in your mouth!"
    hav "Ahhhhhh..."
    show haven_blow wait ub with dissolve
    show haven_blow neutral with dissolve
    hav "Ah fuck. You swallowed it all down didn't you?"
    pc "What else am I going to do with it?"
    hav "Fuck!"
    hide haven_blow with dissolve
    jump haven_sex_repeatable_end

label haven_sex_repeatable_sex_cum_premature:
    hav "So sexy!"
    hav "Ah fuck."
    pc "Huh?"
    if renpy.showing("haven_onback"):
        $ player.sex_cum(havenman, "belly", main_quest_05)
    else:
        $ player.sex_cum(havenman, "ass", main_quest_05)
    hav "Ahh shit!"
    hav "Haaaaa!"
    pcm "Wow, I set him off a bit early."
    pcm "Well, good for me I suppose."
    if renpy.showing("haven_onback"):
        pc "Enjoy looking at me with my legs spread that much?"
    elif renpy.showing("haven_presentass"):
        pc "Enjoy my arse that much?"
    else:
        pc "Enjoy my slit that much?"
    hav "Ah fuck. Could say that."
    if renpy.showing("haven_onback"):
        pc "Mmm. You put it all over my belly."
    else:
        pc "Mmm. You put it all over my bum."
        $ player.spank()
    hav "Better in you. But fuck I couldn't hold it."
    pc "Mmmm. Next time."
    jump haven_sex_repeatable_end





label haven_sex_repeatable_end:
    $ renpy.scene()
    show havman at right1
    with dissolve
    hav "Fuck that was worth it."
    pc "Glad you liked it. I had better wash up now."
    hav "Ok."
    $ pc_dress()
    hide havman with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
