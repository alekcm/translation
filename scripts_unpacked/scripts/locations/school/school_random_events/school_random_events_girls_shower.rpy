label random_event_school_girls_shower:
    $ rand_choice = WeightedChoice([
    ("random_event_school_girls_shower_noevent", 15),
    ("random_event_school_girls_shower_1", 1),
    ("random_event_school_girls_shower_2", 1),
    ("random_event_school_girls_shower_3", 1),
    ("random_event_school_girls_shower_4", 1),
    ("random_event_school_girls_shower_5", 1), 
    ("random_event_school_girls_shower_6", 1),
    
    
    
    ])
    jump expression rand_choice

label random_event_school_girls_shower_noevent:
    "I have a shower."
    return
label random_event_school_girls_shower_1:
    $ player.face_worried()
    girl "Haaaaaaaa!!! ♥"
    pcm "Oh?"
    girl "*Huff* *Huff* *Huff*"
    pcm "Well, good for you..."
    return

label random_event_school_girls_shower_2:
    girl1 "What are you looking at?"
    girl2 "Ah nothing. Sorry."
    girl1 "Better be sorry. Don't need that kind of shit in here as well!"
    return

label random_event_school_girls_shower_3:
    girl1 "Ahhhhh!"
    girl2 "You ok?"
    girl1 "Yeah... I'm fine. Wait don't look!"
    girl2 "What the fuck is that?"
    girl1 "I told you not to..."
    girl2 "It's huge!"
    girl1 "Shhhhhhhhhh!"
    return

label random_event_school_girls_shower_4:
    girl "Ahhhhh! Fucking freezing!"
    girl "I hate this place!"
    return

label random_event_school_girls_shower_5:
    girl1 "What are you looking at?"
    girl2 "Err... Have you taken a test?"
    girl1 "..."
    girl2 "I think you might have to..."
    girl1 "*SOB* I know..."
    return

label random_event_school_girls_shower_6:
    girl1 "How did you end up with those bruises?"
    girl2 "Ugh. Don't ask"
    girl1 "Looks kinda rough."
    girl2 "Yeah..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
