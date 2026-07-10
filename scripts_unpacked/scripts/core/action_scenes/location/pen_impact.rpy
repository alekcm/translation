image pen_imapct_1a = im.Flip("action/location/pen_impact_1.webp", vertical=True)
image pen_imapct_1b = im.Flip("action/location/pen_impact_1.webp", horizontal=True)




image pen_impact_loop:

    "pen_impact_1"
    0.02
    "pen_imapct_1a"
    0.02
    "pen_imapct_1b"
    0.02

    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
