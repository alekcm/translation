label main_quest_04_checkpoint_lobby_return:
    pcm "[miller.name] asked for time to photocopy his files so I should come back tomorrow."
    jump travel
label main_quest_04_checkpoint_lobby_complete:
    pcm "I should speak to [tucker.name] before I agree to help out in the police station."
    jump travel
label main_quest_04_checkpoint_lobby_closed:
    pcm "I need to head inside there and speak to [miller.name]. But I should come back at a more appropriate time"
    jump travel

label checkpoint_lobby_reception_speak:
    if not paige_here():
        pcm "No one is here. I should come back at a better time."
        jump travel
    show paige at right1 with dissolve
    paige.name "How can I help?"
    menu:
        "Ask for help about [mira.name]" if log.interactive("mira_missing_05"):
            jump quest_mira_missing_whore_investigation_security

        "Ask for help to rescue [mira.name]" if log.interactive("mira_missing_09") and not "asked_security" in quest_mira_missing.list:
            jump quest_mira_missing_security_intel_complete
        "Nothing, thanks":

            paige.name "Oh? Okay."
            hide paige with dissolve
            jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
