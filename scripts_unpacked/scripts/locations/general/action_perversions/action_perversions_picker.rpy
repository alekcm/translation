init python:


    def perversion_can_trigger_mast(): 
        if ((player.check_horny(very_extreme=True) or (player.check_horny(extreme=True) and perk_exhib_total_value() > 400) or (player.check_horny() and player.has_perk(perk_exhibitionist))) and (loc_cur.outside and not loc_cur.population >= 2)) or (player.check_horny() and (loc_cur.home_location or dis(dis_home))):
            return True
        return False

    def perversion_can_trigger_flirt():
        if player.check_horny(extreme=True) or player.has_perk([perk_slut, perk_bimbo, perk_sucu, perk_lebo]):
            return True
        return False

    def perversion_can_trigger_preg():
        if player.has_perk(perk_preg_want) and player.has_perk(perk_ovulating) and not player.preg_knows and not player.has_perk(perk_inseminated):
            return True
        return False

    def perversion_can_trigger_exhib():
        if (player.has_perk(perk_exhibitionist) or perk_exhib_total_value() > 500) and loc_cur.outside:
            return True
        return False

    def perversion_can_trigger_train():
        if (player.has_perk([perk_freeuse, perk_sucu, perk_broken]) or player.check_horny(very_extreme=True)) and inv.qty(item_bdsm):
            return True
        return False

    def perversion_can_trigger_bitch():
        if quest_wolfgang.isactive() and quest_wolfgang.sex and wardrobe.qty(item_choker_6) and wolfgang_play_location():
            return True
        return False

    def perversion_can_trigger_any():
        if any([perversion_can_trigger_bitch(), perversion_can_trigger_train(), perversion_can_trigger_exhib(), perversion_can_trigger_flirt(), perversion_can_trigger_mast(), perversion_can_trigger_preg()]):
            return True
        return False

label action_perversion_picker_tombola:
    jump expression WeightedChoice([
    
    
    ("action_mast_event_start", If(perversion_can_trigger_mast(), 100, 0)),
    
    
    ("action_perversion_flirt_start", If(perversion_can_trigger_flirt(), 100, 0)),
    ("action_perversion_flirt_preg_start", If(perversion_can_trigger_preg(), 100, 0)),

    
    ("action_strip_event_tombola", If(perversion_can_trigger_exhib(), 100, 0)),

    
    ("action_perversion_freeusetrain_start", If(perversion_can_trigger_train(), 100, 0)),
    
    
    ("action_perversion_wolfgang_wear_collar", If(perversion_can_trigger_bitch(), 100, 0)),
    ])


label action_perversion_wolfgang_wear_collar:
    pcm "Hmmm, I can play with the doggies."
    $ acc.choker = 6
    pcm "There we go."
    jump travel

label action_perversion_wolfgang_remove_collar:
    pcm "That's enough playing with the animals."
    $ acc.choker = 0
    pcm "There we go."
    jump travel


label action_perversion_freeusetrain_start:
    pc "..."
    pcm "Okay... This is probable going to be a terrible idea."
    pcm "And fun..."
    $ travel_sleep_location()
    pcm "Hmm, over there..."
    $ travel_isolate()
    pcm "This should do."
    $ pc_striptease()
    $ pc_set_temp_outfit()
    pc "..."
    pcm "I'll make use of these I think."
    if inv.qty(item_ballgag) and not player.gagged:
        "I take my gag out and put it on."
        $ player.add_perk(perk_gagged)
    if inv.qty(item_blindfold) and not player.blind:
        "I wrap the blindfold over my eyes"
        $ player.add_perk(perk_blind)
    "I take some of the bindings I have out and start attaching them to myself."
    show sb_doggy1 body_tied with dissolve
    pcm "And now I wait..."
    jump random_event_generic_freeuse_tied_start


label action_perversion_flirt_start:
    pcm "Hmm, maybe I can find someone to entertain me..."
    jump flirt_street_checker

label action_perversion_flirt_preg_start:
    pcm "Hmm, I wonder if I can find someone to help me get pregnant?"
    jump flirt_street_checker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
