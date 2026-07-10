label world_late_trigger:
    if player.confidence >= 50:
        $ player.brow = 3
        pc "I feel more confident being out late at night, but it's still dangerous. I wonder if I should head home?"
        $ player.face_normal()
        $ late_final_warning = True

        jump travel
    else:
        pc "It's far too late for me to be staying out, I really need to go home."
        "***DEV NOTE***"
        "Previously this event moved you straight home. It will change."
        "In future it will allow you to stay out, but Sammy will trigger low confidence events where she is scared and lose mood."
        "If you want to go home, it will have to be done manually instead of the event jumping you straight there."
        "For now I will jump you home."
        $ walk(loc_stairwell)
        jump travel

label stairwell_late:
    if player.confidence >= 50:
        $ player.face_worried()
        pc "I feel more confident being out late at night, but it's still dangerous. I wonder if I should just stay at home?"
        $ player.face_normal()
        $ late_final_warning = True
    elif player.isbroken:
        $ player.face_worried()
        pc "Not very safe out there. But not like I haven't suffered worse..."
        $ player.face_normal()
        $ late_final_warning = True
    else:
        pc "It's too late for me to be going out now."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
