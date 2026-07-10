label felix_talk_test:
    show felix at right1 with dissolve
    felix.name "Talk test. I am here."
    hide felix with dissolve
    jump travel

label felix_gift_picker:
    show felix at right1 with dissolve
    $ temp_var_1 = True
    felix.name "Have something for me?"
    call screen inventory_gift_choice([item_mag_ent, item_mag_porn])
    if buy_inv.qty(item_energydrink):
        if felix.inv.qty(item_energydrink) >= 3:
            felix.name "Already have a few of those [name]. But thanks for thinking of me."
            $ temp_var_1 = False
        else:
            felix.name "Oh? This will come in good for those late nights."
    elif buy_inv.qty(item_energyfood):
        if felix.inv.qty(item_energyfood) >= 3:
            felix.name "Already have a few of those [name]. But thanks for thinking of me."
            $ temp_var_1 = False
        else:
            felix.name "Oh? This will come in good for those late nights."
    elif buy_inv.qty(item_mag_ent) or buy_inv.qty(item_mag_porn):
        if log.interactive("photo_first_01"):
            $ log.find("photo_first_01")


        felix.name "Oh, thanks [name]."
    else:
        show felix frown
        felix.name "No problem, another time."
    if temp_var_1:
        $ felix._love += (inv_value(buy_inv) / 4)
        $ inv_transfer(buy_inv, felix.inv)
    else:
        $ inv_transfer(buy_inv, inv)
    if log.interactive("photo_first_02"):
        jump quest_photo_startingout_magazines
    show felix smile
    jump felix_talk_end

label felix_sell_photos:
    if not has_photos_to_sell():
        pcm "I don't have anything new to sell him"
        jump travel
    show felix at right1 with dissolve
    pc "I have some pictures if you are interested."
    felix.name "Sure, let's have a look."
    $ show_notif_popup("Gave over polaroids")
    if felix_not_have_photo_type("slutty"):
        felix.name "Oh, these ones you are wearing quite revealing clothes."
        pc "Yeah, might fit well with your \"innocent\" magazine."
    if felix_not_have_photo_type("underwear"):
        felix.name "Photos in your underwear?"
        pc "Yup."
        felix.name "Will be able to make use of these."
    if felix_not_have_photo_type("nude"):
        felix.name "Some nude photos in here as well. They will make some nice money."
        pc "Mmmm."
    if felix_not_have_photo_type("porn"):
        felix.name "Err, there are some pretty naughty photos here..."
        felix.name "You sure you are okay selling them?"
        pc "More money for those right?"
        felix.name "Well, yeah."
        pc "Good for me then."
        felix.name "Okay..."
    if photo_has_others():
        felix.name "Hmm, there are other people in these ones. Is that ok?"
        pc "Does it matter?"
        felix.name "Err... I don't want angry people coming to my door looking to kick my arse."
        pc "Then don't use them. Or hide the face. Whatever."
        felix.name "Right..."
    felix.name "Well, yeah I'll take these. Here you go."
    $ felix_sell_photos()
    pc "Thanks."
    felix.name "Come back if you have more."
    hide felix with dissolve
    jump travel

label felix_talk_end:
    $ relax(20, felix)
    $ dialouge = renpy.random.choice([
    "I hang out talking and joking about random stuff.",
    "I hang out for a while chatting and joking around about random topics.",
    "We hang out chatting and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    hide felix with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
