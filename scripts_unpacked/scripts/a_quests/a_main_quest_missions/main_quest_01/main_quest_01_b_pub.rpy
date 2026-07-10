label main_quest_01_reporter1:
    if not t.hour in (18,19,20,21,22,23,0,1,2,3):
        if t.hour < 18:
            pcm "I don't see [simon.fullname] anywhere. It's probably too early for him to be here."
        elif t.hour > 3:
            pcm "I don't see [simon.fullname] anywhere. It's probably too late and he went home."
        jump travel
    else:
        pcm "Hmm, [simon.fullname] is probably around here somewhere. Should I look for him?"
        menu:
            "Yes, look around for him.":
                jump main_quest_01_reporter_start
            "Not right now.":

                jump travel

label main_quest_01_reporter_start_cheat:
    "Resetting mission variables. Make sure to make a new save because this cheat may break the main mission if you have already passed this point in The Institute chain."
    $ main_quest_01 = QuestClass()
    $ simon = Npc(fname="Simon", sname="Banks")
    $ bob = Npc(fname="Bob", sname="Cray")
    jump main_quest_01_reporter_start





label main_quest_01_reporter_start:
    $ player.face_neutral()
    pcm "So this [simon.name] should be around here somewhere now that it's evening. I wonder if I can find him among all these people?"
    pcm "Ah! I see him over there near the bar. Hmmm. Now I wonder how I should approach him?"
    menu:
        "They didn't give me this sexpot body for nothing"(badge="heart_5", enabled=player.check_sex_agree(3, notif=False) and not player.isfat):
            $ add_to_list(main_quest_01.list, "sex_branch")
            jump main_quest_01_reporter_sex_branch
        "I could try and intimidate him"(badge="int_5", enabled=player.check_speech(4, notif=False)):

            $ add_to_list(main_quest_01.list, "intimidate_branch")
            jump main_quest_01_reporter_intimidate_branch
        "Just chatting with him should do the trick"(badge="conf_5", enabled=not player.check_nowill(notif=False, block_face=True)):

            $ add_to_list(main_quest_01.list, "talk_branch")
            pc "I guess a more direct approach could work."
            show simon at right1 with dissolve
            pc "Hey, this seat taken?"
            simon.name "Hmm. Took longer than I expected."
            pc "Huh?"
            simon.name "Sent by The Institute?"
            jump main_quest_01_reporter_intro_busted
        "Dress in my bar clothes and try and get close to him"(badge="allure_6", enabled=pub_waitress.timesworked > 4):

            $ add_to_list(main_quest_01.list, "waitress_branch")
            jump main_quest_01_reporter_bargirl_branch
        "Sit near him and take it from there I suppose":

            $ add_to_list(main_quest_01.list, "wait_branch")
            jump main_quest_01_reporter_intro_drink
        "I'll think about it and come back another day":

            pc "He isn't going anywhere. I'll have a think about what to do before wasting my only chance to get close to him."
            $ walk(loc_revel)
            jump travel





label main_quest_01_reporter_sex_branch:
    pcm "Time to put it to work I suppose..."
    show simon at right1 with dissolve
    pc "Hey, interested in some company?"
    simon.name "Hmm. Took longer than I expected."
    pc "Expecting me?"
    simon.name "Sent by The Institute? Just didn't think they would send someone... quite like you."
    if "school" in tab_top:
        pc "I hear guys like a girl in a school uniform."
        simon.name "Won't disagree there."
    elif player.allure > 100:
        pc "Like what you see?"
        simon.name "Err, that I do."
    else:
        pc "Oh? Hoping for some burly guy to come chat with you?"
        simon.name "Not quite."
    pc "So, since you know why I am here, we can drop the pretence. I want to know why you are poking your nose in Institute business."
    simon.name "Well, that's info I have and you want. Not going to just give up my only leverage."
    pc "Everyone has a price."
    if c.braless and c.clevage:
        simon.name "That why you came over bouncing those tits around?"
        pc "They tend to do that on their own."
        simon.name "Yeah, a bra would normally stop that. But I see you decided to go without."
        pc "Well, wouldn't look so nice with this top."
    elif c.pokenips and (outside or player.desire > 70):
        simon.name "That why you came over with those things ready to take someone's eye out?"
        pc "It's a bit chilli in here and they do what they want."
        simon.name "Right. And not wearing a bra?"
        pc "I like them to be free."
    elif c.slutty:
        simon.name "That why you came over here showing off all that skin?"
        if t.month in ("Spring","Summer"):
            pc "Nice weather out there so I am enjoying it."
            simon.name "Yeah, but bet you like the attention as well."
            pc "Even if I wore a burlap sack, the perverts out there would still look."
        else:
            pc "Err, the weather is nice?"
            simon.name "Hah!"
    elif player.allure > 100:
        simon.name "That why you came over here looking like that?"
        pc "Like what? I like dressing like this."
        simon.name "Or like the attention it brings?"
        pc "Even if I wore a burlap sack, the perverts out there would still look."
    elif "school" in tab_top:
        simon.name "That why you came over here in a uniform?"
        pc "Well, I have a day life as well."
        simon.name "Yeah right. The Institute sending a schoolgirl to do their dirty work."
        pc "Yup."
    else:
        simon.name "If that's the game you are playing, would have expected you to look more the part."
        pc "Looking like that gets unwanted attention."
    pc "So anyway, wanna tell me what you are up to?"
    simon.name "Why should I?"
    pc "Because I am much sweeter than anyone who will come after me. I can be nice. No point in making trouble where there doesn't need to be."
    simon.name "And what do I get out of it?"
    pc "Well, depends on what you know and what you want."
    simon.name "Girl like you obviously knows what a man wants."
    if player.check_sex_agree_choice(diff=2,option1="Go along with sexual advances" ,option2="Shut him down"):

        pc "Ah, it's like that is it?"
        if player.allure > 100:
            simon.name "Of course. Don't act shocked coming over here dressed like that and giving me this cutesy attitude."
        else:
            simon.name "Of course. Acting all shocked while giving me this cutesy attitude."

        if player.iswhore or player.isslut:
            pc "So you want to go somewhere private for the info?"
            simon.name "Sounds good to me."
            pc "And how you going to give it to me?"
            simon.name "Prefer your pussy, but your ass will do."
            pc "Idiot. I mean the info."
            simon.name "Oh? I have it all written down in my bag. Pay my price and you can have it all."
            pcm "Hmm, well easy way to get it I suppose."
            if player.check_sex_agree_choice(diff=4,option1="Have sex in return for the info" ,option2="Tell him no"):
                jump main_quest_01_reporter_sex_branch_prepare
            else:
                jump main_quest_01_reporter_intro_rejectsex
        else:

            pc "So you want me to pay like that for the info?"
            if c.clevage:
                simon.name "Unless you have a pile of cash hidden down that cleavage, then yes."
            elif c.skirt:
                simon.name "Unless you have a pile of cash hidden up that skirt, then yes."
            else:
                simon.name "Unless you have a pile of cash hidden somewhere on you, then yes."

            if player.check_poor():
                pc "Yeah right. If I had a bunch of cash, you think I would be here chatting with you and not drinking myself silly?"
            else:
                if player.sold > 4:
                    pc "And if I do have some hidden, how much? Whores don't go for much."
                else:
                    pc "And if I do have some hidden, how much?"
                simon.name "Let's say £ 10,000."
                if player.cash > 10000:
                    pcm "I have that kind of money, but he can fuck himself if he thinks his info is worth that."
                if player.confidence > 50:
                    pc "Yeah right. No whore is worth that and nor is your info. Cheaper to have you killed."
                    simon.name "What?"
                    pc "Nothing, nothing."
                else:
                    pc "Yeah right. No whore is worth that and nor is your info."
            simon.name "Well then, we have to come to some other arrangement."
            pc "*Sigh* It's what you have been after from the start isn't it?"
            simon.name "No comment."
            if player.check_sex_agree_choice(diff=4,option1="Have sex in return for the info" ,option2="Tell him no"):
                jump main_quest_01_reporter_sex_branch_prepare
            else:
                jump main_quest_01_reporter_intro_rejectsex
    else:

        pc "Err, that's not really a price I am willing to pay."
        $ add_to_list(main_quest_01.list, "sex_branch_gameoffer")
        jump main_quest_01_reporter_intro_simon_game_offer

label main_quest_01_reporter_sex_branch_prepare:
    pc "Right, go somewhere private then?"
    simon.name "Sounds good."
    pc "Follow me."
    hide simon with dissolve
    if pub_waitress.timesworked > 4:
        $ walk(loc_pub_changingroom)
        with dissolve
        pcm "No one here."
        "I wave at [simon.name] to come in."
        show simon at right1 with dissolve
        simon.name "Err, are we allowed back here?"
        pc "It's fine. I work here so no one will bother us."
    else:
        $ walk(loc_pub_toilet_girls)
        with dissolve
        pcm "No one here."
        "I wave at [simon.name] to come in."
        show simon at right1 with dissolve
        simon.name "Err, you sure?"
        pc "You see any women in the pub other than me?"
        simon.name "Not many."
        pc "So no one will bother us here."
    simon.name "Right then..."
    pc "How do I know you are going to give me the info I need?"
    simon.name "It's all in my bag here. Hold up your end of the bargain and it's yours."
    pc "In there?"
    simon.name "Yup. Plus, this is a good deal so no need for me to screw you out of it."
    pc "Hmmm..."
    simon.name "But you are looking a bit over dressed for our deal."
    pcm "Ugh, doesn't look like he is going to slip up and give me what I need unless he gets what he wants."
    pcm "He did say it was all in his bag. Could steal it..."
    pcm "No, that could get me in way more trouble than just bending over."
    pcm "*Sigh* Last chance to back out I guess."
    if player.check_sex_agree_choice(diff=2, option1="Right, okay then", option2="Err, no. I'm ending this now"):
        $ add_to_list(main_quest_01.list, "sex_branch_sex")
        jump main_quest_01_reporter_sex_branch_sex
    else:

        $ player.face_worried()
        pc "Sorry, I was hoping you would slip up. But it's gone a bit too far."
        simon.name "Backing out of it?"
        pc "Yeah, I am not willing to go that far for whatever you have. I'll leave The Institute to deal with it from here."
        pc "See you."
        simon.name "Wait!"
        pc "Try something and I'll scream."
        simon.name "*Tsk* I'm not that kind of guy."
        simon.name "Let's negotiate then. How far are you willing to go?"
        pc "Huh?"
        simon.name "Suck my cock?"
        pc "Oh?"
        menu:
            "Ok, I can do that.":
                $ add_to_list(main_quest_01.list, "sex_branch_blowjob")
                pc "Guess I could go with that."
                simon.name "Great!"
                pc "Err, straight to it then..."
                $ player.face_surprised()
                pc "And looks like your friend is already standing to attention."
                if c.slutty:
                    simon.name "Dressed like that I think you left half the bar standing up."
                elif "school" in tab_top:
                    simon.name "Well, you were right. We do like a girl in a school uniform."
                elif c.braless and c.clevage:
                    simon.name "Couldn't take my eyes off those bouncing tits since you walked in."
                elif c.pokenips and (outside or player.desire > 70):
                    simon.name "Could say the same with your nipples."
                elif player.allure > 100:
                    simon.name "How can I not be when you are dressed like that."
                else:
                    simon.name "Not every day I get a chance with a pretty young thing like you."
                $ player.face_neutral()
                pc "*Sigh*"
                $ pc_strip_upper()
                pc "Okay then..."
                pc "Come here."
                $ npc_race_picker(simon)
                jump main_quest_01_reporter_game_naked_blowjob
            "No, it's still too much.":

                simon.name "*Sigh* You really aren't making this easy are you?"
                simon.name "Can't just ask and expect everything to go your way. Need to pay something."
                if player.check_sex_agree(3, notif=False):
                    if not player.sold:
                        pc "I might not be the most innocent girl there is, but selling myself for The Institute..."
                        pc "I decided it's not something I want to do."
                    else:
                        pc "I might not be the most innocent girl there is, but if they are going to be sending me on jobs like this I probably shouldn't be bending over to solve issues."
                        pc "So I decided it's not something I want to do."
                else:
                    pc "I thought I could do it coming in here, but now it's come to it, I realised I don't want to."
                simon.name "Ok, I'll go along with that. But I still have something you want and you're going to have to cough up something for it."
                simon.name "No sex then. Undress and let me get myself off while looking at you? Nothing inside you."
                pc "Not inside?"
                menu:
                    "Okay then.":
                        $ add_to_list(main_quest_01.list, "sex_branch_buttjob")
                        jump main_quest_01_reporter_game_naked_buttjob
                    "No, still too much.":
                        simon.name "Well, I tried. Not going to just give it up because of your pretty smile."
                        pc "I have a pretty smile?"
                        simon.name "Err, well..."
                        pc "Thanks."
                        simon.name "Err..."
                        simon.name "You're welcome."
                        simon.name "..."
                        simon.name "Well, I'm leaving now."
                        pc "Right, sorry."
                        simon.name "No problem. Was still a better evening than I had planned."
                        hide simon with dissolve
                        pcm "Right then..."
                        $ walk(loc_pub)
                        pc "..."
                        show trixie at right1 with dissolve
                        trixie.name "That was a quick one. Here, y' could prob'ly do with this after that."
                        $ player.add_perk(perk_drinking_beer_2)
                        pc "Err, thanks."
                        trixie.name "Be safe hon."
                        hide trixie with dissolve
                        jump main_quest_01_reporter_intro_rejectsex_catcher

label main_quest_01_reporter_sex_branch_sex:
    $ pc_striptease()
    simon.name "Damn. I thought you looked good dressed but even better without your clothes."
    if player.pregnancy == 1:
        simon.name "That little pouch you have the beginnings of a baby?"
        if not player.vvirgin:
            if player.preg_knows:
                pc "..."
                pc "A baby..."
                simon.name "Bet you had fun making that."
                if player.rapebaby:
                    pc "Yeah sure. Knocked up while being raped is always fun."
                    simon.name "Oh? Sorry..."
                elif player.virginbaby:
                    pc "Great time. Lost my virginity and got a baby all at the same time."
                    simon.name "Ah wow. What luck."
                elif player.soldbaby:
                    pc "Not sure about fun, but left with more money at least."
                    simon.name "Oh? Wow. Hope he paid well."
                    pc "Yeah right. He got the better deal no doubt."
                else:
                    pc "Yeah, though not sure I would have agreed if I knew he would leave something behind in me."
            else:
                if player.creamvag > 0:
                    if player.has_perk(perk_preg_want):
                        pc "Hopefully a baby. But we will see."
                    elif player.has_perk(perk_preg_notwant):
                        pc "Hopefully not."
                    else:
                        pc "Not sure..."
                else:
                    pc "I've been careful so shouldn't be a baby"
        else:
            pc "Probably need to do a bit more working out..."
    elif player.pregnancy > 1:
        simon.name "Looks even bigger naked. Bet you had fun making that."
        if player.rapebaby:
            pc "Yeah sure. Knocked up while being raped is always fun."
            simon.name "Oh? Sorry..."
        elif player.virginbaby:
            pc "Great time. Lost my virginity and got a baby all at the same time."
            simon.name "Ah wow. What luck."
        elif player.soldbaby:
            pc "Not sure about fun, but left with more money at least."
            simon.name "Oh? Wow. Hope he paid well."
            pc "Yeah right. He got the better deal no doubt."
        else:
            pc "Yeah, though not sure I would have agreed if I knew he would leave something behind in me."
    else:
        simon.name "You are such a sexy munchkin."
        pc "Oi, call me that again and I'll put my clothes back on."
        simon.name "Wow, ok..."

    simon.name "Let's see what you have."
    $ npc_race_picker(simon)
    show sb_againstwall2
    hide simon
    with dissolve
    simon.name "Such a perfect arse."
    show sb_againstwall2 pokevaghand with dissolve
    if player.check_sex_agree(3, notif=False):
        show sb_againstwall2 mast happy with dissolve
        pc "If you like my arse that much then you will love it here."
        simon.name "Oh I'm sure I will."
    if player.desire > 80:
        simon.name "Fuck, you are totally soaking. No wonder you just came up and asked to fuck for the info."
        pc "Well, two birds and all that."
    simon.name "So glad The Institute sent someone like you. Sure do know how to convince someone."
    pc "Mmmm."
    simon.name "Gonna have to poke my nose in their business more often."
    show sb_againstwall2 pokevag with dissolve
    pc "Keep provoking them and next time it might be you getting poked instead of me."
    simon.name "Much prefer it be you."
    $ player.spank()
    pc "Ah!"
    simon.name "Mmmm, sending a little whore to me. Have to thank them."
    pc "Don't call me little."
    simon.name "Err, ok... That's the word that upsets you and not being called a whore."
    if player.iswhore:
        pc "Well, I am a whore so what do I care?"
        simon.name "You are also little."
        pc "..."
    elif player.isslut:
        pc "I kinda like being called a whore."
    elif player.check_sex_agree(3, notif=False):
        pc "Well, calling me a whore is kinda fun."
    else:
        pc "..."
    simon.name "Well then. Take it you dirty whore!"
    $ player.sex_vag(simon, main_quest_01)
    show sb_againstwall2 insidevag wink vhappy with dissolve
    pc "Ahhh fuuuuuck!"
    simon.name "Mmmmmmmm."

    "Despite doing this for the job, I relax and try to enjoy what is happening."
    show sb_againstwall2 mast closed with dissolve
    "I used my hand to help get me off as I don't have much faith in [simon.name] getting the job done."
    "Although at this rate he might..."
    pc "Ah yes! Keep going."
    simon.name "Mmmmm."
    $ player.spank()
    pc "Haaaa!"
    simon.name "Ahhh this is the best."
    simon.name "Ooohhhh I am close."
    pc "Mmmm."
    simon.name "Where do you want it?"


    $ player.sex_cum_location_offer(
    difficulty=1, 
    cum_want="main_quest_01_reporter_game_naked_buttjob_cum_want", 
    cum_notwant="main_quest_01_reporter_game_naked_buttjob_cum_not_want", 
    cum_pullout="main_quest_01_reporter_game_naked_buttjob_cum_pullout",
    cum_pullout_anal="main_quest_01_reporter_game_naked_buttjob_cum_pullout_anal", 
    cum_pullout_bj="main_quest_01_reporter_game_naked_buttjob_cum_pullout_blowjob",  
    cum_pullout_poke="main_quest_01_reporter_game_naked_buttjob_cum_pullout_poke",
    cum_bj="main_quest_01_reporter_game_naked_buttjob_cum_blowjob",    
    
    block_anal_check=True
    )





label main_quest_01_reporter_bargirl_branch:
    pcm "Dressing as a waitress should get me close to him."
    $ walk(loc_pub_changingroom)
    $ player.face_neutral()
    pause 1
    $ pc_strip()
    pause 0.5
    $ pub_waitress.work_dress()
    pcm "Right, so apparently he has been here quite a bit so I can probably just pretend I have seen him around."
    pcm "Can't say I have noticed him though so maybe he doesn't interact with the girls much."
    $ walk(loc_pub)
    $ player.face_neutral()
    pause 0.5
    pcm "Right, looks like he is low on booze."
    $ npc_race_picker(simon)
    show pub_serve_talking
    $ player.face_happy()
    with dissolve
    pc "Hey sweetheart, get you another?"
    simon.name "Err, sure."
    hide pub_serve_talking
    $ player.face_neutral()
    with dissolve
    "I head over to the bar and grab a couple of beers from behind the counter."
    show pub_serve_clevage
    $ player.face_happy()
    with dissolve
    pc "Here you go darling."
    simon.name "Thanks."
    hide pub_serve_clevage
    show pub_serve_talking
    $ player.face_neutral()
    with dissolve
    pc "So whats on your mind?"
    simon.name "Huh?"
    pc "Normally when people are alone in here, they can't take their eyes off the serving girls. Seen you round here a lot and your mind is always elsewhere."
    simon.name "Ah. Yeah, can't say I'm here to ogle the girls."
    pc "Well you nurse those drinks more than most in here. So what you after? Maybe I can help you out."
    if player.check_speech(If(c.pants,3,1)):
        $ add_to_list(main_quest_01.list, "waitress_branch_pass_convince")
        simon.name "Hmm. Tell you what. See that guy over there?"
        pc "Hmm, yeah."
        simon.name "What do you know about him?"
        pc "Hmm, seen him about. Why do you want to know?"
        simon.name "That's for me to know."
        pc "Well, if you want me to ask around and see what the other girls know, you're going to have to indulge my curiosity."
        simon.name "Hmmm..."
        simon.name "Ok, sure. Ask the other girls and I'll tell you."
        pc "Right."
        hide pub_serve_talking with dissolve
        pcm "Hmm, only interested in him specifically..."
        show trixie at right5 with dissolve
        pc "That fella over there. What's his deal?"
        show trixie with dissolve:
            xzoom -1
        trixie.name "Ah that's Bob. In here pretty much every day."
        show trixie with dissolve:
            xzoom 1
        pc "What do you know about him?"
        trixie.name "Well, he's married, so not sure you are going to get the good life off him."
        trixie.name "He's usually in here early while I'm workin' and sticks to me like glue. Lonely fella even though he has a wife."
        if pub_waitress.sold > 4:
            pc "He ever pay for extra service?"
            trixie.name "Yeah when he can afford it. Mostly just drowns his sorrows and whines to anyone who listens."
            pc "Whines?"
            trixie.name "Yeah, wife not treatin' him well or some sob story like that. Who knows with a drunkard. Don't really care as long as he pays up."
        else:

            pc "He a pervert like the rest?"
            trixie.name "Of course. Doesn't normally have the cash to keep anyone's attention, but now and then he has a bit."
            pc "He... Errr... You know..."
            trixie.name "Pay for extra? When he can afford it, which isn't common. Best to ignore him and focus on the others with heavier pockets."
        pc "Anything else you know about him?"
        trixie.name "Why do you care?"
        pc "Don't really. But I have a side gig so need to ask."
        trixie.name "Ah. Well not much else anyway. In here every day from work end to closing. Lecherous like most round here but too broke to pay for much."
        pc "Thanks."
        trixie.name "Sure, I expect a drink from you if this gig is getting you paid."
        pc "Heh, sure."
        hide trixie with dissolve
        pcm "Nothing too interesting. Just the same as the rest of the creeps round here."
        pcm "Oh well. Let's see if I can get more info out of [simon.name]."
        show pub_serve_talking with dissolve
        pc "Had a chat about your friend over there."
        simon.name "Yeah?"
        pc "You first. What's the deal?"
        simon.name "Nothing too big. Just his wife looking for dirt on him so is paying me to find it."
        pc "Well, by the sounds of it, he never leaves this place."
        simon.name "I know. That's why I am stuck here every evening as well. Tried asking his workmates about him but no one wants to answer. He works in the hospital over there."
        pc "The hospital? He's a doctor?"
        simon.name "No, some low level person who does paperwork."
        pc "Ok, so why is everyone tight lipped?"
        simon.name "You don't know?"
        pc "Know what?"
        simon.name "The upper management of the hospital basically run all of [town]. Anyone asking questions, or answering, can draw unwanted attention."
        $ player.face_worried()
        pc "Oh? Hope you haven't got me in trouble or something."
        simon.name "Doubt it. I couldn't care about the hospital, just the man over there who happens to work there. I'd rather not poke my nose in the business of big shots."
        $ player.face_neutral()
        simon.name "Your turn. What did you find out?"
        pc "Dunno if it's something worth anything. But he is mostly just what you see. Comes here every night after work, drinks and ogles the girls."
        pc "Not really a lot else to it."
        simon.name "He ever do something his wife would be upset about?"
        pcm "Hmmm, what should I say?"
        menu:
            "Tell the truth":
                $ add_to_list(main_quest_01.list, "waitress_branch_truth")
                pc "If he can afford it, but that's rare. Looks like he has taken a liking to one of us and sticks close to her while the place is empty."
                simon.name "Oh? Just so I am clear and no mistakes. He pays for sex with her?"
                pc "Yeah, when he can afford it. Which isn't often according to her."
                simon.name "Excellent. Means I'm not wasting my time here. Just need to hold out until I can get some photos of them. Guess I'll try and find out when he gets paid and come back then."
                $ player.face_annoyed()
                pc "Hey, photos? Don't be getting the girls in trouble."
                simon.name "Not interested in the girls. Don't worry. I won't be spreading anything about them."
                $ player.face_neutral()
                pc "Good."
            "Tell a lie":
                pc "He seems to have a soft spot for one of the girls, but who here hasn't. Not sure about anything indecent."
                simon.name "Ah well. Suppose I will monitor things more and let the wife decide on that."
        simon.name "Thanks for the help, looks like I don't need to waste as much time here thanks to you."
        pc "Sure. Glad to help."
        simon.name "Y'know, in my line of work I could do with someone like you."
        pc "Yeah, bet you say that to all the girls. What is your line of work anyway? P.I.?"
        simon.name "Pretty much. People pay me to do stuff for them or get information. Pretty girl like you would loosen a lot of tongues."
        pc "Sure. Offer money and I'll consider it."
        simon.name "Actually, it's not much but you saved me time. So here is something."
        $ player.add_money(25)
        pc "Thanks."
        simon.name "Well, I'm going to call it a night. Thanks again."
        pc "Mmm, see ya."
        hide pub_serve_talking with dissolve
        if "waitress_branch_truth" in main_quest_01.list:
            simon.name "Err, come to think of it. Hold on."
            show pub_serve_talking with dissolve
            pc "Mmm."
            simon.name "If he does have a thing for the girls, you could help me out."
            if player.check_speech(3, notif=False) and player.check_sex_agree(2, notif=False):
                pc "Ugh, I can already see where this is going."
                simon.name "Yup. Interested?"
                pc "What is it you need?"
            else:

                pc "How so?"
            simon.name "I'll give you £50 if you can get me steamy photos. Groping and generally something his wife won't like. And for you, him and his cock in one photo I'll give you £150."
            simon.name "£150 for you, him and his cock in one photo."
            pc "Wow."
            simon.name "So? Interested?"
            $ player.soldrequest = "naughty"
            if player.check_whore():
                pc "Hmmm..."
                menu:
                    "Agree":
                        pc "£50 for steamy photos and £150 for his cock?"
                        simon.name "Yup."
                        pc "Right..."
                        pc "Okay then."
                        simon.name "Yeah?"
                        pc "How you going to get the photos though? Not seen a working camera since... Well..."
                        simon.name "I got my hands on a refurbished camera phone. Cost an absolute fortune but is pretty much what keeps food on my table. Digital photos are hard to argue against."
                        pc "That's him over there?"
                        simon.name "Yeah."
                        pc "Not horrible looking at least. He on his own or those people his friends?"
                        simon.name "On his own. Busy here so people share tables."
                        pc "Right. I'll see what I can do..."
                        hide pub_serve_talking with dissolve
                        pcm "Hmmm..."
                        jump main_quest_01_reporter_intro_bob_picker
                    "Refuse":
                        $ NullAction()

            pc "No thanks, not really my thing. You're on your own there."
            simon.name "No worries, think I could convince one of the other girls?"
            if pub_waitress.sold > 2:
                pc "For £150? Definitely."
            else:
                pc "Not sure. That's a fair amount of money so maybe."
            simon.name "Well, thanks anyway."
            pc "See ya."
            hide pub_serve_talking with dissolve

        pcm "Well that went well. Guess people will say anything to a barmaid."
        pcm "Tell [tucker.name] the good news I suppose."
        $ walk(loc_pub_changingroom)
        pause 0.5
        $ pc_strip()
        pause 0.5
        $ pc_dress_slow(pub_waitress.clothes)

        $ main_quest_01.missionvar1 = True
        $ main_quest_01.stage = 2
        $ log.markdone("mq_01_b")
        $ walk(loc_pub)

        jump travel
    else:

        $ add_to_list(main_quest_01.list, "waitress_branch_fail_convince")
        simon.name "Doubt you can help me out. Sorry."
        pc "Sure?"
        simon.name "Yeah, don't worry about it. I'll deal with this on my own."
        pc "Hmm. Well, I'm here if you need me."
        simon.name "Sure."
        hide pub_serve_talking with dissolve
        pcm "Damn, still not much the wiser. But if I push him more he will know something is up..."
        pcm "Hmm, what can I do?"
        pcm "Maybe just drink a beer and go up to him a bit later, see if he changed his mind."
        $ player.add_perk(perk_drinking_beer_2)
        pcm "He is clearly after something. He isn't coming here just to drink and wound up on The Institutes radar by mistake."
        pcm "Seems to be mostly watching over there. But so many people that I can't really see who."
        pcm "Good chance I guess that most of them work at the hospital, but I am not really familiar with any of them."
        pcm "Don't really know anyone from the hospital come to think of it..."
        "I stand there trying to look inconspicuous, although that's not really easy considering I am wearing a bar girl outfit and keep having patrons come up to me."
        $ player.drink_current()
        "I just slowly drink my beer while killing time."
        $ relax(30)
        $ player.drink_current()
        pcm "Ugh, going to be in here forever at this rate. I should just bite the bullet and chat with him."
        show pub_serve_talking with dissolve
        pc "Still here nursing that drink?"
        simon.name "Mmmm."
        pc "Want another?"
        simon.name "Do you really work here?"
        pcm "Fuck!"
        pc "Silly question. Think I just hang out here with all the perverts while wearing this for fashion?"
        simon.name "Since you left, you have mostly hung around over there and not served any customers. Seem more interested in what I am doing."
        pc "What can I say. A mix of boredom and curiosity."
        simon.name "Or someone paid you to watch me. The Institute I would guess."
        menu:
            "Be coy":
                pc "Who are The Institute?"
                simon.name "If you're gonna play like that, I think I'm done for the night. Have a good night... Miss...?"
                pc "Err, [fname]."
                simon.name "I'll see you around [fname]."
                $ renpy.scene()
                with dissolve
                pc "Damn. That went pretty poorly."
                pc "Oh well. I suppose I will have to go and tell [tucker.name] what happened."
                $ main_quest_01.stage = 2
                $ log.markdone("mq_01_b")
                $ walk(loc_revel)
                jump travel
            "Tell the truth":

                pc "Girls got to earn."
                simon.name "Not just the girls. What do you want?"
                jump main_quest_01_reporter_intro_simon_truth





label main_quest_01_reporter_intimidate_branch:
    pcm "The Institute is a pretty powerful group so maybe putting some fear into him would do the job."
    pcm "Am I up to the task though? Don't really look all big and scary..."
    pcm "Will have to leverage the clout of The Institute I suppose."
    show simon at right1 with dissolve
    "I don't say anything to him and just take a seat beside him."
    simon.name "Err, can I help you?"
    pc "Doubt it. Can I help you?"
    simon.name "Not looking for what you're offering, sorry."
    pc "Asking a lot of questions for someone not looking for anything."
    simon.name "Ah! The Institute sent you? Took longer than expected."
    pc "Took a while to decide how to approach the situation."
    simon.name "Usually money does the trick."
    pc "Mmm. But who to pay."
    simon.name "Huh?"
    pc "Pay you to go away or pay someone to make you go away. First one is cheaper but the second one is permanent."
    simon.name "What? You threatening me?"
    pc "Not really. It's why I am here and not someone more scary."
    pc "I'm here to smile at you and ask you why you are poking your nose about in places you shouldn't."
    simon.name "Didn't think The Institute would care that much."
    pc "Maybe they don't. Problem is, we don't know what you are up to."
    pc "Depending on what you are after, maybe we give it to you, maybe we help you get it, maybe we ignore you. Or maybe..."
    simon.name "..."
    pc "So..."
    pc "What you up to?"
    if player.check_speech(5):
        $ add_to_list(main_quest_01.list, "intimidate_branch_pass_intimidate")
        simon.name "*Sigh* Thought if I played it close to the chest, I might be able to squeeze some money off the guys at the top."
        simon.name "Look, I don't care about The Institute. I am being paid by Bob's wife to dig up dirt. He works at the hospital so I need to ask around."
        pc "Bob?"
        simon.name "Him over there. He's a nobody. Just happens to work at the hospital so is close to The Institute."
        pc "Found out anything?"
        simon.name "Other than him being a drunk, nothing worth my time. It's why I thought I might try to squeeze something extra off of you."
        pc "Played it too close to the chest by the look of things."
        simon.name "Looks like it."
        pc "Well, thanks for the info. I'll take it back to the powers that be."
        simon.name "Right."
        if player.allure > 100:
            simon.name "Wait, hold on."
            pc "Mmmm."
            simon.name "So... You are obviously a professional, despite how you look. Or probably that helps. Sweet on the outside and tough inside."
            pc "I'll take that as a compliment."
            simon.name "So how about I pay you to help me get this all over and done with. I get what I want from Bob and no need to be around any more. No more poking around near The Institute."
            pc "Ok, what do you need and how much you paying?"
            simon.name "I'll pay £150. And what I need are incriminating photos of you and him together."
            pc "How \"together\"?"
            simon.name "You, him and his cock in one shot. Can show his wife he's been up to no good and close this case. Job done and I'm gone."
            if not player.check_whore():
                pc "Hah, you're on your own there mate."
                simon.name "Right. Sorry."
                pc "See you round."
                jump main_quest_01_reporter_intimidate_branch_end
            else:
                pc "£150?"
                simon.name "I have it with me. Moment I get that shot it's yours."
                menu:
                    "Agree":
                        $ add_to_list(main_quest_01.list, "intimidate_branch_agree_bobsex")
                        pc "That's him over there?"
                        simon.name "Yeah."
                        pc "Not horrible looking at least. He on his own or those people his friends?"
                        simon.name "On his own. Busy here so people share tables."
                        pc "Ok, then, money up front."
                        simon.name "What? How do I know you will get the job done."
                        if simon.sex:
                            pc "You're asking that after just fucking me and giving me everything I asked for?"
                            simon.name "Err... True."
                        elif player.allure > 100:
                            pc "You want to fuck me?"
                            simon.name "Err, wouldn't say no."
                            pc "Nor will he."
                        elif "school" in tab_top:
                            pc "Think anyone here is going to turn down a school girl?"
                            simon.name "..."
                            simon.name "No..."
                        elif player.pregnancy >= 2:
                            pc "People here have a thing for pregnant girls. We are seen as easy prey."
                            simon.name "Right..."
                        else:
                            pc "Doubting me now? Already got the job done with you, I'll get it done with him as well."
                            simon.name "..."
                        pc "So, pay up."
                        simon.name "Ok. Here."
                        $ player.add_money(150)
                        $ add_to_list(main_quest_01.list, "paid")
                        pc "No need to wait around after. Just get the photos and job done."
                        simon.name "Okay. Hope you are as good as you think you are."
                        pc "You'll see."
                        hide simon with dissolve
                        jump main_quest_01_reporter_intro_bob_picker
                    "Refuse":

                        pc "Tempting, but sorry mate, you're on your own here."
                        simon.name "Right. Thanks anyway."
                        pc "See you round."
                        jump main_quest_01_reporter_intimidate_branch_end
    else:

        $ add_to_list(main_quest_01.list, "intimidate_branch_fail_intimidate")
        if player.allure > 100:
            simon.name "Yeah right. We both know your bosses didn't send you here to act tough."
            simon.name "Pretty sure you were sent here to get more hands on in another way."
            pc "I was sent here to be nice and convince you instead of sending a goon."
            simon.name "Yup. So how about you stick to being nice."
            $ player.face_sus()
            pc "You trying to get at something?"
            simon.name "I am. I can tell you everything you are after no problem. But I want something sweeter than threats in return."
            $ player.face_frown()
            pc "And what do you want?"
            simon.name "Had you come here a bit nicer, I might have been open to negotiation..."
            simon.name "But since you came with threats..."
            pc "Spit it out."
            simon.name "I want to see a girl like you in her place."
            simon.name "Bent over being fucked."
            $ player.face_worried()
            pc "*Sigh*"
            pc "Got a big ego there."
            simon.name "Not really. It's you that came here with the attitude. Let's have a little fun and all is forgiven."
            pcm "Fuck."
            pcm "What a cunt..."
            pcm "Well, was me being the cunt in the first place. But still..."
            pcm "So either I fuck him or he leaves. Shit."
            if player.check_sex_agree_choice(4, "Let him have his way.", "No chance."):
                $ add_to_list(main_quest_01.list, "intimidate_branch_fail_sex")
                $ player.face_annoyed()
                pc "You arse."
                simon.name "That a yes?"
                $ player.face_frown()
                pc "Ugh... Follow me."
                hide simon with dissolve
                if pub_waitress.timesworked > 4:
                    $ walk(loc_pub_changingroom)
                    with dissolve
                    pcm "No one here."
                    "I wave at [simon.name] to come in."
                    show simon at right1 with dissolve
                    simon.name "Err, are we allowed back here?"
                    pc "It's fine. I work here so no one will bother us."
                else:
                    $ walk(loc_pub_toilet_girls)
                    with dissolve
                    pcm "No one here."
                    "I wave at [simon.name] to come in."
                    show simon at right1 with dissolve
                    simon.name "Err, you sure?"
                    pc "You see any women in the pub other than me?"
                    simon.name "Not many."
                    pc "So no one will bother us here."
                simon.name "Right then..."
                jump main_quest_01_reporter_sex_branch_sex
            else:
                pc "Not happening."
                simon.name "Then I'll take my chances."
                $ renpy.scene()
                with dissolve
                pc "..."
                pc "Damn. That failed horribly. Well at least that was the plan."
                pc "Oh well. I suppose I will have to go and tell [tucker.name] what happened."
                $ main_quest_01.stage = 2
                $ log.markdone("mq_01_b")
                jump travel
        else:

            simon.name "Sorry darling, I'll take my chances."
            $ renpy.scene()
            with dissolve
            pc "..."
            pc "Damn. That failed horribly. Well at least that was the plan."
            pc "Oh well. I suppose I will have to go and tell [tucker.name] what happened."
            $ main_quest_01.stage = 2
            $ log.markdone("mq_01_b")
            jump travel


label main_quest_01_reporter_intimidate_branch_end:
    hide simon with dissolve
    $ walk(loc_revel)
    pcm "Wow!"
    pcm "That was a bit scary."
    pcm "Worked though!"
    pcm "So, doesn't care about The Institute and just poking around Bob because of his wife."
    pcm "Pretty boring stuff in the end."
    if "stole_money" in main_quest_01.list:
        pcm "At least I was able to come out of it richer without actually doing anything for it."
        pcm "Seemed a decent guy, shame to stiff him like that."
        pcm "Oh well, he would have done the same to me given the chance."
    pcm "Well, better tell [tucker.name]"
    $ main_quest_01.missionvar1 = True
    $ main_quest_01.stage = 2
    $ log.markdone("mq_01_b")
    jump travel





label main_quest_01_reporter_intro_busted:
    pc "Damn, first thing I say and I'm already busted."
    simon.name "Well, no one these days speaks to someone like me in a pub. Especially not pretty young girls like you."
    simon.name "So... What do you want?"
    pc "I want to know why you are trying to squeeze info from Institute employees."
    $ player.drink_current()
    simon.name "Sorry love, but that's my business and none of yours. Now if you don't mind, I think I'll take this as a cue to be leaving."
    $ renpy.scene()
    with dissolve
    pc "..."
    pc "Damn. That failed horribly. Well at least that was the plan."
    pc "Oh well. I suppose I will have to go and tell [tucker.name] what happened."
    $ main_quest_01.stage = 2
    $ log.markdone("mq_01_b")
    $ walk(loc_revel)
    jump travel

label main_quest_01_reporter_intro_rejectsex:
    pcm "Hmm, I would rather not be messing about with him like that."
    pc "Sorry mate, but I'm not willing to pay that price."
    simon.name "No? Thought that was the whole point in them sending you. And now you back out?"
    simon.name "Think I would give it up just from your pretty smile?"
    pc "I have a pretty smile?"
    simon.name "Err, well..."
    pc "Thanks."
    simon.name "Err..."
    simon.name "You're welcome."
    simon.name "..."
    simon.name "Well, I'm leaving now."
    pc "Aww. Not want to stay so I can try and convince you more?"
    simon.name "I'll take my chances with whoever they send next."
    pc "Ok, mind if I finish your beer?"
    simon.name "Go ahead."
    hide simon with dissolve
    jump main_quest_01_reporter_intro_rejectsex_catcher

label main_quest_01_reporter_intro_rejectsex_catcher:
    $ add_to_list(main_quest_01.list, "sex_branch_reject")
    if not player.drinking:
        $ player.add_perk(perk_drinking_beer_2)
    pcm "Could have just fucked him for the info..."
    pcm "Ugh, no idea why I didn't just pick the easy option."
    pcm "Oh well. Drink this up and head back to [tucker.name] and tell him the news."
    pcm "Didn't seem like such a bad guy though. Hope they don't end up killing him or something."
    $ player.drink_current()
    show simon at right1 with dissolve
    pc "Ah, you're back?"
    simon.name "Yeah..."
    simon.name "Here."
    pc "What's this?"
    simon.name "The info you wanted."
    pc "Oh? Thanks..."
    pc "Why?"
    simon.name "*Tsk*"
    simon.name "Your pretty smile worked."
    $ player.face_happy()
    pc "Oh? Thank you."
    simon.name "Yeah yeah. I'm going before I change my mind."
    hide simon with dissolve
    pc "Bye..."
    pcm "Well..."
    pcm "That was a surprise."
    pcm "Have to smile more instead of bending over."
    pcm "Heh."
    $ player.drink_current()
    pcm "Well, good news for [tucker.name]."
    $ main_quest_01.missionvar1 = True
    $ main_quest_01.stage = 2
    $ log.markdone("mq_01_b")
    jump travel

label main_quest_01_reporter_bobsex_leadup:
    pc "That's him over there?"
    simon.name "Yeah."
    pc "Not horrible looking at least. He on his own or those people his friends?"
    simon.name "On his own. Busy here so people share tables."
    pc "Ok, then, money up front."
    simon.name "What? How do I know you will get the job done."
    if simon.sex:
        pc "You're asking that after just fucking me and giving me everything I asked for?"
        simon.name "Err... True."
    elif player.allure > 100:
        pc "You want to fuck me?"
        simon.name "Err, wouldn't say no."
        pc "Nor will he."
    elif "school" in tab_top:
        pc "Think anyone here is going to turn down a school girl?"
        simon.name "..."
        simon.name "No..."
    elif player.pregnancy >= 2:
        pc "People here have a thing for pregnant girls. We are seen as easy prey."
        simon.name "Right..."
    else:
        pc "Doubting me now? Already got the job done with you, I'll get it done with him as well."
        simon.name "..."
    pc "So, pay up."
    simon.name "Ok. Here."
    $ player.add_money(150)
    $ add_to_list(main_quest_01.list, "paid")
    pc "Right, see you after the job is done."
    simon.name "Okay. Hope you are as good as you think you are."
    pc "You'll see."
    hide simon with dissolve


    jump main_quest_01_reporter_intro_bob_picker





label main_quest_01_reporter_intro_drink:
    pc "I'm not sure what else I can do so I suppose I'll sit near him and hope something comes up."
    show trixie at right3 with dissolve
    trixie.name "Hey sweetie. What can I get you?"
    pc "Erm, a beer please."
    trixie.name "Sure thing. Any particular brand you want?"
    pc "Just something that isn't strong."
    trixie.name "No problem, here you go darlin'. Need anything else, give me a wave."
    $ player.add_perk(perk_drinking_beer_2)
    pc "Thanks."
    hide trixie with dissolve
    pc "..."
    pc "Ok. Now I am here. What do I do?"
    $ player.drink_current()
    menu:
        "Go and speak to him.":
            pc "Hmm, ok. Let's see how this goes."
            show simon at right1 with dissolve
            pc "Hey, how about you buy me a drink?"
            simon.name "Hmm. Took longer than I expected."
            pc "Huh?"
            simon.name "Sent by The Institute?"
            jump main_quest_01_reporter_intro_busted
        "Wait for an opportunity":

            pc "Suppose I will wait and keep an eye on him. I don't really have a clue what I am up to so I think I will just wait."
            pc "He doesn't seem to be doing anything. Just sitting and drinking."
            pc "..."
            $ relax (26)
            $ player.drink_current()
            pc "Still nothing. Almost half an hour gone and he's just drinking. No attempt whatsoever to talk to other people. Does he know I am watching him?"

    show bob at right1 with dissolve
    drunk "Hey sweetheart. How about you join me for a drink? Promise I don't bite."
    pc "(Ugh, this guy is wasted.)"
    pc "No thanks. I would rather be on my own."
    drunk "Aww c'mon darlin', live a little. Our country is in the crapper. Drinking away your worries is the only way to imagine a better life."
    pc "All the more reason to enjoy time alone."
    drunk "Here. Your glass is empty so lemme get you another drink."
    drunk "Two more beers over here."
    show trixie at right3 with dissolve
    trixie.name "Sure thing [bob.name]. Here you are."
    hide trixie with dissolve
    bob.name "Here love, this one's yours. So what's a young lass like you doing in here?"
    $ player.add_perk(perk_drinking_beer_2)
    menu:
        "Make up a reason.":
            $ temp_var_1 = True
            pc "I'm just relaxing after work."
            bob.name "You and me both then. Shame a wee lass like you has to be working and not off enjoying herself."
            pc "Mmmm"
            bob.name "Anyway, I can see you don't want company so I'll leave you and the beer to enjoy yourselves."
            pc "Err, sure. Thanks [bob.name]."
            bob.name "Sure. Come and have a chat if you change your mind."
            hide bob with dissolve
        "Try and get rid of him":

            $ temp_var_1 = False
            pc "Look [bob.name]. I'm just trying to relax alone. I don't want company."
            bob.name "Sure sure. Ok, well enjoy your beer. Come for a chat if you change your mind."
            pc "Sure. See you [bob.name]."
            hide bob with dissolve
            pc "..."
    $ player.drink_current()
    $ relax(15)
    pc "That was easier than I expected. Thought he would hang around no matter what I would say."
    pc "Now what do I do about [simon.fullname]? Still haven't found a way to talk to him."
    if t.hour == 23:
        pc "It's also so late that the barmaid has already rang for last orders. I need to make a move now or it will be too late."
        pc "Hmmm..."
        $ player.drink_current()
        pc "Ok. Let's see how this goes."
        show simon at right1 with dissolve
        pc "Hey, how about you buy me a drink?"
        simon.name "Hmm. Took longer than I expected."
        pc "Huh?"
        simon.name "Sent by The Institute?"
        jump main_quest_01_reporter_intro_busted
    else:
        menu:
            "I need to go and speak to him.":
                pc "Hmmm..."
                $ player.drink_current()
                pc "Ok. Let's see how this goes."
                show simon at right1 with dissolve
                pc "Hey, how about you buy me a drink?"
                simon.name "Hmm. Took longer than I expected."
                pc "Huh?"
                simon.name "Sent by The Institute?"
                jump main_quest_01_reporter_intro_busted
            "Keep waiting for a chance.":


                pc "I suppose I'll just wait it out some more."

    pc "[tucker.name] was right though. I really do need experience since I haven't got the slightest idea what to do here."
    pc "I don't really have anything you could call \"feminine charm\" so can't use that. Talking to random guys in a pub isn't something I am so familiar with."
    $ player.drink_current()
    if player.male_origin:
        pc "And if a girl did that to me before then I would think they were eager. That or she was a whore."
    else:
        pc "Walking up to a guy and just starting a conversation. In my past life that was basically saying \"I want sex\" and I can't see that being any different now."
    pc "Well, I guess this \"Mission\" at least shows how inadequate I am at this. Damn that [tucker.name] always being right."
    show trixie at right3 with dissolve
    trixie.name "Another beer hon? Looks like you need it."
    pc "Yeah sure. Thanks."
    trixie.name "Here you go. Don't drown too much of your sorrows in this place now ya hear?"
    $ player.add_perk(perk_drinking_beer_2)
    pc "Yeah..."
    hide trixie with dissolve
    $ player.drink_current()
    "I spend the next hour or so waiting for my chance to get close to [simon.name]."
    $ player.drink_current()
    $ player.add_perk(perk_drinking_beer_2)
    $ relax(60)
    $ player.drink_current()
    if t.hour == 23:
        pc "It's so late that the barmaid has already rang for last orders and I haven't made any progress. I need to make a move now or it will be too late."
        pc "Hmmm..."
        pc "Ok. Let's see how this goes."
        show simon at right1 with dissolve
        pc "Hey, how about you buy me a drink?"
        simon.name "Hmm. Took longer than I expected."
        pc "Huh?"
        simon.name "Sent by The Institute?"
        jump main_quest_01_reporter_intro_busted
    else:
        jump main_quest_01_reporter_intro_simon_approach

label main_quest_01_reporter_intro_simon_approach:
    pc "This is going nowhere. [simon.name] is just sitting there like everyone else. No attempt to speak to anyone else. Just sitting drinking whatever that is he's drinking."
    pc "Could [tucker.name] have been wrong for once? Maybe this guy isn't doing anything."
    pc "..."
    pc "Huh, could that be the point. He is nobody and [tucker.name] is just seeing what I do?"
    show trixie at right3 with dissolve
    trixie.name "Another one hon?"
    pc "Yeah why not?"
    trixie.name "Thought so. Here you are."
    $ player.add_perk(perk_drinking_beer_2)
    hide trixie with dissolve
    pc "Right... I'll drink this up and if nothing comes up I'll just bite the bullet and go over to talk to him."
    pc "No reason to be sitting here all night scratching my arse. Although a least it's in a pub where I can drink some beer and not out in the cold or something."
    pc "First time being in a pub since the accident actually. A lot of gloomy faces all over the place."
    if t.wkday in ("Friday", "Saturday"):
        pc "Crazy busy in here as well. People drowning their sorrows after the weeks work I suppose so I don't really blame them. A lot more women in here than I expected as well."
    else:
        pc "A lot more busy than I thought it would be for a working day. People don't have much else to do in this shithole life anymore I suppose so I don't really blame them. A lot more women in here than I expected as well."
    $ player.drink_current()
    pc "I thought I would be harassed a lot more than I have been considering it's a pub and I'm alone. But things have been pretty peaceful."
    pc "Ahh. Now that I finally look around, I see why. Looks like some of the women are prostitutes. The sleazy guys are probably aiming at them instead."
    pc "..."
    $ player.drink_current()
    pc "Ok, It's about time I went and spoke to [simon.fullname]."
    pc "Welp. Here goes nothing..."
    show trixie at right3 with dissolve
    trixie.name "Here you go hon. A drink from the man at the end there."
    pc "Err, who? Ahh. It's [simon.fullname]..."
    pc "Thanks."
    $ player.add_perk(perk_drinking_beer_2)
    trixie.name "I didn't buy it for you. He's the one to thank. Enjoy."
    hide trixie with dissolve
    pc "Ok... Well I suppose that's as good a signal as any to go and speak to him."
    show simon at right1 with dissolve
    pc "Err. Hi. Thanks for the drink."
    show simon smile
    simon.name "No problem. Looks like you need it."
    pc "You're telling me."
    simon.name "Want to sit here?"
    pc "Sure."
    $ player.drink_current()
    show simon frown
    simon.name "So they really put you in the deep end didn't they?"
    pc "Huh, what do you mean?"
    simon.name "No need to be coy. I saw you as soon as you came in. Hard to not notice a pretty face like yours. You came in and looked around, saw me then came over and sat nearby."
    simon.name "But then you didn't really have a clue what to do from there. I should be upset that The Institute sent someone as green as you are. But I don't suppose it really matters."
    simon.name "So tell me, what do you want from me?"
    $ player.drink_current()
    menu:
        "Be coy.":
            pc "What are you talking about? Of course I looked around. How else will I find an empty seat?"
            simon.name "If you say so. Well ok. Enjoy your drink, I think I'm done for the night. Have a good night... Miss...?"
            pc "Err, [fname]."
            simon.name "I'll see you around [fname]."
            $ renpy.scene()
            with dissolve
            pc "Damn. That went pretty poorly."
            pc "Oh well. I suppose I will have to go and tell [tucker.name] what happened."
            pc "Probably best to sleep off this booze first though. This small body doesn't seem to handle it too well."
            $ main_quest_01.stage = 2
            $ log.markdone("mq_01_b")
            $ walk(loc_revel)
            jump travel
        "Tell the truth":

            jump main_quest_01_reporter_intro_simon_truth

label main_quest_01_reporter_intro_simon_truth:
    pc "I want to know why you are trying to squeeze info off people who work at The Institute."
    simon.name "Ok. And what do you plan on giving me in return... Miss?"
    pc "So it is just blackmail is it? Well what you get depends on what you know. And my name is [fname]."
    simon.name "I wasn't born yesterday love. I'm not about to give up the only thing of value I have. Make me an offer and I will consider it."
    pc "I can't make an offer without knowing what you have. Not to mention I don't have anything to offer you. I'll have to speak to the people in charge."
    simon.name "Two more please barmaid."
    show trixie at right3 with dissolve
    trixie.name "Sure thing hon, here you go."
    hide trixie with dissolve
    simon.name "Here you go. Now, let's talk."
    $ player.add_perk(perk_drinking_beer_2)
    simon.name "The Institute sent you here to find out what I know and to silence me right?"
    pc "..."
    $ player.drink_current()
    simon.name "I'll take that as a yes. And I am fine with that. For the right offer I am happy to give up what I know and go away quietly."
    pc "Ok, but I don't have anything to offer you. I need to speak to the people in charge first. But to do that I need to know what you have."
    simon.name "Well if you want to leave here with what I know then lets talk about what you can offer."
    pc "How many times do I need to say it. I have nothing to offer. I wasn't given any money to bribe you. I am here just to find out what you know."
    $ player.drink_current()
    jump main_quest_01_reporter_intro_simon_game_offer





label main_quest_01_reporter_intro_simon_game_offer:
    simon.name "Hmm, tell you what. From a pretty little thing like you I am willing to look at alternate deals."
    pc "Ugh, such as?"
    simon.name "Let's go outside where there are not so many people and play a game?"
    pc "..."
    pc "And tell me, what is this game?"
    simon.name "You can ask me any question you like and I will answer it with absolute truth. But in return you have to do what I say. Every question must be paid for."
    pc "And dare I ask what kind of payment you want?"
    simon.name "Hmm, let's settle for one question costs one piece of clothing."
    pc "You want me to strip naked for you?"
    if player.has_perk(perk_exhibitionist):
        $ show_notif_popup("Exhibitionist")
        pc "Sure, why not?"
        jump main_quest_01_reporter_intro_simon_game_offer_agree
    simon.name "Naked? Well that's up to you. Are you able to ask the right questions and get the info you want before you are naked?"
    pc "..."
    simon.name "So... Want to play?"
    if sum([bool(c.pants), bool(c.bra), bool(c.top), bool(c.bottom), bool(c.outfit)]) < 3:
        if c.outfit and not c.pants and not c.bra:
            pcm "Moment I take this off I will be standing there butt naked."
        elif not c.bra and not c.pants:
            pcm "I am not wearing any underwear. I will be naked in no time."
        else:
            pcm "I am barely wearing anything so I'll be naked in no time."
    elif player.check_speech(2, notif=False):
        pcm "Hmm, if it were as simple as asking why he's investigating The Institute, he wouldn't be so eager. There must be something else to it."
    else:
        pcm "Hmm, should just be a case of asking why he's investigating The Institute and job done, right?"

    if player.check_sex_agree(If(sum([bool(c.pants), bool(c.bra), bool(c.top), bool(c.bottom), bool(c.outfit)]) < 3, 4, 2)):
        menu:
            "Agree to play":
                jump main_quest_01_reporter_intro_simon_game_offer_agree

            "Negotiate and offer to help him with his work" if "work" in tab_top:
                jump main_quest_01_reporter_intro_simon_game_offer_negotiate
            "Refuse to play":

                jump main_quest_01_reporter_intro_simon_game_offer_reject
    else:

        jump main_quest_01_reporter_intro_simon_game_offer_reject

label main_quest_01_reporter_intro_simon_game_offer_agree:
    pc "Ok, let's get this over with."
    if renpy.showing("pub_serve_talking"):
        $ renpy.scene()
        show simon smile at right1
        with dissolve
    show simon smile
    simon.name "Great, then come along sweetheart. Let's go somewhere more private."
    pc "Try anything funny and I'll poke your eyes out."
    simon.name "Don't worry pet, I will be a perfect gentleman."
    pc "Yeah, while trying to strip me?"
    simon.name "Yup. I won't do anything you don't agree to."
    pc "I'll hold you to that."
    jump main_quest_01_reporter_game_start

label main_quest_01_reporter_intro_simon_game_offer_reject:
    pc "No, I won't play with you."
    simon.name "As you wish. Good luck in your investigation. I'll see you around [fname]."
    $ renpy.scene()
    with dissolve
    pc "Damn. That went pretty poorly."
    pc "Oh well. I suppose I will have to go and tell [tucker.name] what happened."
    pc "Probably best to sleep off this booze first though. This small body doesn't seem to handle it too well."

    $ main_quest_01.stage = 2
    $ log.markdone("mq_01_b")
    $ walk(loc_revel)
    jump travel

label main_quest_01_reporter_intro_simon_game_offer_negotiate:
    $ add_to_list(main_quest_01.list, "bob_mission_accepted")
    pc "Hold on, you are here for a reason. We can help each other out here."
    simon.name "Hmmm..."
    pc "You are coming here for a reason and obviously you haven't got what you wanted. We are both here being paid to do a job."
    simon.name "Err. I suppose."
    pc "So, I can help you get what you want, you tell me what I want. Win win."
    simon.name "Good idea I guess. But are you up for it?"
    pc "Depends. What does it involve?"
    simon.name "Involves a pretty young barmaid getting very close to someone."
    pc "How close?"
    simon.name "Depends on you. Some lap sitting, groping, that kind of thing. I can sneak some photos and in return I'll give you what you want."
    pc "Photos? Where the hell you get a camera from?"
    simon.name "A shitty old camera phone that I paid an absolute fortune for. It's what keeps me in a job. Hard evidence is hard to come by without photos."
    simon.name "So let me take some steamy photos and we are good."
    simon.name "But..."
    pc "Why do I know I'm not going to like this."
    simon.name "Get me a smoking gun photo and I'll pay you, say... £150?"
    pc "And the smoking gun is?"
    simon.name "You, him and his cock in one photo."
    simon.name "Steamy photos will probably do the job though, so up to you."
    pc "*Sigh*"
    pc "So who is it you are looking to stitch up?"
    simon.name "So you agree?"
    pc "Better than stripping for you in an alleyway."
    simon.name "Great. Bob, him over there. His wife is looking for dirt. Get me these photos and we both leave here with our pockets full."
    pcm "He doesn't seem too bad I guess."
    pc "Right. I'll be back."
    hide pub_serve_talking with dissolve
    pcm "Ok, so..."
    if player.check_speech(3):
        pcm "Hold on..."
        pcm "He pretty much already told me what he's up to."
        pcm "I could just leave and be done with all this."
        menu:
            "Leave now":
                pcm "Yeah, should just go instead of messing about with Bob."
                $ walk(loc_pub_changingroom)
                pause 0.5
                $ pc_strip()
                pause 0.5
                $ pc_dress_slow(pub_waitress.clothes)

                $ main_quest_01.missionvar1 = True
                $ main_quest_01.stage = 2
                $ log.markdone("mq_01_b")

                $ walk(loc_pub)
                pause 0.5
                $ walk(loc_revel)
            "Go up to Bob":
                pcm "I shouldn't just ditch the job."

    jump main_quest_01_reporter_intro_bob_waitress
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
