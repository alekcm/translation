init python:
    def pub_outfit_set():
        pub_waitress.outfit_primary_colour = "crimson"  
        pub_waitress.outfit_secondary_colour = "white"
        pub_waitress.pants_primary_colour = "crimson"
        pub_waitress.pants_secondary_colour = "crimson"
        pub_waitress.socks_primary_colour = "crimson"
        pub_waitress.socks_secondary_colour = "white"
        
        for i in clothes_wardrobe_list:
            setattr(pub_waitress, i, 0)
        pub_waitress.outfit = 6
        pub_waitress.pants = 6
        pub_waitress.socks = 7

    def pub_outfit():
        for i in clothes_wardrobe_list:
            setattr(work, i, 0)
        work.outfit_primary_colour = pub_waitress.outfit_primary_colour
        work.outfit_secondary_colour = pub_waitress.outfit_secondary_colour
        work.pants_primary_colour = pub_waitress.pants_primary_colour
        work.pants_secondary_colour = pub_waitress.pants_secondary_colour
        work.socks_primary_colour = pub_waitress.socks_primary_colour
        work.socks_secondary_colour = pub_waitress.socks_secondary_colour
        
        work.outfit = pub_waitress.outfit
        work.socks = pub_waitress.socks
        work.pants = pub_waitress.pants

    def pub_tips():
        pub_waitress.reward_counter += renpy.random.randint(0, 2)
    def pub_sell_socks():
        pub_waitress.missionvar2 = round_num(numgen(30,60))
    def pub_sell_pants():
        pub_waitress.missionvar3 = round_num(numgen(35,60))

    def pub_reset_vars():
        pub_waitress.reward_counter = 0 
        pub_waitress.missionvar1 = False
        pub_waitress.missionvar2 = 0 
        pub_waitress.missionvar3 = 0 


label pub_waitress_picker:
    if pub_waitress.active == 0:
        jump pub_waitress_joboffer
    elif player.tired <= 20:
        pc "I am too tired to be working right now"
        jump travel
    elif player.cum_visible:
        pc "With cum on me I will be kicked out the pub. I need to wash first. Ugh I am so disgusting..."
        jump travel
    elif pub_waitress.timesworked == 0:
        jump pub_waitress_work_firstday
    else:
        jump pub_waitress_work

label pub_waitress_joboffer:
    show trixie at right1 with dissolve
    trixie.name "Hey hon, what can I get you?"
    pc "Actually I was wondering if there was any work available?"
    trixie.name "Nothing permanent, but we always need girls to pick up the slack in the evenings when it gets a bit more busy."
    trixie.name "So if you want, just come in the evening and pick up a shift. Some time after 5 or so."
    pc "Ok, what's the pay?"
    trixie.name "It's all tips darlin', so that all depends on you. This place is full of perverts so it won't be hard for someone as pretty as you to get decent tips."
    pc "Ah... Ok..."
    trixie.name "Don't worry sweetheart, it's not that bad. Think it over and if you want a shift just pop by, ya hear?"
    trixie.name "If that ain't your kinda thing, can always clean up 'round here in the daytime. Get paid cash as well, not much but at least it ain't tips."
    pc "Ok, thanks for the info."
    hide trixie with dissolve
    pc "Hmmm. I desperately need the money, but can I work in a place like this...?"
    pc "Suppose I will think it over."

    $ log.assign("Pub barmaid")
    $ diary_jobs_pub_func()
    if not quest_cleaner.active:
        $ log.assign("Cleaner")
    $ pub_waitress.activate()
    jump travel

label pub_waitress_work_firstday:
    show trixie smile at right1 with dissolve
    $ pub_reset_vars()
    $ loc_pub_changingroom.locked = False
    trixie.name "Hey hon, since it's your first day, I will walk you through a few things."
    trixie.name "Unlike before, people here rarely go to the bar to order drinks. It's our job to walk around and serve customers. Boss says it brings in more money making sure people always have something to drink."
    trixie.name "Customers also like it more when the girls are walking around. \"Makes the place more pretty\" apparently."
    trixie.name "People will call you over if they want a drink, but if no one has called you over then make sure to go up to people and ask them if they need anything. Don't be standing around picking your nose now."
    trixie.name "You are paid from tips, so you need to be active and approaching people all the time. Hard work but can pay off."
    pc "Ok..."
    trixie.name "Now let's go find a uniform that fits you."
    $ walk(loc_pub_changingroom)
    trixie.name "..."
    trixie.name "Lets see here..."
    $ wardrobe.take(item_outfit_6, all_notif=True)
    $ wardrobe.take(item_socks_7, all_notif=True)
    $ wardrobe.take(item_pants_6, all_notif=True)
    trixie.name "Ah, this one should fit. Here, try it on."
    show trixie with dissolve:
        xzoom -1

    $ pc_striptease()
    pause 0.5
    $ pc_strip_work()
    $ pub_outfit_set()
    $ pub_outfit()
    $ pub_waitress.clothes = tab_top
    $ tab_top = "work"
    $ pc_dress_slow()
    $ pub_waitress.dict["wear_pants"] = True
    $ pub_waitress.dict["wear_socks"] = True

    pc "Done."
    show trixie with dissolve:
        xzoom 1
    trixie.name "Perfect, you look lovely in it."
    show sb_pose_upskirt with dissolve
    if player.has_perk(perk_male, notif=True):
        $ player.face_sus()
        pcm "Shit. I know what the guys are going to be thinking when they see me wearing this."
        pcm "Not a single person out there isn't going to be trying to look up this short skirt..."
        pcm "These knickers are tiny as well and already riding up my arse."
        pc "I'm guessing the skirt is this short on purpose?"
        trixie.name "Yeah, customers tip more when you show some skin."
        pcm "Of course they do..."
    elif player.has_perk([perk_exhibitionist, perk_bimbo, perk_gamine, perk_whore, perk_slut], notif=True):
        $ player.face_happy()
        pc "Short skirt and lots of cleavage, this will help with the tips no doubt."
        trixie.name "Yup, the customers love it."
    elif player.has_perk([perk_meek, perk_broken], notif=True):
        $ player.face_worried()
        pc "I suppose this is what the men like to look at?"
        trixie.name "Yup, the customers love it."
        pc "Okay."
    elif player.check_nowill():
        $ player.face_worried()
        pc "Err, what? It shows my chest of fully and the skirt isn't enough to hide my arse..."
        trixie.name "Yup, the customers love it."
        pc "But isn't it too much?"
        trixie.name "Na. We work for tips so showing a bit of skin earns us more money."
        pcm "This is more than a bit..."
    else:
        $ player.face_sus()
        pc "Quite skimpy isn't it?"
        trixie.name "Yeah, customers tip more when you show some skin."
    $ player.face_normal()
    trixie.name "Just be sure to wear pants since the skirt is so short. Or... Y'know... Don't. Might get you into trouble but could probably earn more."
    if player.has_perk(perk_commando):
        pc "I'd prefer not to. How much trouble that going to get me into?"
        trixie.name "A lot, but it will also fill your pockets."
        if player.showing:
            trixie.name "I would normally tell the girls to make sure not get a belly full of baby. But a bit late with you."
            if trixie.showing:
                pc "You as well it seems."
                trixie.name "Yup."
        else:
            trixie.name "Just be sure you don't let them fill your belly as well. Can work here preggo if you want though. Some pay even more for that."
            if trixie.showing:
                pc "That belly you have because of no knickers?"
                trixie.name "Something like that."
    $ player.face_worried()
    pc "Right..."
    $ player.face_normal()
    hide sb_pose_upskirt with dissolve
    trixie.name "Okay then, take this notebook with you. When they order a drink just write down what they asked for on a new page along with the table number then hand the sheet in at the bar."
    trixie.name "They will prepare the drinks while you walk around getting more orders. Whenever you see an order that's ready at the bar, just grab it and take it to the table."
    pc "Ok."
    trixie.name "Great, then off you go. I won't be holding your hand as it's easy to pick up. Just be sure to keep a smile on your face."
    hide trixie with dissolve
    if player.has_perk(perk_commando):
        show sb_pose_upskirt with dissolve
        pcm "Well, getting rid of these pants that's for sure."
        $ c.pants = 0
        $ work.pants = 0
        $ pub_waitress.dict["wear_pants"] = False
        pcm "Skirt is tiny though. Going to end up showing off a lot if I'm not careful."
        pcm "Oh well..."
        hide sb_pose_upskirt with dissolve
    $ walk(loc_pub)
    pc "Okay then, grab beers from the bar and take them to where they need to go? How will I know where they should go?"
    $ player.right_hand = "beer"
    pc "Ah, a note with the table number. Well, let's find table 8 then."
    jump pub_waitress_work_picker

label pub_waitress_shop:
    call screen inventory_itemshop_screen(shop_pub, show_locked=True)  
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
