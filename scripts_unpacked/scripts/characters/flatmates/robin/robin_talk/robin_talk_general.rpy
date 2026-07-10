init python:

    def robin_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        text_desc = ""
        
        if not robin.has_met:  
            cur_location = None 
        
        
        elif "no_location" in robin.list: 
            cur_location = None 
        elif "pub_leave_offer" in robin.list: 
            cur_location = loc_bus_interior
        elif "slut_outing" in robin.list: 
            cur_location = loc_motel_room2
        elif "bitching" in robin.list: 
            cur_location = dis_park
            text_desc = "Bitching at the park."
        elif "pc_knows_likes_watching" in robin.list and robin.dict["robin_talk_pub_chain"] >= 15 and global_random_noon_number >= 10 and t.hour in (2,3,4,5,6): 
            cur_location = loc_motel_room2
        elif "pc_knows_likes_watching" in robin.list and robin.dict["robin_talk_pub_chain"] >= 15 and global_random_noon_number >= 9 and (t.hour in (22,23, 0, 1,2) or t.time_from_to(03.00, 03.30)): 
            cur_location = loc_pub
        elif people_nude_beach_vball_canplay() and weather_var == 1 and not t.month in ("Autumn", "Winter") and (robin.isslut or "pc_know_want_bussex" in robin.list or "pc_knows_likes_watching" in robin.list or "nudebeachvball_ask_know" in robin.list): 
            cur_location = loc_beach_gym
        elif "can_bitch" in robin.list and t.hour in (22,23, 0, 1,2) and robin.noon_number <= 2 and not robin.showing:
            cur_location = dis_park
            text_desc = "Bitching at the park."
        
        
        elif t.day > 20 and t.time_from_to(22.30, 04.00) and "common_passout" in robin.list: 
            cur_location = loc_common
        elif t.time_from_to(23.30, 07.00): 
            cur_location = loc_bedroom_robin
        elif t.time_from_to(07.00, 07.20): 
            cur_location = loc_bathroom
        elif t.hour == 7: 
            cur_location = loc_kitchen
        elif oskar_here(loc_office_ll) and t.time_from_to(08.00, 08.20) and "oskar_sex" in robin.list and global_random_number in (5,6,7) and t.wkday in weekdays: 
            cur_location = loc_office_ll
        elif t.hour == 8 and (global_random_number > 5): 
            cur_location = loc_common
        elif t.hour == 8:
            cur_location = loc_kitchen
        elif t.wkday in weekdays and t.time_from_to(09.00, 09.30): 
            cur_location = loc_bus_interior
        elif t.wkday in weekdays and t.hour == 12: 
            cur_location = loc_school_cafe
        elif t.wkday in weekdays and t.time_from_to(09.30, 14.00): 
            cur_location = loc_school_hallway
        elif t.wkday in weekend and t.time_from_to(09.00, 12.00): 
            cur_location = loc_bedroom_robin
        elif t.time_from_to(23.10, 23.30): 
            cur_location = loc_bathroom
        elif t.time_from_to(22.30, 23.00) and (global_random_number > 5): 
            cur_location = loc_common
        elif t.time_from_to(22.30, 23.00): 
            cur_location = loc_kitchen
        
        elif t.day <= 10 or t.wkday == "Friday" or t.wkday == "Saturday": 
            if t.wkday in weekdays and t.time_from_to(14.00, 14.30): 
                cur_location = loc_bus_interior
            elif t.time_from_to(14.30, 00.00): 
                cur_location = loc_common
        
        
        elif weather_var == 1 and not t.month in ("Autumn", "Winter"): 
            if t.hour in irange(10, 17): 
                cur_location = loc_beach_gym
            elif t.hour in irange(18, 21): 
                cur_location = loc_beach_fire  
            elif t.time_from_to(22.00, 22.30): 
                cur_location = loc_bus_interior
        
        else: 
            if t.time_from_to(22.00, 22.30) and "soccer_hangout" in robin.list: 
                cur_location = loc_bus_interior
            elif school_soccer_playing(): 
                cur_location = loc_school_field
            elif school_soccer_hangingout() and "soccer_hangout" in robin.list and "soccer_sex_robin" in robin.list and "soccerboys_can_sex" in robin.list and not "soccer_free_use" in robin.list and t.hour < 22: 
                if weather_var > 2 or t.month == "Winter":
                    cur_location = loc_school_locker_old
                else:
                    cur_location = loc_school_field_back_isolate
            elif school_soccer_hangingout() and "soccer_hangout" in robin.list and t.hour < 22: 
                cur_location = loc_school_field_back
            
            
            elif not "soccer_hangout" in robin.list and t.time_from_to(14.00, 14.30): 
                cur_location = loc_bus_interior
            elif t.time_from_to(14.30, 00.00): 
                cur_location = loc_common
        
        if "kickedout_window_entry" in robin.list and loc_cur == loc_bedroom_robin and cur_location in dis_home.locs:
            
            cur_location = loc_bedroom_robin
        
        
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where, text_desc) 

    def robin_can_bus():
        if "pc_know_want_bussex" in robin.list and (robin_here(dis_school.locs) or robin_here(dis_home.locs)) and t.hour in irange(8,21) and not c.inappropriate and robin.lust > 30 and not oskar_here():
            return True
        return False

    def robin_can_bitch():
        if "park_bitch_intro" in robin.list and robin_here(dis_home.locs) and t.timeofday == "night":
            return True
        return False

    def robin_can_slut():
        if robin.isslut and robin_here(dis_home.locs) and (party.appropriate or party2.appropriate) and not player.is_dirty() and t.hour in (20,21,22,23,0,1,2):
            return True
        return False

label robin_action_fun_picker:
    jump expression WeightedChoice([
    ("robin_action_bus_adventure_invite", If(robin_can_bus(), 20, 0)), 
    ("robin_talk_sexobject_offer_outing_start", If(robin_can_slut(), 100, 0)),
    ("robin_action_park_adventure_picker", If(robin_can_bitch(), 100, 0)),
    
    ])

label robin_bedroom_asleep:
    pcm "She is asleep so I probably shouldn't go in."
    jump travel

label robin_talk_subject:
    jump expression WeightedChoice([

    ("robin_talk_general_1", 100),
    ("robin_talk_general_2", 100),
    ("robin_talk_general_3", 100),

    ("robin_talk_school_1", If(t.day > 4, 100, 0)),
    ("robin_talk_school_2", If(t.day > 4, 100, 0)),
    ("robin_talk_school_3", If(t.day > 4, 100, 0)),
    ("robin_talk_school_4", If(t.day > 4, 100, 0)),

    ("robin_talk_perk_ex_1", If(robin.love > 60 and player.has_perk(perk_exhibitionist), 100, 0)),
    ("robin_talk_perk_ex_2", If(robin.love > 60 and player.has_perk(perk_exhibitionist), 100, 0)),
    ("robin_talk_perk_bimbo_1", If(robin.love > 60 and player.has_perk(perk_bimbo), 100, 0)),
    ("robin_talk_perk_bimbo_2", If(robin.love > 60 and player.has_perk(perk_bimbo), 100, 0)),
    ("robin_talk_perk_gym_1", If(robin.love > 60 and player.has_perk(perk_gym_bunny), 100, 0)),
    ("robin_talk_perk_whore_1", If(robin.love > 60 and player.has_perk(perk_whore), 100, 0)),
    ("robin_talk_perk_whore_2", If(robin.love > 60 and player.has_perk(perk_whore), 100, 0)),
    ("robin_talk_perk_whore_3", If(robin.love > 60 and player.has_perk(perk_whore), 100, 0)),
    ("robin_talk_perk_slut_1", If(robin.love > 60 and player.has_perk(perk_slut), 100, 0)),


    ("robin_talk_scav_1", If((t.day + 2) > robin.dict["robin_talk_scav_chain"] and "is_scavver" in robin.list, 100, 0)),
    ("robin_talk_scav_2", If((t.day + 2) > robin.dict["robin_talk_scav_chain"] and "is_scavver" in robin.list, 100, 0)),
    ("robin_talk_scav_3", If((t.day + 2) > robin.dict["robin_talk_scav_chain"]  and "is_scavver" in robin.list and jaylee.love >= 20, 100, 0)),
    ("robin_talk_scav_4", If((t.day + 2) > robin.dict["robin_talk_scav_chain"]  and "is_scavver" in robin.list, 100, 0)),
    ("robin_talk_scav_5", If((t.day + 2) > robin.dict["robin_talk_scav_chain"]  and "is_scavver" in robin.list, 100, 0)),
    ("robin_talk_scav_6", If((t.day + 2) > robin.dict["robin_talk_scav_chain"]  and "is_scavver" in robin.list, 100, 0)),

    ("robin_talk_soccer_play_1", If("soccerboys_ask_tell" in robin.list and drake.has_met, 100, 0)),
    ("robin_talk_soccer_play_2", If("soccerboys_ask_tell" in robin.list and drake.has_met, 100, 0)),

    ("robin_talk_soccer_hangout_1", If("soccer_hangout" in robin.list, 100, 0)),
    ("robin_talk_soccer_hangout_2", If("soccer_hangout" in robin.list, 100, 0)),
    ("robin_talk_soccer_hangout_3", If("soccer_hangout" in robin.list, 100, 0)),
    ("robin_talk_soccer_hangout_4", If("soccer_hangout" in robin.list, 100, 0)),
    
    ("robin_talk_soccer_sex_1", If("soccerboys_can_sex" in robin.list, 100, 0)),
    ("robin_talk_soccer_sex_2", If("soccerboys_can_sex" in robin.list, 100, 0)),
    ("robin_talk_soccer_sex_3", If("soccerboys_can_sex" in robin.list and player.has_perk(perk_whore), 100, 0)),
    ("robin_talk_soccer_sex_4", If("soccerboys_can_sex" in robin.list, 100, 0)),
    ("robin_talk_soccer_sex_5", If("soccerboys_can_sex" in robin.list and "told_sex_" + rachel._original_name in nate.conversation_topics, 100, 0)),

    ("robin_talk_bully_1", If(shane.has_met and not shane.dead and robin_here(loc_school_hallway), 50, 0)),
    ("robin_talk_bully_2", If(shane.has_met and not shane.dead and robin_here(loc_school_hallway), 50, 0)),
    ("robin_talk_bully_3", If(shane.has_met and not shane.dead and robin_here(loc_school_hallway), 50, 0)),
    ("robin_talk_bully_4", If(shane.has_met and not shane.dead and robin_here(loc_school_hallway), 50, 0)),

    ("robin_talk_bussex_1", If("pc_know_want_bussex" in robin.list and busgroper.fname in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_2", If("pc_know_want_bussex" in robin.list and busgroper.fname in robin.sex_who and busgroper.setname in robin.conversation_topics, 100, 0)),
    ("robin_talk_bussex_3", If("pc_know_want_bussex" in robin.list and busgroper.fname in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_4", If("pc_know_want_bussex" in robin.list and busgroper.fname in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_5", If("pc_know_want_bussex" in robin.list and busgroper.fname in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_6", If("pc_know_want_bussex" in robin.list and busgroper.fname in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_7", If("pc_know_want_bussex" in robin.list and busgroper.fname in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_8", If("pc_know_want_bussex" in robin.list and busgroper.fname in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_9", If("pc_know_want_bussex" in robin.list and busgroper.fname in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_10", If("pc_know_want_bussex" in robin.list and busgroper.fname in robin.sex_who, 100, 0)),

    ("robin_talk_insem_1", If("pc_know_want_sexstories" in robin.list and not player.preg_knows and player.has_perk(perk_preg_want) and player.has_perk(perk_inseminated) and not player.has_perk(perk_period), 100, 0)),
    ("robin_talk_insem_2", If("pc_know_want_sexstories" in robin.list and not player.preg_knows and player.has_perk(perk_preg_want) and player.has_perk(perk_inseminated) and not player.has_perk(perk_period), 100, 0)),
    ("robin_talk_robinfirst_preg_1", If(robin.love > 50 and robin.preg == 0 and player.pregnancy >= 2, 100, 0)),
    ("robin_talk_robinfirst_preg_2", If(robin.love > 50 and robin.preg == 0 and player.pregnancy >= 2, 100, 0)),
    ("robin_talk_robinfirst_robinpreg_1", If(robin.love > 50 and robin.showing and robin.pregbabies == 0 and player.pregbabies, 100, 0)),
    ("robin_talk_robinfirst_robinpreg_2", If(robin.love > 50 and robin.showing and robin.pregbabies == 0 and player.pregbabies, 100, 0)),
    ("robin_talk_robinpreg_1", If(robin.love > 50 and robin.showing, 100, 0)),
    ("robin_talk_robinpreg_2", If(robin.love > 50 and robin.showing, 100, 0)),
    ("robin_talk_preg_1", If(robin.love > 50 and player.showing, 100, 0)),
    ("robin_talk_preg_2", If(robin.love > 50 and player.showing, 100, 0)),
    ("robin_talk_preglate_1", If(robin.love > 50 and player.has_perk(perk_period_late), 100, 0)),
    ("robin_talk_preglate_2", If(robin.love > 50 and player.has_perk(perk_period_late), 100, 0)),

    ("robin_talk_sexgossip_1", If("pc_know_want_sexstories" in robin.list and "soccer_hangout" in robin.list and all([drake.sex, nate.sex, dan.sex]) and not "soccerboys_knows_pc_sex" in robin.list, 100, 0)),
    ("robin_talk_sexgossip_2", If("pc_know_want_sexstories" in robin.list and bob.sex, 100, 0)),
    ("robin_talk_sexgossip_3", If("pc_know_want_sexstories" in robin.list, 100, 0)),
    ("robin_talk_sexgossip_4", If("pc_know_want_sexstories" in robin.list and "licked_ass" in jaylee.conversation_topics and robin.dict["robin_talk_scav_chain"] > (t.day + 5) and "is_scavver" in robin.list, 100, 0)),
    ("robin_talk_sexgossip_5", If("pc_know_want_sexstories" in robin.list and schoolguy.sold and schoolguy.creamvag, 100, 0)),
    ("robin_talk_sexgossip_6", If("pc_know_want_sexstories" in robin.list and parkpervert_dani.sex, 100, 0)),
    

    ])





label robin_talk_general_1:
    robin.name "How you been keeping?"
    pc "As best as can be in this place."
    robin.name "Yeah, can't ask for much more than that."
    jump robin_talk_end

label robin_talk_general_2:
    pc "All good?"
    robin.name "Other than being terrified to go out at night, wonderful."
    pc "Should be scared at the daytime as well."
    robin.name "Hah, yeah."
    jump robin_talk_end

label robin_talk_general_3:
    robin.name "Found anything worth doing other than getting drunk?"
    pc "Drugs?"
    robin.name "Yeah.. Not quite what I meant."
    pc "Then no. Nothing."
    jump robin_talk_end





label robin_talk_school_1:
    robin.name "Didn't think I'd be dressing as a schoolgirl again."
    pc "Only time I ever see you in a skirt."
    robin.name "Hah, no choice. It's what they gave me."
    pc "Thought as much."
    jump robin_talk_end

label robin_talk_school_2:
    pc "Don't see you much in classes."
    robin.name "Na, I just turn up for somewhere safe to hang out and free food."
    pc "Not interested in what they have to say?"
    robin.name "They spend far too much time telling us to get fucked in the arse to not get pregnant."
    pc "Yeah... That doesn't seem to be working looking at the bellies around the school."
    jump robin_talk_end

label robin_talk_school_3:
    robin.name "At least the food is free at school."
    pc "Yeah. Even then I wonder if it's too expensive."
    robin.name "Haha. It is sometimes."
    robin.name "Most of the time..."
    jump robin_talk_end

label robin_talk_school_4:
    robin.name "I thought there was a pool at the school."
    pc "Yeah right. All that nice water going to waste. Lucky we even have showers."
    robin.name "I guess. And they are mildly hot."
    pc "Yeah, not sure how they manage that."
    jump robin_talk_end





label robin_talk_naked_first:
    $ robin.dict["robin_talk_lesbian_times"] += 1
    $ add_to_list(robin.list, "naked_talk")
    robin.name "Err... So... You aren't quite dressed."
    if player.has_perk(perk_exhibitionist, True):
        pc "Yeah."
        robin.name "Err... Shouldn't you be?"
        pc "Maybe, but I don't want to be."
        robin.name "Okaaaay... Oh! You are one of those?"
        pc "Those?"
        robin.name "People who get off showing off?"
        pc "Ugh. I guess?"
        robin.name "Right."
    elif dis(dis_home):
        pc "I'm at home. Do I need to be?"
        robin.name "Guess not. Up to you."
        robin.name "We live with boys..."
        pc "Good for them."
        robin.name "Okay..."
    else:
        pc "Yeah... Not always easy round here to remain that way."
        robin.name "Ah. Yeah..."
    jump robin_talk_end

label robin_talk_perk_ex_1:
    robin.name "So, like taking your clothes off I can get... Sort of."
    pc "But?"
    robin.name "In this place? Isn't it just an invitation to get dragged into some alleyway?"
    pc "Just being alive is enough to get dragged off by some cunt."
    robin.name "True..."
    jump robin_talk_end

label robin_talk_perk_ex_2:
    robin.name "So, how often you go outside like that?"
    pc "Like what?"
    robin.name "Arse flapping in the wind."
    pc "Ah, not too often. End up dead in a ditch probably."
    pc "Would be fun to show off outside though."
    robin.name "Should I start digging you a grave?"
    pc "Fuck no! Let whoever kills me do the work."
    robin.name "Ha!"
    jump robin_talk_end

label robin_talk_perk_bimbo_1:
    robin.name "How's my favourite princess doing?"
    pc "Princess?"
    robin.name "Barbie?"
    pc "Ah. Do you have any of those?"
    robin.name "What? No. Like I ever played with dolls."
    pc "Shame."
    jump robin_talk_end

label robin_talk_perk_bimbo_2:
    robin.name "Bet you make the guys happy."
    pc "Huh?"
    robin.name "Being all... Y'know..."
    pc "Err... No? What?"
    robin.name "Like a... Never mind."
    pc "Err. Okay..."
    jump robin_talk_end

label robin_talk_perk_gym_1:
    robin.name "When we gonna play?"
    pc "Errm... Didn't know you were into that kind of thing."
    robin.name "Idiot. Football. Or volleyball. Something."
    pc "Ah."
    jump robin_talk_end

label robin_talk_perk_whore_1:
    robin.name "So been putting your ass to good work?"
    pc "It pays the bills."
    robin.name "Yeah, but think you do it for more than that."
    pc "Well, if you're going to do something anyway, why not get paid for it?"
    robin.name "Ha, your such a slut."
    jump robin_talk_end

label robin_talk_perk_whore_2:
    robin.name "Keeping safe out there I hope. Can't be easy doing what you do."
    pc "You say that like you haven't done it."
    if not robin.sold:
        robin.name "I... Haven't..."
        pc "Wait. Really?"
        robin.name "Nope. No one wants a girl dressed like me."
        pc "Yeah right. Come with me and I'll have you sold off in a heartbeat."
        robin.name "Haha."
    else:
        robin.name "Well, I don't go out advertising myself. Sometimes someone just offers a lot of money."
        pc "Mmm, I suppose so."
    jump robin_talk_end

label robin_talk_perk_whore_3:
    pc "Interested in making more money?"
    robin.name "Not the way you have in mind."
    pc "Why not? Not like you haven't done it before."
    robin.name "Big difference between accepting the odd offer and walking the street with my arse out."
    pc "People would like your arse."
    robin.name "That almost makes it worse..."
    jump robin_talk_end

label robin_talk_perk_slut_1:
    pc "Interested in making more money?"
    robin.name "Not the way you have in mind."
    pc "Why not? Not like you haven't done it before."
    robin.name "Big difference between accepting the odd offer and walking the street with my arse out."
    pc "People would like your arse."
    robin.name "That almost makes it worse..."
    jump robin_talk_end





label robin_talk_scav_1:
    robin.name "Digging out in the streets really messes with my fingernails."
    pc "Oh? Didn't know you cared."
    robin.name "Not like you care with your pretty hands all painted up."
    robin.name "But I prefer to not be digging dirt out from my nails for the rest of the day."
    jump robin_talk_end

label robin_talk_scav_2:
    robin.name "Now and then I dig up some weird stuff while scavenging."
    pc "Anything fun?"
    robin.name "Can't count how many bits of clothing I have sold to the girls that look like they came off a whore."
    pc "Err... A live one I hope."
    robin.name "Let's hope."
    jump robin_talk_end

label robin_talk_scav_3:
    robin.name "[jaylee.name] seems to ask about you a lot."
    pc "Yeah..."
    robin.name "You owe her money or something?"
    pc "No. She kinda has a thing for me..."
    robin.name "Oh right? And you?"
    pc "She's nice. And fun."
    robin.name "But doesn't have a cock."
    pc "Mmm..."
    jump robin_talk_end

label robin_talk_scav_4:
    robin.name "End up coming across all manner of drugs at the beach."
    pc "Ooh. Make a bit of profit off those?"
    robin.name "Yeah... No."
    pc "Haha. Yeah better keep them. Come in handy."
    jump robin_talk_end

label robin_talk_scav_5:
    robin.name "So there is one bonus to contraceptives being banned."
    pc "Really?"
    robin.name "When I used to look for tins and bottles as a kid, you had to sift through all the used condoms."
    pc "Ugh! Fucking hell [robin.name]. I didn't need to know that."
    robin.name "Condoms are banned now so that's... Great?"
    pc "Yeah. Wonderful."
    jump robin_talk_end

label robin_talk_scav_6:
    robin.name "You can also dig up the smokes people throw away, break 'em up and make into roll-ups. Sell those on.."
    pc "Is that how we get smokes these days?"
    robin.name "Well, I don't see any tobacco fields anywhere."
    pc "..."
    jump robin_talk_end






label robin_talk_soccer_play_1:
    robin.name "For a bunch of boys who only play football all day, they are pretty shit at it."
    pc "Might be letting you win?"
    robin.name "Or too hungover to see the ball."
    pc "Might be that."
    jump robin_talk_end

label robin_talk_soccer_play_2:
    robin.name "The boys ever go to the park or beach to play football?"
    pc "Not seen them anywhere else."
    robin.name "Wonder why?"
    pc "Probably cos this place is just as shit for them as it is us."
    robin.name "Doubt anyone is doing to be dragging them in the bushes to rape them."
    pc "Yeah... People might. And stick a knife in them afterwards."
    robin.name "You think?"
    jump robin_talk_end



label robin_talk_soccer_hangout_1:
    robin.name "I wonder where [dan.name] gets all the beer from."
    pc "Hmm, he acts like he has some connections."
    robin.name "Where do they even get the money to pay for it all?"
    pc "That's a better question."
    jump robin_talk_end

label robin_talk_soccer_hangout_2:
    robin.name "So all they do all day is play football and drink all night. How are their livers not dead yet?"
    pc "I know! Damn alcoholics they are."
    jump robin_talk_end

label robin_talk_soccer_hangout_3:
    robin.name "Hope the boys aren't such perverts when you hang out there without me."
    pc "What are you talking about? They are perverts even when you are there."
    robin.name "Well, you know what I mean."
    pc "Err, not really."
    jump robin_talk_end

label robin_talk_soccer_hangout_4:
    robin.name "Those boys really stay out that late getting drunk then stagger in the next morning. No idea how they manage it."
    pc "Well, have you seen the state of them in the morning?"
    robin.name "Well... They are awake... Mostly... Better than I could do."
    pc "Getting old are you?"
    jump robin_talk_end



label robin_talk_soccer_sex_1:
    robin.name "Not sure how you managed it alone before I came along."
    pc "Managed what?"
    robin.name "Three boys all to yourself."
    pc "Ah. Well... Taking turns?"
    robin.name "Haha."
    jump robin_talk_end

label robin_talk_soccer_sex_2:
    robin.name "None of the boys ever get upset with sharing you?"
    pc "Why would they? We are just friends."
    robin.name "Friends don't usually take turns sticking their dick in you."
    pc "They don't? No one told me this before."
    robin.name "You slut!"
    jump robin_talk_end

label robin_talk_soccer_sex_3:
    robin.name "The boys fine with you being a whore?"
    pc "Probably turns them on more."
    robin.name "Oh?"
    pc "Don't act all shocked. Pretty sure it turns you on as well."
    robin.name "Shut up!"
    jump robin_talk_end

label robin_talk_soccer_sex_4:
    robin.name "I take it you are okay with me fucking the boys as well?"
    pc "Less people sticking their cock in me. So sure."
    robin.name "Less people? Don't pretend like you think that's a good thing."
    pc "It's fine. I'm okay with it."
    jump robin_talk_end

label robin_talk_soccer_sex_5:
    robin.name "So I hear your dance friend is also fucking the boys."
    pc "Where did you hear that from?"
    robin.name "[nate.name] doesn't shut up about it."
    pc "Ah, yeah. He acts like he has won the lottery."
    robin.name "Three girls jumping on his cock on a regular basis? I think for him it's better than the lottery."
    pc "Haha!"
    jump robin_talk_end





label robin_talk_bully_1:
    robin.name "Those two arseholes really work at making people hate them."
    pc "I know..."
    robin.name "Won't be long at this rate til someone digs up their body."
    pc "Not if we hide it well enough."
    robin.name "Hah!"
    jump robin_talk_end

label robin_talk_bully_2:
    robin.name "Wouldn't be that bad here if those cunts would hurry up and trouble someone who would kill them."
    pc "Mmmm. Hopefully a matter of time."
    robin.name "It is."
    jump robin_talk_end

label robin_talk_bully_3:
    robin.name "Look at those arseholes prowling around."
    pc "*Tsk*"
    robin.name "Notice how they only mess with girls."
    pc "Afraid to get their ass kicked probably."
    jump robin_talk_end

label robin_talk_bully_4:
    robin.name "Look at the cunts."
    pc "Ignore them..."
    robin.name "..."
    jump robin_talk_end





label robin_talk_bussex_1:
    pc "How's your bus adventures going?"
    robin.name "You should come with me and find out."
    pc "It's not me who likes watching people get fucked."
    robin.name "Ok, so I will watch you get bent over on the bus."
    pc "Yeah, would like that wouldn't you?"
    robin.name "Yup!"
    jump robin_talk_end

label robin_talk_bussex_2:
    $ remove_from_list(robin.conversation_topics, busgroper.name)
    robin.name "So was on the bus."
    pc "Oh?"
    robin.name "Someone finally went all the way. Put it inside me. Spent the bumpy ride bouncing on his cock."
    pc "Nice. Anyone say anything?"
    robin.name "Of course not. Probably jealous it's not them I'm bouncing on."
    pc "Probably."
    jump robin_talk_end

label robin_talk_bussex_3:
    robin.name "Got on the bus to school the other day and it was packed. Stood between these two guys."
    pc "Ha, asking for trouble there."
    robin.name "Yup. Ended up kissing the guy in front while the guy behind fingered my arsehole."
    pc "Oh wow. Getting all romantic with these perverts now?"
    jump robin_talk_end

label robin_talk_bussex_4:
    robin.name "So when you going to join me on the bus?"
    pc "This is your perversion. Not mine."
    robin.name "Yeah right. Like you don't enjoy the rides to school as much as I do."
    pc "Don't think anyone enjoys them as much as you..."
    jump robin_talk_end

label robin_talk_bussex_5:
    robin.name "You know I am not the only one who rides the bus for fun."
    pc "No?"
    robin.name "Seen the same girl a few times and wondered why I kept seeing her. No one needs to ride the bus that often."
    robin.name "Then I caught her trying to wriggle out of some guy's arms."
    pc "So she's not a fan of it then?"
    robin.name "But then I saw her pretend to stumble back into the guys arms. She didn't make much more effort to resist after that."
    pc "Hmmm..."
    jump robin_talk_end

label robin_talk_bussex_6:
    robin.name "I saw one woman on the bus. Older than us and seemed like she worked the hospital or something. All dressed up in a fancy suit."
    pc "Mmm?"
    robin.name "She was super pretty so I noticed her. Like one of those women you used to see on TV."
    robin.name "Anyway, she walks up to stand somewhere, holds onto the handrail and basically shoves her arse into this other guys crotch."
    robin.name "The guy spends the whole time touching her, might have even fucked her, and the whole time she's just standing there pretending to read something."
    pc "You are should be making a bus pervert club."
    jump robin_talk_end

label robin_talk_bussex_7:
    robin.name "Bus was quiet the other day, only a few people on it."
    pc "Oh poor you."
    robin.name "Yeah. So I ended up sitting right next to like the only guy on the bus."
    pc "How'd he react?"
    robin.name "Confused at first, but then I started to touch his crotch."
    pc "You are a bus pervert!"
    robin.name "And? I sucked him off and he wasn't complaining."
    jump robin_talk_end

label robin_talk_bussex_8:
    robin.name "Bus was quiet the other day, only a few people on it."
    pc "Oh poor you."
    robin.name "Yeah. So I ended up sitting right next to like the only guy on the bus."
    pc "How'd he react?"
    robin.name "Confused at first, but then I started to touch his crotch."
    pc "You are a bus pervert!"
    robin.name "And? I sucked him off and he wasn't complaining."
    jump robin_talk_end

label robin_talk_bussex_9:
    robin.name "Some guys on the bus get a bit too pushy sometimes."
    pc "Isn't that kinda why you do it?"
    robin.name "Well yeah. But they sometimes act like it's a foregone conclusion that I will let them do things to me."
    pc "Well, it is..."
    robin.name "I still want to play the game though. If I wanted just to fuck I'd take someone into the toilets at the pub."
    robin.name "I still want them to get all excited and surprised that I am not running away or something."
    pc "Right..."
    jump robin_talk_end

label robin_talk_bussex_10:
    robin.name "Some girl was giving me the right stink eye on the bus."
    pc "Did you have someone's dick in you?"
    robin.name "Well yeah. But but so what? Better me than her."
    pc "Maybe she wanted it to be her?"
    robin.name "Not like there are any shortage of perverts on the bus."
    jump robin_talk_end





label robin_talk_sexgossip_1:
    $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
    pc "So, want a story then?"
    robin.name "Ooh, have something fun?"
    pc "Well, I have been fooling around with the boys at the pitch."
    robin.name "Oooh wow. I didn't know. Err... What did you do with them?"
    pc "I fucked all of them."
    show robin happy
    robin.name "Oooh fuck! Wow. Err..."
    robin.name "Wow!"
    pc "Mmm..."
    jump robin_talk_end

label robin_talk_sexgossip_2:
    pc "So, I was at the pub doing a job. And... Err... Sure you want to know?"
    robin.name "Keep going."
    pc "So this guy offered me some money to seduce some other guy."
    robin.name "Oooh, whoring you out for someone else? Nice friend he has."
    pc "Err, sure. Friends."
    pc "So I only had to play around with him and just a little bit of fun."
    pc "But I kinda liked the guy and ended up going all the way with him."
    pc "Ended up fucking him by the end of it."
    robin.name "Haha, bet he was happy."
    pc "He was."
    jump robin_talk_end

label robin_talk_sexgossip_3:
    robin.name "So, how much fun do you have with the guys at the pub?"
    if pubpatron.naughty and not pubpatron.sex:
        pc "Not a lot actually. I have fooled around a bit but not had sex with any of them."
        robin.name "Yet."
        pc "Haha. Yet."
        robin.name "Tell me when you let one of them give you a good fucking."
        pc "Should take you there to get a good fucking."
        robin.name "Mmm. One day."
    elif pubpatron.sex > 5 and pubpatron.sex > int(pubpatron.sold * 0.6):
        pc "Well, have taken some money for fun but more often than not I wind up drunk and just mess around for free."
        robin.name "Ooh, such a slut you let them fuck you for free?"
        pc "I guess so..."
        robin.name "Even better you dirty bitch."
        pc "Hey. Stop trying to excite me!"
        $ player.spank()
        pc "Ung!"
        pc "Stop!"
    elif pubpatron.sex > 5:
        pc "Well, it's a good way to make some more money."
        robin.name "Oh? Whoring out at the pub a lot?"
        pc "Not sure it would be considered a lot. Still have a job to do."
        robin.name "But still been taken to the toilets and fucked like a bitch?"
        pc "Err... Sure?"
        pc "You really do get into this don't you?"
        robin.name "You're the one being a good little whore."
        pc "Yeah... You are..."
    elif pubpatron.sex:
        pc "Hmm, not a lot actually."
        robin.name "Not a lot isn't a \"no\"."
        pc "Well, no. It's not."
        robin.name "Going to have to come there one night and spy on you."
        pc "Yeah, surprised you haven't already."
    else:
        pc "Err, honestly not really."
        robin.name "Oh? Nothing fun to tell me?"
        pc "Nothing..."
        robin.name "Shame."
    jump robin_talk_end

label robin_talk_sexgossip_4:
    pc "You know [jaylee.name] right?"
    robin.name "Yeah. The scavver girl that has a thing for you."
    pc "I was hanging round her trailer late and night and decided to crash at her place."
    robin.name "Damn. Surprised you made it out alive."
    pc "I woke up to her tongue up my arse."
    robin.name "Haha! Sounds about right. You do a runner?"
    pc "I closed my eyes and enjoyed."
    robin.name "Don't be getting ideas now about sneaking into my room at night."
    pc "Ha. If I do then you will get the same treatment."
    robin.name "Hmmm. Actually might not be so bad."
    jump robin_talk_end

label robin_talk_sexgossip_5:
    pc "So some guy in school came up to me and offered me money."
    robin.name "Oh? In school? Didn't think anyone there could afford it."
    pc "Well, he could I guess."
    robin.name "You fuck him?"
    pc "Fucked him and me left me leaking cum in the toilets."
    robin.name "Ohh you dirty girl."
    jump robin_talk_end

label robin_talk_sexgossip_6:
    pc "So I had a weird encounter."
    robin.name "Aren't most of them?"
    pc "This one more so. I was hiding in the bushes..."
    robin.name "Off to a good start."
    pc "Was keeping an eye out for a friend who was whoring but a bit scared to be left alone."
    pc "Some guy comes up behind me and starts getting all handsy. I kinda just let him carry on."
    robin.name "'Cos you're a slut."
    pc "He sticks it in me and starts all barking and howling like a dog, beating my arse and calling me a bitch."
    robin.name "In a fun way?"
    pc "Yeah, fun thing. Then started going on how he will knot me like a bitch, came inside, howled, beat my ass more and left."
    robin.name "Haha fucking hell [name]! You sure know how to pick them."
    jump robin_talk_end





label robin_talk_insem_1:
    $ player.face_happy()
    pc "So, right now I have lot's of little swimmers trying to make me a mother."
    show robin happy
    robin.name "What? Right now?"
    pc "Yup!"
    jump robin_talk_end

label robin_talk_insem_2:
    $ player.face_happy()
    pc "So, I might be pregnant."
    show robin happy
    robin.name "What? You took a test?"
    pc "No, but right now I have someone still inside me giving it a try."
    robin.name "Ah you slut!"
    jump robin_talk_end

label robin_talk_robinfirst_preg_1:
    robin.name "So how is it being pregnant?"
    pc "Hard to walk and always need to pee. Why?"
    robin.name "Just wondering. Probably won't be too long til I am the same."
    pc "Oh? You trying or something?"
    robin.name "No condoms or pills. So it's bound to happen eventually."
    pc "You don't sound upset."
    robin.name "Not really. Not happy either. If it's going to happen, might as well accept it."
    jump robin_talk_end

label robin_talk_robinfirst_preg_2:
    robin.name "So you getting on okay being pregnant?"
    pc "As best as a huge belly can let me."
    robin.name "Anything I should know about for when it's me like that?"
    pc "Take every chance you can get to pee. And sit. And... Err, do things the moment you can."
    robin.name "Right."
    jump robin_talk_end

label robin_talk_robinfirst_robinpreg_1:
    robin.name "When you were pregnant, you have guys coming up to you more?"
    pc "Yeah, they think since we are pregnant, we are sluts or something so harass a bit more."
    robin.name "Ah. Right... Yeah I guess."
    jump robin_talk_end

label robin_talk_robinfirst_robinpreg_2:
    robin.name "You get much exercise in when you were pregnant?"
    pc "In the beginning, yeah. But after I got huge I just gave yup on it. Walking to the toilet is hard enough."
    robin.name "I know right!"
    jump robin_talk_end

label robin_talk_preg_1:
    pc "Uff. Getting harder and harder to move around."
    pc "Maybe letting it get this far wasn't such a good idea."
    jump robin_talk_end

label robin_talk_preg_2:
    pc "Would think people would move out the way more on the bus after seeing me carrying this belly around. But I swear it's the opposite."
    robin.name "Maybe they think you would be happy to take a seat, even if it's on their cock."
    pc "Haha. Probably I would after all the day walking."
    robin.name "Win win."
    jump robin_talk_end

label robin_talk_robinpreg_1:
    pc "Not able to play football any more with that?"
    robin.name "I still try, but it's hard. Struggling to even walk let alone run."
    pc "As well, Good excuse to play some more once you get rid of it."
    robin.name "Yeah, until someone puts a new one in me."
    if not numgen(0,20):
        pc "GOAL!"
        robin.name "Arsehole!"
    jump robin_talk_end

label robin_talk_robinpreg_2:
    pc "The boyish tomboy with a preggo belly. Bet that gets you some looks."
    robin.name "Na, not really."
    pc "No? Would think most people think you a lesbian."
    robin.name "All the more reason for people to try it with me. Can't imagine the amount of offers to \"turn me to the other side\" I have got."
    pc "Oh wow."
    if not numgen(0,20):
        robin.name "They get pretty shocked when I let them. I let them think they are fucking a lesbian and it's my first time with cock."
        pc "Ahhh fuck you sly bitch!"
    jump robin_talk_end

label robin_talk_preglate_1:
    pc "So, still waiting on my period."
    if player.has_perk(perk_preg_want):
        robin.name "Ooh, good for you. Been wanting this haven't you?"
        pc "Yeah, though still kinda scary."
        robin.name "Yup. Fat [name] for the next while."
        pc "Still early days. Have some time yet."
    else:
        robin.name "Oh?"
        pc "Yeah..."
    jump robin_talk_end

label robin_talk_preglate_2:
    pc "Period isn't coming..."
    robin.name "Yeah, we all know what that means."
    pc "These days, yeah."
    jump robin_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
