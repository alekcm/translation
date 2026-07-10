init python:

    def ko_assault(weight=(5,20), who=None, quest=None):
        if who == None:
            who = rapist
        for _ in range(numgen(weight[0], weight[1])):
            player.sex_forced(who, quest)  
            player.spank()
            player.punch()
            if numgen(1,5) == 1:
                player.sex_anal(who, quest)
                player.sex_cum(who, "anal", quest)
            else:
                player.sex_vag(who, quest)
                if numgen(1,5) == 1:
                    player.sex_cum(who, "pullout", quest)
                else:
                    player.sex_cum(who, "inside", quest)
        player.sex_hideaction()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
