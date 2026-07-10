label whore_street_customer_whatsex:
    if player.has_perk(perk_freeuse):
        pc "I do this for fun so keep your money."
        tempname.name "Oh wow. Okay then."
        return
    pc "What do you want me to do for that?"
    call expression WeightedChoice([

    ("whore_street_customer_whatsex_quickhand", 20),
    ("whore_street_customer_whatsex_quickblow", 20),
    ("whore_street_customer_whatsex_quickfuck", 20),
    ("whore_street_customer_whatsex_continue", 250),
    ]) from _call_expression_16
    return

label whore_street_customer_whatsex_consider:
    pcm "Should I do that for £[player.soldprice]?"
    menu:
        "Go with him":
            pc "Okay, let's go."
            return
        "Back out of it":
            pc "Sorry mate, I don't feel comfortable with that."
            tempname.name "No? Err... Okay..."
            "The guy walks away without looking back."
            pcm "..."
            jump travel

label whore_street_customer_whatsex_quickhand:
    $ player.soldrequest = "hand"
    tempname.name "Come round back and you can wank me off."
    call whore_street_customer_whatsex_consider from _call_whore_street_customer_whatsex_consider
    jump whore_street_customer_pick_location_isolate

label whore_street_customer_whatsex_quickblow:
    $ player.soldrequest = "blow"
    tempname.name "Lets go round back and you can suck me off."
    call whore_street_customer_whatsex_consider from _call_whore_street_customer_whatsex_consider_1
    jump whore_street_customer_pick_location_isolate

label whore_street_customer_whatsex_quickfuck:
    $ player.soldrequest = "vag"
    tempname.name "Lets go round back so I can fuck you."
    call whore_street_customer_whatsex_consider from _call_whore_street_customer_whatsex_consider_2
    jump whore_street_customer_pick_location_isolate

label whore_street_customer_whatsex_continue:
    $ player.soldrequest = ""
    tempname.name "I want to have some fun darling."
    pcm "That's not really an answer..."
    call whore_street_customer_whatsex_consider from _call_whore_street_customer_whatsex_consider_3
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
