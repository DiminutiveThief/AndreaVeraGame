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

transform night_filter_less:
    matrixcolor BrightnessMatrix(-0.1) * TintMatrix ("#c0c8c9")
transform fade_in:
    alpha 0.0
    linear 0.5 alpha 1.0
define moving_out_left= MoveTransition(0.8, leave=offscreenleft)
define moving_out_right= MoveTransition(0.8, leave=offscreenright)
define moveinoutdissolve = ComposeTransition(Dissolve(0.7), before=moving_out_left, after=moving_out_right)
transform sprite_jump:
    # Moves up smoothly over 0.15 seconds
    easein 0.15 yoffset -35  
    # Falls back down smoothly over 0.15 seconds
    easeout 0.15 yoffset 0   
