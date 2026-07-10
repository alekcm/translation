label haven_whore_ending:

    show haven_guard3 at right3 with dissolve:
        xzoom 1
    havguard "Oh hello..."
    havguard "What we got ere?"
    havengateguard.name "Someone looking to escape the rats nest. Be nice."
    havguard "Sure sure. Will be very nice."
    $ player.face_worried()
    pcm "Fuck... What have I gotten myself into..."
    havguard "Come see me when you have worn him out."
    pc "..."
    hide haven_guard3 with dissolve

label haven_whore_ending_catcher:
    $ add_to_list(main_quest_05.list, "gangbanged")
    pcm "Fuck. This is going to be trouble"
    havguardw "Let's see what you got you sweet thing?"
    pc "Huh?"
    havguardw "Shake your ass a bit for us."

    if not player.has_perk([perk_whore, perk_slut, perk_sucu, perk_gamine]):
        pcm "Fuck fuck!"
        pcm "No choice but to play along with this..."
        pcm "I could just run..."
        pcm "Fuck. That would get me nowhere..."

    if player.vvirgin:
        pcm "Fuck. How did I manage to get into this situation?"
        pcm "Never even been with a man and now I have these vultures circling..."

    hide haven_guard1
    hide haven_guard2
    with dissolve
    $ player.face_happy()
    show haven_pose1 happy with dissolve
    pc "You like what you see?"
    havguardw "Oooh looking good."
    havguard2 "Nice!"
    pcm "They are all watching..."
    havguard1 "Let's see those tits!"
    pcm "..."
    $ player.face_neutral()
    show haven_pose1 norm
    $ c.top = 0
    pc "You like?"
    havguardw "Nice. Pierced nipples. Going to enjoy sinking my teeth into those."
    $ player.face_worried()
    pc "Don't be getting too excited or you will be done before we even start."
    havguardw "Don't worry about that love. Body like yours I am sure you will get me going again."
    havguardw "Let's see what you have hiding under those shorts."
    pc "Nothing you haven't seen from the other girls I am sure."
    havguardw "Other girls aren't here. Just you."
    pc "..."
    $ player.face_neutral()
    $ c.bottom = 0
    $ c.pants = 0
    show haven_pose1 norm with dissolve
    havguard1 "Whooo!"
    havguard2 "Fuck!"
    havguardw "Go away you horny toads!"
    havguard1 "Stop trying to hog her!"
    havguardw "Shoo!"
    havguardw "Bend over you sexy girl and let us have a better look."
    pc "Huh?"
    havguardw "Bend over. I want to see your sexy ass so show us what we are gonna enjoy"
    $ player.face_worried()
    show haven_pose1 worried with dissolve
    pc "..."
    $ player.face_neutral()
    show haven_pose1 norm with dissolve
    pc "Ok..."
    hide haven_pose1 with dissolve
    $ player.face_worried()
    show haven_presentass at right with dissolve
    pc "Like this?"
    havguardw "Ah fucking hell!"
    havguard1 "Damn girl! Whassat you have up yer arse?"
    havguard2 "Fuck yes shake it you whore!"
    havguardw "Piss off you lot. Let me have my fun."
    if player.has_perk([perk_whore, perk_slut, perk_sucu, perk_gamine, perk_exhibitionist]):
        pcm "Fuuuck so hot being bent over in front of these horny fucks."
    else:
        pcm "Fuck. Bent over in front of these guys. This is not going to go well."
    show haven_presentass lookdown with dissolve
    havguardw "Damn girl. You are probably the sexiest whore we have had in here."
    havguardw "Good thing you have that plug up there. Some o the girls before couldn't handle it but looks like you came prepared."

    if player.vvirgin:
        pcm "Hope it's not possible to know I am a virgin by looking at me..."
    if player.has_perk([perk_whore, perk_slut, perk_sucu, perk_gamine]):
        pc "Got to make sure you idiots can poke the right hole."
    else:
        pcm "That doesn't really make me feel any better..."

    show haven_presentass mast with dissolve
    havguardw "So smooth. Looks like you look after yourself and aren't too beaten to shit by the punters out there."

    if player.has_perk(perk_whore):
        pc "Yeah right. Those fuckers don't give a shit."
    else:
        pc "I try my best."

    $ player.spank()
    show haven_presentass lookback with dissolve
    pc "Ahh!"
    havguardw "So lovely."
    pc "Won't stay that way if you beat it like that."
    havguardw "Don't try and pretend you don't like it."
    pc "I..."
    $ player.spank()
    show haven_presentass lookdown with dissolve
    pc "Haaaa..."
    $ player.spank()
    havguardw "All you little whores love a good ass beating."
    havguardw "But I have something you will love even more..."
    show haven_presentass poke with dissolve
    show haven_presentass lookback with dissolve
    if player.vvirgin:
        pcm "Aw fuck. He's poking me..."
        pcm "Am I really going to have my first time pretending to be a whore while being watched by these perverts?"
    pc "Ah, what you doing? People are watching."
    havguardw "Not watching but waiting their turn."
    if not player.has_perk([perk_whore, perk_slut, perk_sucu, perk_gamine]):
        pcm "Fuck!"
        pc "Hey, I am not av..."
    else:
        pc "Oh?"

    $ player.sex_vag(havenguardgb, main_quest_05)
    show haven_presentass inside lookdown with dissolve
    pc "Haaa fuck fuck!"
    if player.desire >= 200:
        $ player.sex_cum(havenguardgb, "self", main_quest_05)
        pc "Haaa fuuuuccck! ♥"
        pc "Uuugg ♥"
        havguardw "Not just a whore but a slut as well. Fuck they are the best."
        pc "Huffff..."
    pc "Ahhhh."
    $ player.spank()
    havguardw "Take it you dirty little bitch."
    with hpunch
    pc "Ahhh yes!"
    pc "Take me."
    if not player.has_perk([perk_whore, perk_slut, perk_sucu, perk_gamine]):
        pcm "Fuck I can't believe this is happening..."
    havguardw "Love it when whores come up here. Hope you were paid well cos you are gonna work for it."
    if player.has_perk([perk_slut, perk_sucu]):
        pcm "Not getting anything for this. A big cock in me is enough."
    else:
        pcm "Not getting anything for this. Should make that fucking [tucker.name] pay for it."
    if not player.has_perk([perk_whore, perk_slut, perk_sucu, perk_gamine]):
        pcm "Assuming I let him live for all this..."
    with hpunch
    pc "Haaa!"
    havguardw "Ah yes fuck!"
    with hpunch
    havguardw "Take it you dirty bitch!"
    $ player.spank()
    havguardw "Ah yes yes!"
    show haven_presentass lookback with dissolve
    pc "Ah wait hold on..."
    $ player.sex_cum(havenguardgb, "inside", main_quest_05)
    havguardw "Ahhhhhh!"
    show haven_presentass lookdown with dissolve
    if not player.has_perk([perk_whore, perk_slut, perk_sucu, perk_gamine]):
        pcm "Fuck..."
    pc "Ahhh yes I can feel it."
    if not player.has_perk([perk_whore, perk_slut, perk_sucu, perk_gamine]):
        pcm "Fuck fuck!"
    havguardw "Fuck yes!"
    havguardw "Such a nice little slut."
    $ player.spank()
    pc "Ah!"
    show haven_presentass lookback with dissolve
    pc "That you done?"
    havguardw "Haa. Don't sound too happy..."
    show haven_presentass noman with dissolve
    pc "..."
    pc "I am all leaking now..."
    havguardw "Good whores should always be leaking."
    show haven_presentass lookdown with dissolve
    pc "..."
    hide haven_presentass with dissolve
    havguard1 "Finished with the whore?"
    havguardw "Yeah, have fun."
    pc "Wait what?"
    havguard1 "Ah yes about time."
    pc "Wait hold on. Stop taking your clothes off."
    $ player.face_shock()
    show haven_kiss hav_off vestoff trouoff with hpunch
    pc "*Mmmffff!"
    havguard1 "Mmm, tasty little bitch."
    havguard1 "Now get on yer knees. I don't wanna put that dick in your dirty pussy."
    pc "..."
    $ player.face_worried()
    hide haven_kiss with dissolve
    pcm "I need to bide time til these shits are asleep so I can sneak out and speak to [alex.fname] [alex.sname]..."
    pcm "Fuck, am I going to have to go through all of them before I can manage that..."
    show haven_blow wait ub with dissolve
    havguard1 "Well it ain't gonna suck it's self."

    if player.check_nowill():
        pc "..."
    else:
        pc "Doesn't do any harm to be nicer."
        show haven_blow ah
        $ player.punch()
        pc "Ah!"
        havguard1 "Shut up. You are a whore and your mouth is for being fucked so stop talking and use it for what it's meant for."

    $ player.face_worried()
    pcm "What a cunt!"
    $ player.sex_oral(havenguardgb, main_quest_05)
    show haven_blow 1h with dissolve
    pcm "Should bite this cunts cock off..."
    pcm "Heh, will get me killed but might be worth it."
    pcm "One chomp is all it would take..."
    show haven_blow wait ub with dissolve
    havguard1 "..."
    pcm "Arsehole!"
    show haven_blow 2h with dissolve
    pcm "Get this idiot off so he will go away."
    pc "*Hyuk* *Hyuk* *Hyuk*"
    havguard1 "Ah that's better."
    pcm "Fuck you."
    pc "*Hyuk* *Hyuk* *Hyuk*"
    havguard1 "Haaa."
    pcm "Shut up and cum."
    havguard1 "Ahhh yes fuck!"
    $ player.sex_cum(havenguardgb, "mouth", main_quest_05)
    pc "Mmmmffff!"
    havguard1 "Ahh fuck yes..."
    havguard1 "Huuuuu..."
    show haven_blow wait with dissolve
    if player.check_nowill():
        show haven_blow ub with dissolve
        show haven_blow neutral with dissolve
        hide haven_blow with dissolve
        havguard2 "Right, enough of you bullying the poor girl."
    else:
        show haven_blow ah with dissolve
        pc "*Ptew*"
        pc "Not swallowing your shit."
        hide haven_blow with dissolve
        havguard1 "Bitch!"
        havguard2 "Okay that's enough. Act like a prick and people will treat you like one."
        havguard1 "Hrmf."

    havguard2 "Here, wash your mouth out with this."
    pc "What is it?"
    havguard2 "Some 'o [havenvik.name]'s stuff."
    pc "Sounds good."
    $ haven_drink_brew()
    pc "*HACK* *COUGH*"
    pc "*PHEW*"
    pc "Ahh hit's the spot."
    havguard2 "Right?"
    havguard2 "Got another if you want. Help you get through this."
    pc "..."
    pc "Sure..."
    havguard "Heh, no worries. Here."
    $ haven_drink_brew()
    pc "*COUGH* *COUGH*"
    pc "Goes down better *COUGH* the second time..."
    havguard2 "If you say so."
    pc "Phew."
    havguard2 "Here, come to the bed."
    pc "Ah. You want to have sex as well?"
    havguard2 "Of course. Might not be a cunt like 'im but when [alex.nname] sends a whore I'm going to make use of her."
    havguard2 "Come on, hop on top."
    pc "..."
    pc "Ok..."
    pcm "When is this going to end?"
    show haven_gangbang penisup at right
    with dissolve
    pc "Ah already standing up?"
    havguard2 "Of course. Been hard since you started your show."
    pc "My show..."
    havguard2 "Hope you're ready."
    $ player.sex_vag(havenguardgb, main_quest_05)
    show haven_gangbang penisvag with dissolve
    havguard2 "Ah went in nice an easy."
    pcm "Still leaking the previous guys cum so of course it did..."
    pc "Ah yes so good!"
    pcm "Come on. How many more times..."
    havguard2 "Ah yes you are fucking amazing."
    pc "Oh yes I love your cock in me! ♥"
    with hpunch
    pc "Fuck me harder!"
    with hpunch
    havguard2 "Ah yes yes you perfect little whore! And such nice tits."
    pc "Want to see more of them? ♥"
    hide haven_gangbang
    show haven_cowgirl
    with dissolve
    havguard2 "Mmmm. So lovely. Glad I can have a turn before some rich fucker takes you as his own."
    pc "Huh?"
    havguard2 "Sexy little things like you normally get taken long before we get a turn."
    pc "Ah. Not interested in being property. Rather get drunk and fuck you scum all day."
    with hpunch
    havguard2 "Ahh yes!"
    hide haven_cowgirl
    show haven_gangbang penisvag at right
    with dissolve
    havguard2 "Come here!"
    $ player.spank()
    pc "Ahhh! ♥"
    havguard2 "Knew you loved it before."
    $ player.spank()
    $ player.spank()
    pc "Fuuuuuccckkkk..."
    pc "Haaa..."
    $ player.spank()
    havguard1 "Looks like the whore is enjoying herself."
    havguard2 "Piss off and wait yer turn."
    havguard1 "Don't be so selfish. She can handle some more."
    $ player.sex_oral(havenguardgb, main_quest_05)
    show haven_gangbang blow manblow with hpunch
    pc "Mfff!!!"
    havguard1 "Ah yes. I couldn't wait."
    havguard2 "Idiot, I don't want to be looking at your cock while I'm fucking her."
    havguard1 "Then look at her tits."
    pc "Mfff!!!"
    if player.has_perk([perk_slut, perk_sucu]):
        pcm "Mmmm. Give me more!"
    else:
        pcm "Fuck this is starting to get out of hand."
    show haven_gangbang plugpull with dissolve
    pc "Hmmmmmmffff????"
    if player.has_perk([perk_slut, perk_sucu]):
        pcm "Mmm fuck yes. Take that plug out and put something bigger in it's place!"
    else:
        pcm "The fuck? Someone pulling at my plug?"
    havguard2 "What you doing?"
    havguard3 "If we aren't waiting anymore then I am having a go as well before you break her."
    if not player.has_perk([perk_whore, perk_slut, perk_sucu, perk_gamine]):
        pcm "Fuck no no no!"
    pc "Hmmmmmmffff!!"
    show haven_gangbang noplug with dissolve
    havguard2 "Looks like she loves it anyway."
    if player.has_perk([perk_slut, perk_sucu]):
        pcm "Fuck yes!"
    else:
        pcm "Fuck no!"
    pc "Hmmmmmmffff!!"
    $ player.spank()
    pc "Mfff!!!"
    $ player.sex_anal(havenguardgb, main_quest_05)
    show haven_gangbang anal with dissolve
    pc "###########!!!"
    pcm "FUFUFUFUFUFUFUCK!!!"
    if player.has_perk([perk_whore, perk_slut, perk_sucu, perk_gamine]):
        pcm "FUCK YES!!!!!"
    havguard3 "Ahh yes fuck yes!"
    havguard1 "Piss of you lot. Stop trying to get in on the action."
    with hpunch
    havguard2 "Shut up you selfish bastard."
    show screen blackout(25) with dissolve
    hide screen blackout with dissolve
    havmuff "Ah fuck yes fuck the bitch..."
    show screen blackout(50) with dissolve
    hide screen blackout with dissolve
    havmuff "So nice. Take it"
    $ player.spank()
    havmuff "Ah yes yes!"
    $ player.sex_cum(havenguardgb, "inside", main_quest_05)
    havmuff "Ahh fuck cumming!!!!"
    show screen blackout() with dissolve
    hide haven_gangbang
    show haven_spitroast at right
    hide screen blackout with dissolve
    havmuff "Ah fuck take it take it!"
    with hpunch
    havmuff "Yes yes!"
    show screen blackout() with dissolve
    hide haven_spitroast
    $ t.hour = 2

    $ player.sex_anal(havenguardgb, main_quest_05)
    $ player.sex_cum(havenguardgb, "anal", main_quest_05)
    $ player.sex_cum(havenguardgb, "anal", main_quest_05)

    $ player.sex_vag(havenguardgb, main_quest_05)
    $ player.sex_vag(havenguardgb, main_quest_05)
    $ player.sex_vag(havenguardgb, main_quest_05)
    $ player.sex_vag(havenguardgb, main_quest_05)
    $ player.sex_cum(havenguardgb, "pullout", main_quest_05)
    $ player.sex_cum(havenguardgb, "inside", main_quest_05)
    $ player.sex_cum(havenguardgb, "inside", main_quest_05)
    $ player.sex_cum(havenguardgb, "inside", main_quest_05)

    $ player.sex_oral(havenguardgb, main_quest_05)
    $ player.sex_cum(havenguardgb, "face", main_quest_05)
    $ player.sex_cum(havenguardgb, "chest", main_quest_05)
    $ player.sex_hideaction()

    show haven_gangbang noplug anal at right
    show screen blackout(25) with dissolve
    hide screen blackout with dissolve
    havmuff "Ah yes fuck the bitch!"
    show screen blackout(50) with dissolve
    hide screen blackout with dissolve
    havmuff "Take it!!"
    with hpunch
    show screen blackout(100) with dissolve

    jump haven_whore_ending_recover

label haven_whore_ending_recover:
    if not t.hour in [1,2,3,4]:
        $ player.sex_anal(havenguardgb, main_quest_05)
        $ player.sex_cum(havenguardgb, "anal", main_quest_05)
        $ player.sex_cum(havenguardgb, "anal", main_quest_05)

        $ player.sex_vag(havenguardgb, main_quest_05)
        $ player.sex_vag(havenguardgb, main_quest_05)
        $ player.sex_vag(havenguardgb, main_quest_05)
        $ player.sex_vag(havenguardgb, main_quest_05)
        $ player.sex_cum(havenguardgb, "pullout", main_quest_05)
        $ player.sex_cum(havenguardgb, "inside", main_quest_05)
        $ player.sex_cum(havenguardgb, "inside", main_quest_05)
        $ player.sex_cum(havenguardgb, "inside", main_quest_05)

        $ player.sex_oral(havenguardgb, main_quest_05)
        $ player.sex_cum(havenguardgb, "face", main_quest_05)
        $ player.sex_cum(havenguardgb, "chest", main_quest_05)
        $ player.sex_hideaction()
        $ working(60)
        jump haven_whore_ending_recover

    $ renpy.scene()
    $ player.sex_end()
    show haven_after at right
    pause 1
    $ player.face_worried()
    hide screen blackout with Dissolve(2)
    pc "Ugghhhhh..."
    pc "Ohhhhh..."
    pcm "Fuuck. What the hell..."
    pc "OW ow ow ow ow..."
    pcm "Uhhh. I can feel them leaking from everywhere..."
    pc "..."
    pcm "How many did I let fuck me?"
    pcm "Must have been half of [haven] considering how much is coming out."
    pcm "Ugh. Got to get out of here and do what I came here for."
    pc "Owww..."
    hide haven_after with dissolve
    pc "Oww ow ow..."
    pcm "Clothes. Where did they end up?"
    pcm "Top over there."
    pause 0.5
    $ c.top = work.top
    pause 0.5
    pcm "Fuck. I am sticky everywhere and now it's soaking into my clothes."
    pcm "No choice. Get dressed and out of here before someone else wants to fuck me"
    pcm "Where are my shorts?"
    pcm "Ah, my plug?"
    pcm "..."
    pcm "Should probably put it back in. No [emile.name] to do it for me."
    show screen sex_action_flash("anal")
    pcm "..."
    pcm "Well, that was a lot easier than the first time..."
    pcm "..."
    pcm "Ok. Shorts. Here we go."
    pause 0.5
    $ pc_dress()
    pause 0.5
    pcm "Right. Don't make too much noise..."
    pc "Ouch, ouch, ouch..."
    $ walk(loc_haven_hallway_3f)
    jump haven_access_top_floor_night_office









label haven_virginsex_ending:
    show haven_guard3 at right3 with dissolve:
        xzoom 1
    havguard "Oh hello..."
    $ player.face_worried()
    havguard "What we got ere?"
    havengateguard.name "Hands off!"
    havguard "Okay ok... Have fun."
    havguard "Come see me if you get bored of 'im."
    pc "..."
    hide haven_guard3 with dissolve
    pc "Nice friends you have there."
    havengateguard.name "Don't worry about them. They're just jealous cos they spend too much time with their hands."
    $ player.face_neutral()
    pc "As if you aren't the same."
    $ player.face_happy()
    pc "Bunch of lonely perverts the lot of you I bet."
    $ player.face_neutral()
    havengateguard.name "Well, not lonely today with you here. Look how lovely you look."
    show haven_pose1 happy with dissolve
    pc "You think so?"
    havengateguard.name "Pfft, just fishing now aren't you."
    pc "Maybe..."
    havengateguard.name "Of course you are. Most wonderful thing I have seen in this place since I have been 'ere."
    $ player.face_shy()
    pc "Sweet talker."
    $ player.face_neutral()
    havengateguard.name "It's true. Let me show you."
    hide haven_pose1
    hide haven_guard1
    show haven_kiss veston trouon hav_off
    with dissolve
    pc "Mfff."
    pcm "Mmmm. Wasn't expecting to be kissed."
    pcm "His hands are pressing me right against his crotch..."
    pc "Mmmff. Can feel you are enjoying yourself."
    havengateguard.name "Ah, can tell?"
    pc "Hard to miss."
    show haven_kiss vestoff with dissolve
    havengateguard.name "Can you blame me?"
    $ player.face_shy()
    pc "No..."
    pc "I might be the same..."
    pc "Mffff."
    $ player.face_neutral()
    $ c.top = 0
    show haven_kiss with dissolve
    havengateguard.name "Might be?"
    pc "Shush."
    pc "Mmmfff."
    show haven_kiss trouoff with dissolve
    pc "Oh!?"
    $ player.face_shock()
    pc "What's this?"
    havengateguard.name "Have a guess..."
    $ player.face_happy()
    pc "A mushroom!"
    havengateguard.name "Aw shut it."
    $ player.face_neutral()
    pc "Mmmfff!"
    $ c.bottom = 0
    $ c.pants = 0
    show haven_kiss with dissolve
    havengateguard.name "Such smooth skin. Your ass is wonderful."
    pc "Mmmff."
    havengateguard.name "Let me see some more of you."
    pc "Err..."
    hide haven_kiss with dissolve
    havengateguard.name "This is my bed."
    $ player.face_worried()
    show haven_onback worried at right with dissolve
    hide haven_guard1
    havengateguard.name "Fuck! So lovely."
    havengateguard.name "Can't believe how nice you look."
    pc "Don't just stand there gawking. It's embarrassing."
    havengateguard.name "Sure."
    show haven_onback mast with dissolve
    pc "Err..."
    havengateguard.name "What?"
    pc "It's..."
    pc "Huge!"
    havengateguard.name "Now who is being the sweet talker."
    show haven_onback pcmast with dissolve
    pc "Pfft. Not sweet talking. That thing will hurt."
    havengateguard.name "Well if that thing in your arse is anything to go by, it looks like you have had some practice."
    if player.vvirgin:
        pc "Never where you plan to put that thing..."
    else:
        pc "It doesn't go in that hole."
    havengateguard.name "Sure sure. I don't mind what girls do when they are alone."
    pc "..."
    show haven_onback rest with dissolve
    pc "Whatever..."
    havengateguard.name "Aw, only teasing."
    havengateguard.name "Need to warm you up first then there will be no problem."
    show haven_onback poke norm with dissolve
    pc "Ah. Wait until I'm ready and don't go poking too deep."
    havengateguard.name "Don't worry your sweet tits. I won't go too deep yet."
    show haven_onback poke oh with hpunch
    pc "Haa!"
    show haven_onback poke norm
    havengateguard.name "Just a little."
    pc "Careful."
    show haven_onback breast with dissolve
    havengateguard.name "Mmmm, wet and tight."
    with hpunch
    pc "Haaaa. Slowly..."
    show haven_onback ahh with dissolve
    havengateguard.name "That's right. Just lay back and enjoy."
    pc "Mmmmm."
    pc "Nice feeling you rub there."
    havengateguard.name "Mmm I bet. Warm a girl up and she will scream for it to be deeper."
    pc "Sure, if you say so."
    with hpunch
    pc "Ahhhh haaaa..."
    havengateguard.name "So fucking wet."
    show haven_onback up with dissolve
    pc "Mmmmmmm."
    havengateguard.name "Oh like it do ya?"
    pc "Haaaaa. ♥"
    pc "It's nice."
    with hpunch
    pc "Haaa fuck! ♥"
    havengateguard.name "Mmmm..."
    pc "Deeper."
    havengateguard.name "Oh?"
    pc "Deeper."
    with hpunch
    pc "Ahhhhhhhhh."
    $ player.sex_vag(havengateguard, main_quest_05)
    show haven_onback sex pain with dissolve
    pc "Nnnggggg!"
    havengateguard.name "Haaaaaaa... So warm."
    pc "Fuck fuck!"
    havengateguard.name "Relax..."
    pc "Fuck it's too big."
    havengateguard.name "I'll go slow."
    pc "Yes. Slow!"
    pc "Haaa fuck it's huge!"
    havengateguard.name "Mmmmm. So tight."
    pc "Haaaaa..."
    pc "Fuck, go slow. Take me slow."
    havengateguard.name "Mmmmm. Starting to enjoy?"
    pc "Haaa. Hurting less..."
    with hpunch
    pc "Ahhh."
    havengateguard.name "Mmmmm sexy little bitch. Really so tight"
    show haven_onback oh with dissolve
    pc "Haaaaaa I can feel it stretching me."
    with hpunch
    pc "Ahhhh fuck."
    if player.virgin_pregcheck:
        pcm "So huge for my first time. Fucking hurts but also feels good."
        pcm "I feel so stretched. Haaaaa..."
    else:
        pcm "Not my first time, but fuck it's still stretching me so much."
    pc "Ahhhh. Can go a little faster."
    havengateguard.name "Mmmm."
    with hpunch
    show haven_onback ahh with dissolve
    with hpunch
    pc "Fuck fuck yes!"
    with hpunch
    havengateguard.name "Dirty girl. Take it you little slut!"
    with hpunch
    pc "Haaaa. ♥"
    with hpunch
    pc "Ahh. ♥ Tooooo fast... ♥"
    with hpunch
    pc "Fuck fuck."
    with hpunch
    $ player.sex_cum(havengateguard, "self", main_quest_05)
    show haven_onback ag with hpunch
    pc "Aggggg oo fassssstt ♥"
    pc "HAAAAAA!!!"
    with hpunch
    pc "Waaaa aaaaa yaaaaa dooooiiinnn... ♥"
    pc "Sloooowwwww..."
    with hpunch
    havengateguard.name "Shhhhhhh..."
    havengateguard.name "Take it you tight little bitch!"
    pc "Haaaaaa..."
    havengateguard.name "Take it all inside!"
    with hpunch
    pc "Waaaaaaa???"
    havengateguard.name "Take my cum in you like a perfect whore."
    pc "Waaa waaiiii..."
    $ player.sex_cum(havengateguard, "inside", main_quest_05)
    show haven_onback
    with hpunch
    with hpunch
    with hpunch
    havengateguard.name "Ahhh fuckkkk!!!"
    with hpunch
    havengateguard.name "Yesssss!!!!"
    pc "You are pumping..."
    havengateguard.name "Ahhh yes!"
    show haven_onback ahh with dissolve
    pc "Phhhheeewww..."
    pc "*Hah* *Hah*"
    pc "..."
    show haven_onback norm with dissolve
    pc "Fuck that was intense."
    havengateguard.name "Telling me..."
    havengateguard.name "You were so tight I couldn't hold back."
    show haven_onback poke with dissolve
    havengateguard.name "Take every drop."
    if player.has_perk(perk_preg_want):
        pc "Yes. Pump it all inside."
    else:
        show haven_onback worried
        pc "Huh, wait what?"
        pcm "Fuck. Wasn't thinking about that..."
        show haven_onback norm with dissolve
    pc "Haaaa..."
    pcm "That was nice..."
    show haven_onback noman with dissolve
    havengateguard.name "Look at you you sexy thing."
    show haven_onback down rest thigh with dissolve
    pc "Hey, that's embarrassing..."
    havengateguard.name "Admiring my work seeing you with my cum."
    pc "Pervert! I can feel it leaking out of me."
    $ t.hour = 1
    havengateguard.name "Then we better poke it back in."
    show haven_onback poke worried with dissolve
    pc "Ha what?"
    pc "What are you doing?"
    $ player.sex_vag(havengateguard, main_quest_05)
    show haven_onback sex up oh with dissolve
    pc "Ahhh fuck!"
    havengateguard.name "Much easier going back in."
    pc "Fuck fuck!"
    pc "Haaaaa shit. ♥"
    pc "Haaaa..."
    show haven_onback norm with dissolve
    pc "How are you even still hard?"
    havengateguard.name "I have my ways."
    pc "Oh?"
    pc "Ooooh?"
    pc "Fuck. I'm in trouble..."
    havengateguard.name "Damn right you are."
    show haven_onback ahh with hpunch
    pc "Ahhhh... ♥"
    pc "Fuck yes!"
    with hpunch
    havengateguard.name "Turn you into a right cock hungry whore!"
    with hpunch
    pc "Ah yes keep going!"
    pc "Ahhhh never felt like this before. ♥"
    havengateguard.name "Wanna get on top?"
    show haven_onback norm with dissolve
    pc "Sure. Sounds nice."
    show haven_onback poke with dissolve
    show haven_onback noman with dissolve
    havengateguard.name "Get up."
    hide haven_onback with dissolve
    havengateguard.name "Like that... Yes."
    show haven_cowgirl with dissolve
    pc "Like looking at my tits?"
    havengateguard.name "Mmm, they are lovely."
    with hpunch
    pc "Ahhh so much deeper. You are so big inside me."
    havengateguard.name "Mmmm, I can feel you gripping it. Full of my cum and still going."
    pc "Haa haa haa."
    hide haven_cowgirl
    show haven_gangbang at right
    with dissolve
    pc "Fuck yes. Let me feel you in me pumping it."
    pc "Yes yes yes!"
    pc "Ahhhhhh..."
    $ player.sex_cum(havengateguard,"self", main_quest_05)
    with hpunch
    pc "Ahhh fuck yes yes!"
    pc "Haaaaa."
    pc "*Huff* *Huff* *Huff*"
    $ player.spank()
    pc "Aiiiee!"
    $ player.spank()
    pc "Haaa. What are you doing?"
    havengateguard.name "Spanking that sexy ass you have."
    pc "*Huff*"
    pc "Who told you that you co..."
    $ player.spank()
    havengateguard.name "All girls love a good spanking."
    pc "Who told you that?"
    havengateguard.name "All the girls I have spanked."
    $ player.spank()
    pc "Haaaa. Calm down a bit."
    with hpunch
    havengateguard.name "Take it!"
    pc "Oh?"
    pc "Ready to pump me again?"
    havengateguard.name "Ahhh almost!"
    $ player.spank()
    pc "Haa!"
    $ player.sex_cum(havengateguard, "inside", main_quest_05)
    with hpunch
    havengateguard.name "Ahhhhh!"
    pc "Ooohhh..."
    havengateguard.name "Yes take it slut!"
    $ player.spank()
    pc "Haa. ♥ I feel it."
    havengateguard.name "Haaaaa..."
    havengateguard.name "Mmmm, I could get used to this."
    pc "Mmmmm I bet."
    show haven_gangbang penisup with dissolve
    pc "Oooh. Making me leak again?"
    havengateguard.name "Mmmm. Another time I will take that plug out and fill your arse with something bigger."
    pc "Promises promises..."
    $ t.hour = 1
    pc "Phew..."
    show screen blackout(25) with dissolve
    hide screen blackout with dissolve
    pc "Ahhh, So exhausted..."
    if t.hour in [17,18,19,20,21,22,23,0,1,2,3]:
        show screen blackout(100) with dissolve
        hide haven_gangbang
        $ time_working_to(1,12)
        show haven_onback down norm
        hide screen blackout with Dissolve(2)
        pc "Ugghhhhh..."
        pc "Ohhhhh..."
        pcm "Ah, it's late..."
        pcm "I need to be quiet and sneak out of here"
        pcm "Uhhh. Still feel him leaking out of me..."
        pcm "Ugh. Got to get out of here and do what I came here for."
        pc "Owww..."
        hide haven_onback with dissolve
        pcm "Clothes. Where did they end up?"
        pcm "Top over there."
        pause 0.5
        $ c.top = work.top
        pause 0.5
        pcm "Ok. Shorts. Here we go."
        pause 0.5
        $ pc_dress()
        pause 0.5
        pcm "Right. Don't make too much noise..."
        $ walk(loc_haven_hallway_3f)
        jump haven_access_top_floor_night_office
    else:
        $ player.spank()
        pc "Aie!"
        havengateguard.name "Don't be falling asleep. I need to get back to the gate."
        pc "What? Really?"
        havengateguard.name "Yeah. Can't be laying in bed with you all day. Already got someone covering me but he won't be happy if I take the whole day off."
        pc "Ok..."
        havengateguard.name "Don't worry. Just relax here and I'll come back after my shift is done."
        pc "Ok. See you then."

        hide haven_gangbang with dissolve
        pause 0.5
        show haven_guard1 at right1 with dissolve
        havengateguard.name "Here's your clothes."
        pc "Thanks."
        pause 0.5
        $ pc_dress()
        pause 0.5
        havengateguard.name "Mmmm, sexy little thing."
        show haven_kiss veston trouon hav_off with dissolve
        pc "Mmmmffff."
        hide haven_kiss with dissolve
        havengateguard.name "See ya later."
        hide haven_guard1 with dissolve
        pc "..."
        pc "Ok..."
        pcm "Now what?"
        pcm "I finally got upstairs but now what?"
        pcm "I could just go and walk into [alex.fname] [alex.sname]'s office and try and have a chat with him."
        if not player.check_nowill():
            pcm "Or hang around here. But not sure how long the nice guard will take and this place is a sausage fest..."
            pcm "Fuck. Nice guard... I didn't get his name even after all that talking."
            pcm "Hmmm."
            menu:
                "Go directly to the office":
                    pcm "Best to get out of here now I think and try and have a chat with [alex.fname] [alex.sname]. Hopefully he doesn't get too upset at me for barging in."
                    pause 0.5
                    $ walk(loc_haven_hallway_3f)
                    pause 0.5
                    jump haven_access_top_floor_day_office_enter
                "Stay here and wait until night time":

                    $ NullAction()



        pcm "No... He will be in there with people and will probably beat me up or something."
        pcm "I need to wait until night and catch him off guard so he is afraid of me."
        pcm "Fuck, that means I have to hang around here til night..."
        pcm "Ugh..."
        show haven_guard2 at right1 with dissolve
        havguard "Left you all alone has he?"
        pc "Huh?"
        havguard "Had his fun so now he leaves the rest to us?"
        havguard "Mmmm, I don't mind."
        havguard "Doesn't matter if he's still inside you. Sexy whore like you is worth it."
        pc "Wait what?"
        havguard "Come over here and let's have some fun."
        pc "What? No I am just waiting for him to come back."
        havguard "Yeah right. Then why aren't you hanging out with him downstairs instead of round here with a bunch of guys?"

        if not player.check_nowill():
            pcm "Fuck he's right. A normal person would hang out by the gate with him. But here I am waiting around like a fool so I can sneak into [alex.fname] [alex.sname]'s office."
            pc "Yep, that's what I will do. See ya."
            pause 0.5
            hide haven_guard2
            $ walk(loc_haven_hallway_3f)
            pause 0.5
            pcm "No choice. Got to speak to [alex.fname] [alex.sname] now or end up passed around by that lot."
            pause 0.5
            jump haven_access_top_floor_day_office_enter
        else:

            pc "Err..."
            pc "I'm just..."
            havguard "Yeah sure. Come on let's get a good look at you."
            jump haven_whore_ending_catcher
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
