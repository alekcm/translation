init python:
    def jaylee_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        text_desc = ""
        
        if not jaylee.isactive and "jaylee_meet_events" in jaylee.dict and not renpy.has_label("jaylee_meet_" + str(jaylee.dict["jaylee_meet_events"])):
            text_desc = "Scavving outside of Blaston."
        elif "jaylee_meet_events" in jaylee.dict and renpy.has_label("jaylee_meet_" + str(jaylee.dict["jaylee_meet_events"])):
            text_desc = "Somewhere around the junk yard probably."
        elif t.time_from_to(23.00, 23.30): 
            cur_location = loc_junk_trailer_bathroom
        elif t.time_from_to(22.00, 09.00): 
            cur_location = loc_junk_trailer 
        elif t.hour in [18,19,20,21,9,10]: 
            cur_location = loc_junk_2
        else:
            text_desc = "Somewhere around the junk yard probably."
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where, text_desc) 

label jaylee_meet_picker:
    if not "jaylee_meet_events" in jaylee.dict:
        $ jaylee.dict["jaylee_meet_events"] = 0
    if not "jaylee_talk_sex_chain" in jaylee.dict:
        $ jaylee.dict["jaylee_talk_sex_chain"] = 0
    if not "jaylee_talk_preg_chain" in jaylee.dict:
        $ jaylee.dict["jaylee_talk_preg_chain"] = 0
    if not "jaylee_talk_story_chain" in jaylee.dict:
        $ jaylee.dict["jaylee_talk_story_chain"] = 0
    if not "jaylee_talk_home_chain" in jaylee.dict:
        $ jaylee.dict["jaylee_talk_home_chain"] = 0
    if not "jaylee_talk_outside_chain" in jaylee.dict:
        $ jaylee.dict["jaylee_talk_outside_chain"] = 0


    if renpy.has_label("jaylee_meet_" + str(jaylee.dict["jaylee_meet_events"])):
        jump expression "jaylee_meet_" + str(jaylee.dict["jaylee_meet_events"])
    else:
        jump jaylee_meet_generic_picker

label jaylee_meet_0:
    $ jaylee.dict["jaylee_meet_events"] += 1
    show jaylee at right1 with dissolve
    jaylee.name "Oh, you came back?"
    pc "Yeah, checking the place out and seeing what I can find."
    jaylee.name "Hard work but it pays. An' you get to keep your soul while yer at it."
    pc "Mmm."
    hide jaylee with dissolve
    jump travel

label jaylee_meet_1:
    $ jaylee.dict["jaylee_meet_events"] += 1
    show jaylee at right1 with dissolve
    jaylee.name "So been putting yourself to work?"
    pc "Yeah, how do you know?"
    jaylee.name "[ashon.name] is my brother. He mentioned you picking some stuff up and selling it off."
    pc "Ah."
    jaylee.name "Good to hear I'll be seeing more of you round here."
    pc "Yeah..."
    hide jaylee with dissolve
    jump travel

label jaylee_meet_2:
    $ jaylee.dict["jaylee_meet_events"] += 1
    show jaylee at right1 with dissolve
    jaylee.name "Oh. Much nicer face than the usual lot round here. Could get used to this."
    pc "Huh?"
    jaylee.name "Nothing! Happy to see you."
    hide jaylee with dissolve
    pcm "Okay..."
    jump travel

label jaylee_meet_3:
    $ jaylee.dict["jaylee_meet_events"] += 1
    show jaylee happy at right1 with dissolve
    jaylee.name "HI!"
    pc "Hey."
    hide jaylee with dissolve
    pcm "See ya then?"
    jump travel

label jaylee_meet_4:
    $ jaylee.dict["jaylee_meet_events"] += 1
    pcm "That's the scavver girl."
    show jaylee worried at right1 with dissolve:
        xzoom -1
    jaylee.name "Nng!"
    pc "Need help?"
    jaylee.name "Na. Even with 5 of us that thing ain't coming out. Leave it for another time."
    pc "Ok."
    show jaylee neutral with dissolve:
        xzoom 1
    jaylee.name "[name]!"
    pc "Yes?"
    show jaylee happy
    jaylee.name "Hi!"
    pc "Hey."
    hide jaylee with dissolve
    pcm "Right then."
    jump travel

label jaylee_meet_5:
    $ jaylee.dict["jaylee_meet_events"] += 1
    show jaylee happy at right1 with dissolve
    jaylee.name "Wanna drink?"
    pc "Sure?"
    $ inv.take(item_beer)
    hide jaylee with dissolve
    jump travel

label jaylee_meet_6:
    $ jaylee.dict["jaylee_meet_events"] += 1
    show jaylee angry at right1 with dissolve
    jaylee.name "Ugh!"
    pc "You ok?"
    show jaylee worried
    jaylee.name "Yeah, jus' jammed my finger. Bleeding a bit."
    if inv.qty(item_scrap_cloth):
        pc "I have some cloth if you need to wrap it."
        jaylee.name "Yeah?"
        pc "Here. Wrap it up and should be fine."
        show jaylee happy
        jaylee.name "Thanks."
    else:
        pc "You have something to wrap it in?"
        jaylee.name "I'll just use my top 'til it stops bleeding."
    hide jaylee with dissolve
    jump travel

label jaylee_meet_7:
    $ jaylee.dict["jaylee_meet_events"] += 1
    show jaylee happy at right1 with dissolve
    jaylee.name "Hey [name]. Keeping well?"
    pc "Same as always."
    jaylee.name "Not letting these filthy scavvers push you round?"
    pc "Ugh, they can try."
    jaylee.name "Heh."
    hide jaylee with dissolve
    jump travel

label jaylee_meet_8:
    $ jaylee.dict["jaylee_meet_events"] += 1
    show jaylee happy at right1 with dissolve
    jaylee.name "Hey [name]. Come here."
    pc "Hey. What's up?"
    jaylee.name "Wanna buy these?"
    pc "Ear rings?"
    jaylee.name "Sort of. Nipple rings."
    pc "You dig them up?"
    jaylee.name "Yeah. They were in a little box someone brought back."
    pc "New business opportunity for you there."
    jaylee.name "Right?"
    jaylee.name "Wonder if I can make do with some more. Come across any jewellery stuff and I might buy it off you."
    pc "Yeah? I'll keep you in mind."
    $ jaylee.active = True
    hide jaylee with dissolve
    jump travel

label jaylee_meet_9:
    $ jaylee.dict["jaylee_meet_events"] += 1
    show jaylee happy at right1
    jaylee.name "Hey sweetie. I decided I would sell some stuff."
    pc "Yeah?"
    jaylee.name "Come see me near my trailer after 6 or so."
    pc "Your trailer?"
    jaylee.name "Yeah, I live in this shithole. Got me a nice little place. Come by."
    pc "Ok."
    hide jaylee with dissolve
    jump travel

label jaylee_meet_generic_picker:
    jump expression WeightedChoice([
    ("jaylee_meet_generic_1", 100),    
    ("jaylee_meet_generic_2", 100),  
    ("jaylee_meet_generic_3", 100),  
    ("jaylee_meet_generic_4", 100),  
    ("jaylee_meet_generic_5", 100),  
    ("jaylee_meet_generic_6", 100),  
    ("jaylee_meet_generic_7", 100),  
    ("jaylee_meet_generic_8", 100),    
    ])

label jaylee_meet_generic_1:
    show jaylee at right1 with dissolve
    jaylee.name "Heya cutie. Good to see you still looking around."
    pc "Gotta pay the rent."
    jaylee.name "Junkyard livin' is free ya know."
    pc "Yeah..."
    hide jaylee with dissolve
    jump travel

label jaylee_meet_generic_2:
    show jaylee at right1 with dissolve
    jaylee.name "Hey sweetie. Come hang out later if you want. I am bored just standin' there looking at the stars."
    pc "Girl like you, thought you would have plenty of company."
    jaylee.name "Not the kind of company I want."
    hide jaylee with dissolve
    jump travel

label jaylee_meet_generic_3:
    show jaylee at right1 with dissolve
    jaylee.name "Hey babe. Good seein' your face around instead of the usual miserable lot."
    pc "I bet. Bit of a sausage fest round here. Though that's not always bad."
    jaylee.name "Meh."
    hide jaylee with dissolve
    jump travel

label jaylee_meet_generic_4:
    show jaylee at right1 with dissolve
    jaylee.name "Hey cutie. Come here. Take this."
    pc "Huh? What is it?"
    jaylee.name "Some junk I picked up. Go sell it on to my brother."
    $ inv.take(item_scrap_junk, 3)
    pc "Thanks."
    hide jaylee with dissolve
    jump travel

label jaylee_meet_generic_5:
    show jaylee happy at right5 with dissolve
    jaylee.name "Hey cutie!"
    pc "Hi."
    jaylee.name "Good to see you."
    pc "Err, you too..."
    pc "Any reason you are in my face."
    jaylee.name "No nicer place to be."
    $ player.face_annoyed()
    pc "Shoo!"
    hide jaylee with dissolve
    jump travel

label jaylee_meet_generic_6:
    $ player.spank()
    pc "Ah hey!"
    show jaylee happy at right5 with dissolve
    pc "You?"
    jaylee.name "Me!"
    pc "Bah. Shoo you pervert!"
    jaylee.name "Haha!"
    hide jaylee with dissolve
    jump travel

label jaylee_meet_generic_7:
    show jaylee happy at right1 with dissolve
    jaylee.name "Hey [name]! I have a secret to tell you."
    pc "Huh. Ok."
    show jaylee at right5 with dissolve
    jaylee.name "I want you to sit on my face."
    hide jaylee with dissolve
    pc "I'll stick my thumb up your arse you pervert!"
    pcm "..."
    pcm "That's not really a threat... Damn bitch would like it..."
    jump travel

label jaylee_meet_generic_8:
    show jaylee at right1 with dissolve
    jaylee.name "Hey good lookin'. Any these scavvers give you trouble and I'll kick their arse for them."
    pc "Well, there is this one perverted scavver."
    jaylee.name "Huh? Who?"
    pc "Some horny bitch who prowls the heaps looking for young girls to drag into her trailer. I hear they are never seen again."
    jaylee.name "Oh sweetie. Young girls are safe around me. It's only you who might get dragged away."
    pc "Hah! I'll bite."
    jaylee.name "Please do."
    pc "Shoo!"
    hide jaylee with dissolve
    jump travel





label jaylee_talk_picker:
    if not "jaylee_meet_events" in jaylee.dict:
        $ jaylee.dict["jaylee_meet_events"] = 0
    if not "jaylee_talk_sex_chain" in jaylee.dict:
        $ jaylee.dict["jaylee_talk_sex_chain"] = 0
    if not "jaylee_talk_preg_chain" in jaylee.dict:
        $ jaylee.dict["jaylee_talk_preg_chain"] = 0
    if not "jaylee_talk_story_chain" in jaylee.dict:
        $ jaylee.dict["jaylee_talk_story_chain"] = 0
    if not "jaylee_talk_home_chain" in jaylee.dict:
        $ jaylee.dict["jaylee_talk_home_chain"] = 0
    if not "jaylee_talk_outside_chain" in jaylee.dict:
        $ jaylee.dict["jaylee_talk_outside_chain"] = 0


    if loc_cur in (loc_junk_trailer, loc_junk_trailer_bathroom):
        if t.hour in (23,0,7):
            show jaylee underwear at right1 with dissolve
        else:
            show jaylee at right1 with dissolve
        if t.hour in (23,0,7) and not "seen_naked" in jaylee.conversation_topics:
            jump jaylee_home_talk_naked
    else:

        show jaylee at right1 with dissolve

    jump expression WeightedChoice([
    ("jaylee_talk_home_chain_" + str(jaylee.dict["jaylee_talk_home_chain"]), If(renpy.has_label("jaylee_talk_home_chain_" + str(jaylee.dict["jaylee_talk_home_chain"])) and loc_cur == loc_junk_trailer, 200, 0)),
    ("jaylee_talk_story_chain_" + str(jaylee.dict["jaylee_talk_story_chain"]), If(renpy.has_label("jaylee_talk_story_chain_" + str(jaylee.dict["jaylee_talk_story_chain"])), 300, 0)),
 
    ("jaylee_talk_jay_preg_0", If(not jaylee.dict["jaylee_talk_preg_chain"] and jaylee.days_pregnant > (global_pregnancy_length * 0.3), 100, 0)),
    ("jaylee_talk_jay_preg_" + str(jaylee.dict["jaylee_talk_preg_chain"]), If(renpy.has_label("jaylee_talk_jay_preg_" + str(jaylee.dict["jaylee_talk_preg_chain"])) and jaylee.dict["jaylee_talk_preg_chain"], 100, 0)),
    
    ("jaylee_talk_sextalk_chain_" + str(jaylee.dict["jaylee_talk_sex_chain"]), If(renpy.has_label("jaylee_talk_sextalk_chain_" + str(jaylee.dict["jaylee_talk_sex_chain"])) and jaylee.love > 25, 100, 0)),
    
    ("jaylee_talk_preg_start", If(not "seen_pc_preg" in jaylee.conversation_topics and player.pregnancy > 1, 1000, 0)),
    
    ("jaylee_junk_talk_subject", 100),    
    ])

label jaylee_junk_talk_subject:
    jump expression WeightedChoice([

    ("jaylee_talk_general_1", 100),
    ("jaylee_talk_general_2", 100),
    ("jaylee_talk_general_3", If(any([drake.sex, nate.sex, dan.sex]), 100, 0)),
    ("jaylee_talk_general_4", 100),
    ("jaylee_talk_general_5", 100),
    ("jaylee_talk_general_6", 100),
    ("jaylee_talk_general_7", 100),
    ("jaylee_talk_general_8", 100),

    ("jaylee_talk_leaving_1", If(t.wkday in ["Wednesday", "Thursday"], 50, 0)),
    ("jaylee_talk_leaving_2", If(t.wkday in ["Wednesday", "Thursday"], 50, 0)),
    ("jaylee_talk_leaving_3", If(t.wkday in ["Wednesday", "Thursday"], 50, 0)),

    ("jaylee_talk_return_1", If(t.wkday in ["Friday", "Saturday"], 50, 0)),
    ("jaylee_talk_return_2", If(t.wkday in ["Friday", "Saturday"], 50, 0)),
    ("jaylee_talk_return_3", If(t.wkday in ["Friday", "Saturday"], 50, 0)),

    ("jaylee_talk_preg_1", If(player.pregnancy >= 2 and "seen_pc_preg" in jaylee.conversation_topics, 50, 0)),
    ("jaylee_talk_preg_2", If(player.pregnancy >= 2 and "seen_pc_preg" in jaylee.conversation_topics, 50, 0)),
    ("jaylee_talk_preg_3", If(player.pregnancy >= 2 and "seen_pc_preg" in jaylee.conversation_topics, 50, 0)),

    ("jaylee_talk_pub_1", If(pub_waitress.timesworked > 5, 100, 0)),
    ("jaylee_talk_pub_2", If(pub_waitress.timesworked > 5, 100, 0)),
    ("jaylee_talk_pub_3", If(pub_waitress.timesworked > 5, 100, 0)),
    ("jaylee_talk_pub_4", If(pub_waitress.timesworked > 5, 100, 0)),
    ("jaylee_talk_pub_5", If(pub_waitress.timesworked > 5, 100, 0)),
    ("jaylee_talk_pub_6", If(pub_waitress.timesworked > 5, 100, 0)),
    ("jaylee_talk_pub_7", If(pub_waitress.timesworked > 5, 100, 0)),
    ("jaylee_talk_pub_8", If(pub_waitress.timesworked > 5, 100, 0)),
    ("jaylee_talk_pub_9", If(pub_waitress.timesworked > 5 and not c.outfit == 6, 100, 0)),
    ("jaylee_talk_pub_10", If(pub_waitress.timesworked > 5 and c.outfit == 6 and not "seen_bardress" in jaylee.conversation_topics, 100, 0)),

    ("jaylee_talk_clothes_1", If(c.outfit == 6, 100, 0)),
    ("jaylee_talk_clothes_2", If(c.ass, jaylee.lust, 0)),
    ("jaylee_talk_clothes_3", If(c.clevage and player.breasts > 1, jaylee.lust, 0)),
    ("jaylee_talk_clothes_4", If(c.slutty, jaylee.lust, 0)),
    ("jaylee_talk_clothes_5", If(c.exposed, jaylee.lust, 0)),

    ("jaylee_talk_ask_mags_intro", If(not "mags_ask" in jaylee.conversation_topics, 250, 0)),
    ("jaylee_talk_ask_mags_porn", If("mags_ask" in jaylee.conversation_topics and not "mags_porn" in jaylee.conversation_topics, 250, 0)),
    ("jaylee_talk_ask_mags_felix", If("mags_porn" in jaylee.conversation_topics and school_photo_intro_quest_complete and not "mags_felix" in jaylee.conversation_topics, 250, 0)),
    ("jaylee_talk_ask_mags_felix_photos", If("mags_felix" in jaylee.conversation_topics and not "mags_felix_photos" in jaylee.conversation_topics, 250, 0)),
    ("jaylee_talk_ask_mags_felix_photos_sexy", If("mags_felix_photos" in jaylee.conversation_topics and not "photos_sexy" in jaylee.conversation_topics, 250, 0)),
    ("jaylee_talk_ask_mags_felix_photos_sexy_tell", If("photos_sexy" in jaylee.conversation_topics and not "photos_sexy_told" in jaylee.conversation_topics, 250, 0)),
    ("jaylee_talk_ask_mags_soccerboys", If(not "mags_soccerboys" in jaylee.conversation_topics and "mags_porn" in jaylee.conversation_topics and nate.love >= 30, 250, 0)),

    ])





label jaylee_talk_home_chain_0:
    $ jaylee.dict["jaylee_talk_home_chain"] += 1
    pc "Nice place."
    jaylee.name "Pfft. Yeah right. It's a dump. Don't be talking rubbish just 'cos it's my place."
    pc "Well..."
    pc "It's home at least."
    jump jaylee_talk_end

label jaylee_talk_home_chain_1:
    $ jaylee.dict["jaylee_talk_home_chain"] += 1
    pc "What made you choose to live here anyway?"
    jaylee.name "It was safe."
    pc "Other places are safe as well."
    jaylee.name "Now, yes. Before not so much."
    jaylee.name "When the police... Security, were rounding everyone up to inject them, it was chaos."
    jump jaylee_talk_end

label jaylee_talk_home_chain_2:
    $ jaylee.dict["jaylee_talk_home_chain"] += 1
    pc "So security were rounding everyone up. What does that have to do with living in a crate?"
    jaylee.name "No one is gonna break into a crate. Nothing here. Not that they know of anyway."
    jaylee.name "But the crazies would see a light in a window and kick your door down."
    jaylee.name "Either had to be in a group bigger than the lunatics or hide away from everyone."
    jump jaylee_talk_end

label jaylee_talk_home_chain_3:
    $ jaylee.dict["jaylee_talk_home_chain"] += 1
    pc "But isn't the junkyard new? How did you and [ashon.name] live here when there was no junkyard?"
    jaylee.name "Bunch of us huddled in crates on the trains you see out there."
    jaylee.name "Complete chaos lasted about 2 weeks, but it was still tense for a while afterwards so most of us stuck around."
    jaylee.name "When security set up shop in the sheds over there, we thought it better to just stick around for a bit."
    jaylee.name "Those fucks didn't do shit to help us, but at least them being there scared off the nutters so it was somewhat ok."
    jump jaylee_talk_end

label jaylee_talk_home_chain_4:
    $ jaylee.dict["jaylee_talk_home_chain"] += 1
    pc "How did things end up getting better so quickly? Wasn't that like less than a year ago?"
    jaylee.name "People got jabbed, killed or ran away so security didn't need to be prowling the streets all day hunting plagueies."
    pc "The fuck is a plagueie?"
    jaylee.name "Dunno, just made it up. People who didn't want to be jabbed or were already infected. Nutters basically."
    jaylee.name "We were literally piling and burning bodies in the streets and these fuckers still want to run from the cure."
    pc "Ugh."
    jump jaylee_talk_end

label jaylee_talk_home_chain_5:
    $ jaylee.dict["jaylee_talk_home_chain"] += 1
    pc "So why don't you live somewhere more homely now?"
    if player.has_perk(perk_whore):
        jaylee.name "Yeah right. You take dick for cash so you already know the real cost of living somewhere like that?"
    else:
        jaylee.name "Yeah right. Then I'd have to take dick for cash to pay the rent."
    jaylee.name "Ain't nobody in those builds getting by legit. You lot are all up to something to keep you from the slums."
    jaylee.name "Might be a shitty box, but it's my box and I don't have to take it in the arse to keep it."
    pc "..."
    jump jaylee_talk_end

label jaylee_talk_home_chain_6:
    $ jaylee.dict["jaylee_talk_home_chain"] += 1
    pc "Did you say you were burning bodies in the streets?"
    jaylee.name "Yeah, didn't you have to do that?"
    pc "When we ran away, the city was still in the \"rob and murder anyone you suspect of having food\" stage."
    pc "Of course the scum took that as an opportunity to rape and kill like bandits or raiders."
    pc "Unless you were part of some huge group, you were just waiting to be killed so we got out as quick as we could."
    jaylee.name "Oh..."
    jump jaylee_talk_end

label jaylee_talk_home_chain_7:
    $ jaylee.dict["jaylee_talk_home_chain"] += 1
    jaylee.name "We didn't have such food problems. Not enough to murder for anyway."
    pc "No?"
    jaylee.name "Military folk nearby took control pretty quickly and would shoot on sight anyone breaking curfew."
    jaylee.name "They probably saw the shit going down elsewhere and put a lid on that right away. Plus Blaston is much smaller."
    jump jaylee_talk_end

label jaylee_home_talk_naked:
    $ add_to_list(jaylee.conversation_topics, "seen_naked")
    if player.has_perk(perk_exhibitionist):
        pc "You are naked?"
        jaylee.name "Yeah, just got out the shower. You like?"
        hide jaylee
        show jaylee_pose_stand
        with dissolve
        pc "..."
        $ pc_striptease(True)
        $ pc_set_temp_outfit()
        jaylee.name "Not that I am complaining, but why did you get naked?"
        pc "I like being naked."
        jaylee.name "Okay..."
        jaylee.name "I like you being naked."
    else:
        $ player.face_shy()
        pc "Errr..."
        jaylee.name "What?"
        pc "You are naked?"
        jaylee.name "I just got out the shower. Like what you see?"
        hide jaylee
        show jaylee_pose_stand
        with dissolve
        pc "Errm..."
        pc "Yeah...?"
        pc "And no clothes?"
        jaylee.name "I live in a coffin box. What makes you think I have a nice collection of clothes like you do?"
        jaylee.name "Gotta clean and air my stuff out before tomorrow."
        pc "Right..."
    hide jaylee_pose_stand
    show jaylee underwear at right1
    with dissolve
    jump jaylee_talk_end





label jaylee_talk_story_chain_0:
    $ jaylee.dict["jaylee_talk_story_chain"] += 1
    show jaylee happy at right1
    jaylee.name "Come to keep me company?"
    pc "Sure. What you up to anyway?"
    show jaylee neutral
    jaylee.name "Hanging out. Not much else to do."
    pc "Why here?"
    jaylee.name "I live here. Where else?"
    pc "I mean why not inside?"
    jaylee.name "Fuck all to do in there. At least out here I can look at the sky or people doing stuff."
    if weather_var == 3:
        pc "But it's pissing down."
        jaylee.name "If I hid away every time it was raining, I'd never be out."
    elif weather_var == 4:
        pc "But it's snowing."
        jaylee.name "Yeah, it's so nice."
        pc "I mean... Never mind."
    jump jaylee_talk_end

label jaylee_talk_story_chain_1:
    $ jaylee.dict["jaylee_talk_story_chain"] += 1
    pc "Do much other than scavving?"
    jaylee.name "Na, just check around this dump for stuff. I let [ashon.name] do all the brain work."
    pc "Not thought about work outside here?"
    jaylee.name "Only work I could see out there is letting drunks assfuck me for money."
    jaylee.name "I'll take my chances with the cretins outside the wall."
    jump jaylee_talk_end

label jaylee_talk_story_chain_2:
    $ jaylee.dict["jaylee_talk_story_chain"] += 1
    pc "You head out the wall?"
    jaylee.name "Yeah. Most of the folk there are smart as bricks so need someone who knows what they are looking for."
    pc "Isn't it dangerous?"
    jaylee.name "Na, the goons are too focused on not getting killed to lay hands on the girls that go out."
    pc "Wasn't talking about the goons..."
    jump jaylee_talk_end

label jaylee_talk_story_chain_3:
    $ jaylee.dict["jaylee_talk_story_chain"] += 1
    pc "Aren't there weirdos out there?"
    jaylee.name "Hah! That what the school kids are calling them?"
    pc "Actually no one really talks about them. Everyone avoids the topic."
    jaylee.name "Yeah, good for them."
    pc "You just did as well!"
    jump jaylee_talk_end

label jaylee_talk_story_chain_4:
    $ jaylee.dict["jaylee_talk_story_chain"] += 1
    pc "What do you do when you go out there?"
    jaylee.name "Me? Mostly point at shit and the idiots haul it in the truck."
    jaylee.name "No time to look around at stuff so just grab what looks like has the most salvage."
    jump jaylee_talk_end

label jaylee_talk_story_chain_5:
    $ jaylee.dict["jaylee_talk_story_chain"] += 1
    pc "So how long it usually take when you are out there?"
    jaylee.name "We leave first thing Thursday and usually back before night on a Friday."
    pc "What? You stay out there at night? Isn't that asking for trouble?"
    jaylee.name "Biggest trouble is making sure some brickhead doesn't wank over my face while I sleep."
    jaylee.name "It's fine otherwise."
    jump jaylee_talk_end

label jaylee_talk_story_chain_6:
    $ jaylee.dict["jaylee_talk_story_chain"] += 1
    pc "What if the weirdos sneak up on you at night?"
    jaylee.name "Dunno. Never happened."
    pc "But you prepare for it right?"
    jaylee.name "Yeah, I think so. The goons set up stuff to make sure they can't sneak up on us."
    jaylee.name "Traps n such."
    jump jaylee_talk_end





label jaylee_talk_story_chain_7:
    $ jaylee.dict["jaylee_talk_story_chain"] += 1
    jaylee.name "So what's it like getting by outside this place?"
    pc "What do you mean?"
    jaylee.name "I mean living out there."
    pc "You talk about \"out there\" as if it's the other side of the wall. It's you that heads \"out there\"."
    jaylee.name "Well yeah. But I mostly spend my time here in the junkyard. Don't really get the bus to other areas."
    pc "Well, might be a good thing."
    jump jaylee_talk_end

label jaylee_talk_story_chain_8:
    $ jaylee.dict["jaylee_talk_story_chain"] += 1
    jaylee.name "So... What's it like out there?"
    pc "Has its good and its bad. Bus can take you where you want to go but spend the entire ride with men trying to put their dicks in you."
    jaylee.name "Yeah I heard about that. It really that bad?"
    pc "Not \"that\" bad. Usually they just touch you or wank over you. Rare someone tries to dick you. And if they do it's probably because you let them."
    jaylee.name "Wait, let them? People let them do that?"
    pc "Heh."
    jump jaylee_talk_end

label jaylee_talk_story_chain_9:
    $ jaylee.dict["jaylee_talk_story_chain"] += 1
    pc "Some people enjoy the bus ride. Life is shit everywhere and some people look for fun in the oddest of places."
    pc "Most people get shit drunk or pop some Joy. Some people get their kicks from sticking their arse out on the bus and entertaining some strangers."
    jaylee.name "Uuuh. Wow. People are weird."
    pc "People have nothing much better to do."
    jump jaylee_talk_end

label jaylee_talk_story_chain_10:
    $ jaylee.dict["jaylee_talk_story_chain"] += 1
    jaylee.name "Ok, so other than getting fucked on the bus, what else goes on out there?"
    pc "You can get fucked on the beach if you want."
    jaylee.name "Fucking hell [name], you jus' winding me up now."
    pc "Maybe. Actually the beach isn't a bad place to hang out. Sand, water, sun and booze."
    jaylee.name "But wearing clothes for the beach must make you a target?"
    pc "Pfft. We are targets no matter what we wear."
    jump jaylee_talk_end

label jaylee_talk_story_chain_11:
    $ jaylee.dict["jaylee_talk_story_chain"] += 1
    jaylee.name "So if you're always a target, why go these places?"
    pc "It's life. Gotta live it best you can and accept that shit like this goes on. Not like it goes away if you hide."
    jaylee.name "Sounds like everyone wants to stick it in you out there."
    pc "Yeah right. Like everyone here doesn't want to stick it in you as well. Only difference is they will wind up a corpse if they did."
    jaylee.name "Well... Yeah..."
    jump jaylee_talk_end

label jaylee_talk_story_chain_12:
    $ jaylee.dict["jaylee_talk_story_chain"] += 1
    jaylee.name "But the school is nice?"
    pc "A couple of cunts but otherwise yeah. Not gonna get hit over the head just walking around at least."
    if any([shane.dead, marcus.dead]):
        pc "Actually not seen the cunts for a bit."
    jaylee.name "..."
    jump jaylee_talk_end

label jaylee_talk_story_chain_13:
    $ jaylee.dict["jaylee_talk_story_chain"] += 1
    pc "Got a nice big park not far from my house. It's a good place to relax."
    jaylee.name "No one trying to jump you there?"
    pc "Day time, no. Night time you run a good chance of being dragged into the bushes."
    jaylee.name "Fucking hell [name]. Why the hell you keep telling me I need to get out there when that goes on. Rather hide away here where it's safe."
    pc "Well, it's safe for you here. I still have to watch my arse when I bend over."
    jump jaylee_talk_end





label jaylee_talk_general_1:
    jaylee.name "Keeping up the scavving?"
    pc "Yeah, it pays."
    jaylee.name "Keeps you fit as well."
    pc "Ugh, rather a lazy job but have to make do."
    jump jaylee_talk_end

label jaylee_talk_general_2:
    jaylee.name "So what you been up to these days cutie?"
    pc "Same as always. Trying to get by. Work and alcohol mostly."
    jaylee.name "Do I need to start stocking booze for when you pop by?"
    pc "Hah, na. Plenty of that to go around. World has gone to shit but people still keep up production of booze."
    jaylee.name "It's probably the only thing stopping any riots."
    if player.has_perk(perk_whore):
        pc "That and the whores. Hell we should get a medal for keeping those shits from a murdering rampage."
    else:
        pc "That and the whores. Hell they should probably get a medal for keeping the scum out of a murdering rampage."
    jump jaylee_talk_end

label jaylee_talk_general_3:
    jaylee.name "How's your school harem going?"
    if player.preg_father_class in (drake, nate, dan):
        pc "Still carrying one of their babies so I guess good?"
        pc "Why? You interested?"
        jaylee.name "Sort of. They are your friends so good to know they are well."
        jaylee.name "Not interested in them putting a baby in me as well though. You are enough."
        pc "No? I'm sure they would love to give it a try."
        jaylee.name "Yeah right. Don't need both of us walking round like elephants."
    else:
        pc "That lot? Still hanging around the school as always. Safe there so they hardly leave."
        pc "Why? You interested?"
        jaylee.name "Sort of. They are your friends so good to know they are well."
        pc "Mmmm. They are also interested in seeing your sexy ass."
        jaylee.name "Oh? You like my ass?"
        pc "Don't turn this on me!"
    jump jaylee_talk_end

label jaylee_talk_general_4:
    jaylee.name "You know you have to be the only girl I know that has a wardrobe that extensive."
    pc "What can I say. I like dressing up. Plus gives me something to enjoy."
    pc "If I didn't spend money on my wardrobe then it would probably go all on booze or worse."
    jaylee.name "Well, I'm not complaining. Something new to look at every time you turn up"
    jump jaylee_talk_end

label jaylee_talk_general_5:
    jaylee.name "Keeping up the scavving?"
    pc "Yeah, it pays."
    jaylee.name "Keeps you fit as well."
    pc "Ugh, rather a lazy job but have to make do."
    jump jaylee_talk_end

label jaylee_talk_general_6:
    jaylee.name "Keeping up the scavving?"
    pc "Yeah, it pays."
    jaylee.name "Keeps you fit as well."
    pc "Ugh, rather a lazy job but have to make do."
    jump jaylee_talk_end

label jaylee_talk_general_7:
    jaylee.name "Keeping up the scavving?"
    pc "Yeah, it pays."
    jaylee.name "Keeps you fit as well."
    pc "Ugh, rather a lazy job but have to make do."
    jump jaylee_talk_end

label jaylee_talk_general_8:
    jaylee.name "Keeping up the scavving?"
    pc "Yeah, it pays."
    jaylee.name "Keeps you fit as well."
    pc "Ugh, rather a lazy job but have to make do."
    jump jaylee_talk_end





label jaylee_talk_leaving_1:
    pc "Stay safe out there tomorrow."
    jaylee.name "Aww. Worried about me?"
    pc "A bit."
    jump jaylee_talk_end

label jaylee_talk_leaving_2:
    jaylee.name "Heading out tomorrow. Hope it all goes smooth."
    pc "Big girl like you knows what she is up to. But yeah, be safe."
    jaylee.name "Not always me I am worried about but the clowns that come with us."
    pc "Mmm. Sometimes I think mannequins would be more useful than some of the lumps I see around."
    jump jaylee_talk_end

label jaylee_talk_leaving_3:
    pc "More stuff for you to pick up tomorrow. Be safe."
    jaylee.name "Probably the same old shit. Busted cars, fridges and washing machines."
    pc "A bit."
    jump jaylee_talk_end

label jaylee_talk_return_1:
    pc "So back safe from your trip outside. Glad to see."
    jaylee.name "Yeah, nothing much happen. Some jammed fingers and other scrapes"
    jaylee.name "All good."
    jump jaylee_talk_end

label jaylee_talk_return_2:
    jaylee.name "Looks like the scavvers are getting some good stuff from yesterday's haul."
    pc "Looks like. Good trip by he look of it."
    jaylee.name "Like usual. Lot of junk out there to drag back."
    pc "So no shortage anytime soon?"
    jaylee.name "Na, whole cities worth of shit out there. At this rate would be long dead before we notice a drop in stuff to grab."
    jump jaylee_talk_end

label jaylee_talk_return_3:
    pc "Find anything interesting out there yesterday?"
    jaylee.name "Same old stuff. Usually drag back as much heavy machinery as possible, so don't manage to get any smaller nice stuff."
    pc "No new clothes or stuff like that?"
    jaylee.name "Not unless it's inside a washing machine we carted back with us."
    jump jaylee_talk_end





label jaylee_talk_preg_start:
    $ add_to_list(jaylee.conversation_topics, "seen_pc_preg")
    if not jaylee.love > 40:

        jump jaylee_talk_picker
    jaylee.name "I didn't wanna say anything before, but you are preggo!"
    if jaylee.days_pregnant > (global_pregnancy_length * 0.3):
        pc "Yeah. Now we look like a pair of elephants walking around the junk heaps."
    else:
        pc "Yeah..."
    jaylee.name "Well, now I also wanna lick your belly."
    pc "Thought you might be upset?"
    jaylee.name "Why? Cos you are fucking other people? I am not such a child to be upset at that."
    pc "Well... Good I guess."
    jaylee.name "Good thing I have a nice strong bed that can hold your fat arse."
    if jaylee.days_pregnant > (global_pregnancy_length * 0.3):
        pc "Yeah right. Both of us would collapse almost anything."
        if "slept_together" in jaylee.conversation_topics:
            jaylee.name "Two apparent lesbos walking around knocked up. The guys round here are gonna love it."
            pc "Haha! Fuckers will be having all manner of fantasies."
    else:
        pc "Yeah, you should be so lucky."
    jump jaylee_talk_end

label jaylee_talk_preg_1:
    jaylee.name "Can't be easy scavving about with that belly."
    pc "Not really. But what can you do."
    jaylee.name "Mmmm."
    jump jaylee_talk_end

label jaylee_talk_preg_2:
    jaylee.name "You get the weirdos calling you out with that belly?"
    pc "Belly or not, the weirdos will be weirdos."
    jaylee.name "Haha. Ain't that the truth."
    jump jaylee_talk_end

label jaylee_talk_preg_3:
    jaylee.name "You managing to get work in that state?"
    pc "Yeah, mostly. Not like being pregnant round here is unusual."
    if jaylee.days_pregnant > (global_pregnancy_length * 0.3):
        jaylee.name "True. Half the scav girls have a bun in the oven. Us included."
    else:
        jaylee.name "True. Half the scav girls around here have a bun in the oven."
    pc "And even more Gamines are carrying one around."
    jump jaylee_talk_end





label jaylee_talk_pub_1:
    jaylee.name "How's the pub drunks treating you?"
    pc "Same as always. Nothing to do but find some meaning in the bottom of the glass."
    jaylee.name "Yeah, not gonna find anything there."
    pc "Nope. But worth a look anyway."
    jump jaylee_talk_end

label jaylee_talk_pub_2:
    jaylee.name "Don't you mind showing your ass off to everyone in the pub?"
    pc "Think I got a choice?"
    jaylee.name "Can work somewhere else?"
    pc "Hah. I work everywhere else. Still broke as shit at the end of it all."
    jump jaylee_talk_end

label jaylee_talk_pub_3:
    jaylee.name "Pub guys get handy?"
    pc "Not a person I've met who didn't after some beers."
    jaylee.name "Ugh."
    pc "It's fine. At least they tip when in the bar."
    jump jaylee_talk_end

label jaylee_talk_pub_4:
    jaylee.name "Any girls ever have a go at you in the pub?"
    pc "Rare to see girls in the pub actually. At least not ones who aren't whores."
    jaylee.name "Oh? Get a lot of whores there?"
    pc "Na, only ones that have been picked up already and keeping their punter happy."
    pc "Some guys prefer a date or something. Makes 'em feel normal I suppose."
    jump jaylee_talk_end

label jaylee_talk_pub_5:
    jaylee.name "Heard from folk round here the bar girls are basically whores."
    pc "Think you need to get out this scrapheap a bit and look around before saying that."
    jaylee.name "What? Why?"
    pc "You seen what it's like in the slums? No one wants to live there and will do what's needed to stay away."
    jump jaylee_talk_end

label jaylee_talk_pub_6:
    jaylee.name "Free booze at the pub though eh??"
    pc "Yeah. \"Free\". Just gotta keep who is buying them company."
    jaylee.name "Is that bad?"
    pc "Most of the time, no. Can be fun I guess. Get to chat to new people and relax a bit."
    jump jaylee_talk_end

label jaylee_talk_pub_7:
    jaylee.name "Pub drunks try and get you plastered?"
    pc "All the time."
    jaylee.name "How you manage to avoid it?"
    pc "Avoid?"
    jaylee.name "No?"
    pc "Pfft. Plastered is probably the best way to live round here."
    jump jaylee_talk_end

label jaylee_talk_pub_8:
    jaylee.name "You not worry what people think about you working the pub?"
    pc "Err... No?"
    jaylee.name "I mean it is a bit..."
    pc "Whore like?"
    jaylee.name "I mean... Yeah?"
    pc "Fuck, you really need to get your head out of the junk piles."
    jump jaylee_talk_end

label jaylee_talk_pub_9:
    if "seen_bardress" in jaylee.conversation_topics:
        jaylee.name "When you coming round with that bar dress on again?"
        pc "Who knows. Think it's safe?"
        jaylee.name "Eh? Why not?"
        pc "Not sure how long it will stay on with a bitch like you around."
        jaylee.name "Not long if I can help it."
    else:
        jaylee.name "When you gonna come round and show me that bar dress you have?"
        pc "Oh? Like it do you?"
        jaylee.name "I hear about the sexy girls wearing it. I wanna see."
        pc "We'll see."
    jump jaylee_talk_end

label jaylee_talk_pub_10:
    $ add_to_list(jaylee.conversation_topics, "seen_bardress")
    jaylee.name "That the bar dress? Fuck!"
    pc "Mmmm. Like it?"
    jaylee.name "With you in it. Fuck yes!"
    pc "Now your sounding like one of the drunks."
    jaylee.name "Yeah. Don't need booze t'wanna drag you off alone."
    pc "Down girl!"
    jaylee.name "Woof!"
    jump jaylee_talk_end





label jaylee_talk_clothes_1:
    jaylee.name "Come sit on my lap and I'll buy you a drink"
    pc "Don't remember you drinking much."
    jaylee.name "Whatever it takes to have you sit on me."
    pc "Do I need the dress for that?"
    jaylee.name "Nope!"
    jump jaylee_talk_end

label jaylee_talk_clothes_2:
    jaylee.name "Starting to have sympathy for the boys round here who stare at my arse."
    pc "You should give it to them."
    jaylee.name "Yeah right. You first."
    pc "Same time?"
    jaylee.name "Ha!"
    jump jaylee_talk_end

label jaylee_talk_clothes_3:
    pc "It's usually the guys round here that can't look me in he eyes."
    jaylee.name "Huh?"
    pc "Staring at my tits."
    jaylee.name "Well fuck! Look at them. Wanna stick my face betwe..."
    pc "Don't make me get a stick to beat you with."
    jaylee.name "I won't mind that either."
    jump jaylee_talk_end

label jaylee_talk_clothes_4:
    pc "..."
    jaylee.name "..."
    pc "You gonna say something?"
    jaylee.name "No. Just looking."
    pc "Not even trying to hide it?"
    jaylee.name "Well you aren't hiding anything so why should I pretend?"
    jump jaylee_talk_end

label jaylee_talk_clothes_5:
    jaylee.name "Please say this is an invitation for me to take you inside and..."
    pc "Shush."
    jaylee.name "Standing here like that and it's not?"
    pc "..."
    jaylee.name "Ah. Hard to get is it?"
    jump jaylee_talk_end





label jaylee_talk_sextalk_chain_0:
    $ jaylee.dict["jaylee_talk_sex_chain"] += 1
    pc "So, you a lesbian?"
    jaylee.name "Ha! What kind of question is that?"
    pc "Well, you haven't made much secret of... Y'know."
    jaylee.name "Wanting to stick my tongue up your arsehole?"
    jaylee.name "Swirl it about until..."
    pc "Yes. That."
    jaylee.name "No. I am not a lesbian."
    jump jaylee_talk_end

label jaylee_talk_sextalk_chain_1:
    $ jaylee.dict["jaylee_talk_sex_chain"] += 1
    pc "Not a lesbian, yet..."
    jaylee.name "Want to sit on your face and ride it 'til I scream?"
    pc "..."
    jaylee.name "You seen the perverts round here?"
    pc "Yeah. Some are nice. You are popular with them."
    jaylee.name "Yeah. \"Popular\". You know they have a bet going?"
    pc "They do?"
    jaylee.name "First to fuck me wins the pot."
    if jaylee.showing:
        pc "Well someone must have won the pot a while ago considering the belly."
        pc "Unless it was... Err... Sorry..."

    jump jaylee_talk_end

label jaylee_talk_sextalk_chain_2:
    $ jaylee.dict["jaylee_talk_sex_chain"] += 1
    pc "So someone wins the pot. What do you care."
    jaylee.name "I can't give them that satisfaction."
    pc "Probably satisfy you as well."
    jaylee.name "Maybe. Moment I fuck one of them, everyone will be talking about it."
    pc "And?"
    jaylee.name "Ugh."
    jump jaylee_talk_end

label jaylee_talk_sextalk_chain_3:
    $ jaylee.dict["jaylee_talk_sex_chain"] += 1
    jaylee.name "Having them make bets over it kinda makes it all feel weird. Like I am a whore."
    pc "So? You have your fun and they have theirs."
    jaylee.name "I was pissed off with it at first and got so used to rejecting them. It's kinda became my thing."
    jaylee.name "\"No one can get close to our [jaylee.name]. She's all pure and proper\"."
    jaylee.name "I kinda feel like I need to live up to it now..."
    jump jaylee_talk_end

label jaylee_talk_sextalk_chain_4:
    $ jaylee.dict["jaylee_talk_sex_chain"] += 1
    pc "If you can't fool around with the scavvers round here, why not someone not from here?"
    if any([drake.sex, nate.sex, dan.sex]):
        pc "I have a bunch of boys I drink with who wouldn't hesitate to come here and entertain you."
        jaylee.name "A bunch of them? Fucking hell."
        pc "Well, three. I drink with them after school. Nice lads."
        jaylee.name "How did we go from lesbian to fucked by three guys?"
    elif pub_waitress.sex:
        pc "Take you to the pub. Pretty sure everyone there will like to make yur acquaintance."
        jaylee.name "Yeah. Just like the perverts here. Fuck me like some meat."
        pc "It's not so bad..."
    else:
        pc "Get all dressed up and have some beers down Revel. Meet a couple of lads."
        jaylee.name "Ah the good old one night fuckfest. Think I'll pass."
    jaylee.name "Anyway, think I'd rather sit on your face than go through all that."
    jaylee.name "No chance of ending up with a baby in me."
    jump jaylee_talk_end

label jaylee_talk_sextalk_chain_5:
    $ jaylee.dict["jaylee_talk_sex_chain"] += 1
    pc "So not a lesbian but want to fuck girls instead of boys. Hmmm..."
    jaylee.name "Who told you I want to fuck girls?"
    pc "Err, you?"
    jaylee.name "I don't want to fuck girls. I want to fuck you."
    pc "Oooohhh... Shit."
    jump jaylee_talk_end

label jaylee_talk_sextalk_chain_6:
    $ jaylee.dict["jaylee_talk_sex_chain"] += 1
    $ loc_junk_trailer.locked = False
    jaylee.name "The key to my trailer is up there, behind the sheeting."
    pc "Oh? Why are you telling me that?"
    jaylee.name "If you need somewhere to stay, you can crash here."
    pc "Oh. Thanks, might take you up on the offer..."
    $ player.face_worried()
    pc "Hold on..."
    pc "I feel like I might end up in trouble if I do that."
    show jaylee happy
    jaylee.name "More trouble than you can imagine."
    jump jaylee_talk_end





label jaylee_talk_jay_preg_0:
    $ jaylee.dict["jaylee_talk_preg_chain"] += 1
    pc "Err... You been eating too much?"
    jaylee.name "No..."
    pc "Then how does a lesbian end up with that belly?"
    jaylee.name "I told you. I'm not a lesbian."
    jump jaylee_talk_end

label jaylee_talk_jay_preg_1:
    $ jaylee.dict["jaylee_talk_preg_chain"] += 1
    pc "The baby... It wasn't... You know..."
    jaylee.name "No, nothing like that. Don't worry."
    pc "Okay. Good."
    jump jaylee_talk_end

label jaylee_talk_jay_preg_2:
    $ jaylee.dict["jaylee_talk_preg_chain"] += 1
    pc "So who's the lucky man?"
    jaylee.name "You aren't going to drop this are you?"
    pc "Would you?"
    if player.pregnancy >= 2:
        jaylee.name "I'm not the only one knocked up here."
        pc "Yeah, but you are the only \"not lesbian\" that is."
        jaylee.name "Ugh..."
    else:
        jaylee.name "Yes?"
        pc "Haha. Liar!"
    jump jaylee_talk_end

label jaylee_talk_jay_preg_3:
    $ jaylee.dict["jaylee_talk_preg_chain"] += 1
    pc "So..."
    jaylee.name "This about my baby?"
    pc "Yup."
    jaylee.name "Look, I don't think you want to know."
    pc "Saying that makes me want to know even more."
    jaylee.name "Pfft!"
    jump jaylee_talk_end

label jaylee_talk_jay_preg_4:
    $ jaylee.dict["jaylee_talk_preg_chain"] += 1
    pc "Maybe you decided to let no one win the betting pot and have an orgy with all the scavvers..."
    jaylee.name "..."
    pc "Maybe one of the goons while over the wall scavving."
    jaylee.name "..."
    if dez.has_met:
        pc "Maybe the mechanic from the shop caught your eye?"
        jaylee.name "Well, he's not bad looking."
    jump jaylee_talk_end

label jaylee_talk_jay_preg_5:
    $ jaylee.dict["jaylee_talk_preg_chain"] += 1
    pc "You are a secret porn star who did one too many creampie shoots?"
    jaylee.name "Haha!"
    pc "Oooh, maybe it was a secret meeting with a scrap dealer who offered you the good for your goods?"
    jaylee.name "Yeah right..."
    jump jaylee_talk_end

label jaylee_talk_jay_preg_6:
    $ jaylee.dict["jaylee_talk_preg_chain"] += 1
    if any([drake.sex, nate.sex, dan.sex]):
        pc "Wait, you secretly met the boys from school I told you about and had a wild time with them?"
        jaylee.name "That one wouldn't be too bad."
    pc "Some handsome man came in here and romanced you."
    jaylee.name "You have a wild imagination."
    if pub_waitress.timesworked > 5:
        pc "Decided to go to the pub one night when I wasn't working and keep a nice guy company?"
        jaylee.name "Ha, no chance."
    pc "I'm running out of ideas here."
    jump jaylee_talk_end

label jaylee_talk_jay_preg_7:
    $ jaylee.dict["jaylee_talk_preg_chain"] += 1
    $ add_to_list(jaylee.conversation_topics, "ashon_sex_jaylee")
    pc "You are a secret highway girl looking to earn some extra?"
    jaylee.name "No way."
    pc "Err, maybe... Fuck I am scraping the barrel here."
    jaylee.name "It was [ashon.name]."
    pc "Ah! Why didn't I think of..."
    pc "Hold on..."
    jaylee.name "Not a word!"
    pc "..."
    jump jaylee_talk_end

label jaylee_talk_jay_preg_8:
    $ jaylee.dict["jaylee_talk_preg_chain"] += 1
    pc "So... [ashon.name] eh? How did that come about?"
    jaylee.name "Not gonna drop it are you?"
    pc "Not a chance in hell."
    jaylee.name "We have always done it since kids."
    pc "Ohh..."
    jump jaylee_talk_end

label jaylee_talk_jay_preg_9:
    $ jaylee.dict["jaylee_talk_preg_chain"] += 1
    pc "So weren't lying when you said not lesbian."
    jaylee.name "No..."
    pc "Well, good for you. He is a decent guy."
    jaylee.name "Wait. You serious?"
    pc "Yeah. Could do worse than him."
    jump jaylee_talk_end

label jaylee_talk_jay_preg_10:
    $ jaylee.dict["jaylee_talk_preg_chain"] += 1
    jaylee.name "Thought you would shit all over me for having sex with him."
    pc "Why would I care?"
    jaylee.name "Because he's my brother?"
    pc "No one going to look out for you better than he is."
    jaylee.name "Wow. Didn't expect a sympathetic response."
    jump jaylee_talk_end

label jaylee_talk_jay_preg_11:
    $ jaylee.dict["jaylee_talk_preg_chain"] += 1
    jaylee.name "World isn't how it used to be. Can't trust anyone."
    pc "I know."
    jaylee.name "So me and [ashon.nname] look out for each other."
    pc "That's good."
    jaylee.name "..."
    jump jaylee_talk_end

label jaylee_talk_jay_preg_12:
    $ jaylee.dict["jaylee_talk_preg_chain"] += 1
    pc "[ashon.name] make you happy?"
    jaylee.name "Makes me feel safe."
    pc "He make you feel \"happy\"?"
    jaylee.name "If you wanna know that, go find out."
    pc "Can't be having fun with my friends guy."
    jump jaylee_talk_end

label jaylee_talk_jay_preg_13:
    $ jaylee.dict["jaylee_talk_preg_chain"] += 1
    $ add_to_list(jaylee.conversation_topics, "ashon_sex_offer_pc")
    jaylee.name "I don't mind if you... Do something with [ashon.nname]."
    pc "No?"
    jaylee.name "He probably likes you as well."
    pc "How do you know? Spoke about me?"
    jaylee.name "I like you so he probably does too."
    jump jaylee_talk_end

label jaylee_talk_jay_preg_14:
    $ jaylee.dict["jaylee_talk_preg_chain"] += 1
    jaylee.name "I could invite [ashon.nname] to spend a night with us."
    pc "Oh yeah? Have him knock me up as well?"
    if player.has_perk(perk_preg_want):
        pc "Actually doesn't sound too bad."
    else:
        pc "Actually doesn't sound too bad. The spend night part that is. Not knocking me up."
    jump jaylee_talk_end





label jaylee_talk_ask_mags_intro:
    $ add_to_list(jaylee.conversation_topics, "mags_ask")
    pc "So I get the old jewellery and stuff, but what do you buy the shitty mags for?"
    jaylee.name "You don't know?"
    pc "Wouldn't ask if I did."
    jaylee.name "I cut them up and put them together as new magazines."
    pc "Oh, makes sense."
    jump jaylee_talk_end

label jaylee_talk_ask_mags_porn:
    $ add_to_list(jaylee.conversation_topics, "mags_porn")
    pc "But how does that work? Mixing all those different articles from different magazines is going to make for a pretty shit read."
    jaylee.name "I don't give a shit about the articles. I cut out the pictures and make mags for people to wank over."
    pc "Ah... What? Wank over?"
    jaylee.name "Yeah. Don't matter the content of a magazine, almost all of em have pictures of near naked girls. So I make a porn mag out of it all and sell em."
    pc "Okay then..."
    jump jaylee_talk_end

label jaylee_talk_ask_mags_felix:
    $ add_to_list(jaylee.conversation_topics, "mags_felix")
    pc "So, [jaylee.name], the big time porn baron."
    jaylee.name "Hah! I wish."
    pc "You know I know someone who takes photos. Can probably get you some new material."
    jaylee.name "Oh really? Would love some new material. What kinda stuff?"
    pc "Well he has his own camera setup and studio at the school. So pretty much anything I suppose."
    jump jaylee_talk_end

label jaylee_talk_ask_mags_felix_photos:
    $ add_to_list(jaylee.conversation_topics, "mags_felix_photos")
    jaylee.name "Hold on. Your friend \"has his own cameras and studio\"?"
    pc "Yeah."
    jaylee.name "He taken photos of you?"
    pc "Yeah we did some stuff to promote the school. He asked me to model for him doing school stuff."
    jaylee.name "Oh?"
    jump jaylee_talk_end

label jaylee_talk_ask_mags_felix_photos_sexy:
    $ add_to_list(jaylee.conversation_topics, "photos_sexy")
    jaylee.name "So..."
    pc "Hmmm?"
    jaylee.name "Your photo friend ever taken pics of you that are naughty?"
    pc "Oh? Interested in having some done yourself?"
    jaylee.name "Fuck no. I wanna see yours. Naked [name] under my pillow at night..."
    pc "Hah! Fucking hell you damn pervert."
    jaylee.name "Naked you would be better. I would..."
    pc "Yeah yeah."
    jump jaylee_talk_end

label jaylee_talk_ask_mags_felix_photos_sexy_tell:
    $ add_to_list(jaylee.conversation_topics, "photos_sexy_told")
    jaylee.name "You didn't answer. Any nudie photos of you I can have?"
    if "vsex" in school_photo_quest.list or "asex" in school_photo_quest.list:
        pc "Yeah, got pics of me fucking. Pretty hardcore stuff so would be good for your magazines."
        jaylee.name "Fuck the magazines. I want to keep those ones."
    elif "errotic" in school_photo_quest.list:
        pc "Yeah, got some pretty naughty ones where I show off everything so would be good for your magazines."
        jaylee.name "Fuck the magazines. I want to keep those ones."
    elif "nude" in school_photo_quest.list:
        pc "Yeah, we did some nude shoots so would probably be good for your magazines."
        jaylee.name "Fuck the magazines. I want to keep those ones."
    elif "topless" in school_photo_quest.list:
        pc "Yeah, some of the photos I had my tits out in them. Not super naughty but perverts these days would love them in your mags I guess."
        jaylee.name "I don't care about the mags, I want to have them to keep me company."
    elif "tasteful" in school_photo_quest.list:
        pc "Eh? Sort of? I did some nude shoots but you can't see anything in the photos. My bits are all covered."
        jaylee.name "Damn girl. Gonna drive me wild with something like that."
        pc "You? Thought you wanted for your porn mags."
        jaylee.name "Fuck no. I want them for myself."
    else:
        pc "Not really anything too exciting. I mean some of them are kinda naughty or whatever. But all clothes on and somewhat clean."
        jaylee.name "You don't sound convinced."
        pc "Well, not like we don't know what people are going to do with the pics. So played into that a bit."
        jaylee.name "Ohh. I wanna do the same."
    pc "Damn pervert."
    jump jaylee_talk_end

label jaylee_talk_ask_mags_soccerboys:
    $ add_to_list(jaylee.conversation_topics, "mags_soccerboys")
    pc "I have some boys I hang out with that would probably kill for some of your mags."
    jaylee.name "They don't need to kill for 'em, just pay me and they can have 'em."
    pc "Yeah, not sure I would get them coming way out here even for the mags."
    jaylee.name "No need. You buy them from me and sell to your friends. Put a huge markup on them if you want."
    pc "Hmmm... Good idea..."
    jump jaylee_talk_end





label jaylee_talk_sleep_first_offer:
    jaylee.name "Come to bed and stay the night here instead of heading home."
    pc "Err. You okay with that?"
    hide jaylee
    show jaylee_pose_bed
    with dissolve
    jaylee.name "Cutie like you keeping me warm. What could be better?"
    pc "I'm going to end up molested aren't I?"
    jaylee.name "I'll do everything in my power to make sure you are thoroughly abused. ♥"
    pc "Right..."
    menu:
        "Get into bed" if player.check_sex_agree(2):
            jump jaylee_talk_sleep_join
        "Another time":
            pc "Think I'll say goodnight and head off. Thanks though."
            jaylee.name "No worries. Be safe."
            hide jaylee_pose_bed with dissolve
            jump travel

label jaylee_talk_sleep_offer:
    hide jaylee
    show jaylee_pose_bed
    with dissolve
    jaylee.name "Wanna join me? ♥"
    if "slept_together" in jaylee.conversation_topics:
        menu:
            "Get into bed":
                jump jaylee_talk_sleep_join
            "Another time":
                pc "Not tonight, sorry."
                jaylee.name "No worries. Be safe out there."
                hide jaylee_pose_bed with dissolve
                jump travel
    else:
        menu:
            "Get into bed" if player.check_sex_agree(2):
                jump jaylee_sex_bed_firsttime_start
            "Another time":
                pc "Think I'll say goodnight and head off. Thanks though."
                jaylee.name "No worries. Be safe."
                hide jaylee_pose_bed with dissolve
                jump travel


label jaylee_talk_sleep_join:
    $ add_to_list(jaylee.conversation_topics, "slept_together")
    pc "Sure."
    jump jaylee_sex_bed_start





label shower_event_jaylee:
    if not "showered_together" in jaylee.conversation_topics:
        jump shower_event_jaylee_first

    call shower_scene_start from _call_shower_scene_start_4
    jaylee.name "Hey sweetie."
    "Mini scene where you help each other wash. No art for this yet."
    $ player.shower()
    call shower_scene_end from _call_shower_scene_end_4
    jump travel

label shower_event_jaylee_first:
    show jaylee nude at right1 with dissolve
    jaylee.name "Oh? Come to wash my back have you?"
    pc "Err."
    jaylee.name "Don't be shy. Come on, I'll wash you too."
    if player.check_sex_agree(2):
        menu:
            "Shower with [jaylee.name]":
                jump shower_event_jaylee_agree
            "Sorry, no":
                jump shower_event_jaylee_reject
    else:
        jump shower_event_jaylee_reject

label shower_event_jaylee_agree:
    $ add_to_list(jaylee.conversation_topics, "showered_together")
    call shower_scene_start from _call_shower_scene_start_5
    "Mini scene where you help each other wash. No art for this yet."
    $ player.shower()
    call shower_scene_end from _call_shower_scene_end_5
    jump travel

label shower_event_jaylee_reject:
    $ player.face_worried()
    pc "Err, no thanks..."
    jaylee.name "Another time then."
    pc "..."
    jaylee.name "Well if you aren't joining, at least give me some privacy."
    pc "Ah, right..."
    hide jaylee
    $ walk(loc_junk_trailer)
    pc "..."
    jump travel





label jaylee_sex_bed_firsttime_start:
    $ add_to_list(jaylee.conversation_topics, "slept_together")
    $ pc_set_temp_outfit()
    jaylee.name "Plenty of room. Come here."
    $ renpy.scene()
    show jaylee_kiss hair
    with dissolve
    pc "Mmmff."
    jaylee.name "Mmmm. I wanted this since you first dragged your ass over to the junkyard."
    pc "Dirty scavver girl had her eyes on me from the start."
    jaylee.name "Everyone did. But now you are in my bed."
    $ pc_strip_upper(temp=True)
    pc "Mmmm."
    pc "And what you going to do now you got me in your bed?"
    show jaylee_kiss jaylee_open
    jaylee.name "Do what I've wanted all along."
    $ pc_strip_lower(temp=True)
    jaylee.name "Gonna kiss you all over and suck on your tits."
    jaylee.name "Lick your pussy and stick my tongue up your arse."
    pc "You really have a thing for my arse don't you?"
    jaylee.name "Mostly just a thing for you."
    hide jaylee_kiss
    show jaylee_ontop
    with dissolve
    "[jaylee.name] pushes me down onto the bed and climbs on top of me, rubbing herself against me."
    "She humps me, rubbing herself against my wet pussy while groping my [rlist.name_breasts]."
    pc "You are pretty eager."
    jaylee.name "Been trying to get you in bed for ages. I'm gonna make the most of this."
    pc "Ohh?"
    "[jaylee.name] keeps humping and groping me. I am not too used to being with a girl so I just lay back and let her do as she wishes."
    "She seems to have some idea of what to do, so I go along with it. It feels nice being with someone who is more interested in giving me pleasure than using me for their own."
    "It's not long before I can feel it building up inside me and..."
    $ player.sex_cum(jaylee)
    pc "Haaaaaaa fuck!"
    pc "Yessss!!!"
    "[jaylee.name] doesn't even slow down as she keeps humping me while feeling up my [rlist.name_breasts]."
    jaylee.name "Mmm, like that did you?"
    pc "Mmmm."
    "Her hands are all over me and all I can do is lay there and enjoy what she is making me feel. It is the first time having sex with her and she is determined to make good on it."
    $ player.sex_cum(jaylee)
    "I cum so many more times that night that I lose count and eventually just drift off to sleep..."
    jump bed_sleep_loop

label jaylee_sex_bed_start:
    $ add_to_list(jaylee.conversation_topics, "slept_together")
    $ pc_set_temp_outfit()
    jaylee.name "Bring your sexy arse over here."
    $ renpy.scene()
    show jaylee_kiss hair
    with dissolve
    pc "Mwah."
    $ pc_strip_upper(temp=True)
    jaylee.name "Mmmm."
    show jaylee_kiss jaylee_open
    jaylee.name "You sexy little bean."
    $ pc_strip_lower(temp=True)
    jaylee.name "Gonna kiss you all over and suck on your tits."
    jaylee.name "Lick your pussy and stick my tongue up your arse."
    pc "You really have a thing for my arse don't you?"
    jaylee.name "Mostly just a thing for you."
    hide jaylee_kiss
    show jaylee_ontop
    with dissolve
    "[jaylee.name] pushes me down onto the bed and climbs on top of me, rubbing herself against me."
    "She humps me, rubbing herself against my wet pussy while groping my [rlist.name_breasts]."
    pc "You are pretty eager."
    jaylee.name "Been thinking of this all day."
    pc "Ohh?"
    "[jaylee.name] keeps humping and groping me. I am not too used to being with a girl so I just lay back and let her do as she wishes."
    "She seems to have some idea of what to do, so I go along with it. It feels nice being with someone who is more interested in giving me pleasure than using me for their own."
    "It's not long before I can feel it building up inside me and..."
    $ player.sex_cum(jaylee)
    pc "Haaaaaaa fuck!"
    pc "Yessss!!!"
    "[jaylee.name] doesn't even slow down as she keeps humping me while feeling up my [rlist.name_breasts]."
    jaylee.name "Mmm, like that did you?"
    pc "Mmmm."
    "Her hands are all over me and all I can do is lay there and enjoy what she is making me feel."
    $ player.sex_cum(jaylee)
    "I cum multiple more times that night that I lose count and eventually just drift off to sleep..."
    jump bed_sleep_loop

label bed_wake_jaylee_sex_picker:
    jump expression WeightedChoice([
    ("bed_wake_jaylee_facesit", 100),
    ("bed_wake_jaylee_asslick", 100),
    ])

label bed_wake_jaylee_facesit:
    show jaylee_facesit
    $ pc_strip(temp=True)
    hide screen blackout with hpunch
    "Sammy wakes to Jaylle sitting on her face. Since you have already had sex with her at this point it is not entirely unwelcome. Just a suprise."
    "Sammy will go along with it and be ridden until Jaylee gets her fun."
    hide jaylee_facesit with dissolve
    $ pc_dress_slow("home")
    jump travel


label bed_wake_jaylee_asslick:
    $ pc_strip(temp=True)
    show jaylee_asslick
    $ player.face_shock()
    hide screen blackout with hpunch
    pc "Aiee!"
    if not "licked_ass" in jaylee.conversation_topics:
        show jaylee_asslick happy with dissolve
        jaylee.name "Finally first time getting your ass."
        pc "Pervert!"
        jaylee.name "Shush!"
        show jaylee_asslick tongue with dissolve
        show jaylee_asslick lick with dissolve
    jaylee.name "Mmmmm."
    $ player.face_sleep()
    $ player.face_shy()
    pc "Ooooh..."
    "I am not even sure what to do so I just arch my back giving [jaylee.name] better access and let her do as she pleases."
    "She spreads my ass cheeks and really goes to town licking my arsehole and even makes attempts to penetrate me with her tongue."
    if not "licked_ass" in jaylee.conversation_topics:
        "This is the first time she has ever done it to me, and it is not unplesant. In fact I find myself quite enjoying what she is doing."
        "And the fact she seems to have wanted to do this for a long time makes me feel much more comfortable with it."
    pc "Mmmmm fuck!"
    "She keeps licking me and trying to tongue fuck my arse while playing with my clit. It is really getting me off and I can feel myself cumming from it."
    pc "Haaaaa fuck keep going!"
    pc "Nnnnnggg."
    $ player.sex_cum(jaylee)
    pc "Ahhhhh fuck yes!"
    pc "Haaaaaaa..."
    show jaylee_asslick happy with dissolve
    if not "licked_ass" in jaylee.conversation_topics:
        jaylee.name "Enjoy your first ass licking?"
        pc "Phew."
        jaylee.name "And you call me the pervert."
        pc "You are."
        $ add_to_list(jaylee.conversation_topics, "licked_ass")
    else:
        jaylee.name "Nice way to wake in the morning."
        pc "Mmm, could get used to this."
    hide jaylee_asslick with dissolve
    $ pc_dress_slow("home")
    jump travel





label jaylee_shop_sell:
    show jaylee at right1 with dissolve
    jaylee.name "What you got for me sweetie?"
    call screen inventory_junk_choice(jaylee.inv, choices=[item_scrap_jewel, item_scrap_gem, item_scrap_mag])
    jaylee.name "Come back if you pick up anything else."
    hide jaylee with dissolve
    jump travel

label jaylee_shop_buy:
    show jaylee at right1 with dissolve
    jaylee.name "Come to see what fun I'm offering?"
    call screen inventory_itemshop_screen(jaylee.inv, 30)
    jaylee.name "See you round cutie."
    hide jaylee with dissolve
    jump travel




label jaylee_talk_end:
    $ relax(20, jaylee)
    $ dialouge = renpy.random.choice([
    "I hang out talking and joking about random stuff.",
    "I hang out for a while chatting and joking around about random topics.",
    "We hang out chatting and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    if loc_cur == loc_junk_trailer:
        if not jaylee_here():
            if t.hour == 23:
                jaylee.name "I'm gonna jump in the shower before it gets too late. Join me if you want."
            else:
                jaylee.name "I'm heading out now [name]. Come later if you want to hang out."
        elif t.hour in irange(1,6):
            jaylee.name "It's late [name]. I'm gonna lay down for a bit."
            if not "sleep_together_offer" in jaylee.conversation_topics:
                $ add_to_list(jaylee.conversation_topics, "sleep_together_offer")
                jump jaylee_talk_sleep_first_offer
            else:
                jump jaylee_talk_sleep_offer

    elif loc_cur == loc_junk_2:
        if not jaylee_here():
            if t.hour in dark:
                jaylee.name "I'm gonna head inside now [name]"
            else:
                jaylee.name "I'm gonna get to work [name]. See ya round."
    hide jaylee with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
