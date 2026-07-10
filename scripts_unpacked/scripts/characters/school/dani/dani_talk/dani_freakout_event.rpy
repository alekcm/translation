label dani_freakout_event_courtyard_arrive:
    $ oskar.kill("Killed by Dani. Looks like the shit he put her through ended up too much.")
    $ dani.kill("Arrested after murdering the landlord. I have no idea what happened to her afterwards.")
    $ loc_bedroom_dani.home_location = True
    show police_gen at right1 with dissolve
    police.name "Sorry luv, can't come in 'ere. Go somewhere else."
    pc "Huh? Why? I live here."
    $ player.face_worried()
    police.name "Do ya? Where?"
    pc "Just there, you can see my door from here."
    police.name "That one o' Mr [oskar.sname]'s places?"
    pc "Mr [oskar.sname]? [oskar.name] is my landlord."
    police.name "Right. Wait a bit 'til things here are sorted. Go walk in the park or something."
    pc "What happened?"
    police.name "Bit o' trouble, nothing that concerns you."
    pc "Someone finally stabbed [oskar.name] in the eye or something?"
    police.name "That something a lot o' people would like to do?"
    pc "He's a slum landlord. The list of people is as long as my arm."
    pc "Err... Not me though. Nope. Whatever happened over there, nothing to do with me."
    police.name "Don't matter. We got the girl who did it. Didn't even try to run or hide."
    $ player.face_sad()
    pc "Oh? That's... Good?"
    pc "Wait, who did it? I might know them."
    police.name "..."
    pc "Who?"
    police.name "You know the girl who lives in that place?"
    $ player.face_shock()
    pc "[dani.nname]? Fuck!"
    police.name "Oh? You know the crazy bitch?"
    if dani.hate:
        $ player.face_annoyed()
        pc "Yeah, fucking lunatic."
        police.name "Oh, so something like this is not a surprise?"
        pc "Bitch went mental on me before. Tried to kidnap me."
        police.name "Well, Mr [oskar.sname] wasn't so lucky. He left in a body bag."
        $ player.add_mood(-200)
        $ player.face_worried()
        pc "Oh?"
        police.name "That's all? You don't give a fuck about the dead fella?"
        pc "Fuck him. He deserved worse. What happened to [dani.nname]?"
        police.name "Nothing. Found her stark naked covered in blood, but otherwise fine."
    else:
        $ player.face_annoyed()
        pc "She's my friend. And not crazy."
        police.name "Tell that to Mr [oskar.sname]'s corpse."
        $ player.add_mood(-200)
        pc "Corpse?"
        police.name "Yup."
        $ player.face_worried()
        pc "Is [dani.nname] okay?"
        police.name "\"Is [dani.nname] okay\"? You don't give a fuck about the dead fella?"
        pc "Fuck him. He deserved worse. So is [dani.nname] okay?"
        police.name "Yeah she's fine. Found her stark naked covered in blood, but otherwise fine."
    show police_gen2 at left4 with dissolve
    police2.name "We are done here. Pack up and we're off."
    police.name "Okay."
    hide police_gen2 with dissolve
    police.name "Look's like you can get in now."
    pc "..."
    police.name "Hey, between you and me. What the fuck happened? No one gives a shit this guy was murdered."
    pc "..."
    $ player.face_annoyed()
    pc "Raising rent prices to be unaffordable, then making us fuck him or work in his shitty casino to pay the debt."
    police.name "This girl, one of them?"
    pc "Yeah..."
    police.name "Right."
    $ player.face_worried()
    pc "What's going to happen to [dani.nname]?"
    police.name "She killed someone, so nothing good."
    police.name "But don't look like she's some gang member or proper criminal. So they probably go easy on 'er."
    pc "And what does that mean?"
    police.name "Probably put 'er to work on the farms or summit. Dunno."
    police.name "Go to the checkpoint and ask there."
    pc "Right."
    hide police_gen with dissolve
    pcm "Fuck, [dani.nname] killed that arse?"
    pcm "..."
    pcm "Can't say I am shocked..."
    pcm "Fuck, it's good she managed to do the job properly."
    if dani.hate:
        pcm "Both the lunatic and the scum landlord gone..."
        pcm "Not a bad result."
    pcm "..."
    if loc_kitchen.locked:
        pcm "Hmmm, with that cunt dead, I wonder if I can go back to staying at his place?"
        pcm "No harm in trying."
        $ loc_kitchen.locked = False
    jump travel

label dani_freakout_event_tell_troupe_picker:
    if anabel.hate:
        jump dani_freakout_event_tell_troupe_noana
    else:
        jump dani_freakout_event_tell_troupe_ana

label dani_freakout_event_tell_troupe_ana:
    $ add_to_list(dani.list, "dead_told_troupe")
    $ add_to_list(dani.list, "dead_anabel_knows")
    $ anabel.hate = True
    pc "Errm, girls... Can we talk?"
    show svet at right1
    show rachel at right2
    with dissolve
    show anabel at right3 with dissolve
    rachel.name "What's up [name]?"
    pc "Errm, so you know [dani.nname] lives nearby me?"
    rachel.name "Roomies!"
    pc "So on my way home there were a bunch of security guys hanging around my house."
    show svet worried
    show anabel worried
    svet.name "Oh fuck..."
    anabel.name "Oh no..."
    pc "Not sure the details, but [dani.nname] kinda killed our landlord and got arrested."
    show rachel happy
    rachel.name "Go [dani.nname]!"
    svet.name "[rachel.name]!"
    rachel.name "What? She hated that guy."
    svet.name "Fuck, this is crazy."
    show anabel angry
    anabel.name "What? No she can't have!"
    anabel.name "No way!!!"
    $ anabel.active = False
    hide anabel with dissolve
    pc "Err..."
    pc "Okay..."
    svet.name "Do you know what happened to [dani.nname], [name]?"
    pc "No details. But she was caught red handed. So whatever happens it wont be good."
    svet.name "Fuck..."
    pc "Yeah..."
    pc "..."
    svet.name "Thanks for telling us [name]."
    pc "Yeah..."
    hide svet with dissolve
    rachel.name "[dani.nname] rocks!"
    hide rachel with dissolve
    if not dani.hate:
        pc "Yeah... She does..."
    jump travel

label dani_freakout_event_tell_troupe_noana:
    $ add_to_list(dani.list, "dead_told_troupe")
    pc "Errm, girls... Can we talk?"
    show svet at right1
    show rachel at right2
    with dissolve
    rachel.name "What's up [name]?"
    pc "Errm, so you know [dani.nname] lives nearby me?"
    rachel.name "Roomies!"
    pc "So on my way home there were a bunch of security guys hanging around my house."
    show svet worried
    svet.name "Oh fuck..."
    pc "Not sure the details, but [dani.nname] kinda killed our landlord and got arrested."
    show rachel happy
    rachel.name "Go [dani.nname]!"
    svet.name "[rachel.name]!"
    rachel.name "What? She hated that guy."
    svet.name "Fuck, this is crazy."
    svet.name "Do you know what happened to [dani.nname], [name]?"
    pc "No details. But she was caught red handed. So whatever happens it wont be good."
    svet.name "Fuck..."
    pc "Yeah..."
    pc "..."
    svet.name "Thanks for telling us [name]."
    pc "Yeah..."
    hide svet with dissolve
    rachel.name "[dani.nname] rocks!"
    hide rachel with dissolve
    if not dani.hate:
        pc "Yeah... She does..."
    jump travel

label dani_freakout_event_tell_troupe_ana_alone:
    $ add_to_list(dani.list, "dead_anabel_knows")
    $ anabel.hate = True
    show anabel angry at right1 with dissolve
    $ player.face_worried()
    anabel.name "[name]!"
    pc "Hey [anabel.nname]..."
    anabel.name "Don't \"Hey [anabel.nname]\" me! What the fuck is this you told the girls?"
    pc "Yeah, [dani.nname] kinda got herself in trouble..."
    anabel.name "What bullshit is that? Why would she suddenly do something so crazy?"
    $ player.add_mood(-50)
    if dani.hate:
        $ player.face_angry()
        pc "Suddenly? She was on the fucking edge for ages."
        anabel.name "No she wasn't. She would have told me!"
        pc "Told you? You were the biggest fucking problem. Someone she loved always shitting on her."
        pc "Pushed her so far the fucking lunatic locked me in her room for days just for some comfort."
        anabel.name "What?!"
        pc "The nut job was on the brink a long time ago. Freaked out on me then went off and killed the landlord that was raping her."
        pc "But you too fucking blind to see past your own self."
        pc "Go fuck yourself and your anger."
        hide anabel
        $ walk(loc_from)
        pcm "Selfish cunt!"
        jump travel
    else:
        $ player.face_annoyed()
        pc "Suddenly? She was on the edge for ages."
        anabel.name "No she wasn't. She would have told me!"
        pc "Why would she? Biggest reason she was going mental was because of you."
        anabel.name "What?!"
        pc "You would never listen to her, only judge her and the rest of us for doing what we need to."
        pc "Your self righteous bullshit instead of being the friend she needed."
        pc "Now she's off on some prison farm or something while you get to sit here all smug."
        anabel.name "Fuck you [name]!"
        hide anabel with dissolve
        pcm "Yeah fuck you too..."
        jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
