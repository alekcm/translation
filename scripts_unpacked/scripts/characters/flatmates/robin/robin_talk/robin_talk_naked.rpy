label robin_talk_naked_picker:
    show robin at right1 with dissolve

    jump expression WeightedChoice([
        
    ("robin_talk_naked_" + str(robin.dict["robin_naked_talk"]), 20),     
    ])

label robin_talk_naked_0:
    $ robin.dict["robin_naked_talk"] += 1
    robin.name "Err, you aware you are showing your bit's off?"
    pc "Yeah..."
    robin.name "Right. Okay then."
    pc "..."
    jump robin_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
