label bathroom_enter_occupied:
    $ player.face_worried()

    if robin_here():
        if robin.sex_les:
            pc "Oops, sorry. Hope you don't mind."
            robin.name "Sure, not like you haven't seen it all already."
        elif robin.love > 60:
            pc "Oops, sorry. Hope you don't mind."
            robin.name "No problem."
        else:
            pc "Err, sorry..."
            $ walk(loc_bedroom)
    elif emile_here():
        if emile.love < 40:
            if player.has_perk(perk_male):
                pc "Err, sorry..."
                emile.name "Pervert brother."
            else:
                pc "Err, sorry..."
            $ walk(loc_bedroom)
        else:
            pc "Oops, sorry. Hope you don't mind."
            emile.name "No worries."
    $ player.face_normal()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
