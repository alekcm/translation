label haven_notif_can_set_fire:
    pcm "So I have a lighter and an accelerant. While playing with fire rarely ends well, I could set a fire somewhere and hope the guards come running to deal with it."
    pcm "Question is where? Fire is easy to smell and people will respond to it right away. If it hasn't had time to burn before it's noticed then it will be put out before the guards even know about it."
    pcm "Also need to make sure to pick a good time. If the place is too busy I will be spotted before I even start. People won't take too kindly to trying to set fire to their home."
    $ log.activate("mq_05_fire", notify=True)
    jump travel

label haven_notif_tool:
    $ add_to_list(main_quest_05.conversation_topics, "tool_notif")
    pcm "So I have this crowbar type thing but what should I do with it?"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
