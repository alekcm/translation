label pub_waitress_work_clevage:
    $ pub_tips()
    $ rand_choice = WeightedChoice([
    ("pub_waitress_work_clevage1", 1),
    ("pub_waitress_work_clevage2", If (player.breasts >= 2, 1,0)),
    ("pub_waitress_work_clevage3", 1),
    ("pub_waitress_work_clevage4", If (player.mood <= 30, 2,0)),
    ("pub_waitress_work_clevage5", If (player.mood <= 30, 2,0)),
    ("pub_waitress_work_clevage6", 1),
    ("pub_waitress_work_clevage7", 1),
    ("pub_waitress_work_clevage8", 1),
    
    ])
    jump expression rand_choice

label pub_waitress_work_clevage1:
    show pub_walk_chest with dissolve
    lecher "Hey, hey, look at those."
    pervert "Huh, at what?"
    lecher "Over there, at the barmaid."
    if player.breasts >= 2:
        pervert "Damn! Look at them bounce."
    else:
        pervert "Ohh, showing off her little perkies like that."
    hide pub_walk_chest with dissolve
    jump pub_waitress_work_ogleend

label pub_waitress_work_clevage2:
    show pub_walk_chest with dissolve
    pervert "Christ, she has a pair on her!"
    lecher "Who?"
    pervert "Her, look."
    lecher "Damn..."
    hide pub_walk_chest with dissolve
    jump pub_waitress_work_ogleend

label pub_waitress_work_clevage3:
    show pub_walk_chest with dissolve
    "I smile at the guys I am walking past, but very few of them can manage to look me in the eye."
    hide pub_walk_chest with dissolve
    jump pub_waitress_work_ogleend

label pub_waitress_work_clevage4:
    show pub_walk_chest with dissolve
    $ dialouge = renpy.random.choice([
    "Hey baby. That's a nice dress, but it would look better on my bedroom floor.",
    "Hey sexy. That dress looks great on you... And so would I.",
    "Hey baby. If you’re feeling a bit down, I can feel you up.",
    "Damn girl, I think I could fall madly in bed with you.",
    "Hey baby, let's play carpenter. First we get hammered, then I'll nail you.",
    "Hey sexy, Is that a keg under your dress? Cos I want to tap that arse.",
    "Hey girl. I'm pretty much wasted, but this condom in my pocket doesn't need to be.",
    "Damn, are you a cowgirl? Cos I can see you riding me all night.",
    "Hey, what's a nice girl like you doing in a dirty mind like mine?",
    "Hey sexy, I just popped a boner pill so we have about half an hour to get back to my place.",
    ])
    lecher "[dialouge]"
    $ player.add_mood(3)
    pc "Pffft!"
    hide pub_walk_chest with dissolve
    jump pub_waitress_work_ogleend

label pub_waitress_work_clevage5:
    show pub_walk_chest with dissolve
    lecher "Hey darlin'."
    pc "Hey, you can at least try to look at my face when saying hello."
    $ player.add_mood(-2)
    $ randomnum = renpy.random.randint(1, 40)
    if randomnum == 1:
        lecher "Tell your boobs to stop looking into my eyes!"
    hide pub_walk_chest with dissolve
    jump pub_waitress_work_ogleend

label pub_waitress_work_clevage6:
    show pub_walk_chest with dissolve
    $ dialouge = renpy.random.choice([
    "Damn girl, you will hypnotise me with those things bouncing around.",
    "Christ girl, My face needs to be between those tits!",
    "Damn girl, how do you not put someone's eye out with those things?",
    "Damn girl, how much to get a hold of those things?",
    ])
    lecher "[dialouge]"
    $ player.add_mood(-2)
    pervert "*Sigh*"
    hide pub_walk_chest with dissolve
    jump pub_waitress_work_ogleend

label pub_waitress_work_clevage7:
    show pub_walk_chest with dissolve
    pervert "I love this place."
    lecher "Yup."
    pervert "Look at them bounce."
    lecher "Yup."
    pervert "What I wouldn't give to put my face between them."
    lecher "Yup."
    hide pub_walk_chest with dissolve
    jump pub_waitress_work_ogleend

label pub_waitress_work_clevage8:
    show pub_walk_chest with dissolve
    pcm "Can't wear a bra with this dress and these things are bouncing around like they have a life of their own."
    pcm "Looks like everyone else can notice this as well."
    $ player.add_desire_random(2)
    hide pub_walk_chest with dissolve
    jump pub_waitress_work_ogleend


label pub_waitress_work_ass:
    $ pub_tips()
    $ rand_choice = WeightedChoice([
    ("pub_waitress_work_ass1", 1),
    ("pub_waitress_work_ass2", 1),
    ("pub_waitress_work_ass3", If (player.confidence >= 50, 1,0)),
    ("pub_waitress_work_ass4", If (player.confidence >= 50 and player.desire >= 70, 1,0)),
    ("pub_waitress_work_ass5", If ((player.cum_locations["cum_vagin"] or player.cum_locations["cum_assin"]) and c.pants, 1,0)),
    ("pub_waitress_work_ass6", If (pub_waitress.pants == 0, 1,0)),
    
    
    ])
    jump expression rand_choice

label pub_waitress_work_ass1:
    show pub_walk_ass with dissolve
    lecher "This is why I love this place."
    pervert "Huh, why?"
    lecher "*Nods his head in my direction*"
    pervert "Damn! Think she knows she's showing her ass off to half the pub?"
    if pub_waitress.pants > 0:
        lecher "Of course she does. She probably loves it."
    else:
        lecher "Not even any pants on. She's just asking to be taken to the toilets and fucked."
    hide pub_walk_ass with dissolve
    jump pub_waitress_work_ogleend

label pub_waitress_work_ass2:
    show pub_walk_ass with dissolve
    pervert "Hey look."
    lecher "Wow. Wonder how much it costs to get her in the toilet for 20 minutes?"
    pervert "Pfft 20? Think you will last that long with that ass on you?"
    lecher "No chance."
    hide pub_walk_ass with dissolve
    jump pub_waitress_work_ogleend

label pub_waitress_work_ass3:
    show pub_walk_ass with dissolve
    pcm "I can see all these perverts watching me from the corner of their eye."
    pcm "It's no wonder the skirt on this thing is so short, easy money from these drunks."
    hide pub_walk_ass with dissolve
    jump pub_waitress_work_ogleend

label pub_waitress_work_ass4:
    show pub_walk_ass with dissolve
    $ player.add_desire_random(5)
    pcm "Heh, lets see if I can grab these perverts attention."
    "I walk while swaying my hips a lot more than normal."
    hide pub_walk_ass with dissolve
    jump pub_waitress_work_ogleend

label pub_waitress_work_ass5:
    show pub_walk_ass with dissolve
    pcm "Fuck, I shouldn't have let someone cum in me while I am working. I can feel it leaking."
    if pub_waitress.pants == 0:
        pcm "I hope people can't notice it leaking down my leg or something..."
    else:
        pcm "I hope people can't notice a wet patch in my pants."
    hide pub_walk_ass with dissolve
    jump pub_waitress_work_ogleend

label pub_waitress_work_ass6:
    show pub_walk_ass with dissolve
    if player.confidence < 30:
        $ player.face_worried()
    else:
        $ player.face_shy()
    pcm "This skirt is so short, I am pretty sure I am flashing my arse to these perverts..."
    if player.desire > 60:
        if player.desire > 80 and player.vsex > 10:
            pcm "Maybe they will notice how horny I am and want to solve my issue."
            pcm "Mmmm, fucking me in the backroom with their massi..."
            $ player.face_surprised()
            pcm "Ah... Shooo. Stop thinking like that."
            $ player.face_normal()
        else:
            pcm "They can probably tell how hot I am."
    pcm "Ah well, at least something can keep them happy in this shithole."
    hide pub_walk_ass with dissolve
    jump pub_waitress_work_ogleend
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
