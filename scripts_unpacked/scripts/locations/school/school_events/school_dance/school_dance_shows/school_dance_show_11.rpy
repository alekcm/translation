label school_dance_show_11:
    $ school_dance_quest_show_count += 1
    $ add_to_list(rachel.list, "no_location")
    $ add_to_list(dani.list, "no_location")
    $ add_to_list(anabel.list, "no_location")
    $ add_to_list(svet.list, "no_location")
    $ walk(loc_school_gym)
    show svet dance at right1
    show rachel dance at left3
    with dissolve
    rachel.name "So what we up to today?"
    show dani dance at left2 with dissolve
    svet.name "Same as before. Head to the park and dance a bit."
    show anabel dance at left1 with dissolve
    rachel.name "Okay!"
    dani.name "Money is getting a lot better so sounds good to me."
    anabel.name "Mmm."
    hide rachel with dissolve
    $ renpy.scene()
    $ walk(loc_school)
    $ remove_from_list(rachel.list, "no_location")
    $ remove_from_list(dani.list, "no_location")
    $ remove_from_list(anabel.list, "no_location")
    $ remove_from_list(svet.list, "no_location")
    pause 0.2
    $ walk(loc_busstop_school)
    show rachel dance at right1
    with dissolve
    rachel.name "Ah, it's almost here. Hurry up you lot!"
    hide rachel with dissolve
    $ walk(loc_bus_interior)
    with dissolve
    pcm "Ugh. Packed."
    with hpunch
    pcm "Woah!"
    pcm "Hmmm..."
    pcm "We are actually making decent money these days with all this dancing."
    if player.check_sex_agree(3, exhibitionist=True):
        pcm "And is actually quite fun all things considered."
    else:
        pcm "And is actually quite fun, even if I have to fend of the touchy perverts."
    pcm "The other girls seem to enjoy it as well."
    pcm "Well, [rachel.name] would probably enjoy anything."
    $ player.face_worried()
    pcm "Err, yeah she would. Looks like she is even enjoying what that pervert is doing to her..."
    $ player.face_neutral()
    pcm "How did I wind up squashed in here alone anyway? [rachel.name] is getting felt up by some perv, but where are the rest?"
    show dani dance at left1:
        xzoom -1
    $ player.face_shock()
    with vpunch
    pc "Ah!"
    $ player.face_neutral()
    dani.name "Only me."
    pc "Was wondering what happened to you and [anabel.nname]. Couldn't see you."
    dani.name "Ah, yeah..."
    dani.name "Bus jolted and I ended up on someone's lap. They thought I was a slut offering myself so took me a bit to untangle myself."
    dani.name "Do people really get on these buses to have fun with the deviants?"
    pc "Nooo. [rachel.name] would never do such a thing."
    dani.name "Huh?"
    dani.name "[rachel.name]?"
    show dani with dissolve:
        xzoom -1
    dani.name "Oh?"
    show dani happy
    dani.name "Ooooohhh..."
    dani.name "Yeah I can see her..."
    pc "Can join her if you want."
    show dani neutral with dissolve:
        xzoom 1
    dani.name "No thanks. I have filled my quota of guys trying to stick their dick in me for one day."
    pc "Well, we still have the park to do. Pretty sure you will get more offers."
    dani.name "At least they keep it in their pants. Too public."
    pc "Yeah, their hands don't stop trying to get into mine though."
    show dani happy
    dani.name "Ha! Right!"
    pc "We are here, let's go."

    $ renpy.scene()
    $ walk(loc_busstop_residential, trans=False)
    show dani dance at right1
    show anabel dance at right2
    with dissolve
    dani.name "We all here?"
    pc "Err, I guess."
    anabel.name "Wait. [rachel.name]'s missing."
    dani.name "Looks like she got held up. She will jump off the next stop."
    anabel.name "Hmm..."
    hide dani with dissolve
    $ renpy.scene()
    $ walk(loc_park)

    show svet dance at right1
    show dani dance at left2
    show anabel dance at left1
    with dissolve
    svet.name "Right, so same as always... No [rachel.name]?"
    dani.name "She didn't get off with us."
    svet.name "Ok, well we all know what to do. Let's clean up and wait on [rachel.name]."
    pc "Right."
    $ renpy.scene()
    with dissolve
    "Me and the girls work to clear up a space for dancing. We are mostly doing busywork in the end just waiting for [rachel.name] to return from the bus."
    pcm "Hope she didn't decide to stay for more than another stop. Crazy idiot might end up in more trouble than she can handle."
    pcm "Ugh, these perverts can't keep their eyes off us. Cleaning junk off the floor gives a clear view up our skirts. Probably why most of them arrive early."
    show dani dance at right1 with dissolve
    dani.name "[rachel.name] is taking her time."
    $ player.face_happy()
    pc "Or the guys on the bus are."
    show dani happy
    dani.name "Ah, didn't think of that. Maybe she doesn't want to get off the bus."
    $ player.face_neutral()
    pc "Who knows. She's taking ages though so maybe we should start without her?"
    show rachel dance happy at right2 with dissolve
    rachel.name "No, I'm here."
    rachel.name "Just about."
    dani.name "Oh. Thought you might not come."
    rachel.name "I did come. Then I got off the bus."
    $ player.face_happy()
    pc "Slut."
    rachel.name "Yup. But lost the pinkies. Gonna be tough going."
    $ player.face_neutral()
    rachel.name "Let's start?"
    dani.name "Yeah."
    $ renpy.scene()

    $ show_dance_image()
    "We do our routine as we usually do, though [rachel.name] is a lot more subdued than usual. I am guessing her lack of underwear is causing her to be a bit more modest else she will show everything off."

    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_6
    if c.pants:
        "Not that the underwear that the rest of us are wearing hides much. Combine that with a skirt that struggles to hide anything even when we are standing still, our underwear is on display pretty much the entire time."
    else:
        "Not that the underwear, or in my case the lack of underwear that the rest of us are wearing hides much. Combine that with a skirt that struggles to hide anything even when we are standing still, our asses are on display pretty much the entire time."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_7
    "Looks like everyone has gotten used to this though and just carries on like normal. Not like we can do much about it so no point in even trying."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_8
    $ player.grope()

    "And as expected, while working the crowd, the people seem much more interested in putting their hands up our skirts than anything else."
    $ player.grope()
    pcm "Wonder how [rachel.name] is getting along surrounded by these animals and no knickers?"
    $ player.face_happy()
    pcm "Serves her right."
    $ player.grope_end()
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_9
    "Things start to wind down and we all push into the crowd to squeeze a bit more money out of everyone. Of course they try to give way more than we ask for."
    $ player.busk()
    pc "Thank you, thank you. In the hat please."
    $ player.grope()
    pcm "Dammit, touching is fine but stop trying to stick them inside."
    $ player.grope()
    pc "Thank you. Join us next time for more!"
    $ player.grope()
    pcm "Right. Back to the girls."
    $ player.grope_end()
    $ player.busk_end()
    $ renpy.scene()
    with dissolve
    show svet dance at right1
    show rachel dance at left3
    show anabel dance at left1
    show dani dance at left2
    with dissolve
    svet.name "Getting good at this."
    dani.name "Yeah, they expect us now and seem to treat it like an outing."
    rachel.name "As long as they pay."
    svet.name "They did. Money is better again. Here you all go."
    $ player.add_money(120)
    rachel.name "Oooh. Nice."
    dani.name "Mmm."
    svet.name "Be safe girls. I'm heading off to meet someone."
    rachel.name "See ya."
    hide svet with dissolve
    dani.name "Think she has a date?"
    show rachel with dissolve:
        xzoom 1
    rachel.name "[svet.nname]? No chance."
    anabel.name "You seem so sure."
    rachel.name "I'd quicker believe she was stalking the park looking for a man to murder than be going on a date."
    show anabel happy
    anabel.name "Oh? Maybe I should join her."
    rachel.name "Ha, make this place a lot safer. Anyway I'm heading home. See ya."
    anabel.name "Bye."
    show anabel neutral
    hide rachel with dissolve
    show dani with dissolve:
        xzoom 1
    dani.name "Need a shower after all that. See you guys."
    anabel.name "You heading home?"
    dani.name "Yeah. You coming?"
    anabel.name "Yeah. See you [name]."
    pc "Be safe."
    dani.name "You too."
    hide dani
    hide anabel
    with dissolve
    pcm "Hmm, [dani.nname] isn't meeting her friend today it looks like."

    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
