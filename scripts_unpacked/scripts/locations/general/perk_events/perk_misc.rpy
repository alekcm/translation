label broodmother_sudden_lactation:
    $ player.cover_breasts_force()
    $ player.face_meek()
    $ player.add_perk(perk_lactating, notif=True)
    $ perk_lactating.dict["milk_amount"] = 20
    $ perk_lactating_buildup()
    pcm "I thought my breasts were feeling funny..."
    pcm "Is my body supposed to just start leaking milk like this?"
    pcm "Oh well..."
    $ player.uncover()
    $ player.face_normal()
    jump travel

label pregnancy_want_or_not_choice_first:
    $ add_to_list(player.list, "asked_preg_want")
    pcm "Hmmm, learning a bit about this world and how things are, looks like protection is hard to come by."
    pcm "How do I want to play things? I could just leave it to chance or I could make steps to get what I want."
    jump pregnancy_want_or_not_choice_menu

label pregnancy_want_or_not_choice_repeat:
    $ add_to_list(player.list, "asked_preg_want")
    pcm "Now that all that is over with, do I want to have another baby?"
    pcm "How do I want to play things? I could just leave it to chance or I could make steps to get what I want."
    jump pregnancy_want_or_not_choice_menu

label pregnancy_want_or_not_choice_menu:
    if player.has_perk(perk_broodmother, notif=True):
        pcm "Who am I kidding? Of course I want to get pregnant."
        $ player.add_perk(perk_preg_want, notif=True)
        jump travel
    elif player.has_perk([perk_meek, perk_broken], notif=True):
        pcm "Who am I kidding, as if anyone is going to listen to what I want."
        jump travel
    elif player.has_perk([perk_deadinside], notif=True):
        pcm "Ugh, why even ask myself that? Of course I don't want to end up pregnant."
        $ player.add_perk(perk_preg_notwant, notif=True)
        jump travel
    menu:
        "Try and get pregnant":
            pcm "Getting pregnant it is. I wonder how long it will take?"
            $ player.add_perk(perk_preg_want, notif=True)
        "Leave it to chance":
            pcm "Whatever, if it happens or doesn't. I don't care."
        "Avoid pregnancy as much as I can":
            pcm "I shouldn't take risks. I'll see if I can manage to stay baby free."
            $ player.add_perk(perk_preg_notwant, notif=True)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
