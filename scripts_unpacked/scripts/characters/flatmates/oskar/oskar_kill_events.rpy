label oskar_office_enter_reject:
    if oskar.hate or oskar.rape:
        $ player.face_angry()
        pcm "I'm not going in that cunts office."
    else:
        $ player.face_annoyed()
        pcm "I better not go in there, he already kicked me out. Don't think a smile will get me back in."
    jump travel

label oskar_office_breakin_action:
    if not inv.qty(item_beer_poison) >= 4:
        pcm "What is the point? Trashing his office doesn't help me. Though it will feel good."
        pcm "Unless I am just going to do something fucked like leave some poison for him, so point in wrecking his office."
        jump travel
    if not inv.qty(item_chis):
        pcm "If I want to try and get inside, I probably need to get a tool of some kind..."
        jump travel
    if not t.hour in (0,1,2,3,4):
        pcm "Hmm, now is probably not a good time. I should come past midnight or something when this place is a graveyard."
        jump travel

    pcm "Hmm, am I really going to break in so I can give him these beers?"
    pcm "All I have is this shitty chisel so he will know someone broke in."
    pcm "I might be able to just wait until he leaves the office at some point. Does he ever go and have lunch?"
    menu:
        "Break in":
            $ add_to_list(loc_office_ll.list, "pc_broke_in")
            $ player.face_worried()
            pcm "Hmm, okay then..."
            $ player.face_annoyed()
            "I take the chisel out and use it to start hacking away at the lock area."
            "There isn't much I can do to hide the fact I am breaking in, so I don't even try."
            pcm "Better he thinks some junkies are breaking in or something."
            $ working(15)
            with hpunch
            "It takes me quite a wile to hack away at the lock. I try to be quiet but it is not easy."
            $ working(15)
            with vpunch
            "Being quiet means I am much slower is getting my way into the lock. But eventually I manage it."
            $ working(15)
            with hpunch
            $ player.face_worried()
            pc "*Phew*"
            pcm "Managed it. The door is a mess..."
            $ walk(loc_office_ll)
            $ player.face_worried()
            pcm "Hmm, okay..."
            pcm "He will notice as soon as he comes in the morning that he has been robbed."
            pcm "Well, I'm not actually robbing him, but maybe I should."
            pcm "First the beers."
            $ inv.drop(item_beer_poison, 4, notif=True)
            $ oskar.inv.take(item_beer_poison, 4)
            $ add_to_list(oskar.list, "gave_poison_beer")
            pcm "Right, someone breaks into his office and just leaves some beer. Not suspicious at all..."
            pcm "I should trash the place a bit and make it look like someone was looking for money."
            pcm "When cleaning up he might find te beer and think they were always there."
            with vpunch
            pcm "And some more mess..."
            with hpunch
            pcm "He's a cunt anyway. I should just burn his office."
            with vpunch
            $ player.face_evil()
            pcm "Ha, that would be fun. Just turn it all to ash."
            with hpunch
            pcm "No, I'm here to get my place back, not just trash his stuff..."
            with vpunch
            $ player.face_worried()
            pcm "Hmm, would I even get my place back?"
            pcm "They might just put someone else in charge."
            pcm "Whatever, he is a cunt. So no loss even if I don't get my old place back."
            $ walk(loc_stairwell)
            $ walk(loc_residential)
            pcm "Now I wait I guess."
            jump travel
        "Not now":

            pcm "Better think of something else and come back."
            jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
