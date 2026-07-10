label anabel_talk_subject:
    if not renpy.showing("anabel"):

        show anabel at right1 with dissolve
    jump expression WeightedChoice([
    
    
    ("anabel_talk_general_1", 100),
    ("anabel_talk_general_2", 100),
    ("anabel_talk_general_3", 100),
    ("anabel_talk_general_4", 100),
    

    
    
    
    

    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    

    ])





label anabel_talk_general_1:
    anabel.name "You doing okay?"
    pc "Same as always."
    anabel.name "Good. Stay safe."
    jump anabel_talk_end

label anabel_talk_general_2:
    anabel.name "Did you dance before?"
    pc "Not really. I didn't even know I got signed up until I arrived here."
    anabel.name "Well, not too many clubs to sign up to anyway."
    pc "Yeah, not sure I have seen any others at all."
    jump anabel_talk_end

label anabel_talk_general_3:
    anabel.name "Been getting up to anything?"
    pc "Not really. Same as always."
    anabel.name "That's probably a good thing."
    pc "We will see."
    jump anabel_talk_end

label anabel_talk_general_4:
    anabel.name "Hope you are keeping safe."
    pc "Yeah, as much as I can anyway."
    anabel.name "Ugh."
    jump anabel_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
