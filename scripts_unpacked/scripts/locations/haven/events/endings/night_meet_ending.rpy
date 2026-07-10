label haven_access_top_floor_night_office:
    $ log.markdone("mq_05_upstairs")
    pcm "Right, try to be quiet..."
    $ walk(loc_haven_office)
    pcm "There we go. Pitch black in here so be must be sleeping. Where is he?"
    pcm "Ah there we go."
    pcm "Ok, how should I handle this? Don't want to wake him up with a jump and scare the shit out of him. He would probably end up calling his guards."
    pcm "Ok, game face on and wake him gently..."
    $ player.face_neutral()
    pc "[alex.fname]... [alex.fname]... Wake up and let's talk."
    alex.nname "Ughhhh."
    pc "Wake up [alex.fname]."
    alex.nname "Ughhh. Whaa?"
    alex.nname "Ugh, who are you? What are you doing here?"
    pc "I'm here to ask you some questions."
    show haven_alex at right1 with dissolve
    alex.nname "What? Who sent you?"
    pc "Doesn't matter. Tell me where [ant.name] is."
    alex.nname "What? [ant.name]? So you aren't with the twins? You here to kill me?"
    pc "Kill you? No thanks. Just tell me where [ant.name] is and I will be on my way."
    alex.nname "I don't know where he is. He isn't here if that's what you're asking."
    pc "No?"
    alex.nname "Look, he came here a while ago and I tried ta help him out. But he had some crazy ideas he wanted me to help him with. I told him no and kicked him out. I haven't seen him since. I swear!"
    pc "Ideas?"
    alex.nname "He wanted to use the people downstairs to test some new medicine or drugs on. I don't want to be hurting them so we had a fight and I kicked him out."
    pc "Hmmm. Was hoping I could find him here. Where did he go?"
    alex.nname "No idea but he might have paid a visit to the twins. They might be okay with pulling shit like that."
    pc "The twins? Who are they?"
    alex.nname "No idea. All I know is they deal with shit like that. Trying to make some new stuff to get people stoned. Don't know much about their organisation since I don't deal in drugs."
    alex.nname "Look, I ain't getting myself killed over a shit like [ant.fname]. Do with him what you want but don't be killin' me over some issue you have with him."
    pc "I told you already. No intention of killing you. Now tell me. If I try to walk out of here, is anyone going to stop me?"
    alex.nname "Err. No."
    pc "No?"
    alex.nname "The guy at the gate is to stop people getting up here. Anyone already up here he will assume was allowed so will just let you pass."
    pc "Great."
    pause 0.5
    hide haven_alex
    $ walk(loc_haven_hallway_3f)
    $ player.face_worried()
    pcm "Shit that was scary."
    pcm "Better get out of here before he calls someone to beat me up..."
    pause 0.5
    jump haven_ending_leave_gateguard
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
