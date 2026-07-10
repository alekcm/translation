label action_exercise_vball_normal:
    jump expression WeightedChoice([
    ("action_exercise_vball_normal_1", 100),
    ("action_exercise_vball_normal_2", If (weather_var == 1, 100, 0)),
    ("action_exercise_vball_normal_3", 100),
    ("action_exercise_vball_normal_4", 100),
    ("action_exercise_vball_normal_5", 100),
    ("action_exercise_vball_normal_6", 100),
    ("action_exercise_vball_normal_7", 100),
    ])

label action_exercise_vball_normal_1:
    $ player.face_happy()
    pc "This is nice."
    jump action_exercise_vball_end

label action_exercise_vball_normal_2:
    $ player.face_happy()
    pc "Uff, such lovely weather to be playing."
    jump action_exercise_vball_end

label action_exercise_vball_normal_3:
    "There is a lovely breeze keeping me cool as I play with the girls"
    jump action_exercise_vball_end

label action_exercise_vball_normal_4:
    pc "Go go! Yes!"
    jump action_exercise_vball_end

label action_exercise_vball_normal_5:
    pc "Damn! Nice shot."
    jump action_exercise_vball_end

label action_exercise_vball_normal_6:
    "As we are playing, I notice the boys watching us."
    pcm "Perverts."
    jump action_exercise_vball_end

label action_exercise_vball_normal_7:
    "As I am playing, I end up getting sand in my eye and I have to stop and try and get it out."
    $ player.eye = 3
    pc "Ugh!"
    jump action_exercise_vball_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
