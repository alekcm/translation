image pc_face_mood_flushed_layer:
    "pc_face_mood_flushed"
    matrixcolor OpacityMatrix(If(player.drunk > 100, 1, player.drunk / float(100)))
image pc_face_effect_pink:
    "pc_face_effect_2"
    matrixcolor OpacityMatrix(If((player.desire + player.drunk > 400) or (player.cover_breasts or player.cover_vagina), 1, (player.desire + player.drunk) / 4 / float(100)))
image pc_face_effect_sweat:
    "pc_face_effect_4"
    matrixcolor OpacityMatrix(If(player.hygiene < 50, ((100 - player.hygiene) / 2) / float(100), 0))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
