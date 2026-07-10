



label main_quest_01_reporter_game_start:
    $ walk(loc_alley)
    show simon at right1
    simon.name "Here we go, no one should disturb us here."
    if weather_var >= 3:
        jump main_quest_01_reporter_game_reject_weather
    else:
        jump main_quest_01_reporter_game_start_first

label main_quest_01_reporter_game_start_first:
    pc "Ok, so then answer me. Why are you looking into The Institute?"
    simon.name "Ok, but payment first. Then I will answer."
    pc "..."
    pcm "Am I really going to strip for him?"
    if player.check_sex_agree_choice(diff=4,option1="I just need to try and get the info before things go too far" ,option2="No, stop this before it goes any further", exhibitionist=True):
        pc "Right then..."
        $ temp_var_1 = False
        $ temp_var_2 = 0
        $ temp_var_3 = 0
        $ temp_var_4 = 0
        $ temp_var_5 = 0
        $ temp_var_6 = 0
        $ temp_var_7 = 0
        jump main_quest_01_reporter_game_strip
    else:
        jump main_quest_01_reporter_game_reject

label main_quest_01_reporter_game_reject:
    pc "No, I decided I am not doing this. Undressing in this dirty alleyway is too much."
    jump main_quest_01_reporter_game_reject_cont

label main_quest_01_reporter_game_reject_weather:
    if weather_var == 3:
        pc "What? It's pissing down."
        simon.name "And?"
        pc "Taking my clothes off in this shitty alleyway is bad enough. But I am not doing it in the rain."
    elif weather_var == 4:
        pc "What? It's a blizzard out here."
        simon.name "And?"
        pc "Taking my clothes off in this shitty alleyway is bad enough. But I'll freeze to death out here before you tell me anything."

    if pub_waitress.timesworked > 4:
        pc "Let's go back in the pub into the back room there and do this."
        simon.name "Huh? Think they are just going to let us waltz in?"
        pc "They will if I am with you."
        if "work" in tab_top:
            simon.name "What? Are you actually a barmaid?"
            pc "I am whatever pays. Come on."
        else:
            simon.name "Oh, they know you there?"
            pc "Yeah. Come on."
        $ walk(loc_pub)
        pause 0.5
        $ walk(loc_pub_changingroom)
        jump main_quest_01_reporter_game_start_first
    else:
        jump main_quest_01_reporter_game_reject_cont

label main_quest_01_reporter_game_reject_cont:
    simon.name "Are you sure? Your loss. Good luck in your investigation. I'll see you around [fname]."
    hide simon with dissolve
    pc "Damn. That went pretty poorly but at least I didn't end up naked in this dirty alleyway."
    pc "Oh well. I suppose I will have to go and tell [tucker.name] what happened."
    pc "Probably best to sleep of this booze first though. This small body doesn't seem to handle it too well."
    $ main_quest_01.stage = 2
    $ log.markdone("mq_01_b")
    $ walk(loc_revel)
    jump travel





label main_quest_01_reporter_game_strip:
    if temp_var_3 == 3 or temp_var_2 == 3:
        jump main_quest_01_reporter_game_won
    if c.pants == 0 and c.bra == 0 and c.outfit == 0 and c.top == 0 and c.bottom == 0:
        jump main_quest_01_reporter_game_naked
    else:
        if temp_var_1 == True:
            simon.name "Want to pay for another question?"
        menu:

            "Remove top." if c.top > 0:
                $ c.top = 0
                $ c.jacket = 0
                if c.bra == 0:
                    simon.name "Losing your top with no bra underneath? You were just waiting for an excuse to free those lovely tits weren't you?"
                    pc "I didn't really think this through too well did I?"
                    simon.name "Mmm, I could look at those perky tits all day."
                elif c.braless == True:
                    simon.name "Losing your top with that kind of bra? You were just waiting for an excuse to show off those puppies weren't you?"
                    pc "I didn't really think this through too well did I?"
                    simon.name "Mmm, I could look at those perky tits all day."
                else:
                    simon.name "Mmmm, much better. And bigger than I thought they would be for such a tiny girl."
                    pc "..."
                jump main_quest_01_reporter_game_questions

            "Remove bottoms" if c.bottom > 0:
                $ c.bottom = 0
                if c.pants == 0:
                    simon.name "No pants on? Double win for me."
                    pc "I didn't really think this through too well did I?"
                    simon.name "How about you let me get a closer look?"
                    pc "No chance!"
                    jump main_quest_01_reporter_game_questions
                elif c.pantsless == True or c.thong == True:
                    simon.name "And those pants of yours don't leave much to the imagination. Lucky me."
                    pc "I didn't really think this through too well did I?"
                    simon.name "How about you let me get a closer look?"
                    pc "No chance!"
                else:
                    simon.name "Lovely. I look forward to seeing what you are hiding under those pants"
                    pc "..."
                    simon.name "How about you let me get a closer look?"
                    pc "No chance!"
                jump main_quest_01_reporter_game_questions

            "Remove outfit" if c.outfit:
                $ c.outfit = 0
                simon.name "Lucky me you weren't wearing a separate top and bottoms. We will get closer to the action a lot quicker."
                if not c.bra and not c.pants:
                    simon.name "And no underwear at all under it. You were just asking to show off to me weren't you."
                    pcm "I didn't really think this through too well did I?"
                    simon.name "Nice tits darling. I could look at them all day."
                elif not c.bra:
                    simon.name "And no bra underneath. You were just waiting for an excuse to free those lovely tits weren't you?"
                    pc "I didn't really think this through too well did I?"
                    simon.name "Mmm, I could look at those tits all day."
                elif not c.pants:
                    simon.name "And no pants on? Double win for me."
                    pc "I didn't really think this through too well did I?"
                    simon.name "How about you let me get a closer look?"
                    pc "No chance!"
                elif c.pantsless or c.thong:
                    simon.name "And those pants of yours don't leave much to the imagination. Lucky me."
                    pc "I didn't really think this through too well did I?"
                    simon.name "How about you let me get a closer look?"
                    pc "No chance!"
                jump main_quest_01_reporter_game_questions

            "Remove bra" if c.bra > 0 and (c.top == 0 and c.outfit == 0):
                $ c.bra = 0
                simon.name "Mmmm yes. Let those lovely tits free for me."
                simon.name "For such a slim little girl you have some nice sized ones there. And so perky."
                pc "When you are done gawking, how about you answer me?"
                simon.name "Yes yes."
                jump main_quest_01_reporter_game_questions

            "Remove pants" if (c.pants > 0 or c.socks > 0) and (c.bottom == 0 and c.outfit == 0):
                $ c.pants = 0
                $ c.socks = 0
                simon.name "Ahh yes. The holy grail!"
                if player.phair == 0:
                    simon.name "Completely shaved and smooth. You came prepared didn't you?"
                    pc "I didn't do this for you."
                    simon.name "And yet here you are showing it to me."
                else:
                    simon.name "Nice little bush you have there. I wonder if it's as soft as it looks."
                    pc "Don't even think about it."
                simon.name "I wonder if such a sweet little thing like you has ever given it up to someone?"
                if player.vvirgin == True:
                    pc "..."
                    simon.name "Oh wow. You really are a sweet little thing."
                    pc "Shut up!"
                else:
                    pc "Don't be getting any stupid ideas into your head."
                    simon.name "Okay ok..."
                jump main_quest_01_reporter_game_questions

            "Put a stop to this." if not (c.pants == 0 and c.bra == 0 and c.outfit == 0 and c.top == 0 and c.bottom == 0) and temp_var_1 == True:
                jump main_quest_01_reporter_game_naked_end

label main_quest_01_reporter_game_first_question:
    simon.name "Ok, you held up your end and I have a nice view. So to answer your question."
    simon.name "\"Why are you looking into The Institute?\" Well, the answer is, I am not looking into The Institute."
    pc "What? Then why are you trying to get info from people who work there?"
    simon.name "One question for one piece of clothing. Want me to answer that then you need to pay."
    if c.pants == 0 and c.bra == 0 and c.outfit == 0 and c.top == 0 and c.bottom == 0:
        pc "Shit, one question and I am already standing here with my arse hanging out. I should have thought this through more."
    else:
        pc "Ugh. I need to be more selective with my questions if I want to walk away from this with without having myself stand here stark naked."
    simon.name "So, what'll it be?"
    jump main_quest_01_reporter_game_strip

label main_quest_01_reporter_game_questions:
    if temp_var_1 == False:
        $ temp_var_1 = True
        jump main_quest_01_reporter_game_first_question
    else:
        simon.name "Ok, so you have one question."
        menu:

            "Who are you investigating?" if temp_var_2 == 0:
                $ temp_var_2 = 1
                simon.name "[bob.name]"
                jump main_quest_01_reporter_game_strip

            "Why are you investigating [bob.name]?" if temp_var_2 == 1:
                $ temp_var_2 = 2
                simon.name "His wife paid me to."
                jump main_quest_01_reporter_game_strip

            "What does [bob.name]'s wife want him investigated for?" if temp_var_2 == 2:
                $ temp_var_2 = 3
                simon.name "To find out if he's cheating or not."
                jump main_quest_01_reporter_game_strip



            "Why are you squeezing people in the pub for info?" if temp_var_3 == 0:
                $ temp_var_3 = 1
                simon.name "I was paid to."
                jump main_quest_01_reporter_game_strip

            "Who paid you to investigate the people in the pub?" if temp_var_3 == 1:
                $ temp_var_3 = 2
                simon.name "[bob.name]'s wife."
                jump main_quest_01_reporter_game_strip

            "What does [bob.name]'s wife want him investigated for?" if temp_var_3 == 2:
                $ temp_var_3 = 3
                simon.name "To find out if he's cheating or not."
                jump main_quest_01_reporter_game_strip



            "Why are you investigating people from The Institute?" if temp_var_4 == 0:
                $ temp_var_4 = 1
                simon.name "I am not investigating people from The Institute."
                jump main_quest_01_reporter_game_strip

            "Are you really even a reporter?" if temp_var_5 == 0:
                $ temp_var_5 = 1
                simon.name "No I am not. I am a private investigator. People are more forthcoming to someone calling themselves a reporter over a P.I."
                jump main_quest_01_reporter_game_strip

            "Are you trying to dig up dirt to blackmail The Institute?" if temp_var_6 == 0:
                $ temp_var_6 = 1
                simon.name "No I am not. I have no interest in The Institute."
                jump main_quest_01_reporter_game_strip

label main_quest_01_reporter_game_naked:
    simon.name "And here you stand naked as the day you were born. What a beautiful sight."
    simon.name "But without anymore clothes to pay with, how do you expect to get the info you want now?"
    pc "..."
    simon.name "Tell you what. I'll let you play with my clothes instead."
    pc "What?"
    simon.name "Come here and take my clothes off instead and I will let you ask another question. How about it?"
    pcm "Damn, I'm standing here butt ass naked and still haven't got all the info I need. What should I do?"
    if player.check_sex_agree_choice(diff=4,option1="I have come too far to back out now" ,option2="No, this has gone too far already. I can't continue"):
        jump main_quest_01_reporter_game_naked_cont
    else:
        jump main_quest_01_reporter_game_naked_end

label main_quest_01_reporter_game_naked_cont:
    pc "Ugh"
    pc "What do you want me to do?"
    simon.name "Watching a sexy little munchkin like you has made things a bit... Hard."
    pc "Munchkin? I know I am short, but munchkin?"
    if loc_cur == loc_alley:
        simon.name "We are naked in an alleyway and that's what you choose to focus on?"
    else:
        simon.name "Standing here in front of me stark naked and that's what you choose to focus on?"
    pc "Screw you. Now tell me what the hell you are up to!"
    simon.name "Ok, tell you what. Take this one step further and I will give you all the info you want. No more games."
    pc "Further? How much further can things get at this point?"
    simon.name "Please our friend down there. Once you have done that I will give you everything I have in my bag here. It has all my notes and everything you want."
    pc "What, I'm not touching your \"Friend\" down there."
    simon.name "If you want a more hands off deal, then turn around and let me touch you while I do it myself."
    pcm "Fuck, what do I do?"
    $ npc_race_picker(simon)
    menu:
        "Wrap your fingers around it.":
            jump main_quest_01_reporter_game_naked_handjob
        "Turn around.":
            jump main_quest_01_reporter_game_naked_buttjob
        "End this now.":
            jump main_quest_01_reporter_game_naked_end





label main_quest_01_reporter_game_naked_handjob:
    simon.name "Come here then, it won't bite."
    show sb_handjob nohand worried notop
    hide simon
    with dissolve
    pc "..."
    show sb_handjob down straight
    simon.name "So come on, let's feel your fingers around it."
    show sb_handjob up
    pc "Ugh..."
    show sb_handjob down mast with dissolve
    simon.name "That's the spirit! Acting like it's the first time you've seen a cock."
    show sb_handjob up
    if player.hvirgin == True and player.ovirgin == True:
        pc "It is... First time someone's has been in my hand anyway."
        simon.name "Ohh, first time giving a hand job? Not sure if I should be happy or sad."
    $ player.sex_hand(simon, main_quest_01)
    simon.name "Put some effort in at least."
    pc "Huff."
    show sb_handjob down
    "I start to actually put some effort in and slide my hand up and down the shaft of his cock."
    simon.name "Haaa. Now that's better."
    simon.name "Mmmmmm."
    if player.check_sex_agree(4):
        pcm "Sucking him off would probably make things faster."
        jump main_quest_01_reporter_game_naked_blowjob
    else:
        simon.name "Now how about giving it a taste?"
        pc "What?"
        simon.name "Put it in your mouth."
        pc "..."
        if player.check_sex_agree_choice(diff=2, option1="It will speed things up", option2="Ugh no..."):
            jump main_quest_01_reporter_game_naked_blowjob
        else:

            show sb_handjob up
            pc "I'm not putting it in my mouth. Think yourself lucky you are getting this much."
            simon.name "Suit yourself."
            show sb_handjob down
            pcm "Need to make him finish as quickly as possible. I can't be naked out here all day."
            "I start to furiously jerk off his cock, feeling every bump and vein along his shaft as I rub him."
            simon.name "Ahhh, starting to enjoy yourself finally."
            show sb_handjob up
            pc "Maybe I am."
            show sb_handjob down
            simon.name "Mmmm yeah, dirty girls can't resist it when they see a nice cock."
            show sb_handjob up
            pc "Is that right? We just go weak at the knees when we see one?"
            show sb_handjob down
            simon.name "Of course."
            pcm "Idiot."
            pc "Mmmmmm ♥"
            simon.name "Ahhhh..."
            simon.name "Yeahhhhh..."
            show sb_handjob worried
            $ player.sex_cum(simon, "face",main_quest_01)
            $ player.cum_locations["cum_chest"] = True
            show sb_handjob shock
            pc "Ahhh."
            simon.name "Haaahaha yeahh..."
            show sb_handjob up frown
            pc "Some warning would have been nice!"
            simon.name "Hahaahaaaaa..."
            simon.name "Now that was a better evening than I was expecting. Nothing better than having a girl on her knees after some beers."
            hide sb_handjob with dissolve
            $ pc_dress_under()
            pc "Glad I could brighten your day."
            $ pc_dress()
            jump main_quest_01_reporter_game_sex_post

label main_quest_01_reporter_game_naked_blowjob:
    hide sb_handjob
    hide simon
    show sb_blowjob up poke 1h
    with dissolve
    show sb_blowjob down with dissolve
    show sb_blowjob down suck with dissolve
    $ player.sex_oral(simon,main_quest_01)
    "I wrap my lips around his hard cock and take it into my mouth, tasting the salty precum that has leaked off the end of his cock."
    pc "Mmmmmffff..."
    simon.name "Ahh yeah. Nice and warm."
    show sb_blowjob closed
    simon.name "Haaaaa..."
    show sb_blowjob 2h with dissolve
    pcm "Need to make him finish as quickly as possible. I can't be naked out here all day."
    simon.name "Ahhh, starting to enjoy yourself finally."
    show sb_blowjob poke laugh up with dissolve
    pc "Maybe I am."
    show sb_blowjob suck down with dissolve
    simon.name "Mmmm yeah, dirty girls can't resist it when they see a nice cock."
    pc "Mmfff..."
    pc "(Idiot... Just hurry.)"
    pc "Mmmmmm ♥"
    simon.name "Ahhhh..."
    "He grabs my head and forces himself deeper in my mouth and I can feel him throbbing..."
    simon.name "Yeahhhhh..."
    $ player.sex_cum(simon, "mouth", main_quest_01)
    "His cum fills my mouth as he pushes his cock as deep as I can take. The clear taste of his salty load getting stronger with each throb of his cock."
    pc "Mmmmmfffff."
    simon.name "Haaahaha yeahh..."
    pcm "Damn, I was too slow and he came in my mouth."
    show sb_blowjob poke up ub with dissolve
    pc "Some warning would have been nice..."
    show sb_blowjob neutral with dissolve
    simon.name "Now that was a better evening than I was expecting. Nothing better than having a girl on her knees after some beers."
    show sb_blowjob noman with dissolve
    pc "Glad I could brighten your day."
    hide sb_blowjob with dissolve
    jump main_quest_01_reporter_game_sex_post





label main_quest_01_reporter_game_naked_buttjob:
    simon.name "Good choice. Now turn around."
    if not c.nude:
        $ pc_striptease()
    pc "..."
    show sb_againstwall2 worried
    hide simon
    with dissolve
    simon.name "Wow! Now that's much more beautiful than I expected."
    show sb_againstwall2 cum with dissolve
    simon.name "Such a nice young little ass."
    pc "..."
    simon.name "I can't believe someone with such a perfect ass is bent over right in front of my hard cock."
    pc "Nor can I."
    simon.name "Heh. Don't be so coy. You don't strip off for a guy in an alleyway unless you are enjoying it at least just a bit."
    pc "I just want what you have. Nothing more."
    simon.name "What I have for you is right here baby."
    pc "Yeah, so give it to me."
    simon.name "Mmmm, all in due time you sexy little thing."
    pc "Stop calling me little."
    simon.name "Don't like being called little?"
    pc "..."
    simon.name "Sweetheart. You are a tiny girl with huge appeal. I have never seen such beauty in such a small package."
    pc "..."
    if player.check_sex_agree_choice(diff=1, option1="Am I really pretty?", option2="..."):

        simon.name "You say that as if you don't even know. Fishing for compliments or something?"
        $ player.spank()
        show sb_againstwall2 shock
        pc "Ahh"
        simon.name "Yes you are."
        pc "...Are what?"
        simon.name "Beautiful."
        show sb_againstwall2 happy
        $ player.add_desire(10)
        $ player.add_conf(5)
        pc "..."
    else:
        pc "Am I..."
        pc "..."
        simon.name "Cat got your tongue?"

        pc "Ahh"
        simon.name "And yes you are."
        show sb_againstwall2 happy
        pc "..."
        $ player.add_conf(2)

    pc "Th... Thanks..."
    simon.name "What's that? It must be the first thing you have said to me that wasn't snarky or insulting."
    pc "Count yourself lucky. You deserve much worse than snarky for making me do this."
    simon.name "I'm not making you do anything. This is your choice."
    pc "..."
    simon.name "I have something you want and you have something I want. So we exchange."
    pc "..."
    pc "Isn't that another word for prostitution?"
    simon.name "Maybe. Who cares. We are all whores one way or another. More so these days while living this shit life."
    simon.name "I have to drag up info I don't give a shit about just to avoid starving to death or living under a bridge. If I had to bend over like you are now, I would have to do it."
    simon.name "But no one wants my arse. So I have a lot less to offer than you do. Think yourself lucky you are as beautiful as you are. You can get away with a lot in life by shaking your goods."
    pc "What? My goods...?"
    show sb_againstwall2 pokevaghand with dissolve
    pc "Ahhh! Hey. Stop trying to poke me with that thing."
    simon.name "Don't worry your sweet little ass."
    pc "Don't worry? You are poking me with your cock."
    simon.name "Try and enjoy it. No point only one of us having fun."
    pc "Ugh."
    if player.check_sex_agree_choice(diff=2, option1="Might as well", option2="No, stop poking me"):

        if player.vvirgin:
            if loc_cur.outside:
                pc "Ok, but don't even think of going any deeper. I don't want to be losing my virginity in this smelly alleyway."
            else:
                pc "Ok, but don't even think of going any deeper. I don't want to be losing my virginity in some pub back room."
            simon.name "Why am I not surprised a sweet little thing like you is a virgin?"
        else:
            if loc_cur.outside:
                pc "Ok, but don't even think of going any further. I've no interest in fucking you in this alleyway."
            else:
                pc "Ok, but don't even think of going any further. I've no interest in getting fucked in here."

        pc "Ahh..."
        simon.name "Mmmmmm. Good, let me make you happy."
        if player.vvirgin == True:
            simon.name "A little virgin on the end of my cock should be made to scream for more. I can't be letting your first time be boring."
            pc "Fuck you first time!"
        else:
            simon.name "I wonder how many cocks have made you scream while fucking you?"
            pc "Well so far you aren't one of them."
        simon.name "Mmmmm. Your wet pussy is telling a different story little girl."
        pc "I told you. Stop calling me small!"
        simon.name "Get used to it pumpkin. You will be called a lot worse if you make use of your pussy to solve your problems."
        show sb_againstwall2 pokevag vhappy
        $ player.spank()
        pc "Aii."
        pcm "This shitty guy... But it doesn't feel bad at all. If it was anyone else I would actually be enjoying this a lot more."
        show sb_againstwall2 wink
        $ player.spank()
        pc "Ahh. What are you doing?"
        simon.name "Spanking your fine ass. Little sluts like you love a spanking."
        $ player.spank()
        if player.check_sex_agree_choice(diff=3, option1="Ahhh... Mmmmm...", option2="Stop that. Take it away"):

            simon.name "Mmmm, feels good doesn't it? How about I go a little faster?"
            pc "Mmm."
            simon.name "What a lovely sight. Your sexy ass bent over with my cock pressed against you."
            pc "...Mm..."
            simon.name "Like all little sluts. Once you get them going they can't resist the cock between their legs."
            simon.name "You want me to go all the way don't you?"
            menu:
                "Press against him" if player.check_sex_agree(5, notif=False) and not player.vvirgin:
                    jump main_quest_01_reporter_game_naked_buttjob_sex_proactive
                "Mmmmm, this feels good":

                    jump main_quest_01_reporter_game_naked_buttjob_sex

                "Keep going but don't put it inside!" if not player.vvirgin:
                    jump main_quest_01_reporter_game_naked_buttjob_rub

                "..." if player.vvirgin:
                    if renpy.random.randint(1, 5) == 1:
                        jump main_quest_01_reporter_game_naked_buttjob_jerk
                    else:
                        jump main_quest_01_reporter_game_naked_buttjob_rub

                "No. Keep it out! I'm not losing my virginity here!" if player.vvirgin and not player.check_nowill(notif=False):
                    if renpy.random.randint(0, 1) == 1:
                        jump main_quest_01_reporter_game_naked_buttjob_jerk
                    else:
                        jump main_quest_01_reporter_game_naked_buttjob_rub
        else:

            simon.name "Aww love, you sure know how to play hard to get. You have my hard cock between your legs and you are still playing coy?"
            pc "I just want info from you, not your cock in me."
            simon.name "You could have fooled me darling."
            jump main_quest_01_reporter_game_naked_buttjob_jerk
    else:


        jump main_quest_01_reporter_game_naked_buttjob_jerk





label main_quest_01_reporter_game_naked_buttjob_jerk:
    pc "Don't poke me with that thing. Don't even put it near me."
    simon.name "Okay okay if you say so."
    show sb_againstwall2 pokevaghand with dissolve
    pc "..."
    simon.name "Such a sexy ass. Mmmmm."
    $ player.spank()
    show sb_againstwall2 wink
    pc "Ahhh."
    simon.name "Oh yeah."
    $ player.spank()
    show sb_againstwall2 shock
    pc "Ah."
    simon.name "Ahhhh you sexy little slut. This ass is far too nice to resist."
    pc "..."
    simon.name "Ah don't be getting all shy on me now you dirty little girl."
    pc "Not getting shy. Just waiting for you to finish."
    simon.name "Ahh seeing my cock over your sexy ass is so nice."
    pc "Good for you."
    "I can clearly feel him pressing his cock against my clit as he wanks, using the tip to give me as much stimulation as he can."
    "If it wasn't for the situation, I might actually start enjoying what he is doing."
    simon.name "Ahhh yeah"
    simon.name "Fuuuck."
    if player.check_sex_agree(4, notif=False) and not player.has_perk(perk_preg_want):
        pc "Close?"
        simon.name "Haaa yeah..."
        pcm "He might cum in me at this rate."
        jump main_quest_01_reporter_game_naked_buttjob_cum_blowjob

    elif not player.check_pullout():
        jump main_quest_01_reporter_game_naked_buttjob_jerk_cuminside
    elif renpy.random.randint(1, 4) == 1:
        jump main_quest_01_reporter_game_naked_buttjob_cum_pullout_poke
    else:
        jump main_quest_01_reporter_game_naked_buttjob_cum_pullout

label main_quest_01_reporter_game_naked_buttjob_rub:
    pc "No. Don't go inside. Just keep it like this."
    simon.name "Oh you like being rubbed like this do you?"
    pc "..."
    simon.name "Your pussy is soaked so no point in keeping silent. Your body is telling me everything I need to know."
    pc "Ahhh... Haaaa... ♥"
    show sb_againstwall2 pokevaghand vhappy with dissolve
    simon.name "Mmmm, moan for my cock!"
    "He starts rubbing his cock between my lips and wanking with it pressed against my clit."
    pc "Ahhhhh..."
    show sb_againstwall2 ag
    pc "Oooohhhhh... ♥ ♥"
    simon.name "Your pussy is so warm and this ass of yours. Both begging to be fucked."
    pc "Hufff... Haaaa... ♥"
    show sb_againstwall2 pokevag vhappy with dissolve
    simon.name "Little slut. You want it all the way don't you?"
    if player.check_sex_agree_choice(diff=3, option1="Ahhhh yes... \u2665", option2="No not all the way"):
        jump main_quest_01_reporter_game_naked_buttjob_sex
    else:
        simon.name "Ahhh..."
        simon.name "Tell me."
        show sb_againstwall2 pokevaghand shock with dissolve
        pc "... ♥"
        simon.name "Tell me you love it."
        show sb_againstwall2 happy
        pc "It's... ♥ nice..."
        simon.name "Haaa"
        $ player.spank()
        show sb_againstwall2 ag
        pc "Ahhh~~ ♥"
        show sb_againstwall2 happy
        simon.name "Yeah take it."
        pc "Mmmm."
        simon.name "Haaaahaaaaa."
        show sb_againstwall2 pokevag shock with dissolve
        pc "What are you doing? ♥"
        simon.name "I'm close."
        show sb_againstwall2 happy
        pc "Ah."
        pc "Ohhhh yes ♥"
        pc "Mmmmmmm."
        $ player.spank()
        pc "Yes ♥"
        simon.name "Ahhhhh!"
        if player.check_sex_agree(4, notif=False) and not player.has_perk(perk_preg_want):
            pcm "He might cum in me at this rate."
            jump main_quest_01_reporter_game_naked_buttjob_cum_blowjob

        elif not player.check_pullout() and renpy.random.randint(1, 10) == 1:
            jump main_quest_01_reporter_game_naked_buttjob_jerk_cuminside
        elif renpy.random.randint(1, 4) == 1:
            jump main_quest_01_reporter_game_naked_buttjob_cum_pullout_poke
        else:
            jump main_quest_01_reporter_game_naked_buttjob_cum_pullout

label main_quest_01_reporter_game_naked_buttjob_sex:
    pc "Oooohhhhh... ♥ ♥"
    pc "Ahhh it's deeper ♥."
    simon.name "Mmmmm such a warm pussy. So wet. It's just asking for my cock."
    pc "♥ ♥ ♥"
    $ player.spank()
    pc "Ahhhh."
    simon.name "You like a spanking slut?"
    pc "Uhhhhuhhhh ♥"
    jump main_quest_01_reporter_game_naked_buttjob_sex_insert

label main_quest_01_reporter_game_naked_buttjob_sex_proactive:
    "I don't even answer him and just start pressing back against him. He makes no attenpt to back up and I feel his cock sliding inside of me."
    jump main_quest_01_reporter_game_naked_buttjob_sex_insert

label main_quest_01_reporter_game_naked_buttjob_sex_insert:
    $ player.sex_vag(simon, main_quest_01)
    show sb_againstwall2 ag closed insidevag with dissolve
    pc "Ahhhhhh fuuuuuuckkkkk."
    "He penetrates me fully to the hilt making my body run with such uncontrollable desire, and without pause slowly and rhythmically starts to fuck me."
    pc "♥ Fuck fuck fuuuuu..."
    pc "Ahhhhh~"
    simon.name "Ahhh so good... Such a nice little slut on the end of my cock."
    show sb_againstwall2 wink with dissolve
    if player.virgin_pregcheck == True:
        simon.name "How does it feel to be made a woman?"
        pc "Hhhhuuuu...?"
        simon.name "Not a virgin anymore. Remember this day. Fucked for the first time like the little slut you are."
        $ player.spank()
        pc "Haaaa. ♥ In this shitty place you took it from me!"
        simon.name "I did. You can thank me later."
        pc "Haaaaa."
        $ player.spank()
    pc "Fuck! ♥"
    simon.name "Ahhhh yessssss!"
    "He fucks me against the wall even faster. Each thrust going deeper and deeper into me. His cock throbbing more with each thrust and I can feel him getting a bit erratic."
    simon.name "Ahhh this is the best."
    simon.name "Ooohhhh I am close."
    show sb_againstwall2 open happy with dissolve







    pc "Mmmm."
    simon.name "Where do you want it?"
    $ player.sex_cum_location_offer(
    difficulty=1, 
    cum_want="main_quest_01_reporter_game_naked_buttjob_cum_want", 
    cum_notwant="main_quest_01_reporter_game_naked_buttjob_cum_not_want", 
    cum_pullout="main_quest_01_reporter_game_naked_buttjob_cum_pullout",
    cum_pullout_anal="main_quest_01_reporter_game_naked_buttjob_cum_pullout_anal", 
    cum_pullout_bj="main_quest_01_reporter_game_naked_buttjob_cum_pullout_blowjob",  
    cum_pullout_poke="main_quest_01_reporter_game_naked_buttjob_cum_pullout_poke",
    cum_bj="main_quest_01_reporter_game_naked_buttjob_cum_blowjob",    
    
    block_anal_check=True
    )






label main_quest_01_reporter_game_naked_buttjob_cum_want:
    simon.name "Ahhh fuck!"
    $ player.sex_cum(simon, "inside",main_quest_01)
    "His cock starts to throb inside me as he pushes it as deep into me as he can."
    show sb_againstwall2 neutral with dissolve
    simon.name "Ahhhaaaahhh........"
    simon.name "Ahhh yes! Ahhhhhhhh."
    pc "Haaaaaaaa!"
    simon.name "Ahhhhhhhh....."
    show sb_againstwall2 cum with dissolve
    "He pulls his cock out, and with it I feel the stream of his warm cum start to leak out of me and down my leg."
    pc "I can't believe we just did that."
    simon.name "I told you. Little sluts can't resist a good cock."
    pc "..."
    show sb_againstwall2 noman with dissolve
    if player.pregnancy == 0:
        if player.has_perk(perk_preg_want):
            pcm "Is he going to send me home with a baby in my belly?"
            pc "..."
            $ player.pregnancy = 3
            show sb_againstwall2 happy open with dissolve
            if simon.vvirgin:
                pcm "Mmm, making me a woman and a mother at the same time?"
            pcm "Mmmmm"
            if player.isfat:
                $ player.pregnancy = 1
            else:
                $ player.pregnancy = 0
            show sb_againstwall2 neutral with dissolve
        elif player.pregpills == False:
            pcm "Maybe I shouldn't have let him cum in me. He might end up really marking me as his bitch by making me carry his baby."
            pcm "..."
            $ player.pregnancy = 3
            show sb_againstwall2 shock with dissolve
            if simon.vvirgin:
                pcm "Fuck, I came here a virgin and is he going to make me leave a mother?"
            pcm "Whaaaa!"
            pcm "No no no. Stop Thinking such things..."
            if player.isfat:
                $ player.pregnancy = 1
            else:
                $ player.pregnancy = 0
            show sb_againstwall2 neutral with dissolve
            pcm "Phew..."

    simon.name "Ha. That was the best."
    hide sb_againstwall2
    jump main_quest_01_reporter_game_sex_post

label main_quest_01_reporter_game_naked_buttjob_cum_not_want:
    simon.name "Ahhh fuck!"
    $ player.sex_cum(simon, "inside",main_quest_01)
    "His cock starts to throb inside me as he pushes it as deep into me as he can."
    show sb_againstwall2 shock angry with dissolve
    simon.name "Ahhhaaaahhh........"
    pc "Fuck, I said pullout."
    simon.name "Ahhh yes! Ahhhhhhhh."
    pc "Stop pressing it in me."
    simon.name "Ahhhhhhhh....."
    show sb_againstwall2 cum with dissolve
    "He pulls his cock out, and with it I feel the stream of his warm cum start to leak out of me and down my leg."
    pc "I can't believe we just did that. And you came inside."
    simon.name "I told you. Little sluts can't resist a good cock."
    pcm "He's not even listening..."
    show sb_againstwall2 noman with dissolve
    if not player.preg_knows:
        if player.pregpills == False:
            pcm "Idiot better not end up getting me pregnant."
            pcm "..."
            $ player.pregnancy = 3
            show sb_againstwall2 shock with dissolve
            pcm "Whaaaa!"
            pcm "No no no. Stop Thinking such things..."
            if player.isfat:
                $ player.pregnancy = 1
            else:
                $ player.pregnancy = 0
            show sb_againstwall2 neutral with dissolve
            pcm "Phew..."

    simon.name "Ha. That was the best."
    hide sb_againstwall2
    jump main_quest_01_reporter_game_sex_post

label main_quest_01_reporter_game_naked_buttjob_cum_pullout:
    show sb_againstwall2 cum neutral with dissolve
    $ player.sex_cum(simon, "pullout",main_quest_01)
    "I feel him cumming on my back and arse. His warm wet seed marking me as his bitch."
    simon.name "Ahhhaaaahhh........"
    $ junk_var_1 = 1
    simon.name "Ahhh yes! Ahhhhhhhh."
    pc "Haaaaaaaa!"
    simon.name "Ahhhhhhhh....."
    show sb_againstwall2 noman with dissolve
    pc "I can't believe we just did that."
    simon.name "I told you. Little sluts can't resist a good cock."
    pc "..."
    hide sb_againstwall2
    jump main_quest_01_reporter_game_sex_post

label main_quest_01_reporter_game_naked_buttjob_cum_pullout_anal:
    simon.name "Ahhh fuck!"
    show sb_againstwall2 pokevaghand with dissolve
    show sb_againstwall2 pokeasshand with dissolve
    pc "Mmm, cum on me."
    show sb_againstwall2 pokeass with dissolve
    simon.name "Fuck so good."
    if player.asex == 0:
        $ player.sex_anal(simon, main_quest_01)
        show sb_againstwall2 insideass pain angry with dissolve
        pc "AHHHHHH!"
        pc "What the fuck?!?"
        $ player.sex_cum(simon, "anal", main_quest_01)
        simon.name "Ahhhhhh fuuuuuu!"
        pc "Take it out take it out take it out!!"
        simon.name "Unnnnnnggggg."
        show sb_againstwall2 pokeass shock with vpunch
        pc "Fucking hell."
        simon.name "Mmmmmm."
        pc "Don't \"mmmmm\" me you arsehole. What made you think sticking it up my arse was a good idea?"
        pc "Fuck feels like it's on fire."
        simon.name "What? You didn't want me to cum in your pussy."
        pc "That doesn't mean you stick it in my arse."
        simon.name "What, isn't that how most girls have sex these days?"
        pc "What? No! I dunno. Not me anyway. Never did it before."
        simon.name "No? Sorry. I assumed all you girls did."
        if player.vsex == 1:
            simon.name "Wow, does that mean I got you first time in both holes?"
            pc "Don't be so proud of yourself. Arsehole."
    elif not player.check_anal_agree(notif=False):
        $ player.sex_anal(simon, main_quest_01)
        show sb_againstwall2 insideass with dissolve
        pc "Ah fuck! What the hell?"
        $ player.sex_cum(simon, "anal", main_quest_01)
        simon.name "Ahhhhhh fuuuuuu!"
        pc "Idiot! Some warning would be nice!"
        simon.name "Unnnnnnggggg."
        show sb_againstwall2 pokeass with vpunch
        pc "Shit, it hurts."
        simon.name "Mmmmmm."
        pc "Don't \"mmmmm\" me you arsehole. What made you think sticking it up my arse was a good idea?"
        simon.name "What? You didn't want me to cum in your pussy."
        pc "No. But you could have gave some warning or been more gentle. Not used to having people stick things in my bum."
        simon.name "What, isn't that how most girls have sex these days?"
        pc "Yeah, but I've not exactly gotten used to it."
        simon.name "No? Sorry."
    else:
        $ player.sex_anal(simon, main_quest_01)
        show sb_againstwall2 insideass shock angry with dissolve
        pc "Aie"
        $ player.sex_cum(simon, "anal", main_quest_01)
        simon.name "Ahhhhhh fuuuuuu!"
        simon.name "Unnnnnnggggg."
        simon.name "Mmmmmm."
        pc "Didn't think you would do that."
        simon.name "Mmm, wanted to keep it somewhere warm."
        pc "Right."
        show sb_againstwall2 pokeass neutral with dissolve
    simon.name "Ha. That was the best."
    show sb_againstwall2 noman with dissolve
    pc "I can't believe we just did that."
    simon.name "I told you. Little sluts can't resist a good cock."
    hide sb_againstwall2
    jump main_quest_01_reporter_game_sex_post

label main_quest_01_reporter_game_naked_buttjob_cum_pullout_blowjob:
    simon.name "Come here, on your knees."
    show sb_againstwall2 shock
    pc "Err..."
    hide sb_againstwall2
    show sb_blowjob neutral face 1h up
    with dissolve
    simon.name "Ahhh fuck!"
    $ player.sex_cum(simon, "face", main_quest_01)
    show sb_blowjob neutral closed
    "While I can't see what's going on, I can feel his warm cum hitting my face."
    simon.name "Ahhh yes!"
    simon.name "Mmmmmm."
    show sb_blowjob down with dissolve
    show sb_blowjob up with dissolve
    pc "Safe to open my eyes?"
    simon.name "Mmmm. Yeah."
    show sb_blowjob noman with dissolve
    simon.name "You look good like that."
    pc "Very funny."
    pc "I can't believe we just did that."
    simon.name "I told you. Little sluts can't resist a good cock."
    hide sb_blowjob
    jump main_quest_01_reporter_game_sex_post

label main_quest_01_reporter_game_naked_buttjob_cum_pullout_poke:
    show sb_againstwall2 pokevaghand with dissolve
    $ player.sex_cum(simon, "pullout", main_quest_01)
    "I feel his cock throbbing and him cumming while still pressing it against me."
    simon.name "Ahhhaaaahhh........"
    if player.want_pullout:
        show sb_againstwall2 shock
        pc "Hey, pull it out more."
        show sb_againstwall2 cum with dissolve
        pc "Idiot."
    $ junk_var_1 = 1
    simon.name "Ahhh yes! Ahhhhhhhh."
    simon.name "Ahhhhhhhh....."
    show sb_againstwall2 noman with dissolve
    pc "I can't believe we just did that."
    simon.name "I told you. Little sluts can't resist a good cock."
    pc "..."
    hide sb_againstwall2
    jump main_quest_01_reporter_game_sex_post

label main_quest_01_reporter_game_naked_buttjob_cum_blowjob:
    hide sb_againstwall2
    show sb_blowjob neutral poke 1h up
    with dissolve
    "I quickly press my hips forward to get him out of me and spin around while dropping to my knees to make sure he doesn't cum inside me."
    show sb_blowjob suck down with dissolve
    "My lips barely even get around his cock before..."
    $ player.sex_cum(simon, "mouth", main_quest_01)
    simon.name "Ahhh yes!"
    simon.name "Mmmmmm."
    show sb_blowjob up with dissolve
    simon.name "Haaaaa... So good."
    show sb_blowjob ub poke with dissolve
    show sb_blowjob ub noman with dissolve
    show sb_blowjob neutral with dissolve
    show sb_blowjob laugh with dissolve
    pc "I can't believe we just did that."
    simon.name "I told you. Little sluts can't resist a good cock."
    hide sb_blowjob
    jump main_quest_01_reporter_game_sex_post

label main_quest_01_reporter_game_naked_buttjob_jerk_cuminside:
    "Without warning, he presses his cock deeper until it is inside of me."
    if player.pregpills or player.preg_knows or player.has_perk(perk_preg_want):
        $ player.sex_vag(simon, main_quest_01)
        show sb_againstwall2 insidevag worried shock with dissolve
        pc "Ah fuck!"
        simon.name "Ahhhhhhhh!"
        $ player.sex_cum(simon, "inside",main_quest_01)
        simon.name "Ahhhaaaahhh........"
        simon.name "Ahhh yes! Ahhhhhhhh."
        pc "Haaaaaaaa!"
        simon.name "Ahhhhhhhh....."
        pc "Uff. Who told you to put it inside?"
        show sb_againstwall2 pokevag neutral with dissolve
        show sb_againstwall2 noman with dissolve
        simon.name "Sorry. Kind of caught up in the moment."
        pc "Idiot."
        hide sb_againstwall2
        jump main_quest_01_reporter_game_sex_post
    else:
        $ player.sex_forced(simon, main_quest_01)
        $ player.sex_vag(simon, main_quest_01)
        show sb_againstwall2 insidevag angry pain with dissolve
        pc "Ah fuck!"
        simon.name "Ahhhhhhhh!"
        $ player.sex_cum(simon, "inside",main_quest_01)
        pc "What the fuck are you doing?"
        simon.name "Ahhhaaaahhh........"
        simon.name "Ahhh yes! Ahhhhhhhh."
        with hpunch
        pc "Get off!!"
        hide sb_againstwall2 with hpunch
        if player.firstvsex == simon.fullname:
            pc "Fucking idiot! What did you do that for? I told you I was a virgin and you go and put it in me?"
        else:
            pc "Idiot! What you going to do if I end up pregnant?"
        pc "Fuck!!!"
        jump main_quest_01_reporter_naked_postforced





label main_quest_01_reporter_game_sex_post:
    show simon smile at right1
    with dissolve
    if simon.vsex:
        pc "Yeah yeah. Okay now give me what my pussy just paid for."
    else:
        pc "Now give me what I wanted."
    if player.cum_locations["cum_assin"]:
        pc "And my arse..."
    simon.name "Sure, here you go. Was well worth it."
    pc "I'm sure for you it was."
    $ pc_dress_under()
    if player.cum_locations["cum_vagin"] or player.cum_locations["cum_assin"]:
        if c.pants:
            pc "Ah shit, you are leaking into my pants now."
        else:
            pc "Ah shit, you are leaking down my leg."
    elif player.cum_locations["cum_vagout"] or player.cum_locations["cum_assout"]:
        if c.pants:
            pc "Ah shit. The arse of my pants are all wet now."
        else:
            pc "Ah shit, you are leaking out my arse now."
    else:
        pause 0.5
    $ pc_dress()
    if player.cum_locations["cum_face"]:
        pc "What am I going to do with this you left on my face?"
        simon.name "Keep it. It's a good look on you."
        pc "Ha, yeah right."
    $ player.face_meek()
    pc "... ..."
    pc "..."
    $ player.face_worried()
    pc "So you aren't even looking into The Institute?"
    jump main_quest_01_reporter_game_info_call


label main_quest_01_reporter_naked_postforced:
    show simon smile at right1
    with dissolve
    $ pc_dress_under()
    pc "..."
    $ pc_dress()
    simon.name "I might have went a little too far..."
    pc "Fuck you cunt! Of course you did!"
    simon.name "Sorry. I wanted you to enjoy yourself."
    pc "I was. Until you forced it in. Now go and fuck off you filthy cretin."
    simon.name "Err ok. Well here is my bag..."
    hide simon with dissolve
    pc "Fuck..."
    pc "..."
    if player.firstvsex == simon.fullname:
        pc "I can't believe my first experience was... This..."
        pc "*SOB*"
    else:
        pc "I can't believe that happened..."
        pc "*SOB*"
    pc "I hope it was at least worth something."
    pc "..."
    pc "Nothing at all here about The Institute. He's just investigating that drunkard [bob.name] who works there."
    pc "His wife wants him investigated... Thinks he's cheating... [simon.name] thinks she's just looking for dirt to kick him out and lay claim to his stuff."
    pc "..."
    pc "Fuuuuuck."
    pc "I put all this effort in. Try to be like some movie spy. Get myself raped..."
    pc "I told myself this will be for a greater good. This is important stuff."
    pc "And it's just this. This is rubbish. I thought I would be finding info about industrial espionage or something. Not a scheming wife trying to take her husband's money."
    pc "..."
    pc "Ufff. That's my fault. This was just a training mission. Of course I am not going to be sent on something like that."
    pc "Ugh, well I suppose I should report this all to [tucker.name]. But first I need to go home and sleep off this booze. And a shower to wash that filthy cunt off me."
    jump main_quest_01_reporter_game_complete_wrapup

label main_quest_01_reporter_game_won:
    pc "So you didn't want anything to do with The Institute?"
    simon.name "Looks like you won the game and got the info you wanted, so I'll tell you."
    pc "Ok, why are you looking into The Institute?"
    jump main_quest_01_reporter_game_info_call

label main_quest_01_reporter_game_naked_end:
    pc "No, this has gone too far. I refuse to let it go further."
    if not player.has_perk(perk_exhibitionist):
        $ pc_dress_under()
    simon.name "Hmm, that's a shame. I was enjoying this game."
    pc "That makes one of us."
    if not player.has_perk(perk_exhibitionist):
        $ pc_dress()
    simon.name "Ok, I'll tell you what. You have been a good sport and I have had more fun than I have in a long time. So I'll give you what you want."
    pc "What, you will?"
    simon.name "Sure, I won't ever forget this night. So why not?"
    pc "Ok..."
    pc "So why are you investigating The Institute?"
    jump main_quest_01_reporter_game_info_call

label main_quest_01_reporter_game_info_call:
    simon.name "I don't care about The Institute. [bob.name]'s wife wants him investigated. Pretty sure she is looking for a reason to leave him but she doesn't want to leave empty handed."
    pc "So she wants to find something he has done wrong so she can use it as an excuse to kick him out and claim his stuff?"
    simon.name "Seems that way to me. Whenever I return to her with nothing, she insists I find something and keeps paying me. [bob.name] is a boring git so there is never anything to find."
    if bob.has_met:
        simon.name "All he does is work then drink his evenings away in the pub. I got a little happy when he went up to you. Maybe I could finally get photos of something interesting."
        simon.name "But you were pretty quick to get rid of him. So I wasn't even able to get something I could spin."
    else:
        pc "Who is [bob.name]? What's he got to do with anything?"
        simon.name "Err... Shouldn't you know that? You work with him?"
        pc "No idea who he is."
        simon.name "Err... Okay. Works for the hospital and does nothing but work and drink. I can't even get any info on him I could spin."
    simon.name "Hmm, that gives me an idea. Maybe I could hire you to get [bob.name] in such a situation..."
    if player.check_whore(vag_sex=False):
        pc "Not sure you could afford me."
        simon.name "Oh? Didn't expect that response."
        simon.name "Well, let's see..."
        simon.name "How about £50 for steamy photos and £150 if I can get a shot with you two with his cock out. She can't argue with that."
        pc "You have the money with you?"
        simon.name "I do. Moment I get those shots it's yours."
        menu:
            "Sure, okay":
                $ add_to_list(main_quest_01.list, "agree_bobsex")
                pc "Hmm, let's head back inside."
                simon.name "Ok."
                if c.nude:
                    pc "Hold on."
                    $ pc_dress_slow()
                    pc "Right, let's go."
                $ walk(loc_pub)
                jump main_quest_01_reporter_bobsex_leadup
            "No thanks":
                pc "No thanks. Think I'll pass on the offer."
    else:


        pc "Hey, don't go talking as if I'm willing to be involved in your schemes."
    simon.name "No worries. I'll have to speak to the wife first anyway. I'll contact you if anything comes up."
    pc "I let you have my body for this info, but don't talk to me like we are best buddies. I've no interest in seeing you again."
    simon.name "And I'll be very happy if I see you again. But anyway, I've had a lovely time but I don't think I will outstay my welcome."
    simon.name "See you around [fname]."
    hide simon

    $ player.face_annoyed()
    with dissolve
    pc "Yeah yeah."
    $ player.face_frown()
    pcm "Uff, all that effort and what? A wife investigating her husband? Nothing at all interesting. Wasn't at all worth doing what I did."
    if pc_lost_clothes():
        if player.has_perk(perk_exhibitionist):
            pcm "And as fun as this is, I should probably put something back on."
        else:
            pc "And I'm still standing here naked like an idiot."
        $ pc_dress_slow()
    if player.cum_locations["cum_vagin"]or player.cum_locations["cum_assin"]:
        pcm "Still bloody leaking from that idiot."
    elif player.cum_locations["cum_mouth"]:
        pcm "Gonna need to wash this taste out of my mouth."
    elif player.cum_locations["cum_face"]:
        pcm "I had better try to clean my face."
        "I wipe the cum from my face with my hand and hope it is enough for people not to notice."
        $ player.cum_locations["cum_face"] = False
    elif player.cum_locations["cum_assout"] or player.cum_locations["cum_vagout"]:
        if c.pants > 0:
            pcm "Ugh, my pants are all sticky now."
        else:
            pcm "Ugh, my clothes are all sticky now."
    pcm "Ah well. I suppose I can give [tucker.name] good news. They expected me to fail and here I am with all the info they needed."
    pcm "Better go home first and sleep off this booze though. Gonna have a killer headache in the morning."
    jump main_quest_01_reporter_game_complete_wrapup
    return

label main_quest_01_reporter_game_complete_wrapup:
    $ main_quest_01.missionvar1 = True
    $ main_quest_01.stage = 2
    $ log.markdone("mq_01_b")
    if not loc_cur == loc_pub:
        $ walk(loc_pub)
        with dissolve
    $ walk(loc_revel)
    with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
