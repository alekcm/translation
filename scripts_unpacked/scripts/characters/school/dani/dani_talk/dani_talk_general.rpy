label dani_talk_subject:
    call dani_talk_init from _call_dani_talk_init_1
    if not renpy.showing("dani"):

        show dani at right1 with dissolve
    jump expression WeightedChoice([
    
    
    ("dani_talk_general_1", 100),
    ("dani_talk_general_2", 100),
    ("dani_talk_general_3", 100),
    ("dani_talk_general_4", 100),
    ("dani_talk_general_5", 100),

    ("dani_talk_wine_reminder_haswine", If(log.interactive("quest_daniwine_02") and inv.qty(item_winebottle) and not t.wkday in ["Wednesday", "Thursday", "Friday", "Saturday"], 100, 0)),
    ("dani_talk_wine_reminder_nowine", If(log.interactive("quest_daniwine_02") and not inv.qty(item_winebottle), 50, 0)),

    
    ("dani_talk_courtyard_1", If(loc(loc_stairwell), 100, 0)),
    ("dani_talk_courtyard_2", If(loc(loc_stairwell) and not renpy.has_label("oskar_sex_talk_" + str(dani.dict["oskar_sex_talk"])), 100, 0)),
    ("dani_talk_courtyard_3", If(loc(loc_stairwell), 100, 0)),

    
    ("dani_talk_perk_ex_1", If(dani.love > 60 and player.has_perk(perk_exhibitionist), 100, 0)),
    ("dani_talk_perk_ex_2", If(dani.love > 60 and player.has_perk(perk_exhibitionist), 100, 0)),
    ("dani_talk_perk_bimbo_1", If(dani.love > 60 and player.has_perk(perk_bimbo) and rachel.love > 20, 100, 0)),
    ("dani_talk_perk_bimbo_2", If(dani.love > 60 and player.has_perk(perk_bimbo) and rachel.love > 20, 100, 0)),
    ("dani_talk_perk_gym_1", If(dani.love > 60 and player.has_perk(perk_gym_bunny), 100, 0)),
    ("dani_talk_perk_slut_1", If(dani.love > 60 and player.has_perk(perk_slut), 100, 0)),
    ("dani_talk_perk_pregwant_1", If(dani.love > 60 and player.has_perk(perk_preg_want) and not player.showing, 100, 0)),
    ("dani_talk_perk_slutty_1", If(dani.love > 60 and player.has_perk(perk_slutty), 100, 0)),
    
    

    ("dani_talk_dance_1", If(school_dance_quest_show_count > 2, 100, 0)),
    ("dani_talk_dance_1", If(school_dance_quest_show_count > 2, 100, 0)),
    ("dani_talk_dance_1", If(school_dance_quest_show_count > 5, 100, 0)),
    ("dani_talk_dance_1", If(school_dance_quest_show_count > 2, 100, 0)),
    ("dani_talk_dance_1", If(school_dance_quest_show_count > 2, 100, 0)),
    ("dani_talk_dance_1", If(school_dance_quest_show_count > 2, 100, 0)),

    

    
    ("dani_talk_pubwork_1", If(dani.dict["talk_workingpub_chain"] and not renpy.has_label("dani_talk_workingpub_chain_" + str(dani.dict["talk_workingpub_chain"])), 100, 0)),
    ("dani_talk_pubwork_2", If(dani.dict["talk_workingpub_chain"] and not renpy.has_label("dani_talk_workingpub_chain_" + str(dani.dict["talk_workingpub_chain"])), 100, 0)),
    ("dani_talk_pubwork_3", If(dani.dict["talk_workingpub_chain"] and not renpy.has_label("dani_talk_workingpub_chain_" + str(dani.dict["talk_workingpub_chain"])), 100, 0)),
    ("dani_talk_pubwork_4", If(dani.dict["talk_workingpub_chain"] and not renpy.has_label("dani_talk_workingpub_chain_" + str(dani.dict["talk_workingpub_chain"])), 100, 0)),
    ("dani_talk_pubwork_5", If(dani.dict["talk_workingpub_chain"] and not renpy.has_label("dani_talk_workingpub_chain_" + str(dani.dict["talk_workingpub_chain"])), 100, 0)),
    ("dani_talk_pubwork_6", If(dani.dict["talk_workingpub_chain"] and not renpy.has_label("dani_talk_workingpub_chain_" + str(dani.dict["talk_workingpub_chain"])), 100, 0)),
    
    
    ("dani_talk_pubwhore_1", If(dani.dict["talk_whoringpub_chain"] and not renpy.has_label("dani_talk_whoreingpub_chain_" + str(dani.dict["talk_whoringpub_chain"])), 100, 0)),
    ("dani_talk_pubwhore_2", If(dani.dict["talk_whoringpub_chain"] and not renpy.has_label("dani_talk_whoreingpub_chain_" + str(dani.dict["talk_whoringpub_chain"])), 100, 0)),
    ("dani_talk_pubwhore_3", If(dani.dict["talk_whoringpub_chain"] and not renpy.has_label("dani_talk_whoreingpub_chain_" + str(dani.dict["talk_whoringpub_chain"])), 100, 0)),
    ("dani_talk_pubwhore_4", If(dani.dict["talk_whoringpub_chain"] and not renpy.has_label("dani_talk_whoreingpub_chain_" + str(dani.dict["talk_whoringpub_chain"])), 100, 0)),
    ("dani_talk_pubwhore_5", If(dani.dict["talk_whoringpub_chain"] and not renpy.has_label("dani_talk_whoreingpub_chain_" + str(dani.dict["talk_whoringpub_chain"])) and quest_whore.sold > 5, 100, 0)),
    ("dani_talk_pubwhore_6", If(dani.dict["talk_whoringpub_chain"] and not renpy.has_label("dani_talk_whoreingpub_chain_" + str(dani.dict["talk_whoringpub_chain"])), 100, 0)),

    
    ("dani_talk_pubgloryhole_1", If(dani.dict["talk_gloryholepub_chain"] and not renpy.has_label("dani_talk_gloryholepub_chain_" + str(dani.dict["talk_gloryholepub_chain"])), 100, 0)),
    ("dani_talk_pubgloryhole_2", If(dani.dict["talk_gloryholepub_chain"] and not renpy.has_label("dani_talk_gloryholepub_chain_" + str(dani.dict["talk_gloryholepub_chain"])), 100, 0)),
    ("dani_talk_pubgloryhole_3", If(dani.dict["talk_gloryholepub_chain"] and not renpy.has_label("dani_talk_gloryholepub_chain_" + str(dani.dict["talk_gloryholepub_chain"])), 100, 0)),
    ("dani_talk_pubgloryhole_4", If(dani.dict["talk_gloryholepub_chain"] and not renpy.has_label("dani_talk_gloryholepub_chain_" + str(dani.dict["talk_gloryholepub_chain"])), 100, 0)),
    ("dani_talk_pubgloryhole_5", If(dani.dict["talk_gloryholepub_chain"] and not renpy.has_label("dani_talk_gloryholepub_chain_" + str(dani.dict["talk_gloryholepub_chain"])), 100, 0)),

    
    ("dani_talk_danifirst_preg_1", If(dani.love > 20 and dani.preg == 0 and player.pregnancy >= 2, 100, 0)),
    ("dani_talk_danifirst_preg_2", If(dani.love > 20 and dani.preg == 0 and player.pregnancy >= 2, 100, 0)),
    ("dani_talk_danifirst_danipreg_1", If(dani.love > 20 and dani.showing and dani.pregbabies == 0 and player.pregbabies, 100, 0)),
    ("dani_talk_danifirst_danipreg_2", If(dani.love > 20 and dani.showing and dani.pregbabies == 0 and player.pregbabies, 100, 0)),
    ("dani_talk_danipreg_1", If(dani.love > 20 and dani.showing, 100, 0)),
    ("dani_talk_danipreg_2", If(dani.love > 20 and dani.showing, 100, 0)),
    ("dani_talk_preg_1", If(dani.love > 20 and player.showing, 100, 0)),
    ("dani_talk_preg_2", If(dani.love > 20 and player.showing, 100, 0)),
    ("dani_talk_preglate_1", If(dani.love > 40 and player.has_perk(perk_period_late), 100, 0)),
    ("dani_talk_preglate_2", If(dani.love > 40 and player.has_perk(perk_period_late), 100, 0)),
    
    ])





label dani_talk_general_1:
    pc "How you doing?"
    dani.name "Same as always. Scraping by to make rent."
    pc "Flash [oskar.name] a winning smile."
    dani.name "Yeah..."
    jump dani_talk_end

label dani_talk_general_2:
    dani.name "Doing well with the dance, did you do it before?"
    pc "Not really. Other than with some Vodka in a nightclub."
    dani.name "Haha. Why does that not surprise me?"
    pc "Don't knock it until you try it."
    jump dani_talk_end

label dani_talk_general_3:
    dani.name "[name]!"
    pc "Hey, what you up to?"
    dani.name "Nothing. Like always."
    pc "Yeah..."
    jump dani_talk_end

label dani_talk_general_4:
    dani.name "Hey [name]. How's things?"
    pc "Same as always, scraping by."
    dani.name "Yeah, no change there then."
    pc "Yeah..."
    jump dani_talk_end

label dani_talk_general_5:
    dani.name "Hey [name]. How's things?"
    pc "Same as always, scraping by."
    dani.name "Yeah, no change there then."
    pc "Yeah..."
    jump dani_talk_end





label dani_talk_wine_reminder_haswine:
    dani.name "I am off work tonight if you want to come over with some wine."
    pc "Sure, I'll pop by if I am free."
    dani.name "Sounds good."
    jump dani_talk_end

label dani_talk_wine_reminder_nowine:
    dani.name "Manage to gt any wine?"
    pc "Not yet, I'll keep my eye out."
    dani.name "Would be nice."
    jump dani_talk_end





label dani_talk_courtyard_1:
    pc "Still hanging out here?"
    dani.name "Yeah, safer."
    jump dani_talk_end

label dani_talk_courtyard_2:
    pc "Thought you hanging here would attract [oskar.name] to want to do something."
    dani.name "Not really. And even if it does, better than hanging out elsewhere."
    pc "Hmm, true."
    jump dani_talk_end

label dani_talk_courtyard_3:
    pc "You meet anyone else while hanging out here?"
    dani.name "No, everyone looks at me like I'm a weirdo and avoids me."
    pc "Oh? Maybe I should do the same. Ruining my street credit here."
    dani.name "Haha."
    jump dani_talk_end






label dani_talk_perk_ex_1:
    dani.name "Hope you aren't getting into trouble with your running around naked."
    pc "Err..."
    dani.name "Err what? This is going t get you into trouble."
    pc "It's the risk of trouble that makes it fun."
    dani.name "I'll tell that to your corpse."
    jump dani_talk_end

label dani_talk_perk_ex_2:
    dani.name "Hope you aren't like those weirdos that run around the park."
    if quest_wolfgang.active:
        pc "Errr..."
        pc "Maybe..."
        dani.name "Ugh. I avoid the park because of you weirdos."
        pc "Actually it's fine there. The wierdos will protect you."
        dani.name "Yeah, protect me with their cock in my ass."
    else:
        pc "Dunno, it's you that has fun with the park weirdos."
        dani.name "Yeah right. Can't even go to the park because of it."
    jump dani_talk_end

label dani_talk_perk_bimbo_1:
    dani.name "Didn't think anyone would be able to connect with [rachel.name]."
    pc "Why not? She's nice."
    dani.name "Yeah, she is also extreme."
    pc "It's what makes her fun."
    jump dani_talk_end

label dani_talk_perk_bimbo_2:
    dani.name "Peas in a pod, you and [rachel.name]."
    pc "Join us. Go crazy."
    dani.name "No thanks."
    jump dani_talk_end

label dani_talk_perk_gym_1:
    dani.name "You are keeping well with the dance stuff."
    pc "Yeah, I like to workout and stuff."
    dani.name "I can see that. You should teach [rachel.name]."
    pc "There is no teaching that girl anything."
    jump dani_talk_end

label dani_talk_perk_slut_1:
    dani.name "All these weird perverts everywhere and you choose to embrace them."
    pc "Sure, why not? Not like only men can have fun."
    dani.name "Ugh. Feels weird. I know it's fun, but I can't stand the idea of making people like that happy."
    pc "Err, yeah. They are kinda shitty. But just use them for your own needs and who cares about them?"
    jump dani_talk_end

label dani_talk_perk_pregwant_1:
    dani.name "You are probably the only person in this city that actually want's to get pregnant."
    pc "I'm sure there are others."
    dani.name "Nope. Just you."
    jump dani_talk_end

label dani_talk_perk_slutty_1:
    dani.name "Like showing off?"
    pc "Huh?"
    dani.name "The way you are dressed. It's a dangerous look around here."
    pc "Being alive is dangerous."
    jump dani_talk_end







label dani_talk_dance_1:
    dani.name "Nice to actually do something these days. Can't really go out or have fun so dance is nice."
    pc "Yeah, there are a few things around the academy you can do."
    dani.name "Dance is about the only thing that wont have guys show up just to talk to the girls."
    pc "They might show up, doubt [svet.nname] will entertain them though."
    jump dani_talk_end

label dani_talk_dance_2:
    dani.name "[rachel.name] seems to have so much fun with the dancing."
    pc "Pretty sure she has fun with everything she does."
    dani.name "Well, good she enjoy's, because she is terrible."
    pc "Terrible? That's kind of a complement."
    jump dani_talk_end

label dani_talk_dance_3:
    dani.name "I wonder if its even worth training to dance."
    pc "What do you mean."
    dani.name "People come for the skirts. We could avoid the dance altogether."
    pc "Could, but then no fun for us."
    dani.name "Yeah."
    jump dani_talk_end

label dani_talk_dance_4:
    dani.name "Not sure what is worse. The park dancing or the bus on the way there."
    pc "Hmmm..."
    pc "Bus probably. No where to run."
    dani.name "Park has places they can drag you off to though."
    jump dani_talk_end

label dani_talk_dance_5:
    dani.name "Not sure what is worse. The park dancing or the bus on the way there."
    pc "Hmmm..."
    pc "Bus probably. No where to run."
    dani.name "Park has places they can drag you off to though."
    jump dani_talk_end






label dani_talk_pubwork_1:
    dani.name "Getting home from the pub so late makes me miss so much sleep."
    pc "Yeah, getting up for the academy in the morning is hard when you get home at 3am."
    dani.name "Might as well sleep at the pub and go straight there in the morning."
    pc "Free rent."
    jump dani_talk_end

label dani_talk_pubwork_2:
    dani.name "I'm kind of surprised the pub manages to stay the way it is."
    pc "What do you mean?"
    dani.name "Places like that usually get taken over by gangs or something."
    pc "Maybe they are protected?"
    dani.name "Could be."
    jump dani_talk_end

label dani_talk_pubwork_3:
    dani.name "Wonder where all the beer comes from in the pub."
    pc "Never really thought about it."
    dani.name "It can't be old beer. That would have ran out by now."
    pc "Maybe the farms make it?"
    jump dani_talk_end

label dani_talk_pubwork_4:
    dani.name "Only beer at the pub. Pretty sure places before used to have a huge selection."
    pc "Places before also didn't have perverts wanking in the corner."
    dani.name "Are you sure?"
    pc "No... Not really."
    jump dani_talk_end

label dani_talk_pubwork_5:
    dani.name "You ever drink at the pub? I mean while not working."
    pc "Sometimes. It's not that bad."
    dani.name "Perverts coming up to you all the time?"
    pc "Actually no. They just assume I am a whore already paid for and leave me alone."
    dani.name "Oh?"
    jump dani_talk_end

label dani_talk_pubwork_6:
    dani.name "[trixie.name] manages that place all on her own?"
    pc "Yeah looks like it."
    dani.name "I'm surprised she manages."
    pc "Don't be fooled by her. The person you see is the person she wants to show us."
    jump dani_talk_end



label dani_talk_pubwhore_1:
    pc "How is paying rent now that you are havin fun with guys in the pub?"
    dani.name "Better I guess."
    pc "Only better?"
    dani.name "I get to save some money. [oskar.name] in mostly off my back."
    pc "And off your arse?"
    dani.name "Mostly."
    jump dani_talk_end

label dani_talk_pubwhore_2:
    dani.name "You ever get any strange requests at the pub?"
    if pub_waitress.sold:
        pc "Strange? Don't think so. Usually drunks just want to stick it in then go back to their beer."
    else:
        pc "They are always wanting me to sit with them and keep them company."
        pc "I reject them when they ask for more than that. I'll leave that up to you and [trixie.name]."
    dani.name "..."
    jump dani_talk_end

label dani_talk_pubwhore_3:
    dani.name "Wish those drunks would be more gentle."
    pc "Ha, yeah right. You are asking too much."
    dani.name "Sometimes I feel like I am one of those old rubber dolls."
    pc "I guess in their eyes you pretty much are."
    jump dani_talk_end

label dani_talk_pubwhore_4:
    dani.name "Wish those drunks would be more gentle."
    pc "Ha, yeah right. You are asking too much."
    dani.name "Sometimes I feel like I am one of those old rubber dolls."
    pc "I guess in their eyes you pretty much are."
    jump dani_talk_end

label dani_talk_pubwhore_5:
    dani.name "You earn more money in the highway than the pub?"
    pc "Yeah, but it's not as easy."
    pc "Oddly enough, the pub is usually full of somewhat decent people."
    dani.name "Yeah, not sure I would describe them as that."
    pc "Head up the highway and you will change your mind."
    dani.name "No thanks, I'll stick to the pub."
    jump dani_talk_end

label dani_talk_pubwhore_6:
    dani.name "I thought at first [trixie.name] might get annoyed at doing stuff like that in the pub."
    pc "Yeah, no chance."
    dani.name "She never mentioned anything about it in my first days."
    pc "Because it's not part of the job."
    dani.name "Yet everyone does it."
    pc "Everyone does it everywhere. The pub isn't special with that sort of thing."
    dani.name "I guess."
    jump dani_talk_end



label dani_talk_pubgloryhole_1:
    pc "Having fun at the hole in the pub?"
    dani.name "Wouldn't call it fun."
    pc "You spend time there though don't you?"
    dani.name "Not much. I only go there to take a break. Sit on the toilet and relax a bit."
    pc "Then someone sticks a dick in the hole."
    dani.name "Yeah."
    jump dani_talk_end

label dani_talk_pubgloryhole_2:
    dani.name "Seems odd men would just stick their dick in a hole."
    pc "Are we talking about women here?"
    dani.name "No, the hole in the pub."
    pc "Ah."
    jump dani_talk_end

label dani_talk_pubgloryhole_3:
    dani.name "They stick their dick in a random hole in the wall. Don't they worry something will happen to it?"
    pc "You looking to chop off someones dick?"
    dani.name "No. But I can't say I have never considered it."
    pc "Well, you victory over the dick in a wall will be short lived."
    dani.name "Might still be worth it."
    pc "Haha."
    jump dani_talk_end

label dani_talk_pubgloryhole_4:
    dani.name "What is it that appeals to guys with the hole in the wall?"
    pc "The hole isn't for guys. It's for girls."
    dani.name "You think?"
    pc "No one knows it's you sucking a dick. Earn a bit of cash and go about your life and no one finds out."
    dani.name "Hmmm..."
    jump dani_talk_end

label dani_talk_pubgloryhole_5:
    pc "There is a hole in the park as well you know."
    dani.name "You put one there?"
    pc "Maybe it was someone else."
    dani.name "Sure. But I end up sucking enough dicks at work."
    pc "More money locally."
    jump dani_talk_end





label dani_talk_danifirst_preg_1:
    dani.name "Difficult with that belly?"
    pc "Yeah, you could say that."
    dani.name "Hope I don't have to find out."
    pc "Yeah, don't count on it."
    jump dani_talk_end

label dani_talk_danifirst_preg_2:
    dani.name "Do you manage to get about ok like that?"
    pc "Mostly. Bus is a bit of a nightmare but can't really walk places."
    dani.name "Bus is a nightmare anyway."
    pc "Worse when you can't really escape."
    dani.name "Do you sit down?"
    pc "Fuck no. Someone will sit next to me and trap me in."
    dani.name "Yeah, I learned that lesson quickly enough. Never sit down."
    jump dani_talk_end

label dani_talk_danifirst_danipreg_1:
    dani.name "Ugh, now I know how you felt with this belly."
    pc "Good luck with it. Make sure to pee."
    dani.name "Yeah, that happens sometimes even if I don't want to."
    pc "Ugh."
    jump dani_talk_end

label dani_talk_danifirst_danipreg_2:
    dani.name "So much harder to dance like this. How did you even manage it?"
    pc "Did I manage it? No one actually cares if we can dance. They just like looking at us."
    dani.name "Ah, yeah I guess the belly probably makes it more fun."
    jump dani_talk_end

label dani_talk_preg_1:
    pc "Uff. Getting harder and harder to move around."
    pc "Maybe letting it get this far wasn't such a good idea."
    jump dani_talk_end

label dani_talk_preg_2:
    pc "Would think people would move out the way more on the bus after seeing me carrying this belly around. But I swear it's the opposite."
    dani.name "Are you new to buses or something? You are slow prey and an easy target."
    pc "Still, would be nice at least once to be able to relax."
    dani.name "Good luck with that."
    jump dani_talk_end

label dani_talk_danipreg_1:
    dani.name "Ugh, how did I let myself get like this?"
    pc "You really want me to answer that?"
    dani.name "No, I want to complain!"
    pc "Thought so."
    jump dani_talk_end

label dani_talk_danipreg_2:
    pc "Anyone act differently around you like that?"
    dani.name "Like what? The belly?"
    pc "Yeah."
    dani.name "Not really. Half the girls around here are pregnant so it's a common sight."
    jump dani_talk_end

label dani_talk_preglate_1:
    pc "So, still waiting on my period."
    if player.has_perk(perk_preg_want):
        dani.name "I guess you are happy about that?"
        pc "Yeah, though still kinda scary."
        dani.name "Yup. Fat [name] for the next while."
        pc "Still early days. Have some time yet."
    else:
        dani.name "Oh?"
        pc "Yeah..."
    jump dani_talk_end

label dani_talk_preglate_2:
    pc "Period isn't coming..."
    dani.name "Yeah, we all know what that means."
    pc "These days, yeah."
    jump dani_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
