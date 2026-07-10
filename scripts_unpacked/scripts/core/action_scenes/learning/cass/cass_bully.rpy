layeredimage cass_bully_blow:
    always "cass_bully_blow_base"
    if cass.days_pregnant > (global_pregnancy_length * 0.7):  
        "cass_bully_blow_preg"
layeredimage cass_bully_grope:
    always "cass_bully_grope_base"
    if cass.days_pregnant > (global_pregnancy_length * 0.7):
        "cass_bully_grope_preg"
layeredimage cass_bully_sex:
    always "cass_bully_sex_base"
    if cass.days_pregnant > (global_pregnancy_length * 0.7):
        "cass_bully_sex_preg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
