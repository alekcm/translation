init python:
    def rachel_exhib_stripping_hide():
        if t.hour > 20 and "is_stripping" in rachel.list and rachel_here(loc_school_gym) and not rachel_exhib_stripping_show():
            return True
        else:
            return False

    def rachel_exhib_stripping_show():
        if "show_stripping" in rachel.list and rachel_here(loc_school_gym) and (t.hour >= 21 or t.hour in night):
            return True
        else:
            return False

    def rachel_exhib_stripping_events_trigger():
        if "stripping_trigger" in rachel.list and t.day > rachel.dict["rachel_exhib_try"] and rachel_here(loc_school_gym) and t.hour >= 21 and loc(loc_school_gym) and renpy.has_label("rachel_talk_exhib_inside_talk_" + str(rachel.dict["rachel_exhib_inside_talk"])):
            return True
        else:
            return False

    def exhib_games_playgame(pc_last_played):
        rachel.dict["rachel_talk_exhib_games_played"] = t.hours_total
        rachel.dict["rachel_talk_exhib_games_chain"] += 1
        rachel.dict["rachel_talk_exhib_games_pc_last_played"] = pc_last_played

    def exhib_games_canplay():
        if (rachel.dict["rachel_talk_exhib_games_played"] + 6) <= t.hours_total:
            return True
        else:
            return False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
