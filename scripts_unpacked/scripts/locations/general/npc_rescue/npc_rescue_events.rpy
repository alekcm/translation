init python:
    def npc_rescue():
        label_list = []
        if wolfgang_play_location() and numgen(0,4): 
            renpy.jump("action_npc_rescue_wolf")
        
        for person in diary_people_list:
            if person._original_name.lower() + "_here" in globals() and globals()[person._original_name.lower() + "_here"](If(dis(dis_misc), dis_from.locs, dis_cur.locs)) and renpy.has_label("action_npc_rescue_" + person._original_name.lower()) and weightgen(person.love, If(globals()[person._original_name.lower() + "_here"]([loc_cur, loc_from]), 30, 100)):
                label_list.append("action_npc_rescue_" + person._original_name.lower())
        
        if label_list:
            renpy.jump(renpy.random.choice(label_list))


label action_npc_rescue_anita:
    show kitty at right1 with hpunch
    kitty.name "Oi! Fuck of cunt!"
    kitty.name "SOMEONE IS ATTACKING!!!"
    $ player.grope_end()
    "My attacker quickly runs away."
    pc "*Phew* Thanks for that."
    kitty.name "No problem. Be safe."
    hide kitty with dissolve
    if dis(dis_misc):
        $ walk(loc_from)
    jump travel

label action_npc_rescue_nilay:
    show charity at right1 with hpunch
    charity.name "Oi! Fuck of cunt!"
    charity.name "SOMEONE IS ATTACKING!!!"
    $ player.grope_end()
    "My attacker quickly runs away."
    pc "*Phew* Thanks for that."
    charity.name "No problem. Be safe."
    hide charity with dissolve
    if dis(dis_misc):
        $ walk(loc_from)
    jump travel

label action_npc_rescue_samira:
    show rose at right1 with hpunch
    rose.name "Oi! Fuck of cunt!"
    rose.name "SOMEONE IS ATTACKING!!!"
    $ player.grope_end()
    "My attacker quickly runs away."
    pc "*Phew* Thanks for that."
    rose.name "No problem. Be safe."
    hide rose with dissolve
    if dis(dis_misc):
        $ walk(loc_from)
    jump travel

label action_npc_rescue_vivian:
    show pursy at right1 with hpunch
    pursy.name "Oi! Fuck of cunt!"
    pursy.name "SOMEONE IS ATTACKING!!!"
    $ player.grope_end()
    "My attacker quickly runs away."
    pc "*Phew* Thanks for that."
    pursy.name "No problem. Be safe."
    hide pursy with dissolve
    if dis(dis_misc):
        $ walk(loc_from)
    jump travel

label action_npc_rescue_cassidy:
    show cass angry at right1 with hpunch
    cass.name "AAAAWWWAAAAAAAA WAAAAAAAAAAEEEELLLLLLPPPPP"
    $ player.grope_end()
    "My attacker quickly runs away."
    pc "*Phew* Thanks for that."
    cass.name "Yeah... That was scary..."
    pc "Yeah..."
    hide cass with dissolve
    if dis(dis_misc):
        $ walk(loc_from)
    jump travel


label action_npc_rescue_erika:
    show erika at right1 with hpunch
    erika.name "HEY GUYS! WE HAVE TROUBLE!"
    erika.name "SOMEONE IS ATTACKING!!!"
    $ player.grope_end()
    "My attacker quickly runs away."
    pc "*Phew* Thanks for that."
    erika.name "No problem. Be safe."
    hide erika with dissolve
    if dis(dis_misc):
        $ walk(loc_from)
    jump travel

label action_npc_rescue_zahra:
    show zahra at right1 with hpunch
    zahra.name "HEY GUYS! WE HAVE TROUBLE!"
    zahra.name "SOMEONE IS ATTACKING!!!"
    $ player.grope_end()
    "My attacker quickly runs away."
    pc "*Phew* Thanks for that."
    zahra.name "No problem. Be safe."
    hide zahra with dissolve
    if dis(dis_misc):
        $ walk(loc_from)
    jump travel

label action_npc_rescue_sandy:
    show sandy angry at right1 with hpunch
    sandy.name "What are you doing?!"
    sandy.name "HELP! SOMEONE IS ATTACKING!!!"
    $ player.grope_end()
    "My attacker quickly runs away."
    pc "*Phew* Thanks for that."
    sandy.name "No problem. Be safe."
    hide sandy with dissolve
    if dis(dis_misc):
        $ walk(loc_from)
    jump travel

label action_npc_rescue_lake_dealer:
    show lake_dealer at right1 with hpunch
    lake_dealer.name "Oi, fuck off cunt?!"
    lake_dealer.name "Stop fucking with my customers!"
    $ player.grope_end()
    "My attacker quickly runs away."
    pc "*Phew* Thanks for that."
    lake_dealer.name "Be more careful."
    hide lake_dealer with dissolve
    if dis(dis_misc):
        $ walk(loc_from)
    jump travel


label action_npc_rescue_wolf:
    show wolfman roar at right1 with hpunch
    wolf.name "What we got here?"
    wolf.name "Idiot thinks he can fuck around our territory?"
    $ player.grope_end()
    "My attacker quickly runs away."
    wolf.name "Not so fast!"
    hide wolfman with hpunch
    "He runs after the guy and I lose sight of them."
    pc "*Phew* Thank fuck for that."
    $ player.face_worried()
    if not quest_wolfgang.active:
        pcm "What the hell was that all about? Weird naked man coming to save me."
    else:
        pcm "Kick his ass doggy!"
    if dis(dis_misc):
        $ walk(loc_from)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
