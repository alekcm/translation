label school_dance_show_9:
    $ school_dance_quest_show_count += 1
    $ remove_from_list(dani.conversation_topics, ["dance_went_alone","dance_went_alone_followup"])
    if "dance_went_alone_had_conversation" in dani.conversation_topics:
        show dani dance at right1 with dissolve
        pc "Almost ready?"
        show dani worried
        dani.name "Yeah..."
        pc "You ok?"
        dani.name "That guy said he would come and watch again."
        pc "Oh?"
        dani.name "Yeah... I was thinking..."
        show rachel dance at left2 with dissolve
        rachel.name "You guys ready?"
        dani.name "Err, yeah."
        rachel.name "Come on then."
    $ add_to_list(rachel.list, "no_location")
    $ add_to_list(dani.list, "no_location")
    $ add_to_list(anabel.list, "no_location")
    $ add_to_list(svet.list, "no_location")
    $ walk(loc_school_gym, trans=False)
    show svet dance at right1
    show rachel dance at left3
    show anabel dance at left1
    with dissolve
    show dani dance neutral at left2
    with dissolve
    svet.name "So, we did pretty well last time so I guess we do the same?"
    dani.name "Yeah."
    rachel.name "Whoo!"
    hide rachel with dissolve
    svet.name "She's too eager..."
    dani.name "Mmmm."
    hide dani
    with dissolve
    $ walk(loc_school, trans=False)
    hide svet
    hide anabel
    with dissolve
    pause 0.3
    $ walk(loc_busstop_school, trans=False)
    $ remove_from_list(rachel.list, "no_location")
    $ remove_from_list(dani.list, "no_location")
    $ remove_from_list(anabel.list, "no_location")
    $ remove_from_list(svet.list, "no_location")

    show dani dance at right1
    show rachel dance at right2
    with dissolve
    rachel.name "So, got the pink ones on today?"
    if not c.pants:
        dani.name "Just her bare arse under there."
        show anabel dance at right3 with dissolve
        rachel.name "You saw?"
        dani.name "Yeah..."
        pc "You guys should try it."
    else:
        show anabel dance at right3 with dissolve
        pc "No, just the normal ones."
        rachel.name "Shame. Could have made more money with them."
        dani.name "Mmmm."
        pc "Then you guys put them on."
    show dani happy
    dani.name "Ah. Didn't think of that."
    show rachel happy with dissolve:
        xzoom -1
    rachel.name "Next time we should."
    anabel.name "What? Seriously?"
    show rachel with dissolve:
        xzoom 1
    if c.pants:
        rachel.name "Yeah why not?"
    else:
        rachel.name "Something nice and small to wear. Not like that pervert."
    dani.name "Bus is here."
    hide dani with dissolve
    hide rachel
    hide anabel
    $ walk(loc_bus_interior, trans=hpunch)
    $ player.face_worried()
    pause 0.5
    show rachel dance at left1 with hpunch:
        xzoom -1
    rachel.name "Hup!"
    show rachel happy
    rachel.name "Hey~~"
    $ player.face_neutral()
    pc "Err. What's with that look?"
    rachel.name "Wondering if someone will poke you in the bum again."
    $ player.face_worried()
    pc "Ugh!"
    if c.pants:
        rachel.name "Don't worry. If someone tries then I'll take your knickers off for you."
        if player.isslut:
            pc "Great. Leaking instead of wet pants is just what I need."
        else:
            pc "Err... That's just going to make things worse."
            rachel.name "Pfft."
    else:
        rachel.name "No knickers will make it easy for them."
        pc "Great. Leaking instead of wet pants is just what I need."
    show rachel with dissolve:
        xzoom -1
    rachel.name "Looks like it's [dani.nname] who's getting the attention today though."
    if player.has_perk([perk_slut, perk_bimbo]):
        $ player.face_happy()
    else:
        $ player.face_worried()
    pc "Ah, yeah looks like it."
    rachel.name "Maybe I should go over there and get her knickers off."
    $ player.face_neutral()
    if player.has_perk([perk_slut, perk_bimbo]):
        pc "Hah. Not sure she would appreciate that."
        rachel.name "The guy would though."
        pc "Mmmmm."
    else:
        $ player.face_worried()
        pc "Don't be so mean."
        rachel.name "Just helping her have some fun."

    show anabel dance angry at left2 with vpunch:
        xzoom -1
    anabel.name "Ugh, it's our stop."
    hide anabel with vpunch
    rachel.name "Let's go."
    hide rachel with vpunch
    pause 0.5
    $ walk(loc_busstop_residential, trans=False)
    show rachel dance at right1
    show anabel dance at right2
    with vpunch
    $ player.face_annoyed()
    pc "Damn bus!"
    rachel.name "Heh."
    hide anabel
    hide rachel
    $ walk(loc_park)
    show svet dance at right1
    with dissolve
    svet.name "Right, gather round."
    show rachel dance at left3 with dissolve
    rachel.name "So, same again?"
    svet.name "Pretty much. Where's the rest?"
    show anabel dance worried at left2 with dissolve
    anabel.name "Hmmm. Looks like [dani.nname] got stuck on the bus..."
    show rachel with dissolve:
        xzoom 1
    rachel.name "Really?"
    anabel.name "Mmm, didn't see her get off."
    rachel.name "Well, she was wrapped in the arms of some pervert last I saw. Might have ended up stuck with him."
    anabel.name "She was?"
    rachel.name "Yeah, she'll get off at the next stop and walk here. Let's get stuff ready."
    show anabel neutral
    hide rachel with dissolve
    anabel.name "..."
    svet.name "Err..."
    svet.name "Well, you know what to do. Clean a space and set up the music. We'll wait for [dani.nname] to arrive then get to it."
    anabel.name "Right..."
    hide anabel
    hide svet
    with dissolve
    "I help the rest of the girls with cleaning all the litter and other junk from the floor and help set up the music box."
    show dani dance at right1 with dissolve
    dani.name "Uff!"
    show rachel dance at right2 with dissolve:
        xzoom -1
    rachel.name "Ah you got here?"
    dani.name "Yeah, got caught up on the bus and missed the stop."
    rachel.name "I saw. Need some new underwear?"
    dani.name "No, it's fine. Everything set up?"
    rachel.name "Yeah, just waiting on you."
    svet.name "All here?"
    show svet dance at right1
    show rachel dance at left3
    show dani dance at left2
    with dissolve
    show anabel dance at left1 with dissolve
    svet.name "You okay [dani.nname]?"
    dani.name "Yeah, just missed my stop."
    svet.name "Right. Well we've done this enough already so you all know what to do."
    rachel.name "Yup!"
    $ renpy.scene()
    $ show_dance_image()
    "We do our usual routine as we have practised and the crowd is pretty lively. It seems people have come to expect us here so we have a larger following than any of the previous shows we have done."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_21
    "As usual, [rachel.name] is playing along with the crowd and keeping them entertained. But surprisingly [dani.nname] is joining in with her. She seems to have developed a lot of confidence doing this."
    "[dani.nname] and [rachel.name] are often breaking from the routine to dance closer to members of the audience. As the routine goes on, I start to follow suit."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_22
    "I soon realise how touchy the men get when dancing close to them. But it's clear the crowd is more lively than usual so I just go along with it."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_23
    "The show comes to an end and some of us work the crowd to squeeze tips out of everyone."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_24
    "I suffer the invading hands as best I can until it looks like the only people left are those who have no intention of chipping in. So I make my way over to the rest of the girls."
    $ renpy.scene()
    with dissolve
    show svet dance at right1
    show rachel dance at left3
    show anabel dance at left1
    show dani dance at left2
    with dissolve
    svet.name "Right girls, let's see how we did."
    svet.name "...[rachel.name]'s... [name]'s..."
    svet.name "There we go."

    if c.pants:
        $ player.add_money(60)
        svet.name "Bit less than last week but still not too bad."
        dani.name "Less? Wonder how we managed that. Crowd seemed pretty lively."
        rachel.name "[name] wasn't flashing her arse this week is why."
        pc "You say that like these ones hide much."
        rachel.name "Mmm, but pink is an attractive colour."
        pc "..."
        dani.name "Ah!"
        dani.name "Yeah it is..."
    else:
        $ player.add_money(65)
        svet.name "Similar to last week. [name] managed the most again..."
        rachel.name "[name]'s arse saves the day."
        pc "You say that like yours hide much."
        rachel.name "What you have is much more attractive to this lot."
        dani.name "Yeah it is..."

    rachel.name "Anyway, I'm off. See ya."
    svet.name "Mmm, see you guys."
    hide rachel
    hide svet
    with dissolve
    show dani with dissolve:
        xzoom 1
    anabel.name "You heading home [dani.nname]?"
    dani.name "No, I have stuff to do so see you round."
    anabel.name "Ok, be safe."
    hide anabel with dissolve
    if not "dance_went_alone_had_conversation" in dani.conversation_topics:
        dani.name "See you [name]."
        pc "See you."
        hide dani with dissolve
        pc "..."
        show sb_pose_upskirt with dissolve
        pc "One day I am going to remember to not be left here alone with my arse out..."
        pc "Oh well..."
        hide sb_pose_upskirt with dissolve
        $ dani_yan_max_add(30)
        jump travel

    $ remove_from_list(dani.conversation_topics,"dance_went_alone_had_conversation")
    dani.name "Err..."
    pc "Hmmm?"
    dani.name "So that guy from last week wants me to hang out with him again today."
    pc "Ok."
    dani.name "I was wondering if you wouldn't mind hanging out for a bit and wait for me to make sure everything is ok?"
    pc "You want me to hang out with you? Err..."
    dani.name "No no. Just... Kind of wait around somewhere you can see us."
    pc "You know I am wearing the same tiny skirt as you. He will notice."
    dani.name "That's fine. I'd just feel safer if you were around in case I need to get away quick."
    if not player.check_sex_agree(2):
        $ player.face_worried()
        pc "It's not something I feel comfortable doing. Especially not out here in this tiny dress alone..."
        pc "Plus, I stink and need a shower..."
        pc "Sorry [dani.nname]..."
        dani.name "Mmm. It's fine..."
        dani.name "Well, I'm going. See you."
        pc "Mmm, be safe."
        hide dani with dissolve
        pc "..."
        pc "Hope I don't regret that..."
        $ dani_yan_max_add(30)
        jump travel
    else:
        menu:
            "Hang out with [dani.nname]":
                $ NullAction()
            "Refuse and go home":
                $ dani_yan_max_add(30)
                pc "Sorry [dani.nname], but I have stuff I need to do..."
                pc "Plus hanging out here in this tiny dress..."
                dani.name "Mmm. It's fine..."
                dani.name "Well, I'm going. See you."
                pc "Mmm, be safe."
                hide dani with dissolve
                pc "..."
                pc "Hope I don't regret that..."
                jump travel

    $ dani_yan_max_add(10)
    $ add_to_list(dani.conversation_topics, "dance_waited_during_date")
    pc "I guess. Bit strange to just hang out in the park dressed like this though."
    pc "No choice I guess. Go meet your friend and I'll try and keep an eye on you."
    show dani happy
    dani.name "Thanks a lot [name]! I'll try not to be too long."
    pc "Not sure it will be you making that decision."
    dani.name "Err, true..."
    dani.name "I guess if things get a bit much you can probably come over."
    pc "Two for the price of one? Ha! Go and do what you need to. I'll find somewhere to hang out."
    dani.name "Right."
    hide dani with dissolve
    if weather_var == 3:
        pcm "Hope she is getting good money for this while I hang out in the pissing rain."
    elif t.month in ["Winter", "Autumn"]:
        pcm "Hope she is getting good money for this. Gonna freeze my tits off hanging round here like this."
    else:
        pcm "Hope she is getting good money for this."
        pcm "At least the weather is nice so won't look too strange me wearing a skirt that doesn't hide my arse."
    pcm "Hmm, so where should I hang out?"
    pcm "Could just sit on a bench out in the open, but dressed like this I am going to attract all manner of attention just siting there."
    pcm "Or I could hide somewhere. Ends up making me look like the pervert spying on people though."
    menu:
        "Sit on a bench in the open":
            jump school_dance_show_9_bench
        "Stay a bit hidden":
            jump school_dance_show_9_hide

label school_dance_show_9_bench:
    $ add_to_list(dani.conversation_topics, "dance_waited_police")
    pcm "Might look a bit odd me hanging around like this, but I suppose I can relax a bit while waiting for her."
    $ player.face_worried()
    pcm "..."
    $ player.add_mood(-10)
    pcm "Now I am alone without the girls I am getting strange looks..."
    $ player.face_neutral()
    pcm "Maybe I should sit somewhere."
    "I head over to one of the empty benches and sit down making sure I can still see [dani.nname]."
    pcm "What is [dani.nname] up to?"
    show dance_dani_bench with dissolve
    pcm "Oh?"
    $ relax(15)
    pcm "Okay then..."
    pcm "And people are giving me the eye. She's there like that on the bench having fun yet I am the unusual one."
    hide dance_dani_bench with dissolve
    $ player.face_worried()
    show police_gen with dissolve
    police.name "What'cu doin' 'ere? S'posed to be at the highway doin' this shit."
    pc "Err, I'm just waiting for my friend."
    police.name "Yeah, like all o y're doin'. Don't recognise you. New one out 'ere?"
    if player.check_speech(3):
        pc "New? New what? I'm not round here much."
        police.name "S why you 'ere and not the highway?"
        if player.iswhore:
            pc "I'm no here whoring. Just finished a dance gig and waiting for my friend."
        else:
            pc "Highway? Oh... Errm, I'm not like that. We just finished a dance gig and I'm waiting for my friend."
        pc "This is our dance outfit, not... err, a \"work\" outfit."
        police.name "Hmmm..."
        police.name "And ya friend? Where is he?"
        pcm "Fuck. If I point over to [dani.name], he's gonna see her getting felt up and know for sure whoring is going on..."
        pc "Dunno, that's why I'm waiting here. Supposed to meet..."
        police.name "Yeah sure. Come on. With me."
        pc "What?"
        police.name "You're a new face. Gotta pay ya dues. Come with me."
        if player.check_nowill():
            pcm "Fuck!"
        else:
            pc "Ah no! I see her there! Sorry, gotta go."
            hide police_gen with Dissolve(0.2)
            pcm "Fuck!"
            show dani dance at right1 with dissolve
            pc "Hey."
            dani.nname "Hey, everything ok?"
            pc "Yeah, just had to get away from a guard. Hanging round here dressed like this was drawing attention."
            dani.name "Ah, how did you get away?"
            pc "I just told him I see my friend and rushed off."
            jump school_dance_show_9_interrupt
    else:
        pc "Huh?"
        police.name "I know mosta the whores round 'ere, but you a new face. Jus start out?"
        pc "What? I don't know what you are saying."
        police.name "Fucking bint! Asking ya if you are a new whore. I ain't seen ya face before."
        police.name "Should know ya can't fuck around 'ere."
        $ player.face_shock()
        pc "Wha...?"
        police.name "*Tsk* Talking t'a dense post. Come on. Come wit me."
        pc "What for?"
        police.name "Pay ya dues then ya can fuck off."
        pc "What the... Pay what?"
        police.name "C'mon dumb fuck or I'll drag you."
        pcm "Fuck fuck. What the fuck is this idiot even saying..."

    $ add_to_list(dani.conversation_topics, "dance_waited_police_blowjob")
    "He takes me by the arm and starts walking me somewhere, totally ignoring my protests."
    $ walk(loc_bushes)
    with vpunch
    $ player.face_worried()
    pc "What are we here for?"
    police.name "Pay ya dues. I'm still on t' clock so be quick."
    pc "I don't know what you want..."
    show police_gen at right6 with dissolve
    "The guard puts his hands on my shoulders and pushes me down. As he is pushing I finally realise what he wants from me."
    pcm "Fuck, he thinks I'm a whore. So paying dues is to give them free service?"
    pcm "Fuck fuck!"
    show sb_blowjob shock worried
    hide police_gen
    with hpunch
    pcm "Shit, this is happening."
    show sb_blowjob down frown with dissolve
    "The guard starts unbuttoning his trousers and starts stroking his cock before putting it in my face."
    show sb_blowjob poke with dissolve
    pcm "I'm gonna have to suck him off aren't I?"
    pcm "Shit..."
    police.name "C'mon, ain't got all day."
    show sb_blowjob up with dissolve
    pause 0.5
    show sb_blowjob down with dissolve
    pause 1.0
    show sb_blowjob 2h suck with dissolve
    "Resigned to my fate, I put his cock in my mouth and try to get this over with as quickly as possible."
    if player.iswhore:
        "It's not like I'm not used to being a whore, so I just get to work and \"pay my dues\" to this corrupt shit."
    elif player.isslut:
        "It's not like I haven't had my fair share of cocks, so I just get down to it and \"pay my dues\"."
    else:
        "It's not as if I was hanging out here with innocent intentions. Just didn't think I would be the one sucking a dick."
    "I start with a good pace. I am not trying to make him enjoy but just to get him to cum as quickly as possible."
    "So I vigorously wank him off with both my hands while licking his cock from inside my mouth."
    police.name "Fuck. Good at this aren't ya?"
    "I ignore whatever he is saying and just keep working on his cock."
    "Eventually I feel him start to leak in my mouth a bit and his cock gets a lot harder..."
    $ player.sex_cum(police,"mouth")
    police.name "Ahhh fuck ya dirty whore!"
    police.name "Haaaaaa!"
    "He unloads everything in my mouth and I swallow each pump of it down. By the time he is done, all that's left is whatever leaked out the sides."
    show sb_blowjob poke frown with dissolve
    show sb_blowjob noman up with dissolve
    police.name "Good on ya whore. Now tidy y'self up and piss off outta 'ere."
    police.name "S day 'n' shouldn't be whores round 'ere. I see ya again and I'll be bringin' ya in. Won't be 'avin' a good time then."
    "With that, he walks away leaving me on my knees in the bushes."
    pcm "Ugh! Arsehole."
    hide sb_blowjob with dissolve
    pcm "Better go see if [dani.nname] is still there."
    $ walk(loc_park)
    show dance_dani_bench happy
    with dissolve
    pcm "Doesn't look like she even noticed I went missing. Glad she's at least having fun."
    pc "Hey."
    hide dance_dani_bench
    show dani dance happy at right1
    with dissolve
    dani.nname "Hey, everything ok?"
    pc "Yeah, just had to get away from a guard. Hanging round here dressed like this ended up getting him on my case."
    dani.name "Ah, how did you get away?"
    pc "Had to bribe him."
    jump school_dance_show_9_interrupt


label school_dance_show_9_hide:
    $ add_to_list(dani.conversation_topics, "dance_waited_bushes")
    pcm "Hanging out here people are going to give me odd looks. Don't really want to attract attention..."
    $ walk(loc_bushes)
    with dissolve
    pcm "Hmm, can I see her from here?"
    show dance_dani_bench with dissolve
    pcm "Yeah, and looks like she is already having fun."
    pcm "What did she do last time with this guy? Already seems pretty familiar with him letting herself be felt up like that."
    pcm "Ugh, now I look like a proper pervert spying on her from the bushes."
    if "joined_room1" in havenpeeper.dict and havenpeeper.dict["joined_room1"]:
        hide dance_dani_bench
        show haven_peeping at right
        with dissolve
        pcm "Hmmm, Maybe I am a pervert..."
        pcm "Didn't need to spy on the naked men but I did."
        $ player.add_desire(10)
        if havenpeeper.naughty:
            show haven_peeping grope_tit with dissolve
            pcm "Even let that pervert feel me up and have a bit of fun..."
            if havenpeeper.sex:
                $ player.face_shy()
                show haven_peeping poke_in enjoy shorts_down with dissolve
                if havenpeeper.vvirgin and havenpeeper.preg:
                    pcm "Fuck, even lost my virginity to him and carried his baby..."
                elif havenpeeper.vvirgin:
                    pcm "Fuck, even let him have my virginity while I was all worked up on spying on the men..."
                elif havenpeeper.preg:
                    pcm "Fuck, even let him fuck me and wound up carrying his baby..."
                else:
                    pcm "Even let him fuck me while I was all worked up from spying on the men..."
                pcm "Maybe I am a degenerate..."
        hide haven_peeping
    show dance_dani_bench neutral
    with dissolve
    pcm "Hmmm, whatever. Just wait it out and make sure everything is ok. Looks like she is pretty happy."
    pcm "Wonder if it's the money making her happy or the hand between her legs."
    $ player.grope_ass()
    $ player.face_shock()
    pc "AH!"
    pervert "Wonder what you doin' in here wit me?"
    pc "Fucking sneaking up like that! I could ask you the same."
    pc "Normally walk up to someone and grab their arse?"
    pervert "Sometimes."
    $ player.face_worried()
    pc "Whatever. I'm busy. Go away."
    $ player.grope()
    pervert "Spying on your friend there? Was doing the same when I noticed you here."
    pc "What you spying on her for?"
    pervert "Same as you probably? It's sexy."
    $ player.grope()
    pc "*Tsk* I am just making sure she is ok."
    pervert "Why wouldn't she? She's on a date and enjoyin' herself by the look of it. Seems happy enough wit the guy."
    $ player.grope()
    pervert "Like seeing her wit' her man's hand b'tween her legs? I can do the same for ya."
    pc "Ugh... What you doing?"
    pervert "Same thing that fella is doing to your friend. No point jus' her havin' fun."
    pc "Shoo. Go away."
    pervert "I was 'ere first. No one's keepin' you 'ere."
    pc "*Tsk*"
    if player.check_sex_agree(5):
        menu:
            "Go and interrupt [dani.nname]":
                jump school_dance_show_9_hide_leave
            "Stay here spying on her":
                $ player.add_desire(15)
    else:
        jump school_dance_show_9_hide_leave
    "I stick around spying on [dani.nname], but it is made a bit difficult with the wandering hands of this pervert."
    if player.desire > 75:
        "Would be a lot easier if I wasn't already so horny, keeping track of [dani.nname] is becoming more and more difficult with this distraction..."
    else:
        "Keeping track of [dani.nname] is becoming more and more difficult with this distraction. His fingers keep rubbing between my legs and his other hand pawing at my breast..."
    if c.pants:
        "But eventually he starts taking things a bit further and manages to slip my pants off."
        $ player.grope()
        $ c.pants = 0
        pc "Hey, what are you doing?"
        pervert "More fun without these."
        pc "I didn't say you could take them off."
        pervert "Didn't say I couldn't."
    pc "*Tsk*"
    if havenpeeper.naughty:
        pcm "I seem to be making a habit of letting peeping perverts do what they want with me..."
    else:
        pcm "The hell am I doing letting this pervert do what he wants with me?"
    pcm "Whatever, keep an eye on [dani.nname]."
    pervert "Your friend looks like she's having a good time as well."
    $ player.grope()
    pc "Sure, that makes one of us."
    pervert "And me. So two of us."
    $ player.grope_end()
    $ grope_mastleft = True
    pc "Err, wha are you doing?"
    pervert "Wanking."
    pc "Yeah, and why?"
    pervert "Because you're a sexy little bitch."
    pc "*Sigh*"
    pc "Don't go pointing that at me, I don't need to be having my clothes stained by your stuff."
    pervert "No problem."
    $ c.bottom = 0
    $ player.face_shock()
    with vpunch
    pc "Ah hey! What's this?"
    pervert "No problem now eh? No clothes ta get dirty."
    $ grope_mastleft = False
    $ player.grope_poke()
    pc "What the fuck! Screw you!"
    pervert "Now now. Just relax and keep an eye on your friend. I'll keep you warm out here."
    pc "Bugger off and leave me alone."
    show dance_dani_bench happy
    pervert "Don't be all prude now. No one's keeping ya 'ere. Let me make ya feel good."
    pervert "Relax and enjoy yourself."
    pervert "Mmmmm..."
    pcm "..."
    pcm "This is going a bit far..."
    pcm "Should I go see what..."
    pc "Ugn!"
    $ player.add_desire(15)
    pcm "What [dani.name] is up to?"
    if player.check_sex_agree(5):
        menu:
            "Yes, see what [dani.nname] is doing":
                jump school_dance_show_9_hide_leave
            "Stay here...":
                $ player.add_desire(15)
    else:
        jump school_dance_show_9_hide_leave

    $ add_to_list(dani.conversation_topics, "dance_waited_bushes_sex")
    pc "..."
    pcm "I can... Keep an eye on her... From here..."
    pervert "Mmmm, relax and enjoy..."
    pervert "I'll give you tha fun your friend will be getting soon."
    pervert "Look at her."

    pervert "Your dirty friend is having a great time."
    pervert "Look how happy she is to have her friend finger her on the bench."
    $ player.grope_breasts()
    $ c.top = 0
    pervert "Won't be long til she is riding his cock like a good little slut."
    pervert "Both of you are dirty girls who have a man between their legs."
    pervert "But unlike her, you have a nice hard cock that's about to fuck you while she only has fingers."
    $ player.grope_breasts()
    $ c.bra = 0
    pc "Wait. I never said anything... Ung! Ah!"
    pc "About..."
    $ player.grope_insert()
    $ player.sex_vag(parkpervert_dani)
    pc "Ah fuck yes!"
    pervert "Your body is telling me everything you dirty bitch."
    pc "Ah fuck you shitty pervert."
    pervert "I am, and so are you."
    pervert "Dirty cunt letting a guy who's face you haven't even seen stick his cock in you."
    pc "Ahh..."
    pervert "Now be a good little bitch and get on your fours."
    pc "Ah!"
    $ player.grope_end()
    hide dance_dani_bench
    show sb_doggy1 vag worried shock
    with vpunch
    pervert "That's better, bitches like you should be taken like one."
    pc "Fuck."
    pervert "Good girl, there's a good girl."
    show sb_doggy1 ah
    "The pervert behind me wastes no time and fucks me from the start at a furious pace. It's a wonder how he can even keep it up without slowing down."
    pervert "Mmmmm."
    pervert "Nice little bitch."
    pervert "Be a good girl and take it like one."
    pc "Mmmmm."
    show sb_doggy1 ag closed
    "He keeps pounding away at me and this is turning out to be a lot more enjoyable than I imagined it would be. Somehow he has managed to keep the pace up and I am starting to truly feel like his bitch."
    pervert "Nice little bitches should be fucked like one."
    $ acc.choker = 6
    pc "Ah, what is that?"
    pervert "Bitches like you should be collared like one before being treated like the dirty cunts you are."
    pervert "And you should be taken on fours, rutted and knotted on the grass."
    pc "Ha yes!"
    "He grips hold of me and, somehow still keeping up a fast pace of trusting just keeps on going. I am not sure if he knows or cares but this is feeling pretty damned amazing."
    show sb_doggy1 ah open
    pc "Wait?"
    pc "Knotted?"
    $ player.sex_cum(parkpervert_dani,"inside")
    show sb_doggy1 shock
    pervert "Ahhhh fuck yes!"
    pc "Ahhh fuck!"
    show sb_doggy1 ah
    pervert "Hawoooooo!"
    pervert "Huffff..."
    pervert "Mmmmm."
    show sb_doggy1 poke with dissolve
    show sb_doggy1 noman with dissolve
    pervert "Mmm, you should come here for a walk more often. I'm always happy to give new bitches what they want."
    show sb_doggy1 neutral
    pc "Yeah I bet..."
    if not player.has_perk(perk_preg_want):
        pcm "Can't believe I let him cum inside..."
    pervert "See you round."
    "I watch from between my legs as the pervert pulls his trousers up and leaves."
    pcm "Damn, I got way too carried away there..."
    hide sb_doggy1 with dissolve
    if work.pants:
        $ work.pants = 0
        $ pc_dress_slow()
        pcm "Err... Did that arse really take my knickers with him? Can't see them anywhere."
    else:
        $ pc_dress_slow()
    show sb_pose_upskirt with dissolve
    pcm "Fuck, leaking cum and no underwear..."
    pcm "Ah fuck! I forgot about [dani.nname]!"
    hide sb_pose_upskirt with dissolve
    $ walk(loc_park)
    $ player.face_worried()
    with dissolve
    pcm "Err, she's not on the bench anymore..."
    pcm "Fuck, hope she didn't get dragged off somewhere."
    pcm "Errr..."
    pcm "Can't see her anywh..."
    show dani dance at right1 with dissolve
    $ player.face_shock()
    pc "Ah!"
    pc "Was looking around for you. I lost you."
    show dani happy
    dani.name "Yeah, I noticed."
    $ player.face_worried()
    pc "Err, you're not upset?"
    dani.name "My friend wanted to go somewhere alone so I looked out for you to tell you."
    dani.name "But~~"
    $ player.face_shy()
    pc "Ah..."
    pc "You saw..."
    dani.name "Yup~"
    pc "Right..."
    pc "Well, glad everything is ok. You have fun with him?"
    dani.name "Yeah, he's nice I think."
    $ player.face_neutral()
    dani.name "He wants to meet again after the next show."
    pc "Ah, you're not wanting me to hang out showing my arse off to the park again are you?"
    dani.name "No, I think it's fine. I'll be okay on my own this time."
    pc "Yeah, well should still be careful. People are nice until they are not."
    dani.name "Thanks [name]. Felt a lot better knowing you were here."
    pc "Mmm, no worries. Hope he paid well."
    dani.name "Yeah... He did. Should be okay with food and rent for a bit at least."
    pc "Well, he wants a next time so maybe longer."
    dani.name "Hope so, better him than [oskar.name]."
    pc "Err, I guess..."
    if player.iswhore:
        pc "Nothing saying you can't have both and end up even better off."
        show dani worried
        dani.name "..."
        dani.name "I hate [oskar.name]..."
        $ player.face_worried()
        dani.name "I didn't want to do any of this stuff..."
        dani.name "It's because of him I..."
        pc "Right... It's fine. Sorry."

    show dani happy
    $ player.face_neutral()
    dani.name "Ah well, I had better get home anyway. See you."
    $ player.face_happy()
    pc "Mmm, be safe."
    $ player.face_neutral()
    dani.name "Oh, [name]."
    pc "Mmm?"
    dani.name "Woof!"
    $ player.face_angry()
    pc "Shooo!"
    dani.name "Hahaha!"
    hide dani with dissolve
    $ player.face_normal()
    jump travel

label school_dance_show_9_hide_leave:
    $ player.grope_end()
    hide dance_gropeass with dissolve
    $ walk(loc_park)
    with dissolve
    pcm "Damn pervert..."
    pcm "[dani.nname] still there?"
    show dance_dani_bench happy with dissolve
    pcm "Yup, still there having fun while I was dealing with a gropey pervert..."
    pcm "Lucky her..."
    hide dance_dani_bench
    show dani dance at right1
    with dissolve
    pc "Hey."
    dani.nname "Hey, everything ok?"
    pc "Yeah, wound up drawing the attention of some handsy pervert so thought I would come see you before things got too pokey."
    dani.name "Ah, how did you get away?"
    pc "Just left, he didn't try and stop me."
    jump school_dance_show_9_interrupt

label school_dance_show_9_interrupt:
    $ add_to_list(dani.conversation_topics, "dance_waited_interrupt")
    show theo at right2 with dissolve
    theo.name "Your one of [dani.name]'s dance friends aren't you?"
    pc "The clothes give it away?"
    theo.name "Well [dani.name], now's a good time to go somewhere private you think? Keep out of sight of prying eyes?"
    pc "Oh?"
    dani.name "Yeah, come with us [name]."
    theo.name "Oh, [name] is it. Nice to meet you."
    pc "Mmm, more walking less talking. Don't want to end up caught again."
    theo.name "Follow me."
    $ walk(loc_park_toilet)
    $ player.face_confused()
    pc "Err, why are we going here?"
    theo.name "It's out of sight and we can have some fun."
    pc "Errr..."
    show dani happy
    dani.name "Come on [name]."
    hide dani
    hide theo
    with dissolve
    $ player.face_worried()
    pcm "Uff..."
    pcm "Should I go in?"
    if player.check_sex_agree(3):
        menu:
            "Join them":
                jump school_dance_show_9_toilet
            "Leave them alone":
                $ NullAction()

    pcm "Ah fuck it, this is too much. [dani.nname] can deal with this alone..."
    $ add_to_list(dani.conversation_topics, "dance_waited_interrupt_left")
    jump travel

label school_dance_show_9_toilet:
    $ add_to_list(dani.conversation_topics, "dance_waited_interrupt_toilet")
    pcm "Ah fuck it. In for a penny in for a pound..."
    $ walk(loc_park_toilet_boys)
    pcm "They in the cubicle?"
    pc "You in here..."
    show dance_dani_gropetoilet with dissolve
    pc "Err... I guess so..."
    pcm "How did I wind up in this mess?"
    dani.name "Shut the door."
    pc "Right."
    pc "Okay..."
    pc "Nice weather we are having..."
    show dance_dani_gropetoilet happy
    dani.name "Sorry [name]."
    pc "Heh, you don't look sorry."
    pc "Ah whatever. Not like I haven't done the same."
    show dance_dani_gropetoilet man neutral
    theo.name "This common for you girls?"
    pc "Err..."
    pc "Probably?"
    show dance_dani_gropetoilet front
    dani.name "You think so?"
    pc "Dunno."
    pc "[rachel.name] probably enjoys it too much to ask for payment. Almost got into trouble on the bus thanks to her."
    if any(item in ["told_sex_" + drake.setname, "told_sex_" + nate.setname, "told_sex_" + dan.setname] for item in rachel.conversation_topics) and (nate.sex or drake.sex or dan.sex):
        pc "And she's already having fun with my boys so probably up to other stuff as well."
    pc "No idea about [svet.nname] and you would know more about [anabel.name] than me."
    dani.name "Yeah can't imagine [anabel.nname] doing anything like this."
    show dance_dani_gropetoilet man
    theo.name "Hmm, girls doing what you need to do."
    pc "Money doesn't come for free."
    theo.name "So you dirty sexy girls give men pleasure?"
    pc "Err... What?"
    theo.name "Sorry. I'm trying to get off here so trying to turn the mood more sexy."
    show dance_dani_gropetoilet penis
    pc "Ah."
    $ player.uncover()
    if player.has_perk([perk_whore, perk_exhibitionist], notif=True) or player.check_sex_agree(4):
        pc "Hmmm..."
        if player.has_perk(perk_exhibitionist):
            $ pc_striptease()
        else:
            $ pc_strip_upper(slow=True)
        pc "Better?"
        theo.name "Mmmm."
        show dance_dani_gropetoilet front
        dani.name "Oh? So it is two for one now is it?"
        pc "Shush."
        dani.name "Ha!"
    else:
        pc "Right, I guess..."
    show dance_dani_gropetoilet penis grope with dissolve
    theo.name "I knew I liked you girls."
    pc "Yeah, you and everyone else."
    theo.name "Well, not every day you see a group of young girls flashing their sexy arses for money."
    show dance_dani_gropetoilet man
    dani.name "It's called dancing."
    theo.name "Yeah, no one cares about the dancing, just what you are showing off."
    dani.name "Nooo. You are just one of the dirty ones."
    theo.name "Right. If you say so."
    theo.name "Fuck you are both so sexy!"
    dani.name "Huh?"
    theo.name "And these tits are so nice. Going to enjoy getting more time with them."
    theo.name "Spend all night with you having fun with every part of you."
    dani.name "Huh? Why the weird change in topic?"
    $ player.face_happy()
    pc "Because incoming."
    show dance_dani_gropetoilet front
    dani.name "What?"
    show dance_dani_gropetoilet penis worried cum
    show screen cum_action()
    theo.name "Ahhhh fuck!!"
    dani.name "Ahhhh?!"
    theo.name "Fuck yes!"
    dani.name "Errr..."
    pc "Hahaha! What? Didn't expect it?"
    show dance_dani_gropetoilet front
    dani.name "Ah, I guess not."
    theo.name "Mmmmm,"
    $ player.face_neutral()
    pc "I'll leave you to clean up. Don't take long or I'll be carted off as a whore again."
    hide dance_dani_gropetoilet with dissolve
    $ pc_dress_slow()
    $ walk(loc_park_toilet)
    $ player.cover_reset()
    pcm "Ha, that was actually quite funny."
    pcm "I guess [dani.nname] isn't as used to this as I thought she was."
    if dani.iswhore:
        pcm "Seemed to be having fun though, I guess thats good."
    else:
        pcm "Seemed to be having fun though which is unusual for a first time."
    if player.has_perk(perk_whore) and not dani.iswhore:
        pcm "Was pretty upset with myself the first times I sold myself but she seems pretty okay with it."
    pcm "Maybe she quite likes the guy..."
    show dani dance at right1
    show theo at right2
    with dissolve
    theo.name "Thanks for the fun ladies, but I have to be off now."
    theo.name "See you next time [dani.name]."
    dani.name "Bye."
    hide theo with dissolve
    pc "Next time?"
    dani.name "Yeah, he wants to meet again after the next show."
    pc "Ah, you're not wanting me to hang out showing my arse off to the park again are you?"
    dani.name "No, I think it's fine. He seems quite nice..."
    pc "Yeah, well should still be careful. People are nice until they are not."
    $ walk(loc_park)
    with dissolve
    dani.name "Thanks [name]. Felt a lot better knowing you were here."
    pc "Mmm, no worries. Hope he paid well."
    dani.name "Yeah... He did. Should be okay with food and rent for a bit at least."
    pc "Well, he wants a next time so maybe longer."
    dani.name "Hope so, better him than [oskar.name]."
    pc "Err, I guess..."
    if player.iswhore:
        pc "Nothing saying you can't have both and end up even better off."
        show dani worried
        dani.name "..."
        dani.name "I hate [oskar.name]..."
        $ player.face_worried()
        dani.name "I didn't want to do any of this stuff..."
        dani.name "It's because of him I..."
        pc "Right... It's fine. Sorry."
    show dani happy
    dani.name "Ah well, I had better get home anyway. See you."
    $ player.face_happy()
    pc "Mmm, be safe."
    hide dani with dissolve
    $ player.face_normal()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
