label school_dance_show_4:
    $ school_dance_quest_show_count += 1
    $ walk(loc_school_gym)

    show svet dance happy at right1
    with dissolve
    svet.name "Ah you are here. Okay girls let's have a chat before we practice."
    show rachel dance at left3 with dissolve
    rachel.name "Whats up?"
    show anabel dance at left1
    show dani dance at left2
    with dissolve
    svet.name "Great work at the market girls. You all did a good job."
    dani.name "We going there again today?"
    svet.name "No. While we did a good job and attracted a lot of people, not many of them were interested in buying from the client. Most of the people that were attracted were men."
    svet.name "And not too many of them were interested in buying women's clothes."
    anabel.name "I am shocked!"
    svet.name "Yeah well, despite his poor choice of marketing, we still got paid so all's good."
    show dani worried
    dani.name "So what now? I was hoping I would be able to get some more money."
    svet.name "I am looking out for more opportunities, for now we keep practising. Hopefully I will have something lined up for next time."
    dani.name "Ok..."
    svet.name "Sorry [dani.nname]."
    hide dani with dissolve
    svet.name "..."
    svet.name "For now let's practice our routines so we are ready for a show next time!"
    rachel.name "Yaaay!"
    hide rachel with dissolve
    svet.name "Have fun."
    hide anabel
    hide svet
    with dissolve
    $ show_dance_image()
    "I head over and join the girls in practising our routine."
    pcm "Think we are getting better. Phew, still pretty tiring though"
    $ show_dance_image()
    pcm "Wonder if [svet.name] will manage something for next time..."
    svet.name "FOCUS! Keep in sync with the beat and stop dragging your leg!"
    $ show_dance_image()
    pcm "Got to focus!"
    "We keep up the routine until me and the girls are exhausted."
    $ exercise(180)
    $ player.add_mood(20)
    if player.tired <= 21:
        $ player.add_tired(21 - player.tired)
    $ player.face_neutral()
    pc "Uffff! Huffff!"
    $ renpy.scene()
    with dissolve
    svet.name "Good work girls. Let's call it a day."
    pcm "Yes..."
    $ walk(loc_school_locker_girls)

    show dani dance worried at right1 with dissolve

    $ pc_strip_tops()
    dani.name "..."
    show dani nooutfit
    dani.name "Think we will manage something next time?"
    pc "Hope so."

    $ pc_strip()
    $ acc_shower()
    $ player.set_hair("loose")
    pause 0.5
    hide dani

    $ walk(loc_school_locker_shower)
    $ shower_scene_wash()
    $ walk(loc_school_locker_girls, trans=False)


    show dani nude worried at right1 with dissolve
    $ pc_set_outfit("party")
    $ pc_dress_under()
    pause 0.5
    $ pc_dress()
    $ acc_shower_dress()
    $ player.set_hair()
    pc "You ok?"
    dani.name "Yeah..."
    show dani casual
    if "knows_dani_sex_oskar" in dani.list:
        dani.name "Just want some money so I don't have to pay [oskar.name] another way..."
        pc "Ah."
        dani.name "Doesn't matter. See you next time."
        hide dani with dissolve
        pc "..."
    else:
        dani.name "You been late before in paying [oskar.name]?"
        $ player.face_worried()
        dani.name "Never mind. See you next time."
        $ add_to_list(dani.list, "oskar_sex_comment")
        hide dani with dissolve
        pc "..."
        if oskar.sex:
            pcm "Looks like she will have to bend over to pay her rent as well..."
    call makeup_apply_call from _call_makeup_apply_call_2
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
