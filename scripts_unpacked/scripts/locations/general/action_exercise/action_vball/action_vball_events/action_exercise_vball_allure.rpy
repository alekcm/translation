label action_exercise_vball_allure:
    jump expression WeightedChoice([
    ("action_exercise_vball_allure_1", 100),
    ("action_exercise_vball_allure_2", 100),
    ("action_exercise_vball_allure_3", 100),
    ])

label action_exercise_vball_allure_1:

    guy "Nice ass babe, come back round here so I can get a better look."
    $ player.face_shy()
    pc "..."
    jump action_exercise_vball_end

label action_exercise_vball_allure_2:
    guy "Keep bouncing those tits baby!"
    $ player.face_shy()
    pc "..."
    jump action_exercise_vball_end

label action_exercise_vball_allure_3:
    guy "Hey sexy. Nice arse!"
    $ player.face_shy()
    jump action_exercise_vball_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
