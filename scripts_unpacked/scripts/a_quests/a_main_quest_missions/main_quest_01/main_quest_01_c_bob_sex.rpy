label main_quest_01_reporter_intro_bob_picker:
    $ add_to_list(main_quest_01.list, "bob_mission_accepted")
    pcm "Right, how should I play this?"
    if "paid" in main_quest_01.list and player.check_speech(3):
        pcm "Hold on..."
        pcm "I have the info and his money. I could just leave..."
        pcm "Hmmm..."
        if player.check_nowill(block_face=True):
            pcm "No, I could end up in worse trouble if I do a runner with his money."
        else:
            menu:
                "Leave with his money.":
                    $ add_to_list(main_quest_01.list, "stole_money")
                    pcm "Right, I should try and get lost in the crowd..."
                    pcm "Hopefully he isn't paying too much attention."
                    pcm "Aaaaand..."
                    pcm "Go!"
                    jump main_quest_01_reporter_intimidate_branch_end
                "No, I told him I would do the job.":
                    $ NullAction()
    if "work" in tab_top:
        jump main_quest_01_reporter_intro_bob_waitress
    if pub_waitress.sold:
        pcm "So, I could dress as a waitress and use that as a reason to approach him."
        pcm "Or just go up normally and pretend I know him from the hospital."
        menu:
            "Dress as a waitress":
                pcm "Probably best to dress up."
                $ walk(loc_pub_changingroom)
                pause 1
                $ pc_strip()
                pause 0.5
                $ pub_waitress.work_dress()
                pause 0.5
                $ walk(loc_pub)
                jump main_quest_01_reporter_intro_bob_waitress
            "Go up to him as I am":
                jump main_quest_01_reporter_intro_bob_normal
    else:
        jump main_quest_01_reporter_intro_bob_normal






label main_quest_01_reporter_intro_bob_waitress:
    $ add_to_list(main_quest_01.list, "bobsex_waitress")
    $ npc_race_picker(bob)
    pcm "Ok, grab some drinks..."
    $ player.left_hand = "beer"
    $ player.right_hand = "beer"
    pause 0.5
    show pub_serve_clevage with dissolve
    pc "Here you go sweetie."
    bob.name "Thanks. Err, I only ordered one."
    hide pub_serve_clevage
    show pub_serve_talking
    with dissolve
    $ player.left_hand = ""
    $ player.right_hand = ""
    $ player.add_perk(perk_drinking_beer_2)
    pc "Other one is for me. Could do with a break."
    bob.name "Oh?"
    bob.name "Well, you won't find better company."
    pc "That right?"
    bob.name "Why not take a seat?"
    pcm "Wow, he is being forward. Making this easy for me."
    pc "Don't mind if I do. Not many seats around here though..."
    hide pub_serve_talking
    show pub_serve_lap talk
    with dissolve
    pc "Hope you don't mind."
    bob.name "Not at all. I love how forward you barmaids are."
    pc "Oh? Not your first time?"
    bob.name "Err..."
    pc "I don't mind. Plenty of us girls round here."
    bob.name "I have one girl... But she is a bit pricey. So have to keep myself in check."
    pc "Oh?"
    bob.name "Yeah, doubt I can afford you either."
    pc "It's fine. I'm just looking for a break and some beer before heading off home for the night."
    bob.name "Free beer I can offer for a cutie like you."
    pc "I'll hold you to that."
    $ player.drink_current()
    pc "So see you around here a lot. What's your story?"
    bob.name "Who says I have a story?"
    pc "Everyone does. Might not be the most exciting story, but there is always one."
    bob.name "Probably the same one as most people round here. No better place to be than drowning in a glass."
    pc "Mmm, can relate to that. Wouldn't mind drowning in a glass myself. But got to earn a living."
    bob.name "Mmm, don't we all. Fortunately my work is in the day time."
    pc "Oh? The hospital right?"
    bob.name "Yeah, boring work. Spend my day there looking forward to coming here. Then go home when you close and pass out. Do it all again the next day."
    pc "Nice routine."
    $ player.drink_current()
    pcm "And no mention of a wife. But suppose that's not something you tell a girl sitting on your lap."
    $ player.grope(hands=False)

    pcm "Oh? Getting touchy now?"
    pc "And where do you think that hand is going?"
    bob.name "Want to drink up my beer as well?"
    pc "Err, sure."
    pcm "Shameless distraction."
    $ player.add_perk(perk_drinking_beer_2)
    pc "Who can turn down free beer."
    bob.name "Mmm, keep me company and I'll keep your glass full."
    pc "Oh, that a promise? Could do with all the free beer after the day I've had."
    bob.name "Oh? Wanna tell me about it?"
    pc "Not really. The same as usual. Life and all that."
    pc "Could do with something nice and relaxing."
    pcm "He is clearly a perv, I'm going to push for it."
    $ player.drink_current()
    pc "It's been a loooong and haaaard day."
    bob.name "I bet. And relaxing in my arms will fix everything."
    pc "It's a start at least."
    bob.name "And does the rest involve something here?"
    $ player.grope(hands=False)
    pc "Aie!"
    pc "Careful. Touching me there so suddenly."
    if not c.pants:
        $ add_to_list(main_quest_01.list, "bobsex_waitress_nopants")
        bob.name "Didn't think a bar girl would be working round here with no knickers on. What's your deal?"
        pc "Oh, you noticed?"
        if player.check_horny(extreme=True):
            bob.name "Hard not to, you are soaking wet."
        else:
            bob.name "Hard not to while I am touching you there."
        pc "Heh."
    else:
        bob.name "Not often a bar girl comes up and just sits on your lap. So what's your deal?"

    if not "paid" in main_quest_01.list:
        pcm "This is probably more than enough for his steamy shots. Unless I want to deal with his cock, I should probably end it here."
        menu:
            "End it":
                $ add_to_list(main_quest_01.list, "bobsex_waitress_endearly")
                pc "I was just looking to relax before heading home and thought I would have a bit of fun."
                pc "But I should go before I let things go any further."
                bob.name "Nothing wrong with further."
                if not player.pregnancy >= 2:
                    pc "For you sure. It's me who will end up carrying what you leave behind in my belly."
                else:
                    pc "Maybe another time darling."
                pc "I had fun. See you round."
                $ player.drink_finish()
                hide pub_serve_lap with dissolve
                "I disentangle myself from his lap while he is mercilessly groping me while I try to get up."
                jump main_quest_01_reporter_intro_bob_waitress_redress
            "Carry on":
                $ NullAction()
    else:
        pcm "I Should push things further so I'm not sitting here all day."
    $ player.drink_current()
    if not c.pants:
        jump main_quest_01_reporter_intro_bob_waitress_lapsex_start
    else:

        jump main_quest_01_reporter_intro_bob_waitress_isolate_blow_start





label main_quest_01_reporter_intro_bob_waitress_isolate_blow_start:
    $ add_to_list(main_quest_01.list, "bobsex_waitress_pants")
    pc "Want to know the truth?"
    $ player.beer()
    bob.name "Of course."
    show pub_serve_lap hump with dissolve
    if player.isbroken:
        pc "Serving men is all I want to do."
        bob.name "Oh? Well... Okay then."
    elif player.isslut:
        pc "I just love to fuck. You are the lucky guy I picked out for tonight."
        bob.name "Oh you dirty slut!"
    elif player.has_perk(perk_preg_want):
        pc "I want a baby. And I decided it's your turn to try and put one in me."
        bob.name "Fuck. You dirty girl!"
    elif player.desire > 90:
        pc "I am soaking wet and need someone to give me what I want."
        bob.name "Oh you dirty slut!"
    elif player.mood < 20:
        pc "I feel miserable and thought you inside me could cheer me up."
        bob.name "Well, I can sure try."
    else:
        pc "I just want some fun. Something inside me kind of fun."
        bob.name "Fuck. You dirty girl!"
    pc "You up for it?"
    bob.name "Err, of course."
    pc "Let's go somewhere more private then."
    $ renpy.scene()
    show bob at right1
    with dissolve
    "I jump off of [bob.name]'s lap and take him by the hand, half dragging him to the toilets."
    $ walk(loc_pub_toilet_girls)
    with dissolve
    pc "No one will disturb us in here."
    bob.name "No? Sure?"
    pc "Yeah, only girls round here are the barmaids and the odd whore. So not many people coming in here."
    "I fumble with [bob.name]'s trousers and try to get them undone. Finally I manage it and pull them down, letting his already semi erect cock spring free."
    hide bob
    show sb_blowjob face happy 1h
    with dissolve
    pc "Ooh, what do we have here? Not wasting any time are you?"
    $ having_sex(5)
    $ player.sex_oral(bob, main_quest_01)
    show sb_blowjob suck down with dissolve
    bob.name "Fuck! Nor are you."
    pc "Mmmm."
    "I make sure to keep [bob.name]'s attention on me knowing that [simon.name] probably has his phone poked over the stall and is taking pictures."
    "But mostly I pay attention to [bob.name]'s cock. Despite this being a job, there is no harm in me having a little fun with it. [bob.name] just relaxes against the stall wall and lets me do all the work."
    "It's fine by me, so I use my hands to wank him off while licking his helmet that's in my mouth."
    show sb_blowjob up
    bob.name "Ah fuck. Didn't think I would have you doing this when you came to say hello."
    show sb_blowjob poke laugh up with dissolve
    pc "Bet you hoped I would be though. Doubt this is the first barmaid you have had sucking you off in the toilet."
    bob.name "Hah! No, but not sure I've had one quite as nice as you."
    if player.pregnancy >= 2:
        bob.name "And not a pregnant one at that."
    pc "Bet you say that to all the bargirls."
    show sb_blowjob suck down 2h with dissolve
    bob.name "Ahhh it's nice."
    pc "Mmmm."
    if player.check_sex_agree(4):
        pcm "Might be nicer though if he also helped me out. Wonder if I should offer..."
        if player.check_sex_agree_choice(0, "Interested in going a little further?", "..."):
            show sb_blowjob poke happy up with dissolve
            bob.name "I won't say no to that."
            pc "Ha, okay then."
            jump main_quest_01_reporter_intro_bob_waitress_isolate_sex

    "I know [bob.name] is enjoying so I keep sucking on his cock."
    show sb_blowjob tounge poke up with dissolve
    pc "Bet you didn't think you would be getting this kind of bar service when you came in here."
    bob.name "Can't say I haven't fantasised about having a young barmaid like you sucking my cock, never thought it would happen though."
    pc "Mmmm I bet."
    show sb_blowjob suck down 2h with dissolve
    "I keep back at it, knowing he must be fairly close considering how he is grunting. The pre cum trickling in my mouth confirms this."
    show sb_blowjob laugh poke up with dissolve
    pc "Can feel you're close. You going to give me something?"
    bob.name "Ah, keep going and I will."
    show sb_blowjob suck down 2h with dissolve
    pc "Mmmmm."
    bob.name "Ahhhhhh."
    bob.name "Liiiike... Thaaaat..."
    $ player.sex_cum(bob, "mouth", main_quest_01)
    bob.name "Ahhhhhhhh!"
    pc "Mmmmmmffff."
    bob.name "Haaaaa... Haaaaa..."
    show sb_blowjob ub face up with dissolve
    show sb_blowjob neutral with dissolve
    show sb_blowjob swallow with dissolve
    pc "Ahhhhh."
    bob.name "Fuck. Swallowed it all?"
    show sb_blowjob laugh
    pc "Yup!"
    bob.name "Phew."
    show sb_blowjob neutral
    jump main_quest_01_reporter_intro_bob_normal_sex_wrapup

label main_quest_01_reporter_intro_bob_waitress_isolate_sex:
    $ having_sex(5)
    hide sb_blowjob
    show pub_undress
    with dissolve
    show pub_undress pants_off with dissolve
    $ c.pants = 0
    "I get up off my knees and slide my knickers down to the floor giving [bob.name] a pretty good show."
    show pub_undress stand with dissolve
    hide pub_undress
    show sb_againstwall2 happy
    with dissolve
    pc "You like what you see?"

    bob.name "Mmm."
    pc "Then come here."
    bob.name "Right!"
    show sb_againstwall2 pokevaghand with dissolve
    show sb_againstwall2 worried wink pokevag with dissolve
    "[bob.name] wastes little time and presses me against the wall, cock ready for me."
    bob.name "Mmm, ready?"
    $ player.sex_location_offer()
    if player.want_sexlocation == 1:
        jump main_quest_01_reporter_intro_bob_waitress_isolate_sex_vag
    else:
        jump main_quest_01_reporter_intro_bob_waitress_isolate_sex_anal

label main_quest_01_reporter_intro_bob_waitress_isolate_sex_vag:
    $ having_sex(5)
    pc "Yes, fuck me!"
    $ player.sex_vag(bob, main_quest_01)
    show sb_againstwall2 ag worried insidevag with dissolve
    pc "Oh fuck yes [bob.name]. Give it to me!"
    pc "Huuuuuuu..."
    "[bob.name] doesn't waste much time and goes at it at a pretty good pace right from the start. Not that I am complaining."
    show sb_againstwall2 closed straight with dissolve
    "I close my eyes and focus only on the cock penetrating me and making me feel good. [bob.name] has his hands all over my body but my mind pays attention to only one thing."
    "Before I know it, [bob.name] is really going to town on me. He is gripping at my hips and thrusting as deep as he can into me."
    "I am loving every moment of it. [bob.name] has been a suprise all night. First hanging and talking with him and now bent over and taking his cock in me. Both have been a lot more pleasurable than I would have ever expected."
    show sb_againstwall2 wink ag with dissolve
    pc "Fuck it feels to gooooood..."
    "At this point I am rocking my hips to meet his thrusts, so each of his thrusts is hitting me hard with a loud *slap* reverberating in the alley."
    pc "Fuck fuck keep going!"
    show sb_againstwall2 closed with dissolve
    bob.name "Ahhh yeeessss..."
    pc "Keeeep... Nnnnggg..."
    pc "YES!"

    bob.name "Ahhhhh!!! Gonna... Cuuuummm..."
    $ player.sex_cum_location_offer(
    difficulty=1, choice_inside="Keep going!", choice_pullout="Not inside.",  
    cum_want="main_quest_01_reporter_intro_bob_normal_sex_cum_want", 
    cum_notwant="main_quest_01_reporter_intro_bob_normal_sex_cum_not_want", 
    cum_pullout="main_quest_01_reporter_intro_bob_normal_sex_cum_pullout",
    cum_pullout_anal="main_quest_01_reporter_intro_bob_normal_sex_cum_pullout_anal", 
    cum_pullout_bj="main_quest_01_reporter_intro_bob_normal_sex_cum_pullout_blowjob",  
    cum_pullout_poke="main_quest_01_reporter_intro_bob_normal_sex_cum_pullout_poke",
    cum_bj="main_quest_01_reporter_intro_bob_normal_sex_cum_pullout_blowjob",    
    )

label main_quest_01_reporter_intro_bob_waitress_isolate_sex_anal:
    $ having_sex(5)
    pc "Wait, I don't want to end up pregnant so fuck me in the arse."
    bob.name "Fuck yes!"
    pc "Oh? Guys are not normally that eager."
    show sb_againstwall2 pokevaghand with dissolve
    show sb_againstwall2 pokeasshand with dissolve
    show sb_againstwall2 pokeass with dissolve
    bob.name "First time for me like this. Not many girls wanted to do it like this before."
    pc "Ah, all different now. Getting ass fucked is the only way to have sex and not worry about a baby."
    pc "You not tried it before with the other bar girls?"
    bob.name "Sometimes..."
    "The entire time we have been talking, he has been putting more pressure on my arsehole with his cock, and finally it starts to slip inside me."
    $ player.sex_anal(bob, main_quest_01)
    if player.asex < 5:
        show sb_againstwall2 wink shock worried insideass with dissolve
        bob.name "Ah fuck it's so tight!"
        pc "Nnnng fuck fuck!"
        bob.name "Ah, should I take it slow?"
        pc "Yes! Slow!"
        show sb_againstwall2 neutral with dissolve
        bob.name "Thought you might be used to this."
        pc "No, not yet. But I need to unless I want to risk a baby."
    else:
        show sb_againstwall2 insideass happy with dissolve
        bob.name "Ah fuck yes!"
    pc "Huuuuuu..."
    "[bob.name] takes it fairly slow at first, gently sliding his cock in and out of my ass while gripping onto my hips."
    if player.asex < 5:
        "As he continues to fuck me, he slowly picks up the pace. I start to get used to his cock in my arse so I relax and start to enjoy the feeling of him in me."
    else:
        "As he continues to fuck me, he slowly picks up the pace. I just relax and enjoy the feeling he is giving me."
    show sb_againstwall2 vhappy closed worried with dissolve
    pc "Mmmmm..."
    "I close my eyes and focus only on the cock penetrating me and making me feel good. [bob.name] has his hands all over my body but my mind pays attention to only one thing."
    "Before I know it, [bob.name] is really going to town on my arse. He is gripping at my hips and thrusting as deep as he can into me."
    show sb_againstwall2 wink ag with dissolve
    pc "Fuck it feels too gooooood..."
    "At this point I am rocking my hips to meet his thrusts, so each of his thrusts is hitting me hard with a loud *slap* reverberating in the alley."
    pc "Fuck fuck keep going!"
    show sb_againstwall2 closed with dissolve
    bob.name "Ahhh yeeessss..."
    pc "Keeeep... Nnnnggg..."
    pc "YES!"
    $ player.sex_cum(bob, "anal", main_quest_01)
    pc "Yes yes yes!"
    bob.name "Ahhhhhhhhhhh!!!"
    show sb_againstwall2 wink with dissolve
    bob.name "Haaaaaaa..."
    jump main_quest_01_reporter_intro_bob_normal_sex_wrapup




label main_quest_01_reporter_intro_bob_waitress_lapsex_start:
    pc "I just..."
    bob.name "Why not get more comfortable?"
    pc "Huh?"
    show pub_serve_lap hump with dissolve
    "He shifts around under me and repositions my legs so I am pretty much straddling him."
    pc "Hey."
    bob.name "Here, drink up."
    $ player.drink_finish()
    pc "Ugh. Being a bit too forward aren't you?"
    bob.name "Says the barmaid with no underwear on. Let's not beat around the bush and get to what we both want."
    pcm "Well, I guess he's right. I need this to continue to get those photos."
    pc "Okay."
    show pub_serve_lap rub with dissolve
    pc "Oh? Is that what I think it is?"
    bob.name "It is."
    pc "In public?"
    bob.name "Why not? Doubt you are going to get a room with me."
    pc "Well no."
    bob.name "So here is a good a place as any."
    pc "I guess."
    pc "Let's see what you have then."
    $ player.sex_hand(bob, main_quest_01)
    show pub_serve_lap talk penis with dissolve
    show pub_serve_lap mast with dissolve
    pc "Mmm, not bad."
    bob.name "Glad you like it."
    bob.name "But let's not have it out in the open too long eh? Someone might see."
    if player.check_int(4):
        pcm "Hold on, he's right. Someone might see."
        pcm "Means [simon.name] can see it and get photos."
        pcm "So this is my end of the bargain held up. No need to carry on."
        if player.check_sex_agree_choice(4, "...", "Sorry, got to go!"):
            $ NullAction()
        else:
            hide pub_serve_lap with dissolve
            bob.name "Hey wai..."
            "I quickly rush off leaving him behind on the chair and make my way to the back room."
            jump main_quest_01_reporter_intro_bob_waitress_redress


    pc "Hmm, wonder where it could go without being seen."
    bob.name "I can think of a few places."
    pc "A few?"
    bob.name "Well... One... Two places."
    $ player.sex_location_offer()
    if player.want_sexlocation == 1:
        jump main_quest_01_reporter_intro_bob_waitress_lapsex_vag
    else:
        jump main_quest_01_reporter_intro_bob_waitress_lapsex_anal

label main_quest_01_reporter_intro_bob_waitress_lapsex_vag:
    pc "Ah, well let's stick with the first one."
    show pub_serve_lap prep with dissolve
    "I sit up slightly until I am able to position it under me. Once it is in place I slowly slide down onto it."
    show pub_serve_lap hump with dissolve
    $ player.sex_vag(bob, main_quest_01)
    pc "Haaaaaa fuuuuuu..."
    bob.name "Mmmm dirty girl."
    pc "Mmmmm. I am."
    pc "But don't draw attention or I might end up sacked."
    pcm "Yeah right."
    bob.name "Ok."
    "I quietly rock back and forth while straddling [bob.name]. It is by no means an intense fucking, but its relaxing nature is quite fun anyway."
    "I am helped by his hands on my waist that help me rock with him inside me, sometimes sitting up a bit to pull him out a bit then letting him slide back inside."
    "Our rocking and quiet moans are drawing some attention from those sitting nearby, but other than some curious looks, most people don't pay it much mind."
    "Not unusual for the bargirls here to give extra service after all. As long as the whole pub is not made aware of what we are doing, I don't mind."
    "My mind is brought back to the real world by his fingers digging much more deeply into me..."
    pcm "Fuuu, I can feel he's close..."

    $ player.sex_cum_location_offer(
    difficulty=3, 
    cum_want="main_quest_01_reporter_intro_bob_waitress_lapsex_vag_cum_want", 
    cum_notwant="main_quest_01_reporter_intro_bob_waitress_lapsex_vag_cum_not_want", 
    cum_pullout="main_quest_01_reporter_intro_bob_waitress_lapsex_vag_cum_pullout",

    cum_bj="main_quest_01_reporter_intro_bob_waitress_lapsex_vag_cum_pullout",    
    )

label main_quest_01_reporter_intro_bob_waitress_lapsex_vag_cum_want:
    "I make no attempt to get him to pull out and just keep rocking on his lap until I can feel him throbbing..."
    $ player.sex_cum(bob, "inside", main_quest_01)
    bob.name "Unnnggggg..."
    pc "Haaaaa fuuuuu..."
    pc "*Huff*"
    pcm "Haaa fuck, that was nice!"
    pc "*Phew*"
    pcm "Well, I've had my fun and that's the job done."
    pc "Thanks [bob.name]. It was fun."
    bob.name "It sure was. I look forwa..."
    hide pub_serve_lap with dissolve
    "Without letting him finish, I slowly stand up, feeling his cock slip out of my vagina, fix my dress and walk away without another word."
    jump main_quest_01_reporter_intro_bob_waitress_redress

label main_quest_01_reporter_intro_bob_waitress_lapsex_vag_cum_not_want:
    show pub_serve_lap prep with dissolve
    "I start to lift myself off of [bob.name]'s lap, but his hands pull me back onto him..."
    show pub_serve_lap hump with vpunch
    $ player.sex_cum(bob, "inside", main_quest_01)
    pcm "Fuck! I can feel him throbbing inside..."
    bob.name "Unnnggggg..."
    pc "Haaaaa fuuuuu..."
    pc "*Huff*"
    pcm "Haaa fuck, that was nice!"
    pc "*Phew*"
    pc "Idiot, I told you not inside."
    bob.name "Ahh, sorry, it just felt so..."
    show pub_serve_lap prep with dissolve
    hide pub_serve_lap with dissolve
    "Without letting him finish, I slowly stand up, feeling his cock slip out of me, fix my dress and walk away without another word."
    jump main_quest_01_reporter_intro_bob_waitress_redress

label main_quest_01_reporter_intro_bob_waitress_lapsex_vag_cum_pullout:
    show pub_serve_lap prep with dissolve
    show pub_serve_lap talk penis with dissolve
    show pub_serve_lap talk mast with dissolve
    "I lift myself off his lap and let his cock slip out of me. I then press wrap my fingers round his cock and start wanking him off."
    $ player.sex_cum(bob, "pullout", main_quest_01)
    bob.name "Unnnggggg..."
    pc "Haaaaa fuuuuu..."
    pc "*Huff*"
    pcm "Haaa fuck, that was nice!"
    pc "*Phew*"
    pcm "Well, I've had my fun and that's the job done."
    pc "Thanks [bob.name]. It was fun."
    bob.name "It sure was. I look forwa..."
    hide pub_serve_lap with dissolve
    "Without letting him finish, I slowly stand up, fix my dress and walk away without another word."
    jump main_quest_01_reporter_intro_bob_waitress_redress

label main_quest_01_reporter_intro_bob_waitress_lapsex_anal:
    pc "I would prefer the second place."
    bob.name "What? Really?"
    pc "Why so shocked?"
    bob.name "I must be getting old. Girls never liked that back in the day."
    if player.vvirgin:
        pc "Well, I don't want to have sex yet but still have some fun."
        bob.name "Err... What?"
        pc "Never mind."
    elif player.has_perk(perk_preg_notwant):
        pc "Condoms existed back in the day. These days birth control is taking it in the bum."
    elif player.cycle_conditions["stage"] == "ovulate":
        pc "Bad time of the month to be having it anywhere else."
    elif player.asex > player.vsex and player.asex > 10:
        pc "Mmm, what can I say. I like it there and usually do it this way."
    else:
        pc "Not the same these days. Most people now will have it like this to avoid something growing inside them."
    bob.name "Ah well, I'm not complaining. Something new is always nice as I get older."
    pc "New? Your first time?"
    bob.name "Well, yeah."
    pc "Oooh? Maybe I should be charging you."
    bob.name "I'd better hurry then before you try."
    show pub_serve_lap prep with dissolve
    "[bob.name] lifts me up slightly and with his cock in my hand, I position it right against my arsehole. I then very slowly ease myself down on top of it."
    show pub_serve_lap hump with dissolve
    $ player.sex_anal(bob, main_quest_01)
    pc "Haaaaaa fuuuuuu..."
    bob.name "Mmmm dirty girl."
    pc "Mmmmm. I am."
    pc "But don't draw attention or I might end up sacked."
    pcm "Yeah right."
    bob.name "Ok."
    "I quietly rock back and forth while straddling [bob.name]. It is by no means an intense fucking, but its relaxing nature is quite fun anyway."
    "I am helped by his hands on my waist that help me rock with him inside me, sometimes sitting up a bit to pull him out a bit then letting him slide back inside."
    "Our rocking and quiet moans are drawing some attention from those sitting nearby, but other than some curious looks, most people don't pay it much mind."
    "Not unusual for the bargirls here to give extra service after all. As long as the whole pub is not made aware of what we are doing, I don't mind."
    "My mind is brought back to the real world by his fingers digging much more deeply into me..."
    pcm "Fuuu, I can feel he's close..."
    "With not much else I can do, I press my arse against him so his cock is deep inside me and..."
    $ player.sex_cum(bob, "anal", main_quest_01)
    bob.name "Unnnggggg..."
    pc "Haaaaa fuuuuu..."
    pc "*Huff*"
    pcm "Haaa fuck, that was nice!"
    pc "*Phew*"
    pcm "Well, I've had my fun and that's the job done."
    pc "Thanks [bob.name]. It was fun."
    bob.name "It sure was. I look forwa..."
    hide pub_serve_lap with dissolve
    "Without letting him finish, I slowly stand up, feeling his cock slip out of my arse, fix my dress and walk away without another word."
    jump main_quest_01_reporter_intro_bob_waitress_redress

label main_quest_01_reporter_intro_bob_waitress_redress:
    $ walk(loc_pub_changingroom)
    with dissolve
    pause 0.2
    $ pc_strip()
    if player.cum_locations["cum_vagin"] or player.cum_locations["cum_assin"]:
        $ player.face_worried()
        pcm "Dammit, it's all leaking out of me."
    elif player.cum_locations["cum_vagout"] or player.cum_locations["cum_assout"]:
        $ player.face_worried()
        pcm "Dammit, I am all wet down there thanks to his cum."
    else:
        pause 0.5
    $ pc_dress_slow(pub_waitress.clothes)
    pcm "Right, go and see [simon.name] I guess. Hope [bob.name] doesn't recognise me out of my waitress gear."
    jump main_quest_01_reporter_intro_bob_postwaitresssex_wrapup





label main_quest_01_reporter_intro_bob_normal:
    $ add_to_list(main_quest_01.list, "bobsex_normal")
    if c.slutty:
        pcm "I am dressed pretty slutty so if I just go and chat with him he will think I am a whore looking for a customer."
    elif player.allure > 100:
        pcm "Considering how I am dressed, me walking up and just chatting to him is going to make him think I am a whore looking for customers."
    else:
        "Right, how am I going to speak to him without looking like a whore after a customer."
    pcm "Well, he does work at the hospital so I could pretend I work there as well and have seen him around."
    pcm "It's about as good an idea as I can think of."
    pcm "Get a beer first though. Pretend I am like him and just blowing off steam after a long day."
    "I walk over to the bar and pay for one of the beers that have already been poured."
    $ player.add_money(-5)
    $ player.left_hand = "beer"
    pcm "Right then..."
    show bob at right1 with dissolve
    pc "Oh, [bob.name] right?"
    bob.name "Sorry love. I ain't flush right now so better someone else."
    pcm "Yup, thinks I am a whore."
    pc "If that's what I was up to, I wouldn't be working my shitty job in the hospital. I've seen you around."
    bob.name "Oh?"
    pc "You don't mind if I sit with you? Girl on her own in a place like this draws attention and you are the only friendly face I've seen in here."
    bob.name "Sure, no problem."
    pc "Don't think we chatted before. I'm [name]."
    pcm "Fuck, should have gave him a fake name."
    bob.name "Nice to meet you. Don't remember seeing you around though. You a nurse?"
    pcm "Hmm, if I say yes then I might be expected to know medical stuff. I don't actually know what [bob.name]'s job actually is so no idea if he will catch me out."
    pc "No, I wish. I run errands basically."
    bob.name "Oh? What department do you work for?"
    pcm "Fuck."
    pc "I don't work for any."
    bob.name "Hmmm?"
    pc "\"Running errands\" is just a nice way to say I do all the shit jobs no one else wants to do."
    bob.name "Ah you're a dogsbody?"
    pcm "Yes!"
    pc "I prefer errand girl."
    bob.name "Sure sure. S'what you doing here?"
    pc "Same as the rest. Getting drunk before going home and having another shitty day tomorrow."
    bob.name "I can drink to that."
    $ player.beer()
    "I sit and chat with [bob.name], first about work stuff where he mostly tells me all about his boring job. He just deals with paperwork and isn't a medical expert so doesn't have any authority."
    $ relax(30)
    $ player.beer()
    if c.slutty:
        "Turns out he is actually a pretty okay fella. Despite me sitting here dressed in slutwear, he remains respectful and never makes a comment or pass at me."
    elif player.allure > 100:
        "Turns out he is actually a pretty okay fella. Despite me sitting here dressed as I am, he remains respectful and never makes a comment or pass at me."
    else:
        "Turns out he is actually a pretty okay fella. Despite me being one of the only girls in the place, he remains respectful and never makes pass at me."
    "Ordinarily, that would be a good thing. But I am here to try and get him in a compromising position so [simon.name] can get his photos."
    $ relax(30)
    $ player.beer()
    "I actually find myself enjoying chatting and having beers with him enough that I almost forget what I am here for. But I can't really be hanging out here all night."
    $ relax(30)
    $ player.face_happy()
    pc "...his hair ever grow back?"
    bob.name "No, bald as an eagle the rest of his life!"
    pc "Wow. Must have been devastating."
    $ player.beer()
    $ player.hands_reset()
    bob.name "Another beer?"
    pc "Think I am going to call it for the night [bob.name]."
    bob.name "Shame."
    pcm "Still need to get this job done."
    pc "Had a surprisingly nice time tonight."
    bob.name "\"Surprisingly\"? Thanks."
    pc "Well, coming to a place like this, I didn't have high expectations."
    bob.name "Mmmm."
    pcm "Now or never."
    pc "Hey [bob.name]."
    bob.name "Yeah?"
    pc "How about I thank you for tonight?"
    bob.name "Huh? You just did, I think."
    pc "I mean thank you thank you."
    pc "Properly."
    pc "Alone."
    bob.name "Ooooohhh..."
    bob.name "Sorry. You're a sweet lass. But I don't wanna be taking advantage of a drunk youg'un."
    pcm "Wow, what the fuck? He the only guy with some morals left in this place?"
    pc "Yeah, stop thinking [bob.name]."
    bob.name "Err..."
    pc "Shut up and follow me."
    "I take [bob.name] by the hand and lead him to the back exit of the pub and head out into the alleyway."
    $ walk(loc_alley)
    with dissolve
    if weather_var >= 3:
        pc "Fucking weather. Toilets then."
        pc "Come on."
        $ walk(loc_pub)
        with dissolve
        pause 0.5
        $ walk(loc_pub_toilet_girls)
        with dissolve
        "I pull [bob.name] into one of the cubicles with me. It's the girl's toilet after all so it is deserted."
    "Without any preamble, I press my body against [bob.name]'s and start groping at his cock."
    "He stands there dumbfounded as I fumble with opening his trousers. Eventually I get them down and drop to my knees."
    $ pc_strip_upper()
    bob.name "Whaaa."
    hide bob
    show sb_blowjob face happy 1h
    with dissolve
    pc "Let your friend here do the talking."
    "Despite his protests, he is already sporting a semi and is clearly excited."
    $ having_sex(5)
    $ player.sex_oral(bob, main_quest_01)
    show sb_blowjob suck down with dissolve
    bob.name "Fuck!"
    pc "Mmmm."
    show sb_blowjob poke laugh up with dissolve
    pc "Not complaining now are you?"
    show sb_blowjob suck down 2h with dissolve
    "[bob.name] has been a pretty nice date all things considered, so I put some real effort into giving him a good blowjob."
    "He doesn't seem to be protesting any more either and just has his back against he wall and is happy to let me do all the work."
    "It's fine by me, so I use my hands to wank him off while licking his helmet that's in my mouth"
    show sb_blowjob up
    bob.name "Ah fuck. Didn't think I would have you doing this when you came to say hello."
    show sb_blowjob poke laugh up with dissolve
    pc "Well, I came here to blow off steam. What better way to do that than, well... Blow."
    bob.name "Hah!"
    show sb_blowjob suck down 2h with dissolve
    bob.name "Ahhh it's nice."
    pc "Mmmm."
    if player.check_sex_agree(4):
        pcm "Might be nicer though if he also helped me out. Wonder if I should offer..."
        if player.check_sex_agree_choice(0, "Interested in going a little further?", "..."):
            show sb_blowjob poke happy up with dissolve
            bob.name "What? Err... Ye... *Cough* Ye-es..."
            pc "Ha, okay then."
            jump main_quest_01_reporter_intro_bob_normal_sex_start
    "I know [bob.name] is enjoying so I keep sucking on his cock"
    show sb_blowjob tounge poke up with dissolve
    pc "Bet you didn't think you would be having this kind of end to your night."
    if "school" in tab_top:
        bob.name "Can't say I haven't fantasised about a schoolgirl sucking my cock, never thought it would happen though."
    else:
        bob.name "Can't say I haven't fantasised about having a young lass like you sucking my cock, never thought it would happen though."
    pc "Mmmm I bet."
    show sb_blowjob suck down 2h with dissolve
    "I keep back at it, knowing he must be fairly close considering how he is grunting. The pre cum trickling in my mouth confirms this."
    show sb_blowjob laugh poke up with dissolve
    pc "Can feel you're close. You going to give me something?"
    bob.name "Ah, keep going and I will."
    show sb_blowjob suck down 2h with dissolve
    pc "Mmmmm."
    bob.name "Ahhhhhh."
    bob.name "Liiiike... Thaaaat..."
    $ player.sex_cum(bob, "mouth", main_quest_01)
    bob.name "Ahhhhhhhh!"
    pc "Mmmmmmffff."
    bob.name "Haaaaa... Haaaaa..."
    show sb_blowjob ub face up with dissolve
    show sb_blowjob neutral with dissolve
    show sb_blowjob swallow with dissolve
    pc "Ahhhhh."
    bob.name "Fuck. Swallowed it all?"
    show sb_blowjob laugh
    pc "Yup!"
    bob.name "Phew."
    show sb_blowjob neutral
    jump main_quest_01_reporter_intro_bob_normal_sex_wrapup

label main_quest_01_reporter_intro_bob_normal_sex_start:
    $ having_sex(5)
    hide sb_blowjob with dissolve
    $ pc_striptease()
    pc "Oh? Like what you see?"
    bob.name "Ahem. Yes."
    pc "A lot less chatty now. Cat got your tongue?"
    bob.name "Err, yes? Fuck you are so sexy and I don't want to say something to fuck it up."
    pc "\"So sexy\"? Flattery will get you everywhere."
    show sb_pose_lookback happy smile with dissolve
    pc "You like what you see?"
    bob.name "Mmm."
    pc "Then come here."
    bob.name "Right!"
    show sb_againstwall3 slant wink smile cum
    hide sb_pose_lookback
    with dissolve
    "[bob.name] wastes little time and presses me against the wall, cock ready for me."
    show sb_againstwall3 mast with dissolve
    show sb_againstwall3 poke with dissolve
    bob.name "Mmm, ready?"
    $ player.sex_location_offer()
    if player.want_sexlocation == 1:
        jump main_quest_01_reporter_intro_bob_normal_sex_vag
    else:
        jump main_quest_01_reporter_intro_bob_normal_sex_anal

label main_quest_01_reporter_intro_bob_normal_sex_vag:
    $ having_sex(5)
    pc "Yes, fuck me!"
    $ player.sex_vag(bob, main_quest_01)
    show sb_againstwall3 ag worried sex with dissolve
    pc "Oh fuck yes [bob.name]. Give it to me!"
    pc "Huuuuuuu..."
    "[bob.name] doesn't waste much time and goes at it at a pretty good pace right from the start. Not that I am complaining."
    show sb_againstwall3 closed straight with dissolve
    "I close my eyes and focus only on the cock penetrating me and making me feel good. [bob.name] has his hands all over my body but my mind pays attention to only one thing."
    "Before I know it, [bob.name] is really going to town on me. He is gripping at my hips and thrusting as deep as he can into me."
    "I am loving every moment of it. [bob.name] has been a suprise all night. First hanging and talking with him and now bent over and taking his cock in me. Both have been a lot more pleasurable than I would have ever expected."
    show sb_againstwall3 wink ag with dissolve
    pc "Fuck it feels too gooooood..."
    "At this point I am rocking my hips to meet his thrusts, so each of his thrusts is hitting me hard with a loud *slap* reverberating in the alley."
    pc "Fuck fuck keep going!"
    show sb_againstwall3 closed with dissolve
    bob.name "Ahhh yeeessss..."
    pc "Keeeep... Nnnnggg..."
    pc "YES!"
    bob.name "Ahhhhh!!! Gonna... Cuuuummm..."
    $ player.sex_cum_location_offer(
    difficulty=1, choice_inside="Keep going!", choice_pullout="Not inside.",
    cum_want="main_quest_01_reporter_intro_bob_normal_sex_cum_want", 
    cum_notwant="main_quest_01_reporter_intro_bob_normal_sex_cum_not_want", 
    cum_pullout="main_quest_01_reporter_intro_bob_normal_sex_cum_pullout",
    cum_pullout_anal="main_quest_01_reporter_intro_bob_normal_sex_cum_pullout_anal", 
    cum_pullout_bj="main_quest_01_reporter_intro_bob_normal_sex_cum_pullout_blowjob",  
    cum_pullout_poke="main_quest_01_reporter_intro_bob_normal_sex_cum_pullout_poke",
    cum_bj="main_quest_01_reporter_intro_bob_normal_sex_cum_pullout_blowjob",    
    )

label main_quest_01_reporter_intro_bob_normal_sex_cum_want:
    $ player.sex_cum(bob, "inside", main_quest_01)
    bob.name "Ahh fuck yes!"
    pc "Ah I can feel it in me!"
    bob.name "Nnnnnggggg..."
    pc "Phew."
    jump main_quest_01_reporter_intro_bob_normal_sex_wrapup

label main_quest_01_reporter_intro_bob_normal_sex_cum_not_want:
    $ player.sex_cum(bob, "inside", main_quest_01)
    bob.name "Ahh fuck yes!"
    pc "Ah I can feel it in me! Pull it out."
    $ if_showing("sb_againstwall3", "wink cum", "sb_againstwall2", "wink pokevag", trans=hpunch)
    pcm "Shit, too late..."
    bob.name "Nnnnnggggg..."
    pc "Phew."
    jump main_quest_01_reporter_intro_bob_normal_sex_wrapup

label main_quest_01_reporter_intro_bob_normal_sex_cum_pullout:

    show sb_againstwall3 cum with dissolve
    $ if_showing("sb_againstwall3", "wink mast", "sb_againstwall2", "wink cum", )
    $ player.sex_cum(bob, "pullout", main_quest_01)
    bob.name "Ahh fuck yes!"
    pc "Ah I can feel it on me."
    bob.name "Nnnnnggggg..."
    pc "Phew."
    jump main_quest_01_reporter_intro_bob_normal_sex_wrapup

label main_quest_01_reporter_intro_bob_normal_sex_cum_pullout_blowjob:
    $ if_showing("sb_againstwall3", "poke", "sb_againstwall2", "pokevag",)
    hide sb_againstwall3
    show sb_blowjob poke up
    with dissolve
    show sb_blowjob suck down 2h with dissolve
    $ player.sex_cum(bob, "mouth", main_quest_01)
    pc "Mmmmmfffff."
    bob.name "Ahh fuck yes!"
    pc "Ubbbbbb."
    bob.name "Nnnnnggggg..."
    show sb_blowjob poke up ub 2h with dissolve
    show sb_blowjob neutral with dissolve
    pc "Phew."
    jump main_quest_01_reporter_intro_bob_normal_sex_wrapup

label main_quest_01_reporter_intro_bob_normal_sex_cum_pullout_anal:
    if renpy.showing("sb_againstwall3"):
        show sb_againstwall3 wink mast with dissolve
    else:
        show sb_againstwall2 wink pokevaghand with dissolve
        show sb_againstwall2 pokeasshand with dissolve
        show sb_againstwall2 pokeass shock with dissolve
    pc "Eh? Thats my..."
    $ player.sex_anal(bob, main_quest_01)
    $ if_showing("sb_againstwall3", "sex grit", "sb_againstwall2", "insideass",)
    $ player.sex_cum(bob, "anal", main_quest_01)
    pc "Arssssseeee..."
    bob.name "Ahh fuck yes!"
    $ if_showing("sb_againstwall3", "happy", "sb_againstwall2", "happy",)
    pc "Ah I can feel it in me!"
    bob.name "Nnnnnggggg..."
    pc "Phew."
    jump main_quest_01_reporter_intro_bob_normal_sex_wrapup

label main_quest_01_reporter_intro_bob_normal_sex_cum_pullout_poke:
    $ if_showing("sb_againstwall3", "poke", "sb_againstwall2", "pokevag",)
    $ player.sex_cum(bob, "pullout", main_quest_01)
    bob.name "Ahh fuck yes!"
    $ if_showing("sb_againstwall3", "wink cum", "sb_againstwall2", "wink cum",)
    pc "Ah I can feel it!"
    bob.name "Nnnnnggggg..."
    pc "Phew."
    jump main_quest_01_reporter_intro_bob_normal_sex_wrapup

label main_quest_01_reporter_intro_bob_normal_sex_anal:
    $ having_sex(5)
    pc "Wait, I don't want to end up pregnant so use my arse."
    show sb_againstwall3 mast with dissolve
    bob.name "Fuck yes!"
    pc "Oh? Guys are not normally that eager."
    show sb_againstwall3 poke with dissolve
    bob.name "First time for me like this. Not many girls wanted to do it like this before."
    pc "Ah, all different now. Getting ass fucked is the only way to have sex and not worry about a baby."
    "The entire time we have been talking, he has been putting more pressure on my arsehole with his cock, and finally it starts to slip inside me."
    $ player.sex_anal(bob, main_quest_01)

    if player.asex < 5:
        show sb_againstwall3 grit worried sex with dissolve
        bob.name "Ah fuck it's so tight!"
        pc "Nnnng fuck fuck!"
        bob.name "Ah, should I take it slow?"
        pc "Yes! Slow!"
        show sb_againstwall3 neutral with dissolve
        bob.name "Thought you might be used to this."
        pc "No, not yet. But I need to unless I want to risk a baby."
    else:
        show sb_againstwall3 sex happy with dissolve
        bob.name "Ah fuck yes!"
    pc "Huuuuuu..."
    "[bob.name] takes it fairly slow at first, gently sliding his cock in and out of my ass while gripping onto my hips."
    if player.asex < 5:
        "As he continues to fuck me, he slowly picks up the pace. I start to get used to hs cock in my arse so I relax and start to enoy the feeling of him in me."
    else:
        "As he continues to fuck me, he slowly picks up the pace. I just relax and enjoy the feeling he is giving me."
    show sb_againstwall3 sex happy closed straight with dissolve
    pc "Mmmmm..."
    "I close my eyes and focus only on the cock penetrating me and making me feel good. [bob.name] has his hands all over my body but my mind pays attention to only one thing."
    "Before I know it, [bob.name] is really going to town on my arse. He is gripping at my hips and thrusting as deep as he can into me."
    show sb_againstwall3 wink ag with dissolve
    pc "Fuck it feels to gooooood..."
    "At this point I am rocking my hips to meet his thrusts, so each of his thrusts is hitting me hard with a loud *slap* reverberating in the alley."
    pc "Fuck fuck keep going!"
    show sb_againstwall3 closed with dissolve
    bob.name "Ahhh yeeessss..."
    pc "Keeeep... Nnnnggg..."
    pc "YES!"
    $ player.sex_cum(bob, "anal", main_quest_01)
    pc "Yes yes yes!"
    bob.name "Ahhhhhhhhhhh!!!"
    show sb_againstwall3 smile wink with dissolve
    bob.name "Haaaaaaa..."
    jump main_quest_01_reporter_intro_bob_normal_sex_wrapup

label main_quest_01_reporter_intro_bob_normal_sex_wrapup:
    $ if_showing("sb_againstwall3", "wink happy")
    pc "Fucking hell. Didn't expect that from you."
    bob.name "Say the same about you."
    $ if_showing("sb_blowjob", "laugh")
    pc "Heh."
    if renpy.showing("sb_againstwall3"):
        if "sex" in renpy.get_attributes("sb_againstwall3"):
            show sb_againstwall3 poke with dissolve
        if not "cum" in renpy.get_attributes("sb_againstwall3"):
            show sb_againstwall3 cum with dissolve
    elif renpy.showing("sb_againstwall2"):
        if "insideass" in renpy.get_attributes("sb_againstwall2"):
            show sb_againstwall2 pokeass with dissolve
        if "insidevag" in renpy.get_attributes("sb_againstwall2"):
            show sb_againstwall2 pokevag with dissolve
        if not "mast" in renpy.get_attributes("sb_againstwall2"):
            show sb_againstwall2 cum with dissolve
    if "school" in tab_top:
        bob.name "Always good to know even sweet little school girls like you have a dirty side."
    else:
        bob.name "Always good to know even sweet little girls like you have a dirty side."
    pc "Is it now?"
    bob.name "Mmm."
    $ if_showing("sb_againstwall3", "noman", "sb_blowjob", "noman neutral", "sb_againstwall2", "noman")
    bob.name "Phew."
    $ renpy.scene()
    show bob at right1
    with dissolve
    pc "Made a bit of noise. Better not hang around."
    $ pc_dress_slow()

    if "work" in tab_top:
        bob.name "You heading back to the bar?"
        pc "No, I'll change out of my uniform and call it a night."
    else:
        bob.name "You coming back inside?"
        pc "No, you head in without me. I'll start making my way home."
    bob.name "Ok, well, I hope I see you again."
    $ player.face_happy()
    pc "I bet. See you round [bob.name]."
    $ player.face_neutral()
    hide bob with dissolve
    if "work" in tab_top:
        pcm "Right, get changed and go see [simon.name]."
        jump main_quest_01_reporter_intro_bob_waitress_redress
    pcm "Right, still need to see [simon.name] and..."
    show simon smile at right1 with dissolve
    $ player.face_shock()
    pc "Ah!"
    $ player.face_neutral()
    if loc_cur == loc_alley:
        pc "Sneaking up like some alleyway rapist."
    else:
        pc "Sneaking up like some toilet rapist."
    simon.name "Well, someone had fun."
    if not "paid" in main_quest_01.list:
        pc "Shush. Give me my money."
        simon.name "Yup. Money well spent. Here you go."
        $ player.add_money(150)
    else:
        pc "Shush."
    if not loc_cur == loc_alley:
        pc "You manage to get good photos? Pissing rain out so had to do it here instead."
        simon.name "Yeah no worries. Angles are a bit weird and makes me look like a peeping tom, but clear enough who it is and what you both were up to."
        pc "Well, good I suppose."
    simon.name "Almost thought you wouldn't go through with it. Looked like you were having a good time with [bob.name]."
    pc "I was having a good time. He seemed nice."
    simon.name "Really? Then why did you go through with stitching him up?"
    pc "You are going to fuck him over regardless, so I might as well get paid for something that's going to happen anyway."
    simon.name "You could have warned him."
    pc "Not my business. He was nice to me but who knows what the real situation is."
    if bob.sex:
        simon.name "Didn't have to fuck him though. The blowjob you gave him was more than enough for what I needed."
        pc "I know."
        simon.name "Oh? He made that much of an impression did he?"
        pc "..."

    simon.name "Well anyway, a deal's a deal, here you go. My bag with all the info I have. It will put your bosses' minds at ease."
    simon.name "And not have them send someone less pretty."
    if bob.sex and not simon.naughty:
        simon.name "Well, see you around [name]. After that little peep show you gave, think I'll have to stop off at the highway before heading home."
        if player.check_whore():
            pcm "Hmm, could take this chance to walk away with even more money. He's probably already pretty wound up after that show so might be able to gouge him."
            if player.check_sex_agree_choice(0, "Offer my services.", "Let him leave."):
                jump main_quest_01_reporter_intro_bob_normal_sex_wrapup_sexagain_start
            else:
                pc "Good luck with that."
                simon.name "Mmm."
                hide simon with dissolve
                pcm "Well, that went well. Dealt with [tucker.name]'s problem and earned a bit of money in the process."
                pcm "Better go home first and sleep off this booze though. Gonna have a killer headache in the morning."
                jump main_quest_01_reporter_game_complete_wrapup

    simon.name "Well, see you around [name]."
    pc "Mmm, see you."
    hide simon with dissolve
    pcm "Well, that went well. Dealt with [tucker.name]'s problem and earned a bit of money in the process."
    pcm "Better go home first and sleep off this booze though. Gonna have a killer headache in the morning."
    jump main_quest_01_reporter_game_complete_wrapup





label main_quest_01_reporter_intro_bob_normal_sex_wrapup_sexagain_start:
    $ add_to_list(main_quest_01.list, "simon_whore_offer")
    pc "For another 150, I could save you the trip."
    simon.name "Err... Really? You pulling my leg?"
    pc "You just saw what I did. Make it worth my while and I'll give a personal repeat performance."
    simon.name "Really? Fuck I won't say no to that."
    simon.name "You serious?"
    pc "*Sigh*"
    $ pc_strip_upper()
    show sb_pose_showbreasts
    hide simon
    with dissolve
    pc "Well..."
    pc "Pay up."
    simon.name "..."

    $ player.soldprice = 150
    $ player.add_money(150)
    pc "Thanks."
    $ pc_striptease()
    hide sb_pose_showbreasts
    show sb_againstwall2
    with dissolve
    simon.name "Fuck. So much nicer up close."
    show sb_againstwall2 pokevaghand with dissolve
    if bob.asex:
        pc "Don't be poking me there. I didn't want [bob.name]'s baby and I dont want yours."
        simon.name "Right."
        jump main_quest_01_reporter_intro_bob_normal_sex_wrapup_sexagain_anal
    else:
        $ player.sex_location_offer()
        if player.want_sexlocation == 1:
            jump main_quest_01_reporter_intro_bob_normal_sex_wrapup_sexagain_vag
        else:
            jump main_quest_01_reporter_intro_bob_normal_sex_wrapup_sexagain_anal





label main_quest_01_reporter_intro_bob_normal_sex_wrapup_sexagain_vag:
    show sb_againstwall2 pokevag with dissolve
    if player.cum_locations["cum_vagin"] or player.cum_locations["cum_vagout"]:
        "I am still soaking wet from my last fucking, and with [bob.name]'s cum leaking out of me, [simon.name]'s cock manages to slip right into me."
    elif bob.vsex:
        "I am still soaking wet and streched from having sex with [bob.name], so [simon.name]'s cock manages to slip right into me."
    else:
        "Already pent up from watching the show, [simon.name] wastes little time in pressing against me and his cock slips right in."
    $ player.sex_vag(simon, main_quest_01)
    show sb_againstwall2 insidevag wink with dissolve
    pc "Haa fuck!"
    $ having_sex(5)
    "It's clear he was really wound up as he doesn't even start slowly and just immediatly claws into my ass cheeks while pounding me like a horny rabbit."
    "I press right into him and match the pace of his trusts, pressing back into him and he thrusts into me to push him as deep as possible into me."
    "Seems I might have over done it though because it's not long before..."
    $ player.sex_cum(simon,"inside", main_quest_01)
    simon.name "Ahhhhh fuuuuckkk!!!"
    if not player.has_perk(perk_preg_want) or not player.preg_knows:
        show sb_againstwall2 pokevag with hpunch
        "I manage to buck forward and pull him out of me, though it's probably already too late."
        show sb_againstwall2 cum with dissolve
    simon.name "Fuck fuck fuck!"
    simon.name "Huuuuuu..."
    pc "Mmmm, looks like my show really did get you all hot and bothered."
    if not player.has_perk(perk_preg_want) or not player.preg_knows:
        pc "Some warning would have been nice though. Not interested in having your baby."
    simon.name "Fuck. Even without the show before, this sexy arse is enough to make any man cum right away."
    simon.name "Worth it though."
    $ player.spank()
    pc "Ha!"
    if player.has_perk(perk_preg_want) or player.preg_knows:
        show sb_againstwall2 pokevag with dissolve
    show sb_againstwall2 noman with dissolve
    jump main_quest_01_reporter_intro_bob_normal_sex_wrapup_sexagain_wrapup

label main_quest_01_reporter_intro_bob_normal_sex_wrapup_sexagain_anal:
    show sb_againstwall2 pokeasshand with dissolve
    show sb_againstwall2 pokeass with dissolve
    if bob.asex:
        "Already streched from the ass fucking [bob.name] gave me, [simon.name] finds little resistance in trying to enter me and slides his cock right up my arse."
    else:
        "Already pent up from watching the show, [simon.name] wastes little time in lining up with my arse and pressing it right in first time."
    $ player.sex_anal(simon, main_quest_01)
    show sb_againstwall2 insideass wink with dissolve
    pc "Haa fuck!"
    $ having_sex(5)
    "It's clear he was really wound up as he doesn't even start slowly and just immediatly claws into my ass cheeks while pounding me like a horny rabbit."
    "I press right into him and match the pace of his trusts, pressing back into him and he thrusts into me to push him as deep as possible into me."
    "Seems I might have over did it though because it's not long before..."
    $ player.sex_cum(simon,"anal", main_quest_01)
    simon.name "Ahhhhh fuuuuckkk!!!"
    simon.name "Fuck fuck fuck!"
    simon.name "Huuuuuu..."
    pc "Mmmm, looks like my show really did get you all hot and bothered."
    simon.name "Fuck. Even without the show before, this sexy arse is enough to make any man cum right away."
    simon.name "Worth it though."
    $ player.spank()
    pc "Ha!"
    show sb_againstwall2 pokeass with dissolve
    show sb_againstwall2 noman with dissolve
    jump main_quest_01_reporter_intro_bob_normal_sex_wrapup_sexagain_wrapup

label main_quest_01_reporter_intro_bob_normal_sex_wrapup_sexagain_wrapup:
    simon.name "Going to sleep soundly tonight."
    hide sb_againstwall2
    show simon smile at right1
    with dissolve
    pc "I aim to please."
    simon.name "Mmmm."
    $ pc_dress_under()
    simon.name "Well, I had better go before I am comvinced to empty more of my pockets."
    pc "Oh? Still open for more."
    $ pc_dress_slow()
    simon.name "Hah. See you [name]."
    pc "Mmm, see you."
    hide simon with dissolve
    pcm "Well, that went well. Dealt with [tucker.name]'s problem and earned a bit of money in the process."
    pcm "Better go home first and sleep off this booze though. Gonna have a killer headache in the morning."
    jump main_quest_01_reporter_game_complete_wrapup


label main_quest_01_reporter_intro_bob_postwaitresssex_wrapup:
    $ walk(loc_pub)
    with dissolve
    "Fortunately, [simon.name] has changed seats and is sitting on the complete opposite end of the bar where [bob.name] was."
    show simon smile at right1 with dissolve
    if bob.sex:
        simon.name "Wow. Well you know how to get a job done. Need a tissue?"
        pc "I'll clean up in the toilets afterwards."
    else:
        simon.name "Well, that was something. Some pretty good shots here."
        pc "Yeah? Managed to get what you were after?"
        simon.name "Yup."
    if "paid" in main_quest_01.list:
        simon.name "Well, I got all the photos I needed so good job. Damn I really could use someone like you in my line of work."
        pc "Well, good for you. But with that we are done aren't we?"
        if player.cum_locations["cum_vagin"] or player.cum_locations["cum_assin"]:
            pc "I have someone leaking out of me so no interest in hanging around chatting."
        else:
            pc "I am all sticky thanks to [bob.name] so no interest in hanging around chatting."
        simon.name "Yup, got way more than I needed."
    else:

        simon.name "Well, I got all the photos I needed so good job. Damn I really could use someone like you in my line of work."
        pc "Well, good for you. But about time you paid up now isn't it?"
        if player.cum_locations["cum_vagin"] or player.cum_locations["cum_assin"]:
            pc "I have someone leaking out of me so no interest in hanging around chatting."
        else:
            pc "I am all sticky thanks to [bob.name] so no interest in hanging around chatting."
        simon.name "Yup, got way more than I needed. So here you go."
        if bob.naughty:
            $ player.add_money(150)
        else:
            $ player.add_money(50)

    pc "Good. Well, see you."
    simon.name "See you around [name]."
    hide simon with dissolve
    pcm "Well, that went well. Dealt with [tucker.name]'s problem and earned a bit of money in the process."
    pcm "Better go home first and sleep off this booze though. Gonna have a killer headache in the morning."
    jump main_quest_01_reporter_game_complete_wrapup
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
