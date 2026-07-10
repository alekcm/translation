label oskar_talk_ask_work:
    show oskar at right1 with dissolve
    $ oskar.dict["oskar_ask_work"] = t.day
    pc "I was wondering if there was some work around here I could do to lower my rent."
    oskar.name "Hmmm, Maybe..."
    jump oskar_talk_ask_work_again_catcher









label oskar_talk_ask_work_again_catcher:
    oskar.name "Found some stuff in the back there. Put it to use and I'll drop your payments."
    pc "Stuff?"
    oskar.name "Broom, buckets... Cleaning stuff. Clean up round here and I'll consider it work done and knock a bit off your rent."
    pc "Hmm, office is small. How much will that get me?"
    oskar.name "I was talking about the courtyard. But cleaning the office is a good idea. Each day you clean up I'll knock the rent down."
    pc "Oh, sounds good."
    oskar.name "Mmm."
    hide oskar with dissolve
    if not quest_cleaner.active:
        $ quest_cleaner.activate()
        $ log.assign("Cleaner")
    $ log.activate("quest_rent_b", notify=True)
    jump travel

label oskar_clean_event_apron_give:
    if not loc_office_ll.open():
        pc "[oskar.name] mentioned he has some stuff to clean in, but his office is closed so I'll have to wait."
        jump travel

    $ add_to_list(quest_rent.list, "apron")
    $ add_to_list(quest_cleaner.list, "apron")
    pcm "[oskar.name] mentioned having some stuff in the back room. Guess I should take a look."
    $ walk(loc_office_ll)
    pc "Hi. You mentioned you have some stuff to clean with."
    show oskar at right1 with dissolve
    oskar.name "Yeah. I came across some stuff in the back. Something you can wear while cleaning up."
    $ player.face_worried()
    pcm "Oh shit."
    oskar.name "Can't have it looking like some gamine is wandering around. So dress up while you are cleaning."
    pc "In the back?"
    oskar.name "Yes. Go have a look."
    pcm "I have a bad feeling about this..."
    hide oskar
    $ walk(loc_office_ll_back)
    pcm "Let's see..."
    $ player.face_surprised()
    $ cleaner_outfit_set()
    $ wardrobe.take(item_outfit_19, all_notif=True)
    $ wardrobe.take(item_gloves_4, all_notif=True)
    pcm "Oh? This is not bad actually. Kinda useful."
    $ player.face_neutral()
    $ pc_strip_tops(True)
    if c.socks:
        $ c.socks = 0
        pause 0.3
    pause 0.3
    $ quest_rent.work_dress(slow=True)
    $ player.face_happy()
    pcm "Yeah, this won't be too bad to clean in."
    $ walk(loc_office_ll)
    show oskar at right1 with dissolve
    oskar.name "They fit?"
    $ player.face_happy()
    pc "Yeah, fit's fine."
    oskar.name "Right, then off you go."
    pc "Thanks."
    hide oskar with dissolve
    $ walk(loc_stairwell)
    $ clean_locations_picker()
    $ loc_stairwell.clean_last = t.minutes_total
    jump action_clean_event_picker

label oskar_clean_event_maid_give:
    $ add_to_list(quest_rent.list, "maid")
    $ add_to_list(quest_cleaner.list, "maid")
    show oskar at right1 with dissolve
    if c.outfit == 20:
        oskar.name "I see you are wearing... that... instead of the overalls I gave you."
        pc "Err, shouldn't I?"
        oskar.name "You should. This is much nicer. Gives the place a little more class."
        pc "Class? Really?"
        oskar.name "Yes, this place is better than most in case you haven't looked around. Plus I have people coming to visit me now and then. It would be better if you looked more the part."
        pc "Right..."
        oskar.name "So it's good you are wearing it. Keep doing so from now on and don't bother with the overalls."
        pc "Okay..."
    else:
        oskar.name "[fname]. You got anything more fancy than those overalls?"
        pc "Err, fancy?"
        oskar.name "The overalls work well enough, but it would be nice if this place had a little more class."
        pc "Class? Have you looked around?"
        oskar.name "Yes, and this place is better than most. Plus I have people coming to visit me now and then. It would be better if you looked more the part."
        pc "Err... Right..."
        hide oskar with dissolve
        $ walk(loc_stairwell)
        pcm "What does that even mean?"
        if wardrobe.qty(item_outfit_20):
            pcm "I guess I could try out the maid outfit I have next time."
        else:
            pcm "Suppose I should look around for something more \"classy\"..."
    $ rent_workoff(20)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
