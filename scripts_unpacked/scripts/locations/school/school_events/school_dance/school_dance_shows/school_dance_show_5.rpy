label school_dance_show_5:
    $ school_dance_quest_show_count += 1
    $ dance_hide_girls()
    $ walk(loc_school_gym, trans=False)
    show dani sport worried at left4
    show svet dance at right1
    with dissolve
    dani.name "... for something."
    svet.name "I know... But he isn't interested anymore because it ended up costing him money in the end."
    dani.name "..."
    dani.name "And nothing else lined up for today?"
    show anabel sport at left2 with dissolve
    svet.name "No, nothing."
    dani.name "Any ideas?"
    svet.name "Other than just going out and busking, no. People aren't so eager to..."
    show dani neutral
    dani.name "Busking? What's that?"
    anabel.name "Dancing in the street and hoping people will put money in your hat."
    show dani with dissolve:
        xzoom 1
    dani.name "We can do that?"
    anabel.name "Not sure why you would want to."
    show dani happy
    dani.name "People will pay for it?"
    anabel.name "No you don't get paid for it. You just hope people will put some small money in your hat as a thank you tip or something."
    dani.name "So we get money for it?"
    anabel.name "Yes, but it's not an actual job with a client but it's..."
    show dani with dissolve:
        xzoom -1
    dani.name "So why aren't we doing that then?"
    anabel.name "Because it's not an entirely legiti..."
    show rachel dance happy at left3 with dissolve
    rachel.name "I saw people in the park doing stuff like that a couple of times. We could go there couldn't we?"
    svet.name "*Sigh* This isn't some legit job. It is busking. I have no idea if we will even come away with anything."
    dani.name "Staying here won't bring anything either."
    svet.name "..."
    svet.name "What do you think [anabel.name]?"
    anabel.name "I am against it. The people we would be dancing for would be \"those\" types."
    svet.name "What about you [rachel.name]?"
    rachel.name "Sounds great. I wanna dance in front of another crowd."
    svet.name "[name]?"
    if player.has_perk(perk_exhibitionist, notif=True):
        pc "Sounds fun to me. I like dancing and showing off."
    elif player.has_perk(perk_whore, notif=True):
        pc "If we get paid for it then great."
    elif player.has_perk(perk_slut, notif=True):
        pc "I have no issue showing off to the perverts."
    elif player.has_perk(perk_broken, notif=True):
        pc "I'm fine with whatever."
    elif player.check_nowill():
        pc "Err... Not really a fan of the idea."
    else:
        pc "Not sure. I could do with the money like everyone else. But those types of people watching?"
    svet.name "Hmmm..."
    svet.name "Ok, how about we give it a try just for tonight and see how things pan out? Maybe we don't make any money or security tells us to leave so the choice is made."
    anabel.name "And if we do earn money?"
    svet.name "Then we will have all the information to make a proper decision so we will discuss it properly afterwards."
    svet.name "Right now I have nothing on the cards so this is the only way for us to earn money while dancing tonight."
    dani.name "Ok."
    anabel.name "Hmm..."
    svet.name "Ok, go get changed into your dance outfits and we will meet at the bus stop."
    rachel.name "Sounds good!"
    hide rachel with dissolve
    hide svet with dissolve
    show dani with dissolve:
        xzoom 1
    dani.name "Thanks."
    hide dani with dissolve
    anabel.name "..."
    hide anabel with dissolve
    if player.has_perk(perk_exhibitionist, notif=True):
        pcm "I get to show off my arse in front of a crowd while staying fairly safe with the girls around."
        $ player.face_shy()
        $ player.add_desire_random(10)
        pcm "Exciting..."
    else:
        pcm "Busking in the park? That's going to attract all manner of weirdos..."
    $ walk(loc_school)
    pause 0.5
    $ walk(loc_busstop_school, trans=False)
    $ dance_unhide_girls()
    show svet dance at right1
    show rachel dance at left1
    with dissolve
    svet.name "... the market it was expected that people will come up to you. But in the park make sure people keep their distance ok?"
    rachel.name "Ah it'll be fine. Let them enjoy."
    svet.name "Not sure you are getting my meaning. Keep them at a distance ok?"
    show rachel angry
    rachel.name "Spoilsport!"
    if player.has_perk([perk_gamine, perk_slut, perk_whore, perk_exhibitionist]):
        pcm "Pretty sure she gets your meaning perfectly."
    show dani dance at left2
    show anabel dance at left3
    with dissolve
    svet.name "Great, all ready?"
    dani.name "Yup."
    hide dani
    hide svet
    hide anabel
    hide rachel
    $ walk(loc_bus_interior)
    $ player.face_worried()
    pcm "Ugh, packed as usual..."
    with hpunch
    pc "Sorry. Excuse me. Thanks."
    show dani dance at left1 with dissolve:
        xzoom -1
    pc "Ugh."
    dani.name "Yeah."
    $ player.face_neutral()
    pc "..."
    dani.name "Think it will work?"
    pc "Huh?"
    dani.name "Think people will put money in the hat?"
    $ player.grope()
    pc "Ah!"
    $ player.grope_end()
    $ player.face_angry()
    with hpunch
    show dani worried
    dani.name "Eh, you ok?"
    pc "Yeah, groper..."
    $ player.face_neutral()
    show dani neutral
    dani.name "Ah."
    pc "It might work. No harm in giving it a go anyway."
    dani.name "Hope so. Else [oskar.name] is going to be on me again..."
    pc "Yeah tell me about it."
    dani.name "This is our stop."
    pc "Excuse me, coming through."
    with hpunch
    hide dani with dissolve
    $ walk(loc_park)
    show anabel dance at left1
    show dani dance at left2
    show rachel dance at left3
    show svet dance happy at right1
    with dissolve
    svet.name "Ok, this looks as good a spot as any. Decent foot traffic without blocking people walking by so no one should complain."
    rachel.name "I'll set up the music."
    hide rachel with dissolve
    svet.name "Right, so we just do the routines we practised. And remember to smile and have fun. No one is going to take their money out if we all look miserable."
    pc "Right."
    hide dani
    hide svet
    hide anabel
    with dissolve
    $ show_dance_image()
    "Despite it being just [dancet] and a music box, we manage to attract a somewhat sizeable crowd who relaxes and watches the routines we put on."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call
    "While the people watching tend to be predominantly men, there are quite a few women in the crowd enjoying the show which makes us all feel a little better about ourselves."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_1
    "At the end of each routine, one of us works their way through the crowd with a hat in hand to collect donations. Most people ignore us but there are a fair amount of people who put hand in pocket and give us something."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_2
    "We continue like this, doing a routine then collecting money until most of us are exhausted."
    $ player.add_mood(20)
    if player.tired <= 21:
        $ player.add_tired(21 - player.tired)
    $ player.face_neutral()
    $ renpy.scene()
    with dissolve
    pcm "Ugh, that was pretty tough."
    show svet dance at right1 with dissolve
    svet.name "Okay girls. Gather round."
    show anabel dance at left1
    show dani dance at left2
    show rachel dance at left3
    with dissolve
    dani.name "Phew, that was harder than it thought I would be."
    anabel.name "Yeah, pretty tired after that."
    rachel.name "So? So? How much?"
    svet.name "Doesn't look too bad. Let's see..."
    svet.name "Hmmmm..."
    svet.name "Divide it by 5..."
    svet.name "Here you go."
    $ player.add_money(25)
    svet.name "Not a huge amount but a lot more than I was expecting."
    show dani happy
    dani.name "Great!"
    rachel.name "Same thing next time?"
    svet.name "Well we need to tal..."
    dani.name "Yes, if no other shows then let's come here again!"
    anabel.name "But is it worth it?"
    show dani with dissolve:
        xzoom 1
    dani.name "I had no money before and I have money now."
    anabel.name "But..."
    show anabel worried
    anabel.name "We are dancing for \"them\"."
    dani.name "Who?"
    anabel.name "Can't count how many people touched me while I was going round with the hat."
    show rachel happy with dissolve:
        xzoom 1
    rachel.name "Ha. They did seem to like to touch didn't they?"
    anabel.name "It was horrible..."
    show dani worried
    dani.name "..."
    dani.name "Not really something I want to be doing again."
    rachel.name "Ah that's fine. I'll go out and do it if you have a problem with it."
    show dani neutral
    if player.has_perk([perk_slut, perk_whore, perk_broken, perk_exhibitionist], notif=True):
        pc "I don't mind either."
    anabel.name "But..."
    rachel.name "Okay so all's good. Same again next time yeah?"
    show rachel angry
    rachel.name "I am going to go. I stink!"
    hide rachel with dissolve
    show svet worried
    svet.name "Err. Okay then..."
    svet.name "Next time."
    hide svet with dissolve
    show anabel neutral at right1
    show dani at right2
    with dissolve
    anabel.name "So you are okay with showing off to these types [dani.name]?"
    dani.name "It's horrible. But if I can't pay rent or buy food then it's even worse."
    anabel.name "And you [name]?"
    if player.has_perk(perk_exhibitionist, notif=True):
        pc "Yeah I had fun with it all."
    elif player.has_perk(perk_broken, notif=True):
        pc "Had a lot worse than these people groping me so doesn't really matter."
    elif player.has_perk([perk_slut, perk_whore], notif=True):
        pc "Makes no difference to me. Guys are going to touch you where ever you go so I'm not going to let that stop me from dancing."
    elif player.check_nowill():
        $ player.face_meek()
        pc "..."
    else:
        $ player.face_worried()
        pc "It is what it is."
    show anabel angry
    anabel.name "Hrmf!"
    anabel.name "I just wanted to dance and be safe around girls. Not have to think about all this stuff again."
    $ player.face_neutral()
    hide anabel with dissolve
    dani.name "Err, goodbye?"
    pc "Guess she isn't happy..."
    dani.name "Can't blame her. I agree with her, but..."
    pc "Rent won't pay itself."
    dani.name "Yeah..."
    dani.name "Anyway, I have to go. See you next time."
    pc "Wanna walk together?"
    dani.name "Sorry, I'm not heading home."
    pc "Ok."
    hide dani with dissolve
    show sb_pose_upskirt with dissolve
    pcm "..."
    pcm "Alone with my arse hanging out again..."
    pcm "*Sigh*"
    hide sb_pose_upskirt with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
