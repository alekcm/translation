label mechanic_dez_sell:
    call screen inventory_junk_choice(dez.inv, choices=[item_scrap_ele, item_scrap_metal])
    dez.name "Good."
    hide dez with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
