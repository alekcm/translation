



label school_class_gym_vball:
    pcm "It's volleyball today."
    $ pc_dress_event("sport", loc_school_locker_girls, loc_school_gym)
    jump expression renpy.random.choice([
    "school_class_gym_vball1",
    "school_class_gym_vball2",
    "school_class_gym_vball3",
    "school_class_gym_vball4",
    "school_class_gym_vball5",
    "school_class_gym_vball6",
    "school_class_gym_vball7",
    "school_class_gym_vball8"
    ])


label school_class_gym_vball1:
    pcm "All this warming up and practising moves. I want to play a match."
    jump school_class_gym_end

label school_class_gym_vball2:
    "After the warmup I am assigned to defending against my partner's attacks."
    pcm "Ugh, all I want to do is play a match, not block her shots."
    jump school_class_gym_end

label school_class_gym_vball3:
    "After the warmup we are split in teams for a match."
    $ player.face_happy()
    pc "A match? Yes!"
    pcm "This is so much fun!"
    jump school_class_gym_end

label school_class_gym_vball4:
    "Most of the lesson is spent doing movement exercises."
    pcm "Run left and stop. Right and stop. Left and stop..."
    jump school_class_gym_end

label school_class_gym_vball5:
    "After the warmup we are split in teams for a match."
    pc "C'mon girls! We are not gonna lose this match. Let's get 'em."
    "I play my hardest."
    $ randomnum = renpy.random.randint(1, 100)
    if randomnum > player.fitness:
        $ player.mouth = 8
        pc "Uff, ok... Next time we will show them."
    else:
        $ player.eye = 3
        $ player.mouth = 6
        pc "Yes! Good job girls. That was a good match"
    jump school_class_gym_end

label school_class_gym_vball6:
    "After the warmup we are split in teams for a match."
    pcm "A match? Finally."
    pcm "So much more fun than doing more running exercises."
    jump school_class_gym_end

label school_class_gym_vball7:
    "The lesson is spent doing jumping and landing exercises."
    pcm "Who would have thought so much work had to go into falling over without hurting yourself."
    jump school_class_gym_end

label school_class_gym_vball8:
    pc "All we did for the whole lesson is learn how to get up quickly."
    pcm "Who would have thought that getting up off your arse is a required skill in volleyball?"
    jump school_class_gym_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
