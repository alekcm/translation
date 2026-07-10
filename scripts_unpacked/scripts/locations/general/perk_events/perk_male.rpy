label former_male_first_handjob:

    pcm "Not like I wasn't used to having a cock in my hand in my previous life."
    pcm "But it was at least my cock."
    pcm "Feel kind of weird having someone else's in my hand. Oddly enough it doesn't feel bad."
    pcm "And a lot warmer than I thought it would be."
    return

label former_male_first_blowjob:
    $ player.face_confused()
    pcm "Can't believe I am taking his cock in my mouth..."
    pcm "Having someone do this to me was something I would never refuse. But now it's me blowing some guy."
    pcm "..."
    pcm "Hope I do it right."
    return

label former_male_first_vagsex:
    pcm "Haa... I am losing my virginity as a girl..."
    pcm "It hurts, but not as much as I thought it would."
    pcm "Relax. Relax. That's right. Don't tense up..."
    return

label former_male_first_asssex:
    $ player.face_grit()
    pcm "Fuck. Never really expected I would be letting a man put his cock up my arse..."
    pcm "This body is making me do things I never thought I would..."
    pcm "Not just do, but actually enjoy."
    pcm "Well, I would enjoy if this wasn't so fucking painful!"
    return

label perk_male_first_swallow:
    $ player.face_shock()
    pcm "He came in my mouth!?"
    pcm "What do I do?"
    pcm "Swallow it?"
    pcm "Isn't that what I would have wanted?"
    return

label perk_male_first_facial:
    $ player.face_shock()
    pcm "Errr... All over my face?"
    pcm "Now this is something I never thought I would have done to me."
    pcm "What happened to me? Wasn't long ago I was a man and now I am in a girls body, on my knees with cum all over my face..."
    $ player.face_normal()
    return

label perk_male_first_creampie:
    pcm "Errr... Maybe I should stop him...?"
    pcm "Wasn't thinking at the time. But actually this could be dangerous."
    pcm "Got to get used to being a girl and not let some guy get me pregnant."
    pcm "Can this body get pregnant?"
    return

label perk_male_first_analcreampie:
    pcm "First getting ass fucked and now I have him cumming in me."
    pcm "I know I could have done this as a guy, but for some reason it still feels different."
    pcm "Well, at least I won't get pregnant from him putting it here..."
    return

label perk_male_first_assault:
    pcm "Shit shit!"
    pcm "[emile.name] did warn me things had changed. But fuck!"
    pcm "He is really pushing things..."
    return

label perk_male_first_rape:
    pcm "Fuck shit fuck!"
    pcm "Rapist piece of shit!"
    pcm "If I had my old male body I would kill this fucker!"
    return

label perk_male_first_selloffer:
    $ player.face_shock()
    pcm "Errr. Fuck!"
    if player.soldrequest == "strip":
        pcm "I used to be a man and now I have some guy offering to pay me to take my clothes off?"
    elif player.soldrequest in ["oral", "blow"]:
        pcm "I used to be a man and now I have some guy offering to pay me to suck him off?"
    elif player.soldrequest == "anal":
        pcm "I used to be a man and now I have some guy offering to pay me to fuck me in the ass?"
    else:
        pcm "I used to be a man and now I have some guy offering to pay me for sex?"
    pcm "I know the world has changed. But really?"
    if player.check_poor():
        pcm "Worst part is, I'm broke..."
    $ player.face_normal()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
