



label shower_masturbate:
    call shower_scene_start from _call_shower_scene_start_3
    $ renpy.show(renpy.random.choice(["sb_mast_stand", "sb_againstwall2 mast worried closed tounge"]))
    with dissolve

    $ player.eye = 2
    $ player.mouth = 1
    $ player.brow = 3

    pc "Mmmmm..."

    call masturbate_fantasy_picker from _call_masturbate_fantasy_picker
    call expression rand_choice from _call_expression_9
    pc "Haaaaaa..."
    $ player.sex_cum(nosex, "self")
    $ player.face_orgasm()
    pc "Ahhh yes yes!"
    pc "..."
    $ player.face_shame()
    pc "Fuuuu..."
    $ renpy.scene()
    with dissolve
    call shower_scene_wash from _call_shower_scene_wash_3
    call shower_scene_end from _call_shower_scene_end_3
    jump travel

label bedroom_masturbate:
    if not c.nude:
        $ pc_striptease()
    pause 0.5
    show sb_onback mast ooh worried at right5 with dissolve
    $ player.eye = 2
    $ player.mouth = 1
    $ player.brow = 3

    pc "Mmmmm..."

    call masturbate_fantasy_picker from _call_masturbate_fantasy_picker_2
    call expression rand_choice from _call_expression_10
    pc "Haaaaaa..."
    show sb_onback look_closed ag
    $ player.sex_cum(nosex, "self")
    $ player.face_orgasm()
    pc "Ahhh yes yes!"
    pc "..."
    show sb_onback look_up neutral
    $ player.face_shame()
    pc "Fuuuu..."
    $ renpy.scene()
    with dissolve
    $ pc_dress_slow()
    pause 0.5
    $ player.face_normal()
    jump travel

label bedroom_wake_masturbate:
    show sb_onback mast ooh worried at right5 with dissolve

    $ pc_strip()
    $ player.eye = 2
    $ player.mouth = 1
    $ player.brow = 3
    show screen blackout(25) with dissolve
    pc "Mmmmm..."
    hide screen blackout with dissolve
    $ npc_race_picker()
    call masturbate_fantasy_picker from _call_masturbate_fantasy_picker_3
    call expression rand_choice from _call_expression_11
    jump home_masturbate_end

label masturbate_fantasy_picker:
    $ temp_var_1 = npc_race
    $ rand_choice = WeightedChoice([
    
    
    

    

    
    ("home_masturbate_virgin1", If (player.vvirgin,1,0)),
    ("home_masturbate_imagine1", 1),

    
    
    
    ("home_masturbate_newbody_1", If (t.day < 15 or player.sex < 3,100,0)),

    
    
    

    
    ("home_masturbate_malevirgin_1", If (player.sex < 3 and player.has_perk(perk_male),100,0)),
    ("home_masturbate_malevirgin_2", If (player.sex < 3 and player.has_perk(perk_male),100,0)),
    ("home_masturbate_malevirgin_3", If (player.sex < 3 and player.has_perk(perk_male),100,0)),

    
    ("home_masturbate_pregwant_1", If (player.has_perk(perk_preg_want) and not player.preg_knows,100,0)),

    
    ("home_masturbate_slut_1", If (player.has_perk([perk_slut, perk_sucu]),100,0)),
    ("home_masturbate_slut_2", If (player.has_perk([perk_slut, perk_sucu]),100,0)),
    ("home_masturbate_slut_3", If (player.has_perk([perk_slut, perk_sucu]),100,0)),
    
    
    

    
    ("home_masturbate_simon_sex", If (simon.vsex, 100,0)), 
    ("home_masturbate_simon_blow", If (simon.hsex or simon.osex, 100,0)), 
    ("home_masturbate_simon_naughty", If (simon.naughty, 100,0)), 
    ("home_masturbate_bob_sex", If (bob.vsex, 100,0)), 
    ("home_masturbate_bob_blow", If (bob.hsex or bob.osex, 100,0)), 

    
    ("home_masturbate_haven_peep", If (havenpeeper.vsex, 100,0)), 
    ("home_masturbate_haven_viktor", If (havenvik.hsex or havenvik.osex, 100,0)), 
    ("home_masturbate_haven_gateguard", If (havengateguard.vsex, 100,0)), 
    ("home_masturbate_haven_gangbang", If ("gangbanged" in main_quest_05.list, 100,0)), 
    ("home_masturbate_haven_shower", If (main_quest_05.active == 2, 100,0)), 
    ("home_masturbate_haven_fantasy", If (main_quest_05.active == 2, 100,0)), 

    
    
    

    
    ("home_masturbate_dani_strapon", If ("strapon_sex" in dani.dict and dani.dict["strapon_sex"], 100,0)), 
    ("home_masturbate_dani_pubsex_1", If ("talk_whoringpub_chain" in dani.dict and dani.dict["talk_whoringpub_chain"], 100,0)), 
    ("home_masturbate_dani_pubsex_2", If ("talk_whoringpub_chain" in dani.dict and dani.dict["talk_whoringpub_chain"], 100,0)), 
    ("home_masturbate_dani_pub_gloryhole_1", If ("talk_gloryholepub_chain" in dani.dict and dani.dict["talk_gloryholepub_chain"], 100,0)),
    ("home_masturbate_dani_pub_gloryhole_2", If ("talk_gloryholepub_chain" in dani.dict and dani.dict["talk_gloryholepub_chain"], 100,0)),
    ("home_masturbate_dani_kiss", If (dani.sex_les, 100,0)),  
    ("home_masturbate_dani_scissor", If (dani.sex_les, 100,0)),  

    
    ("home_masturbate_robin_gangbang", If (robin.isslut, 100,0)),  
    ("home_masturbate_robin_doubleblow", If (robin.isslut, 100,0)),  
    ("home_masturbate_robin_cumlick", If ("park_bitch_intro" in robin.list, 100,0)),  
    ("home_masturbate_robin_oskar_1", If (oskar in robin.sex_who_class, 100,0)),  
    ("home_masturbate_robin_oskar_2", If (oskar in robin.sex_who_class, 100,0)),  
    ("home_masturbate_robin_oskar_3", If (oskar in robin.sex_who_class, 100,0)),  
    ("home_masturbate_robin_motel", If ("pc_knows_likes_watching" in robin.list and robin.dict["robin_talk_pub_chain"] >= 15, 100,0)),  
    
    
    

    
    ("home_masturbate_soccer_nate_mast", If (nate.naughty, 100,0)), 
    ("home_masturbate_soccer_train", If (all((nate.sex, drake.sex, dan.sex)), 100,0)), 
    ("home_masturbate_soccer_field", If (drake.naughty, 100,0)), 

    
    ("home_masturbate_bully_shane", If (shane.sex and player.isbroken, 100,0)), 

    
    
    
    
    ("home_masturbate_pub_vsex", If (pubpatron.vsex or pubpatron.asex, 100,0)), 
    ("home_masturbate_pub_fantasy", If (pub_waitress.timesworked, 100,0)), 
    ("home_masturbate_pub_fantasy_stand", If (pub_waitress.timesworked > 10, 100,0)), 
    ("home_masturbate_pub_fantasy_trixie1", If (pub_waitress.timesworked > 10, 100,0)), 
    ("home_masturbate_pub_fantasy_trixie2", If (pub_waitress.timesworked > 10, 100,0)), 

    
    ("home_masturbate_gloryhole_blow", If (ghman.hsex or ghman.osex, 100,0)), 
    ("home_masturbate_gloryhole_vsex", If (ghman.sex, 100,0)), 

    
    ("home_masturbate_bitching_rachel", If ("can_bitch" in rachel.list, 100,0)), 
    ("home_masturbate_bitching_robin", If ("can_bitch" in robin.list, 100,0)), 


    
    ("home_masturbate_vip_dance_rachel", If (log.interactive("quest_dancevip_04"), 100,0)), 
    ("home_masturbate_vip_dance_dani", If (log.interactive("quest_dancevip_04") and not dani.hate or dani.dead, 100,0)), 
    ("home_masturbate_vip_dance_svet", If (log.interactive("quest_dancevip_04"), 100,0)), 
    ("home_masturbate_vip_dance_anabel", If (log.interactive("quest_dancevip_04") and not anabel.hate, 100,0)), 

    ("home_masturbate_vip_dance_rachel_sex", If (partyman in rachel.sex_who_class, 100,0)), 
    ("home_masturbate_vip_dance_dani_sex", If (partyman in dani.sex_who_class and not dani.hate or dani.dead, 100,0)), 
    ("home_masturbate_vip_dance_svet_sex", If (partyman in svet.sex_who_class, 100,0)), 
    ("home_masturbate_vip_dance_anabel_sex", If (partyman in anabel.sex_who_class and not anabel.hate, 100,0)), 

    ("home_masturbate_vip_dance_all_sex", If (partyman in anabel.sex_who_class and not (anabel.hate or dani.hate), 100,0)), 
    ])
    $ npc_race_picker(temp_var_1)
    return





label home_masturbate_virgin1:
    pc "Oh fuck. How will it feel to have a big cock slip inside me?"
    pc "Mmmm wonder when I will find out? Who will be lucky enough to fill me for the first time?"
    pc "Will you make sweet love to me or fuck me like a whore?"
    return

label home_masturbate_imagine1:
    pc "Ah fuck so nice. Haaaa!"
    pc "Who is going to take me and make me feel good?"
    return





label home_masturbate_newbody_1:
    show sb_assup as dream at rightover with dissolve
    pcm "This ass is brand new, who wants to try it out?"
    show sb_assup mast back as dream with dissolve
    pcm "Oh? Someone came for some fun?"
    show sb_assup poke ah as dream with dissolve
    pcm "Mmmm, I can feel you poking me."
    show sb_assup sex ag wink as dream with dissolve
    pcm "Oh yes! Fuck me!"
    pcm "Give this brand new body a good fucking!"
    hide dream with dissolve
    return






label home_masturbate_malevirgin_1:
    show sb_doggy2 shock as dream at rightover with dissolve
    pcm "I don't really know how to do it as a girl. Bend over like this?"
    show sb_doggy2 pokevag happy wink as dream with dissolve
    pcm "Ah fuck, you are poking me!"
    pcm "Never thought this could feel so nice."
    show sb_doggy2 insidevag head_forward as dream with dissolve
    pcm "Ah fuck yes. Give it to me as a girl!"
    pcm "Yes, I never knew it could feel like this!"
    hide dream with dissolve
    return

label home_masturbate_malevirgin_2:
    show sb_doggy1 shock worried as dream at rightover with dissolve
    pcm "First time as a girl so you are going to have to show me how it's done."
    show sb_doggy1 poke normal ah as dream with dissolve
    pcm "Looking to put something inside me are you?"
    pcm "Make me know what it feels like to be a woman?"
    show sb_doggy1 vag ag closed as dream with dissolve
    pcm "Ah fuck yes. Fuck me like the girl I now am!"
    pcm "Yes, I never knew it could feel like this!"
    hide dream with dissolve
    return

label home_masturbate_malevirgin_3:
    show sb_pose_showbreasts down as dream at rightover with dissolve
    pcm "Not used to having breasts. They kinda make me feel nice when I walk."
    show sb_pose_showbreasts forward worried as dream with dissolve
    pcm "Anyone want to play with them? Maybe suck on them and let me know how it feels?"
    show sb_pose_showbreasts tounge down as dream with dissolve
    pcm "Oh it would feel so nice to have someone touching them and licking my nipples."
    hide dream with dissolve
    return


label home_masturbate_pregwant_1:
    show sb_matingpress as dream at rightover with dissolve
    pcm "This is supposed to be the best position for getting knocked up!"
    show sb_matingpress poke down as dream with dissolve
    pcm "Yes! I am spreading myself for you. Do a good job and leave something inside me."
    show sb_matingpress vag happy as dream with dissolve
    pcm "Oh fuck yes. Put it in deep. Make sure to cum in me!"
    pcm "Fill me up and leave me leaking."
    hide dream with dissolve
    return


label home_masturbate_slut_1:
    show sb_dpstand happy bpoke vag as dream at rightover with dissolve
    pcm "Ah fuck, stuck between two men fucking me!"
    pcm "Don't worry, I have two holes. You can share."
    show sb_dpstand poke back as dream with dissolve
    show sb_dpstand bvag ag as dream with dissolve
    pcm "Ah fuck, you are both going to take turns fucking my pussy?"
    pcm "Leave me leaking with both your cum?"
    pcm "Ah yes, do it!"
    hide dream with dissolve
    return

label home_masturbate_slut_2:
    show sb_blowjob poke down as dream at rightover with dissolve
    show sb_blowjob suck as dream at rightover with dissolve
    pcm "Give me all you cocks you perverts!"
    pcm "I will suck them all and youcan cum all over me."
    show sb_blowjob man_left up as dream with dissolve
    pcm "Yes, give me them. I'll make you all feel good."
    show sb_blowjob man_right as dream with dissolve
    pcm "Yes, like that. Keep coming them cumming all over me."
    pcm "Cover my face completly in it."
    hide dream with dissolve
    return

label home_masturbate_slut_3:
    show sb_dpbed vag bpoke as dream at rightover with dissolve
    pcm "It's a good job I have two holes for you guys to fuck!"
    pcm "Mmm, put it in my ass."
    show sb_dpbed banal as dream with dissolve
    pcm "Ah yes, like that. Fill me up from both sides."
    hide dream with dissolve
    return




label home_masturbate_simon_sex:
    $ npc_race_picker(simon)
    show sb_againstwall2 insidevag conc ag wink as dream at rightover with dissolve
    pc "Ah, fuck me in this dirty alleyway! Mmmmm such a slut for letting you fuck me in such a place."
    if simon.vvirgin:
        pc "Taking my virginity in this place. Ohh so dirty. Take my first time like a whore in the street."
    if simon.preg_current and player.preg_knows:
        pc "Mmmm. Fuck another baby in me! Cum inside and let me feel you putting it in there!"
    pc "Fuck yes. Against the wall. Take me like a highway whore!"
    hide sb_againstwall2 as dream with dissolve
    return

label home_masturbate_simon_blow:
    $ npc_race_picker(simon)
    show sb_blowjob suck closed conc as dream at rightover with dissolve
    pc "Mmmm. Sucking you off in an alleyway. So dirty!"
    pc "On my knees in this place. Make me feel like a dirty whore while doing this to me."
    pc "Give me the info I came for. Mmmmmm."
    hide sb_blowjob as dream with dissolve
    return

label home_masturbate_simon_naughty:
    $ npc_race_picker(simon)
    show sb_pose_lookback as dream at rightover with dissolve
    pc "Shitty guy making me strip for you in the alleyway."
    pc "Oh what are you doing there? Getting excited from looking at me?"
    pc "Mmmmm touch me and do what you want to me. I can feel you poking..."
    hide sb_pose_lookback as dream with dissolve
    return

label home_masturbate_bob_sex:
    $ npc_race_picker(bob)
    show sb_againstwall3 smile wink sex as dream at rightover with dissolve
    pcm "Ah, I was only supposed to get dirty photos with you, but I let you fuck me."
    if bob.vvirgin:
        pcm "Paid by someone else to have fun and I gave you my virginity."
    if bob.preg_current and player.preg_knows:
        pc "Even let you knock me up!"
    pc "Fuck yes. Against the wall. Take me like a highway whore!"
    hide sb_againstwall3 as dream with dissolve
    return

label home_masturbate_bob_blow:
    $ npc_race_picker(bob)
    show sb_blowjob suck closed conc as dream at rightover with dissolve
    pcm "Some pervert paid me to suck you off. But you don't know that do you?"
    pcm "Just enjoy my mouth around your cock!"
    hide sb_blowjob as dream with dissolve
    return





label home_masturbate_haven_peep:
    show haven_peeping poke_in enjoy shorts_down as dream at right1 with dissolve
    pc "Ah fuck. Caught looking at all the naked people in the showers and now you are taking advantage of me."
    pc "Ah fuck yes, take me while I look at all the naked bodies washing up. All soapy and shiny"
    pc "Grab my tits while you fuck me! Ah fuck yes!"
    hide haven_peeping as dream with dissolve
    return

label home_masturbate_haven_viktor:
    show expression renpy.random.choice(["haven_blow ballsuck", "haven_blow 1h", "haven_blow 2h", "haven_blow ballrub"]) as dream at rightover with dissolve
    pc "Mmmm. I need two beers. How about I suck you off for them?"
    pc "Oh tasty. Maybe I should drink more of this instead of your shitty moonshine."
    hide blow as dream with dissolve
    return

label home_masturbate_haven_gateguard:
    show haven_onback ag sex up as dream at right with dissolve
    pc "Ah fuck yes. Spread my legs and let me feel that huge cock inside me!"
    pc "These perverts are probably watching but I don't care. Fuck me!"
    if havengateguard.vvirgin:
        pc "Fuck me for the first time. Let me feel what it's like to be penetrated!"
    if havengateguard.preg and player.has_perk(perk_preg_want):
        pc "Give me your baby. I will carry it for you."
    hide haven_onback as dream with dissolve
    return

label home_masturbate_haven_gangbang:
    show expression renpy.random.choice(["haven_gangbang manblow blow", "haven_spitroast"]) as dream at right with dissolve
    pc "Ah fuck. So many of you waiting to take turns fucking me? Don't worry, I will take you all."
    pc "Make sure to keep count. I want to know how many of you shits had fun with me."
    pc "Ah fuck me all night. I will stay here taking all of your cocks!"
    hide haven_gangbang as dream
    hide haven_spitroast as dream
    with dissolve
    return

label home_masturbate_haven_shower:
    show expression "haven_corner " + renpy.random.choice(["man_sex", "man_poke", "man_grind"]) + " tit happy" as dream at right with dissolve
    pc "Mmm, want to help wash me? Come here and clean every part of me."
    pc "Between my legs needs the most attention. Let me feel your cock giving it a good rubbing."
    hide haven_corner as dream with dissolve
    return

label home_masturbate_haven_fantasy:
    show expression renpy.random.choice(["haven_bentover smile noshorts topoff inside", "haven_presentass inside lookdown"]) as dream at right with dissolve
    pc "I've been so bad and need to be punished. Bend me over and give me a spanking."
    pc "Oh, like what you see? Such an innocent girl bent over for you."
    hide haven_bentover as dream
    hide haven_presentass as dream
    with dissolve
    return





label home_masturbate_dani_strapon:
    show sb_bentover head_up back worried oh dani_cum as dream at rightover with dissolve
    pcm "Ah [dani.nname] you pervert. Where did you get this giant cock from?"
    show sb_bentover dani_poke as dream with dissolve
    pcm "Doesn't matter. Fuck me with it!"
    show sb_bentover head_up ooh dani_sex as dream with dissolve
    pcm "Oh fuck yes!"
    hide dream with dissolve
    return

label home_masturbate_dani_pubsex_1:
    show pub_dani_spitroast as dream at rightover with dissolve
    pcm "Ah [dani.nname] you dirty slut. Fucking guys in the pub?"
    show pub_dani_spitroast man_behind as dream with dissolve
    pcm "Oh? Having someone else join you?"
    pcm "Mmm, let me watch you get fucked from both sides!"
    hide dream with dissolve
    return

label home_masturbate_dani_pubsex_2:
    show pub_dani_spitroast as dream at rightover with dissolve
    pcm "Ah [dani.nname] you dirty slut. Sneaking some guy off to such his cock?"
    show pub_dani_spitroast pc as dream with dissolve
    pcm "Want me to give you some help? We can make him blow together."
    pcm "Mmm, suck him off while I watch!"
    hide dream with dissolve
    return

label home_masturbate_dani_pub_gloryhole_1:
    show gh_blow_behind dani_lick as dream at rightover with dissolve
    pcm "Oh? Didn't know you would be in here you dirty slut!"
    show gh_blow_behind dani_suck as dream with dissolve
    pcm "Mmm, thats right. Suck him off and earn that money."
    pcm "Maybe next time I will help you get him off."
    hide dream with dissolve
    return

label home_masturbate_dani_pub_gloryhole_2:
    show gh_blow_behind suck as dream at rightover with dissolve
    pcm "Mmm, don't even know what you look like, but your cock is nice."
    show gh_blow_behind dani_hump as dream with dissolve
    pcm "Oh? You came to have some fun as well [dani.nname]?"
    pcm "I don't mind. Lets enjoy him together."
    show gh_blow_behind dani_poke as dream with dissolve
    pcm "Oh wow, you brought a friend to join us?"
    show gh_blow_behind dani_sex as dream with dissolve
    pcm "Mmmm, yes, take us both you dirty perverts!"
    hide dream with dissolve
    return

label home_masturbate_dani_kiss:
    show sb_laykiss underwear as dream at rightover with dissolve
    pcm "Mmmm, nice way to wake in the morning."
    pcm "Your tongue in my mouth and your tits pressed against me."
    pcm "Maybe we should do something more?"
    hide dream with dissolve
    return

label home_masturbate_dani_scissor:
    show sb_scissoring as dream at rightover with dissolve
    pcm "Fuck, never thought I would be doing this."
    pcm "All the guys want to fuck us, and we are here doing this."
    pcm "Keeping girls fun to the girls"
    hide dream with dissolve
    return





label home_masturbate_robin_gangbang:
    show robin_bimbo_gangbang as dream at rightover with dissolve
    pcm "Damn [robin.name], I turn my back on you for 30 seconds and you have this many dicks in you?"
    pcm "What am I going to do with you?"
    pcm "Such a dirty fucking slut!"
    hide dream with dissolve
    return

label home_masturbate_robin_doubleblow:
    show robin_doubleblow as dream at rightover with dissolve
    pcm "Wow, youare such a slut. So many men lining up for you to suck them off."
    pcm "Maybe I should help you out and suck some of them off as well?"
    pcm "Mmm, both of us being such dirty girls."
    hide dream with dissolve
    return

label home_masturbate_robin_cumlick:
    show robin_facesit mess as dream at rightover with dissolve
    pcm "I swear I didn't know they would all fuck you like that [robin.name]."
    pcm "Mmm, but let me clean you up anyway."
    pcm "Pour all those perverts cum into my mouth."
    hide dream with dissolve
    return

label home_masturbate_robin_oskar_1:
    $ npc_race_picker(oskar)
    show robin_prone as dream at rightover with dissolve
    pcm "Oh? Paying the rent again? Okay, I'll come back later."
    pcm "Or maybe I will watch. Maybe I can pay rent as well."
    pcm "He can fuck us both one after the other."
    hide dream with dissolve
    return

label home_masturbate_robin_oskar_2:
    $ npc_race_picker(oskar)
    show robin_onback as dream at rightover with dissolve
    pcm "Spreading your legs to pay off the rent?"
    pcm "Hmm, should I wait my turn and fuck him too?"
    pcm "He can fuck us both one after the other."
    hide dream with dissolve
    return

label home_masturbate_robin_oskar_3:
    $ npc_race_picker(oskar)
    show robin_againstdesk as dream at rightover with dissolve
    pcm "Oh? Didn't think I would see you bent over the desk when I came in here."
    pcm "Coming in here and stripping off for him. Letting him bend you over."
    pcm "Just for cheaper rent."
    hide dream with dissolve
    return

label home_masturbate_robin_motel:
    show robin_doggy as dream at rightover with dissolve
    pcm "Damn [robin.name]. Half the pub has taken you back to the motel at this point."
    pcm "Everyone knows you by name."
    pcm "How does it feel to walk in a room and know more than half the men there have bent you over?"
    hide dream with dissolve
    return




label home_masturbate_soccer_nate_mast:
    $ npc_race_picker(nate)
    show sb_againstwall2 ag wink mast grass as dream at rightover with dissolve
    pc "Ah [nate.name] you pervert. Want to watch me finger myself?"
    pc "Mmmm. Bet you want to do something more than just watch?"
    pc "Well?"
    hide sb_againstwall2 as dream with dissolve
    return

label home_masturbate_soccer_train:
    $ npc_race_picker(nate)
    show sb_againstwall2 insidevag ag wink mast grass as dream at rightover with dissolve
    pc "Ah fuck! Which one of you are fucking me?"
    pc "Haaa I don't care. Take turns and all of you fuck me!"
    pc "YES! YES!"
    hide sb_againstwall2 as dream with dissolve
    return

label home_masturbate_soccer_field:
    $ npc_race_picker(drake)
    show sb_doggy1 worried ah grass as dream at rightover with dissolve
    pc "Ah I fell over playing. Who is going to help me up?"
    show sb_doggy1 poke shock as dream with dissolve
    pc "Ahhh [drake.name]! That's not helping."
    show sb_doggy1 vag ag closed as dream with dissolve
    pc "YES! YES!"
    hide sb_doggy1 as dream with dissolve
    return





label home_masturbate_bully_shane:
    $ npc_race_picker(shane)
    show sb_againstwall3 worried wink grit sex tile as dream at rightover with dissolve
    pc "Why are you doing this to me [shane.name]?"
    pc "I didn't ask for this!"
    pc "Haaaaa fuuuuckkk!"
    hide sb_againstwall3 as dream with dissolve
    return





label home_masturbate_pub_vsex:
    show sb_againstwall3 wink poke tile as dream at rightover with dissolve
    pc "Mmmm. Take me in the toilets. I came in here just to clean but I can help you with something else."
    pc "Bend over for a tip? Ok, I like big tips."
    show sb_againstwall3 wink ag sex as dream with dissolve
    pc "Ooohhh I feel it. It is big..."
    hide sb_againstwall3 as dream with dissolve
    return

label home_masturbate_pub_fantasy_stand:
    show pub_stand mast as dream at rightover with dissolve
    pcm "Oh, getting your cock out just for me?"
    pcm "Mmm, wank it off while I watch."
    pcm "Cum on me and send me back to work you pervert!"
    hide pub_stand as dream with dissolve
    return

label home_masturbate_pub_fantasy:
    show pub_serve_lap hump rub as dream at rightover with dissolve
    pc "Ohhh I can join you but there are no seats so I'll just sit here."
    pc "Ah what is that? Something sneaking out of your trousers and between my legs."
    show pub_serve_lap prep as dream with dissolve
    show pub_serve_lap hump penis_in as dream with dissolve
    "Ohhh in public. Fuck me and fill me up in front of everyone!"
    hide pub_serve_lap as dream with dissolve
    return

label home_masturbate_pub_fantasy_trixie1:
    show trixie_pub_lapsit as dream at rightover with dissolve
    pcm "Ah [trixie.name] you slut. Sitting on a guy like that for tips?"
    pcm "I wonder where his tip is?"
    pcm "Have you let this pervert take you deep inside?"
    hide trixie_pub_lapsit as dream with dissolve
    return

label home_masturbate_pub_fantasy_trixie2:
    show trixie_pub_mast as dream at rightover with dissolve
    pcm "Ah [trixie.name] you slut. Not even hiding you are wanking off some drunk pervert?"
    pcm "Out here in the open for everyone to see."
    pcm "Mmm, how many guys have you made happy like this?"
    hide trixie_pub_mast as dream with dissolve
    return




label home_masturbate_gloryhole_blow:
    show gh_blow_close lick as dream at right with dissolve
    pcm "Mmm, sucking off some random guy who's face I can't even see."
    pcm "Let me make you feel good."
    show gh_blow_close suck as dream with dissolve
    pcm "Give me something warm in my mouth. Let it all out."
    pcm "Mmmm, give it to me!"
    hide gh_blow_close as dream with dissolve
    return

label home_masturbate_gloryhole_vsex:
    show gh_blow_behind sex_stand as dream at right with dissolve
    pcm "Mmm, don't even know who you are, but you have your dick in me."
    pcm "Don't worry, I'll do all the work."
    show gh_blow_behind sex_down as dream with dissolve
    pcm "Come on, let me feel you start throbbing."
    pcm "Mmmm, give it to me!"
    hide gh_blow_behind as dream with dissolve
    return





label home_masturbate_bitching_rachel:
    show rachel_bitching_1 as dream at rightover with dissolve
    pcm "Such a good bitch you are [rachel.name]. Let those mutts fuck you."
    pcm "You are a dirty pervert letting me send you off to get gang fucked by a bunch of weirdos."
    pcm "Let them fuck you silly!"
    hide dream with dissolve
    return

label home_masturbate_bitching_robin:
    show robin_bitching_1 as dream at rightover with dissolve
    pcm "Such a good bitch you are [robin.name]. Let those mutts fuck you."
    pcm "I already knew you were a dirty slut, going out and fucking guys on the street."
    pcm "But now you run around the park letting everyone take turns on you!"
    hide dream with dissolve
    return







label home_masturbate_vip_dance_rachel:
    $ add_to_list(rachel.list, "dream")
    show rachel_poledance_1 as dream at rightover with dissolve
    pcm "Ah [rachel.name]. You love it being naked in front of all these men dont you?"
    pcm "Of course you do. I wonder how many of them will fuck you in the back rooms tonight?"
    pcm "Quite a lot of them I am sure."
    hide dream with dissolve
    $ remove_from_list(rachel.list, "dream")
    return

label home_masturbate_vip_dance_anabel:
    $ add_to_list(anabel.list, "dream")
    show anabel_poledance_1 as dream at rightover with dissolve
    pcm "Ah [anabel.name]. Always complaining how much you hate this stuff."
    pcm "And now you are in a room full of horny men, dancing naked for them."
    pcm "How many of them want to drag you off and bend you over?."
    hide dream with dissolve
    $ remove_from_list(anabel.list, "dream")
    return

label home_masturbate_vip_dance_dani:
    $ add_to_list(dani.list, "dream")
    if numgen():
        show dani_poledance_1 as dream at rightover with dissolve
    else:
        show dani_poledance_2 as dream at rightover with dissolve
    pcm "Wow [dani.name]. Invite us all for your weird punters party and now you are stripping for them."
    pcm "Didn't expect you would be shaking your arse in a room full of horny men."
    pcm "I can see how much you enjoy it."
    hide dream with dissolve
    $ remove_from_list(dani.list, "dream")
    return

label home_masturbate_vip_dance_svet:
    $ add_to_list(svet.list, "dream")
    if numgen():
        show svet_poledance_1 as dream at rightover with dissolve
    else:
        show svet_poledance_2 as dream at rightover with dissolve
    pcm "Wow [svet.name]. Nice if you to show us how an experianced dancer does it."
    pcm "Getting those clothes off in a room packed full of horny men."
    pcm "Mmm, sounds like fun. Maybe we should all join you."
    hide dream with dissolve
    $ remove_from_list(svet.list, "dream")
    return



label home_masturbate_vip_dance_rachel_sex:
    show dance_rachel_dp ag as dream at rightover with dissolve
    pcm "Oh? Didn't mean to come in here..."
    pcm "Since I am though, you wont mind if I watch will you?"
    pcm "How many men have taken a turn with you before I came in here?"
    hide dream with dissolve
    return

label home_masturbate_vip_dance_anabel_sex:
    show dance_anabel_behind as dream at rightover with dissolve
    pcm "Wow [anabel.name], you turned out to be such a slut!"
    pcm "A few drinks is all it took for half the men here to get their dicks in you?"
    pcm "Ha, well enjoy it you naughty bitch."
    hide dream with dissolve
    return

label home_masturbate_vip_dance_dani_sex:
    show dance_dani_group as dream at rightover with dissolve
    pcm "Ah, good to see you having fun [dani.name]."
    pcm "Inviting us to this whore party and showing everyone how it's done?"
    pcm "Good, let's see how you do it and how many men finish inside you in just one night."
    hide dream with dissolve
    return

label home_masturbate_vip_dance_svet_sex:
    show dance_svet_buk as dream at rightover with dissolve
    pcm "Wow, I can see all over your face how many men you have entertained."
    pcm "Having a nice little collection there. Evry man here cums on your face."
    pcm "Scared they might put something in your belly, so you just let them cover you with it."
    hide dream with dissolve
    return

label home_masturbate_vip_dance_all_sex:
    show sb_tripplesex dani rachel anabel as dream at rightover with dissolve
    pcm "All of you lined up to get fucked? Wow, you aremaking the men really happy."
    pcm "Do you even know who is behind you? Or is it just all dicks for youto take?"
    pcm "Mmm, is there room for me?"
    hide dream with dissolve
    return




label home_masturbate_end:
    pc "Haaaaaa..."
    $ player.sex_cum(nosex, "self")
    $ player.face_orgasm()
    pc "Ahhh yes yes!"
    pc "..."
    $ player.face_meek()
    show screen blackout(100) with dissolve
    hide mastfeet as mast
    hide mastside as mast
    $ pc_dress()
    $ player.sex_hideaction()
    pause 0.5
    jump bed_sleep_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
