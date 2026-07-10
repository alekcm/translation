label rachel_talk_exhib_game_picker:

    if not "rachel_talk_exhib_games_chain" in rachel.dict:
        $ rachel.dict["rachel_talk_exhib_games_chain"] = 0
    if not "rachel_talk_exhib_games_played" in rachel.dict:
        $ rachel.dict["rachel_talk_exhib_games_played"] = 0
    if not "rachel_talk_exhib_games_pc_last_played" in rachel.dict:
        $ rachel.dict["rachel_talk_exhib_games_pc_last_played"] = False

    if not (t.hour >= 21 or t.hour in night):
        pcm "Need to wait until night for that."
        jump travel
    if not exhib_games_canplay():
        pcm "I think that's enough for today."
        jump travel

    show rachel at right1 with dissolve

    if not c.nude:
        jump rachel_talk_exhib_strip

    if rachel.dict["rachel_talk_exhib_games_chain"] == 0:
        jump rachel_talk_exhib_game_start
    elif rachel.dict["rachel_talk_exhib_games_chain"] == 1:
        rachel.name "So, ready to play now?"
        jump rachel_talk_exhib_game_library
    elif rachel.dict["rachel_talk_exhib_games_chain"] == 2:
        jump rachel_talk_exhib_game_doors
    elif rachel.dict["rachel_talk_exhib_games_chain"] == 3:
        jump rachel_exhib_game_cafe
    elif rachel.dict["rachel_talk_exhib_games_chain"] == 4:
        jump rachel_exhib_game_thinking
    elif rachel.dict["rachel_talk_exhib_games_chain"] == 5:
        jump rachel_exhib_game_mast
    elif rachel.dict["rachel_talk_exhib_games_chain"] == 6:
        jump rachel_exhib_game_tease
    elif rachel.dict["rachel_talk_exhib_games_chain"] == 7:
        jump rachel_exhib_game_boys
    elif rachel.dict["rachel_talk_exhib_games_chain"] == 8:
        jump rachel_exhib_game_boys_rachel
    else:
        if rachel.dict["rachel_talk_exhib_games_pc_last_played"]:
            jump rachel_exhib_game_picker_rachel
        else:
            jump rachel_exhib_game_picker_pc

label rachel_exhib_game_picker_rachel:
    pc "So, my turn to get you to do something."
    rachel.name "Okay. What do you want?"
    pc "Hmmm..."
    menu:
        "Something":
            $ NullAction()
        "Something else":
            $ NullAction()
    "Not in yet. But here it will pick random events."
    jump travel

label rachel_exhib_game_picker_pc:
    $ rachel.dict["rachel_talk_exhib_games_pc_last_played"] = True
    rachel.name "Okaaaaay. I have an idea."
    pc "Okay. What do you want?"
    "Not in yet. But here it will pick random events."
    jump travel

label rachel_exhib_game_mason_investigate:
    show mason at right1 with dissolve
    $ add_to_list(mason.list, "mason_investigate")
    mason.pname "Miss [sname]. Can we have a word?"
    pc "Err, sure? Everything ok?"
    mason.pname "The head for some reason told me I should come to you with an issue I have."
    pc "Okay... Well I'm no doctor, but probably you should avoid the highway..."
    mason.pname "He said something that you are an investigator?"
    pc "Err, something like that."
    mason.pname "I'm a bit too busy to look into it. But people have been breaking in the school at night."
    pc "They have? How do you know?"
    mason.pname "Things are moved, not like I left them the night before."
    pc "Okay. Nothing stolen or missing?"
    mason.pname "No. But I don't like the idea of strange people making this place dangerous for you lot."
    pc "Dangerous for us? How does that work?"
    mason.pname "I have no idea who they are. Junkies? Whores bringing customers? Don't want this place attracting the wrong kind of attention."
    pc "Ah..."
    pc "..."
    mason.pname "So, can I leave this issue with you?"
    pc "Err, no..."
    mason.pname "No?"
    pc "I mean, you don't have anything to worry about. I already know who is here at night. And it's not junkies or whores."
    mason.pname "Oh? Then who might it be?"
    pc "Well... Me for one."
    mason.pname "You?"
    pc "Yeah."
    mason.pname "Might I ask why?"
    if "mason_walked_home" in loc_beach_gym.list:
        pc "It's safe. No one comes here other than those we know. Good place to hang out at night where we wont get beaten up."
        pc "You do weird stuff at the beach, I do it here."
        mason.name "Oh? Like that? Err... Okay."
        mason.name "Right..."
    else:
        pc "It's safe. No one comes here other than those we know. Good place to hang out at night where we wont get beaten up."
        mason.pname "Oh? Okay... That makes sense..."
        pc "Yeah..."
        mason.pname "And you know these people. They are from here?"
        pc "Yeah."
        mason.pname "And you can assure me I won't come in one morning to the building burned down or a junkie party going on?"
        pc "I can assure you that if you did see that, it wouldn't involve us."
        mason.pname "..."
        mason.pname "Good enough."
    hide mason with dissolve
    pcm "..."
    jump travel

label rachel_exhib_game_mason_catchnude:
    $ add_to_list(mason.list, "mason_caughtnude")
    show mason at right1 with dissolve
    mason.pname "Miss..."
    $ player.face_shock()
    $ player.cover()
    pc "Ahhh!"
    mason.pname "Err..."
    pc "What are you doing here?"
    mason.pname "I... Err... Didn't feel comfortable leaving this as we did..."
    mason.pname "So I... Wanted to make sure everything is ok..."
    $ player.face_annoyed()
    $ player.uncover()
    pc "Well, everything is fine."
    if "mason_walked_home" in loc_beach_gym.list:
        pc "I bet you just came here to perv on more girls."
        mason.pname "Err... No... I came to make sure everything was okay."
        $ player.face_annoyed()
        pc "Yes, everything is fine. Now go away. Only naked people allowed in at night."
        mason.pname "Right..."
        hide mason with dissolve
        $ player.face_happy()
        pcm "Haha!"
    else:
        mason.pname "You... Are doing this of your own will?"
        pc "Yes. Now go away. Only naked people allowed in at night."
        mason.pname "Are..."
        $ player.face_angry()
        pc "Shoo!"
        mason.pname "Right..."
        hide mason with dissolve
        pcm "Fuck..."
        $ player.face_worried()
        pcm "Caught red handed..."
        pcm "Caught bare arsed?"
        $ player.face_happy()
        pcm "Haha!"
    jump travel

label rachel_exhib_game_mason_joinnude:
    $ add_to_list(mason.list, "mason_joinnude")
    show mason soft at right1 with dissolve
    $ player.eye = 6
    pc "Err..."
    $ player.face_neutral()
    mason.pname "Miss [sname]."
    pc "You are naked."
    mason.pname "You did say only naked people allowed."
    pc "I did, didn't I? Didn't expect you would come back naked."
    mason.pname "It a problem?"
    pc "I guess not. Just don't try and stick your thingy in me when I bend over."
    pc "The hell is a teacher coming in here naked with us for anyway?"
    mason.pname "Err... This sort of thing is not unfamiliar to me..."
    pc "It's not?"
    mason.pname "No."
    pc "Okay, not going to tell?"
    mason.pname "I just want to make sure you girls are okay. Have a bit of fun while at it. Need to be careful when... doing these sorts of things."
    pc "Yeah, not let any strange men in..."
    mason.name "Ask me to leave and I will."
    pc "..."
    pc "Ugh..."
    pc "Come, I'll introduce you to [rachel.name]."
    show mason at left1 with dissolve
    $ walk(loc_school_gym)
    pc "[rachel.name]?"
    show rachel angry at right1 with dissolve
    rachel.name "Hey! You told me a hundred times not to bring any men in here. Now you come here with one."
    pc "Yeah, I didn't bring this one. He just showed up."
    rachel.name "Who is he?"
    pc "[mason.pname]. Our volleyball coach."
    show rachel happy
    rachel.name "Oooh. Dirty teacher."
    mason.pname "Since we are all here naked, you can call me [mason.name]."
    rachel.name "Don't be bringing any strange men here or [name] will get really mad at us."
    mason.name "Good to know."
    rachel.name "Now run around the field!"
    mason.name "What?"
    rachel.name "It's your dare. Run around the field."
    mason.name "Really?"
    pc "Yup."
    mason.name "Okay."
    hide mason with dissolve
    pc "..."
    pc "I didn't think he would actually go."
    rachel.name "Haha!"
    pc "He caught me in the hallway naked."
    rachel.name "Oooh, That sounds fun."
    pc "I told him only naked people allowed. I thought it would get rid of him but seems he is a pervert."
    rachel.name "He's a man."
    pc "Yeah... Should have known..."
    show mason nude at left1 with dissolve
    mason.name "Phew! Done."
    rachel.name "Oooh! Look at that!"
    pc "What?"
    rachel.name "His thingy is standing up."
    $ player.face_happy()
    pc "So it is."
    rachel.name "So he is a pervert."
    mason.name "I told you, I am not unfamiliar with this."
    pc "So much that it makes you hard?"
    mason.name "Why else would we do this?"
    rachel.name "Haha! Pervy coach. Should have known."
    if loc_school_toilet_girls.has_gloryhole:
        $ player.face_shock()
        rachel.name "Bet you are one of the pervs sticking their dick in the hole in the toilets."
        mason.name "The hole? You know about that?"
        pc "No, nothing. Ignore her."
        mason.name "That was..."
        $ player.face_shout()
        pc "I CANT HEAR YOU LALALALA!"
        mason.name "..."
    $ player.face_neutral()
    rachel.name "What other pervert things do you do, pervert?"
    mason.name "Hmm, we used to play volleyball on the beach. But people stopped coming for whatever reason."
    rachel.name "The beach? Have you been [name]?"
    if loc_beach_hangout.visited:
        pc "Yeah, it's kind of nice there."
        pc "Could probably play nude in the day time and no one would care."
        mason.name "Girls maybe. Not so much guys."
        pc "No?"
    else:

        pc "No, but heard about it. Didn't know they had volleyball."
        rachel.name "Isn't it fine to be naked on the beach?"
        mason.name "For girls, yes. Guys, not so much. Especially when playing volleyball."
        rachel.name "Why not?"

    mason.name "No one wants to see a guy jumping around swinging his dick around."
    rachel.name "I do!"
    pc "Wouldn't say no myself."
    mason.name "Then come and play at night."
    pc "Don't we need a 4th for that?"
    mason.name "Not really. It's not about playing but having naked fun."
    rachel.name "Haha. Good because I don't know how to play."
    mason.name "I have seen that from the gym classes."
    mason.name "Anyway girls. Now that I know you are safe here doing what you are doing, I'll leave you to it. I wont return unless you ask me to."
    mason.name "But if you want, meet me at the beach at night and we can play."
    pc "Okay."
    hide mason with dissolve
    rachel.name "Wow. Pervy teacher."
    pc "Yeah. Nude beach volleyball?"
    rachel.name "Sounds like fun."
    $ add_to_list(loc_beach_hangout.list, "nude_vball")
    hide rachel with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
