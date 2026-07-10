image nikolas:
    "nikolas_base"
    function SpriteFocus("nik")

layeredimage brooker:
    at sprite_highlight("psy")
    if psy.heavy_preg:
        "brooker_preg2"
    elif psy.showing:
        "brooker_preg1"
    else:
        "brooker_preg0"

layeredimage nurse:
    at sprite_highlight("nurse")
    always "camilla_base"
    if nurse.heavy_preg:
        "camilla_preg2"
    elif nurse.showing:
        "camilla_preg1"

layeredimage receptionist:
    at sprite_highlight("receptionist")
    always "receptionist_base"
    if receptionist.heavy_preg:
        "receptionist_preg2"
    elif receptionist.showing:
        "receptionist_preg1"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
