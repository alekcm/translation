label quest_mira_missing_whore_investigation_security:
    $ add_to_list(quest_mira_missing.list, "investigate_asked_security")
    show paige at right1
    pc "Err, hi. I'm looking into a girl going missing."
    paige.name "Ah, okay... That happens a lot here. You might... err... want to not look into it."
    pc "Yeah, not going to happen."
    paige.name "Well, okay. But not sure what you think we can do. You have seen this place."
    paige.name "And the people who work here..."
    pc "Yeah, figured it would be a waste of time coming here. But I don't have too many options."
    pc "She was a whore. I've tried to talk to the people round the highway but no one will speak with me."
    paige.name "No, they won't talk with anyone who isn't a whore."
    if quest_whore.sold:
        pc "I know. Was hoping you had other options."
        paige.name "If you want to the... ah.. whores? If you want the girls to speak. You have to be one."
        paige.name "We've, ah... I've? Hmmm... Dressed up and tried to look like one."
        paige.name "Didn't work. They know their own."
        paige.name "They asked if I was willing... to, y'know... but I wasn't."
        pc "I was hoping you might have info on whores going missing or know somewhere else I can look."
        paige.name "Not here. It gets ignored. They don't care here what happens to some... err... Gamines."
        paige.name "There is a P.I. you could talk to, but he would have the same problem."
        if simon.has_met:
            pc "[simon.name]?"
            paige.name "Ah, you know him?"
            pc "Yeah, He was also on my list of people to ask. Hoped you would know more though."
        else:
            pc "A P.I.?"
            paige.name "Yeah, we sometimes use outside help. But we are all in the same boat when it comes to trying to get info from the highway."
            pc "Hmmm..."
        pc "Well, thanks."
    else:
        pc "No? So if I dressed up?"
        paige.name "No, won't work..."
        paige.name "We've, ah... I've? Hmmm..."
        paige.name "It's been tried. Doesn't work. They know their own."
        pc "Right..."
        pc "Any other ideas?"
        paige.name "No. Not unless..."
        pc "Hmmm?"
        paige.name "They asked if I was willing, but I wasn't."
        pc "What do you mean?"
        paige.name "Only way they will speak with you is if you are a whore."
        pc "Oh..."
        pc "Right, I think I understand."
        pc "Well, thanks anyway."
    paige.name "Good luck."
    paige.name "I think if you manage it, to... y'know. Somehow get good with them. You should speak to [cam.name]. He'd love to have someone like that."
    pc "Right... Don't get your hopes up."
    paige.name "Better you than me."
    pc "I bet."
    hide paige with dissolve
    $ walk(loc_checkpoint)
    pcm "So, they know their own..."
    if player.has_perk(perk_gamine) or quest_whore.active:
        pcm "Not a shock really. Whores stick together. Anyone you haven't seen taking a dick could be undercover. Least that's how it used to be."
    else:
        pcm "So, being a whore is one option... A terrible option..."
        pcm "Not managing to find out anything else though."
    pcm "Ugh..."
    $ log.markdone("mira_missing_05")
    jump travel

label quest_mira_missing_whore_investigation_simon:
    $ add_to_list(quest_mira_missing.list, "investigate_asked_simon")
    show simon at right1 with dissolve
    pc "Can I make use of your P.I. talents?"
    simon.name "Can try. What do you need?"
    pc "I need to be able to get info from the whores at the highway."
    if simon.sold or bob.sold:
        simon.name "Well, you are a whore so just go be a whore."
        if player.has_perk(perk_whore) or quest_whore.active:
            pc "What do you mean?"
            simon.name "The girls there look out for each other. They won't talk to anyone who isn't their own."
            simon.name "You're a whore, so go to the highway, fuck some punters and have a chat with the girls there. They will warm to you quickly enough."
            pc "Easy as that?"
            simon.name "For you, yes. For others... Well, we don't all want to get bent over in the bushes for some cash."
            pc "Hmmm... Thanks."
            simon.name "No problem."
        else:
            pc "I'm not a whore."
            if simon.sold:
                simon.name "Fucked me for money so close enough."
            else:
                simon.name "Fucked [bob.name] for some cash. So close enough."
            pc "Well, that was a one off..."
            simon.name "Doesn't matter anyway. Girls at the highway stick together. They won't say anything to you unless you are a whore like they are."
            simon.name "So go to the highway, hook a few punters, chat to the girls and they will open up to you."
            pc "No other way?"
            simon.name "Could pay a whore to do the work for you. No grantee they will actually do the work though."
            simon.name "Every time I have tried, they string me along with just enough to get me to keep paying them. Always amounts to nothing in the end."
            simon.name "You though. Don't seem to have an issue with sex for money. So you can be the whore."
            pc "Right..."
            pc "Thanks..."
    else:
        simon.name "Tried it a bunch myself. Doesn't work out even if you pay them."
        pc "No?"
        simon.name "They stick together. Anyone around that way asking questions is usually bad news for the whores."
        simon.name "So even if it seems to have nothing to do with them, they will keep quiet."
        simon.name "Tried paying them for info or to look around for me before. They just kept stringing me along to keep getting paid but no results in the end."
        pc "Right. So any ideas?"
        simon.name "Not one you would like."
        pc "Well, I'll decide that."
        simon.name "Go be a whore. Dress up, hang out the highway, sell your arse a bit then try asking about. They would be more open to you then."
        pc "Terrible idea. Any others?"
        simon.name "If I had other ideas I would have used them by now."
        simon.name "Getting fucked on the highway isn't something most people would do, so even security struggle making inroads with the whores."
        simon.name "Only other way I can think of is find some addict whore and pay them with drugs. I would bet all my money that will end badly though."
        simon.name "You will end up a corpse in an alleyway before you get any valuable info."
        pc "So bending over is the only option."
        simon.name "Or just giving up on the whole thing."
        pc "Thanks..."
    pc "I'll have a think on it."
    simon.name "Right. Well, have fun with that."
    hide simon with dissolve
    $ walk(loc_revel_backstreet)
    if player.has_perk(perk_gamine) or quest_whore.active:
        pcm "As expected, no way around it. They won't talk unless you are one of them. One of us? Whatever..."
    else:
        pcm "So, they know their own..."
    if player.has_perk(perk_gamine) or quest_whore.active:
        pcm "Not a shock really. Whores stick together. Anyone you haven't seen taking a dick could be undercover. Least that's how it used to be."
    else:
        pcm "So, being a whore is one option... A terrible option..."
        pcm "Not managing to find out anything else though."
    pcm "Ugh..."
    $ log.markdone("mira_missing_05")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
