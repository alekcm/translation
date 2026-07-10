init python:
    def dani_drinkwine_subject_can_trigger_unique():
        
        
        
        
        if not ((t.day - 1) > dani.dict["dani_drinking_wine_day"]) or dani.dict["dani_drinking_wine_day"] == 0:
            return False
        
        
        elif not "drinking_event_played_kissing" in dani.conversation_topics and dani.love >= 100 and pubpatron in dani.sex_who_class:
            return "kissing"
        elif not "drinking_event_played_sex" in dani.conversation_topics and "drinking_event_played_kissing" in dani.conversation_topics:
            return "sex"
        
        
        elif not renpy.has_label("oskar_sex_talk_" + str(dani.dict["oskar_sex_talk"])) and not "drinking_event_played_oskar" in dani.conversation_topics:
            return "Oskar talk"
        
        
        elif not renpy.has_label("dani_talk_workingpub_chain_" + str(dani.dict["talk_workingpub_chain"])) and not "drinking_event_played_pub1" in dani.conversation_topics:
            return "pub1"
        elif not renpy.has_label("dani_talk_whoreingpub_chain_" + str(dani.dict["talk_whoringpub_chain"])) and not "drinking_event_played_pub2" in dani.conversation_topics:
            return "pub2"
        elif not renpy.has_label("dani_talk_gloryholepub_chain_" + str(dani.dict["talk_gloryholepub_chain"])) and not "drinking_event_played_pub3" in dani.conversation_topics:
            return "pub3"
        
        
        elif not "drinking_event_played_dance1" in dani.conversation_topics:
            return "dance1"
        elif school_dance_quest_show_count >= 5 and not "drinking_event_played_dance2" in dani.conversation_topics:
            return "dance2"
        elif "dance_waited_during_date" in dani.conversation_topics and not "drinking_event_played_dancewhore" in dani.conversation_topics:
            return "dancewhore"
        elif not "drinking_event_played_partyfinal" in dani.conversation_topics and quest_dancevip.iscomplete():
            return "finalparty"
        
        
        elif not "drinking_event_played_anabeldrift" in dani.conversation_topics and anabel_alone_academy_day_picker(True) > 6:
            return "anabeldrift"
        elif not "drinking_event_played_preg" in dani.conversation_topics and (player.showing or dani.showing):
            return "preg"
        
        else:
            return False


label dani_drinkwine_subject:


    $ inv_transfer(buy_inv, dani.inv)
    $ dani.dict["dani_drinking_wine_day"] = t.day
    $ dani_yan_remove(numgen(1,4))

    jump expression WeightedChoice([

    
    ("dani_drinking_wine_event_0", If(dani.dict["dani_drinking_wine_counter"] == 0, 10000, 0)),

    
    ("dani_drinking_wine_event_" + str(dani.dict["dani_drinking_wine_counter"]), If(renpy.has_label("dani_drinking_wine_event_" + str(dani.dict["dani_drinking_wine_counter"])), 30, 0)),
    ("dani_drinking_wine_event_kissing", If(not "drinking_event_played_kissing" in dani.conversation_topics and dani.love >= 100 and pubpatron in dani.sex_who_class, 900, 0)),
    ("dani_drinking_wine_event_sex", If(not "drinking_event_played_sex" in dani.conversation_topics and "drinking_event_played_kissing" in dani.conversation_topics, 900, 0)),
    
    
    ("dani_drinking_wine_event_oskar", If(not renpy.has_label("oskar_sex_talk_" + str(dani.dict["oskar_sex_talk"])) and not "drinking_event_played_oskar" in dani.conversation_topics, 100, 0)),

    
    ("dani_drinking_wine_event_pub1", If(not renpy.has_label("dani_talk_workingpub_chain_" + str(dani.dict["talk_workingpub_chain"])) and not "drinking_event_played_pub1" in dani.conversation_topics, 100, 0)),
    ("dani_drinking_wine_event_pub2", If(not renpy.has_label("dani_talk_whoreingpub_chain_" + str(dani.dict["talk_whoringpub_chain"])) and not "drinking_event_played_pub2" in dani.conversation_topics, 100, 0)),
    ("dani_drinking_wine_event_pubglory", If(not renpy.has_label("dani_talk_gloryholepub_chain_" + str(dani.dict["talk_gloryholepub_chain"])) and not "drinking_event_played_pub3" in dani.conversation_topics, 100, 0)),

    
    ("dani_drinking_wine_event_dance1", If(not "drinking_event_played_dance1" in dani.conversation_topics, 100, 0)),
    ("dani_drinking_wine_event_dance2", If(school_dance_quest_show_count >= 5 and not "drinking_event_played_dance2" in dani.conversation_topics and "drinking_event_played_dance1" in dani.conversation_topics, 100, 0)),
    ("dani_drinking_wine_event_dancewhore", If("dance_waited_during_date" in dani.conversation_topics and not "drinking_event_played_dancewhore" in dani.conversation_topics, 100, 0)),
    ("dani_drinking_wine_event_partyfinal", If(not "drinking_event_played_partyfinal" in dani.conversation_topics and quest_dancevip.iscomplete(), 800, 0)),

    
    ("dani_drinking_wine_event_preg", If(not "drinking_event_played_preg" in dani.conversation_topics and (player.showing or dani.showing), 100, 0)),
    ("dani_drinking_wine_event_anabeldrift", If(not "drinking_event_played_anabeldrift" in dani.conversation_topics and anabel_alone_academy_day_picker(True) > 6 and not anabel.hate, 500, 0)),
    
    ("dani_drinking_wine_event_repeatable", 1), 
    
    
    ])

label dani_drinking_wine_event_trigger:
    dani.name "Would be nice if we could get some wine."
    pc "Mmm, not seen anyone selling any. Only this home made stuff."
    dani.name "If you see any, can you get some. Would be so much nicer to relax here with a bottle."
    pc "I'll keep my eye out."
    if loc_highway_slum_still.visited:
        pcm "Might be able to pick some up in the slum off [havenvik.name]."
    $ log.assign("Evening wine")
    jump dani_talk_end

label dani_drinking_wine_event_trigger_repeat:

    dani.name "Be nice if you could get your hands on some more wine."
    if inv.qty(item_winebottle):
        if not loc(loc_bedroom_dani)or t.hour in (9,10,11,0,1):
            pc "I do have some, I can come over later if you want."
            dani.name "Yeah, that would be nice."
        else:
            pc "I do have some actually."
            dani.name "Then what are you waiting for?"
    else:
        pc "I'll see if I can get my hands on some."
        dani.name "Thanks."
    $ log.set_notdone("quest_daniwine_02")
    jump dani_talk_end

label dani_drinking_wine_event_0:
    $ dani.dict["dani_drinking_wine_counter"] += 1
    $ log.set_done("quest_daniwine_02")
    show dani happy
    dani.name "Oooh, some wine. How did you manage this?"
    pc "Someone I know sells booze. I asked them if they could dig up some wine."
    dani.name "I didn't think this stuff was around any more."
    pc "Seemed like a few people have asked for it so he is now stocking it. Costs a fair bit though."
    dani.name "Oh? Should I... like... pay you some money or something?"
    pc "We both know you don't have the money. And i don't think the wine is worth bending over for."
    dani.name "Pfft. Speak for yourself. I'd rather bend over for the wine than for [oskar.name]'s rent."
    $ player.face_happy()
    pc "I'm not sure the bottle will fit. But we can try."
    dani.name "Well, lets at least try to empty it first."
    pc "Haha, sure."
    $ player.face_neutral()
    dani.name "Well, open it."
    pc "Okay..."
    $ player.face_meek()
    pc "Nnng!"
    with vpunch
    $ player.left_hand = "wine_bottle"
    $ player.face_neutral()
    pc "There we go."
    pc "You got any glasses?"
    dani.name "I don't have a door and you think I might have glasses?"
    pc "So, that's a no?"
    dani.name "Haha, of course not. Drink from the bottle."
    pc "Okay, what made you want to hunt out some wine anyway?"
    dani.name "Why not? Things are shit out there so it's nice to be home with some wine."
    pc "You could go to the pub."
    $ player.drink(who=dani)
    $ relax(10)
    if "working_pub" in dani.list:
        dani.name "Yeah no thanks. I have enough of that place working there."
        pc "What, a place where perverts try to put their hand up your skirt isn't your idea of a fun place to drink?"
        dani.name "Their hand isn't the only thing they try to put up my skirt."
    else:
        dani.name "Yeah no thanks, I don't think that's the kind of place I want to be drinking."
        pc "What, getting drunk in a room full of horny perverts isn't your idea of a fun place to drink?"
        dani.name "There are plenty of places people are trying to get my clothes off. Getting drunk in a pub would be a bad idea."
    pc "Ha, I guess so."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "You say that like you enjoy it."
    if player.has_perk([perk_slut, perk_bimbo, perk_sucu]):
        pc "I don't mind. But to each their own."
    elif player.has_perk([perk_bambi, perk_meek]):
        pc "No, it's pretty shitty."
    else:
        pc "Wouldn't say that. But if I worried about that sort of thing, I would never leave my house."
    dani.name "Yeah, I would rather drink at home. No chance of waking up naked and wondering what happened."
    pc "Well, you almost are already naked, so wouldn't need to do much to get the rest off."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "Shoo, pervert."
    pc "Haha, you are the naked one."
    dani.name "I have to dry out my clothes before tomorrow. You are lucky I have spare underwear."
    $ player.drink(who=dani)
    $ relax(10)
    pc "I'll let the perverts know."
    dani.name "Ha, sure."
    $ player.drink(who=dani)
    $ relax(10)
    $ player.left_hand = ""
    pc "Looks like that's the last of the wine."
    dani.name "Aww. Well it's kinda late anyway. I'll probably head to bed."
    pc "Okay, let me get out your window so I don't need to climb over you."
    dani.name "Haha, okay. We should do this again."
    pc "Sure, see ya."
    dani.name "Bye."
    hide dani
    $ walk(loc_stairwell)
    pc "That was nice."
    jump travel

label dani_drinking_wine_event_1:
    $ dani.dict["dani_drinking_wine_counter"] += 1
    $ log.set_done("quest_daniwine_02")
    dani.name "Ooh, more wine. I could get used to this."
    pc "Nothing makes living here better than some casual alcoholism."
    if player.has_perk(perk_alcoholic):
        dani.name "Yeah, sounds like you might have the right idea."
    else:
        dani.name "Haha. Well, here we go then."
    $ player.face_meek()
    pc "Nnng!"
    with vpunch
    $ player.left_hand = "wine_bottle"
    $ player.face_neutral()
    pc "There we go."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "Much better than the beer everywhere else sells."
    pc "Not by much. Might be wine but it's not far off tasting like vinegar."
    dani.name "No expensive twenty year old wines then?"
    pc "Yeah right. Even if I got my hands on that, I'd rather sell it and buy 20 bottles of this cheap stuff."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "True, twenty nights drunk is better than one good night."
    pc "Haha."
    dani.name "And people keep saying this place is one of the good places."
    pc "What do you mean?"
    dani.name "[town]. Supposed to be good here compared to other towns or cities."
    pc "Maybe it is, I haven't been out there."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "Nor me. Only how things were before."
    pc "There are truckers and people like that. They travel around I think."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "You think?"
    pc "Well yeah, I don't even know of other towns out there. Maybe they are just collecting stuff from ruins."
    dani.name "Ah."
    pc "They say this place is better than others, but they never say why or even what the other places are."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "It's all a secret!"
    pc "Maybe this is a prison!!"
    dani.name "Haha! Well I hope I serve my time quickly."
    pc "We have a life sentence it looks like."
    dani.name "Well, this place means it won't be too long left."
    pc "Yup, turn up as a corpse in the bushes. So won't have long left to serve."
    $ player.drink(who=dani)
    $ relax(10)
    $ player.left_hand = ""
    pc "And that's the gourmet wine over."
    dani.name "Shame."
    jump dani_drinking_wine_event_end

label dani_drinking_wine_event_kissing:
    $ add_to_list(dani.conversation_topics, "drinking_event_played_kissing")
    $ add_to_list(dani.list, "kissed")
    $ log.set_done("quest_daniwine_02")
    pc "I have something that we both love."
    show dani happy
    dani.name "Oooh..."
    $ player.face_meek()
    pc "Nnng!"
    with vpunch
    $ player.left_hand = "wine_bottle"
    $ player.face_neutral()
    $ player.drink(who=dani)
    $ relax(10)
    pc "Straight from the bottle."
    dani.name "The way nature intended."
    $ player.drink(who=dani)
    $ relax(10)
    pc "Have you been looking into ways to get out of this place?"
    dani.name "What do you mean?"
    pc "The flat. Finding something nicer."
    dani.name "Not really. Haven't put much thought into it."
    pc "Hmm, I thought since you were pretty pissed off with the rent you might look for something else."
    dani.name "How do you even look for other places these days?"
    pc "Hmmm, haven't thought about that."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "No more websites to just look this stuff up."
    pc "True, used to post ads in shop windows before I think."
    dani.name "Yeah, most shops don't even have windows any more. Plus, not so bad staying here now you are popping over."
    pc "Yeah, wine with me makes up for all the horrors."
    dani.name "Haha."
    dani.name "But seriously, it's kinda nice hanging out here with you."
    pc "Yeah, I bring wine and get you drunk. What's not to like?"
    $ player.drink(who=dani)
    $ relax(10)
    if dani.dict["dani_times_slept_over"]:
        dani.name "Keeping the bed warm with me as well."
        pc "Pretty sure half the town will offer you that for free."
    else:
        dani.name "You should crash here one night. Would be nice."
    pc "Getting you drunk while half naked and sharing a bed. Folks will get te wrong idea."
    dani.name "Would they?"
    pc "What do you mean?"
    dani.name "Errr..."
    show dani_kiss
    hide dani
    with dissolve
    $ player.face_shock()
    pc "Mmmff..."
    hide dani_kiss
    show dani worried at right6
    with dissolve
    $ player.face_worried()
    pc "Errm..."
    pc "That was unexpected."
    dani.name "Sorry, I just..."
    $ player.drink(who=dani)
    $ relax(10)
    $ player.face_happy()
    pc "Trying to steal the wine from my mouth."
    show dani happy
    dani.name "Ha, sure."
    $ player.drink(who=dani)
    $ relax(10)
    $ player.face_neutral()
    $ player.left_hand = ""
    pc "Looks like it's pretty much over anyway."
    dani.name "I... Errm..."
    dani.name "..."
    pc "Ha, it's fine. Don't worry about it."
    dani.name "Okay."
    jump dani_drinking_wine_event_end

label dani_drinking_wine_event_sex:
    $ add_to_list(dani.conversation_topics, "drinking_event_played_sex")
    $ dani.can_sex = True
    $ log.set_done("quest_daniwine_02")
    pc "Aaaand here wo go!"
    show dani happy
    dani.name "Oooh..."
    $ player.face_meek()
    pc "Nnng!"
    with vpunch
    $ player.left_hand = "wine_bottle"
    $ player.face_neutral()
    pc "Down the hatch."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "No better way to get through the day."
    pc "Tell me about it."
    pc "How have you been getting on anyway?"
    dani.name "What do you mean?"
    pc "With the whole [oskar.name] thing, doing stuff at the pub..."
    $ player.drink(who=dani)
    $ relax(10)
    pc "Y'know..."
    dani.name "Ah, yeah..."
    dani.name "Well... Not much to say really."
    dani.name "Not like I can avoid it."
    $ player.drink(who=dani)
    $ relax(10)
    pc "I suppose..."
    dani.name "Nicer hanging out though."
    pc "Huh?"
    dani.name "I mean before I pretty much did everything to pay rent and eat food."
    dani.name "So it's nice to spend time with you and actually just hang out."
    pc "Ah, no stress. Just wine and relaxing."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "Yeah..."
    dani.name "Errm. About what happened before."
    pc "Err, what did happen before?"
    dani.name "The kiss..."
    pc "Ah."
    dani.name "..."
    pc "Errm..."
    dani.name "I kinda hoped you would interrupt me and say something."
    pc "Haha, okay... Err, next time you steal my wine the bottle is going up your arse!"
    dani.name "Haha."
    $ player.drink(who=dani)
    $ relax(10)
    pc "So you are into girls?"
    dani.name "Not really. It's just really nice hanging out and having fun. I guess I just wanted to take it further or make something more of it."
    dani.name "It's just nice being with you, so I thought..."
    dani.name "Dunno..."
    pc "No worries. I know it's weird with all the guys pretty much treating us like whores. So nice to have something more meaningful."
    dani.name "Yeah, something like that."
    dani.name "So, not really into girls. But it would be nice to do something a little more. Or something."
    pc "Yeah I understand."
    dani.name "Maybe next time you stay over or something..."
    $ player.drink(who=dani)
    $ relax(10)
    $ player.left_hand = ""
    pc "Speaking of, looks like that's the wine over with."
    dani.name "Ah, no pressure. It's fine if you head off home."
    pc "I think I will. Think things over."
    pc "Good night [dani.nname]"
    dani.name "Okay, be safe."
    hide dani
    $ walk(loc_stairwell)
    pcm "What was something."
    pcm "If I crash at her place I think she will want something from me."
    if loc_junk_trailer.unlocked:
        pcm "First [jaylee.name] after my ass and now [dani.nname]."
    else:
        pcm "Used to guys wanting my ass, a girl is kinda new."
    pcm "Oh well, if I want some funwith her I'll just stay over."
    jump travel


label dani_drinking_wine_event_oskar:
    $ add_to_list(dani.conversation_topics, "drinking_event_played_oskar")
    $ log.set_done("quest_daniwine_02")
    pc "I come with gifts."
    show dani happy
    dani.name "Oooh..."
    $ player.face_meek()
    pc "Nnng!"
    with vpunch
    $ player.left_hand = "wine_bottle"
    $ player.face_neutral()
    $ player.drink(who=dani)
    $ relax(10)
    pc "Still no glasses?"
    dani.name "You can bring some if you want."
    $ player.drink(who=dani)
    $ relax(10)
    pc "That's your job to get stuff for your place."
    dani.name "I am not buying stuff for this shithole. [oskar.name] would probably up the rent if this place started to look decent."
    pc "Yeah, probably he would."
    pc "Hope he doesn't climb in your window in the morning or something."
    if "slept_over" in loc_bedroom_dani.list:
        pc "I don't want him trying to put his dick in me or something while I am crashing here."
        dani.name "Don't worry, I'll leave you two alone if that happens."
        if oskar.sex:
            pc "Already paying my own rent like that. I don't need to be paying yours as well."
            dani.name "No? I don't mind."
            pc "Ha, I'm sure you don't."
        else:
            pc "Probably won't even get a discount on my own rent."
            dani.name "No problem. I'll accept the discount."
            pc "Ha, I'm sure you would."

    $ player.drink(who=dani)
    $ relax(10)
    dani.name "I usually go visit him on the weekend or something."

    if loc_office_ll_back.visited:
        pc "That shitty back room he has in his office?"
        dani.name "Yeah, or in the office."
    else:
        pc "Odd place for it. He can't even stand to come in the room he is renting you?"
        dani.name "Probably not. I go to his office. He has a dingy back room with a sleeping area."
        pc "Ugh. Prepared is he?"
        dani.name "Lot of girls in this block. Probably making half of them pay rent that way."
        pc "Surprised he can keep up."
        dani.name "Probably a stash of Lebo in his drawer."
        pc "Oh? Maybe you should steal it and become a drug dealer."
        dani.name "Haha. Yeah, [dani.nname] the dealer. I'll make millions."
        dani.name "Or get murdered by a junkie."
        pc "Either way, no more working for you."
        dani.name "Haha."

    $ player.drink(who=dani)
    $ relax(10)
    dani.name "Maybe I should just murder [oskar.name] and keep living here."
    pc "Not sure anyone would care to be honest."
    dani.name "Free rent for everyone."
    pc "The girls around here would help you bury the body."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "Haha, I hope so."
    dani.name "I wonder where the best place to hide a body would be..."
    pc "The lake?"
    dani.name "Too far. I'll have to drag it out there."
    pc "Feed him to the dogs?"
    $ player.drink(who=dani)
    $ relax(10)
    $ player.left_hand = ""
    dani.name "Can't. Everyone ate the dogs already."
    pc "Feed him to the people eating dogs?"
    dani.name "Hahaha!"
    pc "Looks like that's the wine done for."
    dani.name "Next time then."
    pc "Yeah."
    jump dani_drinking_wine_event_end


label dani_drinking_wine_event_pub1:
    $ add_to_list(dani.conversation_topics, "drinking_event_played_pub1")
    $ log.set_done("quest_daniwine_02")
    pc "Thought you might have been a bit fed up with drinking since working at the pub."
    show dani neutral
    dani.name "They don't sell wine there."
    pc "Yeah, I wonder why they don't."
    pc "Nnng!"
    with vpunch
    $ player.left_hand = "wine_bottle"
    $ player.face_neutral()
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "Pretty sure those brutes are happy enough with the piss water they drink."
    pc "Yeah, can't imagine any of them having some actual taste."
    dani.name "Could probably sell them actual piss and they would be fine."
    pc "Yeah right. If it's you pissing in a glass, they would pay double."
    dani.name "Only double?"
    $ player.drink(who=dani)
    $ relax(10)
    pc "Ha! Give it a go and tell me how much you make."
    dani.name "I think if there were money to be made from it, [trixie.name] would have it on the menu."
    pc "Probably. How are you keeping up with the work anyway?"
    dani.name "Fine I guess."
    pc "You guess?"
    $ player.drink(who=dani)
    $ relax(10)
    if school_dance_quest_show_count >= 11:
        dani.name "We pretty much flash our arses in the park and my tit's spill out when I lift my arms."
        dani.name "Bar clothes are modest by comparison."
    elif school_dance_quest_show_count >= 2:
        dani.name "We dance around the park with a shorter skirt, so not much difference there."
    else:
        dani.name "Still getting used to wearing a dress that shows my arse."
    $ player.drink(who=dani)
    $ relax(10)
    pc "But what about the actual work? Or I guess the money."
    dani.name "That's what I am talking about."
    pc "Huh?"
    dani.name "Dragging the beer over to the drunks is easy."
    dani.name "The real work is getting them to put their hand in their pocket and give you a tip."
    pc "Okay...?"
    dani.name "Showing your arse is the best way to get them to do that."
    $ player.drink(who=dani)
    $ relax(10)

    pc "Selling your arse gets even better money."
    if not pubpatron.name in dani.sex_who:
        dani.name "No thanks, I'll leave that job up to you and [trixie.name]."
        if not pub_waitress.sold:
            pc "Up to me? I haven't sold my arse in the pub."
            dani.name "Oh? I thought you had."
            pc "Na. At least not yet. Who knows when I get behind on rent."
        else:
            pc "Easy money if you don't mind some drunk with his booze breath slobbering on you."
            dani.name "Yeah, they try that even out in the open. Smokes and booze on their breath when they try to kiss me."
            pc "You will get used to it."
            dani.name "Probably. Would rather I didn't though."
    else:
        dani.name "Yeah. Wouldn't say that like it's a good thing."
        pc "Better than the alternatives."
        dani.name "I wonder..."
        if "slept_over" in loc_bedroom_dani.list:
            pc "Well, I won't be staying over with you if you decide to go sleep under a bridge."
            dani.name "No? That's a shame."
        else:
            pc "Well, go hang out under a bridge for a few nights and find out."
            dani.name "Maybe I will!"
            pc "Haha."
    $ player.drink(who=dani)
    $ relax(10)
    $ player.left_hand = ""
    dani.name "Out of wine?"
    pc "Yup."
    dani.name "Time to call it a night then I think."
    pc "Yeah."
    jump dani_drinking_wine_event_end


label dani_drinking_wine_event_pub2:
    $ add_to_list(dani.conversation_topics, "drinking_event_played_pub2")
    $ log.set_done("quest_daniwine_02")
    pc "You know, we really should just steal beer from work at this rate."
    show dani neutral
    dani.name "Ugh please no. I drink enough of that stuff with the perverts."
    pc "Free booze. Makes them easier to put up with."
    pc "Nnng!"
    with vpunch
    $ player.left_hand = "wine_bottle"
    $ player.face_neutral()
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "I suppose."
    pc "You suppose? You could do it all sober."
    dani.name "The drunk part isn't the issue."
    pc "Ah. That..."
    pc "You know you don't have to do that."
    $ player.drink(who=dani)
    $ relax(10)
    show dani worried
    dani.name "Sure I don't. I can go live under a bridge instead."
    $ player.face_happy()
    pc "It's free."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "..."
    pc "Hey now. I didn't get this wine for you to be all doom and gloom."
    dani.name "You ever have second thoughts about it?"
    $ player.drink(who=dani)
    $ relax(10)
    if not pub_waitress.sold:
        pc "I don't fuck guys in the toilets like you and [trixie.name]. So not really anything to have second thoughts about."
        dani.name "You don't? I've seen you sitting with those drunks."
        pc "Sure I sit with them. But that's about it."
        show dani neutral
        if pub_waitress.sex:
            dani.name "I'm sure I have seen you going off alone with someone."
            pc "Maybe. But not for money. Just some fun."
            dani.name "Oh..."
    else:
        pc "Dunno. Don't really think about it. Just do what I need to do."
        dani.name "..."
        pc "Plus I'm usually too drunk to care."
        dani.name "No matter how drunk I get, doesn't seem to help."
        pc "Well here, try some more."
        show dani happy
        dani.name "Haha."
    $ player.drink(who=dani)
    $ relax(10)
    pc "Well, at least you aren't at the highway."
    dani.name "That's not really a consolation."
    pc "It's supposed to be."
    dani.name "A terrible one."
    pc "It comes with wine."
    dani.name "..."
    dani.name "Better."
    pc "Not much left though."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "Yeah, and is getting late."
    jump dani_drinking_wine_event_end


label dani_drinking_wine_event_pubglory:
    $ add_to_list(dani.conversation_topics, "drinking_event_played_pub3")
    $ log.set_done("quest_daniwine_02")
    dani.name "More wine!"
    pc "Yup."
    pc "Nnng!"
    with vpunch
    $ player.left_hand = "wine_bottle"
    $ player.face_neutral()
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "..."
    dani.name "Was it you who made that hole in the toilet?"
    pc "What? Little old me? I would never do such a thing! That is pure vandalism!"
    dani.name "What made you come up with that idea?"
    pc "Eh, I didn't, not really. It was those perverts at the pitch."
    $ player.drink(who=dani)
    $ relax(10)
    pc "They wanted to make one at the academy. They say it in some porn book or something. No idea."
    dani.name "And you made one in the pub?"
    pc "Sure. Why not. Better a wall between you when you are sucking a dick."
    pc "Why are you asking anyway?"
    dani.name "No reason really..."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "It just seems no matter what I do these days, someone finds a way to use it as a way to put their dick in me."
    pc "Ah, well yeah. Although that's not much too different to before all this shit."
    dani.name "What do you mean?"
    pc "I mean guys have only ever wanted one thing. Just before some of them used more tactful methods to get it."
    pc "Now the world is shit, their only methods are money or force."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "Sometimes booze."
    pc "True."
    "We sit around, nursing the wine and relaxing. Mostly complaining about the work we do and the perverts we have to put up with."
    $ relax(10)
    $ player.drink(who=dani)
    $ relax(10)
    "[dani.name] doesn't seem like she is in the mood for fun conversation though and mostly wallows."
    $ relax(10)
    $ player.drink(who=dani)
    $ relax(10)
    $ player.left_hand = ""
    pc "Looks like we did good work on that wine."
    dani.name "Yeah."
    dani.name "Sorry for being such a downer."
    pc "Whatever. It is what it is."
    jump dani_drinking_wine_event_end


label dani_drinking_wine_event_dance1:
    $ add_to_list(dani.conversation_topics, "drinking_event_played_dance1")
    $ log.set_done("quest_daniwine_02")
    dani.name "More wine!"
    pc "Yup."
    pc "Nnng!"
    with vpunch
    $ player.left_hand = "wine_bottle"
    $ player.face_neutral()
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "Having fun with the dance?"
    pc "Yeah, not something I really did before, but I am having fun."
    dani.name "What made you join up anyway?"
    pc "Huh? Nothing."
    dani.name "Nothing?"
    pc "Yeah, [svet.nname] asked and I agreed."
    pc "New to the academy and no friends, so no reason to turn down meeting new people."
    dani.name "Thought you woul meet people quite easily."
    $ player.drink(who=dani)
    $ relax(10)
    pc "People who don't want to put their dick in me."
    if dani.sex_les:
        dani.name "Errr... I don't have a dick, but..."
        pc "Shush!"
    else:
        dani.name "Wouldn't be sure about that."
        pc "Well, none of the [dancet] has a dick."
        pc "I think."
    dani.name "Haha!"
    dani.name "Well, don't worry. All the folks watching will happily share theirs with you."
    pc "Yeah I'm sure they will. I'll send them off to [rachel.name]."
    dani.name "..."
    $ player.drink(who=dani)
    $ relax(10)
    pc "What?"
    dani.name "Is she... All there?"
    pc "Probably not."
    dani.name "Isn't it kinda wrong?"
    pc "Is what?"
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "Like if she isn't all there, shouldn't we kinda look after her or something?"
    pc "Dunno, she is the only happy one out of all of us. Maybe she should look after us."
    dani.name "Hmmm..."
    pc "Considering it?"
    dani.name "No, but also yes..."
    pc "Haha!"
    $ player.drink(who=dani)
    $ relax(10)
    pc "Go hang out with her, I'm sure you will have lot's of fun."
    dani.name "Yeah, and lot's of trouble."
    pc "Same thing depnding on how you look at it."
    $ player.drink(who=dani)
    $ relax(10)
    $ player.left_hand = ""
    pc "No more fun with this wine though."
    dani.name "Well, not the drinking kind anyway."
    pc "Shoo!"
    jump dani_drinking_wine_event_end


label dani_drinking_wine_event_dance2:
    $ add_to_list(dani.conversation_topics, "drinking_event_played_dance2")
    $ log.set_done("quest_daniwine_02")
    dani.name "More wine!"
    pc "Yup."
    pc "Nnng!"
    with vpunch
    $ player.left_hand = "wine_bottle"
    $ player.face_neutral()
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "What do you think of whats going on with the dance stuff?"
    pc "What do you mean?"
    dani.name "I mean the clothes are getting less and less."
    pc "Hmmm..."
    pc "Dancing usually does involve not much clothes."
    pc "Well, before anyway. Wasn't most of what you saw on TV with pop stars basically soft porn?"
    dani.name "Yeah, but a bit different in the park with the perverts in front of you."
    pc "Just don't look at them wanking."
    if dani.iswhore:
        dani.name "They might want to buy me if I did."
    elif player.iswhore:
        pc "Might try and buy one of us if you do."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "So you don't have an issue with it all?"
    if player.has_perk(perk_exhibitionist, notif=True):
        pc "No, I like showing off. Let the perverts look."
    elif player.has_perk([perk_whore, perk_sucu], notif=True):
        pc "Not really. The perverts could at least pay for a private dance or something."
    elif player.has_perk([perk_slut, perk_bimbo, perk_party_girl], notif=True):
        pc "Not really. I don't mind a little bit of fun like that."
    elif player.has_perk([perk_broken, perk_meek], notif=True):
        pc "Guys just do as they want no matter how I am dressed."
    else:
        pc "Dunno, guess if I had an issue with it, I would stop going."
    dani.name "There are worse ways to earn a bit of money I suppose."
    pc "Yeah, once you see the girls at the highway doing their work, you start to care a lot less about this stuff."
    dani.name "Yeah? It's pretty bad so I hear."
    pc "The only lower you go from there is the grave."
    dani.name "Fun..."
    $ player.drink(who=dani)
    $ relax(10)
    pc "Act like [rachel.name]. Just enjoy what it is."
    dani.name "Yeah, shaking our asses for the perverts."
    pc "Tits as well."
    if player.breasts == 3:
        dani.name "You and [anabel.nname] maybe. Not the rest of us."
    else:
        dani.name "Well, [anabel.nname] does that the best."
    pc "Dancing was always going to come to this anyway."
    dani.name "What do you mean."
    pc "We live in this shithole. Is there anything anyone does that doesn't involve someone trying to put their dick in you?"
    dani.name "Hmm, handing out flyers?"
    pc "Pfft. Flyers, cleaning, scavving. The moment you are alone, someone is trying to drag you off into the bushes."
    dani.name "Not true!"
    dani.name "Sometimes they don't even bother to drag you to the bushes."
    pc "Ha!"
    $ player.drink(who=dani)
    $ relax(10)
    pc "Showing our asses off in the park, we at least have each other so somewhat protected."
    pc "Much harder to drag us off."
    dani.name "Yeah, so the have to put their hand in their pocket and pay instead."
    pc "Yup."
    $ player.drink(who=dani)
    $ relax(10)
    $ player.left_hand = ""
    pc "That bottle was an hour of park dancing."
    dani.name "Hmm, that puts it in perspective."
    dani.name "More ass shaking means more wine."
    pc "Yup."
    jump dani_drinking_wine_event_end


label dani_drinking_wine_event_dancewhore:
    $ add_to_list(dani.conversation_topics, "drinking_event_played_dancewhore")
    $ log.set_done("quest_daniwine_02")
    dani.name "More wine!"
    pc "Yup."
    pc "Nnng!"
    with vpunch
    $ player.left_hand = "wine_bottle"
    $ player.face_neutral()
    $ player.drink(who=dani)
    $ relax(10)
    pc "Might need it to wash down your dance friend."
    dani.name "Ah him."
    pc "To be expected I guess. We are out there showing our asses off."
    dani.name "Yeah, suprised more people dont come up."
    pc "Well, they kinda do. Hands everywhere when we go begging for some money."
    dani.name "It's not begging. We are working for it."
    pc "Ha, sure."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "Some entertainment for the sad people."
    if quest_dancevip.active:
        pc "Well, at least your ass got us that dance party gig."
        dani.name "Yeah, my ass getting all of yours into trouble."
        pc "I'm sure no one minds."
        dani.name "Except [anabel.name]..."
        pc "Except her..."
    else:
        pc "Going to have a lot more offers no doubt."
        dani.name "Yeah, probably."
        pc "What you going to do about it?"
        if dani.iswhore:
            dani.name "Take the moneyof course."
            pc "Yeah, keeps us fed."
        else:
            dani.name "Not sure. Not something I want to do, but I need the money."
            pc "Yeah, no good having dignity when you are dead."

    $ player.drink(who=dani)
    $ relax(10)
    dani.name "People come expecting us now."
    pc "Yeah, what else do they have to do in life?"
    dani.name "Go to the pub?"
    pc "They probably already do afterwards. We dance early."
    dani.name "Ha, we are the pre party."
    $ player.drink(who=dani)
    $ relax(10)
    pc "Go watch the girls in the park then get plastered in the pub."
    pc "Probably stagger to the highway for a whore."
    dani.name "Hmm, you been to the highway?"
    if loc_truckstop.visited:
        if quest_whore.active and quest_whore.sex:
            pc "Yeah, did some work there..."
            dani.name "Wait, work?"
            pc "Not only you who is desperate for cash."
            dani.name "Yeah, but I didn't realise..."
            pc "It's fine. Gotta do what you gotta do."
        else:
            pc "Yeah, a lot of desperate people there."
            dani.name "You mean whores?"
            pc "Well, desperate whores."
            pc "Most of them are homeless or addicts."
    else:
        pc "Not really, but I have heard about it."
        dani.name "Same. Where all the true whores work."
        pc "True whores?"
        dani.name "Yeah, like people who stand around and offer sex. Or try to attract people."

    $ player.drink(who=dani)
    $ relax(10)
    pc "Well, not a shock a lot of people are like that."
    pc "We shake our ass for money. Not much of a difference."
    dani.name "Less cleanup."
    pc "Haha!"
    pc "Got to go past that place to get this wine."
    dani.name "Hope it only costs money."
    pc "Ha, my ass would probably be cheaper."
    $ player.drink(who=dani)
    $ relax(10)
    $ player.left_hand = ""
    pc "I'll pick some more up next time I am going there."
    jump dani_drinking_wine_event_end


label dani_drinking_wine_event_anabeldrift:
    $ add_to_list(dani.conversation_topics, "drinking_event_played_anabeldrift")
    $ log.set_done("quest_daniwine_02")
    dani.name "More wine!"
    pc "Yup."
    pc "Nnng!"
    with vpunch
    $ player.left_hand = "wine_bottle"
    $ player.face_neutral()
    dani.name "Nice to have a drink with you, can't do this with [anabel.nname]."
    pc "No, she doesn't seem the type."
    dani.name "..."
    $ player.drink(who=dani)
    $ relax(10)
    pc "You good with [anabel.name]?"
    dani.name "Err, somewhat."
    dani.name "Not really."
    dani.name "Dunno..."
    pc "Don't see you two hanging out together so much anymore."
    dani.name "We do... It's just..."
    dani.name "I don't even know. Kinda don't want to talk about it."
    pc "Right, no problem."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "I just don't get it. I need to earn money or die, and she acts like dying should be an option."
    pc "..."
    dani.name "I can't really talk to her about stuff anymore. She doesn't sympathise or something."
    dani.name "Just tells me off as if I am doing something bad."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "It's not like I want to do the stuff I have to do. I would rather earn money working a nice office job or something."
    dani.name "But that's not an option these days. So when I do talk about what happened yesterday or something, I don't wanna be judged."
    pc "Yeah, I can see that getting annoying."
    dani.name "Whatever."
    pc "Well, to new friends then."
    dani.name "Ones that won't shit on me for trying to survive."
    pc "You don't have enough money to pay me to do that for you."
    dani.name "Ha, for once no money is a good thing."
    dani.name "Never been asked for that actually."
    pc "Thank fuck!"
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "The perverts do ask for some weird things though."
    pc "Yeah, don't even need to tell me. It's like they say any old random shit just to get at us."
    dani.name "Kinda feel bad for the whores at the highway, they probably accept the weird requests."
    pc "Probably."
    if player.iswhore:
        pc "I mean, I might also accept if the money was good enough."
    elif dani.iswhore:
        dani.name "If the money was good enough though... Might do it."
    $ player.drink(who=dani)
    $ relax(10)
    $ player.left_hand = ""
    pc "That's the bottle empty. How much to put it up your arse?"
    dani.name "Hmmm, maybe I will give you a friends discount."
    pc "Oh? Then when I am not broke anymore, I'll come and give it a try."
    dani.name "Ha, sure."
    jump dani_drinking_wine_event_end


label dani_drinking_wine_event_partyfinal:
    $ add_to_list(dani.conversation_topics, "drinking_event_played_partyfinal")
    $ log.set_done("quest_daniwine_02")
    dani.name "Wine wine wine!"
    pc "Yup."
    pc "Nnng!"
    with vpunch
    $ player.left_hand = "wine_bottle"
    $ player.face_neutral()
    pc "With all this party stuff, might get sick of the wine like with the pub beer."
    dani.name "Well not sick of it yet. Think we can get some vodka?"
    pc "Hmmm, maybe?"
    pc "Not sure I fancy being tat piss drunk though."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "Would be fun to see."
    pc "Sure, as long as you aren't the one suffering the hangover."
    dani.name "[rachel.name] was getting pretty wild."
    pc "Yeah, but that is pretty much how she always is."
    dani.name "Think she would go there for free?"
    pc "I know for a fact she would."
    if player.has_perk([perk_party_girl, perk_alcoholic]):
        pc "Probabl join her myself. Free booze at a party is a lot better than anything else I will be doing."
    elif player.has_perk([perk_slut, perk_bimbo, perk_sucu, perk_gamine]):
        pc "Hell, might even go myself just to have something nice to do."
    elif player.has_perk([perk_meek, perk_bambi]):
        pc "Was pretty scary going even with you guys, no way I could go on my own."
    else:
        pc "Although, not like there is much else to do. The party might be fun at least."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "All those perverts there. Would be way worse going alone."
    pc "True, but perverts everywhere."
    pc "They might get handsy, but I doubt anyone there is going to drag you off and rape you."
    dani.name "No, just get you drunk so you pass out, then pass your body around."
    pc "Yeah, they would probably do that..."
    pc "But again, no different to pretty much anywhere else."
    dani.name "Don't get drunk."
    $ player.face_meek()
    pc "Errr..."
    pc "Should I put the booze down?"
    $ player.face_neutral()
    dani.name "Don't think I'll be raping your passed out body."
    $ player.drink(who=dani)
    $ relax(10)
    pc "No? Then maybe I'll do it to you."
    dani.name "Sure. I think you would rather me pass out just so you can hog all the wine to yourself."
    pc "Well, at first at least."
    pc "Then I might draw a moustache on you."
    dani.name "Haha!"
    dani.name "I don't have a mirror here. Might end up going out with it."
    pc "I'm sure the people outside would love it."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "They would love anything involving a woman."
    pc "Well, don't get drunk and pass out."
    if "bad_end" in anabel.list:
        dani.name "I poked my head in to see where [anabel.nname] went during the party."
        pc "Ugh, yeah..."
        dani.name "Always telling me off for doing what I do, then give her a few wines and she is even worse."
        pc "Should have known she wouldn't be able to handle a party like that."
        dani.name "It's not like they were raping her. She was encouraging them."
        dani.name "Damn bitch always nagging me then she runs off and fucks half the damn party."
        pc "..."
        dani.name "Whatever. At least she will shut up nagging me or I'll remind her of it."
        pc "Assuming she ever talks to us again."
    else:
        dani.name "[anabel.nname] managed to stay onher feet at the party."
        if "anabel_help" in quest_dancevip.list:
            pc "Yeah, I ended up looking out for her."
            dani.name "Oh?"
            pc "Ugh, the idiot was like a chicken surrounded by foxes."
            pc "If I didn't calm her down, half the party would have fucked her by the end of the night."
            dani.name "Wouldn't have minded seeing that."
        else:
            pc "Yeah, kinda shocked actually."
            dani.name "Same. I thought she would have been tasty meat to the perverts."
            dani.name "Almost wish she had to eat her words. Always nagging me."

    $ player.drink(who=dani)
    $ relax(10)
    $ player.left_hand = ""
    pc "Next time should steal some wine from the party."
    dani.name "They have so much of it."
    jump dani_drinking_wine_event_end



label dani_drinking_wine_event_preg:
    $ add_to_list(dani.conversation_topics, "drinking_event_played_preg")
    $ log.set_done("quest_daniwine_02")
    dani.name "More wine!"
    pc "Yup."
    pc "Nnng!"
    with vpunch
    $ player.left_hand = "wine_bottle"
    $ player.face_neutral()
    if dani.showing:
        pc "Should you actually be drinking?"
        dani.name "Huh? Why not?"
        pc "Err, the belly?"
        if player.showing:
            dani.name "I could ask you the same."
            pc "Hmmm."
    else:
        dani.name "So not worried about drinking with that belly?"
        pc "Should I be?"
        dani.name "Probably not. Just thought I would ask."

    $ player.drink(who=dani)
    $ relax(10)
    dani.name "They force us to have this thing almost none of us want, then take it away from us."
    dani.name "Like we are just cows in a farm or something."
    pc "Mooo!"
    dani.name "Ha, I guess we pretty much are."
    pc "So who gives a shit how it turns out?"
    dani.name "Yeah, let those who forced this on us deal with it."
    pc "Cold."
    dani.name "Not as cold as forcing us."
    pc "..."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "You don't agree?"
    pc "I do. I just thought I was the only one who didn't care."
    dani.name "Pfft. Probably what most think. Especially when you think of the people who work as whores."
    if player.has_perk(perk_whore):
        pc "True. It's pretty much just an extra perk to charge for."
        dani.name "People pay more for it?"
        pc "They pay more for anything that's not standard."
        pc "They pay a lot to try and knock us up. And some people like fucking an already pregnant whore."
        dani.name "I guess perverts will pay for almost anything."
        pc "Pretty much."
    else:
        pc "Hope they have some shady way to get pills or something."
        dani.name "Probably expensive."
        pc "Yeah, cheaper just to see it though."

    $ player.drink(who=dani)
    $ relax(10)
    pc "Probably not even a bad thing for them."
    dani.name "What do you mean?"
    pc "If it comes out half brained, it's probably a good thing for them. Easier to brainwash."
    dani.name "Haha. Maybe."
    pc "Do you actually know what happens to them?"
    dani.name "Just what they tall us. Taken to be raised by more fitting people."
    pc "Yeah, so they say."
    $ player.drink(who=dani)
    $ relax(10)
    dani.name "You think something else?"
    pc "Somewhat. I'm sure some go to good parents, but these orphanages..."
    pc "Kinda sounds like some kind of brainwashing center."
    dani.name "Err, they don't quite make a secret of that."
    pc "They don't? Not really looked into it so not sure what they actually say."
    dani.name "To raise the next generation to be model citizens to rebuild."
    dani.name "Or something like that."
    pc "Ah well, at least tey are fed."
    $ player.drink(who=dani)
    $ relax(10)
    $ player.left_hand = ""
    dani.name "That the wine over?"
    pc "Yeah."
    dani.name "Okay, I will call it a night before this topic get's more depressing."
    jump dani_drinking_wine_event_end


label dani_drinking_wine_event_end:
    $ player.left_hand = ""
    if not "can_sleep" in loc_bedroom_dani.list:
        $ add_to_list(loc_bedroom_dani.list, "can_sleep")
        $ loc_bedroom_dani.home_location = True
        pc "Well, let me get out the window before you lay down."
        dani.name "Sure. But you can stay y'know."
        pc "It's not really a long scary walk home."
        dani.name "Yeah I know. But would be nice. Some company in this shithole."
        if player.tired >= 80 and not player.has_perk(perk_sucu):
            pc "Na, not really tired. I am going to find something else to do."
            jump dani_drinking_sleepoffer_first_reject
        menu:
            "Stay the night":
                jump dani_sleepover_start
            "Another time":
                jump dani_drinking_sleepoffer_first_reject
    else:
        dani.name "You going to stay over tonight?"
        if dani.assault:
            pcm "Considering what she did before, this might not be a good idea."
        menu:
            "Stay the night":
                $ add_to_list(loc_bedroom_dani.list, "slept_over")
                jump dani_sleepover_start
            "Another time":
                pc "No, I'll head off home."
                dani.name "Okay, be safe."
                hide dani
                $ walk(loc_stairwell)
                pc "That was nice."
                jump travel


label dani_drinking_sleepoffer_first_reject:
    dani.name "No problem, but my door is always open for you."
    pc "You got a new door?"
    dani.name "My window."
    pc "Sure. I'll creep in when I want like a rapist."
    dani.name "Haha."
    pc "Good night."
    dani.name "Bye."
    hide dani
    $ walk(loc_stairwell)
    pc "That was nice."
    jump travel




label dani_drinking_wine_event_repeatable:
    $ log.set_done("quest_daniwine_02")
    dani.name "More wine!"
    pc "Yup."
    pc "Nnng!"
    with vpunch
    $ player.left_hand = "wine_bottle"
    $ player.face_neutral()

    call dani_drinkwine_subject_repeatable from _call_dani_drinkwine_subject_repeatable
    $ player.drink(who=dani)
    $ relax(10)

    pc "Drink up."
    dani.name "Mmm."

    call dani_drinkwine_subject_repeatable from _call_dani_drinkwine_subject_repeatable_1
    $ player.drink(who=dani)
    $ relax(10)

    dani.name "Ohh this goes down well."

    call dani_drinkwine_subject_repeatable from _call_dani_drinkwine_subject_repeatable_2
    $ player.drink(who=dani)
    $ relax(10)

    pc "Starting to feel this wine."

    call dani_drinkwine_subject_repeatable from _call_dani_drinkwine_subject_repeatable_3
    $ player.drink(who=dani)
    $ relax(10)

    pc "Bottle almot done."
    dani.name "Aww."

    call dani_drinkwine_subject_repeatable from _call_dani_drinkwine_subject_repeatable_4
    $ player.drink(who=dani)
    $ relax(10)
    $ player.left_hand = ""
    dani.name "Aww, no more wine."
    pc "More another time."
    jump dani_drinking_wine_event_end


label dani_drinkwine_subject_repeatable:





    call expression WeightedChoice([


    ("dani_drinking_wine_event_repeatable_sing", If(not "sing" in quest_daniwine.conversation_topics, 100, 0)),
    ("dani_drinking_wine_event_repeatable_preg", If(not "preg" in quest_daniwine.conversation_topics and player.showing, 100, 0)),
    ("dani_drinking_wine_event_repeatable_school", If(not "school" in quest_daniwine.conversation_topics, 100, 0)),
    ("dani_drinking_wine_event_repeatable_rachel", If(not "rachel" in quest_daniwine.conversation_topics, 100, 0)),
    ("dani_drinking_wine_event_repeatable_winebuy", If(not "winebuy" in quest_daniwine.conversation_topics, 100, 0)),
    ("dani_drinking_wine_event_repeatable_whore", If(not "whore" in quest_daniwine.conversation_topics and all([player.iswhore, dani.iswhore]), 100, 0)),
    ("dani_drinking_wine_event_repeatable_knockup", If(not "knockup" in quest_daniwine.conversation_topics and all([player.iswhore, dani.iswhore]), 100, 0)),
    ("dani_drinking_wine_event_repeatable_svet", If(not "svet" in quest_daniwine.conversation_topics, 100, 0)),
    ("dani_drinking_wine_event_repeatable_felix", If(not "felix" in quest_daniwine.conversation_topics, 100, 0)),
    ("dani_drinking_wine_event_repeatable_oskar", If(not "oskar" in quest_daniwine.conversation_topics, 100, 0)),
    ("dani_drinking_wine_event_repeatable_flyers", If(not "flyers" in quest_daniwine.conversation_topics and quest_flyers.isactive(), 100, 0)),

    ("dani_drinking_wine_event_repeatable_reset", 1), 
    
    ]) from _call_expression_27
    return


label dani_drinking_wine_event_repeatable_reset:


    pc "Wonder what other drinks we can get our hands on?"
    dani.name "Fed up with the wine?"
    pc "No, just curious. They used to have a huge variety back before."
    dani.name "Yeah, probably cost way more than we could afford though."
    pc "Thats almost the case with this."
    dani.name "Ture. I only manage it because you keep trying to get me drunk."
    pc "Trying?"
    dani.name "I am totally sober!"
    $ quest_daniwine.conversation_topics = []
    return



label dani_drinking_wine_event_repeatable_sing:
    $ add_to_list(quest_daniwine.conversation_topics, "sing")
    pc "[rlist.singing_dialogue_1]"
    pc "[rlist.singing_dialogue_2]"
    pc "[rlist.singing_dialogue_3]"
    pc "[rlist.singing_dialogue_4]"
    dani.name "Whooo!"
    return

label dani_drinking_wine_event_repeatable_preg:
    $ add_to_list(quest_daniwine.conversation_topics, "preg")
    dani.name "Wine with that belly?"
    pc "Yeah, not like it's my baby."
    dani.name "Err, is it secretly [rachel.name]'s?"
    pc "Ha, no. I mean i'm forced to have it and then give it away. Why should I care?"
    dani.name "Ah, yeah I guess."
    return

label dani_drinking_wine_event_repeatable_school:
    $ add_to_list(quest_daniwine.conversation_topics, "school")
    pc "Weird that they have the academy opened up."
    dani.name "Yeah, something nice we don't have to pay for."
    pc "Yeah, no one else is doing anything remotely charitable, then you have that place."
    dani.name "Maybe it's a secret plan to get all the girls dressed in school uniforms."
    pc "Hmmm, I might actually believe that over someone being nice."
    return

label dani_drinking_wine_event_repeatable_rachel:
    $ add_to_list(quest_daniwine.conversation_topics, "rachel")
    dani.name "No idea how [rachel.name] manages to get by."
    pc "Pretty sure she almost doesn't."
    pc "She deals with way more shit than we do."
    dani.name "She does?"
    pc "Well she isn't exactly... Y'know. That makes her an easy target."
    dani.name "She never really complains about it."
    pc "The same thing that makes her a target also makes it so she doesn't realise how shit the things that are happening are."
    dani.name "Ah..."
    return

label dani_drinking_wine_event_repeatable_winebuy:
    $ add_to_list(quest_daniwine.conversation_topics, "winebuy")
    dani.name "You okay getting this stuff?"
    pc "What do you mean?"
    dani.name "Didn't you say you had to go somewhere shady to get it?"
    pc "Ah. Yeah."
    pc "Not quite shady. It's a proper shop, kind of. Just in the slums near the highway."
    dani.name "Ah, dangerous round there."
    pc "Can be at night."
    dani.name "Hope you won't get into some trouble getting it."
    pc "If I do, then next time I'll sell your ass for a few bottles."
    return

label dani_drinking_wine_event_repeatable_whore:
    $ add_to_list(quest_daniwine.conversation_topics, "whore")
    dani.name "So what is te weirdest thing a customer ever asked you for."
    pc "Hmmm, they don't usually ask for anything specific."
    pc "Drunk shits are usually so messed up that they are leaking before I even bend over."
    dani.name "Hmm, doesn't seem that way with me."
    pc "They ask for weird stuff?"
    dani.name "Well no. Can't say they ask. They just call me weird things as if it's normal."
    pc "Ah, yeah they do that with me as well. It is kinda normal."
    dani.name "It is?"
    pc "It isnt?"
    return

label dani_drinking_wine_event_repeatable_knockup:
    $ add_to_list(quest_daniwine.conversation_topics, "knockup")
    dani.name "So, like do the guys pretty much ignore you when you tell them to pull out?"
    pc "Ugh, yeah. All the time."
    pc "Pretty much expect it now. It's nice when they listen but not worth the fuss of fighting them when they don't."
    dani.name "Yeah... Pretty much the same with me."
    if dani.showing:
        pc "Yeah I can see that."
        if player.showing:
            dani.name "Yeah, like you can talk."
    pc "I guess it's why half the girls around here have fat bellies."
    dani.name "That and hard to get pills."
    pc "Expensive too. If whoring you need to make enough to pay for those."
    dani.name "I didn't really buy any."
    pc "Lose money on pills or get fat with money and a baby."
    dani.name "Pretty much."
    return

label dani_drinking_wine_event_repeatable_svet:
    $ add_to_list(quest_daniwine.conversation_topics, "svet")
    pc "So [svet.nname] started the dance troupe?"
    dani.name "Yeah, when I arrived I saw her and [rachel.name] dancing in the gym."
    dani.name "Spoke to [anabel.nname] about it and we decided to see what it was all about."
    dani.name "Wasn't doin much else and new friends can be good. So he hung out with them."
    pc "Was kinda shocked when I got asked on the team."
    dani.name "More people more fun."
    pc "Yeah."
    return

label dani_drinking_wine_event_repeatable_felix:
    $ add_to_list(quest_daniwine.conversation_topics, "felix")
    pc "You hang out with [felix.name] much?"
    dani.name "Not really. Some photos now and then."
    pc "Oh? What kind?"
    if felix in dani.sex_who_class:
        dani.name "Err... Usually of us having sex. That or really naughty photos."
        pc "Oh? I need to speak to him and see those."
        dani.name "Pretty sure he would make them with you as well."
    else:
        dani.name "Weird ones. Sexy ones that aren't sexy."
        pc "Ah yeah, same with me. Stand there all normal and smile. But stick your chest out or pull your shorts up the crack of your arse."
        dani.name "Haha yeah."
    return

label dani_drinking_wine_event_repeatable_oskar:
    $ add_to_list(quest_daniwine.conversation_topics, "oskar")
    pc "Still having your fun with [oskar.name]?"
    dani.name "Ugh, don't remind me."
    pc "If you pay cash, will he stop coming?"
    dani.name "Dunno, never tried. I assumed he would come anyway so I usually spend most of my money first."
    dani.name "Give him whats left over."
    pc "You still pay him something?"
    dani.name "Yeah, I don't want him pushing too much. Offering his goons to have a turn or something."
    dani.name "Giving him something keeps him off my back."
    dani.name "Well, figuratively off my back."
    return

label dani_drinking_wine_event_repeatable_flyers:
    $ add_to_list(quest_daniwine.conversation_topics, "flyers")
    pc "Market has some flyer job you can do."
    dani.name "Yeah I tried that out for a bit."
    pc "Oh? Not like it or something?"
    dani.name "It was fine, just didn't pay enough."
    dani.name "Was pretty good to earn a little bit of cash without having to turn up at a specific time."
    pc "Yeah, can just do it when you have a bit of free time."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
