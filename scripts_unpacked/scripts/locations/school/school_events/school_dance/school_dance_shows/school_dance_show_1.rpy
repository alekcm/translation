label school_dance_show_1:
    $ school_dance_quest_show_count += 1
    pause 0.5
    $ walk(loc_school_gym, trans=False)
    show rachel sport at right1
    show svet sport at right2
    show dani sport at left1
    show anabel sport at left2
    with dissolve
    svet.name "Great, all here now."
    anabel.name "What's going on?"
    svet.name "So I may have a commission for us. I told you last time..."
    show dani happy
    dani.name "Commission. So it's paid?"
    svet.name "Yes paid. So I have been speaking to..."
    dani.name "How much does it pay?"
    svet.name "Let me finish would you?"
    show dani neutral
    svet.name "So someone who owns a clothing stall is hoping to have us dance wearing his clothing."
    svet.name "He is hoping that it will drive people to his stand and spend their money. So we need to put on a show to attract attention."
    svet.name "He has given us some of his excess stock to wear while we dance."
    svet.name "We still haven't finalised the details yet but I accepted the clothes since it would be nice for us to all wear the same thing."
    svet.name "So here you go. Change into this and come back so we can practice."
    $ show_notif_popup("Dance clothes received")
    $ wardrobe.take(item_top_20)
    $ wardrobe.take(item_bottom_13)
    $ wardrobe.take(item_socks_1)
    $ wardrobe.take(item_pants_3)
    $ wardrobe.take(item_bra_3)
    dani.name "And the pay?"
    svet.name "I don't know yet. Probably not great so don't get your hopes up. He is desperate to bring in customers so doubt he has much to be spending on us."
    show dani worried
    dani.name "Ok..."
    hide rachel
    hide svet
    hide anabel
    hide dani
    $ walk(loc_school_locker_girls)
    pause 0.5
    $ school_dance_set_clothes()
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ pc_dress_quick("work")
    $ player.set_hair()
    show anabel dance at right3 with dissolve
    anabel.name "Not sure this covers much. Feels like my arse is showing."
    show dani dance at right1 with dissolve
    dani.name "Would be showing your arse if you didn't have those huge pants on."
    show anabel worried
    anabel.name "Thanks..."
    show dani happy
    dani.name "Or a huge ass."
    show anabel angry
    anabel.name "Yeah you can stop now."
    show rachel dance at right2 with dissolve
    rachel.name "Oooh these are nice!"
    if player.check_nowill():
        $ player.face_worried()
        pc "..."
        pc "Doesn't hide much."
        $ player.face_neutral()
    else:
        pc "Pretty revealing."
    rachel.name "Yup, people will love it."
    anabel.name "People?"
    rachel.name "Yeah, anyone we dance for."
    hide rachel
    show dani worried
    with dissolve
    dani.name "Err, dancing in front of others like this?"
    show anabel worried
    anabel.name "Sounded like that..."
    hide anabel with dissolve
    dani.name "Not sure I can do that..."
    hide dani with dissolve
    show sb_pose_upskirt with dissolve
    if player.has_perk(perk_exhibitionist, notif=True):
        pcm "Too revealing? I would be getting rid of these tights and pants if I could."
        pcm "Showing off while dancing could even be fun, but better make sure I'm not gonna be dragged in the bushes and raped after the show first."
    else:
        pcm "Skirt is pretty short..."
        pcm "The tights cover most though so I guess it's not too bad."
    hide sb_pose_upskirt with dissolve
    pause 0.5
    $ walk(loc_school_gym, trans=False)

    show dani dance at left1
    show anabel dance at left2
    show rachel dance at left3
    show svet dance at right1
    with dissolve
    anabel.name "...without showing off what's under the skirt."
    dani.name "It does seem a bit short."
    rachel.name "What are you worrying about? Dancers did this all the time back when. It's how they get attention."
    dani.name "I want to dance, not get attention."
    show rachel at right3 with dissolve
    rachel.name "No one will want to watch us if we are dressed in sweats. We need to stand out if we want to get paid. Right [svet.name]?"
    show svet worried
    svet.name "It's true..."
    svet.name "*Sigh* Dancing isn't always about good routines..."
    rachel.name "Yup. So let's go!"
    hide rachel with dissolve
    svet.name "Let's just give this a try for now. Ok?"
    anabel.name "..."
    dani.name "It will help with getting paid jobs?"
    svet.name "I hope so..."
    hide svet with dissolve
    dani.name "Ok."
    hide dani with dissolve
    show anabel with dissolve:
        xzoom 1
    anabel.name "You okay with his [name]?"
    if player.has_perk(perk_exhibitionist):
        pc "Yeah, I don't mind showing off some skin."
    elif player.has_perk([perk_whore, perk_slut]):
        $ player.face_happy()
        pc "Yeah I don't care. If people like it more than it's ok."
    elif player.has_perk(perk_broken):
        pc "It's fine. If it's what people want to see."
    elif player.check_nowill():
        $ player.face_worried()
        pc "Not really..."
    else:
        pc "Not sure. I'll see how it goes I suppose."
    anabel.name "Hmm..."
    hide anabel with dissolve
    $ player.face_neutral()
    $ show_dance_image()
    "I join the girls and we start our routines. We pick up from where we left off last time and I try to maintain coordination with the rest of [dancet]."
    "I manage quite well and are building a good rhythm with the other girls. While most of us are already good at dancing, it feels good to finally get some coordination going for the routines."
    $ show_dance_image()
    "Towards the end of training it starts to look like we might actually pass as a proper dance troupe."
    $ exercise(180)
    $ player.add_mood(20)
    if player.tired <= 21:
        $ player.add_tired(21 - player.tired)
    $ player.face_neutral()
    pc "Phew!"
    $ renpy.scene()
    with dissolve
    show svet dance at right1 with dissolve
    svet.name "Good job girls. Let's call it for the night. Go clean up and head home."
    hide svet
    $ walk(loc_school_locker_girls, trans=False)
    show dani dance at right1
    show rachel dance happy at right3:
        xzoom -1
    with dissolve
    rachel.name "...we look, the more people will pay for shows. You know what it's like."
    dani.name "..."
    $ pc_strip_tops()
    dani.name "Maybe. If they are shows that help me pay for my room..."
    rachel.name "Don't worry. [svet.name] won't let us down!"
    $ pc_strip()
    $ acc_shower()
    $ player.set_hair("loose")
    pause 0.5
    hide dani
    hide rachel
    $ walk(loc_school_locker_shower)
    $ shower_scene_wash()
    $ walk(loc_school_locker_girls, trans=False)


    show anabel at right1 with dissolve
    pause 0.5
    $ pc_set_outfit("party")
    $ pc_dress_under()
    anabel.name "Get used to it. It's part of the show..."
    $ pc_dress()
    $ acc_shower_dress()
    $ player.set_hair()
    pc "So they say."
    show anabel casual with dissolve
    anabel.name "..."
    anabel.name "Suppose I'll try."
    pc "Mmm."
    anabel.name "See you next time [name]."
    pc "Yeah. See you."
    hide anabel with dissolve
    call makeup_apply_call from _call_makeup_apply_call_1
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
