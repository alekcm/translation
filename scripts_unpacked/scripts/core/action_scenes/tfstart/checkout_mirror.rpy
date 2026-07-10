




































































image checkput_mirror_bs_base:
    "pc_tfstart_checkout_mirror_bs_base"
    pants_primary_colour_transform()
image checkput_mirror_bs_lines:
    "pc_tfstart_checkout_mirror_bs_lines"
    pants_secondary_colour_transform()
image checkput_mirror_breifs:
    "pc_tfstart_checkout_mirror_breifs"
    pants_primary_colour_transform()
image checkput_mirror_thong:
    "pc_tfstart_checkout_mirror_thong"
    pants_primary_colour_transform()

layeredimage tfstart_checkout_mirror:

    always:
        "pc_tfstart_checkout_mirror"
    if c.pants == 1:
        "checkput_mirror_breifs"
    elif c.pants == 6:
        "checkput_mirror_bs_base"
    if c.pants == 9:
        "checkput_mirror_thong"
    if c.pants == 6:
        "checkput_mirror_bs_lines"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
