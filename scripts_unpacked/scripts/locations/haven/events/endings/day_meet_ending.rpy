label haven_access_top_floor_day_office_enter:
    $ add_to_list(main_quest_05.list, "alex_spoketo")
    $ log.markdone("mq_05_upstairs")
    $ walk(loc_haven_office)
    if "flooded" in main_quest_05.list or "set_fire" in main_quest_05.list:
        jump haven_access_top_floor_day_office_danger
    else:
        jump haven_access_top_floor_day_office_nodanger

label haven_access_top_floor_day_office_danger:
    pc "Err, hello. Sorry to barge in like this."
    show haven_alex at right1
    show haven_guard3 at right3
    with dissolve
    alex.name "The fuck are you doing here? Bitch sneaking in while the guards are busy?"
    if c.nude:
        alex.nname "And why the fuck are you naked?"
    havguard "I'll get rid of her."
    pc "Yeah, sorry about the mess. I needed a way to slip past the gate."
    alex.name "What? It was you?"
    pc "Again, sorry. But I need to ask you some questions."
    if player.check_speech(3):
        alex.name "*Sigh*"
        alex.name "You wreck my place and come in here expecting me to be civil?"
        pc "Only wrecked a little. Would have just asked to meet but your guards shoo everyone away."
        alex.name "*Sigh*"
        if player.check_speech(4):
            alex.name "Ok. Let's hear it. Why the fuck would you cause this much trouble just for a meet with me?"
            pc "I am looking for [ant.name] and we are pretty sure you know where he is."
            alex.name "[ant.name]? \"We\"? Who are \"We\"?"
            pc "Doesn't matter."
            alex.name "It does fucking matter! Who the fuck are you?"
            if player.check_speech(4):
                pc "People who have no interest in you or [haven]. Only [ant.name]."
                alex.name "And causing this mess is what? For fun?"
                pc "I didn't plan to come up here. Hoped to just come into [haven], snatch [ant.name] and be gone. But he is nowhere to be found. So no choice but to come and speak with you."
                alex.name "And what? You will just walk out of here afterwards?"
                pc "That's the plan."
                alex.name "*Sigh*"
                alex.name "..."
                alex.name "Give us some privacy."
                havguard "You sure? I could call in..."
                alex.name "Yes. Leave."
                havguard "Ok..."
                hide haven_guard3 with dissolve
                alex.name "..."
                jump haven_access_top_floor_day_office_talkcont

    jump haven_access_top_floor_day_office_beaten

label haven_access_top_floor_day_office_nodanger:
    pc "Err, hello. Sorry to barge in like this."
    show haven_alex at right1 with dissolve
    alex.name "Huh, who are you? How did you get in here?"
    pc "Yeah, sorry about sneaking up on you. But needed to have a talk."
    alex.name "What do you want? Here to try and kill me?"
    pc "Nothing of the sort. Just want some info about someone called [ant.name]"
    alex.name "..."
    if player.check_speech(3):
        alex.name "The fuck you want to know about that shit for?"
        pc "Doesn't matter. I was hoping to find him here but he was nowhere to be seen. So I had no choice but to come and ask you."
        alex.name "Well you won't be seeing him here. I kicked him out."
        pc "Why?"
        alex.name "What do you care?"
        pc "If I know why, then I might know where he went. What was the problem?"
        alex.name "*Sigh*"
        jump haven_access_top_floor_day_office_talkcont
    else:
        $ player.face_worried()
        alex.name "You come in here mentioning that cunts name? GUYS! GET IN HERE NOW!"
        $ player.face_shock()
        pc "Wait, I just want to..."
        show haven_guard3 at right5 with hpunch
        jump haven_access_top_floor_day_office_beaten

label haven_access_top_floor_day_office_beaten:
    alex.name "Shut her up will you?"
    havguard "On it."
    jump haven_caught_and_beaten

label haven_access_top_floor_day_office_talkcont:
    alex.name "He is scum who has caused me no end of trouble. You plan to kill him?"
    pc "I plan to track him down. What happens after that is someone else's problem."
    alex.name "Someone else's...? Hmmm... Ok."
    alex.name "He wanted to use his supposed skills to manufacture and test drugs on people in [haven] and despite what you might think, I actually want to try to help the shits around here."
    alex.name "So I told him to go fuck himself. He left and will not be returning."
    alex.name "So take whatever problem you have with him elsewhere and out of my place. Don't need any more attention than I already have."
    pc "And where is he now?"
    alex.name "No idea for sure. But I heard rumours he had dealings with The Twins."
    alex.name "Now I don't want any more trouble than is needed. So get the fuck out of here before my guards get worried and hit you over the head."
    pc "They going to stop me from leaving?"
    alex.name "They won't trouble you. So go."
    pc "Great."
    pause 0.5
    $ renpy.scene()
    $ walk(loc_haven_hallway_3f)
    pcm "Shit that was scary."
    pcm "Better get out of here before he calls someone to beat me up..."
    pause 0.5
    jump haven_ending_leave_gateguard
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
