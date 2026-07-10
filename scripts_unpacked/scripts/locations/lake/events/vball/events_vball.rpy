



label loc_beach_vball_ask_join:
    $ temp_var_1 = False
    $ add_to_list(loc_beach_gym.list, "beach_vball_asked")
    $ beach_vball_asked = True
    if not erika.has_met or zahra.has_met:

        $ temp_var_1 = True
    show zahra at right1
    show erika at right2
    with dissolve
    pc "Hey, it okay to join in?"
    erika.name "The more the merrier!"
    pc "How do things play out? Teams or what?"
    erika.name "Na, just wait til the round is over and pick a side. We don't worry 'bout scores."
    zahra.name "Cos you always lose."
    erika.name "Lies!"
    pc "Ok, thanks."
    if temp_var_1:
        erika.name "[erika.name]. This is [zahra.name]. Nice to have a new girl round here."
        zahra.name "Mmm, better than the usual perverts."
        if c.nude:
            erika.name "She probably is a pervert since she's naked."
        elif c.exposed:
            erika.name "Might still be a pervert since she's showing off."
        else:
            erika.name "Might still be a pervert."
        zahra.name "Then the boys will love her."
        erika.name "She might want to jump on you."
        pc "I'm right here you know."
        erika.name "Wanna jump on her?"
        pc "Err... No?"
        erika.name "See. Pervert."
        zahra.name "Ignore her. Go play. It's fun."
        pc "Right..."
    $ renpy.scene()
    with dissolve
    jump travel

label loc_beach_vball_nude_join:
    $ temp_var_1 = False
    $ add_to_list(loc_beach_gym.list, "beach_vball_nude_asked")
    if not erika.has_met or zahra.has_met:

        $ temp_var_1 = True
    if not "mason_joinnude" in mason.list:
        if robin_here():
            show robin happy at right1 with dissolve
            robin.name "Ah, you came."
            pc "Yeah, thought I would see what is going on."
            robin.name "Same as usual, except naked. Come and join."
            if mason_here():
                pc "Is that the sports coach over there?"
                robin.name "Yeah, don't mind him. He wont poke you."
                pc "Right."
            hide robin with dissolve
            jump travel
        elif zahra_here() and zahra.has_met:
            show zahra at right1 with dissolve
            zahra.name "You joining us?"
            pc "Err, thinking about it."
            if c.nude:
                zahra.name "Well you are dressed for it. So come on."
            else:
                zahra.name "Well strip off and come over."
            hide zahra with dissolve
            jump travel
        elif erika_here() and erika.has_met:
            show erika at right1 with dissolve
            erika.name "You joining us?"
            pc "Err, thinking about it."
            if c.nude:
                erika.name "Well you are dressed for it. So come on."
            else:
                erika.name "Well strip off and come over."
            hide erika with dissolve
            jump travel
        elif sandy_here() and sandy.has_met:
            show sandy at right1 with dissolve
            if c.nude:
                sandy.name "Come and join [name]!"
            else:
                sandy.name "Strip off and come play with us."
            hide sandy with dissolve
            jump travel
        else:
            if any([zahra_here(), erika_here(), sandy_here()]):

                pcm "I see some girls playing, but no one I know..."
                pc "It okay if I join?"
                if zahra_here():
                    zahra.name "If you dress the part, sure."
                elif erika_here():
                    erika.name "Only if you are naked."
                else:
                    sandy.name "Sure, undress and join!"
                pc "Thanks."
                jump travel
            else:
                pcm "Hmm, I don't see any girls playing. I thought they would be here."
                $ remove_from_list(loc_beach_gym.list, "beach_vball_nude_asked")
                jump travel

    if npc_any_here(exclude=mason):
        show mason nude at right1 with dissolve
        mason.name "Good to see you joining us."
        pc "Thought I would check it out. Looks like you made some friends."
        mason.name "More fun with a group."
        if not c.nude:
            pc "Guess I am over dressed for this party."
            mason.name "That you are."
        else:
            pc "Well, looks like I am wearing the right bikini for this party."
            mason.name "Mmm."
    else:
        show mason at right1 with dissolve
        pc "Oh? Got you clothes on?"
        mason.name "Alone for now so no point in undressing."
        pc "Why not? Then I could have caught you."
        mason.name "Hrmf!"
        if c.nude:
            pc "C'mon. Get 'em off! Not fair I came here nude."
            mason.name "Okay."
            show mason soft with dissolve
            mason.name "Satisfied?"
            pc "Mostly. More fun if that thing was standing up."
            mason.name "I spoke to some people I know. Might have some joining us."
            if temp_var_1:
                pc "Not talking about the guys by the fireplace?"
                mason.name "You know them?"
                pc "Kinda."
                mason.name "Good then. Yes I am talking about them."
            else:
                pc "Oh? Interesting you have a pervert group."
                mason.name "Just some people having fun."
        else:
            mason.name "And what about you? A bikini doesn't count as naked."
            pc "Ah, well. Yeah."
            mason.name "Anyway, I spoke to some people I know. Might have some joining us to play."
            pc "Nude?"
            mason.name "Of course."
            if temp_var_1:
                pc "Not talking about the guys by the fireplace are you?"
                mason.name "You know them?"
                pc "Kinda."
                mason.name "Good then. Yes I am talking about them."
            else:
                pc "Oh? Interesting you have a pervert group."
                mason.name "Just some people having fun."


    mason.name "Join if you are interested."
    pc "Will do."
    $ renpy.scene()
    with dissolve
    if robin_here():
        $ add_to_list(robin.list, "nudebeachvball_ask_know")
        show robin at right1 with dissolve
        pc "Why am I not surprised to see you here?"
        robin.name "Same reason you are here."
        if "can_bitch" in robin.list:
            pc "Dirty bitch."
        elif "pc_know_want_bussex" in robin.list:
            pc "Bus deviant!"
        else:
            pc "Slut."
        robin.name "So joining?"
        pc "I guess..."
        hide robin with dissolve
    jump travel

label loc_beach_vball:
    if not "beach_vball_asked" in loc_beach_gym.list:
        jump loc_beach_vball_ask_join
    $ vball_image()
    "Play volleyball with whoever is currently playing."
    $ player.add_mood(5)
    $ exercise(60)
    $ renpy.scene()
    with dissolve
    jump travel

label loc_beach_vball_nude:
    if not "beach_vball_nude_asked" in loc_beach_gym.list:
        jump loc_beach_vball_nude_join
    if not c.nude:
        pcm "I should undress..."
        $ pc_strip(temp=True)
    $ vball_image()
    "Play volleyball with whoever is currently playing."
    $ player.add_mood(5)
    if mason_here() and t.hour in [2,3] and not "walked_home" in mason.list:
        jump loc_beach_vball_nude_walkhome

    $ exercise(60)
    $ renpy.scene()
    with dissolve
    jump travel

label loc_beach_vball_nude_walkhome:
    $ exercise(60)
    $ renpy.scene()
    show mason hard at right1
    with dissolve
    if not ("mason_caughtnude" in mason.list or "mason_joinnude_alt_intro" in mason.list):
        $ add_to_list(mason.list, "mason_joinnude_alt_intro")
        mason.name "Hello Miss [sname]."
        pc "I knew it! Pervy coach!"
        mason.name "I suppose..."
        pc "Well whatever. You do what you want. Seems everyone is having fun."
        mason.name "And I aim to keep it that way."
        pc "Sure..."
    if "mason_walked_home" in loc_beach_gym.list:
        jump loc_beach_vball_nude_walkhome_repeat
    mason.name "It's getting late. Do you want me to walk you home?"
    pc "Err..."
    mason.name "We can go naked and enjoy a little."
    pc "Wait, enjoy? You planning to pull me in the bushes?"
    mason.name "No. Just going all the way home with nothing on."
    pc "Right..."
    menu:
        "Okay, let's go":
            $ add_to_list(loc_beach_gym.list, "mason_walked_home")
        "No, I'll make my own way home":
            mason.name "Okay, be safe."
            hide mason with dissolve
            jump travel

    mason.name "Do you know the way to the park from here?"
    $ walk(loc_beach_hangout)
    if loc_walk_lake_shrubs.visited:
        pc "Yeah, through the dark and dangerous bushes?"
        mason.name "Ah you do know."
    else:
        pc "Err, get the bus?"
        mason.name "There is a way to walk. Isolated so can do what you want."
    $ loc_walk_lake_shrubs.locked = False
    $ loc_walk_park_shrubs.locked = False
    $ player.face_sus()
    pc "If you murder me, I'll haunt you."
    mason.name "I'd expect nothing less."
    show mason at left1 with dissolve
    $ player.uncover()
    $ walk(loc_beach_locker_boys)
    pc "Ohh, taking me through here."
    if player.hygiene < 40:
        call loc_beach_vball_nude_walkhome_shower from _call_loc_beach_vball_nude_walkhome_shower
    $ walk(loc_lake)
    if not loc_walk_lake_shrubs.visited:
        mason.name "See the opening through there? Quickly before someone sees us."
    else:
        mason.name "Quickly before someone sees us."
    $ walk(loc_walk_lake_shrubs)
    $ loc_walk_lake_shrubs.visited = True
    pc "Since when were you worried about being seen?"
    show mason at right6 with dissolve
    mason.name "Err. Always?"
    mason.name "Risk is the fun part."
    $ player.eye = 6
    pc "And yet you are standing here in front of me with your dick pointing up looking at me."
    mason.name "Err..."
    if player.has_perk([perk_slut, perk_sucu]):
        pc "Want me to fix it?"
        mason.name "Fix it?"
        $ player.face_neutral()
        pc "Yeah. Relieve some tension. Make it go soft."
        mason.name "Err..."
        pc "With my mouth."
        mason.name "I... Err..."
        pc "Suck your cock."
        mason.name "Ah, no. No. Not here."
        pc "No?"
        mason.name "If you do that. Then I won't be horny any more."
        pc "That's kinda the point."
        mason.name "Then I won't be able to carry on naked."
        pc "Huh?"
        mason.name "It's the excitement that makes me do this. Take that away and I'll be too ashamed."
        pc "Oooh. That's why you haven't tried to bend any of us over like most perverts would."
        mason.name "Something like that."
        pcm "Well, kinda makes sense."
        menu:
            "Tease him":
                pc "Why don't I walk in front?"
                mason.name "..."
                $ renpy.scene()
                show sb_pose_lookback happy smile
                with dissolve
                pc "Maybe show you something you like?"
                mason.name "You are walking a dangerous game."
                pc "Oh dear. Am I?"
                hide sb_pose_lookback
                show sb_onfours
                with hpunch
                pc "Oops! I fell over."
                pc "I hope some pervert school coach isn't behind me to take advantage of me."
                mason.name "..."
                pc "What ever would a naked and alone girl do?"
                $ player.spank()
                mason.name "Come on."
                "[mason.pname] walks past me and down the path."
                pc "..."
                $ player.face_neutral()
                pc "Hey. Don't walk away."
                hide sb_onfours with dissolve
                $ walk(loc_walk_park_shrubs)
                show mason nude at left1 with dissolve
                pc "Leaving me all alone back there."
            "Keep walking":
                mason.name "Park is not far from here."
                pc "Right..."
                show mason at left1 with dissolve
                $ walk(loc_walk_park_shrubs)
    else:
        pc "Hello [mason.pname]'s mushroom."
        pc "How are you today?"
        pc "How has this pervert been treating you?"
        pc "..."
        pc "It's not answering."
        mason.name "Yeah, it doesn't tend to."
        $ player.face_neutral()
        pc "Probably for the best."
        mason.name "Park is not far from here."
        pc "Right..."
        show mason at left1 with dissolve
        $ walk(loc_walk_park_shrubs)

    mason.name "You should be able to see the park just ahead."
    if loc_kitchen.locked:
        pc "Why are we going to the park anyway?"
        show mason at right6 with dissolve
        mason.name "You live there don't you?"
        pc "I used to. Got kicked out for not paying rent."
        mason.name "Oh? I didn't know."
        mason.name "So where do you live now?"
        if loc_highway_slum_home.unlocked:
            pc "I live way over the other side in the slums with the whores and junkies."
            mason.name "Oh..."
            mason.name "I'm not walking that way while naked."
            pc "Yeah don't blame you. We will both be raped dead the moment we are seen."
            mason.name "..."
            pc "The park is fine though."
        if log.interactive("quest_homeless_01"):
            pc "Still looking and just staying place to place for now."
            mason.name "Oh..."
            pc "Don't worry. Messing around in the park is fine."
            mason.name "Okay."
        show mason nude at left1 with dissolve
        mason.name "Well let's cut through anyway and..."
    else:
        pc "Yeah, I can. My place is just past it."
        $ player.face_sus()
        pc "Wait. How do you know where I live?"
    show wolfman roar hard at right1 with vpunch
    $ player.face_shock()
    "Wolfman" "RWARRRRR GOT YAAA!!!"
    pc "Ah what the fuck!"
    "Wolfman" "Wait, you aren't a bitch."
    if quest_wolfgang.active:
        $ player.face_neutral()
        pc "Nope. So shoo!"
        "Wolfman" "Have fun."
        hide wolfman with dissolve
        show mason at right5 with dissolve
        mason.name "You know about this?"
        pc "I live just over there, of course I do."
        mason.name "Oh."
        pc "Actually surprised you do."
        mason.name "Yeah..."
        mason.name "I have played around with them before."
        pc "Heh, pervert."
    else:
        $ player.face_angry()
        pc "Kick his ass [mason.pname]!"
        mason.name "Hi Dave."
        show wolfman stand with dissolve
        "Wolfman" "Oh. Hi [mason.name]. Didn't recognise you in the dark."
        $ player.face_worried()
        pc "You know him?"
        mason.name "Yeah, we hang out a bit."
        pc "Hang out with weird park rapists?"
        mason.name "Not quite."
        "Wolfman" "No rapists here. Saw you naked so thought you were a bitch. But you don't have the collar."
        pc "What?"
        mason.name "People come here and wear a specific collar to play around."
        pc "Again. What?"
        mason.name "See the collar he has? If you also have one, he will jump on you and... Well..."
        pc "Rape me?"
        "Wolfman" "No rape. Safe without the collar. Wearing one means you agree. It's all in good fun."
        pc "And people do this by choice?"
        mason.name "Lot of girls have fun with it. Try and make it though the park without being pounced on."
        pc "Really?"
        mason.name "You think it's only us who has weird fun walking through here naked? We all have our... Pleasures."
        pc "And you do this?"
        mason.name "Sometimes."
        pc "Wow..."
        "Wolfman" "Here, if you are interested. Put it on and try to escape."
        $ wardrobe.take(item_choker_6, all_notif=True)
        pc "And what? Get ambushed by weirdos?"
        "Wolfman" "Pretty much. But it's all for good fun. Don't worry, We will treat you right."
        pc "While holding me down and fucking me?"
        "Wolfman" "That's right. Take the collar off or leave the park for it to stop. None of us will touch you without the collar."
        pc "You sure about that?"
        "Wolfman" "I am. This is all for fun. Don't want anyone sad at the end of it."
        pc "Right..."
        show wolfman roar
        "Wolfman" "AWOOOOOOO!!!!!"
        hide wolfman with dissolve
        pc "Wow..."
        mason.name "Didn't think we would bump into someone on the way."
        pc "And you do this? Jump on women in the park?"
        show mason at right6 with dissolve
        mason.name "Yeah, sometimes."
        pc "Are you sure this is what they want?"
        mason.name "Yes. If we did something we shouldn't, then the girls would stop coming."
        mason.name "Have to keep it all willing fun and make sure anyone who breaks the rules are dealt with."
        pc "Dealt with?"
        mason.name "Usually anyone who breaks the rules are..."
        mason.name "Let's just say not all the guys here are interested in the women."
        mason.name "And then there will be a raping or worse."
        $ log.assign("Wolfgang bitch")
        $ log.activate("quest_wolfgang_02")
        pc "Oh..."
        pc "..."
    show mason at left1 with dissolve
    mason.name "Let's go."
    if player.has_perk([perk_slut, perk_sucu], notif=True):
        menu:
            "Put the collar on and run away":
                $ player.face_evil()
                $ acc.choker = 6
                pc "See ya [mason.pname]!"
                hide mason
                $ walk(loc_park)
                jump random_event_wolfgang_picker
            "Walk home":

                $ NullAction()

    $ walk(loc_park)
    mason.name "Way more public here. Let's hurry."
    pc "Wait. How are you getting home? You live far from here?"
    if loc_kitchen.locked:
        mason.name "Probably find somewhere nearby to change and walk home."
    else:
        mason.name "Probably change near your place and walk home."
    pc "Not rush off naked?"
    mason.name "Too scary alone."
    pc "Ooh, scary park rapist scared of being alone."
    mason.name "..."

    if "mason_caught_parknude" in mason.list:
        pc "Then how did I catch you running around naked?"
        mason.name "I didn't say I don't do it. It's just way more scary."
        mason.name "But sometimes I manage to find the courage to do it."
        pc "Then jump out in front of me?"
        mason.name "That was a mistake..."

    if loc_kitchen.locked:
        pc "We going to keep standing here with our asses out?"
        mason.name "Over here."
        $ walk(loc_bushes)
        pc "Oh? Dragging me into the bushes now?"
        show mason at right5 with dissolve
        pc "All naked and with your thingy pointing at me?"
        mason.name "Yeah, we can get dressed and head off."
    else:
        $ walk(loc_residential)
        mason.name "Quick!"
        $ walk(loc_stairwell)
        pc "Come on, before my flatmates see you."
        $ walk(loc_kitchen)
        $ walk(loc_bedroom)
        pc "Think we got away with it."
        show mason at right5 with dissolve
        mason.name "Looks like it."
        $ player.eye = 6
        pc "Errr..."
        pc "Naked man in my bedroom with his hard cock pointing at me?"
        mason.name "Right. I should get dressed and head off."

    if not mason.can_sex and player.has_perk([perk_broken, perk_slut, perk_bimbo, perk_sucu], notif=True) or player.check_sex_agree(3, notif=True):
        $ player.face_neutral()
        if loc(loc_bushes):
            pc "Or we could play in the bushes."
        else:
            pc "Or you could stay the night."
        if player.has_perk(perk_broken):
            $ player.face_meek()
            pc "I'm used to my body being used for this."
        else:
            pc "Can probably find somewhere nicer to hide your thingy."
        mason.name "Err..."
        $ npc_race_picker(mason)
        show sb_blowjob 1h laugh poke with dissolve
        "I don't give him much chance to answer and get on my knees to have some fun with him."
        show sb_blowjob down swallow with dissolve
        show sb_blowjob suck with dissolve
        $ player.face_shock()
        show sb_blowjob nopenis worried up with hpunch
        mason.name "Sorry, I can't do this."
        hide sb_blowjob with dissolve
        pc "Huh?"
        mason.name "It doesn't feel right."
        $ player.face_worried()
        pc "What do you mean?"
        mason.name "Err, another time maybe."
        $ add_to_list(mason.list, "rejected_blowjob")
        show mason gym with dissolve
        hide mason with dissolve
        pcm "Wow. First time ever I think a guy acted like that while I was trying to blow him..."
        jump travel
    else:

        show mason gym with dissolve
        mason.name "It was fun [fname], I look forward to the next time."
        pc "Sure. Get home safe."
        hide mason with dissolve
        jump travel

label loc_beach_vball_nude_walkhome_repeat:
    if not "sex_progress_counter" in mason.dict:
        $ mason.dict["sex_progress_counter"] = 0
    mason.name "It's getting late. Want to go back naked?"
    if mason.dict["sex_progress_counter"] == 0:
        pcm "Hmm, both walking back naked..."
        pcm "Maybe I can tease him or have fun with him on the way home."
        pcm "Assuming he doesn't just jump my ass in the bushes."
    menu:
        "Okay, let's go":
            pc "Sure, let's go."
        "No, I'll make my own way home":
            mason.name "Okay, be safe."
            hide mason with dissolve
            jump travel

    $ player.uncover()
    show mason at left1 with dissolve
    $ walk(loc_beach_hangout)
    $ walk(loc_beach_locker_boys)
    if player.hygiene < 40:
        call loc_beach_vball_nude_walkhome_shower from _call_loc_beach_vball_nude_walkhome_shower_1
    else:
        call mason_sex_picker from _call_mason_sex_picker
    $ walk(loc_lake)
    mason.name "Quickly before someone sees us."
    $ walk(loc_walk_lake_shrubs)
    if "rejected_blowjob" in mason.list and not mason.can_sex:
        call loc_beach_vball_nude_walkhome_nosex_explain from _call_loc_beach_vball_nude_walkhome_nosex_explain
    else:
        call mason_sex_picker from _call_mason_sex_picker_1
    $ walk(loc_walk_park_shrubs)
    call mason_sex_picker from _call_mason_sex_picker_2

    if loc_kitchen.locked:
        pc "Pretty quiet out there as always. You ready?"
        mason.name "I'm ready."
        $ walk(loc_park)
        call mason_sex_picker from _call_mason_sex_picker_4
        $ walk(loc_bushes)
        pc "There we go."
        show mason at right5 with dissolve
        mason.name "That was fun."
        pc "Hehe."
        if mason.want_sex() and not renpy.has_label("mason_sex_walk_chain_" + str(mason.dict["sex_progress_counter"])):
            menu:
                "Have fun with him":
                    jump mason_sex_general_bedroom_tombola
                "Watch him dress":
                    $ NullAction()
        mason.name "Thanks for the fun."
        show mason gym with dissolve
        pc "Get home safe."
        hide mason with dissolve
        jump travel
    else:

        pc "Pretty quiet out there as always. You ready?"
        mason.name "I'm ready."
        $ walk(loc_park)
        call mason_sex_picker from _call_mason_sex_picker_3
        $ walk(loc_residential)
        $ walk(loc_stairwell)
        pc "Phew. The last leg."
        $ walk(loc_kitchen)
        $ walk(loc_bedroom)
        pc "There we go."
        show mason at right5 with dissolve
        mason.name "That was fun."
        pc "Hehe."
        if mason.want_sex() and not renpy.has_label("mason_sex_walk_chain_" + str(mason.dict["sex_progress_counter"])):
            menu:
                "Have fun with him":
                    jump mason_sex_general_bedroom_tombola
                "Watch him dress":
                    $ NullAction()
        mason.name "Thanks for the fun."
        show mason gym with dissolve
        pc "Get home safe."
        hide mason with dissolve
        jump travel

label loc_beach_vball_nude_walkhome_shower:
    pc "Mind if I shower first? You can come in if you want."
    show mason at right5 with dissolve
    mason.name "Err, okay."

    call shower_scene_start from _call_shower_scene_start_6
    call shower_scene_wash from _call_shower_scene_wash_4
    pc "Okay, let's go."
    show mason at left1 with dissolve
    return

label loc_beach_vball_nude_walkhome_nosex_explain:
    $ mason.can_sex = True
    show mason at right5 with dissolve
    mason.name "Err, so about last time."
    $ player.face_happy()
    pc "When you ran away from me trying to suck you off?"
    mason.name "Yeah..."
    $ player.face_neutral()
    pc "It's fine. Don't think I have ever been rejected like that. But it's all good."
    mason.name "..."
    pc "Well, let's go then."
    mason.name "Wait."
    mason.name "It's just I am not used to this sort of thing."
    pc "Huh? Seems like you are plenty used to it. Running around naked with a bunch of girls then raping bitches in the park."
    mason.name "You would think so... But no."
    pc "No?"
    mason.name "I've... Err... Never done this sort of thing before..."
    pc "What thing? I'm lost. Are we talking about the same thing?"
    mason.name "Look. I keep myself safe around the girls. They already kicked [mateo.name] and [kaan.name] from naked fun because they kept trying to stick it in them every chance they got."
    mason.name "I keep my cock away from them so I don't get kicked as well."
    if "nude_vball" in rachel.list:
        pc "And [rachel.name]? She can't walk near a guy without him sticking it in her."
        mason.name "No... Not that I wouldn't. She just seems a bit intense for me."
        pc "Haha! Yeah..."
    pc "So just raping bitches then."
    mason.name "Yeah... About that..."
    pc "What?"
    mason.name "There aren't actually many girls that go bitching. Once a week you might find one. Rest of the time it's just guys."
    $ player.face_worried()
    pc "What? So you just hang around the bushes with your dick in your hand all week waiting for a girl to pass by."
    mason.name "Err... No?"
    pc "That sounds like way less fun than I thought it would be."
    mason.name "Well yeah, you are a girl so get dog piled as soon as you enter."
    mason.name "Most days we hunt each other."
    pc "Ha, yeah I guess. Must be like a buffet... What? Each other?"
    mason.name "Yeah..."
    $ player.face_shock()
    pc "Wait. So you are running around the park hunting other dudes most of the time?"
    mason.name "Or getting hunted."
    $ player.face_worried()
    pc "Getting hunted?"
    pc "..."
    pc "Wait..."
    $ player.face_evil()
    pc "You telling me big strong [mason.name] got himself hunted and made a bitch?"
    mason.name "..."
    $ player.face_neutral()
    pc "Wow. That's... Unexpected..."
    pc "So you really got ass fucked by these guys?"
    mason.name "It's happened."
    pc "Wow... Okay..."
    pc "Wow."
    pc "Ah! So that's why you ran away? I don't have the right bits between my legs?"
    mason.name "Noooo no no no. Nothing like that."
    pc "Then what?"
    mason.name "I've just never actually done it with..."
    $ player.face_shock()
    pc "With a girl?"
    pc "Wow. Aren't you like double my age? Didn't you do anything before the world got shit?"
    mason.name "Wow. Double your age? Not even close."
    $ player.face_neutral()
    pc "Sure old man."
    mason.name "..."
    if "nude_vball" in rachel.list:
        pc "Well, whatever. Pretty sure you could poke [rachel.name] at any point and she would love it."
        if player.vvirgin:
            pc "And if it makes you feel any better, I have never done it either."
            mason.name "That is suprising."
        else:
            mason.name "And you?"
            pc "Try and find out."
    elif player.vvirgin:
        pc "Well... If it makes you feel any better, I have never done it either."
        mason.name "That is suprising."
    show mason at left1 with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
