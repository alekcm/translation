



label school_class_gym_run:
    pcm "Track 'n' field today."
    $ pc_dress_event("sport", loc_school_locker_girls, loc_school_field)
    $ player.face_exercise()
    if player.isfat == True:
        jump expression renpy.random.choice([
        "school_class_gym_runfat1",
        "school_class_gym_runfat2",
        "school_class_gym_runfat3",
        "school_class_gym_runfat4",
        "school_class_gym_runfat5"
        ])
    else:
        jump expression renpy.random.choice([
        "school_class_gym_run1",
        "school_class_gym_run2",
        "school_class_gym_run3",
        "school_class_gym_run4",
        "school_class_gym_run5",
        "school_class_gym_run6"
        ])

label school_class_gym_runfat1:
    pc "Damn [tucker.sname]. Go to school he said, it will be fun he said."
    pc "Gives me this fat body then makes me run my arse off while I cough up a lung."
    jump school_class_gym_end

label school_class_gym_runfat2:
    pc "Ugh, this might not be so bad if it weren't for the boys watching. They better not be laughing at me."
    jump school_class_gym_end

label school_class_gym_runfat3:
    mason.name "Keep going [sname], work up a sweat and shed that extra weight!"
    pc "Grrr. I'm going I'm going."
    jump school_class_gym_end

label school_class_gym_runfat4:
    pc "Kill me please. This is torture. Let me die here in peace."
    jump school_class_gym_end

label school_class_gym_runfat5:
    pc "I know I need to lose some weight, but damn there must be an easier way to go about this."
    mason.name "No slacking [sname]. Get those legs moving!"
    jump school_class_gym_end

label school_class_gym_run1:
    mason.name "Keep it up ladies! Only three more laps left then you can have a rest."
    pc "Uff, uff, uffff"
    jump school_class_gym_end

label school_class_gym_run2:
    mira.name "Come on [name], keep up or [mason.name] will eat you out!"
    $ player.mouth = 2
    pc "What? Eat me o..."
    mira.name "Chew! Chew! Chew you out!"
    $ player.mouth = 3
    pc "Hahaha"
    jump school_class_gym_end

label school_class_gym_run3:
    cass.name "Ufff, ufff, uuff."
    cass.name "Go on without me... I will take the noble sacrifice."
    jump school_class_gym_end

label school_class_gym_run4:
    pc "Keep going keep going. Don't let the boys laugh at you for being so slow."
    jump school_class_gym_end

label school_class_gym_run5:
    if player.male_origin:
        pc "Uff, it's not something I even considered in my previous life. But running is a fair bit harder with a chest like this."
    else:
        pc "I don't remember having a bouncing issue in my previous body. Were my breasts a lot smaller then?"
    jump school_class_gym_end

label school_class_gym_run6:
    pc "Keep going. This is for my own good. Uff. Keep going..."
    jump school_class_gym_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
