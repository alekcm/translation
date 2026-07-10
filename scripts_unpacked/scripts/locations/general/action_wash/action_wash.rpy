label action_wash:
    if loc([loc_bedroom_dani]):
        if dani_here():
            pc "Hope you don't mind me washing up."
            dani.name "Sure, go ahead."
    else:
        $ player.face_worried
        pcm "Should really wash up somewhere more private..."
    $ pc_striptease()
    $ player.add_desire(If(player.has_perk(perk_exhibitionist), 25, 10))
    $ player.add_mood(-5)
    $ player.wash()
    "I quickly wash my body down with some warm water and hand soap and use some paper towels to pat myself dry."
    $ player.face_normal()
    if not weightgen(4000, danger_weight()):
        pc "That should do until I can have a show..."
        jump random_event_generic_danger_1
    pc "That should do until I can have a shower."
    $ pc_dress_slow()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
