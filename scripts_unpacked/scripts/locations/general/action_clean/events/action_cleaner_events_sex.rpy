label action_clean_event_sex_debug:
    "Debug for cleaning sex event. assumes you have maid or bar uni on"
    $ maid_outfit_set()
    $ pc_dress("work")
    $ renpy.show(renpy.random.choice(["sb_onfours", "sb_doggy1", "sb_doggy2"]))
    with dissolve
    $ player.sex_location_offer(
    sex_vag_want="action_clean_event_sex_vag_want",
    sex_vag_notwant="action_clean_event_sex_vag_notwant",
    sex_anal="action_clean_event_sex_anal",
    who=pervert
    )

label action_clean_event_sex_vag_want:
    $ c.pants = 0
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_penetrate_vag_slow]"
    $ if_showing("sb_onfours", "up vag", "sb_ontop", "back ag", "sb_doggy1", "ag vag head_down", "sb_doggy2", "head_back happy wink insidevag", "sb_assup", "sex")
    $ player.sex_vag(punter, quest_cleaner)
    $ player.face_excited()
    if player.want_sexlocation == 2:
        pc "[rlist.having_sex_thats_not_anal_happy]"

    "[rlist.having_sex_action]"
    "[rlist.having_sex_action]"
    pervert "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"

    if not numgen(0,10):
        call action_clean_event_sex_anal_switch from _call_action_clean_event_sex_anal_switch

    "[rlist.having_sex_enjoy]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_yes]"
    $ player.sex_cum_location_offer(
    difficulty=2, choice_inside="Keep going!", choice_pullout="Not inside.",
    cum_want="action_clean_event_sex_vag_cum_want", 
    cum_notwant="action_clean_event_sex_vag_cum_notwant", 
    cum_pullout="action_clean_event_sex_cum_pullout",
    cum_pullout_poke="action_clean_event_sex_cum_pullout_poke",
    cum_pullout_anal="action_clean_event_sex_cum_pullout_anal",    
    )

label action_clean_event_sex_vag_notwant:
    $ c.pants = 0
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    "[rlist.having_sex_tease_vag]"
    if player.want_sexlocation == 2:

        pcm "[rlist.having_sex_asked_anal_wonder]"
        pc "[rlist.having_sex_asked_anal_comment]"

        if player.check_speech(2):
            pervert "[rlist.having_sex_asked_anal_respond]"
            jump action_clean_event_sex_anal
        else:
            if player.check_sex_agree(4):
                jump action_clean_event_sex_vag_want
            else:
                pervert "[rlist.having_sex_asked_anal_respond]"
    $ player.sex_forced(punter, quest_cleaner)
    $ player.sex_vag(punter, quest_cleaner)
    $ player.face_angry()
    "[rlist.having_sex_penetrate_vag_slow]"
    $ if_showing("sb_onfours", "vag up", "sb_doggy1", "grit vag", "sb_doggy2", "head_back shock squint angry insidevag")
    pc "[rlist.having_sex_thats_not_anal_angry]"
    $ dialouge = WeightedChoice([
    ("Don't worry, I'll pull out.", 1),
    ("It's ok. I'll try not to cum inside.", 1),
    ("Don't worry. Just relax and enjoy.", 1),
    ("It's ok. I just want to make you feel good.", 1),
    ])
    punter "[dialouge]"
    pc "[rlist.having_sex_take_it_out]"
    jump action_clean_event_sex_forcesex

label action_clean_event_sex_anal:
    $ c.pants = 0
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    "[rlist.having_sex_tease_vag]"
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    $ if_showing("sb_doggy2", "pokeasshold")
    $ if_showing("sb_doggy2", "pokeass")

    "[rlist.having_sex_vag_to_ass_switch]"

    $ player.sex_anal(punter, quest_cleaner)
    $ player.face_excited()
    $ if_showing("sb_onfours", "ass", "sb_ontop", "doggy", "sb_doggy1", "anal", "sb_doggy2", "insideass")

    "[rlist.having_sex_penetrate_ass_slow]"
    pervert "Ahhhhhh so warm."
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    jump action_clean_event_sex_anal_jump

label action_clean_event_sex_anal_jump:
    pervert "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"

    "[rlist.having_sex_man_close]"
    "[rlist.having_sex_pc_close_anal]"
    $ player.face_orgasm()

    pervert "[rlist.having_sex_man_close_dialogue]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_cum_dialogue]"

    menu:
        "Mmm, fill me up!":

            jump action_clean_event_sex_ass_cum_want
        "Mmm. Pull out and cover me with your cum!":

            if player.check_speech(2):
                jump action_clean_event_sex_cum_pullout
            else:

                jump action_clean_event_sex_ass_cum_notwant

label action_clean_event_sex_anal_switch:
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    $ if_showing("sb_doggy2", "pokeasshold")
    $ if_showing("sb_doggy2", "pokeass")
    "[rlist.having_sex_vag_to_ass_switch]"

    if player.want_sexlocation == 2:
        pc "Finally aiming for the hole I asked for? ♥"
    else:
        pc "[rlist.having_sex_tease_ass_suprise]"

    "[rlist.having_sex_vag_to_ass]"
    $ player.sex_anal(punter, quest_cleaner)
    $ if_showing("sb_onfours", "ass", "sb_ontop", "doggy", "sb_doggy1", "anal", "sb_doggy2", "insideass")
    "[rlist.having_sex_penetrate_ass_slow]"
    pc "[rlist.having_sex_yes]"
    jump action_clean_event_sex_anal_jump

label action_clean_event_sex_vag_cum_want:
    pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    pervert "[rlist.having_sex_man_cum_inside_vag_dialogue]"

    $ player.sex_cum(punter, "inside", quest_cleaner)

    "[rlist.having_sex_cumming_inside_vag_want_action]"
    $ if_showing("sb_ontop", "up happy", "sb_doggy1", "oh", "sb_doggy2", "happy straight")
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"

    jump action_clean_event_sex_end

label action_clean_event_sex_vag_cum_notwant:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    pervert "[rlist.having_sex_man_cum_inside_vag_dialogue]"

    $ player.sex_cum(punter, "inside", quest_cleaner)

    "[rlist.having_sex_cumming_inside_vag_notwant_action]"
    $ if_showing("sb_ontop", "back shock", "sb_doggy1", "shock", "sb_doggy2", "shock squint angry")
    pervert "Ahh yes."
    pc "Ah what are you doing?"

    pc "[rlist.having_sex_came_inside_vag_notwant_reaction]"
    pervert "[rlist.having_sex_came_inside_vag_notwant_excuse]"
    $ if_showing("sb_ontop", "surprise", "sb_doggy1", "neutral", "sb_doggy2", "frown worried")
    pc "*Sigh*"
    jump action_clean_event_sex_end

label action_clean_event_sex_cum_pullout:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    pervert "[rlist.having_sex_cumming_pullout_man_dialogue]"

    $ if_showing("sb_onfours", "poke", "sb_doggy1", "poke", "sb_doggy2", "cum")
    $ player.sex_cum(punter, "ass", quest_cleaner)
    "[rlist.having_sex_cumming_pullout_action]"
    pervert "Ahh yes!"
    pc "[rlist.having_sex_cumming_pullout_reaction]"

    jump action_clean_event_sex_end

label action_clean_event_sex_cum_pullout_anal:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    pervert "[rlist.having_sex_pc_cum_pullout_ask_anal_reply]"
    jump action_clean_event_sex_anal_switch

label action_clean_event_sex_cum_pullout_poke:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    pervert "[rlist.having_sex_cumming_pullout_man_dialogue]"
    $ if_showing("sb_onfours", "poke", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    $ player.sex_cum(punter, "pullout", quest_cleaner)
    "[rlist.having_sex_cumming_pullout_poke_action]"
    if player.want_pullout:
        $ if_showing("sb_ontop", "back shock", "sb_doggy1", "shock", "sb_doggy2", "shock squint angry")
        pc "[rlist.having_sex_cumming_pullout_poke_reaction]"
        $ if_showing("sb_onfours", "poke", "sb_doggy1", "poke", "sb_doggy2", "cum")

        "[rlist.having_sex_cumming_pullout_poke_reaction_followup]"
        pc "[rlist.having_sex_came_inside_vag_notwant_reaction]"
    else:

        pc "[rlist.having_sex_came_inside_vag_want]"
    jump action_clean_event_sex_end

label action_clean_event_sex_ass_cum_want:
    pc "[rlist.having_sex_pc_cum_inside_ass_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    pervert "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    $ if_showing("sb_ontop", "up happy", "sb_doggy1", "oh", "sb_doggy2", "happy straight")
    $ player.sex_cum(punter, "anal", quest_cleaner)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    pervert "Ahh yes."
    pc "[rlist.having_sex_came_inside_ass_want]"
    jump action_clean_event_sex_end

label action_clean_event_sex_ass_cum_notwant:
    pc "[rlist.having_sex_pc_cum_ass_pullout_ask]"
    pervert "[rlist.having_sex_man_cum_inside_ass_dialogue]"

    $ player.sex_cum(punter, "anal", quest_cleaner)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    pervert "Ahh yes."
    $ if_showing("sb_ontop", "surprise", "sb_doggy1", "neutral", "sb_doggy2", "frown worried")
    pc "[rlist.having_sex_came_inside_ass_notwant_reaction]"
    pervert "[rlist.having_sex_came_inside_ass_notwant_excuse]"
    pc "*Sigh*"
    pc "Whatever..."
    jump action_clean_event_sex_end

label action_clean_event_sex_end:
    $ if_showing("sb_onfours", "poke", "sb_doggy1", "poke", "sb_doggy2", "cum")
    pervert "That was fun."
    $ if_showing("sb_onfours", "noman", "sb_ontop", "no_doggy", "sb_doggy1", "noman", "sb_doggy2", "noman")
    "The guy pulls his trousers up and walks away without another word."
    $ renpy.scene()
    with dissolve
    $ pc_dress()
    pcm "Right... Well, better get back to it."
    jump action_clean_event_picker

label action_clean_event_sex_forcesex:
    if player.has_perk(perk_freeuse):
        $ player.face_angry()
        with hpunch
        pc "Ugh! Not so rough!"
        $ player.face_cry()
        if player.selling:
            pervert "Stop struggling, I paid to fuck you!"
        else:
            pervert "This will go a lot easier if you stop struggling!"
        pc "I'm not struggling you idiot!"
        "He continues to pin me down as he thrusts inside me. Fucking me with increased vigour."
        pervert "Mmmmm, such a lovely young slut."
        pc "..."
        pervert "Ahhhhhh!"
        $ player.sex_cum(rapist, "inside", quest_cleaner)
        pervert "Ahhh yes!"
        pc "Had your fun?"
        $ if_showing("sb_onfours", "noman", "sb_ontop", "no_doggy", "sb_doggy1", "noman", "sb_doggy2", "noman")
        "Once he is finished inside me, he quickly pulls out, puts his trousers on and leaves. Leaving me alone."
        $ renpy.scene()
        with dissolve
        pc "Idiot."

    elif player.check_fight(2):
        $ player.sex_end()
        $ player.face_angry()
        $ if_showing("sb_onfours", "noman", "sb_ontop", "no_doggy", "sb_doggy1", "noman", "sb_doggy2", "noman", trans=vpunch)
        "I jump away as he tried so grab hold of me, but he doesn't manage to keep a grip on me. Realising his predicament, he quickly pulls his trousers up and runs away."
        $ renpy.scene()
        with dissolve
        pc "What the fuck! What a cunt!"
        $ player.face_cry()
        if player.has_perk([perk_whore, perk_numb]):
            $ player.sex_end()
            pcm "Fuck that was a close one. Just trying to clean and these fuckers do that?"
            pc "*Phew*"
            jump action_clean_event_picker
        pc "*SOB*"
        if player.virgin_pregcheck:
            pc "My first time comes to this..."
        pc "I can't believe that just happened..."
        pc "..."
    else:

        $ player.face_angry()
        with hpunch
        "I try to worm my way out of his grasp, but I am not strong enough and he pulls me closer while fucking me."
        $ player.face_cry()
        pc "Fuck!"
        if player.selling:
            pervert "Stop struggling, I paid to fuck you!"
        else:
            pervert "This will go a lot easier if you stop struggling!"
        pc "Fuck you!"
        "He continues to pin me down as he thrusts inside me. Fucking me with increased vigour knowing that I can't push him off."
        if player.virgin_pregcheck:
            pervert "Mmmmm, such a lovely young slut. And is that blood? Were you a virgin?"
            pervert "Oh man having popped the cherry of some little teenage slut. I will have to tell everyone."
            pc "*SOB*"
        else:
            pervert "Mmmmm, such a lovely young slut."
            pc "*SOB*"
        pervert "Ahhhhhh!"
        pc "*SOB*"
        $ player.sex_cum(rapist, "inside", quest_cleaner)
        pervert "Ahhh yes!"
        pc "*SOB*"
        $ if_showing("sb_onfours", "noman", "sb_ontop", "no_doggy", "sb_doggy1", "noman", "sb_doggy2", "noman")
        "Once he is finished inside me, he quickly pulls out, puts his trousers on and leaves. Leaving me alone."
        $ renpy.scene()
        with dissolve
        pcm "Bastard!"
        pc "*SOB*"
        if player.virgin_pregcheck:
            pc "My first time comes to this..."
        pc "I can't believe that just happened..."
        pc "..."
    jump action_clean_event_done_change

label action_clean_event_sex_cumrun:
    $ player.sex_forced(rapist, quest_cleaner)
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold", trans=vpunch)
    $ player.face_shock()
    pc "Ah what the hell?"
    "I feel the guy furiously masturbating while holding onto me."
    if player.has_perk(perk_freeuse):
        pcm "Right then..."
        if danger_gen(20,1) and c.skirt:
            if c.pants:
                "He grabs at my pants and tries to rip them off."
                $ wardrobe.drop(globals()["item_pants_" + str(c.pants)])
                pc "Oi! They cost me money!"
            $ if_showing("sb_onfours", "vag up", "sb_doggy1", "grit vag", "sb_doggy2", "head_back shock squint angry insidevag", trans=hpunch)
            $ player.sex_vag(streetpervert, quest_cleaner)
            "[rlist.having_sex_penetrate_vag_forced]"
            jump action_clean_event_sex_forcesex
        $ player.sex_cum(rapist, "ass", quest_cleaner)
        pervert "Nnnnggg!!"
        $ if_showing("sb_onfours", "noman", "sb_ontop", "no_doggy", "sb_doggy1", "noman", "sb_doggy2", "noman")
        $ player.face_annoyed()
        pcm "Just cums then runs?"
        $ renpy.scene()
        with dissolve
        pcm "Useless idiot!"
        jump action_clean_event_picker
    else:

        pc "Get off!"
        if player.check_fight(2):
            $ player.sex_end()
            $ if_showing("sb_onfours", "noman", "sb_doggy1", "noman", "sb_doggy2", "noman", trans=vpunch)
            "I manage to wiggle out of his grasp and prepare to get up."
            $ renpy.scene()
            with dissolve
            pcm "Where did he go? Ran away? Arsehole!"
            jump action_clean_event_picker
        if danger_gen(20,1) and c.skirt:
            if c.pants:
                "He grabs at my pants and tries to rip them off."
                $ wardrobe.drop(globals()["item_pants_" + str(c.pants)])
                pc "Oi!"
            $ if_showing("sb_onfours", "vag up", "sb_doggy1", "grit vag", "sb_doggy2", "head_back shock squint angry insidevag", trans=hpunch)
            $ player.sex_vag(rapist, quest_cleaner)
            "[rlist.having_sex_penetrate_vag_forced]"
            jump action_clean_event_sex_forcesex
        $ player.sex_cum(rapist, "ass", quest_cleaner)
        pervert "Nnnnggg!!"
        pc "Ah fuck you!"
        $ if_showing("sb_onfours", "noman", "sb_ontop", "no_doggy", "sb_doggy1", "noman", "sb_doggy2", "noman")
        $ player.face_angry()
        pc "*Tsk*"
        $ renpy.scene()
        with dissolve
        pc "Arsehole!"
        jump action_clean_event_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
