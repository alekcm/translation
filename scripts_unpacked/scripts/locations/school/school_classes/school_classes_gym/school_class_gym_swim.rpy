



label school_class_gym_swim:
    pcm "Swimming class today."
    $ pc_dress_event("swim", loc_school_locker_girls, loc_school_pool)
    jump expression renpy.random.choice([
    "school_class_gym_swim1",
    "school_class_gym_swim2",
    "school_class_gym_swim3",
    "school_class_gym_swim4",
    "school_class_gym_swim5",
    "school_class_gym_swim6"
    ])


label school_class_gym_swim1:
    "You spend the lesson doing 25m laps."
    jump school_class_gym_end

label school_class_gym_swim2:
    pc "I don't remember ever being asked if I could swim. Good job I learned this stuff as a child and it's not really something you forget."
    pc "I picked it back up quite easily in this new body."
    jump school_class_gym_end

label school_class_gym_swim3:
    pc "Butterfly? Ugh, I always hated butterfly..."
    jump school_class_gym_end

label school_class_gym_swim4:
    "You see a commotion off near the changing rooms while swimming."
    pc "Whats going on over there?"
    show cass swim at right1
    cass.name "What do you think? Some boys probably tried to sneak in and watch us swimming."
    pc "Ah..."
    hide cass
    jump school_class_gym_end

label school_class_gym_swim5:
    $ player.mouth = 4
    $ player.brow = 3
    "Someone sneaks up behind you and pulls up your swimsuit giving you a wedgie."
    $ player.face_angry()
    pc "Ah fuck that hurts!"
    pc "Bitch!"
    jump school_class_gym_end

label school_class_gym_swim6:
    $ player.eye = 3
    $ player.mouth = 1
    pc "Backstroke, so relaxing. It's like laying down on the water as if it's a bed. I could easily fall asleep."
    jump school_class_gym_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
