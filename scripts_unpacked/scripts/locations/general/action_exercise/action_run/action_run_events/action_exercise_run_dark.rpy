label action_exercise_run_dark:
    jump expression WeightedChoice([
    ("action_exercise_run_dark_1", 100),
    ("action_exercise_run_dark_2", 100),
    ("action_exercise_run_dark_3", 100),
    ("action_exercise_run_dark_4", 100),
    ("action_exercise_run_dark_5", 100),
    ("action_exercise_run_dark_6", 100),
    ("action_exercise_run_dark_7", 100),
    ("action_exercise_run_dark_8", 100),
    ])

label action_exercise_run_dark_1:
    "As I am running I almost trip over my untied laces."
    pcm "Ah fuck."
    "While bending over to tie them..."
    $ player.spank()
    guy "Sexy ass!"
    $ player.face_annoyed()
    pc "Cunt!"
    jump action_exercise_run_end

label action_exercise_run_dark_2:
    "As I am running I pass a group of guys hanging around."
    pcm "..."
    pcm "Nothing?"
    pcm "Good."
    jump action_exercise_run_end

label action_exercise_run_dark_3:
    "As I am running, a strange man seems to be purposely moving into my path. I have to slow down to pass and still almost bump him."
    $ player.face_worried()
    pc "Creepy..."
    $ player.add_mood(-3)
    jump action_exercise_run_end

label action_exercise_run_dark_4:
    pcm "The lights from be buildings shining through the trees look so beautiful. Almost looks like stars."
    $ player.mouth = 4
    pc "So pretty..."
    $ player.add_mood(3)
    jump action_exercise_run_end

label action_exercise_run_dark_5:
    pcm "The park is so peaceful at night. Would actually be nice to relax here more if I knew there weren't perverts hiding in the bushes."
    $ player.add_mood(3)
    jump action_exercise_run_end

label action_exercise_run_dark_6:
    "As I am running I can feel the cool night breeze on my skin."
    pc "Ahhhh..."
    $ player.add_mood(3)
    jump action_exercise_run_end

label action_exercise_run_dark_7:
    $ player.brow = 3
    "As I am running I notice a small animal in the dark heading straight for me."
    $ player.face_worried()
    pcm "The fuck is that?"
    pcm "..."
    pcm "Maybe I should go..."
    pcm "Damn, just a plastic bag blowing in the wind. Scared the life out of me!"
    $ player.add_mood(-2)
    jump action_exercise_run_end

label action_exercise_run_dark_8:
    guy "No need for all this running [rlist.name_deg]. Come to my place and I'll give you a workout."
    pcm "..."
    $ player.add_mood(-2)
    jump action_exercise_run_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
