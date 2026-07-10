label action_whore_discover_first:
    if log.interactive("quest_homeless_start_03"):
        pcm "Just arrived in an unfamiliar town and already considering this..."
        pcm "How else am I supposed to make money though? Maybe there are other jobs around?"
        if player.pregnancy >= 2:
            pcm "Doubt anyone would want to hire someone close to pushing out a baby."
            pcm "Hmm, doubt anyone would want to pay me to have fun with them either..."
            pcm "Fucked either way."
            pcm "Ugh, I'm fucked because I was fucked..."
        pcm "No harm in asking though. Not like I have to actually bend over for anyone."
        pcm "Ugh, how has it come to this?"
    elif player.has_perk(perk_gamine, notif=True):
        pcm "Hmmm, lot of girls around looking like they are selling themselves."
        pcm "Was a disgusting job before and cant imagine things are any better these days."
        pcm "Maybe a should have a chat with one of the girls and see how things work."
    elif player.has_perk(perk_sucu, notif=True):
        pcm "Hmmm, lot of girls hanging around looking for customers it seems."
        pcm "This could be a good way to keep myself from getting tired after taking that weird pill."
        pcm "Make some money at the same time."
    elif not loc_highway_slum_home.locked:
        pcm "Hmmm, lot of girls around looking like they are selling themselves."
        pcm "Now that I live in this dump, most of my neighbours are whores."
        pcm "I wonder if I should find out about how it works?"
    else:
        pcm "Hmmm, lot of girls hanging around who look like they are selling themselves..."
        pcm "Not like I haven't done it before so might be worth checking out."

    show kitty at right1 with dissolve
    pc "Hey. New around here and wondering how things work."

    if player.has_perk(perk_gamine, notif=True):
        kitty.name "And? I'm not your mother. Go away."
        pc "No? You don't do mother play? I thought that would be popular."
        kitty.name "Wha...? Oh fuck you, bitch."
        $ player.face_shock()
        pc "That's not nice Mummy."
        kitty.name "Pffft!!!"
        pc "I just found you and you reject me so quickly! What did I do to upset you Mummy?"
        kitty.name "Haha! That mouth will get you killed."
        $ player.face_happy()
        pc "So how do I go about getting it filled for some money?"
        kitty.name "Look around. You attract someone and take 'em somewhere alone."
        $ player.face_normal()
        pc "Hmmm... No pimp or something to \"protect\" me?"
        kitty.name "Fuck no. They tried and ended up dead. No cunt to take our money any more."
        kitty.name "Hang around here, find someone, fuck 'em and you are done."
        pc "Sounds good. Girls group together to keep off weirdos?"
        kitty.name "Yeah, try and stick with the other girls and keep an eye out for each other."
        pc "Right, thanks Mum."
        kitty.name "Yeah."
    elif kitty.has_met:
        kitty.name "And? I'm not your mother. Go away."
        pc "No, but you kinda helped me out before so thought I would ask."
        kitty.name "I don't remember you."
        pc "No... I spent some time in [haven]. You kinda warned me how to keep safe."
        kitty.name "Ah, you stayed there? Where?"
        pc "Where? In some shitty alcove in the shared sleeping area with one eye open."
        kitty.name "Hmmm... Okay then."
        kitty.name "You hang around here, make eye contact with people you want to be with and look sexy. Folk who have no interest will ignore you."
        kitty.name "If they keep looking, then you might have a fish on the hook so go talk to them."
        pc "Right. Anything we should be aware of?"
        kitty.name "Don't go with them until you know what they want from you and you set a price."
        kitty.name "Some freaks here want weird shit. Pay to beat you up, want you to shit on 'em or other things. Best avoid 'em. Never worth it."
        kitty.name "An' don't go nowhere that no one can hear your screamin'. It's how you end up a corpse."
        pc "Err... Corpses common?"
        kitty.name "No. But still something to be careful of."
        pc "Right... Thanks..."
    else:
        kitty.name "And? I'm not your mother. Go away."
        pc "Err... Right then..."
        hide kitty with dissolve
        kitty.name "*Tsk* Hold on."
        show kitty at right1 with dissolve
        pc "Hmmm?"
        kitty.name "Look around. You can see what's going on. Hang around looking sexy and people will come to you."
        pc "Okay. That's it? No protection racket or anything like that?"
        kitty.name "Fuck no. They tried that and ended up dead. Dunno if the whores killed em, security or the boss at [haven]. Anyone who tries ends up dead."
        pc "Oh? Err, good I guess."
        kitty.name "Not like those fucks would protect us anyway. So more money for us getting fucked."
        pc "So I'm good just to... advertise myself? Not gonna piss anyone off?"
        kitty.name "Yeah all good. Stick with the other girls, watch each others backs and don't get killed."
        pc "Thanks."
    kitty.name "Stay safe."
    hide kitty with dissolve
    pcm "Right then. Just stand around and get paid..."
    pcm "Sounds easy enough."
    $ log.assign("Street walking")

    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
