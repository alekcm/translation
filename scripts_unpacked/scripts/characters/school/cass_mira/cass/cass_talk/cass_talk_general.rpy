label cass_talk_general_tombola:
    jump expression WeightedChoice([
    
    
    ("cass_talk_general_1", 100),
    ("cass_talk_general_2", 100),

    
    ("cass_talk_school_1", If(dis(dis_school) and not mira.active and not quest_mira_missing.active, 100, 0)),
    ("cass_talk_school_2", If(dis(dis_school), 100, 0)),
    ("cass_talk_school_3", If(dis(dis_school), 100, 0)),  
    ("cass_talk_school_4", If(dis(dis_school), 100, 0)),

    
    ("cass_talk_bully_1", If(not shane.dead and school_bully_quest_bully_cass_target and dis(dis_school) and not "cass_poison" in shane.list, 50, 0)),
    ("cass_talk_bully_2", If(not shane.dead and school_bully_quest_bully_cass_target and dis(dis_school) and not "cass_poison" in shane.list, 50, 0)),
    ("cass_talk_bully_3", If(not shane.dead and school_bully_quest_bully_cass_target and dis(dis_school) and not "cass_poison" in shane.list, 50, 0)),
    ("cass_talk_bully_4", If(not shane.dead and school_bully_quest_bully_cass_target and dis(dis_school) and not "cass_poison" in shane.list, 50, 0)),

    
    ("cass_talk_whore_1", If(cass.iswhore and dis(dis_truckstop), 100, 0)),
    ("cass_talk_whore_2", If(cass.iswhore and dis(dis_truckstop) and quest_whore.sold >= 10, 100, 0)),
    ("cass_talk_whore_3", If(cass.iswhore and dis(dis_truckstop), 100, 0)),
    ("cass_talk_whore_4", If(cass.iswhore and dis(dis_truckstop) and quest_whore.sold >= 10, 100, 0)),
    ("cass_talk_whore_5", If(cass.iswhore and dis(dis_truckstop), 100, 0)),
    ("cass_talk_whore_6", If(cass.iswhore and dis(dis_truckstop) and t.month == "Winter", 100, 0)),
    ("cass_talk_whore_7", If(cass.iswhore and dis(dis_truckstop), 100, 0)),
    ("cass_talk_whore_8", If(cass.iswhore and dis(dis_truckstop), 100, 0)),

    
    ("cass_talk_perk_ex_1", If(cass.love > 60 and player.has_perk(perk_exhibitionist), 100, 0)),
    ("cass_talk_perk_ex_2", If(cass.love > 60 and player.has_perk(perk_exhibitionist), 100, 0)),
    ("cass_talk_perk_bimbo_1", If(cass.love > 60 and player.has_perk(perk_bimbo), 100, 0)),
    ("cass_talk_perk_bimbo_2", If(cass.love > 60 and player.has_perk(perk_bimbo), 100, 0)),
    ("cass_talk_perk_gym_1", If(cass.love > 60 and player.has_perk(perk_gym_bunny), 100, 0)),
    ("cass_talk_perk_slutty_1", If(cass.love > 60 and player.has_perk(perk_slutty), 100, 0)),

    
    ("cass_talk_cassfirst_preg_1", If(cass.love > 50 and cass.preg == 0 and player.pregnancy >= 2, 100, 0)),
    ("cass_talk_cassfirst_preg_2", If(cass.love > 50 and cass.preg == 0 and player.pregnancy >= 2, 100, 0)),
    ("cass_talk_cassfirst_casspreg_1", If(cass.love > 50 and cass.showing and cass.pregbabies == 0 and player.pregbabies, 100, 0)),
    ("cass_talk_cassfirst_casspreg_2", If(cass.love > 50 and cass.showing and cass.pregbabies == 0 and player.pregbabies, 100, 0)),
    ("cass_talk_casspreg_1", If(cass.love > 50 and cass.showing, 100, 0)),
    ("cass_talk_casspreg_2", If(cass.love > 50 and cass.showing, 100, 0)),
    ("cass_talk_preg_1", If(cass.love > 50 and player.showing, 100, 0)),
    ("cass_talk_preg_2", If(cass.love > 50 and player.showing, 100, 0)),
    ("cass_talk_preglate_1", If(cass.love > 50 and player.has_perk(perk_period_late), 100, 0)),
    ("cass_talk_preglate_2", If(cass.love > 50 and player.has_perk(perk_period_late), 100, 0)),



    
    
    
    
    
    

    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    

    
    
    
    
    
    
    

    ])







label cass_talk_soccerboys_meet_0:
    $ cass.dict["cass_soccerboys_talk"] += 1
    pc "You ever spoke to the boys out on the field?"
    cass.name "Not really. Seen them playing but never spoke to them. Why?"
    pc "Ah I went and had a chat with them. They invited me to play with them."
    cass.name "Oooh. Running around with a bunch of sweaty boys?"
    jump cass_talk_end

label cass_talk_soccerboys_meet_1:
    $ cass.dict["cass_soccerboys_talk"] += 1
    pc "They seem decent enough though."
    cass.name "Who?"
    pc "The boys playing football."
    cass.name "Ah. I'm sure they are happy to have you running around with them."
    pc "What's that supposed to mean?"
    show cass laugh
    cass.name "Nothing, nothing!"
    jump cass_talk_end

label cass_talk_soccerboys_meet_2:
    $ cass.dict["cass_soccerboys_talk"] += 1
    cass.name "You alone with three boys?"
    pc "Yeah... And?"
    cass.name "And nothing."
    pc "Right."
    jump cass_talk_end

label cass_talk_soccerboys_meet_3:
    $ cass.dict["cass_soccerboys_talk"] += 1
    pc "You know you can come and join us play if you want."
    cass.name "What? Nooooo."
    pc "Why not?"
    cass.name "I'll leave the troublemaking to you."
    jump cass_talk_end







label cass_talk_general_1:
    pc "You doing okay?"
    cass.name "Yeah, same as always."
    jump cass_talk_end

label cass_talk_general_2:
    cass.name "The park is nice. One of the few places that you can pretend is normal."
    pc "Yeah, as long as it's day time."
    cass.name "Well, yeah. Like everywhere."
    jump cass_talk_end



label cass_talk_school_1:
    cass.name "Where is that [mira.name]? Haven't seen her all day."
    pc "Relaxing by the lake probably."
    if weather_var == 1:
        cass.name "Hmm, hope so. Lovely out there today. Should go and join her."
        pc "Yeah, you in a bikini. Pretty sure you will cause a commotion."
        cass.name "Hey!"
    else:
        cass.name "In this weather?"
        pc "Well, even when it's like this. Probably better than this place."
        cass.name "Probably."
    jump cass_talk_end

label cass_talk_school_2:
    pc "I don't see you often at the gym."
    cass.name "Of course not. Perverts are bad enough with me jumping around."
    pc "You might have fun."
    cass.name "Sure. I'll leave that kind of fun to you."
    jump cass_talk_end

label cass_talk_school_3:
    pc "Some quiet places to relax around here at least."
    cass.name "Yeah. But sometimes better to relax in the busy places. Less chance of idiots coming up to you."
    pc "Ha, yeah. Most peaceful in the busier places."
    jump cass_talk_end

label cass_talk_school_4:
    pc "What do you get up to outside of this place?"
    cass.name "Nothing. Here and home. Don't do much else."
    pc "What about work?"
    if cass.iswhore:
        cass.name "The highway mostly. Don't have time for anything else."
    else:
        cass.name "I look around, start a job. Boss tries to grope me or something, find a new job and start all over again."
    jump cass_talk_end



label cass_talk_perk_ex_1:
    cass.name "I can't even imagine going out dressed all revealing and you run around naked."
    pc "Should try it some time."
    cass.name "I like being alive thanks."
    pc "I'm still alive."
    jump cass_talk_end

label cass_talk_perk_ex_2:
    cass.name "It's almost crazy what you do."
    pc "What I do?"
    cass.name "Prance around all naked."
    pc "I don't \"prance\"."
    cass.name "Then what would you call it?"
    pc "Streaking?"
    jump cass_talk_end

label cass_talk_perk_bimbo_1:
    cass.name "Sometimes I wish I could be as happy as you."
    pc "Err. Thanks?"
    cass.name "Being a bimbo round here surely makes things a lot easier to deal with."
    pc "A bimbo?"
    cass.name "Err. I mean... Nothing."
    jump cass_talk_end

label cass_talk_perk_bimbo_2:
    cass.name "Do the guys like the bimbo act?"
    pc "Err... Not sure what you mean."
    cass.name "Yes you do."
    pc "Everyone loves me."
    cass.name "Haha."
    jump cass_talk_end

label cass_talk_perk_gym_1:
    pc "You should join me running or something one day."
    cass.name "No thanks. Me and running don't get along."
    pc "Yeah, might knock yourself out with those chest monsters."
    if player.breasts == 3:
        cass.name "Like you are one to talk."
    else:
        show cass angry
        cass.name "This is my laughing face..."
    jump cass_talk_end

label cass_talk_perk_slutty_1:
    cass.name "Dressed like that, you will have half the town after you."
    pc "So no change then?"
    cass.name "Haha."
    jump cass_talk_end




label cass_talk_cassfirst_preg_1:
    cass.name "Pregnant?"
    pc "No, it's [name]."
    cass.name "Thanks dad."
    jump cass_talk_end

label cass_talk_cassfirst_preg_2:
    cass.name "You okay carrying that around?"
    pc "Well, I can't leave it at home, so no choice."
    cass.name "You could leave it somewhere else."
    pc "Not sure that's how it works."
    cass.name "Not sure you get my meaning."
    jump cass_talk_end

label cass_talk_cassfirst_casspreg_1:
    cass.name "I thought it wouldn't be that bad after seeing you manage it. But this thing is killing my back."
    pc "Yeah, and it only gets worse."
    cass.name "And almost pissed myself the other day."
    pc "Yeah I didn't need to know that part."
    jump cass_talk_end

label cass_talk_cassfirst_casspreg_2:
    cass.name "Takes me ages to get around now."
    pc "Yeah. I didn't realise how much harder it would be to just walk around."
    cass.name "I would sit somewhere but within 30 seconds I'd have some idiot come sit next to me."
    pc "Ask him to massage your feet."
    cass.name "Haha."
    jump cass_talk_end

label cass_talk_preg_1:
    pc "Uff. Getting harder and harder to move around."
    pc "Maybe letting it get this far wasn't such a good idea."
    jump cass_talk_end

label cass_talk_preg_2:
    pc "Would think people would move out the way more on the bus after seeing me carrying this belly around. But I swear it's the opposite."
    cass.name "Yeah... Bus perverts probably see it as easy prey."
    pc "Yeah. Can't run away from them."
    jump cass_talk_end

label cass_talk_casspreg_1:
    pc "You getting more attention with the belly?"
    cass.name "Yeah. Way more than I thought I would. Think they would avoid the farting girl ready to pee herself, but no."
    pc "Might be what attracts them."
    cass.name "Probably..."
    if not numgen(0,20):
        pc "That at the giant tits."
        cass.name "I'l serve you to them."
    jump cass_talk_end

label cass_talk_casspreg_2:
    pc "..."
    cass.name "What?"
    pc "Just wondering how you manage to fit all that into your clothes."
    cass.name "I almost can't."
    jump cass_talk_end

label cass_talk_preglate_1:
    pc "So, still waiting on my period."
    if player.has_perk(perk_preg_want):
        cass.name "And?"
        pc "Err, just thought I would bring it up."
        cass.name "I know you. Don't pretend like it's a bad thing."
        pc "You are supposed to pretend with me!"
    else:
        cass.name "Oh?"
        pc "Yeah..."
    jump cass_talk_end

label cass_talk_preglate_2:
    pc "Period isn't coming..."
    cass.name "..."
    pc "Thanks for the support, you always know what to say to make me feel better."
    jump cass_talk_end

label cass_talk_pregnant_discover:
    $ add_to_list(cass.list, "seen_pregnant_" + str(cass.preg))
    if cass.preg == 1:
        pc "Oh? Pregnant? How'd you manage that?"
    else:
        pc "Pregnant again? Who's the lucky man?"
    cass.name "Yeah..."
    if cass.pregnant_who == busgroper:
        cass.name "Should have probably walked instead of getting the bus..."
        pc "Oh? Went that far did it?"
        cass.name "Yeah..."
        pc "Congrats?"
        cass.name "Thanks..."
    elif cass.pregnant_who == lover:
        cass.name "I got a little carried away with a new friend."
        pc "Oh? You dirty girl!"
    elif any(x == cass.pregnant_who for x in [punter, highpayer]):
        if cass.iswhore:
            cass.name "Someone from the highway gave me this."
            pc "Ah. Well, was going to happened eventually I suppose."
            cass.name "Yeah."
        else:
            cass.name "Errm..."
            cass.name "Don't ask..."
            pc "Okay."
    elif cass.pregnant_who == rapist:
        cass.name "..."
        pc "Ah... Yeah okay..."
        cass.name "Yeah..."
    else:
        cass.name "Errm, does it make me sound bad that I don't know?"
        pc "Not really."
    jump cass_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
