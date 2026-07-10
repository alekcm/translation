image dance_dani_bench = LayeredImageProxy("dance_dani_bench_layered", Transform(xalign = (0.65)))

layeredimage dance_dani_bench_layered:

    always:
        "dance_dani_bench_base"

    group face:
        attribute neutral default:
            "dance_dani_bench_neutral"
        attribute happy:
            "dance_dani_bench_laugh"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
