transform vera_spot:
    xalign 0.1
    yalign 1.0

transform vera_car:
    xalign 0.9
    yalign 1.0

transform andrea_shotgun:
    xalign 0.8
    yalign 1.0

transform andrea_car:
    xalign -0.1
    xzoom -1.0
    yalign 1.0

transform night_filter:
    matrixcolor BrightnessMatrix(-0.1) * TintMatrix ("#7C8587")
transform alt_hotel:
    matrixcolor BrightnessMatrix(-0.13) * TintMatrix ("#eac0c0")

transform sprite_jump:
    # Moves up smoothly over 0.15 seconds
    easein 0.15 yoffset -35  
    # Falls back down smoothly over 0.15 seconds
    easeout 0.15 yoffset 0   