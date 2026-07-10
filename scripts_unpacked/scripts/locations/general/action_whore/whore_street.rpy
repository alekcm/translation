label whore_street_mira_quest_start_setter:
    $ tempname = punter
    $ quest_temp = quest_mira_missing
    $ npc_race_picker()
    jump whore_street_mira_quest_checker

label whore_street_start_setter:
    $ tempname = punter
    $ quest_temp = quest_whore
    $ npc_race_picker()
    jump whore_street_checker





label whore_street_mira_quest_checker:
    if not dis(dis_truckstop):
        pcm "I doubt I will get any info round here. I need to head to the truck stop or highway."
        jump travel
    jump whore_street_checker

label whore_street_checker:
    if loc(loc_motel_pinkroom):
        jump pinkroom_advertise_start
    elif player.cum_visible:
        pcm "I have cum on me. Doubt anyone will want to buy me until I clean up."
        if dis(dis_truckstop):
            pcm "I can probably rent a room in the motel and use it's showers."
        jump travel
    elif dis_cur == dis_haven:
        jump dis_haven_whore
    elif dis(dis_walk):
        pcm "There is no one here, I should find somewhere better."
        jump travel
    elif loc_cur in dis_home.locs:
        pcm "Need to actually go out to do that."
        jump travel
    elif dis(dis_checkpoint) and not dis(dis_junkyard):
        pcm "Not many customers here. I'm most likely just going to end up arrested if I try anything here."
        jump travel
    elif player.allure < 250:
        pcm "Not really dressed sexy enough to draw attention so might find it hard to get customers."
        if not "party" in tab_top:
            pcm "I should swap to my party gear and make sure it's revealing."
        else:
            pcm "I should make sure my clothes are revealing enough to draw attention."
    elif dis_cur == dis_school and not "school" in tab_top:
        pcm "If I am going to sell myself round here, I could probably make more if I put my uniform on. The perverts would love it."

    jump whore_street_start

label whore_street_start:
    if not loc_cur.can_whore:
        pcm "I should go somewhere better."
        $ travel_whore_location()
    $ show_whore_image()
    "[rlist.whore_start_available]"
    $ working(10)
    if whore_customer_weight():
        jump whore_street_customer_pick_location
    else:
        call whore_street_no_customer_tombola from _call_whore_street_no_customer_tombola
    $ quest_mira_intel_trigger("quest_mira_missing_intel_whore_whores_picker")
    pcm "[rlist.whore_start_waiting]"
    $ show_whore_image()
    "[rlist.whore_start_available]"
    $ working(10)
    if whore_customer_weight():
        jump whore_street_customer_pick_location
    else:
        call whore_street_no_customer_tombola from _call_whore_street_no_customer_tombola_1

    $ quest_mira_intel_trigger("quest_mira_missing_intel_whore_whores_picker")
    pcm "[rlist.whore_start_waiting]"
    $ show_whore_image()
    "[rlist.whore_start_available]"
    $ working(10)
    if whore_customer_weight():
        jump whore_street_customer_pick_location
    else:
        call whore_street_no_customer_tombola from _call_whore_street_no_customer_tombola_2

    $ quest_mira_intel_trigger("quest_mira_missing_intel_whore_whores_picker")
    pcm "[rlist.whore_start_waiting]"
    $ renpy.scene()
    with dissolve
    jump travel

label whore_street_freeuse_toggle:
    if not player.has_perk([perk_sucu, perk_slut, perk_bimbo, perk_broken]):
        pcm "I'm not going to just give it away for free."
        $ player.remove_perk(perk_freeuse)
    elif player.has_perk(perk_freeuse):
        pcm "I need to start charging money instead of giving it away."
        $ player.remove_perk(perk_freeuse)
    else:
        pcm "I should stop charging money for sex and just have some fun."
        $ player.add_perk(perk_freeuse)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
