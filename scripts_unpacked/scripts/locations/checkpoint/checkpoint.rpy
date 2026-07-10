label loc_checkpoint_visit:
    pcm "The main route following the highway is completely blocked off. Any vehicles looking to come in are stopped and searched. No idea what for."
    pcm "It's a depressing looking place..."
    pcm "I can see what I'm guessing is a police station near the checkpoint."
    if main_quest_04.active == 1 and main_quest_04.stage == 1:
        jump main_quest_04_loc_checkpoint_visit
    elif log.interactive("quest_homeless_start_03"):
        pcm "This is where I ended up stumbling through when I arrived to the city."
        pcm "No idea how I managed to get through. It's all pretty well guarded."
        pcm "I guess the crazy people chasing me caused a pretty big distraction."
    jump travel_arrival

label main_quest_04_loc_checkpoint_visit:
    pcm "I need to head inside there and speak to [miller.name]."
    $ main_quest_04.stage = 2
    jump travel

label loc_checkpoint_guardpost_visit:
    "This location is purely to allow you to talk to one of the guards manning the checkpoint."
    "It will give you a lot of lore and information about what is going on here."
    "No other purpose right now other than being a good lore dump for those interested."
    jump travel_arrival

label loc_checkpoint_guardpost_chat:
    "Here you will meet an old timer guard. He stands here most of the day just keeping an eye out for anything strange."
    "You will get a lot of outside the city lore from him."
    "As the main world storyline starts to pick up, he will drop hints as to whats going on and what to expect."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
