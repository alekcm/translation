label haven_bedroom_prompt:
    pcm "Hmmm..."
    $ player.eye = 2
    pcm "This place is like a graveyard right now."
    pcm "..."
    pcm "This would be a good time to scavenge around for anything useful."
    $ player.face_worried()
    pcm "If I get caught though I doubt an apology will settle the matter. I will probably be beaten up and kicked out on my arse for trying to rob these people."
    pcm "Better be careful."
    $ player.face_normal()
    $ add_to_list(loc_haven_bedroom.list, "bedroom_propt")
    jump travel

label haven_bedroom_bedbag1:
    "I search through one of the sleeping bags to see if there is anything worth taking."
    pcm "Ugh, this thing stinks. Hope I don't end up coming away with some fleas in my hair."
    $ haven_bedroom_search_caught()
    $ working(10)
    jump travel_arrival

label haven_bedroom_bedbag2:
    "I search through one of the sleeping bags to see if there is anything worth taking."
    pcm "Doesn't feel like there is anything worth taking in this bag."
    $ haven_bedroom_search_caught()
    $ working(10)
    jump travel_arrival

label haven_bedroom_bedbag3:
    "I search through one of the sleeping bags to see if there is anything worth taking."
    pcm "Ah, what's this? Some cigs and a lighter. I'll take those."
    $ inv.take(item_haven_lighter)
    $ inv.take(item_cigs)
    $ haven_bedroom_search_caught()
    $ working(10)
    jump travel_arrival

label haven_bedroom_bedbag4:
    "I search through one of the sleeping bags to see if there is anything worth taking."
    pc "Can't find anything of interest."
    $ haven_bedroom_search_caught()
    $ working(10)
    jump travel_arrival

label haven_bedroom_bedcorner:
    "I search around the bed in the corner to see if there is anything worth taking."
    pcm "Hmm, a jar of brew wedged between the mattress and wall. Think I will help myself."
    $ inv.take(item_brew)
    $ haven_bedroom_search_caught()
    $ working(10)
    jump travel_arrival

label haven_bedroom_beddoor:
    "I search around and in the bed to see if there is anything worth taking."
    pcm "Lot of empty cans on the wall here but nothing that will help me out."
    $ haven_bedroom_search_caught()
    $ working(10)
    jump travel_arrival

label haven_bedroom_bedfar:
    "I search around and in the bed to see if there is anything worth taking."
    pcm "Nothing at all. Whoever sleeps here clearly cleans up and takes everything with them."
    $ haven_bedroom_search_caught()
    $ working(10)
    jump travel_arrival

label haven_bedroom_bedright:
    jump haven_intel_14

label haven_bedroom_search_caught:
    show havman at right1 with dissolve
    hav "Someone with sticky fingers eh?"
    $ player.face_worried()
    pc "What? No, I was..."
    hav "Yeah right. Just looking for something? And you thought you would find it in someone else's belongings?"
    pc "What? No I..."
    hav "People don't much like thieves around here. Taking stuff from people who already have nothing."
    hav "If I let them know, what do you think will happen to you?"
    pc "I wasn't..."
    hav "Last person was woke up in the night by someone snipping off some fingers. Person before that had his ears removed."
    $ player.face_surprised()
    pc "..."
    hav "You are much more pretty than the last ones. I'm guessing people would love to have a share of you."
    $ player.face_worried()
    if player.iswhore or player.isslut:
        pc "And I am guessing you will keep your mouth shut if you get me to yourself?"
        hav "That's right. So let's go somewhere more private and you can convince me to keep quiet"
    if player.int >= 40:
        pc "And let me guess. You are willing to keep quiet for a price?"
        hav "That's right. So let's go somewhere more private and you can convince me to keep quiet"
    else:
        pc "What do you want?"
        hav "I want you to follow me somewhere more private to convince me not to tell anyone."
    $ player.eye = 2
    pc "And why would anyone believe you?"
    hav "People know me round here. You, on the other hand, are a new face. And no one will believe a new face."
    $ player.eye = 3
    pcm "Fuck!"
    $ player.eye = 1
    pc "And why should I believe you will keep quiet?"
    hav "Because I don't give a shit that you were nicking peoples stuff. If they were dumb enough to leave it laying around in this place then it's their own fault. I only care about what I can gain from it."
    pc "What if I offered you something else?"
    hav "Follow me."
    hide havman with dissolve
    pcm "*Sigh*"
    pcm "I knew if I got caught I would end up in trouble..."
    pcm "Getting kicked out of here isn't really an option though."
    if loc_cur == loc_haven_bedroom:
        $ walk(loc_haven_hallway_1f)
    else:
        $ walk(loc_haven_hallway_2f)
    $ player.face_worried()
    if player.iswhore or player.isslut:
        pcm "No doubt this pervert will want to fuck me to keep quiet."
    else:
        pcm "I wonder if there is something other than me that will keep him quiet."

    show havman at right1
    if loc_cur == loc_haven_hallway_1f:
        $ walk(loc_haven_room1)
    else:
        $ walk(loc_haven_room3)

    $ player.face_worried()

    hav "So...?"
    hav "What else you got to offer other than those bouncy tits?"
    if player.has_perk(perk_sucu, notif=True):
        pc "*Sigh* We both know what you want."
        jump haven_bedroom_search_caught_sex

    if inv.qty(item_brew) and inv.qty(item_cigs):
        pc "I have some booze and cigs."
    if inv.qty(item_cigs):
        pc "I have some cigs..."
        jump haven_bedroom_search_caught_brewoffer
    elif inv.qty(item_brew):
        pc "I have some brew..."
        jump haven_bedroom_search_caught_brewoffer
    else:
        $ player.eye = 6
        "..."
        $ player.eye = 1
        jump haven_bedroom_search_caught_sex

label haven_bedroom_search_caught_brewoffer:
    hav "Really?"
    hav "Ok, I am listening. Brew and cigs are always good for a deal. How much you got?"

    $ temp_var_1 = str(inv.qty(item_brew)) + " brew" + If(inv.qty(item_brew) > 1, "s", "")
    $ temp_var_2 = str(inv.qty(item_cigs)) + " pack" + If(inv.qty(item_cigs) > 1, "s of cigs", " of cigs")
    pc "I have [temp_var_1] and [temp_var_2]."

    if player.check_speech(5, notif=False):
        $ temp_var_3 = 4
    elif player.check_speech(4, notif=False):
        $ temp_var_3 = 5
    elif player.check_speech(3, notif=False):
        $ temp_var_3 = 6
    else:
        $ temp_var_3 = 8

    if inv.qty(item_brew) + inv.qty(item_cigs) >= temp_var_3:
        hav "Oh?"
        hav "Ok, that sounds good to me."
        hav "I'll take [temp_var_3] of either. Prefer cigs and I'll make up the rest in brew."
        hav "Sound good?"
        if player.check_sex_agree(4):
            menu:
                "Sounds good":
                    pc "Ok... Here."
                    $ haven_pay(temp_var_3)
                    hav "Lovely, it was a pleasure."
                    hide havman with dissolve
                    pcm "Arsehole!"
                    jump travel
                "Hmm, maybe I should use my body":

                    jump haven_bedroom_search_caught_sex
        else:
            pc "Ok... Here."
            $ haven_pay(temp_var_3)
            hav "Lovely, it was a pleasure."
            hide havman with dissolve
            pcm "Arsehole!"
            jump travel

label haven_bedroom_search_caught_sex:
    $ player.face_worried()
    hav "So body it is."
    if player.has_perk(perk_sucu, perk_slut, notif=True) or player.check_sex_agree(5):
        jump haven_bedroom_search_caught_sex_slut
    pc "..."
    hav "Let's see those lovely looking tits of yours."
    $ player.eye = 6
    pc "..."
    $ c.top = 0
    hav "Wow. Worth it!"
    $ player.eye = 1
    pc "For one of us."
    hav "For you as well, unless you don't want your fingers."
    pc "..."
    hav "Get on your knees."
    pc "What? Why?"
    hav "Why else would a man ask a whore to get on her knees."
    pc "..."
    show haven_blow wait ah with dissolve
    hav "..."
    hav "Well? I'm not gonna stand here all day beating it off. Put your mouth to use."
    show haven_blow neutral
    hav "Listen, quicker you get me off, quicker you get out of here. You are a whore so do a good job."
    pc "..."
    pcm "Cunt!"
    show haven_blow cum lookup with dissolve
    pause 0.5
    show haven_blow cum lookdown with dissolve
    pause 0.5
    show haven_blow 1h with dissolve
    $ player.sex_forced(havenblackmail, main_quest_05)
    $ player.sex_oral(havenblackmail, main_quest_05)
    hav "Ahh thats it!"
    hav "Love a good little whore on my cock."
    pcm "Shitty cunt!"
    if player.check_sex_agree(4):
        pcm "He's right about one thing though. Quicker I get him off, the quicker I get out of here."
        pcm "Plus, if I take too long he might end up wanting to fuck me instead."
        if player.vvirgin:
            pcm "Last thing I need is my first time being with this arsehole."
        show haven_blow ballsuck with dissolve
        hav "Ah yeah, you sexy little bitch. Suck those balls and get your babies ready."
        if player.has_perk(perk_preg_want):
            pcm "Babies?"
        hav "Haaa."
        if player.has_perk(perk_preg_want):
            pcm "What about babies?"
        hav "Mmmm yeah suck em."
        if player.has_perk(perk_preg_want):
            pcm "Does he want to give me a baby?"
        hav "Haaaaaa."
        if player.has_perk(perk_preg_want):
            pcm "Not gonna get a baby if he cums on my face..."
        if player.check_sex_agree(4) and not player.has_perk(perk_preg_want):
            jump haven_bedroom_search_caught_sex_blow
        elif player.has_perk(perk_preg_want) == True:
            jump haven_bedroom_search_caught_sex_pregwant
        else:
            jump haven_bedroom_search_caught_sex_cont
    else:

        hav "Ah yeah, you sexy little bitch. Suck those balls and get your babies ready."
        hav "Haaa."
        hav "Mmmm yeah suck em."
        hav "Haaaaaa."
        jump haven_bedroom_search_caught_sex_cont

label haven_bedroom_search_caught_sex_blow:
    show haven_blow 2h with dissolve
    pc "*Huk* *Huk* *Huk*"
    hav "Ah damn girl keep going!"
    hav "Bet you make a lot of money with that mouth of yours out there."
    hav "Ahh shit I am cumming!"
    show haven_blow cum with dissolve
    hav "Ah yeah open your mouth. I will put it all inside."
    $ player.sex_cum(havenblackmail, "mouth", main_quest_05)
    hav "Ahhh yes you dirty bitch!"
    hav "Ahhhhh."
    hav "Haaaa fuck. So nice."
    show haven_blow wait ub with dissolve
    show haven_blow neutral with dissolve
    pc "So, I got you off and now you will be keeping your mouth shut."
    hav "Sure thing sweetheart."
    hide haven_blow with dissolve
    pc "Don't call me sweetheart."
    hav "Whatever you say."

    $ pc_dress()
    pause 0.5
    hide havman
    $ walk(loc_haven_hallway_1f)
    pause 0.5
    $ walk(loc_haven_shower)
    pcm "Better wash that filthy shit's cum out my mouth."
    jump travel

label haven_bedroom_search_caught_sex_cont:
    hav "Come 'ere girl. You aren't putting any effort into this. Might as well do the work myself."
    pc "Whaaa?"
    hide haven_blow with dissolve
    show haven_bentover mast at right with dissolve
    pc "What are you doing?"
    hav "Bending you over, what does it look like?"
    pc "What? Wait?"
    hav "Wait for what? You give a shitty blowjob so let's see if your pussy does a better job."
    hav "How the fuck a whore like you makes money on the street I have no idea. Can't even get a guy off when getting kicked out of here is the alternative."
    pcm "Fuck. He's still holding me to that. Hoped he would give up after I blew him."
    if player.vvirgin:
        pcm "Am I really going to lose my virginity to some blackmailing fuck?"
    $ c.bottom = 0
    $ c.pants = 0
    pcm "He really is going to fuck me..."
    hav "Mmm, such a nice ass. Shame about the tramp stamp though. But I suppose you need to show everyone what an easy whore you are."
    pcm "..."
    show haven_bentover poke with dissolve
    if player.vvirgin:
        pcm "Fuck! What do I do? He is going to take it from me unless I can do something about it."
    else:
        pcm "He's poking me but I can't refuse him or else I will be kicked out of this place or worse... Shit."
    $ player.sex_vag(havenblackmail, main_quest_05)
    if player.virgin_pregcheck:

        show haven_bentover sad inside with dissolve
        $ player.add_mood(-10)
        $ player.face_tears()
    else:
        show haven_bentover inside with dissolve
    hav "Ahhhh so warm."
    pcm "..."
    hav "Haahaaaa."
    hav "Such a wet little slut. Don't try and say you aren't enjoying this!"
    if player.virgin_pregcheck:
        pcm "Fuck, why didn't I stop him from taking it from me?"
    else:
        pcm "*Sigh* The plug in my ass is giving me more pleasure than you, Just hurry up."
    hav "Haaa so nice."
    hav "Hahaaaaa."
    pcm "Come on, you have to be close."
    hav "Ahhhhh."
    show haven_bentover mast with dissolve
    $ player.sex_cum(havenblackmail, "pullout", main_quest_05)
    $ player.face_tears()
    hav "Ahhh yes!"
    pc "..."
    hav "Ahhhhh."
    show haven_bentover nomanfull with dissolve
    pc "That us done?"
    hav "Haaa. Girl, you know how to kill the mood."
    pc "There was no mood, Just you blackmailing me. Now we are done."
    hide haven_bentover with dissolve
    $ pc_dress()
    pause 0.5
    hide havman
    $ walk(loc_haven_hallway_1f)
    $ player.face_sad()
    pause 0.5
    $ walk(loc_haven_shower)
    $ player.face_sad()
    pcm "Better wash that filthy shit's cum off my arse."
    jump travel

label haven_bedroom_search_caught_sex_pregwant:
    show haven_blow wait with dissolve
    hav "Ah, why'd you stop?"
    pc "This is taking too long."
    hide haven_blow with dissolve
    $ c.bottom = 0
    $ c.pants = 0
    pause 0.5
    pc "Let's just get this over with. Don't wanna be here any longer than I need to be."
    pcm "And can't risk you blowing your load on my face."
    hav "Fine by me."
    show haven_bentover mast frown at right with dissolve
    hav "Fuck, I was focusing on your tits so much but this ass is something as well."
    pc "Yeah whatever, just do what you need to do."
    hav "Would fuck this ass of yours if it wasn't already full."
    pcm "Good job it is full then."
    show haven_bentover poke with dissolve
    pause 0.5
    show haven_bentover inside with dissolve
    $ player.sex_vag(havenblackmail, main_quest_05)
    hav "Ahhhh so warm."
    pcm "Idiot, of course it is."
    hav "Haahaaaa."
    pcm "..."
    hav "Such a wet little slut. Don't try and say you aren't enjoying this!"
    pc "Mmmm."
    pcm "Plug in my arse and the chance of getting pregnant is what is exciting me. You are the worst part of it all."
    pcm "Just give me what comes out of your cock."
    hav "Haaa so nice."
    hav "Hahaaaaa."
    pcm "Come on, you have to be close."
    hav "Ahhhhh."
    show haven_bentover mast with dissolve
    $ player.sex_cum(havenblackmail, "pullout", main_quest_05)
    hav "Ahhh yes!"
    pc "What the fuck!?"
    hav "Ahhhhh."
    hide haven_bentover with hpunch
    $ player.face_angry()
    pc "The fuck are you doing?!"
    hav "Ah what? I pulled out? What's the problem?"
    pc "Fucking idiot!"
    hav "What I don't understand?"
    pc "Idiot idiot idiot!"
    $ pc_dress()
    pause 0.5
    hide havman
    $ walk(loc_haven_hallway_1f)
    $ player.face_angry()
    pcm "Fuck!"
    $ walk(loc_haven_bedroom)
    $ player.face_angry()
    pause 0.5
    $ walk(loc_haven_bed)
    $ player.face_angry()
    pcm "Worthless shit. Couldn't even do something so simple. Useless blackmailing shit."
    pcm "..."
    $ player.face_normal()
    pc "*Sigh*"
    pcm "..."
    pcm "No idea why I came here. Have to go to the shower and wash this idiot off me."
    jump travel

label haven_bedroom_search_caught_sex_slut:
    $ player.face_normal()
    pc "Let's get this over with."
    $ c.top = 0
    hav "Huh? Bit eager no?"
    pc "Not really. But I don't have time to be messing about with you. So let's do this so I can get rid of you."
    hav "Ouch. Kinda ruining the mood here."
    pc "Oh?"
    pc "Should I be more seductive?"
    pc "Come here you sexy beast. I love being blackmailed and forced to fuck some dirty shit. It turns me on so much."
    pc "Pull down my pants and ravish me."
    $ c.bottom = 0
    $ c.pants = 0
    pc "Here you go, I did it for you. Fuck me like a whore you blackmailing shit!"
    hav "..."
    pc "Well, what are you waiting for. Get your cock out."
    pc "My arsehole is already taken so you only have 2 holes to choose from. You going to face fuck me or take my pussy?"
    hav "..."
    pc "Well, what are you waiting for? Fuck me!"
    show haven_grope grope hold neutral with dissolve
    hav "..."
    pc "Here, let me help."
    show haven_grope mast penis with dissolve
    pc "Hmm, only half chub? Thought anything would get a rapist shit like you off."
    hav "What? I am no rapist!"
    pc "No?"
    hav "Of course not!"
    pc "Blackmailing a girl to fuck you is rape. And people who rape are rapists. That makes you a rapist."
    hide haven_grope with hpunch
    hav "Fuck you! I am no rapist."
    hide havman with dissolve
    pc "..."
    pcm "He left..."
    if player.has_perk(perk_sucu, notif=True):
        pcm "Actually wanted him to fuck me. Maybe I bullied him too much."
        pcm "Oh well, his loss."
    else:
        pcm "Was prepared to actually fuck him to keep him quiet, but this turned out even better."
        pcm "Better get dressed and out of here in case he changes his mind."
    $ pc_dress_slow()
    pause 0.5
    $ walk(loc_haven_hallway_1f)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
