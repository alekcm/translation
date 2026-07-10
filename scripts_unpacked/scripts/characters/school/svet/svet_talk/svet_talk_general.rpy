

label svet_talk_subject:
    jump expression WeightedChoice([

    ("svet_talk_general_1", 100),
    ("svet_talk_general_2", 100),
    ("svet_talk_general_3", 100),
    
    
    
    
    
    
    
    ])





label svet_talk_general_1:
    svet.name "How you keeping [name]?"
    pc "Going good."
    svet.name "Good to hear."
    jump svet_talk_end

label svet_talk_general_2:
    svet.name "Keeping up the dancing I hope?"
    if player.pregnancy >= 2:
        pc "Trying, not easy with this belly."
        svet.name "Yeah, I can imagine."
    else:
        pc "When I can. Gotta earn some money as well."
        svet.name "Yeah, don't I know it."
    jump svet_talk_end

label svet_talk_general_3:
    svet.name "Keeping up the dancing I hope?"
    if player.pregnancy >= 2:
        pc "Trying, not easy with this belly."
        svet.name "Yeah, I can imagine."
    else:
        pc "When I can. Gotta earn some money as well."
        svet.name "Yeah, don't I know it."
    jump svet_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
