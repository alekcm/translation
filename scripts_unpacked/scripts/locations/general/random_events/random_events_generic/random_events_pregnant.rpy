label random_event_generic_pregnant:
    jump expression WeightedChoice([
    
    ("random_event_generic_pregnant_1", If (player.pregnancy >= 2, 100, 0)),
    ("random_event_generic_pregnant_2", If (player.pregnancy >= 2, 100, 0)),
    ("random_event_generic_pregnant_3", If (player.pregnancy >= 3, 100, 0)),
    ("random_event_generic_pregnant_4", If (player.pregnancy >= 2, 100, 0)),

    ("random_event_generic_pregnant_5", If (not player.preg_knows and player.days_pregnant < (global_pregnancy_length * 0.2) and not player.has_perk(perk_period_late), 100, 0)),
    ("random_event_generic_pregnant_6", If (player.pregnant and not player.preg_knows and player.days_pregnant > (global_pregnancy_length * 0.3) and not player.has_perk(perk_period_late), 100, 0)),
    ("random_event_generic_pregnant_7", If (player.pregnant and not player.preg_knows and player.days_pregnant > (global_pregnancy_length * 0.3) and not player.has_perk(perk_period_late), 100, 0)),
    ("random_event_generic_pregnant_8", If ( player.has_perk(perk_period_late), 100, 0)),

    ("travel", 1),
    
    
    
    ])



label random_event_generic_pregnant_1:
    $ player.face_shock()
    pc "Ohhh. A kick!"
    $ player.face_happy()
    pc "Soon little one."
    if player.has_perk(perk_broodmother):
        pcm "Then we can start on getting you a brother or sister."

    jump travel

label random_event_generic_pregnant_2:
    $ player.face_neutral()
    pcm "I suppose being pregnant isn't so bad."
    if player.has_perk(perk_male):
        pcm "Not something I ever though would happen being born a man..."
    jump travel

label random_event_generic_pregnant_3:
    $ player.face_surprised()
    pcm "Ufff. Getting around with this huge belly is starting to become a struggle."
    jump travel

label random_event_generic_pregnant_4:
    man "Hey [rlist.name_sexy]! Have fun putting that in your belly?"
    $ player.face_annoyed()
    pcm "Idiot."
    man "Next time call me. I'll fuck a bunch more in you!"
    pc "*Tsk*"
    jump travel



label random_event_generic_pregnant_5:
    pc "..."
    $ player.face_puke()
    pc "Ubbb..."
    $ player.face_normal()
    if player.preg_amount:
        pcm "Fuck, this is what happened the last time I was pregnant..."
        pcm "Think I need to take a test."
        if player.has_perk(perk_preg_notwant):
            pcm "Or a pill..."
    else:
        pcm "What the fuck?"
    jump travel

label random_event_generic_pregnant_6:
    pcm "Damn, I swear I am getting bigger. I need to start working out or something."
    jump travel

label random_event_generic_pregnant_7:
    if player.has_perk(perk_preg_want):
        pcm "Hmmm, Not time for my period yet, but I swear I am getting bigger. Maybe I am pregnant at last."
    else:
        pcm "..."
        pcm "Not time for my period yet, but I swear I am getting bigger..."
    jump travel

label random_event_generic_pregnant_8:
    if player.has_perk(perk_preg_want):
        pcm "No period yet. Yay!"
    else:
        pcm "C'mon period! Hurry up for once."
    jump travel

label random_event_generic_inseminated:
    jump expression WeightedChoice([
    ("random_event_generic_inseminated_1", If (not player.has_perk(perk_preg_want, perk_map), 100, 0)),
    ("random_event_generic_inseminated_2", If (not player.has_perk(perk_preg_want, perk_map), 100, 0)),
    ("random_event_generic_inseminated_3", If (player.has_perk(perk_preg_notwant) and not player.has_perk(perk_map), 100, 0)),
    ("random_event_generic_inseminated_4", If (player.has_perk(perk_preg_notwant) and inv.qty(item_map_pill) and not player.has_perk(perk_map), 100, 0)),
    ("random_event_generic_inseminated_5", If (player.has_perk(perk_preg_want), 100, 0)),
    ("random_event_generic_inseminated_6", If (player.has_perk(perk_preg_want), 100, 0)),
    ("travel", 1),  
    ])

label random_event_generic_inseminated_1:
    pcm "I really should take a pill or something or else I might end up pregnant."
    jump travel

label random_event_generic_inseminated_2:
    pcm "Ugh, not a good time of the month and I may end up pregnant. I really should take a pill or something."
    jump travel

label random_event_generic_inseminated_3:
    pcm "Fuck, I really don't want to end up pregnant. I need to do something about it."
    jump travel

label random_event_generic_inseminated_4:
    pcm "Ugh, no way am I letting myself end up pregnant..."
    $ item_inv_call = True
    call item_map_pill_action from _call_item_map_pill_action

label random_event_generic_inseminated_5:
    pcm "Hmm, wonder if I will wind up pregnant?"
    jump travel

label random_event_generic_inseminated_6:
    pcm "A dangerous time of the month. Hope I end up pregnant."
    jump travel

label random_event_generic_lactation:
    jump expression WeightedChoice([
    ("random_event_generic_lactation_1", If (loc_cur.population >= 2 and player.milky, 100, 0)),
    ("random_event_generic_lactation_2", If (player.milky, 100, 0)),
    ("random_event_generic_lactation_3", If (not player.milky and perk_lactating.dict["milk_amount"] in irange(10,15), 100, 0)),
    ("random_event_generic_lactation_4", If (not player.milky and perk_lactating.dict["milk_amount"] in irange(10,15), 100, 0)),
    ("travel", 1),  
    ])

label random_event_generic_lactation_1:
    pcm "Ugh, I am leaking and people can see..."
    jump travel

label random_event_generic_lactation_2:
    pcm "I really need to milk myself."
    jump travel

label random_event_generic_lactation_3:
    pcm "I can feel a pressure in my breasts. I need to milk myself soon if I don't want to start leaking."
    jump travel

label random_event_generic_lactation_4:
    pcm "Hmmm..."
    $ player.cover_breasts_force()
    pcm "Probably about time I milked myself."
    $ player.cover_reset()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
