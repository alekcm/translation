label loc_haven_lobby_visit:
    pc "..."
    pcm "Well that was easy. Not even sure if there was anyone who would stop me even if I wore a police uniform. Looks like it was a good time to come here"
    pcm "Ok... Time to look around and see if I can spot anyone who might be [ant.name]."

    jump travel

label loc_haven_bedroom_visit:
    $ player.face_worried()
    pc "..."
    pcm "People are resorting to sleeping like this to escape the rain and cold?"
    pcm "Looks like most of the whores are grouped up on one end of the room. If I want to find somewhere to sleep I should probably go over there."
    pcm "Some men are around the place, but not many. I wonder if that's because all the whores have just come back from working at night."

    show kitty at right1 with dissolve
    if kitty.has_met:
        kitty.name "Reality just sinking in?"
        pc "Huh?"
        pcm "Oh shit, I know her..."
        kitty.name "Most girls who come in here head straight to their place, avoiding eye contact with anyone. You look like a deer stuck in headlights."
        kitty.name "So let me guess. First time here and you are just realising how shitty it can be to live like this."
        kitty.name "Sorry to break it to you love, but we are all in here like cattle. Get used to it. No private rooms with room service around here."
        pcm "Seems she doesn't recognise me..."
        pcm "Og course not. I look different."
        kitty.name "Over there in the alcove is somewhere you can put down. The girl that was there before you was afraid it would collapse on her so moved to the floor."
        pc "Collapse on her? Will it?"
        kitty.name "Probably not."
    else:
        havwhore "Reality just sinking in?"
        pc "Huh?"
        havwhore "Most girls who come in here head straight to their place, avoiding eye contact with anyone. You look like a deer stuck in headlights."
        havwhore "So let me guess. First time here and you are just realising how shitty it can be to live like this."
        havwhore "Sorry to break it to you love, but we are all in here like cattle. Get used to it. No private rooms with room service around here."
        pc "..."
        havwhore "Over there in the alcove is somewhere you can put down. The girl that was there before you was afraid it would collapse on her so moved to the floor."
        pc "Collapse on her? Will it?"
        havwhore "Probably not."
    pc "..."
    pc "Thanks..."
    kitty.name "[kitty.name]."
    kitty.name "Few things to keep in mind. The girls are working when it's night and here when it's day. The men are working when it's day and here when it's night."
    kitty.name "So sleep, shit and shower when it's day so you are with other girls. Avoid being here at night."
    kitty.name "And don't piss anyone off cos no one here is coming to help you if you get your arse beat."
    pc "Thanks for the advice."
    kitty.name "Mmmm."
    hide kitty with dissolve
    pcm "Well, okay then..."
    $ walk(loc_haven_bed)
    $ loc_haven_bed.visited = True
    pcm "No one will be upset if I claim this spot but I shouldn't get too comfortable in this place."
    jump travel

label loc_haven_lounge_visit:
    pcm "Old sofas, chairs and random things to sit on. I guess this is where people hang out to chat."
    pcm "Not sure how safe those firepits are. But since half the room is collapsed I suppose there is enough ventilation."
    jump travel

label loc_haven_storage_visit:
    pcm "Just a storage room. I probably shouldn't hang out here too much. Good place to get caught alone."
    $ walk(loc_haven_lounge)
    jump travel

label loc_haven_shower_visit:
    $ player.face_worried()
    pcm "Ugh, this is depressing. Looks like a large communal shower. No surprise that there are no stall doors or shower curtains. Want to shower, you need to expose your arse to everyone."
    pcm "I shouldn't stand around gawking for too long. Give these people some privacy."
    $ player.face_normal()
    $ loc_haven_shower_stall.visited = True
    jump travel

label loc_haven_utilities_visit:
    pcm "That room is right at the back of the showers. Walking there with my clothes on will get me soaking wet and draw attention so I can't get there right now."
    pcm "The warning signs on the door suggest it's some kind of maintenance room. Doubt I am going to find [ant.name] in there."
    $ loc_haven_utilities.visited = True
    jump travel

label loc_haven_room1_visit:
    pcm "This room is a shithole. Even worse than the rest of the building. The damp from the shower stalls is making all manner of weird stuff grow on the walls."
    jump travel

label loc_haven_room2_visit:
    if loc_haven_lounge.visited:
        pcm "Not much of interest in here. Though I can hear people speaking in the lounge next door. Might be able to overhear them if I try."
    else:
        pcm "Not much of interest in here. Though I can hear muffled voices coming from the room next door. Might be a good place to eavesdrop."
    jump travel

label loc_haven_room3_visit:
    pcm "Looks like some people have been playing dice in here. Other than that, nothing really interesting going on."
    jump travel

label loc_haven_hallway_3f_visit:
    pcm "Looks like the stairs heading up to the 3rd floor. The hallway has some kind of gate installed to stop people passing and some guy sitting behind it."
    pcm "No doubt this is the way up to [alex.fname] [alex.sname]'s place."
    pcm "If I want to speak to him I will have to find my way up there. Although I doubt the guy guarding the gate will just let me pass"
    $ loc_haven_hallway_3f.visited = True
    $ loc_haven_hallway_3f.locked = True
    jump travel

label haven_searched:
    $ log.markdone("mq_05_b")
    $ log.deactivate("mq_05_info")
    $ log.deactivate("mq_05_fire")
    $ log.deactivate("mq_05_pipes")
    $ log.deactivate("mq_05_pipesbreak")
    $ log.deactivate("mq_05_guard")
    $ log.deactivate("mq_05_sprinklers")
    pcm "I have looked around pretty much everywhere and no sign of [ant.name]. Though it's troublesome that I don't know what he looks like."
    pcm "Probably shouldn't just go around asking people if they know him. Good way for him to catch wind of me or for someone to tell him I am looking for him."
    pcm "If I want to keep searching for him, the best place might be the showers where I can see people naked. He can't hide his skin patches in the nude."
    pcm "I can also eavesdrop on the lounge by hanging out in the room next to it or in my bunk where I can listen to the girls talking and see if I can overhear anything about him."
    pcm "But if he isn't here, then I would just be wasting my time..."
    pcm "If that's the case I will have to try to find my way up to [alex.nname] and try and find out from him."
    pcm "*Sigh* Kinda hoped this would be quick and easy but looks like I am going to be here for some time."
    $ player.add_mood((70 - player.mood))
    $ main_quest_05.stage = 3
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
