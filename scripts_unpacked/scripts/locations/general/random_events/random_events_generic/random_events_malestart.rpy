label random_event_generic_malestart:
    $ player.body_conf += 1
    jump expression WeightedChoice([
    ("random_event_generic_malestart_1", 100),
    ("random_event_generic_malestart_2", 100),
    ("random_event_generic_malestart_3", If (player.breasts > 1, 100, 0)),
    ("random_event_generic_malestart_4", player.allure),

    ])

label random_event_generic_malestart_remove:
    pcm "Hmmm..."
    pcm "Living in this body was really weird at first, but I almost forget that this wasn't the one I was born in."
    pcm "Been quite a while since I woke up in it."
    pcm "I wonder how things would have been if I had been born like this."
    pcm "Heh, that's an interesting thought. I wonder what I would have been like..."
    call screen perk_choice(perk_origin_list)
    $ player.remove_perk([perk_male, perk_preg_notwant, perk_preg_want])
    $ remove_from_list(player.list, "asked_preg_want")
    if player.origin_perk in [perk_nerd, perk_gym_bunny, perk_waif]:
        pcm "Not super exciting. But have to start somewhere."
    elif player.origin_perk == perk_bimbo:
        pcm "All the fun with none of the worry. Would be interesting."
    elif player.origin_perk == perk_gamine:
        pcm "Not the best type of life to have. But at least being wise to the world would keep me somewhat safe."
    elif player.origin_perk == perk_bambi:
        pcm "Would I be like that? People will no doubt see me as an easy target. Would be rough."
    elif player.origin_perk == perk_exhibitionist:
        pcm "Heh. Got a new sexy body so why not show it off? Could be interesting."
    elif player.origin_perk == perk_broodmother:
        pcm "A young, fit and healthy body would no doubt be able to give birth to strong and healthy kids."
    elif player.origin_perk == perk_wildcard:
        pcm "Maybe a little bit wild? Could be pretty fun."
    elif player.origin_perk == perk_party_girl:
        pcm "Why not have a little fun and go a bit crazy?"
    elif player.origin_perk == perk_meek:
        pcm "I know I have been in bad situations, but should I really embrace that?"
    elif player.origin_perk == perk_party_girl:
        pcm "Booze and fun times? Ha, yeah that sounds like something I would do."
    elif player.origin_perk == perk_deadinside:
        pcm "Not like this world has anything to be happy about."
    elif player.origin_perk == perk_addict:
        pcm "So much bad in the world, why would anyone want to go through it sober?"
    elif player.origin_perk == perk_princess:
        pcm "The world is at my feet. All the fun and no hard work."
    else:
        "No perk. This is a bug, please report."
    pcm "Well, might as well start living a real life in this body and not looking back to my old one."
    jump travel

label random_event_generic_malestart_1:
    pcm "Hmm, does it take me longer to walk with these smaller legs?"
    jump travel

label random_event_generic_malestart_2:
    pause 0.1
    with hpunch
    $ player.face_shock()
    pc "Ah!"
    pcm "Tripping over my feet in this new body..."
    jump travel

label random_event_generic_malestart_3:
    pcm "Gonna take me some time to get used to having breasts."
    pcm "Wear a bra and it digs into my sides, don't wear one and they jump about all over the place..."
    jump travel

label random_event_generic_malestart_4:
    pcm "Is it my imagination or do people look at me a lot more than they used to?"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
