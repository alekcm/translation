init python:
    def scav_clothes_caught():
        working(10)
        if numgen(0, 2000) < danger_weight():
            renpy.jump("random_event_generic_danger")

    def craft_scrap_clothes():
        if c.nude and inv.qty(item_scrap_clothes) >= 4:
            inv.drop(item_scrap_clothes, 4)
            wardrobe.take(renpy.random.choice([item_outfit_9]), dress=True)
        elif c.cansee_vagina:
            inv.drop(item_scrap_clothes, 2)
            wardrobe.take(renpy.random.choice([item_bottom_14, item_bottom_24, item_bottom_25]), dress=True)
        elif c.cansee_breasts:
            inv.drop(item_scrap_clothes, 1)
            wardrobe.take(renpy.random.choice([item_top_21, item_top_29, item_bra_8]), dress=True)
        else:
            inv.drop(item_scrap_clothes, 2)
            wardrobe.take(renpy.random.choice([item_bottom_14, item_bottom_24, item_bottom_25, item_top_21, item_top_29, item_bra_8]), dress=True)

label scav_clothes_jump:
    if tab_top == "temp_outfit":
        $ pc_dress_event(tab_top_backup)
        jump travel
    if dis(dis_home_area) and not loc_kitchen.locked:
        $ walk(loc_bedroom)
        pcm "I can just wear stuff from my wardrobe."
        jump travel

    elif robin_here(dis_cur.locs) and robin.love > 40 and not dis(dis_residential):
        jump robin_ask_clothes
    elif jaylee_here(dis_cur.locs) and jaylee.love > 40:
        jump jaylee_ask_clothes
    elif dan_here(dis_cur.locs):
        jump soccer_ask_clothes
    elif mira_here(dis_cur.locs) and "pc_knows_whore" in mira.list:
        jump mira_ask_clothes

    if c.nude:
        pcm "I can't be going around naked. I need to find something to wear."
    elif c.cansee_breasts:
        pcm "I can't be going around with my tits out. I need to find something to wear."
    elif c.cansee_vagina:
        pcm "I can't be going around with my arse out. I need to find something to wear."
    else:
        pcm "I need to find something to cover myself with."
    $ travel_isolate()
    pcm "..."
    if inv.qty(item_scrap_clothes) > 2:
        pcm "I have some ratty clothes with me I can probably make use of..."
        jump scav_clothes_craft
    pcm "Need to find something laying around I can make use of..."
    $ scav_clothes_caught()
    pcm "Let's see..."
    pcm "..."
    jump scav_clothes_look

label scav_clothes_look:
    $ scav_clothes_caught()
    if not numgen(0,1):
        $ player.face_happy()
        $ dialouge = WeightedChoice([
        ("Ah, something  can use...", 1),
        ("Yes! I can use this.", 1),
        ("Nice, this is useful.", 1),
        ("This will do.", 1),
        ("Got something!", 1),
        ])
        pcm "[dialouge]"
        $ inv.take(item_scrap_clothes, numgen(1,2))
    else:
        $ player.face_annoyed()
        $ dialouge = WeightedChoice([
        ("Shit, can't find anything...", 1),
        ("Come on, there must be something.", 1),
        ("Fuck, nothing.", 1),
        ("Ah come on, I can't find a damn thing.", 1),
        ("Nothing...", 1),
        ])
        pcm "[dialouge]"
    $ scav_clothes_caught()
    if inv.qty(item_scrap_clothes) > 2:
        jump scav_clothes_craft
    else:
        jump scav_clothes_look

label scav_clothes_craft:
    pcm "Hmmm, let's see..."
    "I try to stay hidden while cobbling something together to wear."
    pcm "Hope no one sees me while I am doing this..."
    $ scav_clothes_caught()
    "I am managing to get something together that looks like clothes..."
    pcm "Almost..."
    $ scav_clothes_caught()
    pcm "..."
    pcm "Done!"
    $ craft_scrap_clothes()
    pcm "There we go..."
    if c.cansee_breasts and inv.qty(item_scrap_clothes) > 2:
        pcm "Now for my top..."
        jump scav_clothes_craft
    else:
        jump travel

label jaylee_ask_clothes:
    $ walk(jaylee_here(class_loc=True))
    show jaylee at right1 with dissolve
    pc "Err, can I borrow some clothes off you?"
    jaylee.name "You asking me for clothes? Haha!"
    pc "Yeah, I kinda lost mine..."
    jaylee.name "Hmmm. Tempted to refuse just so I can see you prance around like that."
    jaylee.name "Suppose I can dig up some spares though."
    if c.cansee_breasts:
        $ wardrobe.take(item_top_40, notif=True, dress=True)
    if c.cansee_vagina:
        $ wardrobe.take(item_bottom_32, notif=True, dress=True)
    pc "Thanks! Don't need to be showing everything off now."
    jaylee.name "Yeah..."
    jump jaylee_talk_end

label robin_ask_clothes:
    $ walk(robin_here(class_loc=True))
    show robin at right1 with dissolve
    pc "Err, can I borrow some clothes off you?"
    robin.name "What? You? Don't you have a massive wardrobe?"
    pc "My stuff, kinda ended up going missing."
    robin.name "Really? Ugh."
    robin.name "Sure, I think I have something."
    if c.cansee_breasts:
        $ wardrobe.take(item_coat_10, notif=True, dress=True)
    if c.cansee_vagina:
        $ wardrobe.take(item_bottom_26, notif=True, dress=True)
    pc "Thanks! Don't need to be showing everything off now."
    robin.name "Yeah..."
    jump robin_talk_end

label soccer_ask_clothes:
    if any([nate_here(loc_school_field_back), drake_here(loc_school_field_back), dan_here(loc_school_field_back)]):
        $ walk(loc_school_field_back)
    else:
        $ walk(loc_school_field)
    pc "Err, guys. Can I borrow something to wear?"
    dan.name "Yeah, I have something extra you can have."
    $ wardrobe.take(item_coat_10, notif=True, dress=True)
    pc "Thanks! Don't need to be showing everything off now."
    jump travel

label mira_ask_clothes:
    $ walk(mira_here(class_loc=True))
    show mira at right1 with dissolve
    pc "Do you have anything I can wear? I kinda got into some trouble."
    mira.name "Yeah, I have some spare whore stuff stashed away for this reason."
    if c.cansee_breasts:
        $ wardrobe.take(item_top_41, notif=True, dress=True)
    if c.cansee_vagina:
        $ wardrobe.take(item_bottom_34, notif=True, dress=True)
    pc "Wow. Wern't kidding when you called it whore stuff."
    mira.name "Yeah."
    jump mira_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
