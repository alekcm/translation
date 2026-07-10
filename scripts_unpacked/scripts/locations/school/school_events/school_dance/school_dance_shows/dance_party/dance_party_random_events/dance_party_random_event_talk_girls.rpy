label random_event_picker_dance_party_talk_tombola:
    if quest_dancevip.dict["wine_amount"]:
        pc "Anyone for wine?"
    else:
        pcm "Oh?"
label random_event_picker_dance_party_talk_tombola_direct:
    jump expression WeightedChoice([
    ("random_event_picker_dance_party_talk_anabel", If(anabel_here(), 10, 0)),
    ("random_event_picker_dance_party_talk_dani", If(dani_here(), If(dani.hate, 0, 10), 0)),
    ("random_event_picker_dance_party_talk_rachel", If(rachel_here(), 10, 0)),
    ("random_event_picker_dance_party_talk_svet", If(svet_here(), 10, 0)),

    ("random_event_picker_dance_party_talk_none", If(not any([anabel_here(), dani_here(), rachel_here(), svet_here()]) or (dani.hate and dani_here() and not any([anabel_here(), rachel_here(), svet_here()])), 100, 0)),

    ])

label random_event_picker_dance_party_talk_none:


    pcm "Hope the girls are doing okay..."
    jump travel


label random_event_picker_dance_party_talk_anabel:
    show anabel at right1 with dissolve
    jump expression WeightedChoice([
    ("random_event_picker_dance_party_talk_anabel_1", If(player.drunk >= 100, 100, 0)),
    ("random_event_picker_dance_party_talk_anabel_2", 100),

    ("random_event_picker_dance_party_talk_anabel_tipsy_1", If(anabel.is_tipsy and not anabel.is_wasted, 100, 0)),
    ("random_event_picker_dance_party_talk_anabel_tipsy_2", If(anabel.is_tipsy and not anabel.is_wasted, 100, 0)),

    ("random_event_picker_dance_party_talk_anabel_drunk_1", If(anabel.is_wasted, 100, 0)),
    ("random_event_picker_dance_party_talk_anabel_drunk_2", If(anabel.is_wasted, 100, 0)),
    
    ("dance_party_first_event_anabel_harm_picker", If(not renpy.has_label("dance_party_first_event_chain_" + str(quest_dancevip.dict["intro_chain"])) and quest_dancevip.dict["first_party"] and "anabel_harm" in quest_dancevip.list and anabel_here() and quest_dancevip.dict["wine_amount"], 300, 0)),
    
    ("dance_party_first_event_anabel_help_picker", If(not renpy.has_label("dance_party_first_event_chain_" + str(quest_dancevip.dict["intro_chain"])) and quest_dancevip.dict["first_party"] and "anabel_help" in quest_dancevip.list and anabel_here() and quest_dancevip.dict["wine_amount"], 300, 0)),
    
    ("dance_party_first_event_anabel_comment_topless", If(not ("bottomless_comment" in anabel.list or "topless_comment" in anabel.list) and "topless" in anabel.list and not "nude" in anabel.list, 1000, 0)),
    ("dance_party_first_event_anabel_comment_bottomless", If(not ("bottomless_comment" in anabel.list or "topless_comment" in anabel.list) and "nude" in anabel.list and not "topless" in anabel.list, 1000, 0)),
    ("dance_party_first_event_anabel_comment_nude", If(not "nude_comment" in anabel.list and "topless" in anabel.list and "nude" in anabel.list, 1000, 0)),
    
    ])

label random_event_picker_dance_party_talk_dani:
    if dani.hate:
        pcm "I don't want to talk to her..."
        jump travel
    show dani at right1 with dissolve
    jump expression WeightedChoice([
    ("random_event_picker_dance_party_talk_dani_1", If(player.drunk >= 100, 100, 0)),
    ("random_event_picker_dance_party_talk_dani_2", 100),

    
    ("dance_party_first_event_dani_comment_topless", If(not ("bottomless_comment" in dani.list or "topless_comment" in dani.list) and "topless" in dani.list and not "nude" in dani.list, 1000, 0)),
    ("dance_party_first_event_dani_comment_bottomless", If(not ("bottomless_comment" in dani.list or "topless_comment" in dani.list) and "nude" in dani.list and not "topless" in dani.list, 1000, 0)),
    ("dance_party_first_event_dani_comment_nude", If(not "nude_comment" in dani.list and "topless" in dani.list and "nude" in dani.list, 1000, 0)),
    
        
    
    
    ("random_event_picker_dance_party_talk_dani_partysex_talk", If("party_sex_comment" in dani.list and not "party_sex_talk" in dani.list and  quest_dancevip.dict["first_party"], 5000, 0)),

    ])

label random_event_picker_dance_party_talk_rachel:
    show rachel at right1 with dissolve
    jump expression WeightedChoice([
    ("random_event_picker_dance_party_talk_rachel_1", If(player.drunk >= 100, 100, 0)),
    ("random_event_picker_dance_party_talk_rachel_2", 100),

    
    ("dance_party_first_event_rachel_comment_topless", If(not ("bottomless_comment" in rachel.list or "topless_comment" in rachel.list) and "topless" in rachel.list and not "nude" in rachel.list, 1000, 0)),
    ("dance_party_first_event_rachel_comment_bottomless", If(not ("bottomless_comment" in rachel.list or "topless_comment" in rachel.list) and "nude" in rachel.list and not "topless" in rachel.list, 1000, 0)),
    ("dance_party_first_event_rachel_comment_nude", If(not "nude_comment" in rachel.list and "topless" in rachel.list and "nude" in rachel.list, 1000, 0)),
    
    
    
    ("random_event_picker_dance_party_talk_rachel_partysex_talk", If("party_sex_comment" in rachel.list and not "party_sex_talk" in rachel.list and  quest_dancevip.dict["first_party"], 5000, 0)),

    ])

label random_event_picker_dance_party_talk_svet:
    show svet at right1 with dissolve
    jump expression WeightedChoice([
    ("random_event_picker_dance_party_talk_svet_1", If(player.drunk >= 100, 100, 0)),
    ("random_event_picker_dance_party_talk_svet_2", 100),

    
    ("dance_party_first_event_svet_comment_topless", If(not ("bottomless_comment" in svet.list or "topless_comment" in svet.list) and "topless" in svet.list, 1000, 0)),
    ("dance_party_first_event_svet_comment_bottomless", If(not ("bottomless_comment" in svet.list or "topless_comment" in svet.list) and "nude" in svet.list, 1000, 0)),
    ("dance_party_first_event_svet_comment_nude", If(not "nude_comment" in svet.list and "topless" in svet.list and "nude" in svet.list, 1000, 0)),
    
    
    

    ])







label random_event_picker_dance_party_talk_anabel_1:
    anabel.name "Err, don't you think you should be careful with the drinks?"
    pc "It's fine, I'm not spilling them."
    anabel.name "I meant the drinking..."
    pc "Ehh!"
    jump random_event_picker_dance_party_talk_anabel_end

label random_event_picker_dance_party_talk_anabel_2:
    anabel.name "We are doing more drink serving than dancing."
    pc "Yeah, guess it's the main part of the job."
    anabel.name "The drinks are free. Not like it's hard to just grab your own."
    if player.has_perk(perk_alcoholic):
        pc "I know, grabbing my own is easy."
    jump random_event_picker_dance_party_talk_anabel_end


label random_event_picker_dance_party_talk_anabel_tipsy_1:
    pc "Ohh, been enjoying the booze?"
    anabel.name "Somewhat. When I serve the guys, they always offer me some."
    pc "Well, have fun."
    jump random_event_picker_dance_party_talk_anabel_end

label random_event_picker_dance_party_talk_anabel_tipsy_2:
    pc "Getting that booze in you. Should be fun."
    anabel.name "They keep asking to share with them..."
    jump random_event_picker_dance_party_talk_anabel_end

label random_event_picker_dance_party_talk_anabel_drunk_1:
    anabel.name "Wheww [name]!"
    pc "Having fun?"
    anabel.name "[name]!"
    pc "Haha."
    jump random_event_picker_dance_party_talk_anabel_end

label random_event_picker_dance_party_talk_anabel_drunk_2:
    anabel.name "How [name]! [name]..."
    pc "[anabel.nname]!"
    anabel.name "The wine is freee!"
    pc "I know. Drink until you drop."
    jump random_event_picker_dance_party_talk_anabel_end



label dance_party_first_event_anabel_comment_topless:
    $ add_to_list(anabel.list, "topless_comment")
    pc "Err, giving them some fresh air?"
    anabel.name "Ah, someone, kinda..."
    anabel.name "I lost my top..."
    pc "Okay, well have fun with that."
    jump random_event_picker_dance_party_talk_anabel_end

label dance_party_first_event_anabel_comment_bottomless:
    $ add_to_list(anabel.list, "bottomless_comment")
    pc "I know the skirt was small. Looks like it got smaller when I wasn't looking."
    anabel.name "I don't know how it happened."
    pc "Sure sure."
    jump random_event_picker_dance_party_talk_anabel_end

label dance_party_first_event_anabel_comment_nude:
    $ add_to_list(anabel.list, "bottomless_comment")
    $ add_to_list(anabel.list, "topless_comment")
    $ add_to_list(anabel.list, "nude_comment")
    pc "Errrm... Good for the guys I guess."
    anabel.name "Huh?"
    pc "Nothing."
    anabel.name "I'm not the only one who lost stuff."
    pc "I didn't say anything."
    jump random_event_picker_dance_party_talk_anabel_end



label random_event_picker_dance_party_talk_anabel_end:
    "We chit chat for a bit then I go on my way."
    $ relax(5, anabel)
    hide anabel with dissolve
    jump travel



label random_event_picker_dance_party_talk_dani_1:
    dani.name "Hey [name], taking a break."
    pc "Yeah, a couple of minutes here with no one harassing me."
    dani.name "Well, getting harassed is what we are paid for."
    pc "True."
    jump random_event_picker_dance_party_talk_dani_end

label random_event_picker_dance_party_talk_dani_2:
    dani.name "Good job we actually practised dance with the whole stripper stage."
    pc "Yeah, didn't expect to see it be a full pole dance thing."
    jump random_event_picker_dance_party_talk_dani_end


label dance_party_first_event_dani_comment_topless:
    $ add_to_list(dani.list, "topless_comment")
    pc "Err, no top?"
    if dani.iswhore:
        dani.name "No, someone paid to take it off me."
        pc "Oh?"
        dani.name "Supposed to earn here, right?"
    else:
        show dani worried
        dani.name "Err... It kinda..."
        pc "Perverts round here."
        dani.name "Yeah..."
    jump random_event_picker_dance_party_talk_dani_end

label dance_party_first_event_dani_comment_bottomless:
    $ add_to_list(dani.list, "bottomless_comment")
    pc "Err, lost your skirt?"
    if dani.iswhore:
        dani.name "Yeah. Well, no. Someone paid for it."
        pc "Oh?"
        dani.name "Supposed to earn here, right?"
    else:
        show dani worried
        dani.name "Err... It kinda..."
        pc "Perverts round here."
        dani.name "Yeah..."
    jump random_event_picker_dance_party_talk_dani_end

label dance_party_first_event_dani_comment_nude:
    $ add_to_list(dani.list, "bottomless_comment")
    $ add_to_list(dani.list, "topless_comment")
    $ add_to_list(dani.list, "nude_comment")
    pc "Errrm... Having fun showing off?"
    if dani.iswhore:
        dani.name "No. But will have fun with the money they paid me to be here like this."
        pc "Err, good for you."
    else:
        show dani worried
        dani.name "Ah, well... No, but they offered money."
        pc "Yeah, have to pay the rent some how."
        dani.name "..."
    jump random_event_picker_dance_party_talk_dani_end

label random_event_picker_dance_party_talk_dani_partysex:
    $ add_to_list(dani.list, "party_sex_comment")
    pcm "Hmm, looks like [dani.name] has gone missing."
    if dani.iswhore:
        pcm "Not a suprise I guess. Hope she is earning enough to be worth it."
    else:
        pcm "Hope she knows what she is doing..."
    jump travel

label random_event_picker_dance_party_talk_dani_partysex_talk:
    $ add_to_list(dani.list, "party_sex_talk")
    pc "Err, you kinda went missing for a bit."
    if dani.iswhore:
        dani.name "Yeah, they were offering some money to go with them."
        pc "Ah okay. Get paid?"
        dani.name "Of course."
    else:
        dani.name "Err... Yeah..."
        pc "Errm... Get paid?"
        dani.name "..."
        pc "Sorry..."
    jump random_event_picker_dance_party_talk_dani_end

label random_event_picker_dance_party_talk_dani_end:
    show dani neutral
    "We chit chat for a bit then I go on my way."
    $ relax(5, dani)
    hide dani with dissolve
    jump travel



label random_event_picker_dance_party_talk_rachel_1:
    rachel.name "You been sneaking the booze? They dn't mind."
    if player.has_perk(perk_alcoholic) or player.drunk > 80:
        pc "Yeah, they really don't care."
    else:
        pc "Seems like they don't. Probably want us drunk."
    rachel.name "Maybe I should stay the night here. Free booze, beds and not freezing my ass off."
    pc "Don't worry. Stay here and your ass will get a different feeling."
    jump random_event_picker_dance_party_talk_rachel_end

label random_event_picker_dance_party_talk_rachel_2:
    pc "Having fun?"
    rachel.name "Yeah, the guys are nice."
    pc "Well, make sure you get out of here with all your clothes on."
    rachel.name "Why?"
    jump random_event_picker_dance_party_talk_rachel_end


label dance_party_first_event_rachel_comment_topless:
    $ add_to_list(rachel.list, "topless_comment")
    if player.has_perk([perk_slut, perk_bimbo, perk_sucu]):
        pc "Lost your top?"
        rachel.name "Yeah."
        pc "Slut!"
        rachel.name "Awww thanks."
    elif "can_play_games" in rachel.list:
        pc "Getting your tits out here as well now?"
        rachel.name "Everyone should see them."
        rachel.name "Want to look?"
        pc "They are right in front. I can't not see them."
    else:
        pc "Lost your top?"
        rachel.name "No."
        pc "Well you aren't wearing one."
        rachel.name "Yeah. But it's not lost. I know were it is."
        pc "Ah... Okay..."
    jump random_event_picker_dance_party_talk_rachel_end

label dance_party_first_event_rachel_comment_bottomless:
    $ add_to_list(rachel.list, "bottomless_comment")
    if player.has_perk([perk_slut, perk_bimbo, perk_sucu]):
        pc "Why even wear the skirt. Just gets in the way."
        rachel.name "NO PINKIES!!!"
    elif "can_play_games" in rachel.list:
        pc "Oooh. Showing off the goods."
        rachel.name "Maybe I should bend over."
        pc "Sure."
    else:
        pc "Lost your skirt?"
        rachel.name "No."
        pc "Well you aren't wearing one."
        rachel.name "Yeah. But it's not lost. I know were it is."
        pc "Ah... Okay..."
    jump random_event_picker_dance_party_talk_rachel_end

label dance_party_first_event_rachel_comment_nude:
    $ add_to_list(rachel.list, "nude_comment")
    $ add_to_list(rachel.list, "bottomless_comment")
    $ add_to_list(rachel.list, "topless_comment")
    if player.has_perk([perk_slut, perk_bimbo, perk_sucu]):
        pc "Going to get dragged off to a room and passed around like this."
        rachel.name "Well they are taking their time doing it."
        pc "Bend over some more."
    elif "can_play_games" in rachel.list:
        pc "Should I tell you to run around the house?"
        rachel.name "Huh?"
        pc "First running around the academy, now here."
        rachel.name "Ahhh."
    else:
        pc "Err, naked is it?"
        rachel.name "Yup. You like?"
        pc "I'm sure everyone else does."
        rachel.name "Thanks."
    jump random_event_picker_dance_party_talk_rachel_end

label random_event_picker_dance_party_talk_rachel_partysex:
    $ add_to_list(rachel.list, "party_sex_comment")
    pcm "Hmm, can't see [rachel.name] anywhere."
    pcm "That dirty bitch aready get dragged of by a guy?"
    pcm "Hmm, probably more than one guy."
    jump travel

label random_event_picker_dance_party_talk_rachel_partysex_talk:
    $ add_to_list(rachel.list, "party_sex_talk")
    pc "Thought we lost you for a bit there."
    rachel.name "You did!"
    pc "Oh?"
    rachel.name "Bunch of guys took me somewhere. It was fun."
    pc "Oh? Okay then."
    jump random_event_picker_dance_party_talk_rachel_end

label random_event_picker_dance_party_talk_rachel_end:
    "We chit chat for a bit then I go on my way."
    $ relax(5, rachel)
    hide rachel with dissolve
    jump travel



label random_event_picker_dance_party_talk_svet_1:
    svet.name "Keep your wits about you [name]."
    if player.drunk >= 80:
        pc "Bit too late for that. Free booze!"
        svet.name "Then at least make sure to get paid."
    else:
        pc "Sure, who knows what might happen in this party with free booze and lot's of men."
        svet.name "..."
    jump random_event_picker_dance_party_talk_svet_end

label random_event_picker_dance_party_talk_svet_2:
    svet.name "Keeping out of trouble?"
    pc "Probably not."
    svet.name "..."
    jump random_event_picker_dance_party_talk_svet_end


label dance_party_first_event_svet_comment_topless:
    $ add_to_list(svet.list, "topless_comment")
    pc "Surprised to see you, err... Like this."
    svet.name "Why? Get paid for it, don't give this stuff for free."
    pc "I guess..."
    jump random_event_picker_dance_party_talk_svet_end

label dance_party_first_event_svet_comment_bottomless:
    $ add_to_list(svet.list, "bottomless_comment")
    pc "No skirt?"
    svet.name "Someone bought it."
    pc "Okay."
    jump random_event_picker_dance_party_talk_svet_end

label dance_party_first_event_svet_comment_nude:
    $ add_to_list(svet.list, "bottomless_comment")
    $ add_to_list(svet.list, "topless_comment")
    $ add_to_list(svet.list, "nude_comment")
    pc "We doing stripteases now?"
    svet.name "As long as they pay enough for it."
    jump random_event_picker_dance_party_talk_svet_end

label random_event_picker_dance_party_talk_svet_end:
    "We chit chat for a bit then I go on my way."
    $ relax(5, svet)
    hide svet with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
