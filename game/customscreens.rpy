screen tips_screen:
    text "Ohh the creature."

screen attack_examine:
    imagebutton:
        sensitive examine_button_enabled 
        pos (1050, 450)
        focus_mask True
        idle "combat/examine.png"
        hover "combat/examine select.png"
        if full_examined == False:
            action Jump ("examine_first")
        else:
            action Jump ("examine_done")

    imagebutton:
        sensitive attack_button_enabled
        pos (250, 450)
        focus_mask True
        idle "combat/attack.png"
        hover "combat/attack select.png"
        if tutorial_done == False:
            action [Jump("combats"), Hide("attack_examine")]     
        else: 
            action [Jump("post_tutorial_combat"), Hide("attack_examine")]    
screen theBody:
   
    imagemap:
        ground "Background/longuevest.png"    
        hover "Background/vesthighlight.png"  
        hotspot (650, 459, 195, 203) action Jump ("body")
screen theBody2:
    imagemap:
        ground "Background/Body BG SC1.png"
        hover "Background/Body Part HL1.png"
        hotspot (225, 144, 381, 303) action [Play ("sound", "EyeTouch.mp3"), Jump ("eyes_body")]
        hotspot (326, 509, 258, 131) action [Play ("sound", "Neck.mp3"), Jump ("throat_body")]
        hotspot (587, 799, 454, 257) action [Play ("sound", "BodyTouch.mp3"), Jump ("torso_body")]
screen combat:

    add "combat/combat bg grayscale.png"


    add andrea_vera:
        pos (1200, 800)

        
    if flour_found:
        imagebutton:
            sensitive flour_found
            pos (0, 50)
            focus_mask True
            idle "combat/combat flr base.png"
            hover "combat/combat flr hl.png"
            selected_idle "combat/combat flr hl.png"
            selected (flour == True)
            action [ToggleVariable("flour"), SetVariable("arwselected", False), SetVariable("hmrselected", False), ToggleVariable ("something_selected")]
    imagebutton:
            sensitive enabled
            pos (0, 350)
            focus_mask True
            idle "combat/combat hmr base.png"
            hover "combat/combat hmr hl.png"    
            selected_idle "combat/combat hmr hl.png"  
            action [ToggleVariable("hmrselected"), SetVariable("arwselected", False), SetVariable("flour", False), ToggleVariable ("something_selected")]
            selected (hmrselected == True)

    imagebutton:
        sensitive enabled
        pos (0, 650)
        focus_mask True
        idle "combat/combat arw base.png"
        hover "combat/combat arw hl.png"    
        selected_idle "combat/combat arw hl.png"  
        action [ToggleVariable("arwselected"), SetVariable("hmrselected", False), SetVariable("flour", False), ToggleVariable ("something_selected")]
        selected (arwselected == True)




    imagebutton:
        sensitive paragon_enabled
        focus_mask True

        if invisible == False:
            if head_floured == True:
                idle "combat/paragon head flour.png"
                hover "combat/paragon head flour hl.png"
                selected_idle "combat/paragon head flour hl.png"
                
            else:
                idle "combat/paragon head base.png"
                hover "combat/paragon head base hl.png"
                selected_idle "combat/paragon head base hl.png"
        else: 
            idle "combat/paragon head invisible.png"
            hover "combat/paragon head invis hl.png"
            selected_idle "combat/paragon head invis hl.png"
        if something_selected == True:   
            if flour == True:
                action [SetVariable("invisible", False), SetVariable("head_floured", True), Jump("correct")]
            else:
                action Jump("wrong1")
        else: 
            action NullAction()
    imagebutton:
        sensitive paragon_enabled
        focus_mask True
        if invisible == False:
            if torso_floured == True:
                idle "combat/paragon torso flour.png"
                hover "combat/paragon torso flour hl.png"
                selected_idle "combat/paragon torso flour hl.png"
            
            else:
                idle "combat/paragon torso base.png"
                hover "combat/paragon torso base hl.png"
                selected_idle "combat/paragon torso base hl.png"
        else:
            idle "combat/paragon torso invis.png"
            hover "combat/paragon torso invis hl.png"
            selected_idle "combat/paragon invis hl.png"
        ##action ToggleVariable("blue_btn_selected", True,False)
        ##selected(blue_btn_selected)
        
        if something_selected == True:   
            if flour == True:
                action [SetVariable("invisible", False), SetVariable("torso_floured", True), Jump("correct")]
            else:
                action Jump("wrong1")
        else: 
            action NullAction()
        #if green_btn_selected:
            #       action Jump("incorrect")    

    imagebutton:
            sensitive paragon_enabled
            focus_mask True
            ##action NullAction()
            if invisible == False:
                if tail_floured == True:
                    idle "combat/paragon tail flour.png"
                    hover "combat/paragon tail flour hl.png"
                    if tailhmred == True:
                        idle "combat/paragon tail injured.png"
                        hover "combat/paragon tail injured hl.png"
                else:
                    idle "combat/paragon tail base.png"
                    hover "combat/paragon tail base hl.png"
            else:
                idle "combat/paragon tail invis.png"
                hover "combat/paragon tail invis hl.png"
                selected_idle "combat/paragon tail invis hl.png"
            ## action ToggleVariable("red_btn_selected", True, False)
            
            ##action NullAction()
            if flour == True:
                action [SetVariable("invisible", False), SetVariable("tail_floured", True), Jump("correct")]
            else:
                action NullAction()

                
            
            
            ## else:
                ##   action NullAction()
            ##   selected(red_btn_selected)
            ## if blue_btn_selected == True:
                
            #   if green_btn_selected:
            #      action Jump("incorrect")
                
            
        

screen combat2:

    add "combat/combat bg grayscale.png"
    add andrea_vera:
        pos (1200, 800)
    
        


    imagebutton:
            sensitive enabled
            pos (0, 350)
            focus_mask True
            idle "combat/combat hmr base.png"
            hover "combat/combat hmr hl.png"    
            selected_idle "combat/combat hmr hl.png"  
            action [ToggleVariable("hmrselected"), SetVariable("arwselected", False), SetVariable("flour", False), ToggleVariable ("something_selected")]
            selected (hmrselected == True)

    imagebutton:
        sensitive enabled
        pos (0, 650)
        focus_mask True
        idle "combat/combat arw base.png"
        hover "combat/combat arw hl.png"    
        selected_idle "combat/combat arw hl.png"  
        action [ToggleVariable("arwselected"), SetVariable("hmrselected", False), SetVariable("flour", False), ToggleVariable ("something_selected")]
        selected (arwselected == True)


    imagebutton:
        focus_mask True
        sensitive paragon_enabled
        if head_floured == True:
            idle "combat/paragon head flour.png"
            hover "combat/paragon head flour hl.png"
            selected_idle "combat/paragon head flour hl.png"
        else:
            idle "combat/paragon head base.png"
            hover "combat/paragon head base hl.png"
            selected_idle "combat/paragon head base hl.png"
        if something_selected == True:
            action Jump ("wrong2")
        else:
            action NullAction()
    imagebutton:
        focus_mask True
        sensitive paragon_enabled
        if torso_floured:
            idle "combat/paragon torso flour.png"
            hover "combat/paragon torso flour hl.png"
            selected_idle "combat/paragon torso flour hl.png"
        else: 
            idle "combat/paragon torso base.png"
            hover "combat/paragon torso base hl.png"
            selected_idle "combat/paragon base flour hl.png"
        if something_selected == True:
           action Jump ("wrong2")
        else:
            action NullAction()
        #if green_btn_selected:
            #       action Jump("incorrect")    

    imagebutton:
        
        sensitive paragon_enabled
        focus_mask True
 
        idle base_tail
        hover base_tail_hl
        selected_idle base_tail_hl
        action NullAction()
        
        if something_selected == True:
            if arwselected == True and tailhmred == True:
                action Jump("finishedcombat")
            if hmrselected == True and tailhmred == False:
                action [SetVariable("base_tail", "combat/paragon tail injured.png"), SetVariable ("base_tail_hl", "combat/paragon tail injured hl.png"), SetVariable("tailhmred", True), Jump("hit_tail")]
        
      ##  else:
        ##    action Jump("wrong2")
        
      
            

            

            

                
            

screen bathroomintro:
    imagemap:
        ground "Background/Bathroom/bathroom body items final.png"
        hover "Background/Bathroom/bathroom body hl hammer no hl tint.png"
        hotspot (508, 502, 361, 217) action Jump ("test_body")

screen bathroom1:
    imagemap:
        ground "Background/BathRoom/bathroom body items final.png"
        hover "Background/BathRoom/bathroom body only items hl.png" 
        hotspot (257, 184, 60, 138) action Jump ("shampoo")
        hotspot (1561, 219, 363, 215) action Jump ("towels")   
        hotspot (1517, 462, 258, 430) action Jump ("sledgehammer")
screen hotel_2:
    imagemap:
        ground "Background/bluehotelplain.png"
        hover "Background/bluehotelverahl(1).png"
        hotspot (1759, 460, 134, 85) action Jump ("crossword_puzzle")
        hotspot (186, 3, 171, 327) action Jump ("sight_see")
        hotspot (615, 221, 548, 244) action Jump ("wake_vera")
screen test2:
    modal False
    image "token_1(1).png"
screen crossword:
    
    add "Background/CrossWord/CrosswordUi.png"
    textbutton "Go Back":
        text_size 100
        xalign 0.2
        action Jump("hotel_2_stop")

    imagebutton:
        if box1Filled == True:
                sensitive False
        focus_mask True
        idle "Background/CrossWord/Down1.png"
        hover "Background/CrossWord/Down1Hover.png"
        insensitive "Background/CrossWord/1DownInsensitive.png"
        action [SetVariable("correctAnswer", "shrink"), Jump("type_in")]
    imagebutton:
        if box2Filled == True:
            sensitive False
        focus_mask True
        idle "Background/CrossWord/Down2.png"
        hover "Background/CrossWord/Down2Hover.png"
        insensitive "Background/CrossWord/FilledDown2.png"
        action [SetVariable("correctAnswer", "bohr"), Jump("type_in")]
    imagebutton:
        if box3DownFilled == True:
                sensitive False
        focus_mask True
        idle "Background/CrossWord/Down3.png"
        hover "Background/CrossWord/Down3Hover.png"
        insensitive "Background/CrossWord/3DownFilled.png"
        action [SetVariable("correctAnswer", "hope"), Jump("type_in")]
    imagebutton:
        if boxAcrossFilled == True:
                sensitive False
        focus_mask True
        idle "Background/CrossWord/Across1(1).png"
        hover "Background/CrossWord/AcrossHover.png"
        insensitive "Background/CrossWord/AcrossFilled.png"
        action [SetVariable("correctAnswer", "throwup"), Jump("type_in")]
    
    
        
screen cleaning_time:
    add "Background/BathRoom/full br no body no highlight final.png"
    if brush_grabbed == False:
        imagebutton:
            focus_mask True
            idle "Background/BathroomClean/mop map.png"
            hover "Background/BathroomClean/mop map hl.png"
            action Jump("brush_grab")
    if bleach_grabbed == False:
        imagebutton:
            focus_mask True
            idle "Background/BathroomClean/spray bottle map.png"
            hover "Background/BathroomClean/spray bottle hl.png"
            action Jump ("bleach_grab")
    if towels_grabbed == False:
        imagebutton:
            focus_mask True
            idle "Background/BathroomClean/towel map.png"
            hover "Background/BathroomClean/towel map hl.png"
            action Jump ("towels_grab")
       
screen hit_body:
    add "Background/BathRoom/bathroom body no hammer.png"
    if hammer_grabbed == False:
        imagebutton:
            focus_mask True
            idle "Background/justhammer.png"
            hover "Background/justhammerhl.png"
            action Jump ("hitBody")
init:
            $ timer_range = 0
            $ timer_jump = 0
            $ time = 0

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
screen countdown:
    timer 0.01 repeat True action If(time>0, true=SetVariable('time', time -0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.1 xmaximum  300 at alpha_dissolve


screen kill_him:
    imagemap:
        ground "Background/BathRoom/bathroom body no hammer.png"
        hover "Background/BathRoom/bathroom bg only body hl no hammer.png"
        hotspot (508, 502, 361, 217) action Jump ("smash_head")

####### VARIABLES
