label action_exercise_run_conf:
    jump expression WeightedChoice([
    ("action_exercise_run_conf_1", 100),
    ("action_exercise_run_conf_2", 100),
    ("action_exercise_run_conf_3", 100),
    ("action_exercise_run_conf_4", 100),
    ("action_exercise_run_conf_5", 100),
    ("action_exercise_run_conf_6", 100),
    ("action_exercise_run_conf_7", 100),
    ])

label action_exercise_run_conf_1:
    girl "Keep running bitch. You're gonna need to be faster than that if you want to catch a man."
    $ player.face_annoyed()
    pcm "Cunt!"
    jump action_exercise_run_end

label action_exercise_run_conf_2:
    "As I am running, I notice at the corner of my eye a man jogging behind me keeping perfect pace with me."
    $ player.face_worried()
    pcm "What does he want? Is he following me?"
    pcm "Ugh!"
    jump action_exercise_run_end

label action_exercise_run_conf_3:
    if c.ass:
        guy "Nice ass you got there bitch."
    elif c.skirt and (c.thong or c.pantsless):
        guy "Nice ass bitch. Bend over and show us some more!"
        if not pants:
            guy "You know you want a good fuckin' going out without any knickers on."
            guy "Come 'ere! I got what you be wantin'"
    else:
        guy "Keep shaking those hips ya dirty whore!"
    $ player.face_annoyed()
    pcm "Idiot."
    jump action_exercise_run_end

label action_exercise_run_conf_4:
    if c.clevage and c.braless:
        guy "Damn bitch, bounce those tits some more fer us!"
        guy "Mmmm, come 'ere an' giv' us a taste ya dirty girl!"
    elif c.clevage:
        guy "Ey bitch. Let me put ma face between your sweaty tits!"
    elif c.braless:
        guy "Hey sugar tits! Come 'ere and let me 'ave a feel!"
    else:
        guy "Keep bouncing those tits you dirty whore! Come 'ere and I'll make ya feel good."
    $ player.face_annoyed()
    pcm "Arsehole."
    jump action_exercise_run_end

label action_exercise_run_conf_5:
    guy "Look at da running whore!"
    $ player.face_annoyed()
    pc "Piss off!"
    guy "Fuck you bitch!"
    pc "..."
    jump action_exercise_run_end

label action_exercise_run_conf_6:
    "As I am running I notice a group of boys pointing at me and laughing among themselves."
    pcm "The hell..."
    jump action_exercise_run_end

label action_exercise_run_conf_7:
    "As I am running, I see something at the corner of my eye before..."
    $ player.punch()
    pcm "The fuck was that? Someone throwing stuff at me?"
    jump action_exercise_run_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
