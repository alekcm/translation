label random_event_picker_dance_party_tombola:

    if not "first_party" in quest_dancevip.dict:
        $ quest_dancevip.dict["first_party"] = False
    if not "intro_chain" in quest_dancevip.dict:
        $ quest_dancevip.dict["intro_chain"] = 0

    if t.hour == 4:
        jump dance_party_end
    jump expression WeightedChoice([
    
    ("random_event_picker_dance_party_general_dance_recall", If(dance_is_dancing(), 5000, 0)),

    
    ("random_event_picker_dance_party_general_1", If(quest_dancevip.dict["wine_amount"], 100, 0)),
    ("random_event_picker_dance_party_general_2", If(quest_dancevip.dict["wine_amount"], 100, 0)),
    ("random_event_picker_dance_party_general_3", If(quest_dancevip.dict["wine_amount"], 100, 0)),
    ("random_event_picker_dance_party_general_4", If(quest_dancevip.dict["wine_amount"], 100, 0)),
    ("random_event_picker_dance_party_general_5", If(quest_dancevip.dict["wine_amount"], 100, 0)),
    ("random_event_picker_dance_party_general_6", If(quest_dancevip.dict["wine_amount"] and player.drunk > 50, 100, 0)),
    
    
    ("random_event_picker_dance_party_takeclothes_1", If(t.hour < 12 and c.top, max(player.drunk, 20), 0)),
    ("random_event_picker_dance_party_takeclothes_2", If(t.hour < 12 and c.bottom, max(player.drunk, 20), 0)),
    
    
    ("random_event_picker_dance_party_drink_1", If(quest_dancevip.dict["wine_amount"] and player.has_perk(perk_alcoholic), 100, 0)),
    ("random_event_picker_dance_party_drink_2", If(quest_dancevip.dict["wine_amount"] and player.mood <= 30, 500, 0)),
    
    
    ("random_event_picker_dance_party_grope_1", 100),
    ("random_event_picker_dance_party_grope_2", 100),
    
    
    ("random_event_picker_dance_party_anabel_taken", If(anabel.drunk >= 100 and not "party_sex" in anabel.list and anabel_here(dis(dis_partyhouse)), 1000, 0)),
    
    
    ("dance_party_drink_topup", If(not quest_dancevip.dict["wine_amount"], 100, 0)),
    
    
    ("random_event_picker_dance_party_general_gropesex", If((player.drunk >= 50 or t.hour < 12) and c.nude, (player.drunk / 3), 20)),
    ("random_event_picker_dance_party_general_gropeblow", If((player.drunk >= 50 or t.hour < 12) and c.nude, (player.drunk / 3), 20)),
    ("random_event_picker_dance_party_general_gangbang_invite", If((player.drunk >= 50 or t.hour < 12) and c.nude, (player.drunk / 6), 20)),
    
    
    ("random_event_picker_dance_party_general_sex_invite", If(player.drunk >= 80 or t.hour < 12, player.drunk, 20)),
    
    
    ("random_event_picker_dance_party_talk_tombola", If(any([anabel_here(), dani_here(), rachel_here(), svet_here()]) and not dance_is_dancing(), 100, 0)),

    
    ("random_event_picker_dance_party_talk_rachel_partysex", If("party_sex" in rachel.list and not "party_sex_comment" in rachel.list and quest_dancevip.dict["first_party"], 5000, 0)),
    ("random_event_picker_dance_party_talk_dani_partysex", If("party_sex" in dani.list and not "party_sex_comment" in dani.list and quest_dancevip.dict["first_party"], 5000, 0)),

    
    

    
    ("dance_party_first_event_chain_" + str(quest_dancevip.dict["intro_chain"]), If(renpy.has_label("dance_party_first_event_chain_" + str(quest_dancevip.dict["intro_chain"])) and quest_dancevip.dict["first_party"], 1000, 0)),
    
    ("dance_party_first_event_anabel_harm_picker", If(not renpy.has_label("dance_party_first_event_chain_" + str(quest_dancevip.dict["intro_chain"])) and quest_dancevip.dict["first_party"] and "anabel_harm" in quest_dancevip.list and anabel_here() and not anabel.drunk == 100, 100, 0)),
    
    ("dance_party_first_event_anabel_help_picker", If(not renpy.has_label("dance_party_first_event_chain_" + str(quest_dancevip.dict["intro_chain"])) and quest_dancevip.dict["first_party"] and "anabel_help" in quest_dancevip.list and anabel_here(), 100, 0)),

    ])


label dance_party_end:
    pcm "Hmm, looks like the party is winding down and people are starting to leave."
    pcm "Guess I should start getting ready to head off as well."
    if quest_dancevip.dict["wine_amount"]:
        $ walk(loc_party_kitchen)
        if player.has_perk(perk_alcoholic):
            pcm "Goodbye wine."
            $ dance_party_serve_wine(drink=True)
        $ dance_party_empty_wine()
        pcm "There we go."
    pcm "Hmmm..."
    if quest_dancevip.dict["first_party"]:
        jump dance_party_end_first_party
    $ walk(loc_party_bedroom1)

    menu:
        "Change and head off home":
            $ pc_dress_event("daily", where2=loc_party_main)
            $ walk(loc_revel_backstreet)
            jump travel
        "Stay the night here":

            $ pc_dress_event("home")
            jump bed_sleep_loop

label dance_party_sleep_loop:
    $ pc_strip(True)
    if t.hour < 5 or t.hour > 18:
        $ player.sex_blackout(partyman, quest_dancevip, 6)
    elif t.hour == 5:
        $ player.sex_blackout(partyman, quest_dancevip, 3)
    else:
        $ player.sex_blackout(partyman, quest_dancevip, 1)
    jump bed_sleep_loop

label dance_party_wake_sex:
    $ player.sex_vag(partyman, quest_dancevip)
    $ player.sex_hideaction()
    show sb_onback hump worried
    $ player.face_shock()
    hide screen blackout with hpunch
    $ player.face_angry()
    $ player.eye = 2
    "I wake up with a start and realise someone is having sex with me."
    show sb_onback look_up
    pc "Ah what the fuck! Get off me!"
    partyman.name "Ahhhhh!"
    $ player.sex_cum(partyman, "inside", quest_dancevip)
    pc "Shit shit! Fuck off!"
    show sb_onback no_sex with dissolve
    "I start wriggling my way from under him. He gets the hint and starts to dress and leave."
    hide sb_onback with dissolve
    pc "Cunt!"
    pcm "Ugh, Guess I better get out of here..."
    if tab_top in "home":
        $ pc_dress("daily")
    else:
        $ pc_dress()
    $ walk(loc_party_main)
    if school_dance_at_party():
        pcm "Party is still going on?"
        pcm "Ugh..."
        jump travel
    else:
        pcm "Everyone left?"
        jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
