# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define ab = Character("Andrea", callback = name_callback, cb_name = "andrea", color="#d63e0c")
define vl = Character("Vera", callback = name_callback, cb_name = "vera", color="#9cc7e4")
define sl =  Character("Sloane", callback = name_callback, cb_name = "sloane", color="#9cc7e4")
define w =  Character("Waiter")
define unknown =  Character("Burn", callback = name_callback, cb_name = "??", color="E0DEDE")
define dm = Character("Dominic")
image vera happy = At('testvera', sprite_highlight('vera'))
image andrea happy = At('testandrea', sprite_highlight('andrea'))
define al = Character("Alex")




  
layeredimage andrea:
    ##at sprite_highlight ('frances_unknown')
    at sprite_highlight ('andrea')
    group body:
        attribute body: 
            "images/Sprites/Andrea/andreahalfbodyreal.png"
    group face:
        attribute neutral:
            "images/Sprites/Andrea/AB Neutral.png"
        attribute happy:
            "images/Sprites/Andrea/AB Happy.png"
        attribute angry:
            "images/Sprites/Andrea/AB Angry.png"
        attribute sad:
            "images/Sprites/Andrea/AB Sad.png"
        attribute scared:
            "images/Sprites/Andrea/AB Scared.png"
        attribute offput:
            "images/Sprites/Andrea/AB Offput.png"
        attribute stern:
            "images/Sprites/Andrea/AB Stern.png"
        attribute offputEC:
            "images/Sprites/Andrea/AB Offput EC.png"
        attribute scaredEC:
            "images/Sprites/Andrea/AB Scared EC.png"
        attribute annoyed:
            "images/Sprites/Andrea/AB Annoyed.png"



layeredimage vera:
    ##at sprite_highlight ('frances_unknown')
    at sprite_highlight ('vera')
    group body:
        attribute body: 
            "images/Sprites/Vera/VL Halfbody Blank.png"
        attribute bodyflip:
            "images/Sprites/Vera/Flipped/vl halfbody flipped.png"
    group shirt:
        attribute shirt1:
            "images/Sprites/Vera/VL Shirt 1.png"
        attribute shirt2:
            "images/Sprites/Vera/VL Shirt 2.png"
        attribute shirt3:
            "images/Sprites/Vera/VL Shirt 3.png"
        attribute shirt1flip:
            "images/Sprites/Vera/Flipped/bikini bill flipped.png"
        attribute shirt2flip:
            "images/Sprites/Vera/Flipped/dcac flipped.png"
        attribute shirt3flip:
            "images/Sprites/Vera/Flipped/alice chained flipped.png"
    group expressions:
        attribute neutral:
            "images/Sprites/Vera/VL Neutral.png"
        attribute neutral2:
            "images/Sprites/Vera/VL Neutral2.png"
        attribute happy:
            "images/Sprites/Vera/VL Happy.png"
        attribute sad:
            "images/Sprites/Vera/VL Sad.png"
        attribute angry:
            "images/Sprites/Vera/VL Angry.png"
        attribute annoyed:
            "images/Sprites/Vera/VL Annoyed.png"
        attribute neutralflipped:
            "images/Sprites/Vera/Flipped/vl neutral 1 flipped.png"
        attribute neutral2flipped:
            "images/Sprites/Vera/Flipped/vl neutral 2 flipped.png"
        attribute happyflipped:
            "images/Sprites/Vera/Flipped/vl happy flipped.png"
        attribute sadflipped:
            "images/Sprites/Vera/Flipped/vl sad flipped.png"
        attribute angryflipped:
            "images/Sprites/Vera/Flipped/vl angry flipped.png"
        attribute annoyedflip:
            "images/Sprites/Vera/Flipped/vl annoyed flipped.png"

layeredimage sloane:
    ##at sprite_highlight ('frances_unknown')
    at sprite_highlight ('sloane')
    group body:
        attribute body: 
            "images/Sprites/Sloane/s base new.png"
    group face:
        attribute neutral:
            "images/Sprites/Sloane/s neutral new.png"
        attribute smile:
            "images/Sprites/Sloane/s smile new.png"
       
        attribute stern:
            "images/Sprites/Sloane/s stern new.png"
        attribute curious:
            "images/Sprites/Sloane/s curious new.png"
       
screen theBody:
   
    imagemap:
        ground "Background/longuevest.png"    
        hover "Background/vesthighlight.png"  
        hotspot (650, 459, 195, 203) action Jump ("body")
screen theBody2:
    imagemap:
        ground "Background/Body BG SC1.png"
        hover "Background/Body Part HL1.png"
        hotspot (225, 144, 381, 303) action Jump ("eyes_body")
        hotspot (326, 509, 258, 131) action Jump ("throat_body")
        hotspot (587, 799, 454, 257) action Jump ("torso_body")
default red_btn_selected = False
default blue_red_combine = False
default flour = False 
default head_floured = False
default torso_floured = False
default tail_floured = False
default invisible = False
default hmrselected = False
default arwselected = False

screen test:
    image "combat/av good.png":
        pos (300, 800)
        

    imagebutton:
            pos (0, 50)
            focus_mask True
            idle "combat/combat flr base.png"
            hover "combat/combat flr hl.png"
            action SetVariable("flour", True)
    imagebutton:
  
            pos (0, 350)
            focus_mask True
            idle "combat/combat hmr deselected.png"
            hover "combat/combat hmr hl.png"    
            ##selected_idle "combat/combat hmr hl.png"  
            action SetVariable("hmrselected", True)

    imagebutton:

        pos (0, 650)
        focus_mask True
        idle "combat/combat arw base.png"
        hover "combat/combat arw hl.png"    
        ##selected_idle "combat/combat hmr hl.png"  
        action SetVariable("arwselected", True)


    imagebutton:
        focus_mask True
    
        if invisible == False:
            if head_floured == True:
                idle "combat/paragon head flour.png"
                hover "combat/paragon head flour hl.png"
               # selected_idle "combat/paragon head flour hl.png"
            else:
                idle "combat/paragon head base.png"
                hover "combat/paragon head base hl.png"
               # selected_idle "combat/paragon head base hl.png"
        else: 
            idle "combat/paragon head invisible.png"
            hover "combat/paragon head invis hl.png"
           # selected_idle "combat/paragon head invis hl.png"
           
        if flour == True:
            action [SetVariable("invisible", False), SetVariable("head_floured", True)]
        else:
            action NullAction()
    imagebutton:
        focus_mask True
        if invisible == False:
            if torso_floured == True:
                idle "combat/paragon torso flour.png"
                hover "combat/paragon torso flour hl.png"
              #  selected_idle "combat/paragon torso flour hl.png"
            else:
                idle "combat/paragon torso base.png"
                hover "combat/paragon torso base hl.png"
               # selected_idle "combat/paragon torso base hl.png"
        else:
            idle "combat/paragon torso invis.png"
            hover "combat/paragon torso invis hl.png"
           # selected_idle "combat/paragon invis hl.png"
        ##action ToggleVariable("blue_btn_selected", True,False)
        ##selected(blue_btn_selected)
        if flour == True:
            action [SetVariable("invisible", False), SetVariable("torso_floured", True)]
        else:
            action NullAction()
        #if green_btn_selected:
            #       action Jump("incorrect")    

    imagebutton:
            focus_mask True
            ##action NullAction()
            if invisible == False:
                if tail_floured == True:
                    idle "combat/paragon tail flour.png"
                    hover "combat/paragon tail flour hl.png"
                else:
                    idle "combat/paragon tail base.png"
                    hover "combat/paragon tail base hl.png"
            else:
                idle "combat/paragon tail invis.png"
                hover "combat/paragon tail invis hl.png"
                selected_idle "combat/paragon tail invis hl.png"
            ## action ToggleVariable("red_btn_selected", True, False)
        
            if flour == True:
                action [SetVariable("invisible", False), SetVariable("tail_floured", True)]
            else:
                action NullAction()
         ##   selected(red_btn_selected)
         ## if blue_btn_selected == True:
                
            #   if green_btn_selected:
            #      action Jump("incorrect")
                
            
        



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
label start:
   ## default combat_round = 1

    default blue_btn_selected = False   
    stop music
    pause 2.0
    $ hammer_grabbed = False
    $ bleach_grabbed = False
    $ towels_grabbed = False
    $ brush_grabbed = False
    $ gatheredItems = 0    
    scene bathroom body items final
    stop music
    $ sanity = 2
    $ correctAnswer = "null"
    $ buttonClicked = "null"
    $ seenEyes = False
    $ seenThroat = False
    $ seenTorso = False
    $ box1Filled = False
    $ box2Filled = False
    $ box3DownFilled = False
    $ boxAcrossFilled = False
    $ boxesFilled = 0
    $ grabbedBlue = False

    
    play sound  "WaterDripHotel.mp3" loop
    "..."
    "..."
 
    call screen bathroomintro
    
    label test_body:
        
        hide screen bathroomintro
        scene body bg sc1

        if seenEyes == True and seenThroat == True and seenTorso == True:
            jump examinedBody
        call screen theBody2
    

    
    label body:
        "The soon-to-be-corpse isn't as bad as I expected him to be." 
        
        ##variables##
    
            

    label eyes_body:
        $ seenEyes = True
        "His eyes are still going back and forth like a circle of ants."
        "I'm sure the rest of his face wants to follow suit, but she got him good."
        "Right in the spinal column."
        "..."
        "Probably could've been faster about it, though, would've made the rest of him less messy."
        
        jump test_body

    label throat_body:
        $ seenThroat= True
        "This one was a close call."
        "She told me she just wanted to shut him up, but if it swelled up a bit more he'd probably have suffocated."
        
        jump test_body
        
    label torso_body:
        $ seenTorso = True
        "There's a clean shot just below the ribs."
        "A graze, but a deep one."
        "It's not bleeding anymore - she'd staunched the flow enough that it didn't kill him."
        
        jump test_body
    label examinedBody:
        hide screen theBody2
        scene bathroom body items final
        
        "...guh...Guh..."
        "The raised mass of burnt tissue around his throat quivers."
        "It sounds like ground meat being pressed through a narrow tunnel."
        show andrea body scared at left
        ab "{i}Fuck!{/i}"
        play sound "towelrackfall.mp3"
        "I stumble backwards into one of the towel racks, sending the crashing contents to the ground."
        "He isn't supposed to be able to do that."
        "She got him in the spinal cord ."
        "I stifle my rapid breath and avert my gaze from his to the rest of the room."
        "I can still feel it on me."
        $ soap_checked = False
        $ towels_checked = False
        label checkbathroom:
            call screen bathroom1
       
        
    label shampoo:
        play sound "BleachSwish.mp3"
        $ soap_checked = True
        "This place is too cheap to have any of those complimentary shampoo bottles, so we had to bring our own."
        "There's more heavy-duty stuff mixed in there, too."
        "Bleach, disinfectant, stain remover."
        jump checkbathroom
    label towels:
        play sound "TowelHold.mp3"
        $ towels_checked = True
        "The towels the motel provided are surprisingly alright. Looks like they've actually been cleaned."
        "It was still a good choice to bring our own, though."
        jump checkbathroom
    label sledgehammer:
        
        if soap_checked == True and towels_checked == True:
            hide screen bathroom1
            "You don't usually think of a sledgehammer as being super sophisticated, but this one's custom made."
            "It's long enough that I can get good momentum behind it, without putting too much strain on me. I opted for wood instead of steel - packs less of a punch, but the head makes up for it."
            "I've taken pride in keeping it clean. It's just as good as the day I got it."
            "I run my hands over the handle, feeling for the grooves I've worn in."
            "The weight sits evenly in my grasp but I can't find it in myself to be comforted"
            "I tighten my grip, then unclench it."
            "I turn to meet the gaze of the soon-to-be-corpse. It hasn't wavered, even if the gurgling has quieted down."
            "He threatens to slide farther into the bathtub, his head lolling against the wall."
            "Its head. Its head. Not his."
            "Its head."
            show andrea body sad at left
            "I stand up, willing my knees to comply."
            "His eyes–its eyes–the eyes of the soon-to-be corpse follow me all the way up."
            "This thing really is handy."
            "It's usually meant for breaking tiles or ice or construction–y'know, sledgehammer shit–but it's taken on way worse."
            "I've got a good swing by now. One shot's usually all I need to get the job done."
            "I draw back my arm and raise the hammer."
            "Try to raise it."
            "Can't raise it."
            "{i}Damn it.{/i} Move."
            "It's a nice hammer-a really good fucking hammer."
            "It's probably the best friend I have in this entire shitty motel."
            "If I spin it just right, it's doing the hard part for me."
            "Gives me a good few feet between me and what I have to do."
            "Handy thing."
            "..."
            "I'm going to throw up."
            "The wave of vertigo sends the sledgehammer to the floor and me scrambling out of the door."
            scene hotel1
            stop sound 
            play audio "DoorClose.mp3"
            "I clumsily throw it shut behind me."
            "My hand finds the wall, bracing me before I keel over."
            "The bile in my throat recedes into a roiling knot around my chest. My breaths come out sharp and spasmodic."
            "Out of the corner of my eye, the red glow of the digital clock sears into my brain."
            jump outofroom
        else:
            "There's other things to busy my eyes with right now."
            "..."
            jump checkbathroom
            
    label outofroom:
        
        play music "HotelAmbient.mp3" loop
        show andrea body scared at right
        "I can't see the time but I get the message."
        "I don't have time for this."
        show vera body shirt1 annoyed at left
        vl "Jesus, Andy."
        "Across the room, Vera looks over from her bed."
        vl "I heard something falling. What happened?"
        "I grit my teeth to try and get myself together enough to give an answer that I don't have to choke out."
        vl "Did you do it?"
        "Breathe in, breathe out. Things are happening how they happen: no amount of bush-beating's going to change that."
        "Just let it seep beneath the skin."
        ab "You {i}said{/i} you got his spinal cord."
        ab "He's-...it's still-"
        show andrea sad 
        "I bite my tongue before I let her hear the rest of the tremble in my voice."
        ab "It won't shut up."
        vl "So you {i}didn't{/i} do it."
        "Vera crosses her arms."
        show vera body shirt1 angry 
        vl "What the hell? It's been an hour."
        show andrea body angry 
        ab "I just need some air."  
        vl "You {i}need{/i} to get your shit together."
        vl "It doesn't have much left. Something's going to get infected sooner or later."
        "I turn away and begin rifling through the belongings strewn on the bed."
        "Water bottle, keys, jacket- ...There-jacket pocket."
        vl "What are you doing?"
        "I pull out the pack of cigarettes from inside and push one out."
        "It's the last of three. It's going to good use."
        show andrea body sad 
        ab "I told you. I need some air."
        vl "Don't be stupid; you can't leave."
        ab "I'm not going to leave."
        "I fish the lighter from the pocket and flick it to life."
        vl "You're stalling. Pussying around isn't going to make it any easier. You'll just have a hard reset when you get back to it."
        "The air turns bitter and I inhale a lungful of smoke. The burn feels more purging than acrid. My tension eases as much as my nerves will allow."
        vl "Are you listening to me?"
        ab "Vera. I just {i}need a minute{/i}."
        "I'll repeat it as many times as it takes for it to sink in-for the both of us."
        "Vera's right. Next time I go in there-turn the soon-to-be into the {i}is{/i}. It's just going to be more pungent."
        vl "Okay, {i}alright{/i}. Take your breather, whatever."
        vl "Just give me one of those."
        "Without waiting a breath, she reaches out and grabs the cigarette out of my hand."
        vl "Thanks for lighting it."
        show andrea body angry 
        ab "What the hell!"
        "I expect her to smile, but it looks like even she's tired. Can't even manage to be properly coy."
        "Good, I don't need to waste any more energy on her than I already have on."
        show vera body shirt1 neutral2 
        vl "It's my finder's fee."
        "She inhales, then cringes at the taste."
        show vera body shirt1 annoyed 
        vl "You're driving me to smoke, {i}Andy{/i}, look how far you've pushed me."
        "I swear under my breath and get out the next cigarette. Down to my last one."
        show andrea body sad 
        ab "Any signs of trouble while I was in there?"
        vl "No, no one's cracked the case in the last hour."
        vl "{i}But{/i}, that might change if you don't hur-"
        ab "I know."
        ab "I'll do it. I know."
        "The second cig doesn't hit the spot as much as the first, but it gives me something to do with my hands."
        vl "Sure."
        "There's a pause after that."
        "We both stare at the clock as the red morphs from two thirty-one to thirty-two."
        "The soon-to-be-corpse has been here for the better part of two hours-not that it'd know."
        "Or maybe he does. His ears should still work, probably would've overheard us."
        "Its ears..."
        "Its ears."
        show vera body shirt1 neutral 
        vl "You think this place has a fire alarm?"
        ab "I checked earlier. It's too cheap for that. We're screwed if it isn't."
        vl "That'd make sense. Just our luck, right?"
        vl "It's like a PSA. 'Don't smoke kids, or else you'll be busted for murder.'"
        "I manage a huff of laughter."
        show andrea body happy 
        ab "Dunno, maybe we could turn it around. Get this place on a healthcode violation."
        vl "I mean, it deserves it."
        show vera body shirt1 happy 
        vl "Violating lodging regulations {i}and{/i} harboring two felons."
        ab "Not felons yet-..."
        "She cuts me off."
        vl "Who in their right mind would check in?"
        "I try to find something to add. It burns up with the smoke."
        "I look at the clock, then at the door, then at Vera."
        "It's two thirty three, now." 
        show andrea sad 
        show vera body shirt1 neutral2 
        vl "...He {i}is{/i} a piece of shit, remember."
        "She crushes her cigarette out on the nighstand ashtray."
        vl "That girl he was chatting up. She looked like she was sixteen, max."
        vl "You know the type-dark and brooding drifter, new in town."
        vl "Catnip for stupid kids."
        ab "You said, yeah."
        "'Run-of-the-mill-power-high-creep', Vera had called him. 'Really trying to leverage that aura of mystery.'"
        vl "Anyone that misses him is either in on it or stupid."
        vl "They'd give you an award if they knew."
        ab "I get it."
        "She'd found him at a bar in town. We'd been on his trail for a while-more out of practicality than a real sense of justice."
        "I offered to go along but she'd said it'd just make things more difficult."
        "She's probably right."
        ab "Let me finish this and I'll finish it off."
        vl "Promise?"
        "It's not like I talked to the guy when she brought him in - out cold and stuffed in a duffle bag."
        "She could be lying for all I know. I wouldn't put it past Vera. Maybe this isn't some creep. Maybe he's some poor idiot fresh out of college, trying to find himself on a roadtrip."
        "I could press, but she could lie. It's routine."
        "It's easier like this. I can indulge in whatever peace it gives me."
        ab "Yeah, promise."
        "I manage to extend the cig's lifespan a few more minutes, before it's basically a stub. I twist it down on the ashtray."
        vl "Be my guest, I'll start packing."
        "She doesn't offer to come with me and I'm sure as hell not going to ask."
        "I extricate myself from the bed. Moving comes easier this time."
        "It'll be over in the next five minutes. You can handle anything for five minutes."
        play sound "DoorOpen.mp3" volume 1.3
        label kill_guy:
            stop music
            scene fullbathroomim1
            "I pull open the bathroom door."
            play sound "WaterDripHotel.mp3" loop
            "The soon-to-be-corpse's eyes are on me immediately. It's been looking in anticipation."
            "They're spiderwebbed with red, but no tears- thank God."
            "The hammer is where I left it, the malaise in the air coating it like rust."
            "It clings to me like a swarm of gnats. A buzz that works its way under my skin."
            call screen hit_body
            label hitBody:
                scene bathroom body no hammer
                play sound "HammerPickup.mp3"
                $ hammer_grabbed = True
            call screen kill_him
            label smash_head:
                "I take the hammer, try to find comfort in the steady grip, and fail again."
            "Just five minutes - not even that."
            "I raise it over my head."
            "You wouldn't think something like this requires much finesse, right? There's an art to it, though."
            "High enough that you get good leverage behind it, but not so high you lose your hold on it."
            "Handy thing."
            "Reliable."
            "Reflexively, I open my mouth to say something to the soon-to-be-corpse. An apology, probably."
            "It doesn't make it past the shrapnel coating my throat."
            "I bring the hammer down."
            play sound "MeatSound.mp3"
            "It does its job without protest."
            play sound "WaterDripHotel.mp3" loop
            "It's harder than crushing down carapace and easier than impacting particularly sinewy muscle."
            "There isn't any resistance. Bone and tissue and grey matter all yield, clinging eagerly to the head of the hammer with a wet crunch."
            "I linger there, my weapon resting in the mass of flesh."
            "I don't want to pull it out."
            "I don't want to see. I don't want to feel the light pop as the hammer peels away."
            "The choice is made for me. The shaking in my hands comes on so suddenly that it slips out, the handle clattering against the rim of the bathtub."
            play sound "HammerFall.mp3"
            "What's left in its wake looks like the pulp of an overripe fruit. I can see the suggestion of hair, of eyes, of bones."
            "Part of me had hoped that if I destroyed someone thoroughly enough, they'd cross the threshold from human to meat."
            "They don't. They linger in the door frame."
            show andrea body scared at left 
            ab "{i}There{/i}."
            "I finally manage to grind out."
            ab "I did it. You happy?"
            show andrea body scaredEC at left
            ab "That enough?"
            "I place my hand on the edge of the bathtub. I don't quite know what to do with it."
            "I don't know what it wants me to do from here or how things work now."
            "The answer comes quickly."
            "For a moment I ignite."
            scene andreaprologuecg
            "On some preternatural level I begin to burn. I can feel it pass through veins made kindling and out through rapid breaths."
            unknown "Not enough."
            unknown "Never enough."
            unknown "Sated. For now."
            unknown "Should've given him to me before."
            unknown "Warm flesh. Better kindling."
            "Its disapproval-its rage, its vindictiveness-laps at me"
            ab "That wasn't part of the deal."
            "From where it flickers in my chest, the sensation descends down my arm."
            unknown "Death was. You have given it to me it."
            unknown "Sated. For now."
            unknown "No."
            play sound "FireNoise.mp3" loop
            
            "I grab the body's arm. I don't know if it's Burn enacting its will or just intuition."
            "It catches instantly. The heat is searing and I brace against pain that never comes."
            "Orange and red tear a warpath through goosebumped skin."
            "It crumbles into chalky black. The flesh comes next, then muscle."
            
            scene black
            "I close my eyes after that."
            "The smell is sickly-sweet, with a corroded metal undercurrent."
            "I feel Burn prodding at the edge of my consciousness like an impatient pet."
            "It wants me to look, wants me to shared in its wonder."
            "I push it back. It's the closest I have to sway over it."
            "I stay there until the crackling dies down."
            stop sound fadeout 1.0
            "I give it one more minute for good measure."
            scene full br no body no highlight final
            show andrea body scared at right
            "When I open my eyes, there is only black."
            "Ash paints the bathtub. It clings to the faucet. It mixes with the droplets falling from it in an inky mush."
            unknown "Finished."
            unknown "I made it quick."
            show andrea angry 
            ab "{i}Thanks.{/i}"
            unknown "Ungrateful."
            show andrea sad 
            ab "We're done, right?"
            show andrea offput
            ab "You're done, {i}right?{/i}"
            show andrea offputEC
            "Even if I try to hide the desperation in my voice, it doesn't matter with Burn."
            unknown "For now. Yes."
            unknown "Sated. For now."
            unknown "The next. Later."
            show andrea angry
            ab "When?"
            "A pause."
            unknown "When I need it."
            show andrea sad at right
            "Should've known better than to ask for a straight answer."
            "It leaves without a goodbye."
            "It leaves me with all the grace of a knife twisted out of a wound."
            "It leaves me alone."    
            "Even the faucet's stopped dripping."
            "I slide to the floor, knees drawn up, hands pressing to my closed eyes until I see dots."
            "Vera will come in soon; she has to have heard it."
            "I should start on clean up before she gives me shit."
        "I keep myself against the wall to avoid stepping in any of the aftermath."
        label test_clean:
            
           
            if gatheredItems == 3:
                jump clean
            call screen cleaning_time
        
    ## menu gathering:
           
            
        ##   "Towels" if towels_grabbed == False:
        ##     jump towels_grab
            ##"Bleach" if bleach_grabbed == False:
            ##  jump bleach_grab
            ##"Brush"if brush_grabbed  == False :
            ##  jump brush_grab
            ##"Clean" if gatheredItems == 3:
                ##jump clean
                
        label towels_grab:
            play sound "TowelHold.mp3"
            "I get the towels."
            $ gatheredItems +=1 
            $ towels_grabbed = True
            jump test_clean
        label bleach_grab:
            play sound "BleachSwish.mp3"
            "I get the cleaner."
            $ gatheredItems +=1
            $ bleach_grabbed = True
            jump test_clean
        label brush_grab:
            play sound "MopHandle.mp3"
            "I grab the mop."
            $ gatheredItems +=1
            $ brush_grabbed = True
            jump test_clean
label clean:
    "I have my weapons of choice."
    "I'm just about done dousing the rag in bleach, when the door cracks open."
    play sound "DoorOpen.mp3"

    show vera body shirt1 neutral2 at left
    vl "There we go. Knew you could do it."
    "She looks at the now-corpse appraisingly."
    vl "Got him in one, huh?"
    
    ab "Yeah."
    vl "Messy, though."
    ab "You can take that up with Burn."
    "The hammer's familiar, but it wouldn't be my first option for this."
    "Burn just likes things messy."
    "At least it didn't insist on a live cremation."
    vl "Think I'll pass."
    "She strides past me, picking up one of the other mops."
    vl "{i}Anyway{/i}, lets get this cleaned up."
    vl "I'll get the tub."
    "At least I'm not left sweeping up the aftermath."
    "Maybe it's Vera's approximation of mercy."
    "She snaps on her gloves and we get to work."
    "It goes quick. Or maybe I'm just too far away from myself to notice."
    "We get the bathroom to the same state as where we found it."
    "Save for the corpse."
    "Besides that, it honestly looks better than before."
    "In our dilligence to clean up our tracks, we chipped away at the built up grime clinging to the area."
    "Vera says something about beginning to counteract some of our misdeeds with Good Samaritan points that I only half hear."
    stop sound
    scene hotel1
   
    "When we leave the bathroom, it's four in the morning."
    "It's the time of year where the sky's already begun to lighten and the first notes of birdsong start up."
    show vera body shirt1 neutral2 at left
    show andrea body sad at right
    vl "Let's go. Don't wanna linger."
    ab "Right."
    "I grab our stuff. We traveled light in here. Just a few backpacks between us. The rest is in the van."
    label car_go:

        "Vera grabs the dufflebag."
    "We leave the keys on the unmanned front desk down the hall and make our way out to the parking lot."
    "We've been calling it 'the' van or 'our' van. It's really {i}my{/i} van. I got it on my dime: for suspiciously cheap"
    "I really don't want to know what it's been through before I got it, but it's getting the job done."
    "It's nondescript, durable, and has plenty of storage space."
    "If things get real rough, we can even spend the night inside."
    show vera body shirt1 neutral at right
    vl "Shotgun!"
    show andrea body neutral at left

    ab "Aw, damn, you beat me to it."
    "I say, as if letting her drive was a possibility."
    scene black
    hide andrea
    hide vera
    play sound "CarStartSfx.mp3"
    "I coax the car feebly to life, but it's steady enough once we get on the road."
    play sound "CarAmbient.mp3" loop
    scene car bg aznight
    show vera body shirt1 neutral at right
    show andrea body neutral at left:
        xalign -0.1
        xzoom -1.0

    "This time of night, it may as well be a graveyard."
    "I can count the number of other drivers on one hand and all the buildings merge together into one looming grey mass."
    "A quiet falls between us that I don't intend to let last very long."
    "I reach for the radio."
menu:
    "Something rough.":
        play music "RoughRadioNew.mp3" loop
        jump end

    "Something quiet.":
        play music "CarRadioAmbient.mp3" loop
        jump end


label end:   
    show andrea body sad at left
    show vera shirt1 neutral at right    
    vl "So..."
    "It's a real occasion that Vera's at a loss for words."
    vl "We should get off a couple exits down, probably stop there somewhere."
    vl "Sloane's isn't that far, I think she still has that job open."
    "We could've maybe stayed at the motel, but it's better safe than sorry."
    "There should be plenty of other locations like it on the way."
    "If not? Hey-there's the van."
    ab "She'll be suspicious."
    vl "Oh yeah, one hundred percent."
    vl "But she likes us."
    ab "She likes {i}me{/i}."
    show vera annoyed
    "Vera scoffs."
    vl "Semantics. Anyway."
    vl "She won't ask too many questions as long as we're on top of it."
    vl "She'll probably let us chat her up too."
    ab "Hopefully the guys she has on retainer are actually useful."
    vl "If not we'll just look somewhere else."
    "..."
    vl "Or die, I guess."
    ab "Don't say that."
    show vera body shirt1 happy
    vl "I'm not saying we'll do that. It's just always a possibility."
    vl "Anytime you do anything, technically."
    ab "Do that on your own time, then."
    show vera annoyed
    vl "What if I did, huh?"
    vl "What if we got into a pile up right now and I died-"
    ab "That wouldn't be good."
    vl "And that was the last thing you ever said to me."
    vl "Makes you think."
    ab "That'd still be on my time."
    ab "Technically."
    vl "Okay, so what if when we stopped, you went to go take a piss or whatever, and then I got hit by a car."
    ab "In the bathroom?"
    vl "No, I'd be waiting outside for you."
    vl "Would that make it better?"
    "..."
    ab "Yeah, sure, alright."
    ab "That'd be awesome, Vera."
    show vera neutral2
    vl "That's cold."
    "..."
    vl "What were we on about again?"
    ab "Sloane. Job. Maybe knowing someone."
    vl "That's, like, three things, anyway-"
    vl "Hopefully, whatever she throws at us isn't too much of a pain."
    "Sloane's always a toss up."
    "The Paragons she deals with are under the radar."
    "Sometimes it's because they're small potatoes."
    "Other times, it's because they're things no one else wants to get their hands dirty with."
    ab "We'll deal."
    ab "We should have time."
    vl "Burn give you a date?"
    ab "Of course not."
    ab "That'd be too easy, right?"
    ab "It said it was fine until it 'needed', which could mean, I don't know..."
    ab "I don't think even it knows."
    vl "Fucking headcase."
    "I tap my fingers along to the radio in an off-beat rhythm."
    ab "I kind of just don't want to think about it right now."
    "The ash clings to the inside of my nose. The callouses that wear in my palms are only now easing."
    "It feels like I'm expecting something. Another ultimatium from Burn. Or a sudden wave of jesus-fucking-christ-you-heartless-monster. Or police sirens, because we did a sloppy job."
    "None of it's worth lingering on. Ashes to ashes ({i}ha{/i}), dust to dust."
    "{i}Keep your eyes on the road. Keep your head clean.{/i}"
    "{i}Nothing matters besides the next step.{/i}"
    vl "Alright."
    vl "What do you want to think about, then?"
    $ held_up = False
    $ food_sich = False
    $ spied = False
    menu talk:
        "Nothing, just keep driving.":
            jump keep_going

        "How are {i}you{/i} holding up?" if held_up == False:
            jump holding_up

        "What's the food situation?" if food_sich == False:
            jump food_situaton

        "...I spy." if spied == False:
            jump i_spy

    label keep_going:
        if held_up == False:
            ab "I think talking's just going to fill my head up with...I don't know."
            "Vera gives me a side glance."
            vl "All right, suit yourself."
            "She obliges, thankfully."
            "The rest of the ride is spent in silence."
            "Part of me wonders if it was the right choice."
            "Maybe hearing Vera yap would've been a good distraction."
        else:
            "I think that's enough conversation for now."
            "We spend the rest of the ride in silence."
        jump after_car
    label holding_up:
        $ held_up = True
       
        ab "I mean, I know this isn't as much of a {i}thing{/i} for you. But, still."
        ab "You were the one who got him."
        vl "He didn't put up much of a fight."
        ab "Yeah, but that's not really what I'm talking about."
        ab "It's one thing to plan all this out."
        ab "It's another to actually do it."
        "She considers, then shrugs."
        vl "It's not like there was another option."
        vl "Us or him."
        "Me or him, really."
        vl "And you were too chicken-shit to grab him yourself so..."
        show andrea angry 
        ab "{i}Hey{/i}, I got the job done."
        show andrea sad 
        ab "You volunteered."
        vl "'Cause I knew you were chicken shit."
        "I release a sharp sigh."
        ab "You sure it wasn't because you were getting bored?"
        show vera body shirt1 neutral 
        vl "That wasn't {i}not{/i} part of it."
        vl "Three birds with one stone."
        ab "What's the third one?"
        show vera neutral2 
        vl "Guy was an asshole, remember?"
        vl "Don't even have to be bogged down by guilt if we're doing a public service."
        "Right. Sure."
        "The now-corpse deserved what was coming to it."
        "It's better for both of us to take Vera at her word."
        ab "You didn't really answer, though. Are you good?"
        vl "Right now, I'm tired."
        show vera annoyed
        vl "And I wish this car had better AC."
        vl "And I wish we weren't in bumfuck Arizona."
        vl "But besides that, I'm good."
        show andrea neutral 
        ab "Cool, just wanted to make sure."
        "Vera's built for this more than I am."
        "And even if she wasn't, I don't know how honest she'd be."
        "But, it's still my job to check in."
        "Not like anyone else will."
        jump talk

    label food_situaton:
        $ food_sich = True
        ab "You hungry?"
        ab "I think there's a couple rest stops up ahead. We could probably grab something."
        vl "You still have an appetite after that?"
        "I pause to think about it."
        ab "...Yeah, guess so."
        "The nausea from earlier's receded."
        "Guess not eating all day overrules the visceral disgust of first-degree murder."
        vl "I could eat."
        ab "Okay, uh-..."
        "I keep my eyes peeled for any signs."
        "One comes into view after a few minutes."
        show vera neutral 
        vl "Waffle Home?"
        ab "Right, there's like a million of those out here."
        vl "I'm not going there."
        show andrea body happy
        ab "What, you too ritzy for it?"
        "I've seen her eat food off the floor."
        vl "You don't wanna know what happened the last time I went into a Waffle Home."
        ab "Well, now I do."
        show vera neutral2 
        vl "I was never the same afterwards."
        vl "I don't think your fragile heart could handle it, Andy."
        "I glance at her out of the corner of my eye."
        "She says it flatly. Knowing her, she could just as easily be fucking with me, as she is to have had some sort of serious incident relating to Waffle Home."
        ab "So no food, then?"
        vl "Nah, don't wanna stop."
        vl "Maybe the next place we stop will have something."
        "Or maybe this was just a needlessly roundabout way to tell me she didn't actually want to get food."
        jump talk

    label i_spy:
        $ spied = True
        ab "I spy with my little eye...something red."
        "Vera looks over at me, confused."
        "She's quick on the uptake, though."
        vl "That stop light, the one we just passed."
        ab "Bingo. Your turn."
        show vera neutral 
        vl "M'kay..."
        vl "I spy, with my little eye..."
        vl "Something black."
        $ steering_wheel = False
        $ sky = False
        $ asphalt = False
        menu look:
            "The dark stain I can't get off the rearview mirror." if steering_wheel == False:
                $ steering_wheel = True
                jump picked_wheel

            "The sky." if sky == False:
                $ sky = True
                jump picked_sky

            "The asphalt.":
                $ asphalt = True
                jump picked_asphalt
    label picked_asphalt:
        ab "The asphlat-the one on the road, I mean."
        show vera annoyed
        vl "{i}No.{\i} That's, like, the lamest option."
        vl "Try again."
        jump look
    label picked_sky:
        ab "No moon out, basically opaque."
        show vera annoyed
        vl "No, it's a dark indigo at best."
        vl "Maybe with hints of grey, if you squint."
        vl "Try again."
        jump look
    label picked_wheel:
        ab "The one on your side."
        "It'd been there when I got the car."
        "I've tried the whole gambit to get it off: bleach, car cleaner, even trying to scrape it off."
        "I don't even know what it is."
        show vera body happy
        vl "Yeah!"
        vl "That's it."
        ab "That thing's probably a hazard."
        "It's not that big, but if you have to go 'Oh, it's only sort of an impediment,' it's a bad sign."
        vl "That's why I take shotgun."
        show andrea body happy
        ab "If we crash, I know who to blame."
        vl "Wouldn't have it any other way."
        jump talk

label after_car:
    stop music
    stop sound
    "By the time we flag a place down, I'm almost passed out at the wheel."
    "It's nicer than the past motel, even if marginally."
    "The plants outside aren't quite as wilted."
    "I open the door, then wait for Vera to do the same."
    "When we walk in, the lady behind the desk looks as beleaguered as we both must feel."
    "If she's surprised to see people check in so late, it's concealed beneathed hooded lids and patchy eyeshadow."
    "We pay for our room-fifty dollars-which Vera cites as robbery under her breath."
    scene hotel_2
    "A cursory sweep of it shows no cockroaches-at least none big enough to notice, which is good enough for me."
    show andrea body neutral at right
    vl "You think Sloane cares about when we come in?"
    ab "No, as long as it's not too late."
    ab "Don't think anyone's snapped up the job that quick."
    show vera annoyed shirt1 body at left
    vl "Good, because I'm not getting up before eleven."
    "I mumble in agreement as I get ready for bed."
    "Tired sucks, but tired also means I'm too foggy to dwell."
    "The insides of my eyelids are blissfully blank when I close them."
    ab "Night."
    show vera neutral
    vl "Night."
    hide andrea 
    hide vera
    "I think I hear her say something after that, but I'm out before I fully process it."
    "..."
    scene bluehotelplain
    play sound "audio/morningambience.mp3"loop
    "Morning comes suddenly."
    "My body wakes up before I do."
    "By the time I'm cognizant, I'm already sitting up ram-rod straight."
    "My heart's only now retreating from my throat."
    show andrea body neutral at left
    "The edge of whatever dream lodged it up there fades out."
    "The sky outside is turning from orange to a grayish-blue, so it can't be {i}that{/i} early."
    "Looks like Vera got her wish."
    "I get up and into a steady rhythm."
    "Clothes. Check the windows. Shower. Brush teeth."
    "Check the windows {i}again{/i}, then wait."
    "Vera's still fast asleep."
    "She's usually a light sleeper-breathe in her direction and she's up. Yesterday must've taken more out of her than she let on."
    "It's half-past ten. I just have to twiddle my thumbs for thirty minutes before I oblige her."
    "It leaves me another long stretch of dead air."
    "Watching the numbers on the clock slowly move up can only keep me occupied for so long: maybe there's something else to do."
    "Or, I could just wait around 'til Vera gets up."
    $ sight_saw = False
    label hotel_2_stop:
        
        call screen hotel_2
    
    label crossword_puzzle:
        if boxesFilled == 4:
            "I think I've just got the one in me for today."
            jump hotel_2_stop
        "I reach for the crossword puzzle on the coffee table."
        "I feel like I'm unearthing some long forgotten tomb when I peel back the dust-caked cover."
        "Maybe the promise of teasing my brain will bring me some calm."
    label opencrossWord:
        call screen crossword
        
        ##crossword
    label type_in:
        python:
            answer = renpy.input("Answer? (Lowercase)")
        
            
        if answer == correctAnswer:
            if correctAnswer == "shrink":
                $ box1Filled = True
                $ boxesFilled += 1
            if correctAnswer == "bohr":
                $ box2Filled = True
                $ boxesFilled += 1
            if correctAnswer == "hope":
                $ box3DownFilled = True
                $ boxesFilled += 1
            if correctAnswer == "throwup":
                $ boxAcrossFilled = True
                $ boxesFilled += 1

        else:
            "No, I don't think that's it."
        if boxesFilled == 4:
            "There, brain successfully teased."
            jump hotel_2_stop
        jump opencrossWord
    label sight_see:
        if sight_saw == True:
            "I think that's enough sight-seeing for now."
            jump hotel_2_stop
        "I look out the window."
        "One car passes by."
        "A second car passes by."
        "A third car passes by."
        "Oh, look. A cyclist."
        "Way to break from the mold."
        "Then a fourth car-oh shit, a bus."
        "This goes on for a bit."
        $ sight_saw = True
        jump hotel_2_stop
    label wait:
        "Sometimes, nothing is the best option."
        "I elect to spend the next thirty moments clearing my head as much as I can."
        jump wake_vera
label wake_vera:
    "Eleven comes before I know it."
    "I go over to shake Vera up."
    "As soon as I touch her shoulder, she jerks awake."
    "Her eyes snap wide open, before narrowing into annoyance."
    scene hotel_2
    show vera body shirt2 annoyed at left
    show andrea body neutral at right
    vl "Ugh..."
    "She makes a sound like a car backfiring."
    ab "What? I didn't wake you before eleven."
    "She turns her venom towards the digital clock on her nightstand."
    vl "{i}Traitor{/i}."
    "She slowly extricates herself from the bed."
    vl "Did you call Sloane?"
    ab "Not yet. I was waiting for you."
    "I pull my phone from my purse."
    show vera neutral2
    vl "You have the story straight, right?"
    ab "Mhmm."
    ab "We're strapped for cash. And we're looking for information about weird cases, so we can-"
    "Vera cuts me off."
    vl "We have a vested interest. Personal project."
    "I cringe."
    show andrea annoyed
    ab "That's suspicious as hell."
    vl "We don't have anything better, do we?"
    vl "Again, she'll suspect something either way."
    vl "As long as we don't give her a reason to pry, we'll be fine."
    vl "And if things get hairy we can, y'know-..."
    "She makes a remarkably accurate recreation of an explosion with her hands."
    show andrea sad
    ab "I don't want it to come to that."
    vl "It won't! Probably."
    vl "That's why we're having this conversation."
    show vera body shirt2 happy at left
    vl "We'll handle things as they come, Andy, my dear."
    "She claps my shoulder."
    "I gingerly lean away."
    show andrea annoyed
    ab "Don't patronize me."
    vl "I'm not. Promise."
    "Her expression doesn't exude reassurance."
    vl "Anyways, give her a call. I'll get ready."
    hide vera
    "I roll my eyes, but oblige."
    play sound "audio/phonering.mp3"
    show andrea neutral
    unknown "Andrea?"
    stop sound
    "If Sloane's surprised at all, it doesn't show."
    "It's a talent of hers. She makes it sound as if she's already worked whatever conversation you're having into her schedule."
    ab "Yeah, hey, it's me."
    sl "Are you calling about the job?"
    ab "Uh, straight to business–"
    "Christ, I sound like a kid trying to hide that I threw a baseball through her window."
    ab "Mhmm. Is it still open?"
    sl "It is. My colleague's still looking for some helping hands. I was hoping you two would bite."
    sl "..It {i}is{/i} both of you, right?"
    ab "Yeah, Vera's around."
    "Vera tilts her head back to look at me."
    show vera body shirt2 neutral at left
    vl "Is she asking about me?"
    "She mouths."
    hide vera
    sl "Sounds like it."
    sl "When are you free? If you're in the area, there's a lovely diner that's opened up."
    sl "My treat."
    ab "We're maybe...twenty minutes out from your place?"
    sl "Sounds good. It's the Honey Tiger Diner, on Commons Street."
    sl "I'll see you in an hour."
    ab "Yeah, see you there."
    "There's a pause."
    sl "Tell Vera hello for me."
    "There's the click of a receiver dropping."
    show vera body shirt2 neutral2 at left
    vl "So?"
    ab "Sloane says hello."
    ab "And she wants to meet up in an hour. Looks like the job's still open."
    vl "That was quick."
    ab "She said she was hoping 'we'd bite.'"
    show vera annoyed 
    vl "{i}Ugh{/i}. She always puts things so weird."
    ab "I mean, it's a pretty normal thing to say."
    vl "Maybe just 'cause it's from her."
    vl "I dunno, it always feels like we're bugs in those little...maze, toy bracelets kids have."
    show andrea neutral
    ab "She's our best shot right now."
    "I've always gotten along better with Sloane than Vera has, but I can see where she's coming from."
    "She could be completely transparent and her intentions completely benign and she'd still sound like she was scheming something."
    ab "...I mean, if it's too much of an issue we-"
    show vera neutral2
    vl "It's good."
    "I click my tongue."
    ab "Right. Let's get ready, then."
    hide andrea
    hide vera
    label sloane_diner:
        "We dont have to worry about breakast, so we get out quick."
    scene diner
    "The drive over is shorter than the last. Most of the time is spent finding a place to park."
    "The Honey Tiger Diner is probably the most put-together amenity we've seen over the last two weeks."
    "Even if it's not anything fancy (Sloane has standards, but she's not shilling out for us) the fact that the sign on the top isn't trying to extricate itself from the wall and the windows aren't cobwebbed is good enough."
    "There's a {i}ding{/i} as we go through the door."
    "Sloane is sitting in a middle booth. It doesn't look like she's ordered yet."
    "She waves us over. There's just the slightest drag to Vera's footsteps."
    play music "SloaneSmile.mp3" loop
    show sloane body smile:
        xzoom -1.0
        xalign -0.1
        yalign 1.0
    sl "There you are. Thanks for the punctuality."
    "Her voice is smooth-like she's cut out the breaths to save time."
    show andrea body neutral:
        xalign 0.9
        yalign 1.0
    ab "Thanks for having us."
    "I slide in and pull out a chair for Vera."
    show vera bodyflip shirt2flip neutralflipped:
        xalign 0.98
        yalign 1.0
    vl "Yeah, thanks."
    "Sloane's gaze lingers on her for a moment. Vera rests her head on her hand and faces towards the ground in record time."
    sl "How are you two? Keeping busy?"
    ab "Not really, we're trying to fix that."
    ab "I think we've had a long enough vacation."
    "Sloane raises an eyebrow."
    sl "Vacation?"
    show andrea body happy
    ab "We've been coasting by on savings."
    "{i}My{/i} savings."
    show andrea body neutral
    vl "But, uh, sabbatical's over. We're looking to get back in the game."
    "Vera leans out towards the rest of the diner."
    vl "Which ones our waiter? You said it's your treat, right?"
    sl "I {i}did{/i}."
    sl "How rude of me."
    "She waves down a hurried looking young man."
    "Sloane keeps it simple: coffee with two creams and a sugar and some kind of omelet."
    "Vera takes a coffee with {i}one{/i} cream and {i}two{/i} sugars and one of those waffle-bacon-egg combo monstrosities."
    w "What about you, miss?"
    $ drink_chosen = "coffee"
    menu:
        "Just a black coffee.":
            jump black_coffee

        "Orange juice.":
            $ drink_chosen = "juice"
            jump orange_juice

        "Coffee with two creams and two sugars.":
            jump two_cream


    label black_coffee:
        "It's simple and I need the energy."
        jump breakfast_food
    label orange_juice:
        "I don't think caffeine's going to do me much good besides making me more wired."
        "I'll go with something easy."
        jump breakfast_food
    label two_cream:
        "I may as well continue the trend."
        jump breakfast_food
    
    label breakfast_food:
        w "Sounds good. Anything to eat?"
        $ food_chosen = "Null"
        menu:
            "Something Savory.":
                $ food_chosen = "eggs and bacon"
                jump eggs_bacon

            "Something Sweet.":
                $ food_chosen = "pancakes"
                jump blueberry


    label eggs_bacon:
        "I go for the eggs and bacon."
        "It's a protein wombo-combo."
        "Should help with the energy."
        jump ordered_food

    label blueberry:
        "I go for the blueberry pancakes."
        "Not exactly nutritious, but I think I need something sweet."
        "Blueberry beats chocolate. Always has."
        jump ordered_food
   

    label ordered_food:
        w "Sounds good, I'll be over with that in a second."
        "We watch him all the way back to the kitchen before we continue."
    sl "Anyhow. The job."
    show sloane body neutral
    "I sit up straighter on impulse. Old habits die hard."
    ab "You said we would be a good fit for it."
    "Sloane nods and begins digging around in her bag."
    sl "It came around just at the perfect time, it sounds like."
    "She places a manilla folder on the table."
    "But, when I go to open it, she places a hand to keep it closed."
    sl "Just a second. I wanted to ask some questions beforehand."
    show vera annoyedflip
    vl "You couldn't have asked us over the phone?"
    sl "It's more practical to talk here. Are you in a rush?"
    "I give Vera a side eye."
    ab "No, it's fine."
    ab "Ask away."
    sl "Not that I don't appreciate the help. But why the sudden interest in my work?"
    sl "I didn't get the impression you had much love for the sort of hunts I deal in."
    "Vera crosses her arms."
    vl "Got bored."
    show andrea body happy
    ab "...I think I've been playing safe long enough. Figured it's about time I get another perspective."
    ab "Push myself."
    sl "Mmm."
    "I do my best not to shift under her scrutiny."
    show andrea neutral
    "I can't blame her, it's a pretty bullshit story."
    "No one really goes to Sloane because they want to."
    sl "I'm glad you're taking to things, Andrea."
    sl "I know your entrance into all of this was pretty abrupt."
    "Vera pulls her lips into a thin line."
    show sloane smile
    sl "And it's good to see {i}you{/i} back to form."
    vl "Sure."
    ab "Thanks, appreciate the sentiment."
    vl "So, the {i}job?{/i}-"
    show sloane body neutral
    sl "One more thing."
    show vera angryflipped
    vl "{i}Goddammit.{/i}"
    "Vera hisses under her breath."
    show vera annoyedflip
    "I kick her lightly under the table."
    "She was on me for keeping the story straight and now she's getting all pissy with Sloane."
    ab "It's fine. What is it?"
    "Sloane pointedly ignores Vera."
    sl "You asked me if I knew anyone who was particularly well-versed in Paragons in a scientific context."
    sl "It's..."
    "She clicks her tongue."
    sl "It's a strange ask, is all I'm saying. It's not what I expected from you two."
    "I rest my hand on my knee and tighten the grip."
    show andrea body happy
    ab "Just a personal project-personal {i}interest.{/i} Again, trying to see new perspectives.."
    sl "What about you, Vera? I didn't take you for much of an academic."
    show vera neutralflipped
    vl "Just giving her a hand with her nerd shit."
    "She supplies helpfully."
    show vera neutral2flipped
    "At this point it's not about if Sloane believes us; it's it's question of whether she believes whatever we have going on is worth the effort to pry out of us."
    sl "I see."
    "She raps her fingers against the table, before taking her hand off the folder."
    sl "Good to know I can aid in some of those latent passions."
    sl "My friend can definitely help."
    "She gestures for us to open it."
    "Inside is pretty sparse."
    "A newspaper clipping, what looks like some sort of report, and a photo."
    show andrea stern
    ab "Right, uh, you said they were having some trouble?"
    "She nods."
    sl "They're tracking a particularly difficult one: the thing's already killed once, apparently."
    sl "But, they aren't much of a fighter."
    sl "They're just looking for some protection- said something about maybe getting some samples."
    show sloane body smile
    sl "Should be straight forward enough."
    "Some of the tension leaves me."
    "This is more routine."
    "The rundown, the bundle of evidence- all straight to the point."
    ### change to an image map
    "The questions are just as routine."
    $ newspaper_picked = False
    $ autopsy_picked = False
    $ photo_picked = False
    menu evidence:
        "Newspaper." if newspaper_picked == False:
            $ newspaper_picked = True
            jump newspaper
        "Autopsy." if autopsy_picked == False:
            $ autopsy_picked = True
            jump autopsy
        "Photo." if photo_picked == False:
            $ photo_picked = True
            jump photo
        "Question Sloane." if photo_picked == True and newspaper_picked == True and autopsy_picked == True:
            jump question_sloane
    label newspaper:
        "It's the front page of an article from a week ago."
        "It discusses a disappearance somewhere called Clyver City."
        "Apparently, it's the third in a string of incidents."
        "A lady named Vivian Planchart."
        "It doesn't give much in the way of details-mostly just reiterates that any information should be reported to the proper authorities, and that the woman was last seen walking home from work."
        jump evidence
    label autopsy:
        "It's a scan of an autopsy. It says its from the day before yesterday."
        "It gives the details of one Robin Clarke: Male, 35 years old, six feet."
        "It says he was found dead in the bathroom of his home by his wife."
        "Body was mangled significantly and found in a state of-quote-partial dissolution."
        "The notes mention that it was covered in cuts reminiscent of bite marks, but further testing would be needed to match them to any specific species."
        jump evidence
    label photo:
        "That's definitely a photo of {i}something.{/i}"
        "I almost want to say it's roadkill, but it looks more like a...mound of flesh and fur."
        "Someone's helpfully put a dinner plate next to it for scale and it seems to be about the same size."
        jump evidence
    label question_sloane:
        "When it becomes clear Vera and I have finished looking over the evidence, Sloane crosses her arms."
        sl "This is the case my colleague was following up on."
        sl "There's been a series of disappearences a few towns over. He had some initial thoughts it may be Paragon related and the autopsy pretty much confirms it."
        ab "Guessing Robin here was one of the missing persons?"
        show sloane body curious
        sl "Mhm."
        sl "{i}But,{/i} he was the first to go missing. A week or so before Vivian."
        sl "It's just that the body that turned up now."
        "I wince. Not a lot of good conclusions to come to when a corpse's been kept around somewhere before being dropped off."
        ab "So, how'd your buddy get wrapped up in it?"
        sl "Dominic-..."
        show sloane body stern
        "Dominic. I'll put that into the mental file cabinet."
        sl "He's got some ties down at the morgue, so he managed to get his hands on that sample in the picture."
        sl "He told me he has some leads, but wanted to get some hands on deck before he pursued them."
        ab "That's where we come in, yeah?"
        sl "Like I said. Simple."
        show sloane body smile
        sl "You keep Dominic's head on his shoulders and you can probe it for whatever information you want for your...personal project."
        "I'm still not happy with how honey-tinged her words are, but we take what we can get."
        "We got what we needed without issue; we'll have to hope it continues just as smoothly."
        vl "Sounds good. Awesome."
        vl "Now-"
        "We're interrupted by the arrival of our waiter."
        "It provides a good shake-up to switch gears."
        "It also means that we have to stay for the rest of the meal and fill the air when we've already finished business."
        "I offer a lukewarm 'thanks' and take my [food_chosen]."
        if food_chosen == "eggs and bacon":
            jump egg_route
        elif food_chosen == "pancakes":
            jump pancake_route
        


        label egg_route:
            "The eggs look about as appetizing as anything can right now."
            "They left them a little too runny for what I usually prefer, but it's not like I asked them otherwise."
            "It smells like they've glazed the bacon with some sort of honey. There's a sweet scent under the slight char."
            jump vera_lookover
        label pancake_route:
            "They've been arranged in an even stack. I never figured out how these places manage to make them look so neat."
            "Even the blueberries are uniform, arranged across the surface like rows of carefully dug, fruit-flavored graves."
            "The surface of one is soft when I prod it."
            "Nice. Most important part."
            jump vera_lookover
       
        label vera_lookover:
            show vera bodyflip shirt2flip happyflipped at right
            vl "Ooh, looks good."
            "Vera peers over my shoulder."
            "Instinctively, I pull my plate away."
            show andrea body annoyed
            ab "You have your own."
            "I gesture to the precarious mound of breakfast foods piled on her plate."
            vl "Sheesh, I was just making an observation."
            show andrea body neutral
            ab "Sure you were."
            vl "It's like you're setting me up for failure."
            vl "Expecting the worst and all that."
            vl "You can have some of mine if you want."
            "I know her game. She'll ask for a bite then manage to scarf down half the meal."
            ab "I {i}don't{/i} want yours."
            show andrea body annoyed 
            "Vera rolls her eye."
            show vera bodyflip shirt2flip neutral2flipped 
            vl "Damn. Okay."
            "I open, then close my mouth. Whatever tangent this runs off into is going to be a nothing conversation."
            show andrea body neutral 
            "Instead, I try to muster whatever appetite I've got and start on my food."
            if food_chosen == "eggs and bacon":
                jump egg_eat
            elif food_chosen == "pancakes":
                jump pancake_eat
        
        label egg_eat:
            "The egg splits open and starts running as soon as I press my fork against it. I have to partition my bacon to prevent from getting all mushy."
            "Again, it's runnier than I'd like."
            "It tastes alright once I gather it onto my fork-it definitely is eggs."
            "But the texture's still all off. It's too yielding, it coats my mouth too easily."
            "I realize I've paused mid-bite, the offending yolk dripping back onto my plate."
            sl "Everything alright?"
            "Sloane peels herself away from what passes as conversation between her and Vera."
            "I clear my throat and rapidly take a drink of my [drink_chosen] to get the taste out of my mouth."
            ab "Yeah, I'm good."
            vl "You know how it is with eggs."
            "Vera offers hastily."
            vl "They're fine until they start tasting like eggs, right?"
            ab "Yup."
            "Good thing there's half the meal left, right?"
            "It's fucking eggs and bacon. It's {i}fucking{/i} breakfast."
            "I'm fine, I'm good. I've got it under control."
            "Having eyes on me should keep it easier. Pressures me more to get a grip."
            "It should."
            "It does."
            "I stab a fork into the bacon strip vindictively."
            "There's a light {i}crack{/i} as it breaks through the outer layer of glaze."
            "The inside is still the slightest bit tender."
            "I bite into it."
            "It feels like biting into meat that's been left out in the sun."
            "It feels like breaking through cracking, calcified skin, into what's left of flesh."
            jump ash_food
        label pancake_eat:
            "There's a slightly damp, mushy texture to the pancakes."
            "They've been prematurely drenched in syrup, which coats the inside of my mouth as I bite in."
            "It's a little too sweet, sickly almost."
            "And there's hints of food left too long on the stove; there's a slight char underneath it."
            "It must be why the blueberries are so yielding-they're almost liquidated."
            "I realize I've paused mid-bite, awkwardly licking the remnants of smushed berries off of my lips."
            show sloane body curious
            sl "Everything alright?"
            "Sloane peels herself away from what passes as conversation between her and Vera."
            "I clear my throat and rapidly take a drink of my [drink_chosen] to get the texture out."
            show andrea body sad
            ab "Yeah, I'm good."
            vl "They probably used the mix for that stuff."
            "Vera offers hastily."
            vl "Makes it feel all caulky and shit."
            show andrea body neutral
            ab "Yeah, must be that."
            "Haven't even made it halfway through the meal."
            "It's fucking pancakes. It's {i}fucking{/i} breakfast."
            "I'm fine, I'm good. I've got it under control."
            "Having eyes on me should keep it easier. Pressures me more to get a grip."
            "It should."
            "It does."
            "I stab another fork into the stack vindictively."
            "There's another light {i}squish{/i} as it pierces through one pancake into the next."
            "I cut it, then bring it up to my lips."
            "It feels like biting into an overdone mass of something."
            "It feels like biting into flesh that's been left to boil until it's melted into pulpy meat."
            jump ash_food
        label ash_food:
            show andrea body scared 
            "The food turns to ash in my mouth."
            "In one frenetic motion, I grab my napkin and spit into it. I stand up bolt upright, my sinews yanked to attention."
            show sloane body stern
            sl "You sure everything's fine?"
            "I think I see some genuine concern from Sloane. Not a good sign."
            "I grit my teeth."
            show andrea body offput 
            ab "Food's burnt."
            "I can see Vera's grip tense around her fork."
            "Not a conversation I'm excited for."
            show andrea body scared 
            ab "I'm gonna-bathroom, I'll be right back."
            hide vera 
            hide sloane
            "I don't bother asking where it is, I can figure it out."
            "I can feel stares trailing me as I move."
            "Or maybe I don't. Fuck, maybe I'm just losing my grip."
            "I follow the sign to the back of the restaurant and go in."
            stop music
            play sound "DoorOpen.mp3"
            "It's blissfully empty."
            "I screw my eyes shut and bring my hands to my face, nails scratching at the scalp."
            show andrea body scaredEC at left
            "I keep my mouth locked firmly tight. I don't know whether it's vomit or a sob or a scream that's climbing up my throat."
            "I can't be doing this, not here."
            "This is fucked, I'm fucked. This isn't a luxury I can afford."
            "I cup a handful of water and throw it in my face."
            "It's lukewarm. My free hand tightens on the sink."
            "Can't get my head straight; can't keep a face up for Sloane; can't choke down goddamn food."
            "Can't bash in a skull without Vera dropping it in my lap like a cat bringing in roadkill."
            "This is only the first one."
            "What's gonna happen next?"
            "I know Burn's listening. I can't feel it, but if I wanted to-if I wanted to pry myself open like rotten floorboards-I could."
            "I don't need to; I already know what it thinks."
            "{i}Stupid little girl.{/i}"
            "{i}Ungrateful coward.{/i}"
            "It might push its deadline up just to spite me."
            "Not that it'd call it spite."
            "It's always motivation with it. Encouragement. A test. The chance to be something better."
            "Less fragile."
            "Stronger."
            "The off-beat {i}click, click{/i} of my shoes against the tile punctuates the thought that I've already been in here too long."
            "Someone else is gonna come in and see me."
            "But it feels like if I go out there again, trying to make idle chatter while the scent of burnt meat lingers over me like cling wrap I'll collapse in on myself.."
            "I just need a second."
            "I don't have a cigarette on me, so it's the next-best thing."
            ab "{i}Tyger, Tyger...{/i}"
            "I feel myself mumble out the words more than I hear myself say them."
            "Eighteen years and twelve grades of English, I have no idea why this is the thing I kept from it."
            ab "{i}Burning bright.{/i}"
            "The stanza's woven itself into the grooves of my muscle memory."
            "It's a ritual, habit, whatever."
            "It gives me something to do, keeps me grounded with a rhythm."
            "I'm used to using it to stay calm when something's about to bite my head off."
            "But, I'll welcome it now, anyhow."
            "Not quite a comfort, but verging on one."
            show andrea body scared at right
            "I pry my eyelids open."
            "My hearts' stopped syncopating, and I will my hands into stillness after a few stern glares."
            "There. Managable."
            "Enough to go back out and finish whatever pleasantries it'll take to get out of here, then deal with whatever Vera inevitably latches on to."
            show sloane body stern:
                xzoom -1.0
                xalign -0.1
                yalign 1.0
            show vera bodyflip shirt2flip neutral2flipped:
                xalign 0.98
                yalign 1.0
            show andrea body neutral:
                xalign 0.9
                yalign 1.0
            "By the time I make it back to the table, my back's straight and I've swapped out the bile climbing up my throat for idle conversation."
            "Neither Sloane nor Vera put much effort into hiding the fact they're suspicious, but don't stop me when I pivot away."
            "The twenty minutes until we get our check go by quickly."
            show andrea body sad at right
            "Sloane wishes us good luck on the job and hopes our-"
            sl "-newfound freedom serves us well."
            "I thank her for the meal. She leaves."
            "The waiter asks if we want to take the food to go, and Vera answers 'yes' before I can decline."  
            hide andrea
            hide vera
            "Neither of us say anything."
            "I lead the way back to the car and she has the courtesy to wait for me to put my keys in the ignition before starting."

            label car_argument:
                stop music
            scene carbgazday
            show andrea body sad at right
            show vera body shirt2 annoyed at left
            vl "Andy."
            "She begins slowly."
            show andrea body annoyed 
            ab "{i}Don't.{/i}"
            "She takes a breath to try and steady herself. It doesn't work."
            vl "So. What's up?"
            "I don't look at her, I just reach for the gear shift."
            "She grabs my hand before I can take it out of park."
            show andrea body angry 
            ab "Hey, what the fuck?"
            show vera body shirt2 angry 
            vl "I asked you a question."
            ab "Nothing. {i}Nothing's{/i} up."
            vl "Nothing my ass-"
            "She balls her other hand into a fist."
            vl "'Sloane likes me-...'"
            "She does her best mimicry of me."
            vl "'She's our best shot'."
            ab "Can we {i}not{/i} do this? We got the job. She was gonna be suspicious of us anyway."
            vl "Yeah, okay, you turning into a-a what-zombie halfway through breakfast didn't contribute to it at all."
            ab "I wasn't-..."
            show andrea body sad
            ab "I told you, my food was-..."
            "A low hiss escapes Vera."
            vl "It wasn't. It wasn't fucking burnt. I told you to get a grip. Christ, you're worse than yesterday."
            show andrea body angry
            ab "{i}Let me go, Vera.{/i}"
            "For a moment, I think I'm going to have to wrench my hand free, before she pulls away sharply."
            show andrea body sad
            vl "Are you going to answer me? Or are you just gonna keep playing dumb?"
            show andrea body angry
            ab "What do you want me to say?"
            ab "What the hell do you want from me?"
            vl "I told you-I {i}keep{/i} telling you. Get your-"
            ab "Get my shit together?"
            "I whirl on her. Whatever part of my brain I can usually count on to remind me that this is too much effort - that arguing usually is, {i}especially{/i} arguing with Vera - seems to have calcified."
            ab "You keep saying that, over and over and over-"
            vl "Because you don't and you're going to have to if this is going to-..."
            ab "Let me talk."
            "I grip the steering wheel until my knuckles go white."
            "Careful. Watch it."
            "Temper yourself."
            "{i}In the forests of the night...{/i}"

            ab "What's wrong with you? Get my-...get it together?"
            ab "I bashed in his fucking head and torched him."
            ab "I can still smell it. Taste it."
            "Gristle and muscle rendered into ash; food for the overeager air conditioning."
            show andrea body scared
            ab "It's been a day-{i}less{/i}than a day."
            ab "I don't know how you expect me to-what?-walk it off."
            ab "At least pretend to care."
            "Vera clicks her tongue."
            vl "You barely did anything."
            "She leans in closer. It's somewhere between a confession and a dare."
            vl "{i}I{/i} found him."
            vl "{i}I{/i} took him out."
            vl "{i}I{/i} did it even when he begged for his stupid little life like a dog."
            vl "{i}I{/i} dragged him halfway across town because I knew {i}you{/i} couldn't do it."
            ab "Don't act like this is about me."
            "Another scratch of laughter."
            show vera body shirt2 neutral2
            vl "It's always about you! This entire damn thing is about you."
            vl "It's your deal. It's your hit list. Your lifeline."
            ab "I'm just your excuse to do whatever you want, hurt whoever you want."
            ab "Easy execution block right in front of you."
            ab "Me dying was probably the best thing to happen to you."
            show vera body shirt2 neutral
            vl "Tell me to leave then."
            "Her hand hovers over the car door; a threat."
            vl "Kick me out of this car."
            vl "It's yours."
            show andrea body angry
            ab "Don't-..."
            vl "No, go on."
            vl "You don't need me around. You can take care of yourself just fine. You're way stronger now."
            "Another hairbreadth closer."
            show vera body shirt2 happy
            vl "Right?"
            "I almost answer reflexively."
            "Oblige her. Throw her bag at her in agreement. {i}'Like hell I need you.'{/i}"
            "{i}I never did.{/i}"
            "Just to rattle her; something to loosen the certainty pulled taut over her face."
            "She'd probably listen."
            "Vera's always like that. Leave the door open and she'll fall over herself to break for it."
            "I stay silent though, teeth gritted."
            "Slowly, she pulls away from the door, then leans back in her seat with a sigh."
            vl "There. Thought so."
            show andrea body sad
            ab "Fuck you."
            vl "You could do this without me, but you won't. You don't have the guts."
            vl "Or you don't think you do. Whatever."
            show vera body shirt2 annoyed
            vl "Yeah, you caught me. I don't care about whoever you turned into mincemeat."
            "Of course she was just placating me about who he was. She probably didn't even get his name before cutting his throat."
            vl "Maybe I liked cutting him up. Maybe I didn't. Maybe you're going to spend your entire life being haunted by guilt."
            vl "He died the same either way. Whoever's next will, too."
            vl "It's either you or them. Take Burn up on it."
            show andrea body annoyed
            ab "You know it won't listen."
            "I'm latching onto a rhetorical. I just want to do something besides sit mutely like I'm a child being given a lecture."
            show vera body shirt2 neutral2
            vl "Feel however bad you want. Cry yourself to sleep. Bottle it up. You're good at that."
            vl "Just don't let it screw us over. You got a chance most people didn't it and it'd be stupid if you wasted it-because you couldn't keep it together over breakfast and someone got too curious."
            vl "What happened sucks. Not fair. Etcetera etcetera, But it did so-..."
            "She puts her hands up."
            vl "Guess you'll have to deal with it."
            show andrea body sad 
            ab "I {i}am{/i} dealing with it."
            ab "Maybe if you give me more than twelve hours, I'll save some more face."
            show vera body shirt2 sad
            vl "Okay."
            "A stalemate is the closest thing to an admission of guilt I'll get from her."
            play sound "audio/CarStartSFX.mp3"
            "I put the car into reverse and she doesn't stop me, this time."
            ab "Hope this guy actually has something useful."
            "She doesn't respond. Anything else I'll say's just going to sound like I'm desperate to break the tension."
            "The realization that it's not a hope, but a {i}need{/i} that we get something creeps up steadily with the rumble of asphalt."
            "I need something. Some sort of hint that there's a way out of this."
            "Something that comes before I've beat the last bits of guilt out of myself."
            "..."
            label chapter_1:
            hide andrea
            hide vera
            "We drive for a while."
            "I consider going for the radio and a glance out of the corner of my eye tells me Vera is too, but neither of us make a move."
            "A tacid admission that we're both too spent to talk."
            "We track down a place pretty easy, around eight."
            "I pay the front desk. We get the keys."
            "The room's fine, but not particularly clean."
            "We go to bed early."
            scene hotel1
            "I don't dream."
            "Neither of us thinks to set an alarm, so it's the sun that wakes me."
            "Six in the morning it looks like: crack of dawn."
            "It's unusual for Vera to be up before me."
            "Even if she's a light sleeper, she'll usually go back to bed whenever she rouses, until she deems the day worthy enough to drag herself into."
            "But, she comes out of the bathroom just as I sit up."
            "She's already dressed and it smells like she's showered."
            show vera body shirt3 neutral2 at left
            vl "...Hey."
            "I rub the sleep from my eyes."
            show andrea body sad at right
            ab "Hey."
           
            "I ruffle through my bag to pick out my clothes. I take longer than I really need."
            hide vera
            "Vera's eyes boring into my back don't help."
            vl "How'd you sleep?"
            ab "All right."
            "I pull out a shirt."
            ab "You?"
            vl "Good."
            vl "Mostly."
            vl "Air conditioner kept me up for a bit."
            ab "Ah, yeah. Sounds like a pain."
            "I pause to change."
            show andrea sad
            ab "We really know how to pick these places, huh?"
            "After all the times we've been at each other's throats, you'd think we'd have developed a protocol for this."
            vl "Technically, it was your call."
            "Her voice is soft. It's not apologetic, but it seems there's a weak attempt to lift the octave into some sort of joke."
            ab "I'll let you pick the next one, then."
            ab "You can pay for it, too."
            show andrea body happy
            "I take the fall to be the first to break a smile."
            "The tension drops from her frame."
            show vera body shirt3 neutral at left
            vl "Nevermind. You should consider a job in real estate after all this."
           
            "And that's that."
            hide vera
            hide andrea
            "I shower, inching the heat up centimeter by centimeter 'til it hits as hot as I can handle."
            "It's early, so I can afford to drag my feet a little: I take my time to wash whatever tension sleep hasn't soothed down the drain."
            "Not everything is purged, but it's enough that when I step back out into the motel room, conversation doesn't feel like pantomime."
            show vera body shirt3 neutral2 at left
            vl "Ready to go?"
            show andrea body neutral at right
            ab "I'm good."
            ab "I think the guy's an hour out."
            ab "We can probably give him the same story we gave Sloane."
            vl "Interested in research, just trying to broaden our horizons, yadda-yadda-yadda."
            ab "Just about, yeah."
            vl "{i}Good{/i}"
            vl "Sighs."
            vl "I don't think I could handle any more bullshitting."
            "I glance around the room."
            "There isn't much to pack. It's a lot lighter load than last night."
            ab "Off we go, then."
            "We drop off the keys, check that no one's snuck up on us in the parking lot, then get back to the car."
            play sound "audio/CarStartSFX.mp3"
            play sound "CarAmbient.mp3" loop
            scene carbgazday
            show vera body shirt3 neutral2 at left
            show andrea body neutral at right
            "The heaviness from last night hangs in the air for a moment, then dissipates into the rumbling of the road."
            vl "...Got any tunes?"
            "One of the few things Vera relents in is my ownership of the radio."
            ab "Let me see."
            menu:
                "Something quiet":
                    jump ambience2
                "Something rough":
                    jump rough2
                "Skip it":
                    jump skipmusic
            label ambience2:
                stop sound
                vl "Trying to set the mood?"
                ab "What mood?"
                "She shrugs."
                play music "audio/music/AmbienceRadio2.mp3" loop
               
                jump car2
            label rough2:
                stop sound
                show vera happy
                vl "Ooh, crunchy."
                "This is usually more to her taste."
                play music "audio/music/RoughRadio3.mp3" loop
                jump car2
           
            label skipmusic:
                "Vera raises an eyebrow."
                vl "Nothing for now?"
                ab "Nah, just wanna brood for a bit."
                jump car2
    label car2:
        "The car ride goes by quickly."
        "Or at least the first thirty minutes do."
        show vera neutral2
        vl "We should get breakfast."
        "She checks out the window."
        vl "We're shooting towards brunch, at this point."
        "I've been too focused on driving to really notice but, yeah, haven't eaten anything since yesterday afternoon."
        ab "Right. Wanna hunt down a place?"
        vl "Drive-through, probably, it'll save time."
        show vera neutral
        vl "Long as it's not Waffle Home..."
        show andrea body happy
        ab "Of course."
        "It's not long before we spot an exit promising amenities along the way."
        "Neither of us are looking for anything in particular, so we just pull over into the first burger joint we encounter."
        "I'm keenly aware of Vera glancing at me all the way through ordering, to when we park to eat."
        "I've just opted for a slider, while she's gotten a shake and some fries."
        "She wolfs them down like someone's going to steal them if she doesn't finish them within two minutes."
        show andrea body neutral
        "I'm slower about it."
        "It's probably just validating whatever suspicions she has about my ability to eat without having a mini-breakdown."
        "She's not all the way off the mark: the patty looks a lot less appetizing on second glance, though that could just be a symptom of this place's quality."
        "I follow in her footsteps and shove it in my mouth as quickly as I can. It goes down easy. No smell of char: nothing."
        "Vera's still staring."
        show andrea annoyed
        ab "I'm fine, you know. I'm not gonna choke if you don't monitor me."
        vl "I know, I know."
        show vera happy
        vl "Just missed a spot."
        "She puts a finger to my chin and brushes her thumb against my bottom lip, wiping away whatever food scrap was left over."
        "Vera keeps it there a few seconds longer. Her skin's rough, a product of years spent carving callouses into it."
        show andrea body neutral
        ab "Hey-"
        vl "Hey what?"
        "She retracts her hand and wipes it against her pant leg."
        show vera body shirt3 neutral
        vl "I'm just being helpful."
        "I crumple up the paper that'd covered my burger and toss it into the makeshift plastic-bag trashcan on the backseat."
        ab "Thanks."
        "I don't know if taking the reassurance at face value or scrutinizing it into oblivion is the call here."
        "I settle on a middle ground: starting the car and getting back on the road."
        vl "This the spot?"
        "Vera asks me after we reach some sign of civilization, a few miles out."
        "The address we'd been given read like a home address, so it feels like it should be in a neighborhood."
        "Rows of near identical houses greet us."
        ab "Nice place."
        "It's the type where every one of them has a garage and a backyard large enough to have a playground."
        "I drive slowly, looking at the numbers rendered in golden script over each doorway."
        "5321...5319...5317–"
        ab "5315. Here."
        "The house is unremarkable. It doesn't even have any tacky lawn decorations to distinguish it from its fellows."
        vl "Do we park in the driveway or..."
        "There's only one car there right now, but I don't know if the guy's the type to be on our asses about it."
        ab "Better do it curbside."
        "I pull over nearby then head out, Vera following suit."
        "I ring the doorbell once, twice, before I get an answer."
        play sound "DoorOpen.mp3"
        # show alex body neutral
        unknown "Oh, hey!"
        unknown "You're with Sloane, right?"
        show andrea body happy
        ab "That's us."
        "Vera gives a half hearted wave next to me."
        ab "Are you Dominic?"
        "I'm a little thrown by their appearence."
        "They look young for a researcher, but what do I know."
        unknown "Oh, nah, I'm Avery."
        al "I'm Dominic's apprentice. He's in the back right now."
        al "You guys can come in. I'll get him."
        # show alex body embarassed
        show vera body happy
        vl "Awesome. Thanks a bunch."
        "They step aside and oblige."
        "The living room we're greeted with doesn't seem to have been prepared for company."
        "There's a suggestion of a couch beneath a layer of discarded clothing. Boxes and various knick knacks litter the floor."
        "Nothing food or anything else organic, though-thank God."
        "Avery clicks their tongue."
        al "Sorry about the mess."
        al "I'll..."
        "They scamper over to the couch, gathers up an armful of clothing, and deposits into a mound I assume must've once been a laundry hamper."
        show vera body shirt3 neutral at left
        vl "It's all good."
        "Vera takes it as an invitation to sit."
        vl "You can go ahead and get your guy."
        show andrea body happy
        ab "Yeah, don't worry. You should see the van."
        "When they don't say otherwise, I join Vera on the couch."
        "They give an awkward laugh."
        al "Gotcha, no problem."
        "They disappear into the hallway."
        "Once they're out of view, Vera turns to me."
        show vera body shirt3 neutral2
        vl "You know, the car's not nearly as bad as this."
        show andrea neutral
        ab "I was just trying to pacify him. It'd suck if he was on edge the whole time."
        "She leans back."
        vl "It's kinda weird for an academic type to have an apprentice."
        vl "Not like {i}bad{/i} weird, I just haven't heard about it much."
        ab "Really?"
        "Vera's had her skin in the game longer than me. Even if we both went through the whole mentorship process, I'm not sure of the nitty-gritty of it."
        vl "Yeah, I mean. Maybe Dominic's one of those...sleeper nerds."
        ab "{i}Huh?{/i}"
        "Maybe it's some terminology I haven't heard."
        show vera angry
        vl "Like, guys who shove their faces in books, but are actually real killers."
        ab "I've literally never heard anyone call it that."
        vl "Whatever. {i}Anyway.{/i} He probably isn't, so it's not like he can prep poor Alex over there for when the Paragons come calling."
        ab "I mean, look at him. I dunno how much help he needs."
        vl "Muscles aren't gonna do you much when you're dealing with a murder-monster twice your size."
        ab "Guess not."
        "It looks like Vera might elaborate, but she drops the topic after that. She begins to drum her fingers against her knee impatiently."
        "Even if she'd brought it up, it's a sore spot."
        "It makes me wonder how Miranda's doing."
        "She's checked in a few times since I went off on my own, but I haven't spoken to her since everything with Burn."
        "It's probably for the best."
        "I'm yanked from my thoughts by footsteps from the hall."
        dm "Apologies for the wait!"
        #show dominic body neutral
        dm "I was finishing something up."
        dm "Avery said you're Sloane's girls?"
        vl "Sure, you could say that."
        "He navigates through the mess with an expert, unfaltering gait."
        #show dominic happy
        "He puts two hands out, one in front of each of us."
        "...A handshake? I presume."
        "I throw my hat in the ring and shake his right hand."
        "Vera follows suit."
        show andrea happy
        ab "Pleased to meet you."
        show vera neutral
        vl "Likewise!"
        dm "It's just more efficient that way."
        "He explains once we're done."
        "I can just make out Avery lingering in the doorway behind him, not quite sure what to do with themself."
        dm "I only set aside ten minutes for introductions, you know? Already wasted five so far, but as long as you follow me we'll get ahead of schedule."
        "He begins going back the way he came, not bothering to check whether or not we're following."
        "Vera and I exchange glances. She just shrugs and beckons me to go after him."
        "The house gradually becomes less cluttered as we go on."
        "There's a bathroom, a bedroom, and a few other closed doors."
        "All in all, it looks perfectly mundane, until we get to the back of the house."
        "What I assume was once a dining room has been split in half: one part resembles a lab and the other some sort of study."
        "The contrast is sharp."
        "The lab portion has a table with several petri dishes and a microscope; cupboards with glassware of various sizes line the wall."
        "There's even one of those portable camping showers hanging on the wall, that I think's meant to be a makeshift eyewash station."
        "The floor is tiled and the lights are fluorescent."
        "Conversely, the study side is carpeted, with antique-looking lamps overhanging it."
        "The wall is lined with bookshelves, each stacked to the brim. The books are interspersed with the occasional object: skulls, jewels, and the like."
        "Some of the equipment escapes me, though: the machines are definitely dated, but I can't pinpoint the era."
        # show dominic neutral
        dm "So, how much has Sloane told you?"
        show andrea neutral
        ab "You're looking into a disappearance, right? You think it might be Paragon-related."
        ab "She gave us some evidence: newspaper clippings, autopsy file, photo."
        vl "Quality's pretty shit, though."
        "He nods."
        dm "Avery's the one that took it. Don't hold it against them."
        dm "They're a capable little thing! They just don't have a very steady hand."
        show vera neutral2
        vl "Yeah, uh, sorry."
        vl "Didn't mean anything by it."
        "Dominic waves a dismissive hand."
        dm "No trouble, you're correct."
        ab "So, th-"
        show andrea stern
        dm "The assignment, yes."
        # show dominic happy
        "He shuffles past me to a corkboard pinned to a door and pulls a small sheet of stapled papers pinned to it."
        dm "Usually I don't bother with things of this sort, you see."
        dm "The types that just pick off one or two folks aren't anything special - it's tragic! Terrible! - but not unique. And not worth facing."
        "I'm familiar enough with these types to know that the best approach is just nodding and making noises of affrimation."
        dm "But! This one has a {i}preference{/i}, a taste for certain sorts."
        vl "That usually means it's, like-"
        "She clicks her tongue."
        vl "High concept."
        # show dominic neutral
        dm "If you'd like to call it that."
        "A better term for it is 'specific'."
        "More picky a Paragon is, the more likely it is to be able to utilize specific sorts."
        show vera annoyed
        vl "Guess I would."
        show vera neutral2
        ab "In terms of new-"
        dm "New information?"
        dm "Glad you asked"
        show andrea annoyed 
        "Yeah, okay."
        "Not like I had anything relevant to say anyway."
        show andrea stern
        dm "Here's what I have on hand. Not much beyond what I sent Sloane {i}but{/i} it might be something to catch your eye."
        "He hands over the stack to Vera and I look over her shoulder to examine it."
        "It's some kind of report. The format isn't one I've seen before, I don't know if it's something standarized in this field of work."
        "There's a date referring to the last sighting, observations taken from the morgue, and a couple theories."
        "They range from 'some sort of goo thing' to 'big monster the size of a small monster'."
        "I can piece it together well enough though: based on the injuries, it might emit or have a second skin of some sort of toxic-ish material."
        "The last known location of the victim, was somewhere in a town nearby."
        "It's not that bulky and it seems to have an ambush hunting style. It could try and be reforming."
        "That last part's the most concerning one."
        dm "Make sense?"
        "He leans over, just from the side of us."
        show vera neutral2
        vl "Yup! Some kind of moist, acid monster. Can't be that big."
        "Good, we're of the same mind."
        "I offer a thumbs up."
        dm "That's about the shape of it."
        dm "You had some questions-"
        show vera happy
        vl "Questions for you?"
        vl "{i}Glad you asked.{/i}"
        # show dominic confused
        vl "Yeah, a couple."
        "To my chagrin, she looks to me to answer."
        show andrea neutral 
        ab "Ah, yeah."
        "I have to reel in the information before it slips out of my mind."
        ab "I know you look over some special cases, we had a question about certain types."
        ab "I guess-hm-"
        "I click my tongue, hopefully he takes my hesitation for confusion rather than trepidation."
        ab "Strange encounters with Paragons. I know that's not very specific but...odd set ups with humans, I guess."
        ab "One's that are more docile or tricky. That maybe have an interest in working with people besides sucking the life out of them."
        "I wouldn't call Burn 'docile', but parasitic may be overplaying my hand."
        dm "Hmm..."
        "He taps his foot."
        dm "You're right, it {i}isn't{/i} very specific. But I can see what I have. There's certainly cases beyond your usual arrangements." 
        # show dominic happy
        dm "I'll take a look at it while, how about that?"
        ab "Cool."
        "I think that's a safe bet to ask for now."
        vl "We better get going on our way, then."
        "She nudges me in a not-so subtle motion that she wants to evacuate the situation as quickly as possible."
        ab "Mhm, unless there's anything else-"
        dm "Do try and not completely pulverize it. Get some samples, if you can."
        vl "Totally. We're masters of finesse."
        "She grabs my hand."
        vl "C'mon."
        "She moves with such urgency that I barely catch the 'good luck' Dominic throws me, followed by Avery's apologetic 'good luck'."
        "When we're past the doorstep, Vera sighs."
        show vera annoyed       
        vl "Man that guy sucked."   
        "Vera doesn't like most people, but I'll give her this one."
        show andrea annoyed
        ab "He's really trying to make the most of the five seconds it'd take us to respond."
        ab "At least it was quick."
        vl "{i}Yeah{/i}, I guess."
        vl "Info better be worth it."
        ab "Better be..."
        scene carbgazday
        "We step into the car. Our first stop should be near where the disappearence was."
        show vera body shirt3 neutral2 at right
        vl "Was pretty funny when I cut him off, though, got that hundred yard stare."
        show andrea body happy at left
        ab  "Yeah, I'll give you that one."
        "I glance back down at the the place the newspaper mentioned."
        "Based on the map, it isn't far from here."
        show andrea neutral
        ab "We should start with scoping out the place, maybe ask some folks if they've seen anything weird."
        vl "What's the story?"
        vl "Like, why are we asking around?"
        show andrea stern
        "I tap my chin in thought."
        menu:
            "We're doing a documentary for film class.":
                jump filmclass
            "We're a rookie bad-cop good-cop duo on our first case, trying to resolve our differences to bring justice to the victim.":
                jump goodbadcop
            "We're writing vacationing and want to make sure there's no danger.":
                jump vacation

        label filmclass:
            ab "C'mon, have you ever met a film student?"
        show andrea happy
        ab "Most exploitative guys on the planet."
        show vera angry
        vl "I'm a lot of things, but I'm not a film bro."
        vl "Do I {i}look{/i}like a film bro?"
        "I make a show of really considering it."
        ab "A little."
        vl "You're just fucking with me now, aren't you?"
        ab "Yeah."
        vl "But actually, what should we do?"
        jump betteroption

        label goodbadcop:
            ab "Tale as old as time."
        show andrea happy
        ab "It'll probably activate some sort of familiar neuron."
        show vera happy
        vl "...Okay, I'll bite."
        vl "Who's the bad cop and who's the good cop, though?"
        menu:
            "I'm bad, you're good.":
                jump andybad
            "I'm good, you're bad.":
                jump andreagood

        

        label andreagood:
            ab "I think you've got that villanious air."
        vl "Is it the eye?"
        ab "Nah-well, a little-I mean it's the attitude."
        vl "I've always thought myself as more of a wild card, not a bad cop."
        show vera neutral
        vl "Who knows what I'll do, maybe I'll fly off the handle."
        show vera happy
        vl "Or maybe I'll save the day with my out of the box approach."
        ab "Same difference. I think you could instill some sort of fear into witnesses."
        vl "Aw, Andy."
        "She puts a hand over her heart."
        vl "You're too sweet."
        vl "But actually, what should we do?"
        jump betteroption

        label andybad:
            ab "I kind of have the outfit for it, y'know. And the hammer."
        vl "I can kind of see it."
        vl "You've got that devilish air."
        show vera neutral   
        vl "Buuut...I dunno feels like you don't fully sell it. You've got like..."
        "She leans in, a little too close for comfort."
        vl "Too much gentleness in your eyes."
        vl "They'll see right through you."
        ab "And you've got some sort of death stare?"
        show vera happy
        "She rolls her eye, then points to the place where her other one should be."
        vl "I can say I lost it in some mysterious accident that sent me down the wrong path."
        ab "Mmm, makes sense."
        vl "But actually, what should we do?"
        jump betteroption
        

        label vacation:
            ab "It's pretty straightforward."
        ab "If you're going somewhere, you wanna make sure it's not dangerous."
        show vera annoyed
        vl "Who'd wanna vacation in a place like this, though."
        vl "You could find a million of these kinds of towns on every highway exit."
        ab "Do you have a better option?"
        label betteroption:
            show vera neutral2
        vl "Mmm..."
        vl "We could say we're just collecting info for some news thing."
        vl "Like a school paper, or issuing a warning for a campus."
        "I toss the idea around."
        show andrea neutral
        ab "I think that could work. As long as we don't drop too many details about what college we're going to."
        ab "I dunno what kind of schools are even around here."
        vl "We can be subtle."
        vl "It's our speciality, right?"
        ab "'Course."
        "I say, after a few moments of hesitation."
        vl "Awesome!"
        show vera neutral
        vl "We've got a plan, then, drive on."
        "I oblige and start driving."
        "I opt for a populated area near the original site-a strip mall."
        "Even if this thing's the sneaky kind, if it's been seen at all it'd be somewhere with more eyes on it."
        label stripmall:
            scene strip mall
        show vera bodyflip shirt3flip neutral2flipped at right
        show andrea body neutral at left
        "It's the afternoon, so it's pretty busy."
        "On one hand, it's good, because there's a lot of options."
        "On the other, {i}there's a lot of options.{/i}"
        "Gives me a bit of choice paralysis."
        vl "Looks like we got our work cut out "
        ab "Yeah..."
        ab "I think we should split up. Helps cover more ground."
        vl "Cool with me."
        "She's already giving the place a cursory glance."
        vl "Can you do the, like, talking to people part?"
        show vera annoyedflip
        vl "I think talking to Sloane drained me for the last day or two."
        "That's a surprise. It's not often that Vera latches onto something for so long."
        "Grudge or not."
        ab "Good with me, just give me a call when you're done."
        show vera neutralflipped
        vl "Right on."
        "With that, she scampers off."
        "I'm left, relatively, on my lonesome."
        "Thinking on it, when {i}was{/i} the last time I spent more than a few hours without Vera over the last few weeks."
        "We've been traveling in close quarters and have stuck to power in numbers."
        "A break would be good-Vera probably feels the same."
        "'Break' is a bit of an exaggheration, I'm "

            


        

        
        label combat:

            
            default health = 3
            default monster = 3
            
            if health == 0:
                "You lose."
            
            if monster == 0:
                "You win."
           
            "Alright, time to go."
            "..."
            call screen test
            
            #$ time = 3
            #$ timer_range = 3
            #$ timer_jump = 'incorrect'
            #show screen countdown
            
            #"..."
        label incorrect:
            "Not quite."
            $ green_btn_selected = False
            $ health -= 1
           
            ##$ combat_round += 1
            jump combat

        label correct:
            #hide screen countdown
            "Great job, you don't die."
            $ monster -= 1
            ##$ combat_round += 1
            jump combat

        label round2:
            "Okay, we made it."
            "..."
        












        return
            
            