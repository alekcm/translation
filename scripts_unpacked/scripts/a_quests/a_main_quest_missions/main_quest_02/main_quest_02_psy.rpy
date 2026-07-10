



label main_quest_02_psychologist:
    $ walk(loc_hospital_psy)
    with dissolve
    tucker.name "[psy.name]? I am here with [fname] [sname]."
    show tucker at right3 with dissolve
    show brooker at right1 with dissolve
    psy.name "Miss [sname]? Wonderful. So good to finally meet you."
    pc "Err, hi. Finally?"
    psy.name "Yes. I have heard so much about you. That's all [tucker.name]. I'll take it from here."
    tucker.name "Ok. Try to take this seriously [fname]."
    hide tucker with dissolve
    psy.name "So Miss [sname]. I have read up about you and your situation so you can speak freely here. There is no secret info that I am not already privy to."
    psy.name "I am here to look after your mental health in regards to the missions you will be undertaking but also about the current changes in your life."
    pc "Ok."
    psy.name "So please, sit down and relax. I would like to ask how you are feeling about these tasks you have been asked to undertake. How do you feel about them?"
    pc "Well. It gives me something to do and some meaning to my life."
    psy.name "Meaning to your life?"
    pc "Well yeah. It's not like I was anything important in my old life. This at least gives me the chance to be a part of something bigger at the start of this new life."
    psy.name "Out of curiosity, why do you refer to them as your \"new\" and \"old\" life?"
    if quest_homeless_start.active:
        pc "I came here with nothing and had to start new. I had only the clothes on my back while running away from all the chaos."
        pc "So new life, new start. Whatever you want to call it."
    else:
        if player.male_origin:
            pc "Hmm, well that's how it feels. I was a guy not too long ago and now I am not. I honestly feel like a totally different person than I used to be."
        else:
            pc "Hmm, well that's how it feels. I might be the same gender as before but nothing else is familiar. I feel like a totally different person than who I used to be."
        pc "And it's not like my old life was anything special. I only really remember major parts of it and none of that seemed exciting or worth returning to."
        if player.male_origin:
            pc "No chance of getting back to being a man either since I died and who I used to be is long gone."
        pc "So despite being suddenly put into an unfamiliar body and this weird situation, it kinda feels like I have been given a new chance at life."
        pc "I can't say I fully trust The Institute and their wider intentions, but I am at least mostly certain they mean no harm to me. So I can try and make something of myself working with them."
    psy.name "Well it is good to hear you are looking forward and working to improve your life and not looking backwards with regrets. Such an attitude will help a lot with moving forward in life."
    psy.name "And I know you had your first mission. Do you mind telling me how that went?"
    if main_quest_01.missionvar1 == True:
        jump main_quest_02_psychologist_passed
    else:
        jump main_quest_02_psychologist_failed





label main_quest_02_psychologist_passed:
    pc "Well, I got the info that they wanted even though it was expected that I wouldn't."
    psy.name "And tell me how you managed to do that."
    pc "Tell you how?"
    psy.name "Yes. Knowing what you did and how you managed to convince [simon.name] to give you the information that [tucker.name] asked you to get will allow me to better know what missions to recommend or allow you on."
    pc "Allow me on?"
    psy.name "Well yes. Certain missions require certain abilities or skills. Some people might use violence or intimidation, others may use cunning or deceit."
    psy.name "Depending on what methods you are comfortable with will determine what situations I can allow you to get into."
    pc "So you want to know everything...?"
    psy.name "It would be very helpful."
    pc "..."

    menu:
        "Tell the truth":
            if "sex_branch" in main_quest_01.list:
                jump main_quest_02_psychologist_truth_sex
            elif "intimidate_branch" in main_quest_01.list:
                jump main_quest_02_psychologist_truth_intimidate
            elif "waitress_branch" in main_quest_01.list:
                jump main_quest_02_psychologist_truth_waitress
            else:
                jump main_quest_02_psychologist_truth_wait
        "Avoid the details":
            if "sex_branch" in main_quest_01.list:
                jump main_quest_02_psychologist_lie_sex
            elif "intimidate_branch" in main_quest_01.list:
                jump main_quest_02_psychologist_lie_intimidate
            elif "waitress_branch" in main_quest_01.list:
                jump main_quest_02_psychologist_lie_waitress
            else:
                jump main_quest_02_psychologist_lie_wait





label main_quest_02_psychologist_lie_sex:
    pc "Well, what is there to say? I made use of the body I was given."
    psy.name "You went that far?"
    pc "Isn't it what was expected of me? Seduce men into doing what I want from them? What The Institute wants from them?"
    psy.name "While it is one way, it doesn't need to be the only way."
    pc "Is the most direct way."
    jump main_quest_02_psychologist_wrapup

label main_quest_02_psychologist_lie_intimidate:
    pc "The Institute is powerful and scary. I took advantage of the weight behind them. Told him to tell me or he won't see the next person The Institute sends."
    psy.name "..."
    if "intimidate_branch_pass_intimidate" in main_quest_01.list:
        pc "Worked and job done. He gave me his bag with all the info and left."
    else:
        pc "Didn't quite work out though and he demanded I fuck him in return for the info."
    psy.name "..."
    jump main_quest_02_psychologist_wrapup

label main_quest_02_psychologist_lie_waitress:
    pc "I had worked the bar before, so I dressed up in my uniform, brought him a beer and had a chat with him."
    if "waitress_branch_pass_convince" in main_quest_01.list:
        pc "People are pretty quick to trust a barmaid so he spilled the info without much need to convince him."
    else:
        pc "He was tight lipped though and eventually cottoned on to who I was. Well, who sent me anyway."
        if "bob_mission_accepted" in main_quest_01.list:
            pc "But he offered me to help him out with his own job and he would give up what I was after."
            pc "I helped him out and got the job done."
            jump main_quest_02_psychologist_wrapup
        else:
            pc "So he suggested we play a game. One truthful answer to a question in return for my clothes."
            jump main_quest_02_psychologist_lie_wait_catcher

label main_quest_02_psychologist_lie_wait:
    pc "Well, what is there to say? After I had some drinks in the pub, he bought me something so I went over and talked with him."
    pc "He was aware the moment I entered I was after him. But he also noticed I was inexperienced and he took advantage of that."
    pc "He suggested a game. I take off a piece of clothing and he will answer a question."
label main_quest_02_psychologist_lie_wait_catcher:
    psy.name "And you agreed?"
    menu:
        "I wanted to get the info and earn The Institute's trust":
            $ player.add_conf(5)
        "It was the price to pay for the info":

            $ player.add_conf(5)
        "I thought it would be kinda fun":

            $ player.add_conf(10)

    if not simon.naked:
        pc "In the end, I was able to get the info needed before stripping fully. And since I won the game he gave me all his notes."
        pc "So he gave me his bag and after a quick chat about what was in his notes, he left and I went home to sleep off the booze."
    else:

        pc "But either the booze or him outsmarting me made me ask dumb questions. I ended up naked in the alleyway without getting much info out of him."
        pc "He then said if I got him off, he would hand over everything..."


        if not simon.naughty:
            pc "I refused."
            pc "But then he told me that he has had so much fun, he will give me the bag anyway. After a quick chat about what was in his notes, he left and I went home to sleep off the booze."
            jump main_quest_02_psychologist_wrapup


        $ temp_var_1 = player.vsex + player.asex + player.hsex + player.osex
        if temp_var_1 >= 20:
            pc "I have been with my fair share of men so it's not like it was an unfamiliar situation for me. So I gave him what he wanted and he happily handed over his bag."
            jump main_quest_02_psychologist_wrapup


        elif simon.vsex > 0:
            pc "Things ended up getting fairly heated and then he gave me his bag and left."
            jump main_quest_02_psychologist_wrapup


        elif simon.osex > 0:
            pc "I ended up... Pleasing him, he handed over his bag and that's the end of it."
            jump main_quest_02_psychologist_wrapup
        else:


            pc "He got himself off, handed over his bag and left."
            jump main_quest_02_psychologist_wrapup





label main_quest_02_psychologist_truth_sex:
    pc "Well... I thought I would just use a direct method to convince him to give me what I wanted."
    psy.name "And what would that be."
    pc "Show him I am available in return for him telling me what he was up to."
    psy.name "Available?"
    pc "Sex."
    psy.name "Oh?"
    pc "I made it clear from the start I would make him happy if he told me what he was up to."
    psy.name "Well... Did it work?"
    if "sex_branch_reject" in main_quest_01.list:
        pc "Yes and no."
        pc "He was up for it and agreed to give the info if I pleased him..."
        pc "In the end though I didn't go through with it."
        pc "Not entirely sure why. Would have been the easiest way to get it all over and done with."
        psy.name "Oh? But you managed to get everything in the end. How did that happen?"
        pc "Not even sure myself. I thought I would drown my misery in a beer and he just came up to me afterwards."
        pc "Handed me his bag with his papers in it and left."
        pc "Claimed my pretty smile convinced him."
        psy.name "Well that is surprising."
        pc "I am guessing he realised he didn't really have a hand to play against The Institute so just gave it up to get them off his back."
        jump main_quest_02_psychologist_wrapup
    elif "sex_branch_gameoffer" in main_quest_01.list:
        pc "I couldn't go through with it so not really."
        pc "But he was still open to alternative deals and suggested we play a game."
        jump main_quest_02_psychologist_truth_game_catcher
    else:
        if "sex_branch_buttjob" in main_quest_01.list:
            pc "Errr..."
            pc "I tried to negotiate him down."
            pc "First he offered me to give him a blowjob, but I refused that."
            pc "He then commented he won't give up the info unless I at least give him something to be happy about."
            pc "Suggested that I undress for him and let him wank while looking at me."
            psy.name "You agreed?"
            pc "Well, he was right. Can't just walk up and ask him for the info. Had to give him something in return."
            psy.name "And how did that turn out?"
            if simon.sex:
                pc "Errr..."
                psy.name "Something happen."
                pc "Well, I wasn't willing to have sex with him for the info..."
                pc "But..."
                pc "Hmmm..."
                pc "I liked what he was doing. I had fun with him touching me while wanking."
                pc "So when he poked between my legs, I let him."
                pc "I fucked him just for the fun of it."
                psy.name "Oh? Interesting."
            else:
                pc "Fine I guess. He wanked off on my arse, came over me and was more than happy with the outcome."
            pc "Afterwards, he held up his end of the deal and gave me his bag with all the info in it."
            jump main_quest_02_psychologist_wrapup
        elif simon.sex:
            pc "Yes..."
            pc "We went to the toilet, had sex and he gave me everything I wanted."
        elif simon.osex:
            pc "Kind of. I negotiated him down to a blowjob. After that he gave me everything I wanted."
        psy.name "And how do you feel having done that?"
        if simon.vvirgin:
            pc "Dunno. My first time should maybe have been more romantic I guess."
        elif player.iswhore:
            pc "Not like I haven't had sex for something in return before. So I guess fine."
        elif player.sold:
            pc "Well..."
            pc "It wasn't my first time... Errr, exchanging... Things..."
        elif player.isslut:
            pc "Got the info and fucked at the same time. Win win as far as I am concerned."
        psy.name "And that was everything?"
        if "bob_mission_accepted" in main_quest_01.list:
            pc "Not quite..."
            jump main_quest_02_psychologist_truth_bob_mission
        else:
            pc "Yeah. Ended up going smoother than I expected. Was actually surprised with myself."
            jump main_quest_02_psychologist_wrapup


label main_quest_02_psychologist_truth_intimidate:
    pc "Well, I thought I would leverage the \"intimidation factor\" of The Institute."
    pc "Walked straight up to him and pretty much asked him what he was up to."
    pc "Might have implied that having him killed would be a nice and easy solution to him poking his nose around."
    psy.name "Wow. Okay... How did that go?"
    if "intimidate_branch_pass_intimidate" in main_quest_01.list:
        pc "He bought it. Handed everything he knew over to me."
        psy.name "Oh? And that was it?"
        if "bob_mission_accepted" in main_quest_01.list:
            pc "Not quite..."
            jump main_quest_02_psychologist_truth_bob_mission
        else:
            pc "Yeah. Ended up going smoother than I expected. Was actually surprised with myself."
            jump main_quest_02_psychologist_wrapup
    else:
        pc "He didn't buy it. Or he called my bluff. Either way he wasn't giving up what he had."
        pc "He pretty much told me since I had been a bit of a cunt to him, I can apologise by fucking him."
        psy.name "And did you?"
        pc "Yes. It was that or leave empty handed."
        psy.name "You could have left empty handed."
        pc "I know..."
        jump main_quest_02_psychologist_wrapup

label main_quest_02_psychologist_truth_waitress:
    pc "Well, I have actually been working in the pub before. So I was pretty familiar with the place."
    psy.name "Oh? That must have made things a lot easier."
    pc "It did. I dressed in my bar uniform and served him a beer and struck up a conversation with him."
    psy.name "That's pretty good. How did it go?"
    if "waitress_branch_pass_convince" in main_quest_01.list:
        pc "Pretty well. I commented most people are busy trying to look up our skirts, but his eyes are elsewhere. So what's bothering him."
        pc "He told me he was a P.I. and asked what I knew about some guy over the other side of the pub. Didn't know at the time he worked in the hospital."
        pc "Told him I would ask around and he told me why he was looking into [bob.name]. Turned out [simon.name] had no interest in The Institute after all."
        if "bob_mission_accepted" in main_quest_01.list:
            pc "But then he offered me a job."
            psy.name "He offered you a job?"
            jump main_quest_02_psychologist_truth_bob_mission
        pc "That was pretty much it. I got changed and left. Pretty easy in the end."
        jump main_quest_02_psychologist_wrapup
    else:
        pc "Not too well. He wasn't very interested in talking."
        pc "I wasn't too sure what to do at that point, so thought I would wait for him to drink his drink so I could bring him a new one and try again."
        pc "Turns out he was watching me watch him. He knew something was up, so when I went to top him up he pulled me up on it."
        psy.name "But you still got the job done, so what happened?"
        if "bob_mission_accepted" in main_quest_01.list:
            pc "Well, reason he wasn't looking up the girls skirts is because he was investigating [bob.name] who works at the hospital."
            pc "We had a chat and in the end he asked me to help him out."
            psy.name "Help him out?"
            jump main_quest_02_psychologist_truth_bob_mission
        else:
            pc "[simon.name] seemed willing to part with the info if we played a game together."
            jump main_quest_02_psychologist_truth_game_catcher


label main_quest_02_psychologist_truth_wait:
    pc "Well, I didn't really know what to do. Going to the pub like that alone. So I just sat nearby and waited for a chance to get close to him."
    pc "I spent quite some time waiting and ended up having a few drinks while I was there. Can't be sitting in a pub with an empty glass."
    pc "In the end it was [simon.name] buying me a drink that gave me an excuse to talk to him. It seems he knew right away I was looking for him but he didn't really know why."
    pc "I felt that at that point, telling him lies would make him just go away, so I told him the truth and directly asked him what he was up to. He asked to play a game with me in return for his notes in his bag."
label main_quest_02_psychologist_truth_game_catcher:
    psy.name "And what kind of game did he want to play?"
    pc "He wanted me to strip while asking him questions. One question for one piece of clothing."
    psy.name "And you agreed?"
    if player.has_perk(perk_exhibitionist):
        pc "Sure. Playing strip games are fun."
    else:
        menu:
            "I wanted to get the info and earn The Institutes trust":
                $ player.add_conf(5)
            "It was the price to pay for the info":

                $ player.add_conf(5)
            "I thought it would be kinda fun":

                $ player.add_conf(10)

    if not simon.naked:
        pc "In the end, I was able to get the info needed before stripping fully. And since I won the game he gave me all his notes."
        pc "So he gave me his bag and after a quick chat about what was in his notes, he left and I went home to sleep off the booze."
    else:




        pc "In the end though he answered everything very directly and my questions weren't enough to get what I needed."
        psy.name "So you ended up stripping fully?"
        pc "Yes, I was standing there with my arse out when he made a proposal. Basically if I got him off he would hand over the bag."


        if simon.sold:
            pc "I refused."
            pc "But then he told me that he has had so much fun, he will give me the bag anyway. "
            psy.name "And that was it?"
            jump main_quest_02_psychologist_truth_bob_mission


        if not simon.naughty:
            pc "I refused."
            pc "But then he told me that he has had so much fun, he will give me the bag anyway. After a quick chat about what was in his notes, he left and I went home to sleep off the booze."
            jump main_quest_02_psychologist_wrapup


        elif simon.rape > 0:
            pc "I agreed to let him touch himself while groping me..."
            pc "But then in the end..."
            pc "He pushed too far and raped me."
            pc "..."
            pc "After he got what he wanted, he left his bag on the floor and left."
            if player.pregnancy >= 2:
                psy.name "Oh... The baby you are carrying...?"
                if simon.fullname in player.father:
                    if simon.vvirgin == True:
                        pc "Yes, he took my virginity and left his baby in me."
                    else:
                        pc "Yes, the baby is his..."
                else:
                    pc "No, this one isn't his."
            else:
                psy.name "Oh... Should I arrange a test for you?"
                pc "Test?"
                psy.name "A pregnancy test."
                pc "No, I will deal with that myself."

            psy.name "Ok..."
            if t.day > 10:
                pc "I think that's enough talking about this. I was warned it would happen by my sister, at school and by most of the schoolgirls. Let a guy near you and they will fuck you."
            else:
                pc "I think that's enough talking about this. I was warned it would happen by my sister. Let a guy near you and they will fuck you."
            pc "So I pretty much expected it would happen even as I was letting him touch me. It was a price I was willing to pay for the info it seems."
            jump main_quest_02_psychologist_wrapup


        if (player.vsex + player.asex + player.hsex + player.osex) >= 20:
            pc "I have been with my fair share of men so it's not like it was an unfamiliar situation for me. So I gave him what he wanted and he happily handed over his bag."
            jump main_quest_02_psychologist_wrapup


        elif simon.vsex > 0:
            pc "He asked me to turn around and he would jerk off while touching my bum."
            psy.name "And is that what happened?"
            pc "No, at some point he started to poke me with his cock... You know... Down there..."
            pc "If felt pretty nice and I ended up letting him poke deeper and deeper until he was fucking me in the alleyway."
            psy.name "How do you feel about having done that?"
            if simon.vvirgin == True:
                pc "Well, In hindsight I should have probably lost my virginity in a more romantic way than fucked in an alleyway by someone like him."
            else:
                pc "Kinda mixed feelings. Getting fucked in an alleyway is one of the least romantic things I can imagine."
            if simon.fullname in player.father and (player.pregnancy > 1 or player.preg_knows == True):
                pc "And letting him get me pregnant was probably a horrible thing to allow."
            pc "But at the time I was enjoying myself despite knowing I was there just for the mission. So I guess it wasn't all bad."
            jump main_quest_02_psychologist_wrapup










        elif simon.hsex:
            if player.male_origin:
                pc "He asked me to start masturbating him. Felt a bit awkward at first but I suppose it's like riding a bike. He seemed to quite enjoy it."
            else:
                pc "He asked me to start masturbating him. Not something I really wanted to be doing in an alleyway but just went along with it anyway."
            if simon.osex:
                pc "He then guided me down getting me to start giving him a blowjob."
                if player.male_origin:
                    pc "This was something I was not at all familiar with. I didn't really know how to... Do it... So I just mimicked what I saw the girls do in porn."
            else:
                pc "He then guided me down trying to get me to start giving him a blowjob. But, I didn't go along with his plan and just finished him off with my hand."
            if simon.swallow:
                pc "Eventually he came in my mouth. As I was thinking about what to do next he happily give me all the stuff from his bag."
                pc "After a quick chat about what was in his notes, he left and I went home to sleep off the booze."
            elif simon.facial:
                pc "Eventually he ended up cumming all over my face. As I was thinking about what to do next he happily give me all the stuff from his bag."
                pc "After a quick chat about what was in his notes, he left and I went home to sleep off the booze."
            else:
                pc "Eventually he came and seemed happy enough to give me all the stuff from his bag."
                pc "After a quick chat about what was in his notes, he left and I went home to sleep off the booze."
            jump main_quest_02_psychologist_wrapup
        else:


            pc "He asked me to turn around and he would jerk off while touching my bum."
            psy.name "And is that what happened?"
            pc "Pretty much. He did try to poke at me. If I had gave him some leeway I most likely would have ended up getting fucked in the alley. But I made sure to keep him in check."
            if player.preg_father_class == simon and player.preg_knows:
                if player.vvirgin:
                    pc "What I didn't realise is that it doesn't require full penetration to end up pregnant. So here I am, still a virgin but with a baby growing inside me."
                else:
                    pc "What I didn't realise is that it doesn't require full penetration to end up pregnant. So here I am, not having had sex with [simon.name] but still with his baby growing inside me."
            else:
                pc "He ended up coming on my ass and spoiling my pants. But he seemed happy enough with the outcome and gave me his notes. After a quick chat about what was in his notes, he left and I went home to sleep off the booze."
            jump main_quest_02_psychologist_wrapup





label main_quest_02_psychologist_truth_bob_mission:
    pc "Well, [simon.name] was investigating [bob.name]. He... Asked for help getting his job done."
    psy.name "Hmm. How so?"
    pc "He offered me money to get close to [bob.name] so he could get some photos of us together."
    psy.name "You were investigating him and he ended up asking you for help? Did you accept?"
    if "stole_money" in main_quest_01.list:
        $ player.face_worried()
        pc "Kindof..."
        pc "In a way..."
        psy.name "Hmmm. No need to hesitate."
        $ player.face_neutral()
        pc "I told him I would do it and took his money."
        pc "But then left the pub with his money."
        psy.name "Pffft! Really?"
        pc "Yeah... I had the info and his money. He is trying to screw someone over so I didn't feel too bad just fucking off with it."
        pc "Plus thought [tucker.name] wouldn't be too upset since it was kind of protecting someone from The Institute."
        psy.name "Well that is a surprise."
        psy.name "Well, [bob.name] isn't really from The Institute. He works for the hospital."
        pc "Same thing isn't it?"
        psy.name "Not at all. The Institute was in charge of the black projects and the hospital was a cover. Only a fraction of people working at the hospital knew about The Institute prior to..."
        psy.name "Well, you know."
        psy.name "Even now most people just assume it's upper management and are unaware of who we really are."
        pc "Well, good to know. Won't have [tucker.name] being upset with me for doing it."
        jump main_quest_02_psychologist_wrapup
    else:
        pc "Yeah. He was offering decent money. Just wasn't sure if doing so was going against The Institutes interests."
        psy.name "Well, [bob.name] isn't really from The Institute. He works for the hospital."
        pc "Same thing isn't it?"
        psy.name "Not at all. The Institute was in charge of the black projects and the hospital was a cover. Only a fraction of people working at the hospital knew about The Institute prior to..."
        psy.name "Well, you know."
        psy.name "Even now most people just assume it's upper management and are unaware of who we really are."
        pc "Hmm, so they probably don't care what happens to [bob.name]..."
        psy.name "Well, people who work for the hospital are always valued. But The Institute won't step in to solve personal issues for a paper pusher."
        pc "Hmmm."
        psy.name "So what happened with [bob.name]?"
        if "bobsex_waitress" in main_quest_01.list:
            if "waitress_branch" in main_quest_01.list:
                pc "Well, I was already dressed as a waitress so used that to get close to him."
            else:
                pc "I needed to get close to him so I changed into my waitress uniform and used that."
            pc "Brought him some beers to get close to him and started chatting to him."
            psy.name "He didn't think anything strange, a waitress coming to chat to him?"
            pc "Err..."
            pc "..."
            psy.name "There is something else?"
            pc "You don't know anything about the pub do you?"
            psy.name "No, I have never been there."
            if pub_waitress.sold > 5:
                pc "We make some extra income providing extra services. It's pretty well understood by most of the people drinking there."
            elif pub_waitress.sold:
                pc "It's... Not uncommon to give extra services."
            else:
                pc "Some of the girls there give extra services to the customers."
            psy.name "Extra services?"
            pc "Whoring."
            psy.name "Oh... Okaaay. I did not know that."
            psy.name "So going up to someone to chat is a common thing?"
            pc "Pretty much. No one would find it strange. So I just took some beers, chatted with him then sat on his lap."
            psy.name "How did that make you feel?"
            pc "Wasn't the first pub pervert's lap I've sat on and probably won't be the last."
            psy.name "..."
            psy.name "And was that all you did?"

            if "bobsex_waitress_nopants" in main_quest_01.list:
                pc "Errr. Yes?"
                psy.name "Hmmm. There is something more?"
                pc "Errm..."
                pc "Well, when I changed into my work uniform. It kind of didn't have any underwear. They tend to get bought a lot while working."
                pc "So yes, I stayed on his lap..."
                pc "While he took his trousers off..."
                psy.name "In the middle of the pub?"
                pc "Err. Not entirely an uncommon sight."
                psy.name "Right..."
                psy.name "I didn't realise the pub was that kind of place."
                pc "Every place in [town] is that kind of place."
                pc "I'm guessing you don't get out much."
                psy.name "No... I don't."

                if bob.sex:
                    pc "Well anyway. I sat on him and we continued..."
                    psy.name "I thought you were already sitting on him."
                    pc "I \"sat\" on him."
                    psy.name "I don't get it."
                    if bob.vsex:
                        pc "I stood up a bit while still straddling him, he poked his cock between my legs and I sat back down."
                    else:
                        pc "I stood up a bit while still straddling him, he poked his cock at my arse and I sat back down."
                        psy.name "Wait. Arse?"
                        pc "Yes. Only form of birth control these days."
                    psy.name "Oh... Okay."
                    pc "Well, anyway. Once we finished up, I went and changed, met [simon.name] to make sure he got the photos and left."
                    jump main_quest_02_psychologist_wrapup
                elif bob.naughty:
                    pc "Anyway, just before he was able to put it inside me, I realised that I already met [simon.name]'s needs."
                    pc "He asked me for a shot of the two of us and his cock in frame. And his cock was between my legs on full display."
                    pc "So I told [bob.name] I was done, jumped up and ended it."
                    pc "Changed out of my uniform, met [simon.name] to make sure he was able to get the photos and left."
                    jump main_quest_02_psychologist_wrapup
                else:
                    pc "Well, before things went too far, I called it quits and headed off."
                    psy.name "He didn't have a problem with that?"
                    pc "No, just some company is enough for these perverts. The rarely get clingy."
                    psy.name "And [simon.name] was okay with that?"
                    pc "Sure, might not have got his cock in the shot but they were still steamy."
                    jump main_quest_02_psychologist_wrapup
            else:
                pc "No. I needed to do more to get what [simon.name] was after. Since time was getting on, I talked really dirty in [bob.name]'s ear and offered him a fun time."
                pc "No one in the pub would refuse such an offer, so we went to the toilets together."
                pc "I knew [simon.name] would need to put his phone over the stall to get photos. So I kept [bob.name]'s attention down low."
                psy.name "Hmmm?"
                pc "I got on my knees and sucked his cock."
                psy.name "Oh?"
                if not bob.sex:
                    pc "I went at it for a while, [bob.name] came and that was job done. I changed, met [simon.name] to make sure everything was good and went home."
                else:
                    pc "But..."
                    pc "I was enjoying myself there strangely enough."
                    pc "I asked [bob.name] if he wanted to go further. Of course he didn't refuse."
                    pc "So ended up having sex with him as well in the toilet."
                    psy.name "You were enjoying yourself?"
                    pc "Yes. Is that so shocking?"
                    psy.name "A little. I thought it would be purely professional."
                    pc "It was. Doesn't mean you can't also have fun."
                    psy.name "Hmmm..."
                    pc "Anyway. Once we finished up, I changed and looked for [simon.name] to make sure he got the shots he needed and left."
                jump main_quest_02_psychologist_wrapup
        else:

            pc "I needed to somehow get close to him. I kind of lied to him and told him I had seen him around the hospital while working there."
            pc "I told him I didn't want to be a lone girl in the pub and if I could drink with him. He was more than happy to have the company."
            psy.name "How did it go?"
            pc "Quite well actually. [bob.name] was good company and I ended up having a nice evening with him."
            psy.name "Did you go through with getting the pictures?"
            pc "I did..."
            psy.name "But?"
            pc "I'm not even sure at that point if I went off alone with him because of the job or just because it was a nice way to end the evening I had with him."
            pc "Suppose it could have been both..."
            pc "He wasn't even up for it at first. Said he didn't want to take advantage of a young drunk girl and I could go home to sleep off the booze."
            psy.name "Oh? Wasn't expecting that?"
            pc "Pub is full of perverts and no doubt [bob.name] included. But I guess when you are with your young work colleague, maybe it's a little different."
            pc "It's fine ogling the barmaids who make money off of it, but a normal girl who just wanted to drink away the shit day is different I suppose."
            psy.name "So what did you do."
            pc "Took him by the hand and dragged him off so we could be alone."
            pc "Once alone I threw myself at him and couldn't get his clothes off quick enough."
            pc "I didn't even think much about the photos at that point and just did what I wanted to do."
            pc "But even though I did enjoy myself, once it was all done, I told him goodbye and sent him back in the pub while I met with [simon.name]."
            pc "He managed to get the photos he wanted and we said our goodbyes."
            if "simon_whore_offer" in main_quest_01.list:
                pc "Although..."
                psy.name "Something happen?"
                pc "Yeah..."
                pc "Just as [simon.name] was leaving, he made a comment."
                psy.name "About what?"
                pc "About enjoying the show and that he will stop off by the highway."
                psy.name "Ok. What would he do there?"
                pc "It's most people's way of saying they are going to find a whore to have sex with."
                psy.name "Oh? What did that have to do with you?"
                pc "I kind of offered to save him the journey..."
                psy.name "I don't understand."
                pc "I told him if he doubled my money, he could have me."
                psy.name "Ohhh..."
                pc "He didn't last long. My performance had him already wound up and it was over almost before it began."
                pc "But he was happy and paid up, so all good I suppose."
            jump main_quest_02_psychologist_wrapup





label main_quest_02_psychologist_wrapup:
    psy.name "Well, you did what you needed to do to get the mission done. It is an admirable trait and one that will be of huge benefit in future missions."
    if "bob_mission_accepted" in main_quest_01.list:
        psy.name "And what you did with [bob.name] I suppose shows your ability to adapt to a situation."
    if main_quest_01.sex:
        pc "What? You think future missions might require me to have sex with people again?"
    elif main_quest_01.naughty:
        pc "What? You think future missions might require me to use my body again?"
    else:
        pc "You think in future missions I might have to make use of my body?"
    psy.name "It's possible. You are a fixer. Fixers are required to do what's needed. Often very unpleasant things. As I mentioned before, some require violence or aggression. Others need other traits or qualities."
    psy.name "Someone as beautiful as you will no doubt have to make use of your allure on many occasions. It is a trait that many make use of. Combine that with how young you look, you can easily manipulate people."
    pc "I can?"
    if quest_homeless_start.active:
        psy.name "Why not? With [nik.name] supporting you, you can pass as whoever you might want to."
    else:
        psy.name "Easily. You weren't so young in your \"old\" life. Strictly speaking you and I are of a similar age. But this body of yours does not show that at all."
        psy.name "Your age here says 18, but looking at you, you could probably add or remove a few years on either side. That opens up a lot of possible personalities for you to use."
    psy.name "A dim witted diva, a naïve schoolgirl, a woman desperate to catch a husband, a stupid bimbo... Frankly the list is as long as my arm."
    pc "But that's not who I am."
    psy.name "But it can be. You do what you need to do to complete the mission. But you can also be {i}who{/i} you need to be. You just spoke to [nik.name], do you not understand the importance of being able to change yourself?"
    pc "Errr..."
    psy.name "If you are trying to get something from someone who has a liking for young blondes with big breasts, then that's who you become. Maybe someone wants a goth girl with tattoos, so off you go and get some tattoos, goth clothes and dark hair."
    psy.name "You become who you need to be to complete the mission."
    pc "Like putting on a mask?"
    psy.name "Precisely. Put on a mask with a persona and act out like that person would."
    psy.name "And compartmentalise. You are you, [fname] [sname]. But when on missions you are no longer [fname], instead you are whoever you need to be."
    pc "So I am [name] while living my daily life. But \"The Fixer\" when working? Hmmm, sounds like a plan. I will give it a go."
    psy.name "Wonderful. And if you need to talk further then feel free to come and give me a visit. I will make time in my schedule to see you."
    pc "Sounds good. Goodbye."
    psy.name "Goodbye Miss [sname]."

    hide brooker
    $ relax(60)
    jump main_quest_02_final





label main_quest_02_psychologist_failed:
    pc "Well, honestly. It was a bit... Underwhelming."
    psy.name "Why would you say that?"
    pc "Well, I know it's just me overthinking things. But I imagined something more... Hmmm. Thrilling I suppose."
    pc "Like something out of a movie. A femme fatale from the old novels or something. I don't really know. Just more to it than there was."
    psy.name "Do you really think they would send you without any training on such a mission?"
    pc "Of course not, but it's still the kind of thing you first think about when people are telling you to get close to someone and gain intel from them. Like a spy."
    psy.name "Well it's not so far from the truth, but not for a training mission. You might yet have a chance to become the femme fatale you wanted to be."
    psy.name "There may be a lot asked of you in future missions."
    pc "What do you mean?"
    psy.name "I mean that you are in training to basically be a femme fatale as you so put it. But I will let [tucker.name] give you the full explanation on that. He has high hopes for you."
    pc "He does? Are you sure we are talking about the same person here?"
    psy.name "Haha. Yes he has. Although I imagine he would never admit it to you."
    psy.name "But I am glad your first mission went well. I just wanted to say hello and have a little chat with you as I am hopeful you will pay me a visit after your missions."
    psy.name "I am here to help you keep a good state of mind."
    pc "Hmm, we will see."
    psy.name "It was nice meeting you Miss [sname]."
    hide brooker
    $ relax(60)
    jump main_quest_02_final





label main_quest_02_final:
    $ walk(loc_hospital_lobby)
    with dissolve
    pc "Hmm, I suppose I have a lot to think about."
    show tucker at right1 with dissolve
    tucker.name "One session with the psychologist and you start talking to yourself?"
    pc "Ahh. [tucker.sname]?"
    tucker.name "[tucker.name] if you would."
    pc "Sorry. What are you doing sneaking up on me?"
    tucker.name "We still have something to talk about."
    $ player.face_worried()
    pc "Uff, more?"
    tucker.name "Yes, I still need to pay you. But we also need to have a fairly long chat so if you would prefer to do this another day then it's not a problem."
    pc "Ok, this sounds serious."
    tucker.name "It is, but don't be thinking your usual doom and gloom. There is nothing to worry about. I just need to fill you in on a lot of the details about what will be expected of you going forward."
    tucker.name "Come and pay me a visit when you are ready to have a chat."
    $ player.face_neutral()
    pc "Ok..."
    tucker.name "And [fname]"
    pc "Hmm?"
    tucker.name "Good work."
    hide tucker with dissolve
    $ main_quest_03.activate()
    $ main_quest_02.complete()
    $ log.assign("Becoming the Fixer")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
