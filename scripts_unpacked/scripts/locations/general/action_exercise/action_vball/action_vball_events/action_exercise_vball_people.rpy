label action_exercise_vball_people:
    jump expression WeightedChoice([
    ("action_exercise_vball_robin_1", If(robin_here() and image_showing("robin"), 100, 0)),
    ("action_exercise_vball_robin_2", If(robin_here() and image_showing("robin"), 100, 0)),

    ("action_exercise_vball_erika_1", If(erika_here() and image_showing("erika"), 100, 0)),
    ("action_exercise_vball_erika_2", If(erika_here() and image_showing("erika"), 100, 0)),
    

    ("action_exercise_vball_zahra_1", If(zahra_here() and image_showing("zahra"), 100, 0)),
    ("action_exercise_vball_zahra_2", If(zahra_here() and image_showing("zahra"), 100, 0)),
    ("action_exercise_vball_zahra_3", If(zahra_here() and kaan_here() and image_showing("zahra"), 100, 0)),
    
    ("action_exercise_vball_sandy_1", If(sandy_here() and image_showing("sandy"), 100, 0)),
    ("action_exercise_vball_sandy_2", If(sandy_here() and image_showing("sandy"), 100, 0)),
    ("action_exercise_vball_sandy_3", If(erika_here() and sandy_here() and image_showing("sandy"), 100, 0)),

    ("action_exercise_vball_rachel_1", If(rachel_here() and image_showing("rachel"), 100, 0)),
    ("action_exercise_vball_rachel_2", If(rachel_here() and image_showing("rachel"), 100, 0)),

    ])

label action_exercise_vball_robin_1:
    pc "Go [robin.name]!"
    jump action_exercise_vball_end

label action_exercise_vball_robin_2:
    robin.name "Go [name]!"
    jump action_exercise_vball_end

label action_exercise_vball_erika_1:
    erika.name "I got it I got it!!"
    erika.name "Fuck!"
    jump action_exercise_vball_end

label action_exercise_vball_erika_2:
    pc "You have it [erika.name]!"
    jump action_exercise_vball_end

label action_exercise_vball_zahra_1:
    zahra.name "Too easy. You lot need to do better."
    jump action_exercise_vball_end

label action_exercise_vball_zahra_2:
    zahra.name "To you [name]!"
    zahra.name "Nice!"
    jump action_exercise_vball_end

label action_exercise_vball_zahra_3:
    pc "[zahra.name], Stop posing for the boys and play!"
    zahra.name "Jealous?"
    pc "Ugh."
    jump action_exercise_vball_end

label action_exercise_vball_sandy_1:
    sandy.name "Ooooh yeah!"
    jump action_exercise_vball_end

label action_exercise_vball_sandy_2:
    sandy.name "Awww. Almost."
    jump action_exercise_vball_end

label action_exercise_vball_sandy_3:
    sandy.name "Ass out the sand [erika.name] or I'll put my thumb up it."
    erika.name "Promises promises."
    jump action_exercise_vball_end

label action_exercise_vball_rachel_1:
    rachel.name "Uuuwaaaaaaa!!"
    jump action_exercise_vball_end

label action_exercise_vball_rachel_2:
    rachel.name "*Huff* *Huff*"
    rachel.name "I'm gonna die!"
    jump action_exercise_vball_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
