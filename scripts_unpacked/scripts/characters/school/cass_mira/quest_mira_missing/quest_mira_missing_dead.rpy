label quest_mira_missing_dead_discover:
    $ mira.kill()
    $ mira.dead_message = "I found her washed up on the beach after having gone missing for a while."
    pcm "Hmm, why are people gathering over there?"
    pc "What's going on?"
    show zahra at right1 with dissolve
    zahra.name "Someone washed up on the beach?"
    pc "Junkie?"
    zahra.name "Na, whore probably. Was a girl."
    $ player.face_worried()
    pc "Oh?"
    hide zahra with dissolve
    "I poke my way through the crowd to have a look out of morbid curiosity."
    show mira_washup at right2 with dissolve
    pc "..."
    $ player.add_mood(-200)
    $ player.add_conf(-20)
    pcm "Fuck! That looks like [mira.name]..."
    pcm "Fuck!"
    pcm "It is [mira.name]..."
    pcm "Fuck fuck fuck!!!"
    hide mira_washup
    hide mira_washup_cen
    show police_gen at right1
    with dissolve
    police1.name "Alright, move along. We've got it from here."
    police1.name "Come on, out the way!"
    hide police_gen
    $ walk(loc_beach_locker_girls)
    $ walk(loc_beach_locker_girls_stall)
    $ player.face_worried()
    pcm "Fuck, that was [mira.name]!"
    pcm "How the fuck did that happen?"
    $ player.face_cry()
    pcm "How..."
    pcm "No..."
    pcm "This is horrible..."
    $ player.face_wail()
    pcm "And [cass.name], she will be devastated..."
    "I stay in the stall for who knows how long crying and trying to compose myself."
    $ relax(40)
    pcm "..."
    pcm "Right..."
    pcm "I'm going to have to tell [cass.name] about this..."
    $ add_to_list(quest_mira_missing.list, "dead_beach")
    if quest_mira_missing.isactive():
        $ log.fail_quest("mira_missing_10")
    jump travel

label quest_mira_missing_dead_tellcass:
    show cass at right1 with dissolve
    if "dead_beach" in quest_mira_missing.list:
        pc "Err... [cass.nname]. I have some news."
        cass.name "About [mira.name]?"
        pc "It's not good..."
        show cass worried
        cass.name "What? Tell me."
        pc "I was at the beach and security found her."
        cass.name "Found her? Where is she?"
        pc "She was... Not alive..."
        cass.name "What???"
        show cass cry
        cass.name "No no no no no!"
        cass.name "It couldn't have been her. It was someone else!"
        pc "I saw her... I'm sorry [cass.name]."
        cass.name "No! It wasn't her!"
    else:
        pc "Err... [cass.nname]..."
        pc "It's been quite a while since we have seen or heard anything from [mira.name]."
        show cass worried
        cass.name "..."
        pc "I think it's about time we accepted what might have happened."
        cass.name "What???"
        show cass cry
        cass.name "No no no no no!"
        cass.name "I will find her!"
        cass.name "I wont accept it!!!"
    $ add_to_list(cass.list, "broken")
    hide cass with hpunch
    pc "..."
    pcm "I wish it wasn't her."
    jump travel

label quest_mira_missing_dead_assume:
    pcm "It's been so long since [mira.name] went missing and still no word of her."
    pcm "..."
    pcm "I think it's safe to assume at this point we aren't going to see her again..."
    pcm "Fuck..."
    $ mira.kill()
    $ mira.dead_message = "She went missing one day and was never seen again."
    $ add_to_list(quest_mira_missing.list, "dead_assume")
    if quest_mira_missing.isactive():
        $ log.fail_quest("mira_missing_10")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
