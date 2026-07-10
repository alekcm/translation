label school_dance_show_22:
    $ school_dance_quest_show_count += 1
    $ walk(loc_school_gym)
    show anabel dance1 tights usport at left1
    show dani dance1 tights usport at left2
    show rachel dance1 tights usport at left3
    show svet dance1 tights usport happy at right1
    with dissolve

    svet.name "[dancet], gather round."
    svet.name "I have invited some people to come and watch our routine next time."
    dani.name "Pretty busy out there right now so might want to hang out in here until we are all ready."
    pc "Busy?"
    anabel.name "[svet.name] set up a show for us. Bunch of people out there waiting to see our routine."
    if player.check_nowill():
        $ player.face_worried()
    else:
        $ player.face_happy()
    pc "Ah right."
    pc "So we waiting on the others?"
    dani.name "Yeah [rachel.name] is still getting ready. I think [svet.name] is outside now organising the crowd."
    pc "How many?"
    dani.name "20 or so. Maybe more..."
    $ player.face_neutral()
    pc "Ah not too many then."
    dani.name "What? That's loads of people. They came here to watch us."
    show rachel usport tights dance1 happy at right2 with dissolve
    rachel.name "Ah so many people came! This is going to be great!"
    rachel.name "You all ready? Ah I can't believe this!"
    hide rachel with dissolve
    anabel.name "..."
    anabel.name "She seems eager."
    rachel.name "COME ON!"
    anabel.name "*Sigh*"
    anabel.name "Off we go I guess. Ready [dani.name]?"
    dani.name "Yeah..."
    hide anabel with dissolve
    hide dani with dissolve
    pause 0.5
    $ walk(loc_school_gym)
    show bg_school_gym_people_attendance onlayer bg_screen
    show anabel dance1 tights usport at left1
    show dani dance1 tights usport at left2
    show rachel dance1 tights usport at left3
    show svet dance1 tights usport at right1
    with dissolve
    svet.name "Alright girls. We have practiced this before so you know what to do. And remember. SMILE!"
    svet.name "Try to have fun out here. Now lets go."
    hide svet
    hide anabel
    hide rachel
    hide dani
    with dissolve
    pc "Okaaay. Let's try to do this..."
    "*NOTE* There will be a proper dance image here of the 5 of you dancing together. For now I will put the simple activity one instead."
    show activity_dance with dissolve
    "Me and the girls start our routine. While at first we are all nerves, encouragement from the crowd gives us all confidence and we start to relax more while dancing."
    "As the show progresses I start to actually enjoy the show and dancing with the girls. It seems like they may also be enjoying themselves."
    $ exercise(180)
    "As the show ends, we all take a bow and are greeted by clapping and whistling."
    hide activity_dance with dissolve
    $ player.face_happy()
    pcm "Sounds like they enjoyed themselves."
    pcm "Phew, that's good."
    "We all wave to the crowd and work our way back to the changing rooms."
    pause 0.5
    hide bg_school_gym_people_attendance onlayer bg_screen
    $ walk(False, "school_locker_girl", 420)
    $ player.add_mood(20)
    if player.tired <= 21:
        $ player.add_tired(21 - player.tired)
    $ player.face_neutral()
    show anabel dance1 tights usport at left1
    show dani dance1 tights usport at left2
    show rachel dance1 tights usport at left3
    show svet dance1 tights usport at right1
    with dissolve
    svet.name "Good job girls. That went pretty well I think."
    show rachel happy
    rachel.name "They LOVED it!"
    svet.name "If you say so [rachel.name]."
    rachel.name "Didn't you hear them. We looked so sexy out there. They loved our new outfits."
    svet.name "Hmmm."
    show anabel worried
    anabel.name "Didn't sound like it was the outfits they loved but what they showed off."
    rachel.name "Yup. Keep this up and we will get shows for weeks."
    show rachel angry
    rachel.name "Ugh, I am all sweaty..."
    hide rachel with dissolve
    dani.name "That was fun, but... Are they really here to see us dance? Or just see us?"
    svet.name "..."
    svet.name "Not sure that matters if we want to find some paying work..."
    show dani happy
    dani.name "Think it will help?"
    svet.name "Of course it will. But might have to change our routine a bit to... To play into it I guess."
    show anabel angry
    anabel.name "Hrmf!"
    hide anabel with dissolve
    dani.name "Ok..."
    hide dani with dissolve
    svet.name "What's your thoughts on this [name]? You have been quiet."
    if player.isslut or player.iswhore:
        pc "I don't care. Perverts are always looking up my skirt so makes no difference here."
        if player.iswhore:
            pc "Would be better if they were paying to look up it though. That lot out there got a free show."
            svet.name "Err..."
            svet.name "Okaay..."
    elif player.isbroken:
        pc "If it makes them happy, I am fine with it."
    elif player.check_nowill():
        pc "It's a bit embarrassing to be honest. But... Dancers have always done it haven't they?"
    else:
        pc "Part of the job I guess."
    svet.name "..."
    svet.name "Guess we will just have to see how things go with this promotion."
    hide svet with dissolve
    pause 0.5
    $ shower_scene("party")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
