label school_photo_quest_photoshoot_assplay_1:
    "*** NOT WRITTEN YET ***"
    "This is just here as a teaser for what is to come."
    pc "So I dread to ask, but what do you want to do with this ass shoot?"
    felix.name "Well, the guy seems to have a serious anal fetish, so let's drag this out as much as we can."
    felix.name "Hmm, there is no way to talk on this topic using polite words so..."
    felix.name "First we will get some closeups of you spreading your ass cheeks and photograph your arsehole. "
    pc "Right."
    felix.name "Once we have him hooked on those photos, probably some photos with your fingers inside."
    felix.name "Afterwards maybe make use of some props such as plugs, dildos, whatever we come across to be honest."
    if acc.anus:
        pc "Well, have something in my arse right now so won't be a problem getting anything inside once I take it out."
        felix.name "Err..."
        felix.name "Right. Good to know I guess."
    elif main_quest_05.active == 2:
        pc "Well, I spent quite some time with a plug the size if a fist up my arse before, so should be fine."
        felix.name "You did?"
        pc "Yeah, don't ask."
    elif player.asex > 10:
        pc "Well, been fucked in the arse enough that toys should be no problem."
        felix.name "Err, good to know I guess."
    else:
        pc "Can't say I am too experienced with things up my arse, but whatever. We can give it a try."
    pc "But if you suggest fruit or something then I will be putting it in your arse."
    felix.name "I wasn't. But now I am curious..."
    pc "I don't want anything getting lost up there."
    felix.name "Err, ok. No fruit then."
    if felix.sex:
        felix.name "He also wants to see you with a cock in your arse. And seeing cum leaking out of it."
        felix.name "We have done stuff before so I am guessing you are fine with that being me. But if not then we will deal with it when we get there."
    else:
        felix.name "Main issue is the last part. He wants to see a cock in your arse and afterwards cum leaking from it."
        felix.name "We can fake the cum but not the cock."
        pc "..."
        felix.name "So..."
        pc "We both know what you are going to say so just spit it out."
        felix.name "Well... It's up to you."
        pc "Let's see when the time comes if you will be putting your cock in my arse."
    felix.name "Anyway, as I mentioned. For now it will be just some closeups. Nothing inside."
    pc "Ok, so I'll go wash up I suppose and meet you on set?"
    felix.name "Sounds good."
    $ walk(loc_school_photo_changingroom)
    pause 0.5
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ player.wash()
    pc "Some makeup wouldn't hurt."
    $ acc.makeup_on = True
    pc "That should do it."
    pause 0.5
    $ walk(loc_school_photostudio)
    $ player.face_happy()
    pc "Ta daa!"
    felix.name "Oh! Didn't expect you naked."
    pc "How else you going to see my arsehole?"
    felix.name "Thought you would have a robe or something."
    $ player.face_angry()
    pc "No, the lazy developer hasn't drawn one yet so I have to come out here naked."
    felix.name "Ok, well this is as far as the event goes anyway, maybe you will get a robe later."
    $ player.face_neutral()
    felix.name "For now, here is a teaser of the photoshoot we will be doing."
    show ps_anus at right with dissolve
    felix.name "Perfect closeup that leaves nothing to the imagination."
    felix.name "As the shoot progresses, you will have bigger objects put in your bum until [felix.name] fucks you."
    hide ps_anus with dissolve
    $ walk(loc_school_photo_changingroom)
    pause 0.5
    $ pc_dress_quick("daily")
    pause 0.5
    $ walk(loc_school_darkroom)
    pc "All good?"
    felix.name "Yeah, though no pay since this is a temp event."
    pc "No robe and then no pay. Damn cheater!"
    $ walk(loc_school_hallway)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
