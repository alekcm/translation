layeredimage prepare_image:

    group ass:
        attribute ass "prepare_image_ass"

    group breasts:
        attribute breasts "prepare_image_breasts"

    group belly:
        attribute belly "prepare_image_belly"


layeredimage prepare_image_ass:
    always "prepare_ass"
    if tattoo.ass:
        "prepare_ass_tat"

layeredimage prepare_image_breasts:
    always "prepare_breasts"
    if tattoo.chest:
        "prepare_breasts_tat"
    if acc.nipring:
        "prepare_breasts_rings"

layeredimage prepare_image_belly:
    always "prepare_belly"
    if acc.navelring:
        "prepare_belly_ring"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
