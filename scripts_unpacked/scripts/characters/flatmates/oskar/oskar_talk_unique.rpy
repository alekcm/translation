label oskar_talk_meet_house:
    show oskar at right1 with dissolve
    oskar.name "[fname] isn't it?"
    pc "Err, yeah. You are?"
    oskar.name "[oskar.fname] [oskar.sname]. I own this place you are living."
    pc "Ah, hi."
    oskar.name "Just here to inform you that some of your rent has already been prepaid by whoever set this up for you."
    pc "Ah, that's good."
    oskar.name "Mmm. You have until the 16th to come see me again. I'll probably see you around, but if not you can come to my office and settle things up."
    oskar.name "For now the amount is $[rent_amount] per week."
    pc "For now?"
    oskar.name "Things are changing in [town] every day. That price is also with the academy offsetting much of the cost so won't find any better out there."
    pc "Okay. Where is your office?"
    oskar.name "Downstairs at the entrance. Hard to miss."
    pc "Right. Thanks."
    hide oskar with dissolve
    pcm "That's the guy [emile.name] was telling me about. Told me I shouldn't miss payments or I'll be in trouble."
    pcm "..."
    $ quest_rent.activate()
    $ log.assign("Paying rent")
    jump travel

label oskar_talk_meet_office:
    if not log.interactive("quest_rent_a"):
        pc "Hi. I'm looking for [oskar.name]. Is that you?"
        show oskar at right1 with dissolve
        oskar.name "That's right. And you are?"
        pc "[name]... Err, [fname] [sname]. I live in your house."
        oskar.name "Ah yes. [emile.name]'s sister. I remember. What can I do for you?"
        pc "[emile.name] said I should come chat with you about how much I should pay."
        oskar.name "Your first two weeks were paid up. From there you need to pay £[rent_amount] a week."
        pc "Right. Should I stop by here to pay or...?"
        oskar.name "If you want to pay early you can. If not I will come by on Sunday and collect from everyone."
        pc "Right. Ok. Thanks."
        hide oskar with dissolve
        $ quest_rent.activate()
        $ log.assign("Paying rent")
        $ diary_rent = Diary_Class("Paying rent", "I visited my landlord today and had a chat with him. I need to pay him every Sunday. \n" + emile.fname + " told me if I don't pay, I will put to work for him.\n\n She seemed to imply it was a pretty bad thing.")
    else:

        pcm "Hmm, expected this place to be a bit more fancy."
        show oskar at right1 with dissolve
        oskar.name "[fname] isn't it? Can I help you?"
        pc "Ah, no. I just came to make sure I know where to pay."
        oskar.name "You're in the right place."
        hide oskar with dissolve
        pcm "Right..."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
