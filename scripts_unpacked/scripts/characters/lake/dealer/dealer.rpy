init python:
    def lake_dealer_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        if not lake_dealer.has_met:
            cur_location = None
        
        elif t.time_from_to(20.00, 03.00):
            cur_location = loc_beach_rocks
        
        return npc_here_check(location, cur_location, where)

layeredimage lake_dealer:
    at sprite_highlight("lake_dealer")
    always "lake_dealer_body"
    group gen auto:
        attribute pants default
    group coat auto:
        attribute closed default
        attribute null

label lake_dealer_meet:
    show lake_dealer at right1 with dissolve
    lake_dealer.name "Pretty girl. Think you gonna want what I got."
    $ player.face_worried()
    pc "Err, no thanks..."
    lake_dealer.name "Got sweets to make you happy and ones to make babies go away."
    pcm "Wait what? Babies go away?"
    pc "What are you talking about?"
    lake_dealer.name "Talking about good stuff. The kind you can't get in other places."
    show lake_dealer open with dissolve
    pc "Riight... Okay, whatev..."
    lake_dealer.name "Av a look."
    call screen inventory_itemshop_screen(lake_dealer.inv)
    $ player.face_surprised()
    pc "Err, ok. Wow."
    show lake_dealer closed with dissolve
    lake_dealer.name "Ya like? Come see me when it's dark near the boats fer some more."
    pc "Okay."
    hide lake_dealer with dissolve
    jump travel

label lake_dealer_shop:
    show lake_dealer at right1 with dissolve
    $ tempname = lake_dealer
    $ quest_temp = None
    $ npc_race_picker(lake_dealer)
    lake_dealer.name "Can't keep away eh?"
    if lake_dealer.lust == 100:
        show lake_dealer open penis with dissolve
        if not "shown_penis" in lake_dealer.list:
            call lake_dealer_shop_expose_firsttime from _call_lake_dealer_shop_expose_firsttime
        elif "shown_penis_ran_away" in lake_dealer.list:
            $ remove_from_list(lake_dealer.list, "shown_penis_ran_away")
            lake_dealer.name "Came for another look?"
            pc "Ugh..."
            pc "Just show me what you are selling."
            lake_dealer.name "No problem."
        elif not numgen(0, 2) or (lake_dealer.sex or lake_dealer.osex):
            if lake_dealer.sex or lake_dealer.osex:
                lake_dealer.name "Want to help out and get a discount?"
            else:
                lake_dealer.name "Suck it while you shop and I'll knock the price down."
                if player.pregnancy >= 2:
                    lake_dealer.name "Or we can do something much nicer for a better price."
                else:
                    lake_dealer.name "Or we can do something much nicer and I'll even throw in a free pill."
                pc "Err..."
            if player.check_whore():
                jump lake_dealer_shop_discount
    else:

        show lake_dealer open with dissolve
    call screen inventory_itemshop_screen(lake_dealer.inv)
    if lake_dealer.lust == 100 and "penis" in renpy.get_attributes("lake_dealer"):
        if not numgen(0,20):
            if not numgen(0, 20):
                lake_dealer.name "Nnng!"
                $ player.sex_cum(lake_dealer, "face")
                $ player.face_shock()
                $ player.eye = 3
                pc "Ah! Fuck!"
                $ player.face_annoyed()
                lake_dealer.name "Mmmmm... Sorry, couldn't help it."
                $ player.face_eye = 3
                pc "In my fucking eye!"
                $ player.face_eye = 2
                pc "How the hell did you even shoot it that far?"
                $ player.face_eye = 3
                pc "Idiot!"
                $ player.face_eye = 2
            else:
                lake_dealer.name "Nnng!"
                $ player.sex_cum(lake_dealer, "belly")
                $ player.face_shock()
                pc "Ah! Pervert!"
                $ player.face_annoyed()
                lake_dealer.name "Mmmmm... Sorry, couldn't help it."
        else:

            $ lake_dealer.add_lust(-40)
    show lake_dealer closed with dissolve
    lake_dealer.name "See ya soon."
    hide lake_dealer with dissolve
    jump travel

label lake_dealer_shop_discount_ask:
    show lake_dealer at right1 with dissolve
    pc "How about something fun for a discount?"
    if lake_dealer.want_sex():
        lake_dealer.name "Sounds good to me."
        show lake_dealer open penis with dissolve
        jump lake_dealer_shop_discount
    else:
        lake_dealer.name "Sorry love, not in the mood for that."
        show lake_dealer open with dissolve
        lake_dealer.name "Y' can still shop normally."
        call screen inventory_itemshop_screen(lake_dealer.inv)
        lake_dealer.name "Cheers [rlist.name_cute]."
        hide lake_dealer with dissolve
        jump travel

label lake_dealer_shop_discount:
    $ temp_var_2 = lake_dealer.inv.value()
    $ temp_var_3 = False
    $ npc_race_picker(lake_dealer)
    if player.has_perk(perk_freeuse):
        pc "Sure. I mean, no! Err..."
        pc "We can fuck but no discount."
        lake_dealer.name "Huh?"
        " I just turn around and bend over."
        jump lake_dealer_shop_sex
    menu:
        "Sure, why not?":
            $ player.selling = True
            $ temp_var_3 = True
            jump lake_dealer_shop_blowjob
        "Bend over" if player.has_perk([perk_whore, perk_sucu]):
            pc "Sure, give me some cheap stuff."
            $ player.selling = True
            $ temp_var_1 = True
            jump lake_dealer_shop_sex
        "No thanks":

            pc "Think I'll pass."
            lake_dealer.name "No worries."
            show lake_dealer closed with dissolve
            lake_dealer.name "See ya soon."
            hide lake_dealer with dissolve
            jump travel

label lake_dealer_shop_expose_firsttime:
    $ add_to_list(lake_dealer.list, "shown_penis")
    if player.has_perk(perk_exhibitionist):
        $ player.face_happy()
        pc "Oooh, you like to show off too?"
        lake_dealer.name "Err, yeah..."
        pc "Nice!"
        lake_dealer.name "This is not the reaction I usually get."
        pc "Should I run off screaming to make you feel better?"
        lake_dealer.name "Hah, no."
        pc "Okay then. So let's see what you have."
    elif player.check_sex_agree(2):
        pc "Ah, err... Okay then. You aware you cock is out and pointing at me?"
        lake_dealer.name "Yup."
        pc "Okay then..."
        pc "Right..."
        pc "So I am shopping with your cock in my face then?"
        lake_dealer.name "Yup."
        pc "Right."
    else:
        pc "Ah!"
        hide lake_dealer with vpunch
        $ walk(loc_from, trans=hpunch)
        pcm "Ugh, can't even buy dodgy shit from a shady dealer..."
        $ add_to_list(lake_dealer.list, "shown_penis_ran_away")
        jump travel
    return

label lake_dealer_shop_blowjob:
    $ npc_race_picker(lake_dealer)
    pc "Okay then..."
    $ renpy.show(random(["sb_blowjob down", "sb_spitroast down"]))
    hide lake_dealer
    with dissolve
    "He's already got his cock out so I get down and prepare to suck him off."
    pc "[rlist.handjob_touch_cock]"
    $ player.sex_oral(lake_dealer)
    $ if_showing("sb_blowjob", random(["suck down", "suck 2h down"]), "sb_spitroast", "blow down", "sb_layblow", "down blow")
    "[rlist.blowjob_start_suck]"
    $ if_showing("sb_blowjob", "up", "sb_spitroast", "up", "sb_layblow", "forward")
    pc "[rlist.blowjob_muffle]"

    call screen inventory_itemshop_screen(lake_dealer.inv, 20)

    lake_dealer.name "[rlist.having_sex_man_close_dialogue]"
    $ if_showing("sb_blowjob", "angry closed", "sb_spitroast", "angry closed")
    lake_dealer.name "[rlist.blowjob_cum_mouth_man_dialogue]"
    $ player.sex_cum(lake_dealer, "mouth")

    "[rlist.blowjob_cum_mouth]"
    lake_dealer.name "[rlist.having_sex_man_yes]"
    pc "[rlist.blowjob_muffle]"
    $ if_showing("sb_blowjob", "face 1h up happy ub", "sb_spitroast", "straight up neutral mast", "sb_layblow", "forward")
    $ if_showing("sb_blowjob", "laugh", "sb_spitroast", "happy")
    pc "[rlist.blowjob_cum_mouth_swallow_reaction]"
    lake_dealer.name "[rlist.blowjob_cum_mouth_swallow_reaction_man]"
    $ renpy.scene()
    show lake_dealer at right1
    jump lake_dealer_shop_sex_end

label lake_dealer_shop_sex:
    $ npc_race_picker(lake_dealer)
    $ renpy.scene()
    $ renpy.show(renpy.random.choice(["sb_onfours", "sb_ontop", "sb_doggy1", "sb_doggy2"]))
    with dissolve
    "[rlist.foreplay_preparesex_fours]"
    $ player.sex_location_offer(0, sex_vag_want="lake_dealer_shop_sex_vag", sex_anal="lake_dealer_shop_sex_anal", who=lake_dealer)

label lake_dealer_shop_sex_vag:
    $ c.pants = 0
    $ c.bottom = 0
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_penetrate_vag_slow]"
    $ if_showing("sb_onfours", "up vag", "sb_ontop", "back ag", "sb_doggy1", "ag vag head_down", "sb_doggy2", "head_back happy wink insidevag", "sb_assup", "sex")
    $ player.sex_vag(lake_dealer)
    $ player.face_excited()
    "[rlist.having_sex_action]"

    call screen inventory_itemshop_screen(lake_dealer.inv, If(player.has_perk(perk_freeuse), 0, 40))

    lake_dealer.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(lake_dealer, "inside")
    "[rlist.having_sex_cumming_inside_vag_want_action]"
    $ if_showing("sb_ontop", "up happy", "sb_doggy1", "oh", "sb_doggy2", "happy straight")
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"
    $ if_showing("sb_onfours", "poke", "sb_doggy1", "poke", "sb_doggy2", "cum")
    lake_dealer.name "That was fun."
    $ if_showing("sb_onfours", "noman", "sb_ontop", "no_doggy", "sb_doggy1", "noman", "sb_doggy2", "noman")
    $ renpy.scene()
    show lake_dealer at right1
    with dissolve
    jump lake_dealer_shop_sex_end

label lake_dealer_shop_sex_anal:
    $ c.pants = 0
    $ c.bottom = 0
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    "[rlist.having_sex_tease_vag]"
    pc "Fuck me in the ass. It's safer than taking a pill."
    lake_dealer.name "Okay."
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    $ if_showing("sb_doggy2", "pokeasshold")
    $ if_showing("sb_doggy2", "pokeass")

    "[rlist.having_sex_vag_to_ass_switch]"

    $ player.sex_anal(lake_dealer)
    $ player.face_excited()
    $ if_showing("sb_onfours", "ass", "sb_ontop", "doggy", "sb_doggy1", "anal", "sb_doggy2", "insideass")

    "[rlist.having_sex_penetrate_ass_slow]"
    lake_dealer.name "Ahhhhhh so warm."

    call screen inventory_itemshop_screen(lake_dealer.inv, If(player.has_perk(perk_freeuse), 0, 40))

    lake_dealer.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    $ if_showing("sb_ontop", "up happy", "sb_doggy1", "oh", "sb_doggy2", "happy straight")
    $ player.sex_cum(lake_dealer, "anal")
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    lake_dealer.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_ass_want]"
    $ if_showing("sb_onfours", "poke", "sb_doggy1", "poke", "sb_doggy2", "cum")
    lake_dealer.name "That was fun."
    $ if_showing("sb_onfours", "noman", "sb_ontop", "no_doggy", "sb_doggy1", "noman", "sb_doggy2", "noman")
    $ renpy.scene()
    show lake_dealer at right1
    with dissolve
    jump lake_dealer_shop_sex_end

label lake_dealer_shop_sex_end:
    $ pc_dress()
    if lake_dealer.inv.value() == temp_var_2:
        if temp_var_3:
            lake_dealer.name "You didn't even buy anything. Just wanted to suck on my cock?"
        else:
            lake_dealer.name "You didn't even buy anything. Just wanted to fuck?"
        pc "Shush!"
        if not lake_dealer.can_sex:
            lake_dealer.name "Can ask next time. I'm not gonna turn down someone like you."
            $ lake_dealer.can_sex = True
        else:
            lake_dealer.name "No problem here."
        if temp_var_1:
            lake_dealer.name "Anyway, here is your pill."
            $ inv.take(item_map_pill)
            pc "Thanks."
        if not numgen(0,10):
            lake_dealer.name "You can have one of these since you are such a slut. Have fun with it."
            $ inv.take(item_lebo)
            pc "Oooh..."
    elif temp_var_1:
        lake_dealer.name "Cheers [rlist.name_cute]. Here you go, as promised."
        $ inv.take(item_map_pill)
        pc "Thanks."
    else:
        lake_dealer.name "Cheers [rlist.name_cute]."
    hide lake_dealer with dissolve
    jump travel

label lake_dealer_sex_ask:
    show lake_dealer at right1 with dissolve
    pc "Wanna have some fun in the sand?"
    if lake_dealer.want_sex():
        lake_dealer.name "Of course I do."
        $ event_end_interrupt_label = "lake_dealer_sex_end"
        $ npc_race_picker(lake_dealer)
        $ tempname = lake_dealer
        $ quest_temp = None
        jump whore_street_sex_start_picker
    else:
        lake_dealer.name "Hard to keep up with you beach sluts. Sorry [rlist.name_cute]."
        pc "Oh..."
        hide lake_dealer with dissolve
        jump travel

label lake_dealer_sex_end:
    $ renpy.scene()
    show lake_dealer at right1
    with dissolve
    lake_dealer.name "Love the beach. You sluts are the best."
    pc "Thanks."
    $ pc_dress()
    hide lake_dealer with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
