



label robin_talk_pub_chain_0:
    $ robin.dict["robin_talk_pub_chain"] += 1
    pc "Ended up going to the pub on Revel for work."
    robin.name "Oh? Seen that place but didn't go in. Not my type of place."
    pc "Probably for the best."
    robin.name "I would ask \"perverts everywhere?\" but we both know the answer to that already."
    pc "Haha yeah."
    jump robin_talk_end

label robin_talk_pub_chain_1:
    $ robin.dict["robin_talk_pub_chain"] += 1
    robin.name "So how bad is the pub?"
    pc "Not that bad actually. Most people there are working and just getting drunk before heading home for the night."
    robin.name "Really? Would have thought with the booze flowing it would have been worse."
    pc "Not really. Most people behave themselves there."
    jump robin_talk_end

label robin_talk_pub_chain_2:
    $ robin.dict["robin_talk_pub_chain"] += 1
    robin.name "Most people behave themselves at the pub? Most people?"
    pc "Yeah. Get the odd perverted comment or wandering hands."
    robin.name "Hmm, guess it's to be expected."
    pc "Not really made any easier with the tiny uniform I have to wear."
    jump robin_talk_end

label robin_talk_pub_chain_3:
    $ robin.dict["robin_talk_pub_chain"] += 1
    robin.name "Tiny uniform at the pub?"
    pc "Yeah. A frilly dress that doesn't cover much of your top or bottom."
    robin.name "Can't you get a more decent one?"
    pc "It is purposely short. Gets us more tips apparently."
    jump robin_talk_end

label robin_talk_pub_chain_4:
    $ robin.dict["robin_talk_pub_chain"] += 1
    robin.name "Tips at the pub? They don't pay you proper money?"
    pc "No, everything is earned through tips. Won't earn a thing otherwise."
    robin.name "That... Kinda sounds shady."
    pc "I guess that's the point..."
    jump robin_talk_end

label robin_talk_pub_chain_5:
    $ robin.dict["robin_talk_pub_chain"] += 1
    robin.name "So only tips? Does that mean you have to... Y'know. Flirt and stuff with the people there."
    pc "Eh, somewhat. Flirting is not quite my thing but suppose that doesn't matter when your dress doesn't even cover your arse."
    if player.breasts > 1:
        robin.name "With your tits, I guess it doesn't cover much of those either."
        pc "Not really..."
    robin.name "Well, at least you can just focus on the work and not deal with them too much."
    pc "If only. Still a lot of lonely people there looking to chat."
    jump robin_talk_end

label robin_talk_pub_chain_6:
    $ robin.dict["robin_talk_pub_chain"] += 1
    robin.name "And the pub drunks tip better if you hang out and chat?"
    pc "Of course."
    robin.name "Sounds like the whole system is set up to make you do that."
    pc "Yeah, though isn't that the case everywhere?"
    robin.name "I guess... Haven't really looked into that kind of work. Everyone wants you to smile in pretty dresses."
    pc "Ha, you in a pretty dress. I'd like to see that."
    jump robin_talk_end

label robin_talk_pub_chain_7:
    $ robin.dict["robin_talk_pub_chain"] += 1
    robin.name "So how much does shaking your arse in the pub for drunks pay? It at least worth it?"
    pc "Dunno if it's worth it. It keeps me from starving at least. You interested?"
    robin.name "No... Think I would rather not wear a dress."
    pc "The dress is your problem? Not the drunks? All the wandering hands? Offers to whore?"
    robin.name "No, that other stuff is daily life no matter where you... Wait, whore?"
    pc "Yeah..."
    jump robin_talk_end

label robin_talk_pub_chain_8:
    $ robin.dict["robin_talk_pub_chain"] += 1
    robin.name "I... Didn't realise the pub was, y'know... A whorehouse?"
    pc "It's not. It's just a pub. Doesn't stop people from offering for some time alone though."
    robin.name "Oh..."
    robin.name "Err..."
    robin.name "Right. OK..."
    jump robin_talk_end

label robin_talk_pub_chain_9:
    $ robin.dict["robin_talk_pub_chain"] += 1
    robin.name "Err, the pub. Did you ever go alone with someone?"
    pc "..."
    robin.name "Sorry, I probably shouldn't ask..."
    pc "Ugh, it's fine. Just makes me realise how normal this shit has become."
    robin.name "Yeah... Half the girls in school are probably whores and no one thinks anything strange."
    pc "Half? Think that's too few considering how many are pregnant."
    if player.pregnancy >= 2 and robin.days_pregnant > (global_pregnancy_length * 0.3):
        robin.name "Err... Yeah... Says the two pregnant girls."
        pc "Haha!"
    elif player.pregnancy >= 2 or robin.days_pregnant > (global_pregnancy_length * 0.3):
        robin.name "Err... Yeah..."
    else:
        robin.name "Mmm, probably."
    jump robin_talk_end

label robin_talk_pub_chain_10:
    $ robin.dict["robin_talk_pub_chain"] += 1
    if not pub_waitress.sold:
        pc "But no, I haven't went alone with someone in the pub."
        robin.name "No?"
        pc "Don't sound too surprised!"
        robin.name "Eh, just thought people like us need to earn money and it's the best way to. So pretty much assume everyone has done it."
        if player.sold:
            pc "Err, I have... Just not at the pub."
        pc "What about you?"
        if robin.sold:
            robin.name "Rent doesn't pay itself."
            pc "."
        else:
            robin.name "No..."
            pc "You don't sound sure."
            robin.name "I haven't. But I ain't so stupid to think I won't. I'm broke and one missed payment from homelessness."
            pc "Yeah... Or worse from what I hear about our landlord..."
    else:
        pc "It's better than the tips they give."
        robin.name "..."
        pc "What?"
        robin.name "Tips..."
        pc "Oh shut up!"
        robin.name "Haha, was it just the tip?"
        pc "I know where you sleep. A quick and easy murder."
        if robin.sold:
            robin.name "Well, if it makes you feel any better, you aren't the only one. Rent doesn't pay itself."
            pc "Yeah, it doesn't."
        else:
            robin.name "If it makes you feel any better, I ain't so stupid to think I won't do such things. I'm broke and one missed payment from homelessness."
            pc "Yeah... Or worse from what I hear about our landlord..."

    jump robin_talk_end

label robin_talk_pub_chain_11:
    $ robin.dict["robin_talk_pub_chain"] += 1
    robin.name "Do you get any fun out of showing off in the bar?"
    pc "Strange question."
    robin.name "I just heard some people kinda do it on purpose. Things are pretty shit these days so get some fun where you can."
    if player.has_perk(perk_exhibitionist, notif=True):
        pc "Well, yeah I do. I like showing off as you probably know by now."
        if "soccer_pc_naked" in robin.list:
            robin.name "Well, yeah. But being naked with the boys is a bit different. They aren't going to rape you in the alleyway."
            pc "No, but whatever. I'll show off to anyone."
            robin.name "Haha."
        elif c.nude:
            robin.name "Err, yeah... Bit of a dumb topic to have with the naked girl..."
            pc "Yup!"
        else:
            robin.name "Yeah, just thought that out there working alone might... Reign you in?"
            pc "Nope, not happening."
            robin.name "Pervert!"
    elif player.has_perk([perk_bimbo, perk_slut, perk_whore], notif=True):
        pc "Like most things these days, gotta take what fun you can out of it."
        robin.name "Even people looking at your knickers."
        pc "You assume I wear any."
        robin.name "Err... You don't?"
        pc "Depends. Some perverts offer to buy them."
        robin.name "Wow! Okay then..."
    else:
        pc "Err, I guess I just got used to it."
        robin.name "Used to it?"
        pc "Yeah, it's not like I can stop it. People are perverts everywhere and my dress is tiny. After a bit working there you forget that people can even see."
        robin.name "So you go about flashing your arse without a care in the world?"
        pc "Pretty much."
    jump robin_talk_end

label robin_talk_pub_chain_12:
    $ robin.dict["robin_talk_pub_chain"] += 1
    robin.name "Tempted to come to the pub just to watch you flash your arse."
    pc "Err, didn't think you were into girl's arses."
    robin.name "Oh, not really. More just to see you working and how it goes."
    pc "Want to see me make a fool of myself?"
    robin.name "No. Err, hard to say. Not sure..."
    jump robin_talk_end

label robin_talk_pub_chain_13:
    $ robin.dict["robin_talk_pub_chain"] += 1
    $ add_to_list(robin.list, "pc_suspect_likes_watching")
    robin.name "In the pub, it's not something I could do..."
    pc "But..."
    robin.name "Dunno. The idea of watching you do it is kinda..."
    pc "You get off on in?"
    robin.name "What! NO!"
    if "pc_suspect_likes_watching" in robin.list:
        $ add_to_list(robin.list, "pc_knows_likes_watching")
        pc "I knew it. You do get off on watching."
        robin.name "What? No."
        pc "Liar!"
    elif "pc_knows_likes_watching" in robin.list:
        pc "Ah, yeah you like to watch..."
        pc "Whatever. I don't care."
    elif "pc_know_want_bussex" in robin.list:
        pc "Yeah, says the girl who gets the bus to be felt up."
    else:
        pc "Tell that to someone who believes you."
    $ add_to_list(robin.list, "pc_suspect_likes_watching")
    jump robin_talk_end

label robin_talk_pub_chain_14:
    $ robin.dict["robin_talk_pub_chain"] += 1
    robin.name "Well, maybe the pub thing does..."
    pc "Well, not like you need to be invited. Pub is open to everyone."
    robin.name "Yeah, but going there alone drinking, won't they think I am a whore?"
    pc "Doubt it with the way you dress. Someone looking for a one nighter maybe."
    robin.name "Ha, not sure that's any better."
    jump robin_talk_end

label robin_talk_pub_chain_15:
    $ robin.dict["robin_talk_pub_chain"] += 1
    pc "With how busy the pub is, it's a fairly safe place. So doesn't matter what others think."
    robin.name "But won't people come up to me?"
    pc "Of course. And you just tell them \"No\"."
    pc "Or... Don't. Up to you."
    jump robin_talk_end





label robin_talk_bus_0:
    $ robin.dict["robin_talk_bus_chain"] += 1
    robin.name "I have a question."
    pc "Mmm?"
    show robin worried
    robin.name "It's... Err..."
    robin.name "Does getting the bus for you..."
    pc "Ah. Yeah. Hard to get off the bus without someone trying to do something."
    show robin happy
    robin.name "Ah, not just me then? Twice on the way to school someone has tried to put something up my skirt."
    pc "Yeah, sounds about normal."
    jump robin_talk_end

label robin_talk_bus_1:
    $ robin.dict["robin_talk_bus_chain"] += 1
    robin.name "Damn buses. Was just standing there and someone put their hand down the back of my trousers."
    pc "Oh?"
    robin.name "Yeah..."
    robin.name "This stuff happens to you as well right?"
    pc "Yeah, happens to everyone as far as I know. Heard a few people complain about it."
    robin.name "Yeah?"
    jump robin_talk_end

label robin_talk_bus_2:
    $ robin.dict["robin_talk_bus_chain"] += 1
    robin.name "So I was just standing on the bus and some guy was humping me the entire ride."
    pc "Yeah, happens. You not able to move away?"
    robin.name "Err. Should I?"
    pc "Well, Yeah? Shouldn't you?"
    robin.name "..."
    jump robin_talk_end

label robin_talk_bus_3:
    $ robin.dict["robin_talk_bus_chain"] += 1
    robin.name "How is the bus when you are wearing a skirt?"
    pc "Pretty sure you can imagine what it's like. Just got to make sure to wear knickers."
    pc "More trouble if they try to take them off."
    robin.name "Really? They do that?"
    pc "If you let them get away with it, they will probably fuck you right there in front of everyone."
    robin.name "Oh?"
    jump robin_talk_end

label robin_talk_bus_4:
    $ robin.dict["robin_talk_bus_chain"] += 1
    robin.name "Things ever go that far for you on the bus?"
    if busgroper.vvirgin:
        pc "Err... Yeah..."
        robin.name "Really?"
        pc "I got on the bus a virgin and got off... Not a virgin."
        robin.name "Oh wow!"
    elif busgroper.sex:
        pc "Err... Yes?"
        robin.name "Really?"
        pc "Yeah. Things ended up... Pokey..."
        robin.name "Oh?"
    elif busgroper.naughty:
        pc "Err, yeah. Lose clothes, groped, wanked on... Kinda like most people."
        robin.name "So you were never... Y'know..."
        pc "Fucked on the bus? No."
        robin.name "Oh."
    else:
        pc "Think I have got off lightly and not had much happen. Have heard of other girls though that ended up losing clothes and other stuff."
        robin.name "Yeah?"
        pc "Seems pretty common."
    jump robin_talk_end

label robin_talk_bus_5:
    $ robin.dict["robin_talk_bus_chain"] += 1
    if "soccer_hangout" in robin.list:
        robin.name "So I was on the bus the other day and was drunk from hanging with you lot at the field."
    else:
        robin.name "So I was on the bus the other day and had a bit to drink before..."
    pc "Bus and drunk. A recipe for... Well, ending up naked."
    robin.name "Yeah, pretty much."
    pc "Oh? That bad?"
    robin.name "Well, no. Sort of..."
    jump robin_talk_end

label robin_talk_bus_6:
    $ robin.dict["robin_talk_bus_chain"] += 1
    robin.name "The guy on the bus started groping me from behind. I was drunk and just stood there."
    pc "Yeah, doing that just makes them take it further."
    robin.name "He reached round the front and unbuttoned my trousers and started pulling them down."
    pc "And you still let him?"
    robin.name "Err... I just kinda stood there..."
    jump robin_talk_end

label robin_talk_bus_7:
    $ robin.dict["robin_talk_bus_chain"] += 1
    robin.name "The bus guy then tried to put it between my legs. But he was much taller than me so didn't have an angle."
    pc "Lucky?"
    robin.name "So just stood there while he groped my tits and humped between my legs."
    pc "Oh?"
    pcm "Is she getting off on this?"
    robin.name "Ended up getting home with his stuff in my knickers."
    jump robin_talk_end

label robin_talk_bus_8:
    $ robin.dict["robin_talk_bus_chain"] += 1
    pc "So been having any more fun on the bus?"
    robin.name "Err... Fun?"
    pc "Yeah?"
    robin.name "..."
    robin.name "Err... No?"
    pcm "She really does, doesn't she?"
    jump robin_talk_end

label robin_talk_bus_9:
    $ robin.dict["robin_talk_bus_chain"] += 1
    pc "Gonna end up poked if you let the bus guys do that they want."
    robin.name "You think?"
    pcm "Yup... She is doing it on purpose. I wonder..."
    pc "Well, I know some people probably like it."
    show robin happy
    robin.name "You like it?"
    pc "Wasn't saying me you idiot."
    show robin worried
    robin.name "Oh..."
    jump robin_talk_end

label robin_talk_bus_10:
    $ robin.dict["robin_talk_bus_chain"] += 1
    pc "Alright. Come on. Out with it. You and the bus."
    robin.name "Err..."
    pc "You keep talking about it and you don't sound upset in the slightest."
    robin.name "Err... I am upset."
    pc "Yeah right."
    jump robin_talk_end

label robin_talk_bus_11:
    $ robin.dict["robin_talk_bus_chain"] += 1
    robin.name "First time on the bus it happened, it was just weird. But then it kept happening."
    robin.name "I just ignored it at first because I just couldn't be bothered to kick up a fuss."
    robin.name "But then I just started to wonder how far they would go with it. So let them out of curiosity."
    pc "Yeah, curiosity. That's what you tell yourself eh?"
    robin.name "Well..."
    jump robin_talk_end

label robin_talk_bus_12:
    $ robin.dict["robin_talk_bus_chain"] += 1
    robin.name "Then that one guy on the bus tried pulling my trousers down."
    pc "Ah yeah, him."
    robin.name "I thought that was going way too far. So wanted to stop him."
    robin.name "But... I didn't. I just carried on standing there with my heart thumping in my chest."
    robin.name "Even when his dick was between my legs, I still just stood there."
    pc "Mmmm."
    jump robin_talk_end

label robin_talk_bus_13:
    $ robin.dict["robin_talk_bus_chain"] += 1
    robin.name "Wanna know the worst part about the bus guy?"
    pc "Sure."
    robin.name "My stop came and I needed to pull my trousers up to get off."
    pc "Yeah, had that happen before."
    robin.name "They were round my thighs so not very low. Could have pulled them up easily."
    robin.name "But I bent over to pull them up..."
    pc "Oh?"
    jump robin_talk_end

label robin_talk_bus_14:
    $ robin.dict["robin_talk_bus_chain"] += 1
    pc "So how far did you bend over for the bus guy?"
    robin.name "More than enough..."
    robin.name "And I took a long time doing it."
    robin.name "..."
    robin.name "I was disappointed he didn't... Y'know."
    pc "Didn't you say he left something in your knickers?"
    robin.name "Yeah, I didn't know at the time he was already finished."
    jump robin_talk_end

label robin_talk_bus_15:
    $ robin.dict["robin_talk_bus_chain"] += 1
    robin.name "After I got home with the bus guy's stuff in my knickers, I went to my room alone."
    robin.name "I was so ashamed."
    pc "Sounds more like you were wanting it."
    robin.name "I did. I..."
    robin.name "Touched myself still with my dirty knickers on..."
    pc "Oh wow."
    jump robin_talk_end

label robin_talk_bus_16:
    $ robin.dict["robin_talk_bus_chain"] += 1
    pc "You are asking for trouble messing with bus folk like that you know?"
    robin.name "Never heard of someone ended up hurt from the bus perverts."
    if robin.days_pregnant > (global_pregnancy_length * 0.3):
        pc "I was thinking more along the lines of ending up pregnant..."
        robin.name "Yeah, too late for that."
    else:
        pc "I mean winding up pregnant. Those guys won't pull out."

        if player.pregnancy >= 2:
            robin.name "Err... Have you looked in the mirror."
            pc "Yes, but we aren't talking about me here."
        else:
            robin.name "..."
    jump robin_talk_end

label robin_talk_bus_17:
    $ robin.dict["robin_talk_bus_chain"] += 1
    robin.name "I don't care if I end up in trouble because of the bus."
    pc "No?"
    robin.name "No..."
    robin.name "Well, I do. But..."
    robin.name "Whenever something happens to me on the bus, my heart is beating so much with excitement I can feel my ears throbbing."
    robin.name "No matter what my mind tells me, my body refuses to do anything except stand there and accept it."
    pc "You are going to end up fucked on the bus."
    robin.name "I know."
    jump robin_talk_end

label robin_talk_bus_18:
    $ robin.dict["robin_talk_bus_chain"] += 1
    $ add_to_list(robin.list, "pc_know_want_bussex")
    pc "Whatever, just make sure to tell me when you end up fucked on the bus so I can have fun hearing the story."
    robin.name "Haha, maybe you should come with me."
    if busgroper.sex:
        pc "You know I have been fucked on the bus before."
        robin.name "What, really?"
        if busgroper.preg:
            pc "Yeah, they also got me pregnant. It's why I say you should be careful."
        elif busgroper.sex > 5:
            pc "Bunch of times."
        elif busgroper.sex == 1:
            pc "Yeah, once."
        else:
            pc "Yeah, couple of times."
        robin.name "Fuck!"
        pc "Hey, don't be getting all excited on me you bloody pervert."
        robin.name "Shush!"
        pc "..."
    else:
        if player.has_perk([perk_slut, perk_bimbo, perk_exhibitionist]):
            pc "Doubt it would be the worst thing I've ever done."
        else:
            pc "Haha, don't drag me into your perverted games."
        robin.name "Yeah, bet you would like it too."
        pc "No comment."
        robin.name "Haha."
    jump robin_talk_end





label robin_talk_soccersex_chain_0:
    $ robin.dict["robin_talk_soccersex_chain"] += 1
    robin.name "So... Having sex with the boys at the pitch?"
    pc "Err..."
    if "soccerboys_seen_pitchsex" in robin.list:
        robin.name "I mean, we all watched you get fucked on the pitch..."
    elif "soccerboys_seen_dare_sex" in robin.list:
        robin.name "I mean I watched you get fucked on a dare, so..."
    elif "soccerboys_seen_dare_blowjob" in robin.list:
        robin.name "I mean I watched you suck a dick for a dare, so..."
    elif "soccerboys_seen_gloryhole_cum" in robin.list:
        robin.name "Well, you did go off with [nate.name] to make a gloryhole and come back with a messy face..."
    elif "soccerboys_seen_dare_handjob" in robin.list:
        robin.name "Kind of hard to keep it secret when I saw you giving a handjob on a dare..."
    elif "soccerboys_seen_dare_naked" in robin.list:
        robin.name "Well, stripping off for a dare so easily. Can kind of assume what else is going on..."
    elif "soccerboys_seen_shower" in robin.list:
        robin.name "Well, going off to shower with the boys. Kind of easy to assume other things are going on..."
    elif player.has_perk([perk_freeuse]):
        robin.name "I mean, I'm just guessing since you kinda don't turn anyone down."
    elif player.has_perk([perk_slut, perk_sucu]):
        robin.name "I mean, I'm just guessing since you are kind of a slut."
    elif player.has_perk([perk_exhibitionist]):
        robin.name "I mean, I'm just guessing since you like prancing around naked and they are perverts."
    elif player.has_perk([perk_broken]):
        robin.name "I mean, I'm just guessing since you kinda just do what people tell you, and they are perverts."
    else:
        robin.name "It's not really a secret any more..."
    pc "Yeah... Guess no point in hiding it."
    robin.name "Why didn't you tell me you were fooling around with them?"
    if all([nate.sex, dan.sex, drake.sex]):
        pc "\"Oh hey [robin.name]. How you doing? By the way I have been getting fucked by the guys we are hanging around with.\""
        pc "Not really a good conversation opener..."
        robin.name "True..."
    elif any([nate.sex, dan.sex, drake.sex]):
        pc "Oh, by the way [robin.name]. One of the boys fucked me while you weren't looking. Forgot to tell you."
        robin.name "Haha, okay. Point taken."
    else:
        pc "Not really been doing much with them. Just a little bit of fun I guess."
        robin.name "Just a little bit? Sure."
    jump robin_talk_end

label robin_talk_soccersex_chain_1:
    $ robin.dict["robin_talk_soccersex_chain"] += 1
    robin.name "Well, I know now that you have been messing with the boys so no need to hide it."
    pc "Wasn't really hiding it. Just not something that's easy to bring up."
    robin.name "Well, no matter now."
    robin.name "Guess I should have known though considering how you all act with each other."
    pc "Huh?"
    robin.name "You don't seem to mind at all that they are perverts and always looking at your body, making comments... Y'know."
    pc "Well, they do the same with you."
    robin.name "..."
    jump robin_talk_end

label robin_talk_soccersex_chain_2:
    $ robin.dict["robin_talk_soccersex_chain"] += 1
    pc "So you are okay with what I have been doing with the boys?"
    robin.name "Yeah. I don't care. Not a lot to enjoy these days so go for it."
    pc "Mmmm."
    jump robin_talk_end

label robin_talk_soccersex_chain_3:
    $ robin.dict["robin_talk_soccersex_chain"] += 1
    robin.name "The boys treat you well?"
    pc "Yeah, they aren't a bad lot."
    robin.name "Even [nate.name]?"
    pc "Pervert that he is, but he's alright."
    jump robin_talk_end

label robin_talk_soccersex_chain_4:
    $ robin.dict["robin_talk_soccersex_chain"] += 1
    robin.name "Was gonna ask how things got started with you and the boys, but pretty obvious I guess."
    pc "Yeah, just hanging out and things sort of started."
    robin.name "Yeah, and they are all perverts so..."
    pc "True."
    jump robin_talk_end

label robin_talk_soccersex_chain_5:
    $ robin.dict["robin_talk_soccersex_chain"] += 1
    robin.name "So the boys... How does it usually work?"
    pc "Work?"
    robin.name "Well, three of them and one of you."
    robin.name "I imagine you getting pretty skewered keeping them all happy."
    pc "You pervert."
    jump robin_talk_end

label robin_talk_soccersex_chain_6:
    $ robin.dict["robin_talk_soccersex_chain"] += 1
    robin.name "So, [nate.name] at the front, [drake.name] at the back..."
    pc "You are putting way too much thought into this."
    robin.name "Hmm, but that leaves [dan.name] without..."
    pc "..."
    jump robin_talk_end

label robin_talk_soccersex_chain_7:
    $ robin.dict["robin_talk_soccersex_chain"] += 1
    robin.name "There is no bed round the back of the pitch so would be hard to have all three at the same time."
    pc "If you are that interested, why don't you find out?"
    robin.name "You okay with me watching?"
    if "pc_suspect_likes_watching" in robin.list:
        $ add_to_list(robin.list, "pc_knows_likes_watching")
        pc "I knew it. You do get off on watching."
        robin.name "What? No."
        pc "Liar!"
    elif "pc_knows_likes_watching" in robin.list:
        pc "Ah, yeah you like to watch..."
        pc "Whatever. I don't care."
    else:
        $ add_to_list(robin.list, "pc_suspect_likes_watching")
        pc "Watching? I mean you offe..."
        pc "Wait. Do you like watching?"
        robin.name "No. Nooo. I just thought that's what you meant."
    jump robin_talk_end

label robin_talk_soccersex_chain_8:
    $ robin.dict["robin_talk_soccersex_chain"] += 1
    pc "Instead of watching, the boys would be happy for you to join."
    robin.name "What? I can't do that!"
    pc "Why not?"
    robin.name "Err, aren't they? Like, your friends?"
    pc "Pfft. They are perverts I have fun with. There is no relationship."
    jump robin_talk_end

label robin_talk_soccersex_chain_9:
    $ robin.dict["robin_talk_soccersex_chain"] += 1
    robin.name "Dunno, feels a bit weird with the boys."
    pc "Why?"
    robin.name "Dunno. I just played football with them and kinda avoided hanging out with them."
    robin.name "Got used to ignoring their attention but then saw you hanging with them and not like I had anything better to do."
    pc "Got so used to rejecting them that having fun with them feels awkward?"
    robin.name "Yeah..."
    jump robin_talk_end

label robin_talk_soccersex_chain_10:
    $ robin.dict["robin_talk_soccersex_chain"] += 1
    pc "If you want, I'll have a chat with them?"
    robin.name "And say what? \"Hey guys, why don't you drag [robin.name] off to the bushes and ravage her?\""
    pc "Err, yeah. That would work."
    robin.name "It was a joke!"
    jump robin_talk_end

label robin_talk_soccersex_chain_11:
    $ robin.dict["robin_talk_soccersex_chain"] += 1
    pc "Ok, if you insist. I will put it much more delicately."
    robin.name "Err, but... Hmmm."
    pc "Trust me. I'll put the idea out slowly. See their reaction to it."
    robin.name "Hmmm..."
    jump robin_talk_end

label robin_talk_soccersex_chain_12:
    $ robin.dict["robin_talk_soccersex_chain"] += 1
    $ add_to_list(robin.list, "soccerboys_asked_sex")
    robin.name "Ok, but don't be all obvious about it?"
    pc "Err, about what?"
    robin.name "The boys."
    pc "Ah. Don't worry. I'll ease the idea in and take it slow."
    robin.name "..."
    robin.name "Thanks..."
    jump robin_talk_end

label robin_talk_soccersextold:
    $ add_to_list(robin.list, "soccerboys_can_sex")
    pc "So I poked around with the boys. Pretty sure they are willing to have fun with you as well."
    robin.name "What? You sure?"
    pc "Yeah. Just, y'know. Don't reject them when they come onto you?"
    robin.name "You didn't make me come across like some slut did you?"
    pc "Noooo. I put it out there gently. So don't worry."
    robin.name "Right..."
    jump robin_talk_end





label robin_talk_sexgossip_chain_0:
    $ robin.dict["robin_talk_sexgossip_chain"] += 1
    robin.name "So, you gotten up to anything interesting recently?"
    pc "Err, same as always. You know how it is."
    robin.name "Yeah... I mean, err... Y'know."
    pc "Err, no. What?"
    robin.name "Never mind."
    jump robin_talk_end

label robin_talk_sexgossip_chain_1:
    $ robin.dict["robin_talk_sexgossip_chain"] += 1
    robin.name "I mean have you got up to anything interesting interesting."
    pc "Err, are you asking about my sex life?"
    robin.name "Shhhhh!"
    pc "Ah fuck! Not just watching but you want me to tell you stuff?"
    robin.name "I.. Err..."
    jump robin_talk_end

label robin_talk_sexgossip_chain_2:
    $ robin.dict["robin_talk_sexgossip_chain"] += 1
    pc "The more I get to know you, the more I realise you are a bloody deviant."
    robin.name "..."
    if player.has_perk(perk_broken, notif=True):
        pc "Well, you wouldn't be the first to get off on me and won't be the last. I don't mind."
        robin.name "Err, great?"
    elif player.has_perk([perk_slut, perk_whore, perk_bimbo, perk_exhibitionist], notif=True):
        pc "Not that I care. Just kinda funny."
        robin.name "Oh har har!"
    elif player.has_perk(perk_bambi, notif=True):
        pc "I seem to attract deviants. Though usually they are trying to grope me or drag me in the bushes."
        robin.name "Err, yeah. That happens to everyone."
        pc "Yeah, though I swear I attract them more."
    else:
        pc "Whatever. I don't care. World is broken enough without me judging people living in it."
        robin.name "..."
    jump robin_talk_end

label robin_talk_sexgossip_chain_3:
    $ robin.dict["robin_talk_sexgossip_chain"] += 1
    if player.vvirgin:
        pc "Not sure you are going to get much out of me though."
        robin.name "What do you mean?"
        pc "About what I have got up to. I don't really get up to much."
        robin.name "Oh? That's a shame."
    elif player.sex < 10:
        pc "Not much to tell though. I haven't gotten up to too much out there."
        robin.name "What do you mean?"
        pc "Telling you about my sex life. I haven't done a lot."
        robin.name "Oh? That's a shame."
    else:
        pc "So wanting to hear about my sex life?"
        robin.name "Err..."
        pc "You already outed yourself so no point in acting coy now."
        robin.name "Yeah..."
    jump robin_talk_end

label robin_talk_sexgossip_chain_4:
    $ robin.dict["robin_talk_sexgossip_chain"] += 1
    pc "So what kind of stuff you want to hear about?"
    robin.name "Err, anything?"
    pc "Anything?"
    robin.name "..."
    robin.name "Yeah?"
    pc "You sure?"
    robin.name "I don't want to... Err, open wounds or something so..."
    pc "Mmmm..."
    jump robin_talk_end

label robin_talk_sexgossip_chain_5:
    $ robin.dict["robin_talk_sexgossip_chain"] += 1
    $ add_to_list(robin.list, "pc_know_want_sexstories")
    robin.name "But honestly, anything. The good, the bad, the nasty..."
    pc "Opening a can of worms there. You sure?"
    robin.name "Yeah..."
    pc "Ok, well I'll see..."
    jump robin_talk_end





label robin_talk_sexobject_chain_0:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    pc "So, I have a question."
    robin.name "Mmm?"
    pc "You like watching people have sex and like hearing stories about it all."
    robin.name "Err... Okay?"
    pc "But what is it you actually want to do?"
    robin.name "Err... I'm not sure you want to hear about that..."
    pc "Wouldn't ask if I didn't"
    jump robin_talk_end

label robin_talk_sexobject_chain_1:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    pc "It's got to be something juicy if you don't want to tell."
    robin.name "I wouldn't call it juicy. It's just a bit embarrassing."
    pc "Now I want to know even more..."
    jump robin_talk_end

label robin_talk_sexobject_chain_2:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    robin.name "Sure you want to know about what I want?"
    pc "Of course."
    robin.name "..."
    robin.name "I... Don't know how to tell it..."
    pc "Just out and say..."
    jump robin_talk_end

label robin_talk_sexobject_chain_3:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    robin.name "When I was young, I lived in a shithole caravan site."
    pc "A gypsy?"
    robin.name "Err, not the polite way to call us, but sure."
    robin.name "Always playing in the mud and getting dirty. Second hand clothes or whatever we could steal from the donation bins."
    pc "Not much different to these days then."
    robin.name "Ha, worse these days. No donation bins."
    jump robin_talk_end

label robin_talk_sexobject_chain_4:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    robin.name "So always playing rough with the boys in my shitty clothes. Fighting, climbing around building sites, playing football. Y'know, typical kids stuff."
    pc "Err, not sure that's so typical."
    robin.name "Well, I found out later it wasn't. But for me it was normal. Not many girls around to play with so just played with the boys."
    pc "Ah, playing all the boyish games. I guess that's why a dress is alien for you?"
    robin.name "Well, that and no money to buy actual clothes. Most of what I wore were hand me downs from older boys around the caravan site."
    pc "Mmmm."
    jump robin_talk_end

label robin_talk_sexobject_chain_5:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    robin.name "Well, I didn't think much of it at the time wearing the shitty clothes and playing rough."
    pc "But..."
    robin.name "But then puberty hit. Not just for me but for all the boys I hung around with. Things got a little weird then."
    pc "Yeah, I can imagine."
    jump robin_talk_end

label robin_talk_sexobject_chain_6:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    robin.name "Puberty was when I really noticed I was the only girl in the group I used to hang out with."
    robin.name "Things started to get a bit weird. The boys started acting differently around me. Their own hormones probably."
    pc "Everyone fancied you?"
    robin.name "Not sure I would go that far. I was a little girl covered in mud and dirt in boys clothes that were far too big for me."
    robin.name "But I was the only girl there, so it got me the attention of the horny boys."
    jump robin_talk_end

label robin_talk_sexobject_chain_7:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    robin.name "But I was still the girl who was getting into fights and playing in the mud. So I ignored their clumsy attempts to come onto me."
    robin.name "Eventually they either got the message or a punch. Either way, they stopped and things sort of went back to normal. Well, normalish."
    pc "Okay..."
    robin.name "Still growing up in oversized clothes and filthy. But I grew up more and started to grow breasts and come into my body. The differences between me and the boys becoming more clear every day."
    pc "Okay. But still not sure what this has to do with what you \"want\"."
    robin.name "I'm getting there."
    jump robin_talk_end

label robin_talk_sexobject_chain_8:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    robin.name "So I started to grow up more. But the boys ignored me. Afraid of the stuff that happened before. I'd punch them if they tried anything."
    robin.name "Then I started to notice the other girls in school. All pretty and makeup, flirting and all that."
    pc "You are into girls?"
    robin.name "Nooo. Nothing like that..."
    jump robin_talk_end

label robin_talk_sexobject_chain_9:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    pc "Ok, not into girls but you were noticing them. What's the deal?"
    robin.name "Err, hard to say..."
    pc "All that backstory and you leave me with \"hard to say\"?"
    robin.name "Difficult to say. Embarrassing to say..."
    pc "Just spit it out..."
    jump robin_talk_end

label robin_talk_sexobject_chain_10:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    robin.name "What I want..."
    pc "Yeah..."
    robin.name "Is... Ah fuck!"
    pc "Come on, I know worse about you so just spit it out."
    robin.name "I want to be pretty!"
    pc "Oh? Err... That's it?"
    robin.name "..."
    jump robin_talk_end

label robin_talk_sexobject_chain_11:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    robin.name "Well, not just pretty..."
    robin.name "I want to be desired."
    pc "Pretty sure you already are."
    robin.name "Maybe, but not like that."
    pc "Like what then?"
    jump robin_talk_end

label robin_talk_sexobject_chain_12:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    robin.name "I want to be pretty as in... Ugh. How do I say it..."
    robin.name "I want it so when a man looks at me, he sees nothing but... Hmmm..."
    robin.name "I don't want him to see me, I want him to see sex."
    pc "Ah, you want to be seen as a sex object?"
    robin.name "Yes!"
    jump robin_talk_end

label robin_talk_sexobject_chain_13:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    robin.name "A sex object. I don't want him to try to talk to me, be my friend, get to know me or whatever."
    pc "You want him to want to fuck you."
    robin.name "Yeah. I want to be only desired. I want to walk into a room and have everyone know what my arse looks like but can't answer what my hair colour is."
    robin.name "I want to feel like those girls in school with the vultures circling in the hopes of fucking the girl."
    jump robin_talk_end

label robin_talk_sexobject_chain_14:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    pc "Well, what's stopping you from dressing up and acting like a sexpot?"
    robin.name "Well, I don't know how..."
    pc "It's not rocket science."
    robin.name "It is when you don't know what to do."
    jump robin_talk_end

label robin_talk_sexobject_chain_15:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    if player.has_perk(perk_male, notif=True):
        pc "Let me tell you a secret about men."
        robin.name "Mmm?"
        pc "It's much less about how you act and much more about how you look. Especially with what you want."
        pc "You want to walk into a room and have all eyes on you, then dress like people will look at you."
    elif player.has_perk([perk_slut, perk_bimbo, perk_exhibitionist, perk_whore]):
        pc "Men are simple creatures when it comes to looking like a sexpot."
        robin.name "Oh?"
        pc "You just need to dress the part. It's not about how you act but about how you look."
        robin.name "But, shouldn't you act all flirty and girly like?"
        pc "Well, it helps. But you want people to want to fuck you. Start by looking like someone who wants to be fucked."
    else:
        pc "I think you are over thinking things with wanting to be a sexpot."
        robin.name "How so?"
        pc "Just dress up with all the bells and whistles that you saw the girls in school with. Men are dumb apes."
        pc "They see a girl dressed sexy, they look and they want to... Yeah, you know."
    robin.name "You think?"
    pc "Yeah..."
    jump robin_talk_end

label robin_talk_sexobject_chain_16:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    pc "The real question is though is how you want to look."
    robin.name "How so?"
    pc "Well, you have different types of sexy. Elegant sexy, cute sexy..."
    robin.name "Fuck me sexy?"
    pc "Oh? Well that one is easy."
    jump robin_talk_end

label robin_talk_sexobject_chain_17:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    pc "Fuck me sexy is just about wearing as little clothes as possible."
    if c.slutty and not "home" in tab_top:
        robin.name "Like you?"
        pc "Err... Yes?"
    pc "A tiny skirt that barely covers your arse, cleavage, makeup..."
    robin.name "Think I could pull it off?"
    pc "Yeah, easily. Do you want to?"
    robin.name "Oh fuck yes."
    pc "Oh?"
    jump robin_talk_end

label robin_talk_sexobject_chain_18:
    $ robin.dict["robin_talk_sexobject_chain"] += 1
    $ add_to_list(robin.list, "sexobject_clothes_buy")
    robin.name "Will you help me out with looking like that?"
    pc "You want me to?"
    robin.name "Yeah..."
    pc "Oh dear [robin.name], wanting to look like a highway whore. How you have fallen."
    robin.name "Shut up!"
    pc "Hahaha!"
    $ log.assign("Making a slut")
    jump robin_talk_end

label robin_talk_sexobject_bedroom_thoughts:
    $ add_to_list(robin.list, "sexobject_clothes_bedroom_thoughts")
    pcm "So [robin.name] wants to look like a..."
    pcm "Well, a slut..."
    pcm "I should look around somewhere to pick up some clothes."
    pcm "Hmm, this better not be a sneaky way to get some free clothes out of me."
    jump travel

label robin_talk_sexobject_market_thoughts:
    $ add_to_list(robin.list, "sexobject_clothes_market_thoughts")
    pcm "Hmm, I can probably pick up some clothes for [robin.name] here."
    pcm "Gonna cost me though..."
    jump travel

label robin_talk_sexobject_funwear_thoughts:
    $ add_to_list(robin.list, "sexobject_clothes_funwear_thoughts")
    pcm "Hmm, I can probably pick up some clothes for [robin.name] in the funwear shop."
    pcm "Gonna cost me though..."
    jump travel

label robin_talk_sexobject_neddle_buy:
    if player.cash < 500:
        $ player.face_worried()
        pcm "Not sure I have enough money to pick up what I want to for [robin.name]. I should come back when I can afford it."
        jump travel
    $ add_to_list(robin.list, "sexobject_clothes_bought")

    if frida_here() and saskia_here():
        pc "Hey!"
        show saskia at right1
        show frida at right2
        with dissolve
        frida.name "Oooh, look who it is."
        if log.completed("mq_05_prep_b"):
            saskia.name "Oh. [tuc] sent you here again for some more dress up? That dirty bastard."
        else:
            saskia.name "Oh? Looking for something interesting?"
        pc "Err, yeah. Maybe?"
        saskia.name "So what you after. Got a lot here you might want."
        pc "I'm looking for something sexy."
        frida.name "Came to the right place. Sexy how? Sexy princess? Sexy maiden?"
        pc "Err... A cheap whore?"
        saskia.name "Ohh we have lots 'o that!"
        frida.name "Loads. Lot a cheap whores round here wanting to look like a cheap whore."
        frida.name "Come round here an 'ave a look."
        pc "Right..."
        "I spend the next 20 minutes or so going through some of the options and picking out what I think would be best."
        $ loiter(who=[saskia, frida])
        $ player.spend(500)
        $ inv.take(item_robin_package)
        saskia.name "She's gonna get picked right up in that lot."
        frida.name "Haha. Don't set your prices too high or you'll scare 'em off."
        pc "Ugh..."
        pc "Well, thanks for the help."
        saskia.name "Sure. Give some free service for friends of mine and I might not charge you for the clothes next time."
        pc "Yeah yeah..."
    elif frida_here():
        pc "Hey!"
        show frida at right1
        frida.name "Oooh, look who it is."
        if log.completed("mq_05_prep_b"):
            frida.name "That pervert sending you here again to look all dirty for him?"
            pc "Err, who?"
            frida.name "[tuc]. You fucking him and looks like he enjoys dressing you all naughty like."
            pc "Err, if you say so..."
        else:
            frida.name "Come here to get all tarted up or looking for something more special?"
            pc "Err... Tarted up I guess?"
        frida.name "Great. Going for the whore look or want to keep it classy?"
        pc "Errm... Whore?"
        frida.name "Ok, a whore. Expensive?"
        pc "So cheap it might as well be free."
        frida.name "The best kind. We have a lot 'o stuff for the junkie whores round here. Come 'ave a look."
        "I spend the next 20 minutes or so going through some of the options and picking out what I think would be best."
        $ loiter(who=[frida])
        $ player.spend(500)
        $ inv.take(item_robin_package)
        frida.name "Tell your friends about us. Got all the slut wear a cheap whore could ever need. Will give discounts if we can put em to work."
        pc "Right... Thanks."
    else:
        pc "Hey!"
        show saskia at right1
        saskia.name "Oh hey [name]!"
        if log.completed("mq_05_prep_b"):
            saskia.name "Didn't think [tuc] would be sending you back here so soon. He tired of the gamine look and wants to fuck you in something else?"
        else:
            saskia.name "Oh? Looking for something interesting?"
        pc "Err, yeah. Maybe?"
        saskia.name "So what you after. Got a lot here you might want."
        pc "I'm looking for something sexy."
        frida.name "That I can do. What kind of look you after?"
        pc "Err... A cheap whore?"
        saskia.name "Ohh we have lots 'o that!"
        saskia.name "Half the people round here are either highway whores or wanting to dress their bint as one."
        pc "Right..."
        saskia.name "Come. 'Ave a look!"
        "I spend the next 20 minutes or so going through some of the options and picking out what I think would be best."
        $ loiter(who=[saskia])
        $ player.spend(500)
        $ inv.take(item_robin_package)
        saskia.name "You're gonna get picked right up in that lot."
        pc "Ugh..."
        pc "Well, thanks for the help."
        saskia.name "Sure. Give some free service for friends of mine and I might not charge you for the clothes next time."
        pc "Yeah yeah..."
    $ renpy.scene()
    $ walk(loc_school_hallway_2f)
    pcm "Right then. Got two outfits for her to pick from. Guess I could wear the other one."
    pcm "Let's see what [robin.name] thinks."
    $ log.markdone("quest_robinslut_01")
    jump travel

label robin_talk_sexobject_funwear_buy:
    if player.cash < 500:
        $ player.face_worried()
        pcm "Not sure I have enough money to pick up what I want to for [robin.name]. I should come back when I can afford it."
        jump travel
    $ add_to_list(robin.list, "sexobject_clothes_bought")
    pcm "Right then... Let's see here..."
    show fun_girl at right1 with dissolve
    pc "Err, hey."
    fun_girl.name "How can I help you cutie?"
    pc "Umm, I'm kinda looking for something."
    fun_girl.name "Sure, we got all you need for some fun here. What kind of fun you looking for?"
    pc "Errm, a friend of mine wants to... err..."
    fun_girl.name "Don't be shy darlin'. What your \"friend\" need?"
    pc "Umm, she wants to look all sexy."
    fun_girl.name "Oooh, we got lotsa that. Sexy how so?"
    pc "Like a cheap whore?"
    fun_girl.name "Wonderful! That's our specialty. Get a lot of actual cheap whores in 'ere."
    fun_girl.name "Come 'ave a look. Lotta stuff to choose from."
    "I spend the next 20 minutes or so going through some of the options and picking out what I think would be best."
    $ loiter()
    $ player.spend(500)
    $ inv.take(item_robin_package)
    fun_girl.name "Oooh your \"friend\" gonna have to fight 'em off."
    pc "Why do you keep saying friend like that? It really is for a friend."
    fun_girl.name "Sure, no judgement here."
    pc "Well, thanks for this."
    fun_girl.name "Umm, before you go."
    pc "Hmm?"
    fun_girl.name "Might wanna get your \"friend\" to invest in some protection if she's gonna be having fun like this."
    pc "Err, you sell it here?"
    fun_girl.name "Sorry sweetheart. Way too hot."
    pc "Right..."
    pc "Thanks anyway."
    fun_girl.name "Come again!"
    hide fun_girl
    $ walk(loc_revel_backstreet)
    pcm "Right then. Got two outfits for her to pick from. Guess I could wear the other one."
    pcm "Let's see what [robin.name] thinks."
    $ log.markdone("quest_robinslut_01")
    jump travel

label robin_talk_sexobject_market_buy:
    if player.cash < 500:
        $ player.face_worried()
        pcm "Not sure I have enough money to pick up what I want to for [robin.name]. I should come back when I can afford it."
        jump travel
    $ add_to_list(robin.list, "sexobject_clothes_bought")
    pcm "Right then... Let's see here..."
    if frida_here(loc_market_stall_needle) or saskia_here(loc_market_stall_needle):
        pcm "Well, looks like someone is at those crazy girls' stall so they are probably a good bet."
        $ walk(loc_market_stall_needle)
        if frida_here() and saskia_here():
            pc "Hey!"
            show saskia at right1
            show frida at right2
            with dissolve
            frida.name "Oooh, look who it is."
            if log.completed("mq_05_prep_b"):
                saskia.name "Oh. [tuc] sent you here again for some more dress up? That dirty bastard."
            else:
                saskia.name "Oh? Looking for something interesting?"
            pc "Err, yeah. Maybe?"
            saskia.name "So what you after. Got a lot here you might want."
            pc "I'm looking for something sexy."
            frida.name "Came to the right place. Sexy how? Sexy princess? Sexy maiden?"
            pc "Err... A cheap whore?"
            saskia.name "Ohh we have lots 'o that!"
            frida.name "Loads. Lot a cheap whores round here wanting to look like a cheap whore."
            frida.name "Come round here an 'ave a look."
            pc "Right..."
            "I spend the next 20 minutes or so going through some of the options and picking out what I think would be best."
            $ loiter(who=[saskia, frida])
            $ player.spend(500)
            $ inv.take(item_robin_package)
            saskia.name "She's gonna get picked right up in that lot."
            frida.name "Haha. Don't set your prices too high or you'll scare 'em off."
            pc "Ugh..."
            pc "Well, thanks for the help."
            saskia.name "Sure. Give some free service for friends of mine and I might not charge you for the clothes next time."
            pc "Yeah yeah..."
        elif frida_here():
            pc "Hey!"
            show frida at right1
            frida.name "Oooh, look who it is."
            if log.completed("mq_05_prep_b"):
                frida.name "That pervert sending you here again to look all dirty for him?"
                pc "Err, who?"
                frida.name "[tuc]. You fucking him and looks like he enjoys dressing you all naughty like."
                pc "Err, if you say so..."
            else:
                frida.name "Come here to get all tarted up or looking for something more special?"
                pc "Err... Tarted up I guess?"
            frida.name "Great. Going for the whore look or want to keep it classy?"
            pc "Errm... Whore?"
            frida.name "Ok, a whore. Expensive?"
            pc "So cheap it might as well be free."
            frida.name "The best kind. We have a lot 'o stuff for the junkie whores round here. Come 'ave a look."
            "I spend the next 20 minutes or so going through some of the options and picking out what I think would be best."
            $ loiter(who=[frida])
            $ player.spend(500)
            $ inv.take(item_robin_package)
            frida.name "Tell your friends about us. Got all the slut wear a cheap whore could ever need. Will give discounts if we can put em to work."
            pc "Right... Thanks."
        else:
            pc "Hey!"
            show saskia at right1
            saskia.name "Oh hey [name]!"
            if log.completed("mq_05_prep_b"):
                saskia.name "Didn't think [tuc] would be sending you back here so soon. He tired of the gamine look and wants to fuck you in something else?"
            else:
                saskia.name "Oh? Looking for something interesting?"
            pc "Err, yeah. Maybe?"
            saskia.name "So what you after. Got a lot here you might want."
            pc "I'm looking for something sexy."
            frida.name "That I can do. What kind of look you after?"
            pc "Err... A cheap whore?"
            saskia.name "Ohh we have lots 'o that!"
            saskia.name "Half the people round here are either highway whores or wanting to dress their bint as one."
            pc "Right..."
            saskia.name "Come. 'Ave a look!"
            "I spend the next 20 minutes or so going through some of the options and picking out what I think would be best."
            $ loiter(who=[saskia])
            $ player.spend(500)
            $ inv.take(item_robin_package)
            saskia.name "You're gonna get picked right up in that lot."
            pc "Ugh..."
            pc "Well, thanks for the help."
            saskia.name "Sure. Give some free service for friends of mine and I might not charge you for the clothes next time."
            pc "Yeah yeah..."
    else:

        pc "Let's have a look around then I suppose..."
        show activity_walk
        "I take a look around popping into various stalls. Fortunately the kind of clothes [robin.name] will be wearing is fairly popular so not oo hard to find."
        $ loiter(60)
        $ player.spend(500)
        $ inv.take(item_robin_package)
        "Still takes a little while though as I need to pop from stall to stall to pick up the different bits."
    $ renpy.scene()
    $ walk(loc_market)
    pcm "Right then. Got two outfits for her to pick from. Guess I could wear the other one."
    pcm "Let's see what [robin.name] thinks."
    $ log.markdone("quest_robinslut_01")
    jump travel





label robin_talk_oskarsexrent_chain_0:
    $ robin.dict["robin_talk_oskarsexrent_chain"] += 1
    robin.name "Umm, so I had a weird thing happen..."
    pc "Hmm?"
    robin.name "[oskar.name] came up to me for a chat."
    pcm "Fuck!"
    pc "Yeah?"
    robin.name "He kinda implied I could pay rent another way."
    pc "..."
    robin.name "Yeah..."
    jump robin_talk_end

label robin_talk_oskarsexrent_chain_1:
    $ robin.dict["robin_talk_oskarsexrent_chain"] += 1
    robin.name "What do you think of [oskar.name]'s offer?"
    pc "Doesn't matter what I think. This is up to you."
    robin.name "But isn't it basically whoring?"
    if robin.isslut:
        pc "Do you care? You're a slut anyway so what's a little whoring on the side?"
    elif player.iswhore:
        pc "And? Not like I haven't fucked for money."
    else:
        pc "Well, not like that's wrong really. Can you even pay the money?"
    robin.name "..."
    robin.name "If I do something for fun or offered, then it's my choice."
    robin.name "This kind of feels like I am forced to accept."
    pc "Or you could pay."
    jump robin_talk_end

label robin_talk_oskarsexrent_chain_2:
    $ robin.dict["robin_talk_oskarsexrent_chain"] += 1
    robin.name "[oskar.name]'s offer still leaves a bad taste in my mouth."
    pc "I think that's his plan."
    robin.name "[name]!"
    pc "Ha, sorry..."
    pc "Well, maybe look at it this way. If you are going to be kicked out on your arse then you have a fallback option."
    robin.name "I guess..."
    jump robin_talk_end

label robin_talk_oskarsexrent_chain_3:
    $ robin.dict["robin_talk_oskarsexrent_chain"] += 1
    $ add_to_list(robin.list, "oskar_sex")
    robin.name "What would you do about [oskar.name]'s offer?"
    if oskar.sex:
        pc "I'm already fucking him for lower rent..."
        robin.name "What!? Really?"
        pc "Yeah... He knocks off way more rent for 10 minutes of bending over than I can earn working in a few hours."
    elif player.iswhore:
        pc "I mean, it's not like I'm not already selling myself. So what would I care?"
        pc "Most of the money I earn goes towards rent anyway, so why whore in shady places when I can just fuck [oskar.name]?"
    elif robin.isslut:
        pc "You have probably fucked much worse guys than him fucking on the bus or in the pub. At least [oskar.name] is sober and clean."
    else:
        pc "Hard to say. Being homeless and living in the slum is way worse than what he is offering..."
    robin.name "..."
    robin.name "Probably..."
    jump robin_talk_end

label robin_talk_oskarsexseen_chain_0:
    $ robin.dict["robin_talk_oskarsexseen_chain"] += 1
    pc "So... Fucking [oskar.name]?"
    robin.name "Yeah..."
    pc "And?"
    robin.name "And what?"
    pc "Give more info!"
    robin.name "*Sigh*"
    jump robin_talk_end

label robin_talk_oskarsexseen_chain_1:
    $ robin.dict["robin_talk_oskarsexseen_chain"] += 1
    pc "So... [oskar.name]?"
    robin.name "It's like you said. Cheaper to bend over than to pay."
    pc "Having any fun?"
    robin.name "..."
    robin.name "It's not horrible..."
    jump robin_talk_end

label robin_talk_oskarsexseen_chain_2:
    $ robin.dict["robin_talk_oskarsexseen_chain"] += 1
    robin.name "I just pop round to his office in the morning now and then and let off some steam."
    robin.name "You know, sometimes you have one of those dreams and wake up a bit..."
    robin.name "So I go to his office and it lowers the rent at the same time."
    pc "Mmmm..."
    jump robin_talk_end

label robin_talk_oskarsexseen_chain_3:
    $ robin.dict["robin_talk_oskarsexseen_chain"] += 1
    robin.name "Plus, [oskar.name] is kinda good looking I guess."
    robin.name "Even if it is the kind of good looking where you also want to punch him in the face."
    pc "Ask him, he might lower the rent more for that kind of fun."
    robin.name "Haha!"
    jump robin_talk_end

label robin_talk_oskarsexseen_chain_4:
    $ robin.dict["robin_talk_oskarsexseen_chain"] += 1
    robin.name "So yeah... Just decided there is no harm paying the rent that way."
    pc "Well, have you seen the slums?"
    robin.name "Err, no. I won't go near that place."
    if loc_highway_slum.visited:
        pc "It's not pretty. It's where both our corpses would be getting raped if we stopped paying rent here."
    else:
        pc "Nor me, but I have heard that it's pretty bad."
    jump robin_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
