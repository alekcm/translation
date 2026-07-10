



label start_sismeet_1:
    show emile at right1 with dissolve
    emile.name "There you are! I'm here looking all over for you forgetting you are basically a new person!"
    pc "Hey [emile.name]..."
    emile.name "Hey..."
    emile.name "..."
    emile.name "Well this is a bit awkward..."

    menu:
        "It's good to see you":
            $ player.face_happy()
            show emile happy
            emile.name "Good to see you too... [fname]."
            $ player.face_neutral()
            pc "..."
        "You're telling me":

            $ player.face_frown()
            $ emile.dict["tut_anger"] += 1
            show emile worried
            emile.name "Yeah, I can't imagine..."
            pc "Yeah..."

    if emile.days_pregnant > (global_pregnancy_length * 0.3):
        pc "Looks like more than I realised has changed."
        emile.name "You'll see how much once we're outside."
        pc "I'm talking about the belly."
        emile.name "Ah... This? Yeah a lot of change."
    show emile neutral
    emile.name "Well anyway, they filled me in on all the details. Bit of a shock but I'm glad they were able to save you."
    emile.name "I thought for sure that you wouldn't be coming back. Not after what happened..."
    $ player.face_worried()
    emile.name "..."
    emile.name "Well... Enough of that. The Institute has arranged a small flat for you. I'm supposed to take you straight there and get you settled in."
    $ player.face_neutral()
    emile.name "But can't really have you going around in that hospital gown."
    emile.name "C'mon, let's buy you something decent on the way home. Shops are on the way anyway."
    if player.male_origin:
        pc "Ok, my old clothes won't even fit any more and this gown isn't really something I can go around in."
        $ walk(loc_hospital_entrance)
        emile.name "Nope. And going for a walk to the shops might help you get used to your new legs a bit."
    else:
        pc "None of my old clothes survive?"
        $ walk(loc_hospital_entrance)
        emile.name "They might have, no idea where they are now though. They were in the car and I didn't spend any time getting the bags out the boot."
        emile.name "The walk will do you good anyway. Get those legs moving."

    if emile.days_pregnant > (global_pregnancy_length * 0.3):
        pc "The walk? What about you carrying that belly around?"
        emile.name "We can take it slow."
    pc "..."
    pc "Get used to it right...?"
    $ player.face_worried()
    pc "I woke up in a new body, and am supposed to get used to it?"
    emile.name "Not to sound harsh, but not a lot else you can do. Acting normal is all we can do. [nik.name] was telling me that it's for the best."
    $ player.face_neutral()
    pc "For the best?"
    emile.name "Yeah, claims that the best thing for you is to return as close to normalcy as possible. Psychologically speaking."
    $ player.face_surprised()
    pc "Get used to it or I'll hang myself from the ceiling fan is it?"
    show emile happy
    emile.name "You got it [name], so let's get you out of that gown and into something more comfortable. Then off to your flat where you can unwind."
    $ walk(loc_revel)
    show emile neutral
    $ player.face_neutral()
    emile.name "I'll be staying with you for a few days and tomorrow a counsellor from the hospital will come to have a chat with you about some stuff."


    if player.male_origin:
        emile.name "To be honest I wasn't really listening. Was still trying to get over having a new sister."
        menu:
            "A new sister?":
                $ player.mouth = 4
                pc "Your new sister?"
                $ player.add_conf(5)
                $ player.add_comfort(10)
                emile.name "What girl doesn't want a little sister?"
                pc "Little sister? They gave me a new ID but am I your *little* sister?"
                show emile neutral
                $ player.mouth = 1
                emile.name "You have a meeting tomorrow where you will find all that out. But for now you are here and alive, it's all that matters."
                pc "You really *are* enjoying this aren't you?"
                show emile happy
                emile.name "Yup..."
            "I'm not your sister.":

                $ player.face_annoyed()
                pc "I'm not your new sister."
                show emile worried
                $ emile.dict["tut_anger"] += 1
                emile.name "Fraid your gonna have to be. They didn't tell me directly, but from what I could gather, this whole situation is a bit hush hush. Probably why they wanted rid of you so soon after waking you up."
                $ player.brow = 1
                pc "Yeah seemed that way to me too. Wonder if what they did was even legal?"
                show emile neutral
                emile.name "Legal or not, I'm not complaining. You are alive and that's all that matters."
                pc "Hmmm"

        $ player.brow = 1
        $ player.mouth = 1
        show emile neutral
        emile.name "Plus if you ask me, they gave you an upgrade."
        $ player.mouth = 4
        pc "Hey!"
        show emile happy
        emile.name "C'mon, a bit of work and you will be fighting off the guys with a stick."
        $ player.brow = 3
        $ player.mouth = 9
        pc "Fuck!!"
        show emile neutral
        emile.name "What? What's wrong?"
        pc "I just realised I'm a girl!"
        emile.name "Errrmm... Yeah... Are you feeling ok?"
        $ player.mouth = 2
        pc "No I mean I'm a girl. You said I'll be fighting off the guys with a stick."
        emile.name "Well maybe not yet, but..."
        pc "Guys! Because I'm a girl. So guys will be after me, not girls."
        show emile happy
        emile.name "Ahhhh."
        $ player.mouth = 8
        emile.name "Well... Yes. Welcome to the other side of the fence sister. More for you to get used to."
        $ walk(loc_market)
        show emile neutral
        $ player.mouth = 1
        $ player.brow = 1
        emile.name "And talking of getting used to things, here we are."
        emile.name "Ready to get you into some proper clothes?"
        menu:
            "Yeah, let's get me out of this hospital gown":
                $ player.add_conf(5)
                $ player.mouth = 1
                show emile happy
                pc "Yeah, I don't really want to be walking around like this. And there is too much of a breeze..."
                if player.breasts == 3 and not player.male_origin:
                    pc "And doesn't feel like they knew where to stop when they added tits to this body. Who the hell added these things."
                else:
                    emile.name "That's the spirit, we will have you sorted in no time."
            "Doesn't look like I have much of a choice":

                $ player.mouth = 8
                pc "Doesn't look like I have much of a choice. I can't be walking around wearing a hospital gown."
                emile.name "Not really. So let's get going. And try to at least enjoy yourself"
                pc "Else the ceiling fan gets ever closer?"
                emile.name "Haha. Too right!"
            "I think I'd prefer to just go home":

                $ player.face_annoyed()
                $ emile.dict["tut_anger"] += 1
                pc "Can't I just go home? I'm not really in the mood to be going shopping."
                show emile worried
                emile.name "Not gonna happen I'm afraid. Can't have you looking like an escaped mental patient. So let's go and get this all over with."
    else:

        emile.name "To be honest I wasn't really listening. Was far too eager to get you out of the hospital and back to a normal life."
        pc "You're enjoying this aren't you?"
        show emile happy
        emile.name "Yup..."
        emile.name "C'mon [name], can't I take some enjoyment from this situation? It is kinda funny. Always wanted a little sister."
        pc "Little sister? They gave me a new ID but am I your \"little\" sister?"
        emile.name "You have a meeting tomorrow where you will find all that out. But for now you are here and alive, it's all that matters."
        emile.name "Plus if you ask me, they gave you an upgrade. Makes a change from how you were before."
        pc "Ugh, you still going to make fun of me about that? What was it you used to call me?"
        show emile neutral

        call screen perk_choice(perk_origin_list)
        $ player.check_perk_combo()
        emile.name "Because you were. Anyway, what makes you who you are isn't just how you look. Plus I am sure with a bit of work you will be fighting the guys off with a stick."
        if emile.showing:
            pc "You're one to talk. Doesn't look like you have been beating them off."
        else:
            pc "*Sigh* Was bad enough before. You telling me it's gonna be worse?"
        emile.name "Maybe..."
        emile.name "Probably..."
        emile.name "The way things have changed since you were asleep means it's probably going to be a lot worse."
        $ player.face_worried()
        pc "Changed?"
        emile.name "..."
        emile.name "Let's talk about that later. Just know that a lot has changed for you to get used to."
        $ walk(loc_market)
        show emile neutral
        $ player.face_neutral()
        emile.name "And talking of getting used to things, here we are."
        emile.name "Ready to get you into some proper clothes?"
        pc "Yes, the wind blowing up my gown is driving me crazy."
        emile.name "Great, let's grab you some essentials and get you home to relax."

    $ walk(loc_market)
    show emile neutral
    if player.male_origin:
        emile.name "So first things first, we need to get you a bra."
        $ player.face_worried()
        pc "What?"
        show emile happy
        emile.name "The worst comes first! Sorry [name], but gotta get you fitted. The most important part of a girl's wardrobe is a well fitting bra."
        pc "Yeah throw me in the deep end why don't you!"
        if player.breasts == 3:
            emile.name "Looks like they gave you some pretty impressive ones as well. You are going to need them."
            pc "..."
        $ walk(loc_market_stall_needle)
        show emile neutral
        $ player.mouth = 8
        emile.name "Well not quite. Doesn't even look like they have someone to measure you. Should probably get you a sports bra and leave the fitting for another day."
        $ player.mouth = 1
        $ player.brow = 1
        pc "Sounds good to me."
        show emile happy
        emile.name "Me too. Since it's me who's paying! Bras are expensive!"

    elif player.has_perk([perk_bimbo, perk_commando, perk_slut]):
        $ player.add_comfort(30)
        $ emile.dict["tut_anger"] += 1
        emile.name "I was thinking we would start off with a bra, but knowing you, you probably aren't interested."
        $ walk(loc_market_stall_needle)
        if player.has_perk(perk_commando):
            pc "Not really."
        else:
            pc "Just some knickers would do the job."
            if player.breasts == 3:
                emile.name "Even with those massive things?"
                pc "Even better."
                $ emile.dict["tut_anger"] += 1
        emile.name "Ugh, right..."
        jump start_shopping_4_dress_slutty
    else:
        if not player.breasts == 1:
            emile.name "So judging by how you have been bouncing around while walking here, maybe we should look at bras first."
            $ player.face_shock()
            pc "What?"
            show emile happy
            emile.name "You new friends there seem to have a mind of their own."
            $ player.face_annoyed()
            pc "Yeah way to make me not feel self conscious about myself."
            emile.name "Don't worry, I am sure only those who were on the same street as us noticed."
        else:
            emile.name "So should probably start off with some underwear."
        $ walk(loc_market_stall_needle)
        show emile neutral
        $ player.face_neutral()
        pc "..."
        pc "This doesn't look like the type of place that will do bra fitting. Should probably stick to a sports bra for now."
        show emile happy
        emile.name "Great!"
        pc "Huh?"
        emile.name "Well it's me who's paying and bras are expensive."

    show emile neutral
    emile.name "Hmmm..."
    emile.name "These look good, c'mon, let's try them out."

    menu:
        "Let's? Both of us?":

            $ player.face_worried()
            pc "Let's? You want to come with me to the changing rooms?"
            if emile.days_pregnant > (global_pregnancy_length * 0.3):
                pc "Don't think we will fit in there together with your extra passenger."
                emile.name "We will make do. Unless you wanna be alone?"
            else:
                emile.name "Well yeah... Unless you would prefer to be alone?"
            menu:
                "No, it's fine...":

                    $ player.add_comfort(5)
                    pc "Err, no. I suppose it's fine."
                    emile.name "Ok, let's go."
                    jump start_shopping_2_sis
                "Yeah, I think alone is better":

                    pc "Yeah I think I would prefer to do this alone."
                    emile.name "Okay then, if you insist."
                    $ emile.dict["tut_anger"] += 1
                    jump start_shopping_2_alone
        "Ok.":

            pc "Sure, but no more talk about my bouncy new friends."
            if emile.days_pregnant > (global_pregnancy_length * 0.3):
                emile.name "Only if you shut up about the belly."
            else:
                emile.name "Okay let's go!"
            $ player.add_comfort(10)
            jump start_shopping_2_sis






label start_shopping_2_sis:

    $ walk(loc_mall_changingroom)
    $ player.mouth = 1
    $ player.brow = 1
    emile.name "Ok, take off the gown and try them on."
    $ pc_strip()
    $ player.update_stats()
    show emile worried
    emile.name "Wow, just the gown? They didn't even splash out for some underpants?"
    emile.name "Looks like we need to pop into the cosmetics shop as well before we head home. Got a bit of a gorilla look going on down there!"
    $ player.face_worried()
    show emile neutral
    pc "Think you could focus on something other than my legs?"
    emile.name "Wasn't talking about your legs, but sure. Try out the bras then we can pick out some other bits for ya."
    $ daily.bra_primary_colour = "white"
    $ daily.bra_secondary_colour = "blue"
    $ c.bra = 2
    if player.male_origin:
        emile.name "How does it feel?"
        pc "How is it supposed to feel? I have no idea if this is good or bad. It feels like I have a sports bra on!"
        emile.name "Okay ok... Try the other one."
    else:
        emile.name "Bit of a big one isn't it? Wouldn't be easy to hide under your clothes."
        pc "Mmmm."
        emile.name "Ok, try the other one."
    $ player.brow = 1
    $ daily.bra_primary_colour = "blue"
    $ daily.bra_secondary_colour = "navy"
    $ c.bra = 3
    if player.male_origin:
        emile.name "It shouldn't feel too tight or too loose. And certainly not cut into the skin."
        pc "..."
        emile.name "Ok, probably too much to ask. Well then pick the one you like the look of most."
    else:
        emile.name "Got a bit of cleavage going with that one."
        pc "..."
        emile.name "What do you think?"
    pc "Hmmm..."
    call screen inventory_clothes_choice([item_bra_2, item_bra_3])
    if c.bra == 2:
        $ daily.bra_primary_colour = "white"
        $ daily.bra_secondary_colour = "blue"
    pc "This one I suppose..."
    emile.name "Okay great. Let's take it. Put your gown back on and I'll find you something proper to wear."
    hide emile with dissolve
    $ c.outfit = 1
    jump start_shopping_3





label start_shopping_2_alone:
    hide emile
    $ walk(loc_mall_changingroom)

    $ player.mouth = 8
    $ player.brow = 1

    if player.male_origin:
        pc "Never thought I would be in a changing room trying on bras!"
        pc "Okay let's give this a go."
    else:
        pcm "*Phew* A moment to breathe without her commenting about my body."
    $ pc_strip()
    $ player.update_stats()
    pcm "..."
    show sb_pose_lookback with dissolve
    pcm "First time I've properly seen myself in the mirror."
    pcm "Myself? Is this really me? My new body, new life? Everyone keeps saying I need to get used to it."
    pcm "But is this really me?"
    menu:
        "She's me, what else is there?":

            $ player.add_conf(5)
            $ player.add_comfort(20)
            pcm "Of course she is me. Looking a bit different doesn't change who I am."
            if player.male_origin:
                pcm "Even if I do have tits now..."
            elif player.breasts == 3:
                pcm "Even if I do suddenly have massive tits..."
        "I haven't a clue who I am now":

            $ player.add_comfort(-10)
            pcm "One moment I am one person, then I wake up in the hospital and now a stranger is looking at me in the mirror. I haven't a clue who or what I am."

        "But aren't I still a man?" if player.male_origin:
            $ player.add_comfort(-25)
            pc "Being in a different body doesn't change who I am. I am still the guy I always was... aren't I?"
            if player.breasts == 3:
                pcm "Even if I do suddenly have massive tits..."
                $ player.add_comfort(-15)

    emile.name "Everything okay in there?"
    hide sb_pose_lookback with dissolve
    $ player.face_shock()
    pc "Yeah fine, I'm just..."
    emile.name "Yeah yeah, I don't need the details."
    $ player.face_worried()
    pc "..."
    pcm "Ok, better try these out."
    $ daily.bra_primary_colour = "white"
    $ daily.bra_secondary_colour = "blue"
    $ c.bra = 2
    if player.male_origin:
        pc "Ok... Does being a girl let me automatically know if this is good or not?"
    else:
        pcm "Should have decent support but they it's a bit big."
    pcm "Suppose I should try the other."
    $ daily.bra_primary_colour = "blue"
    $ daily.bra_secondary_colour = "navy"
    $ c.bra = 3
    $ daily.bra = 3

    if player.male_origin:
        pc "Nope, still haven't a clue what I am doing..."
        pc "Maybe I should have let [emile.name] change with me."
        $ wardrobe.take(item_bra_3)
    else:
        pcm "Less support but would go nicer with every day clothes. Especially since I have no idea when I will be able to expand my wardrobe."
        call screen inventory_clothes_choice([item_bra_2, item_bra_3])
        if c.bra == 2:
            $ daily.bra_primary_colour = "white"
            $ daily.bra_secondary_colour = "blue"
            pause 0.5
    $ c.outfit = 1
    show emile at right1
    $ walk(loc_market_stall_needle)
    emile.name "Picked one you like?"
    pc "Yeah..."
    show emile happy
    emile.name "Haha, well I suppose it was too much to ask to find something you liked. Now to get you something proper to wear."
    hide emile with dissolve
    jump start_shopping_3





label start_shopping_3:

    if not loc_cur == loc_market_stall_needle:
        $ walk(loc_market_stall_needle)
        pc "..."
    else:
        $ player.face_worried()
        pcm "Hope she wasn't upset I went alone."
        pcm "Ah well..."
    show emile neutral at right1 with dissolve

    if player.male_origin:
        emile.name "I got something to wear and picked up some underwear for you to..."
        $ player.face_shock()
        pc "Knickers?"
        emile.name "Don't worry, they don't let you try those on so we can just pick them off the rack."
        $ player.face_worried()
        emile.name "I don't suppose you need all the details. But there are 3 types mostly."
        pc "Sure, a lesson on girls' knickers."
        show emile happy
        emile.name "Yup. Gotta help a new girl out."
        show emile neutral
        emile.name "So we have boy shorts. Might be what you are used to. Although girl ones are not as loose."
        emile.name "Briefs are smaller and the more common type you will see girl's wearing. They come in every design and pattern you can imagine."
        emile.name "And the smaller ones like thongs, not sure you want to start out with those."
        emile.name "So I picked up a few packs but I am not rich so pick what you like the look of."
    else:
        emile.name "I got something to wear and picked up some underwear for you to choose."
        pc "Sounds good."
        emile.name "I am not rich so pick a pack you like the look of and ill put the rest back."
    call screen inventory_clothes_choice([item_pants_1, item_pants_4, item_pants_5])

    if c.thong:
        $ player.add_comfort(10)
        if player.body_conf < -150:
            emile.name "Let's not go too extreme right away. Stick to some simple briefs for now and try some other stuff once you are used to things more."
            $ wardrobe.drop(item_pants_5)
            $ wardrobe.take(item_pants_1)
            $ daily.pants = 1
            $ c.pants = 1
            pc "If you say so..."
        else:
            emile.name "You sure? First day in that body and you are already looking to show off your arse in a thong? Shouldn't you make do with some briefs?"
            menu:
                "Yeah you are probably right.":

                    $ wardrobe.drop(item_pants_5)
                    $ wardrobe.take(item_pants_1)
                    $ daily.pants = 1
                    $ c.pants = 1
                    pc "Ok, If you say so."
                    emile.name "Okay let's grab a pack in your size. We will just stick to white for now"
                "What's wrong with thongs?":

                    $ daily.pants = 5
                    $ emile.dict["tut_anger"] += 1
                    $ player.add_conf(5)
                    $ player.add_comfort(10)
                    if player.male_origin:
                        pc "Gotta get used to being a girl isn't it? So let's go for something entirely girly."
                        show emile worried
                        emile.name "If you insist. Here, take these ones. They are fairly normal as far as thongs go"
                    else:
                        pc "They don't give you a noticeable panty line and tend to stay in place."
                        show emile worried
                        emile.name "If you insist. Here, take these ones. They are fairly normal as far as thongs go"
    else:


        emile.name "Okay let's grab a pack in your size. We will just stick to white for now"
    show emile neutral
    emile.name "Best to wash them before you wear them. But we don't have a lot of choice so you should put a pair on when we are trying on some clothes."
    if player.body_conf < -140 or player.has_perk([perk_nerd, perk_gamine, perk_bambi]):
        jump start_shopping_4_trousers
    elif c.thong or player.has_perk([perk_gym_bunny]):
        jump start_shopping_4_dress_slutty
    else:
        jump start_shopping_4_dress

label start_shopping_4_dress:
    show emile neutral at right1
    emile.name "Since summer is around the corner, let's get you something cool."
    pc "Sounds good to me."
    hide emile with dissolve
    pcm "Still feel like I am coming down with the world's biggest hangover..."
    pcm "Being dragged around here doesn't help matters much. Hopefully can get home soon and just..."
    pcm "Process things?"
    show emile at right1 with dissolve
    emile.name "We are almost done. Here, put these on and we will head off to pay for them."
    hide emile
    $ walk(loc_mall_changingroom)
    pause 0.5

    $ c.pants = 0
    $ pc_strip_tops()
    $ daily.outfit_primary_colour = "sky"
    $ daily.outfit = 3
    $ wardrobe.take(item_outfit_3)
    pause 0.5
    $ pc_dress_under()
    if c.thong:
        $ player.face_worried()
        pcm "These really are tiny. The don't cover anything and ride right up my arse."
        pcm "Oh well, can't back out now and ask [emile.name] for another pair."

    if player.male_origin:
        $ player.face_worried()
        pcm "Err..."
        pcm "She got me a dress..."
        pc "Are you there [emile.name]?"
        pcm "..."
        pcm "Guess not."
        pcm "..."
        pcm "No choice I suppose."
        if c.thong:
            $ wardrobe.drop(item_outfit_3)
            $ wardrobe.take(item_outfit_4)
            $ daily.outfit = 4
            $ pc_dress_slow()
            $ player.face_meek()
            pcm "Err... What the hell. This dress doesn't suit this bra at all..."
            pcm "Looks like I got dressed in a tornado."
            $ player.face_annoyed()
            pcm "Let's see..."
            pc "Nng!"
            $ c.bra = 0
            $ daily.bra = 0
            with hpunch
            $ player.face_happy()
            pcm "Better..."
            $ player.face_meek()
            pcm "Err... Fuck. Is it better?"
            if player.breasts == 3:
                pcm "These things they gave me are ready to spill out of the dress..."
                pcm "And looks like my nipples are poking through."
            else:
                pcm "Looks like my nipples are poking through the dress. And this dress doesn't really hide much."
            pcm "Better than the stupid bra though. Couldn't you have got me something better [emile.name]?"
    else:
        pause 0.5
    $ player.face_neutral()
    $ pc_dress_slow()
    pause 0.5

    jump start_shopping_4_cosmetics

label start_shopping_4_trousers:
    if not loc_cur == loc_market_stall_needle:
        $ walk(loc_market_stall_needle)
    show emile neutral at right1
    if player.male_origin:
        emile.name "As for clothes, let's stick to something you are used to. Some simple trousers and a top. Wait by the changing rooms and I'll bring you something."
    else:
        emile.name "As for clothes, let's stick to something simple. Some simple trousers and a top. Wait by the changing rooms and I'll bring you something."
    pc "Sounds good to me."
    hide emile with dissolve
    if player.male_origin:
        pcm "Bras, knickers, blouses... Not something I thought I would be concerned about..."
        pcm "Well, at least not on me..."
        pcm "*Sigh*"
    else:
        pcm "Still feel like I am coming down with the world's biggest hangover..."
        pcm "Being dragged around here doesn't help matters much. Hopefully can get home soon and just..."
        pcm "Process things?"
    show emile at right1 with dissolve
    emile.name "We are almost done. Here, put these on and we will head off to pay for them."
    hide emile
    $ walk(loc_mall_changingroom)


    $ c.pants = 0
    $ pc_strip_tops()

    $ daily.bottom_primary_colour = "black"
    $ daily.top_primary_colour = "black"
    $ daily.top_secondary_colour = "crimson"

    $ daily.top = 7
    $ daily.bottom = 4
    $ wardrobe.take(item_top_7)
    $ wardrobe.take(item_bottom_4)

    pause 0.5
    $ pc_dress_slow()
    pause 0.5

    jump start_shopping_4_cosmetics

label start_shopping_4_dress_slutty:
    show emile neutral at right1
    emile.name "Right... Well since summer is around the corner, let's get you something cool."
    pc "Sounds good to me."
    emile.name "I bet. Ill go and pick something out."
    hide emile with dissolve
    pcm "Still feel like I am coming down with the world's biggest hangover..."
    pcm "Being dragged around here doesn't help matters much. Hopefully can get home soon and just..."
    pcm "Process things?"
    show emile at right1 with dissolve
    emile.name "We are almost done. Here, put these on and we will head off to pay for them."
    hide emile
    $ walk(loc_mall_changingroom)
    pause 0.5
    $ player.update_stats()
    $ pc_strip_tops()


    if player.has_perk(perk_bimbo):
        $ daily.bra = 0
        $ daily.outfit_primary_colour = "sky"
        $ daily.pants_primary_colour = "white"
        $ daily.pants_secondary_colour = "grey"
        $ daily.outfit = 11
        $ wardrobe.take(item_outfit_11)
        $ daily.pants = 5
        $ wardrobe.take(item_pants_5)
    elif player.has_perk(perk_commando):
        $ daily.bra = 0
        $ daily.pants = 0
        $ daily.outfit_primary_colour = "sky"
        $ daily.outfit = 4
        $ wardrobe.take(item_outfit_4)
    elif player.has_perk(perk_exhibitionist):
        $ c.pants = 0
        $ daily.bra = 0
        $ daily.outfit_primary_colour = "sky"
        $ daily.outfit = 4
        $ wardrobe.take(item_outfit_4)
    else:
        $ daily.pants = 5
        $ daily.bra = 0
        $ daily.outfit_primary_colour = "sky"
        $ daily.outfit = 4
        $ wardrobe.take(item_outfit_4)
        $ wardrobe.take(item_pants_5)

    pause 0.5


    $ player.face_neutral()
    $ pc_dress_slow()
    pause 0.5
    if c.bra:
        $ player.face_meek()
        pcm "Errr... This dress looks terrible with this bra."
        $ c.bra = 0
        $ daily.bra = 0
        pcm "Better, but I should probably get something else and not bounce around everywhere."
    jump start_shopping_4_cosmetics

label start_shopping_4_cosmetics:
    $ walk(loc_market_stall_needle)

    if c.skirt:
        if player.male_origin:
            $ player.face_worried()
            pc "..."
        else:
            pcm "Not too bad I guess..."
    elif player.male_origin:
        pcm "This top is tiny, doesn't cover my belly at all. And isn't it kinda see through?"
        pcm "And these trousers. Basically riding right up my arse."
    else:
        pcm "Guess I can't complain. Top is a bit tacky but beggars can't be choosers."
    show emile happy at right1 with dissolve
    if c.slutty and not player.male_origin:
        emile.name "Yup, just as I remember. Spilling out at the top and the bottom."
        show emile neutral
        if player.breasts == 3:
            emile.name "Although spilling out at the top far more than you used to."
            $ player.eye = 6
            pc "Really?"
            $ player.face_happy()
            pc "So I am..."
            emile.name "Ugh."
        $ player.face_neutral()
        emile.name "Though looks like you need to sort those legs out."
    elif player.male_origin and c.slutty:
        if player.breasts == 3:
            emile.name "Wow. Err... Okay then. You are aware..."
            pc "That these things are ready to jump out my clothes?"
            emile.name "Right... And the bra?"
            pc "It looked stupid with this dress you got me."
        else:
            emile.name "What happened to the bra? Looks like you are ready to poke someone's eye out."
            pc "It looked stupid with this dress you got me."
        emile.name "Well, Okay then. Already know what to wear with what."
        pc "..."
        emile.name "Wouldn't have paid for it if I knew."
        emile.name "But looks like you need to sort those legs out."
    elif player.male_origin and c.skirt:
        pc "You got me a dress?"
        emile.name "Yeah. What's wrong with that?"
        pc "Considering how little maintenance this body has had. I am expecting Saxton Hale to charge in at any moment and try to capture me."
        show emile neutral
        emile.name "Hmm true, you do need to sort those legs out."
    elif c.top and player.breasts == 3:
        emile.name "Looking good. Didn't realise your new assets would stand out so much in that top though."
        emile.name "A bit of sun and a run on the treadmill and I might start getting jealous."
    else:
        emile.name "Looking good. A bit of run on the treadmill and I might start getting jealous."




    $ player.mouth = 2
    emile.name "And get a haircut."
    $ player.mouth = 9
    $ player.brow = 3
    emile.name "And a bit of blush..."
    show emile neutral
    emile.name "Let's get you home. Can't imagine today has been easy for you."
    $ player.mouth = 8
    menu:
        "Thanks for being here":

            pc "No it hasn't been, but thanks for being here."
            emile.name "..."
        "Can't say it has been":

            $ emile.dict["tut_anger"] += 1
            pc "Can't say it's been one of my best days..."
            emile.name "..."

    emile.name "But before we head home we should buy you some bits from the cosmetics shop."
    pc "The cosmetics shop?"
    emile.name "Yeah, you will probably need some makeup and razors to take care of yourself with."
    $ player.mouth = 9
    $ player.brow = 3
    pc "Mmm, but nothing more. I don't want to spend another hour in this place."
    $ walk(loc_market)
    show emile at right1
    emile.name "Yeah ok. Today has probably been exhausting for you even though it's only been a couple of hours."
    $ player.mouth = 8
    pc "You could say that."

    emile.name "Ok, I will just get some basics. You can deal with the rest another day"
    emile.name "This and this should do, I'll go and pay."
    hide emile with dissolve
    pc "..."
    show emile at right1 with dissolve

    emile.name "Don't worry, we'll get you adjusted..."


    show emile at right1
    $ player.mouth = 1
    pc "Thanks..."
    emile.name "I'm serious [name]! You need to look after yourself. You cannot let a brand new body like that go to waste."
    $ walk(loc_market)
    show emile at right1
    pc "I haven't had a moment to even scratch my ass and I'm already struggling under the weight of all this."
    emile.name "Language [name], not very lady like of you."
    $ player.mouth = 8
    $ player.eye = 2
    pc "Not helping."
    show emile happy
    emile.name "Haha, maybe not. But it's fun."
    $ walk(loc_residential)
    show emile neutral
    $ player.mouth = 1
    $ player.eye = 1
    emile.name "Not far now. Then you can relax and avoid thoughts of hanging from the ceiling fan."
    if emile.days_pregnant > (global_pregnancy_length * 0.3):
        emile.name "And fuck! I could do with getting off my feet. Not easy walking around all day like this."
        pc "I bet."
    pc "How do you know where I live? Don't you live somewhere else?"
    emile.name "After your accident The Institute set me up there for a while. Lived there for a couple of months before I moved further into the city."
    pc "The hospital did?"

    if emile.dict["tut_anger"] == 0:
        emile.name "Yeah, the hospital, well, Institute, helped me out with a place to stay so I could check up on you."
        pc "Why would they care?"
        emile.name "Guess they figured keeping me happy would keep you happy after you got out."
        $ walk(loc_stairwell)
        show emile at right1
        emile.name "And here we are. Kinda nice being back."
    elif emile.dict["tut_anger"] > 3:
        emile.name "Yeah, The Institute thought that treating me well would make things easier for you so I took advantage of it."
        $ player.brow = 3
        $ player.mouth = 8
        pc "Took advantage?"
        $ walk(loc_stairwell)
        show emile at right1
        emile.name "Here we are. Let's get you sorted out"
    else:
        emile.name "Yeah, the hospital, well, Institute, tried to help me out where they could on account of you being their prized subject."
        $ player.brow = 3
        $ player.mouth = 8
        pc "Subject?"
        $ walk(loc_stairwell)
        show emile at right1
        emile.name "Here we are. Home sweet home!"
    jump start_home_1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
