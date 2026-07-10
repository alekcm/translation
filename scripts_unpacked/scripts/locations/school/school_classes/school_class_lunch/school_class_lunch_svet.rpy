label school_class_lunch_svet:
    $ rand_choice = WeightedChoice([
    ("school_class_lunch_svet_1", 100),
    ("school_class_lunch_svet_2", 100),
    ("school_class_lunch_svet_3", 100),
    ("school_class_lunch_svet_4", 100),
    
    
    
    
    
    
    ("school_class_lunch_svet_11", If(drake.setname in rachel.conversation_topics and not "told_sex_" + drake.setname in rachel.conversation_topics,300,0)),
    ("school_class_lunch_svet_12", If(nate.setname in rachel.conversation_topics and not "told_sex_" + nate.setname in rachel.conversation_topics,300,0)),
    ("school_class_lunch_svet_13", If(dan.setname in rachel.conversation_topics and not "told_sex_" + dan.setname in rachel.conversation_topics,300,0)),
    
    ("school_class_lunch_svet_15", If(any(item in ["pregnant_" + drake.setname, "pregnant_" + nate.setname, "pregnant_" + dan.setname] for item in rachel.conversation_topics), 1000, 0)),
    ])
    jump expression rand_choice

label school_class_lunch_svet_1:
    show svet at right with dissolve
    svet.name "Hey [name]. Hope you're keeping up with your training."
    pc "Yeah, when I can."
    svet.name "Glad to hear it."
    jump school_class_lunch_end

label school_class_lunch_svet_2:
    show svet at right
    show rachel happy at right2
    with dissolve
    rachel.name "...and then it was all over the place. I have no idea how it happened but it was so~~ funny."
    rachel.name "Hey [name]."
    pc "Hey."
    show rachel angry
    rachel.name "But did mean afterwards we had to clean it all up. That wasn't fun at all."
    svet.name "Serves you right."
    rachel.name "Boooo!"
    jump school_class_lunch_end

label school_class_lunch_svet_3:
    show svet at right
    show rachel happy at right2
    with dissolve
    rachel.name "...about this liquid that if you put it on your skin, you will stay looking younger."
    svet.name "And he told you drinking it is better?"
    rachel.name "Ah you know about it?"
    svet.name "*Sigh*"
    svet.name "You wanna tell her [name]?"
    if player.int <= 20:
        pc "Tell what? If you drink it, it makes you younger?"
        rachel.name "Yeah so he told me. We should go get some."
        svet.name "Ugh!"
    else:
        pc "But his has a special version where you just close your eyes and he will apply it directly?"
        show svet happy
        svet.name "Haha!"
        rachel.name "Huh, he does?"
    jump school_class_lunch_end

label school_class_lunch_svet_4:
    show rachel at right1 with dissolve
    pc "Hey."
    rachel.name "So I was thinking. If you put two of them together, what do you think will happen?"
    pc "Two of what?"
    rachel.name "Not what silly, who."
    pc "Ok, so two of who?"
    rachel.name "Two of them."
    pc "Who are them?"
    rachel.name "I don't know. I guess it could be anyone."
    pc "Okaaay. So put two people together and... What?"
    rachel.name "That's what I was asking you. I don't know."
    pc "Ok... A mystery..."
    jump school_class_lunch_end





































label school_class_lunch_svet_11:
    show rachel at right1 with dissolve
    rachel.name "Soooo..."
    if "told_sex_" + rachel._original_name in drake.conversation_topics:
        pc "Something to tell me?"
        rachel.name "Oh?"
        if player.isslut:
            pc "I heard a story about one of my friends fucking a dirty little slut."
        else:
            pc "Someone has been having fun."
        rachel.name "Ahh he told you?"
        $ player.face_happy()
        pc "Of course."
        rachel.name "Hah."
    elif player.isslut:
        show rachel at right6 with dissolve
        rachel.name "I flirted with that boy you like fucking."
        pc "Err, what one?"
        rachel.name "The blondie. [drake.name]."
        pc "Ah, you fucking him now too?"
        rachel.name "Yeah. Cant let you hog all the fun."
    else:
        rachel.name "So I have been chatting to that boy you hang out with."
        pc "Err, what one?"
        rachel.name "The blondie. [drake.name]."
        pc "Ok?"
        rachel.name "Err, nothing..."
    $ remove_from_list(rachel.conversation_topics, drake.name)
    $ add_to_list(rachel.conversation_topics, "told_sex_" + drake.name)
    jump school_class_lunch_end

label school_class_lunch_svet_12:
    show rachel at right1 with dissolve
    rachel.name "Soooo..."
    if "told_sex_" + rachel._original_name in nate.conversation_topics:
        pc "Something to tell me?"
        rachel.name "Oh?"
        if player.isslut:
            pc "I heard a story about one of my friends fucking a dirty little slut."
        else:
            pc "Someone has been having fun."
        rachel.name "Ahh he told you?"
        $ player.face_happy()
        pc "Of course."
        rachel.name "Hah."
    elif player.isslut:
        show rachel at right6 with dissolve
        rachel.name "I flirted with that boy you like fucking."
        pc "Err, what one?"
        rachel.name "The pretty boy. [nate.name]."
        pc "Ah, careful with that one. He's a dirty pervert."
        rachel.name "That a bad thing?"
        pc "Well, no. I guess not."
    else:
        rachel.name "So I have been chatting to that boy you hang out with."
        pc "Err, what one?"
        rachel.name "The pretty boy. [nate.name]."
        pc "Two perverts chatting. Only one way that ends."
        rachel.name "Ha, right?"
    $ remove_from_list(rachel.conversation_topics, nate.name)
    $ add_to_list(rachel.conversation_topics, "told_sex_" + nate.name)
    jump school_class_lunch_end

label school_class_lunch_svet_13:
    show rachel at right1 with dissolve
    rachel.name "I started talking to that [dan.name] that you like hanging out with."
    pc "Oh? He can be a bit difficult to talk to. Doesn't say a lot."
    rachel.name "Oh? So wasn't just me then."
    if player.isslut:
        pc "Na, someone like his it's better to just tell him what you want and not play the usual games."
        rachel.name "Ah really?"
        pc "You want to fuck him I guess?"
        rachel.name "Well, we fooled about but dunno about him."
        pc "Just tell him to fuck you then all good."
        show rachel happy
        rachel.name "Okay~"
    else:
        pc "So? What you been chatting about?"
        show rachel happy
        rachel.name "Well, was less chatting and more..."
        pc "Okay okay..."
    $ remove_from_list(rachel.conversation_topics, dan.name)
    $ add_to_list(rachel.conversation_topics, "told_sex_" + dan.name)
    jump school_class_lunch_end

label school_class_lunch_svet_15:
    show rachel at right1 with dissolve
    rachel.name "So..."
    show rachel worried
    rachel.name "..."
    pc "Err. What's the problem"
    rachel.name "Maybe you can help me with telling the father I am preggo."
    pc "Do I know who it is?"
    show rachel neutral
    rachel.name "It's [rachel.pregnant_who.name]'s baby."
    $ player.face_shock()
    pc "Oooooohhh..."
    if player.preg_knows and player.preg_father_class == rachel.pregnant_who:
        $ player.face_angry()
        pc "That bastard."
        rachel.name "What?"
        pc "Who you think knocked me up?"
        show rachel happy
        rachel.name "Really? Hahahha. Lucky shit."
        pc "Hrmf!"
    else:
        $ player.face_neutral()
        pc "Yeah sure. I'll have a chat with him."
        rachel.name "Thanks."
    $ remove_from_list(rachel.conversation_topics, "pregnant_" + rachel.pregnant_who._original_name)
    $ add_to_list(rachel.pregnant_who.conversation_topics, "pregnant_" + rachel._original_name)
    jump school_class_lunch_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
