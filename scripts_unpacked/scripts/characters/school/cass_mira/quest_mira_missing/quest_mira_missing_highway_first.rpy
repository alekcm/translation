label quest_mira_missing_go_highway_first_prompt:
    pcm "[cass.name] wants to go to the highway and ask around. Is now a good time?"
    menu:
        "Go with her now":
            jump quest_mira_missing_go_highway_first_start
        "Another time":
            pcm "Shouldn't leave it too long though..."
            jump travel

label quest_mira_missing_go_highway_first_start:
    show cass at right1 with dissolve
    pc "So, want to head off to the highway?"
    cass.name "Yeah, let's go. Can get the bus to the truck stop and walk."
    $ walk(loc_busstop_school)

    if "cass_knows" in quest_whore.list:
        cass.name "Hope we can find something out. I still can't believe you two did this."
    else:
        cass.name "Hope we can find something out. I'm still not convinced she was working there."

    pc "Got to do what you need to do get by these days."
    hide cass with dissolve
    show cass at right6
    $ walk(loc_bus_interior)
    cass.name "Maybe. But didn't seem like she was desperate for money. Isn't it just junkies that do that sort of thing?"
    pc "I guess..."
    cass.name "Plus, she didn't seem... you know... whore like..."
    pc "Almost everyone is a whore these days. Just a matter of price."
    if cass.sold:
        cass.name "Yeah... I guess..."
    else:
        cass.name "I've never done that."
        if player.sold:
            pc "Give it time."
        else:
            pc "Nor me, but we are the minority."
    cass.name "Getting close."
    hide cass with dissolve
    $ walk(loc_busstop_truckstop)
    $ walk(loc_truckstop)
    if "cass_knows" in quest_whore.list and quest_whore.sold > 5:
        $ add_to_list(quest_mira_missing.list, "investigate_whore_route")
        show cass at right1 with dissolve
        pc "It's a bit early so not so busy right now."
        show cass worried
        cass.name "Yeah, I don't see too many... errr..."
        pc "Whores, Street walkers, Highway girls, Strumpets, Girls of negotiable aff..."
        cass.name "Yeah I get it..."
        pc "Well, let's see who is around and ask them."
        cass.name "No. I need to do this myself."
        pc "Err, why?"
        cass.name "They will talk to me if you are around. But what about tomorrow or the next day when you aren't here?"
        pc "They will ignore you."
        cass.name "Yeah. So that's pointless for me. Then I won't get anywhere."
        pc "Hmmm, okay. Just be sure to scream if any problems."
        cass.name "Err, okay..."
        hide cass with dissolve
        pcm "No one will speak to her..."
        pcm "She will come back with nothing."
        pcm "Ugh..."
        "I stand around for a while waiting for [cass.name] to return."
        $ relax(20)
        pcm "Hmm, I see her. Doesn't look too happy."
        show cass worried at right1 with dissolve
        cass.name "Well, you were right..."
        pc "Mmmm."
        cass.name "What now?"
        pc "Now you leave it to me."
        cass.name "Ugh! I don't want to just forget about it."
        pc "Unless you are willing to do the same as we have, you don't have much choice."
        cass.name "..."
        hide cass with dissolve
        pc "Err..."
        pc "Where are you going?"
        show cass worried at right1
        $ walk(loc_busstop_truckstop)
        cass.name "Give me time to think [name]."
        hide cass with dissolve
        pcm "Err, right then..."
        $ log.markdone("mira_missing_04")
        $ log.markdone("mira_missing_05")
    else:
        $ add_to_list(quest_mira_missing.list, "investigate_nowhore_route")
        show cass at right1 with dissolve

        if any([rose_here(dis_truckstop.locs), kitty_here(dis_truckstop.locs), charity_here(dis_truckstop.locs), pursy_here(dis_truckstop.locs)]):
            cass.name "There are some people around. Should we ask around?"
            pc "Yeah I guess so."
            cass.name "Okay..."
            hide cass with dissolve
            if rose_here(dis_truckstop.locs):
                $ temp_var_1 = rose.last_spoke_to
                pcm "Guess I'll speak to her."
                pc "Err, hey."
                show rose at right1 with dissolve
                rose.name "What you want? Don't look like a whore or a customer."
                pc "I'm trying to find out about a friend of mine."
                rose.name "Good for you."
                hide rose with dissolve
                $ player.face_worried()
                pcm "Err... Okay then..."
                $ rose.last_spoke_to = temp_var_1
            if kitty_here(dis_truckstop.locs):
                $ temp_var_1 = kitty.last_spoke_to
                pcm "Let's see..."
                $ walk(kitty_here(class_loc=True))
                show kitty at right1 with dissolve
                pc "Hi, I'm trying to find a friend who works round here."
                $ player.face_worried()
                kitty.name "Fuck off!"
                hide kitty with dissolve
                pcm "Right..."
                $ kitty.last_spoke_to = temp_var_1
            if charity_here(dis_truckstop.locs):
                $ temp_var_1 = charity.last_spoke_to
                $ walk(charity_here(class_loc=True))
                show charity at right1 with dissolve
                pc "Hi. My friend is missing and I wanted to know if you knew something."
                charity.name "Don't know nothing about nothing."
                pc "She worked here, you might know her."
                hide charity with dissolve
                $ player.face_worried()
                pcm "Ugh!"
                $ charity.last_spoke_to = temp_var_1
            if pursy_here(dis_truckstop.locs):
                $ temp_var_1 = pursy.last_spoke_to
                $ walk(pursy_here(class_loc=True))
                show pursy at right1 with dissolve
                pc "I am looking for my friend. She worked here and I can't see her anywhere."
                $ player.face_worried()
                pursy.name "*Tsk* Fuck off cunt!"
                pc "She might be missing and..."
                pursy.name "Don't give a fuck. Piss off!"
                hide pursy with dissolve
                pcm "..."
                $ pursy.last_spoke_to = temp_var_1
            pcm "No one speaking at all..."
            pcm "[mira.name] could have been friends with one of them and they still keep quiet."
            pc "Ugh!"
            $ walk(loc_truckstop)
            pcm "So what now?"
            show cass worried at right1 with dissolve
            cass.name "Any luck?"
            pc "None."
            cass.name "Nor me..."
        else:

            cass.name "I don't see too many people around."
            pc "No. Probably too early."
            cass.name "Might as well ask around anyway."
            pc "Yeah."
            hide cass with dissolve
            "I walk around and try and ask people. But there aren't too many around and those that are here give me a dirty look or tell me to fuck off."
            $ relax(10)
            $ player.grope()
            pc "Ah!"
            $ player.grope_end()
            guy "Come on, let's go 'ave some fun."
            pc "No!"
            "I walk away and try and see if I can find [cass.nname]"
            show cass at right1 with dissolve
            pc "Anything?"
            cass.name "No. Not too many people here and I don't really feel safe just hanging around."

        pc "..."
        cass.name "Any ideas?"
        pc "I can ask around some people I know. See if they have any ideas on what to do."
        pc "But doesn't look like the girls here are going to speak to us."
        cass.name "No. Probably put a knife in us if we push it."
        pc "Mmmm."
        cass.name "Okay... Well no point hanging around this shithole."
        pc "Yeah..."
        hide cass with dissolve
        pcm "Err. See you round?"
        $ log.markdone("mira_missing_04")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
