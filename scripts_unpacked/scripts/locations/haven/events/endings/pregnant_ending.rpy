label haven_pregnant_ending_start:
    $ player.face_worried()
    $ add_to_list(main_quest_05.list, "pregnant_exit")
    pcm "Fuck... My belly is getting bigger..."
    pcm "I'm pregnant aren't I?"
    pcm "Shit shit shit..."
    $ player.face_worried()
    pcm "Fuck. I can't be staying around this shithole while carrying a baby."
    pcm "Place is bad enough even under normal circumstances. Carrying this thing around will end up with us both dead in no time..."
    pcm "Ugh, the fuck do I do?"
    pcm "..."
    pcm "[ant.name] is a doctor, or at least was. Maybe I can use that as an excuse."
    pcm "Ugh, no other choice."
    pcm "Need to pretend to be some knocked up Gamine looking for a doctor."
    pcm "Pretend... Fuck, it's just what I am."
    $ walk(loc_haven_landing)
    $ player.face_worried()
    pc "Err, hi..."
    if not haven_guard_hours():
        show haven_guard2 at right1 with dissolve
        havenmeanguard.name "Piss off."
        pc "I know I'm not allowed. But I need to speak to [alex.name] about a doctor for my baby."
        havenmeanguard.name "Don't give a shit. Fuck off!"
        pc "Please. I am desperate..."
        havenmeanguard.name "*Tsk*."
        havenmeanguard.name "Only way you gettin' up 'ere is if you leave the rest o' us happy."
        havenmeanguard.name "Wanna come up?"
        if player.has_perk(perk_whore):
            pcm "Just like I expected."
        else:
            pcm "Fuck..."
        pc "Err..."
        pc "No other way?"
        havenmeanguard.name "Nope. I don't give a fuck 'bout your belly or your kid. Fuck off and die in a ditch for all I care."
        havenmeanguard.name "Lettin' you up there needs to be worth my while."
        pc "Right..."
        pc "No choice then I guess..."
        havenmeanguard.name "Nope."
        $ loc_haven_landing.dict["gate_open"] = True
        havenmeanguard.name "C'mon."
        pc "..."
        $ walk(loc_haven_toplanding)
        $ walk(loc_haven_hallway_3f)
        pc "So where is [alex.name]?"
        havenmeanguard.name "At tha end there. But you coming wit' me first. Whore that arse out then you can go see 'bout your baby."
        pc "..."
        $ walk(loc_haven_guardroom)
        show haven_guard3 at right3 with dissolve:
            xzoom 1
        havguard "What we got ere?"
        havenmeanguard.name "Some whore looking for an escape."
        havguard "Oh? Sounds like fun."
        $ player.face_worried()
        pcm "Fuck... What have I gotten myself into..."
        pc "..."
        $ havguardw = Character('Haven guard', color="#ffffff")
        jump haven_whore_ending_catcher
    else:

        $ add_to_list(main_quest_05.list, "pregnant_exit_nice_guard")
        show haven_guard1 at right1 with dissolve
        if not havengateguard.has_met:
            havengateguard.name "Sorry love. Not allowed up here."
            pc "I know..."
        pc "I was wondering if there was some way to speak to [alex.name]. I am pregnant and I know he knows the doctor round here."
        havengateguard.name "Oh?"
        havengateguard.name "No way I can let you up here. The other guys will tear me apart if I do."
        pc "What? There is no way? I just need to speak to [alex.name] for 5 minutes."
        havengateguard.name "My neck on the line if you get caught. I ain't risking livin' back in the slum for this."
        pc "Please. I don't want to carry a baby round here."
        havengateguard.name "Best I can do is get you upstairs as a whore to entertain the guys. How you speak to [alex.nname] after that is on you."
        pcm "Fuck..."
        pcm "Better than nothing though. Not like I have much choice in the matter."
        pcm "Unless I want to be hanging round here all fat..."
        pc "Err, I suppose..."
        havengateguard.name "Really?"
        pc "I can't stay around here. Too risky."
        havengateguard.name "Right then. Well, ok..."
        $ loc_haven_landing.dict["gate_open"] = True
        havengateguard.name "Come on then."
        $ walk(loc_haven_toplanding)
        havengateguard.name "I'll try and make it easy for you by calming the guys down a bit. But you are gonna have to do a lot of work."
        pc "Right..."
        $ walk(loc_haven_hallway_3f)
        pc "So where is [alex.name]?"
        havenmeanguard.name "At the end there."
        pc "..."
        $ walk(loc_haven_guardroom)
        jump haven_whore_ending
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
