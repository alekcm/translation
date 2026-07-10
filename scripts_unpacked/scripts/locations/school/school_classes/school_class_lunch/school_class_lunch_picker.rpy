label school_class_lunch:

    $ walk(loc_school_cafe, trans=False)
    if school_met_friend == False:
        with dissolve
        jump school_class_lunch_alone
    else:
        jump school_class_lunch_picker


label school_class_lunch_picker:
    $ rand_choice = WeightedChoice([
    ("school_class_lunch_cassmira_1", If(cass.isactive and mira.isactive and not "hospitalised" in mira.list,100, 0)),
    ("school_class_lunch_cassmira_2", If(cass.isactive and mira.isactive and not "hospitalised" in mira.list,100, 0)),
    ("school_class_lunch_cassmira_3", If(cass.isactive and mira.isactive and not "hospitalised" in mira.list,100, 0)),
    ("school_class_lunch_cassmira_4", If(cass.isactive and mira.isactive and not "hospitalised" in mira.list,100, 0)),
    ("school_class_lunch_cassmira_5", If(cass.isactive and mira.isactive and not "hospitalised" in mira.list,100, 0)),
    ("school_class_lunch_cassmira_6", If(cass.isactive and mira.isactive and not "hospitalised" in mira.list,100, 0)),
    ("school_class_lunch_cassmira_7", If(cass.isactive and mira.isactive and not "hospitalised" in mira.list,100, 0)),
    ("school_class_lunch_cassmira_8", If(cass.isactive and mira.isactive and not "hospitalised" in mira.list,100, 0)),
    ("school_class_lunch_cassmira_9", If(cass.isactive and mira.isactive and not "hospitalised" in mira.list,100, 0)),
    ("school_class_lunch_cassmira_10", If(cass.isactive and mira.isactive and not "hospitalised" in mira.list,100, 0)),

    ("school_class_lunch_cass_1", If(cass.isactive and not mira.isactive and not quest_mira_missing.active,100, 0)),
    ("school_class_lunch_cass_2", If(cass.isactive,100, 0)),
    ("school_class_lunch_cass_3", If(cass.isactive and school_bully_quest_bully_event_stage > 4 and not shane.dead, 100, 0)),  
    ("school_class_lunch_cass_4", If(cass.isactive,100, 0)),
    ("school_class_lunch_cass_5", If(cass.isactive and school_soccer_quest_hangout_prompt, 100, 0)),
    ("school_class_lunch_cass_6", If(cass.isactive,100, 0)),
    ("school_class_lunch_cass_7", If(cass.isactive and school_dance_quest_show_count >= 5, 100, 0)),
    ("school_class_lunch_cass_8", If(cass.isactive,100, 0)),
    ("school_class_lunch_cass_9", If(cass.isactive,100, 0)),
    ("school_class_lunch_cass_10", If(cass.isactive and pub_waitress.timesworked >= 8, 100, 0)),

    ("school_class_lunch_mira_1", If(mira.isactive and not cass.isactive and not "hospitalised" in mira.list,1,0)),
    ("school_class_lunch_mira_2", If(mira.isactive and not cass.isactive and not "hospitalised" in mira.list,1,0)),
    ("school_class_lunch_mira_3", If(mira.isactive and not cass.isactive and not "hospitalised" in mira.list,1,0)),
    ("school_class_lunch_mira_4", If(mira.isactive and cass.isactive and not "hospitalised" in mira.list,1,0)),
    ("school_class_lunch_mira_5", If(mira.isactive and not cass.isactive and not "hospitalised" in mira.list,1,0)),
    ("school_class_lunch_mira_6", If(mira.isactive and not cass.isactive and not "hospitalised" in mira.list,1,0)),
    ("school_class_lunch_mira_7", If(mira.isactive and cass.isactive and not "hospitalised" in mira.list,1,0)),

    ("school_class_lunch_dani_1", If (school_dance_lunch_can_trigger() and dani.isactive and pub_waitress.timesworked >= 8 and not "asked_pub_work" in dani.list and dani.love >= 30, 100, 0)),
    ("school_class_lunch_dani_2", If (school_dance_lunch_can_trigger() and dani.isactive and school_bully_quest_bully_event_stage > 4 and not shane.dead, 100, 0)),  
    ("school_class_lunch_dani_3", If (school_dance_lunch_can_trigger() and dani.isactive and school_bully_quest_bully_event_stage >= 10, 100, 0)),  
    ("school_class_lunch_dani_4", If (school_dance_lunch_can_trigger() and dani.isactive, 100, 0)),
    ("school_class_lunch_dani_5", If (school_dance_lunch_can_trigger() and dani.isactive, 100, 0)),
    ("school_class_lunch_dani_6", If(school_dance_lunch_can_trigger() and dani.isactive and player.iswhore and not dani.iswhore, 100, 0)),
    ("school_class_lunch_dani_7", If(school_dance_lunch_can_trigger() and dani.isactive and "dani_photos_pc_knows" in school_photo_quest.conversation_topics and not "dani_photos_dani_knows_pc_knows" in school_photo_quest.conversation_topics, 100, 0)),
    ("school_class_lunch_dani_8", If(school_dance_lunch_can_trigger() and dani.isactive and "dani_photos_dani_knows_pc_knows" in school_photo_quest.conversation_topics, 100, 0)),
 
    ("school_class_lunch_danianabel_1", If (school_dance_lunch_can_trigger() and all([dani_here(), anabel_here()]), 100, 0)),
    ("school_class_lunch_danianabel_2", If (school_dance_lunch_can_trigger() and all([dani_here(), anabel_here()]) and pub_waitress.timesworked >= 8, 100, 0)),
    ("school_class_lunch_danianabel_3", If (school_dance_lunch_can_trigger() and all([dani_here(), anabel_here()]), 100, 0)),
    ("school_class_lunch_danianabel_4", If (school_dance_lunch_can_trigger() and all([dani_here(), anabel_here()]), 100, 0)),
    ("school_class_lunch_danianabel_5", If (school_dance_lunch_can_trigger() and all([dani_here(), anabel_here()]), 100, 0)),
    ("school_class_lunch_danianabel_6", If (school_dance_lunch_can_trigger() and all([dani_here(), anabel_here()]), 100, 0)),
    ("school_class_lunch_danianabel_7", If (school_dance_lunch_can_trigger() and all([dani_here(), anabel_here()]), 100, 0)),
    ("school_class_lunch_danianabel_8", If (school_dance_lunch_can_trigger() and all([dani_here(), anabel_here()]), 100, 0)),
    ("school_class_lunch_danianabel_9", If (school_dance_lunch_can_trigger() and all([dani_here(), anabel_here()]), 100, 0)),
    

    ("school_class_lunch_svet_1", If (school_dance_lunch_can_trigger() and svet.isactive, 100, 0)),
    ("school_class_lunch_svet_2", If (school_dance_lunch_can_trigger() and all([svet.isactive,rachel.isactive]), 100, 0)),
    ("school_class_lunch_svet_3", If (school_dance_lunch_can_trigger() and all([svet.isactive,rachel.isactive]), 100, 0)),
    ("school_class_lunch_svet_4", If (school_dance_lunch_can_trigger() and rachel.isactive, 100, 0)),
    
    
    
    
    
    
    ("school_class_lunch_svet_11", If(school_dance_lunch_can_trigger() and rachel.isactive and drake.fname in rachel.conversation_topics and not "told_sex_" + drake.fname in rachel.conversation_topics,500,0)),
    ("school_class_lunch_svet_12", If(school_dance_lunch_can_trigger() and rachel.isactive and nate.fname in rachel.conversation_topics and not "told_sex_" + nate.fname in rachel.conversation_topics,500,0)),
    ("school_class_lunch_svet_13", If(school_dance_lunch_can_trigger() and rachel.isactive and dan.fname in rachel.conversation_topics and not "told_sex_" + dan.fname in rachel.conversation_topics,500,0)),
    
    ("school_class_lunch_svet_15", If(school_dance_lunch_can_trigger() and rachel.isactive and any(item in ["pregnant_" + drake.fname, "pregnant_" + nate.fname, "pregnant_" + dan.fname] for item in rachel.conversation_topics), 2000, 0)),

    ("school_class_lunch_soccerboys_1", If(drake.has_met and all([school_soccer_quest.isactive,drake.isactive,nate.isactive,dan.isactive]),100,0)),
    ("school_class_lunch_soccerboys_2", If(drake.has_met, 100 - player.mood, 0)),
    ("school_class_lunch_soccerboys_3", If(drake.has_met, nate.lust, 0)),
    ("school_class_lunch_soccerboys_4", If(drake.has_met and all([school_soccer_quest.isactive,drake.isactive,nate.isactive,dan.isactive]),100,0)),
    ("school_class_lunch_soccerboys_5", If(drake.has_met and all([school_soccer_quest.isactive,drake.isactive,nate.isactive,dan.isactive]),100,0)),
    ("school_class_lunch_soccerboys_6", If (drake.has_met and mira.isactive,1,0)),
    ("school_class_lunch_soccerboys_7", If(drake.has_met and all([school_soccer_quest.isactive,drake.isactive,nate.isactive,dan.isactive]),100,0)),

    ("school_class_lunch_alone", 20),

    ("school_class_lunch_dani_postdance", If (dani.isactive and "dance_went_alone" in dani.conversation_topics and school_dance_quest_show_count == 9,10000,0)), 

    ])
    jump expression rand_choice

label school_class_lunch_alone:
    with dissolve
    "I grab something to eat and find somewhere empty to sit and eat my food."
    jump school_class_lunch_end

label school_class_lunch_alone_post:
    "I can't see anyone I know so I just grab something to eat and find somewhere empty to sit."
    jump school_class_lunch_end

label school_class_lunch_end:
    $ renpy.scene()
    with dissolve
    $ school_lunch()
    pcm "Oh? That's lunch over?"
    $ walk(loc_school_hallway)
    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
