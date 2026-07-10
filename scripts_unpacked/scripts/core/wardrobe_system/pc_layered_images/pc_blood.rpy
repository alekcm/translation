image pc_cut_face_1 = im.Alpha("characters/pc/blood/cut_face.webp", 0.2)
image pc_cut_face_2 = im.Alpha("characters/pc/blood/cut_face.webp", 0.4)
image pc_cut_face_3 = im.Alpha("characters/pc/blood/cut_face.webp", 0.6)
image pc_cut_face_4 = im.Alpha("characters/pc/blood/cut_face.webp", 0.8)


layeredimage pc_blood_face:

    if blood.special == "haven": 
        "blood_haven"

    if blood.face == 1:
        "pc_cut_face_1"
    elif blood.face == 2:
        "pc_cut_face_2"
    elif blood.face == 3:
        "pc_cut_face_3"
    elif blood.face >= 4:
        "pc_cut_face_4"
    if blood.face > 4:
        "blood_face"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
