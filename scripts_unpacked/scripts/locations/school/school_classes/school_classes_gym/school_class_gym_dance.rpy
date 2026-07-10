



label school_class_gym_dance:

    pcm "It's dance classes today."
    $ pc_dress_event("sport", loc_school_locker_girls, loc_school_gym)

    if school_dance_can_ask_join_team():

        call school_class_gym_dance_jointeam from _call_school_class_gym_dance_jointeam_1
    else:
        $ player.face_exercise()
        if player.isfat == True:
            jump expression renpy.random.choice([
            "school_class_gym_dance_fat1",
            "school_class_gym_dance_fat2",
            "school_class_gym_dance_fat3",
            "school_class_gym_dance_fat4",
            "school_class_gym_dance_fat5",
            "school_class_gym_dance_fat6",
            "school_class_gym_dance_fat7",
            "school_class_gym_dance_fat8",
            "school_class_gym_dance_fat9",
            "school_class_gym_dance_fat10",
            "school_class_gym_dance_fat11"
            ])
        elif school_dance_quest_on_team == True:
            jump expression renpy.random.choice([
            "school_class_gym_dance_team1",
            "school_class_gym_dance_team2",
            "school_class_gym_dance_team3",
            "school_class_gym_dance_team4",
            "school_class_gym_dance_team5",
            "school_class_gym_dance_team6",
            "school_class_gym_dance_team7",
            "school_class_gym_dance_team8",
            "school_class_gym_dance_team9",
            "school_class_gym_dance_team10"
            ])
        else:
            jump expression renpy.random.choice([
            "school_class_gym_dance1",
            "school_class_gym_dance2",
            "school_class_gym_dance3",
            "school_class_gym_dance4",
            "school_class_gym_dance5",
            "school_class_gym_dance6",
            "school_class_gym_dance7",
            "school_class_gym_dance8",
            "school_class_gym_dance9",
            "school_class_gym_dance10",
            "school_class_gym_dance11",
            "school_class_gym_dance12"
            
            
            
            
            
            ])





label school_class_gym_dance_fat1:
    "I am not good enough to try a routine so I practice simple steps."
    pc "Uff, this is a lot harder than it looks."
    pc "Damn [tucker.sname] signing me up for this."
    jump school_class_gym_end

label school_class_gym_dance_fat2:
    "I am not good enough to try a routine so I practice simple steps."
    show svet angry at right1 with dissolve
    svet.name "[fname] move your fat arse!"
    $ player.mouth = 5
    pc "I'm trying!"
    jump school_class_gym_end

label school_class_gym_dance_fat3:
    "I am not good enough to try a routine so I practice simple steps."
    show svet angry at right1 with dissolve
    pc "Ugh, feels like I have two left feet."
    svet.name "And a fat arse. Focus on dealing with that and you will have an easier time."
    $ player.mouth = 9
    svet.name "*Sigh* I should send you out running instead."
    jump school_class_gym_end

label school_class_gym_dance_fat4:
    "I am not good enough to try a routine so I practice simple steps."
    pcm "Uff, this is a lot harder than I thought it would be."
    pcm "1, 2, 3, step. 1, 2, 3, step..."
    pcm "I need to build my stamina more. Maybe a jog in the park now and then."
    jump school_class_gym_end

label school_class_gym_dance_fat5:
    "I am not good enough to try a routine so I practice simple steps."
    pcm "Keep to the rhythm, keep to the rhythm, keep to the rhythm..."
    pc "Ack!"
    jump school_class_gym_end

label school_class_gym_dance_fat6:
    $ player.mouth = 1
    "I am not good enough to try a routine so I practice simple steps."
    pc "I'm doing it, I'm doing it. Heh yes yes."
    $ player.mouth = 3
    show svet angry at right1 with dissolve
    svet.name "Yes [fname]. 1, 2, 3, Step... Good good."
    jump school_class_gym_end

label school_class_gym_dance_fat7:
    "I am not good enough to try a routine so I practice simple steps."
    show svet angry at right1 with dissolve
    pc "Uff, uffff. This is not... Ufff. Easy at all..."
    svet.name "Keep going [fname]. Now is not the time to be resting that fat arse you have."
    $ player.mouth = 5
    pc "Grrr"
    jump school_class_gym_end

label school_class_gym_dance_fat8:
    "I am not good enough to try a routine so I practice simple steps."
    show svet angry at right1 with dissolve
    svet.name "This is simple stuff [fname]. How do you expect to do a routine if you can't do the basic steps?"
    pc "I'm trying I'm trying..."
    jump school_class_gym_end

label school_class_gym_dance_fat9:
    "I am not good enough to try a routine so I practice simple steps."
    show svet angry at right1 with dissolve
    svet.name "Keep going [fname]. You can do better than this."
    pc "Yes... Yes... Better... Ufff..."
    jump school_class_gym_end

label school_class_gym_dance_fat10:
    "I am not good enough to try a routine so I practice simple steps."
    show svet angry at right1 with dissolve
    svet.name "Move [fname]! Don't make me get a whip and beat you like the fat cow you are!"
    pc "I'm moving I'm moving!"
    jump school_class_gym_end

label school_class_gym_dance_fat11:
    "I am not good enough to try a routine so I practice simple steps."
    "♪ ... like the only girl in the wooooorld ... ♪"
    $ player.mouth = 8
    pc "If this wasn't hard enough, I have to dance to this?"
    jump school_class_gym_end





label school_class_gym_dance_team1:
    "I practice my routines with the rest of the [dancet]."
    show svet happy at right1 with dissolve
    svet.name "Good [name]. Keep it up. Step, step... Wonderful!"
    pc "Ooh yes."
    jump school_class_gym_end

label school_class_gym_dance_team2:
    "I practice my routines with the rest of the [dancet]."
    pcm "Kinda glad [tucker.name] put me down for dance class. This is a lot more enjoyable than I would have thought."
    show svet happy at right1 with dissolve
    svet.name "No slacking [name]! Get to it."
    pc "Yes yes."
    jump school_class_gym_end

label school_class_gym_dance_team3:
    "I practice my routines with the rest of the [dancet]."
    $ player.mouth = 6
    pc "♪ ... make me feel, like I'm the only girl in the world... ♪"
    pc "Whoo!"
    jump school_class_gym_end

label school_class_gym_dance_team4:
    "I practice my routines with the rest of the [dancet]."
    show svet happy at right1 with dissolve
    svet.name "More hip movement [name]. You are not some drunk guy in a nightclub stumbling around but a girl on a stage looking to impress!"
    pc "Yes [svet.name]."
    jump school_class_gym_end

label school_class_gym_dance_team5:
    "I practice my routines with the rest of the [dancet]."
    show svet at right1 with dissolve
    svet.name "Ability is what you are capable of, motivation determines what you do and your attitude determines how well you do it."
    svet.name "Keep that in mind ladies."
    jump school_class_gym_end

label school_class_gym_dance_team6:
    "I practice my routines with the rest of the [dancet]."
    show svet at right1 with dissolve
    svet.name "Don't just think what you want to do. FEEL it. You dance with your body so let your body take control!"
    svet.name "Just like the music you are dancing to, let it all come from the heart."
    jump school_class_gym_end

label school_class_gym_dance_team7:
    "I practice my routines with the rest of the [dancet]."
    show svet at right1 with dissolve
    svet.name "Come on girls! You aren't strippers dancing on a pole. You need to actually dance to the rythm and feel the music."
    svet.name "You're not dancing for drunk fools but people that expect more from you."
    jump school_class_gym_end

label school_class_gym_dance_team8:
    "I practice my routines with the rest of the [dancet]."
    show svet at right1 with dissolve
    svet.name "Focus ladies. There is no such thing as talent. It's hard work and practice that will allow you to go anywhere you want."
    svet.name "Make no mistake, there is no one in this world that got anywhere with talent alone. It is a lie! So keep those feet moving!"
    jump school_class_gym_end

label school_class_gym_dance_team9:
    "I practice my routines with the rest of the [dancet]."
    pc "Feel the music... Let my body take control... Dance with the heart... Feel the music..."
    show svet happy at right1 with dissolve
    svet.name "Good [name], good. Keep it up. Nice rhythm."
    jump school_class_gym_end

label school_class_gym_dance_team10:
    "I practice my routines with the rest of the [dancet]."
    show svet at right1 with dissolve
    svet.name "Wonderful [name]. Keep this up and I will make a professional out of you yet."
    pc "Yes [svet.name]."
    jump school_class_gym_end





label school_class_gym_dance1:
    "I attempt one of the dance routines"
    pc "Getting there, getting there..."
    pc "Ouch! Dammit! Almost..."
    jump school_class_gym_end

label school_class_gym_dance2:
    "I attempt one of the dance routines"
    pc "Much more fun now that I have half a clue what I am up to."
    "♪ ... like the only girl in the wooooorld ... ♪"
    pc "But c'mon... This?"
    jump school_class_gym_end

label school_class_gym_dance3:
    "I attempt one of the dance routines"
    pc "Shake it, shake it like a po..."
    show svet at right1 with dissolve
    svet.name "[fname]! You are learning to dance not shaking your ass for likes on Insta! So dance!"
    pc "Yes [svet.name]!"
    jump school_class_gym_end

label school_class_gym_dance4:
    "I attempt one of the dance routines"
    pc "1 and 2 cross it 3 and 4 clap!"
    pc "Ufff."
    jump school_class_gym_end

label school_class_gym_dance5:
    show svet at right1 with dissolve
    svet.name "Land with the front of your feet, not your heels. No one wants to hear your stomping on the stage like an elephant."
    pc "Yes [svet.name]!"
    jump school_class_gym_end

label school_class_gym_dance6:
    show svet at right1 with dissolve
    svet.name "Make sure to breathe. Holding your breath while focusing on the routine will tire you out too much for the following moves."
    svet.name "And count your steps in your mind. Saying it out loud is wasting breath. Literally."
    jump school_class_gym_end

label school_class_gym_dance7:
    show svet at right1 with dissolve
    svet.name "Spread those legs girls. Your thighs would be level with the floor no matter how tall or short you are."
    pc "Yes [svet.name]!"
    jump school_class_gym_end

label school_class_gym_dance8:
    show svet at right1 with dissolve
    svet.name "Chest out. Arm up! Don't cover your face with your arm."
    svet.name "Aaaand pivot, left, left and sliiiiiide."
    jump school_class_gym_end

label school_class_gym_dance9:
    show svet at right1 with dissolve
    svet.name "Work through your mistakes [name]. If you just stop then it's obvious but if you work through it no one will notice. Just power through and pick back up the routine."
    pc "What if I trip over?"
    svet.name "Then make it part of the dance. Get up with style and carry on. Everyone makes mistakes, it's how you cope with it that matters."
    jump school_class_gym_end

label school_class_gym_dance10:
    pc "Left and slide and right and slide. Squat and up and left leg right leg."
    pc "Damn, this is a killer on my thighs. Uuuugh."
    jump school_class_gym_end

label school_class_gym_dance11:
    show svet at right1 with dissolve
    svet.name "Down like you are squatting for a floor toilet. Arse out, chest up, look forward and bring your hips in a circle. And watch your arms, no resting them on your thighs."
    pc "Ahhhh this is a pain. My legs are killing me."
    svet.name "Power through it [name]!"
    jump school_class_gym_end

label school_class_gym_dance12:
    show svet at right1 with dissolve
    svet.name "Now make sure to smile. Let me see those teeth. Dancing is exhausting but you are still expected to look good and sexy."
    pc "Ugh, but it's so hard."
    svet.name "I'll kick you in the butt if you \"but\" me again!"
    jump school_class_gym_end







label school_class_gym_preg_kicked:
    show mason at right1 with dissolve
    mason.name "[fname], let's have a talk."
    pc "Yes [mason.name]?"
    mason.name "I am afraid in your current condition I can't allow you to do any impact exercises or sports."
    mason.name "There are classes set up here to help people in your condition, I suggest you take them."
    pc "Ok..."
    mason.name "Okay then, off you go.."
    hide mason with dissolve
    $ school_gym_preg = True
    jump school_class_gym_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
