    # The script of the game goes in t32 file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define ab = Character("Andrea", callback = name_callback, cb_name = "andrea", color="#d63e0c")
define vl = Character("Vera", callback = name_callback, cb_name = "vera", color="#9cc7e4")
define sl =  Character("Sloane", callback = name_callback, cb_name = "sloane", color="#9cc7e4")
define w =  Character("Waiter")
define unknown =  Character("Burn", callback = name_callback, cb_name = "??", color="E0DEDE")
define unknown2 = Character("???", callback=name_callback, cb_name = "???", color="#4E575DFF")
define dm = Character("Dominic", callback = name_callback, cb_name = "dominic", color="#d63e0c")
define hk = Character("Rina", callback = name_callback, cb_name = "rina", color="#51408e")

define tn = Character("Teen")
##image vera happy = At('testvera', sprite_highlight('vera'))
##image andrea happy = At('testandrea', sprite_highlight('andrea'))
define al = Character("Avery", callback = name_callback, cb_name = "avery")



layeredimage dominic:
    at sprite_highlight ('dominic')
    group body:
        attribute body:
            "images/Sprites/Dominic/dominic base.png"
    group face:
            attribute happy:
                "images/Sprites/Dominic/dominic happy.png"
            attribute angry:
                "images/Sprites/Dominic/dominic angry.png"
            attribute sad:
                "images/Sprites/Dominic/dominic sad.png"
            attribute neutral:
                "images/Sprites/Dominic/dominic neutral.png"
            attribute thinking:
                "images/Sprites/Dominic/dominic thinking.png"
            attribute excited:
                "images/Sprites/Dominic/dominic excited.png"
layeredimage avery:
    at sprite_highlight ('avery')
    group body:
        attribute body:
            "images/Sprites/Avery/averybase.png"
    group face:
        attribute neutral:
            "images/Sprites/Avery/avery neutral one.png"
        attribute neutral2:
            "images/Sprites/Avery/avery neutral two.png"
        attribute angry:
            "images/Sprites/Avery/avery angry.png"
        attribute embarrassed:
            "images/Sprites/Avery/avery embarrassed.png"
        attribute happy:
            "images/Sprites/Avery/avery happy.png"
        attribute sad:
            "images/Sprites/Avery/avery sad.png"
        attribute thinking:
            "images/Sprites/Avery/avery thinking.png"
        attribute worried:
            "images/Sprites/Avery/avery worried.png"
        

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


default red_btn_selected = False
default attackChance = 0
default next_round = "null"
default tutorial_done = False
default blue_red_combine = False
default flour = False 
default tt = "hello"
default based = False
default head_floured = False
default hmr_hovered = False
default torso_floured = False
default tail_floured = False
default invisible = True
default flour_active = False
default hmrselected = False
default arwselected = False
default something_selected = False
default tailhmred = False
default torsohmred = False
default base_tail = "combat/paragon tail base.png"
default base_tail_hl = "combat/paragon tail base hl.png"
default base_torso = "combat/paragon tail base.png"
default base_torso_hl = "combat/paragon tail base hl.png"
default base_head = "combat/paragon tail base.png"
default base_head_hl = "combat/paragon tail base hl.png"
default andrea_vera = "combat/av good.png"
default flour_found = False
default full_examined = False
default enabled = True
default torso_hit = False
default examine_button_enabled = False
default attack_button_enabled = False
default paragon_enabled = False
default andrea_vera_health = "good"
default head_hit = False
default tooltip_posx = 0
default tooltip_posy = 0

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
        play sound meattunnel
        "...guh...Guh..."
        "The raised mass of burnt tissue around his throat quivers."
        "It sounds like ground meat being pressed through a narrow tunnel."
        show andrea body scared at right
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
            show andrea body sad at right
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
            scene hotel1 with fade
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
        show vera body shirt1 annoyed at vera_spot
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
            show andrea body scared at right 
            ab "{i}There{/i}."
            "I finally manage to grind out."
            ab "I did it. You happy?"
            show andrea body scaredEC at right
            ab "That enough?"
            "I place my hand on the edge of the bathtub. I don't quite know what to do with it."
            "I don't know what it wants me to do from here or how things work now."
            "The answer comes quickly."
            "For a moment I ignite."
            scene andreaprologuecg
            "From the palm up and outward, veins are made kindling, and blood into fuel."
            "It should hurt. If there were any justice in the world it should fry my nerves."
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

    show vera body shirt1 neutral2 at vera_spot
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
    scene hotel1 with fade
   
    "When we leave the bathroom, it's four in the morning."
    "It's the time of year where the sky's already begun to lighten and the first notes of birdsong start up."
    show vera body shirt1 neutral2 at vera_spot
    show andrea body sad at right
    vl "Let's go. Don't wanna linger."
    ab "Right."
    "I grab our stuff. We traveled light in here. Just a few backpacks between us. The rest is in the van."
    label car_go:

        "Vera grabs the dufflebag."
    "We leave the keys on the unmanned front desk down the hall and make our way out to the parking lot."
    "We've been calling it 'the' van or 'our' van. It's really {i}my{/i} van. I got it on my dime: for suspiciously cheap."
    "I really don't want to know what it's been through before I got it, but it's getting the job done."
    "It's nondescript, durable, and has plenty of storage space."
    "If things get real rough, we can even spend the night inside."
    show vera body shirt1 neutral at right with MoveTransition (0.1)
    show andrea body neutral at andrea_shotgun with MoveTransition (0.1)
    vl "Shotgun!"

    ab "Aw, damn, you beat me to it."
    "I say, as if letting her drive was a possibility."
    scene black
    hide andrea
    hide vera
    play sound "CarStartSfx.mp3"
    "I coax the car feebly to life, but it's steady enough once we get on the road."
    play sound "CarAmbient.mp3" loop
    scene car bg aznight
    show vera bodyflip shirt1flip neutralflipped at vera_car
    show andrea body neutral at andrea_car

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
    show andrea body sad at andrea_car
    show vera shirt1flip neutralflipped at vera_car    
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
    show vera annoyedflip
    "Vera scoffs."
    vl "Semantics. Anyway."
    vl "She won't ask too many questions as long as we're on top of it."
    vl "She'll probably let us chat her up too."
    ab "Hopefully the guys she has on retainer are actually useful."
    vl "If not we'll just look somewhere else."
    "..."
    vl "Or die, I guess."
    ab "Don't say that."
    show vera bodyflip shirt1flip happyflipped
    vl "I'm not saying we'll do that. It's just always a possibility."
    vl "Anytime you do anything, technically."
    ab "Do that on your own time, then."
    show vera annoyedflip
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
    show vera neutral2flipped
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
        show vera bodyflip shirt1flip neutralflipped
        vl "That wasn't {i}not{/i} part of it."
        vl "Three birds with one stone."
        ab "What's the third one?"
        show vera neutral2flipped
        vl "Guy was an asshole, remember?"
        vl "Don't even have to be bogged down by guilt if we're doing a public service."
        "Right. Sure."
        "The now-corpse deserved what was coming to it."
        "It's better for both of us to take Vera at her word."
        ab "You didn't really answer, though. Are you good?"
        vl "Right now, I'm tired."
        show vera annoyedflip
        vl "And I wish this car had better AC."
        vl "And I wish we weren't in bumfuck Arizona."
        vl "But besides that, I'm good."
        show andrea body neutral
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
        show vera neutralflipped
        vl "Waffle Home?"
        ab "Right, there's like a million of those out here."
        vl "I'm not going there."
        show andrea body happy
        ab "What, you too ritzy for it?"
        "I've seen her eat food off the floor."
        vl "You don't wanna know what happened the last time I went into a Waffle Home."
        ab "Well, now I do."
        show vera neutral2flipped
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
        show vera neutralflipped
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
        show vera annoyedflip
        vl "{i}No.{\i} That's, like, the lamest option."
        vl "Try again."
        jump look
    label picked_sky:
        ab "No moon out, basically opaque."
        show vera annoyedflip
        vl "No, it's a dark indigo at best."
        vl "Maybe with hints of grey, if you squint."
        vl "Try again."
        jump look
    label picked_wheel:
        ab "The one on your side."
        "It'd been there when I got the car."
        "I've tried the whole gambit to get it off: bleach, car cleaner, even trying to scrape it off."
        "I don't even know what it is."
        show vera bodyflip happyflipped
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
    show vera annoyed shirt1 body at vera_spot
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
    show andrea body neutral at right
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
    show vera body shirt2 annoyed at vera_spot
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
    show vera body shirt2 happy at vera_spot
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
    show vera body shirt2 neutral at vera_spot
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
    show vera body shirt2 neutral2 at vera_spot
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
    scene diner with fade
    "The drive over is shorter than the last. Most of the time is spent finding a place to park."
    "The Honey Tiger Diner is probably the most put-together amenity we've seen over the last two weeks."
    "Even if it's not anything fancy- Sloane has standards, but she's not shilling out for us. the fact that the sign on the top isn't trying to extricate itself from the wall and the windows aren't cobwebbed is good enough."
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
        "It says he was found dead by the side of the road, around the same area."
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
            show vera bodyflip shirt2flip happyflipped
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
            ab "I'm gonna-bathroom, I'll be right back."
            
            hide andrea body scared with moveoutright
            scene diner with fade
            label bathroom_diner:
                "I don't bother asking where it is, I can figure it out."
            "I can feel stares trailing me as I move."
            "Or maybe I don't. Fuck, maybe I'm just losing my grip."
            "I follow the sign to the back of the restaurant and go in."
            stop music
            play sound "DoorOpen.mp3"
            scene diner at night_filter
            "It's blissfully empty."
            "I screw my eyes shut and bring my hands to my face, nails scratching at the scalp."
            show andrea body scaredEC
            scene diner at night_filter:
                blur 4
                pause 0.3
                blur 5
                pause 0.3
                blur 6
                pause 0.3
                blur 5
                pause 0.3
                blur 4
                pause 0.3
    
                repeat 
            show andrea body scaredEC
            "I keep my mouth locked firmly tight. I don't know whether it's vomit or a sob or a scream that's climbing up my throat."
            "I can't be doing this, not here."
            "This is fucked, I'm fucked. This isn't a luxury I can afford."
            "I cup a handful of water and throw it in my face."
            scene diner at night_filter:
                blur 8
                pause 0.2
                blur 9
                pause 0.2
                blur 10
                pause 0.2
                blur 9
                pause 0.2
                blur 8
                pause 0.2
    
                repeat 
            show andrea body scaredEC
            "It's lukewarm. My free hand tightens on the sink."
            "Can't get my head straight; can't keep a face up for Sloane; can't choke down goddamn food."
            "Can't bash in a skull without Vera dropping it in my lap like a cat bringing in roadkill."
            "This is only the first one."
            "What's gonna happen next?"
            "I know Burn's listening. I can't feel it, but if I wanted to-if I wanted to pry myself open like rotten floorboards-I could."
            "I don't need to; I already know what it thinks."
            "{i}Stupid little girl.{/i}"
            "{i}Ungrateful coward.{/i}"
            scene diner at night_filter:
                blur 9
                pause 0.2
                blur 10
                pause 0.2
                blur 11
                pause 0.2
                blur 10
                pause 0.2
                blur 9
                pause 0.2
    
                repeat 
            show andrea body scaredEC
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
            scene diner at night_filter:
                blur 8
                pause 0.2
                blur 9
                pause 0.2
                blur 10
                pause 0.2
                blur 9
                pause 0.2
                blur 8
                pause 0.2
    
                repeat 
            show andrea body scaredEC
            "I feel myself mumble out the words more than I hear myself say them."
            "Eighteen years and twelve grades of English, I have no idea why this is the thing I kept from it."
            ab "{i}Burning bright.{/i}"
            scene diner at night_filter:
                blur 4
                pause 0.3
                blur 5
                pause 0.3
                blur 6
                pause 0.3
                blur 5
                pause 0.3
                blur 4
                pause 0.3
    
                repeat 
            show andrea body scaredEC
            "The stanza's woven itself into the grooves of my muscle memory."
            "It's a ritual, habit, whatever."
            "It gives me something to do, keeps me grounded with a rhythm."
            "I'm used to using it to stay calm when something's about to bite my head off."
            "But, I'll welcome it now, anyhow."
            scene diner at night_filter:
                blur 1
                pause 0.3
                blur 2
                pause 0.3
                blur 3
                pause 0.3
                blur 2
                pause 0.3
                blur 1
                pause 0.3
    
                repeat 
            show andrea body scaredEC
            "Not quite a comfort, but verging on one."
            show andrea body scared
            scene diner at night_filter
            show andrea body scared
            "I pry my eyelids open."
            "My hearts' stopped syncopating, and I will my hands into stillness after a few stern glares."
            "There. Managable."
            "Enough to go back out and finish whatever pleasantries it'll take to get out of here, then deal with whatever Vera inevitably latches on to."
            scene diner with fade
            
            
            "By the time I make it back to the table, my back's straight and I've swapped out the bile climbing up my throat for idle conversation."
            show andrea body neutral with MoveTransition(0.8, enter=offscreenright):
                xalign 0.9
                yalign 1.0
            show sloane body stern:
                xzoom -1.0
                xalign -0.1
                yalign 1.0
            show vera bodyflip shirt2flip neutral2flipped: 
                xalign 0.98
                yalign 1.0
            "Neither Sloane nor Vera put much effort into hiding the fact they're suspicious, but don't stop me when I pivot away."
            
            "The twenty minutes until we get our check go by quickly."
            show andrea body sad
            "Sloane wishes us good luck on the job and hopes our-"
            show sloane smile
            sl "-newfound freedom serves us well."
            "I thank her for the meal. She leaves."
            "The waiter asks if we want to take the food to go, and Vera answers 'yes' before I can decline."  
            hide andrea
            hide vera
            "Neither of us say anything."
            "I lead the way back to the car and she has the courtesy to wait for me to put my keys in the ignition before starting."

            label car_argument:
                stop music
            scene carbgazday with fade
            show andrea body sad at andrea_car
            show vera bodyflip shirt2flip annoyedflip at vera_car
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
            show vera bodyflip shirt2flip angryflipped
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
            show andrea body angry
            ab "At least pretend to care."
            "Vera clicks her tongue."
            vl "You barely did anything."
            "She leans in closer. It's somewhere between a confession and a dare."
            show vera bodyflip shirt2flip angryflipped with move:
                xoffset -100
            vl "{i}I{/i} found him."
            show vera angryflipped with MoveTransition(0.1):
                xoffset -200
            vl "{i}I{/i} took him out."
            show vera angryflipped with MoveTransition(0.1):
                xoffset -300
            vl "{i}I{/i} did it even when he begged for his stupid little life like a dog."
            show vera angryflipped with MoveTransition(0.1):
                xoffset -400
            vl "{i}I{/i} dragged him halfway across town because I knew {i}you{/i} couldn't do it."
            ab "Don't act like this is about me."
            "Another scratch of laughter."
            show vera bodyflip shirt2flip neutralflipped
            vl "It's always about you! This entire damn thing is about you."
            vl "It's your deal. It's your hit list. Your lifeline."
            ab "I'm just your excuse to do whatever you want, hurt whoever you want."
            ab "Easy execution block right in front of you."
            ab "Me dying was probably the best thing to happen to you."
            show vera bodyflip shirt2flip neutralflipped
            vl "Tell me to leave then."
            "Her hand hovers over the car door; a threat."
            vl "Kick me out of this car."
            vl "It's yours."
            show andrea body angry
            ab "Don't-..."
            vl "No, go on."
            vl "You don't need me around. You can take care of yourself just fine. You're way stronger now."
            show vera bodyflip shirt2flip happyflipped with move:
                xoffset -500
            "Another hairbreadth closer."
            
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
            show vera bodyflip shirt2flip annoyedflip
            vl "Yeah, you caught me. I don't care about whoever you turned into mincemeat."
            "Of course she was just placating me about who he was. She probably didn't even get his name before cutting his throat."
            vl "Maybe I liked cutting him up. Maybe I didn't. Maybe you're going to spend your entire life being haunted by guilt."
            vl "He died the same either way. Whoever's next will, too."
            vl "It's either you or them. Take Burn up on it."
            show andrea body annoyed
            ab "You know it won't listen."
            "I'm latching onto a rhetorical. I just want to do something besides sit mutely like I'm a child being given a lecture."
            show vera bodyflip shirt2flip neutral2flipped
            vl "Feel however bad you want. Cry yourself to sleep. Bottle it up. You're good at that."
            vl "Just don't let it screw us over. You got a chance most people didn't it and it'd be stupid if you wasted it-because you couldn't keep it together over breakfast and someone got too curious."
            vl "What happened sucks. Not fair. Etcetera etcetera, But it did so-..."
            "She puts her hands up."
            vl "Guess you'll have to deal with it."
            show andrea body sad 
            ab "I {i}am{/i} dealing with it."
            ab "Maybe if you give me more than twelve hours, I'll save some more face."
            show vera bodyflip shirt2flip sadflipped at vera_car with move:
                xoffset 0
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
                scene carbgazday with fade
            hide andrea
            hide vera
            "We drive for a while."
            "I consider going for the radio and a glance out of the corner of my eye tells me Vera is too, but neither of us make a move."
            "A tacid admission that we're both too spent to talk."
            scene car bg aznight with fade
            "We track down a place pretty easy, around eight."
            play sound "SFX/keys1.mp3"
            "I pay the front desk. We get the keys."
            "The room's fine, but not particularly clean."
            "We go to bed early."
            scene hotel1 with fade
            "I don't dream."
            "Neither of us thinks to set an alarm, so it's the sun that wakes me."
            "Six in the morning it looks like: crack of dawn."
            "It's unusual for Vera to be up before me."
            "Even if she's a light sleeper, she'll usually go back to bed whenever she rouses, until she deems the day worthy enough to drag herself into."
            "But, she comes out of the bathroom just as I sit up."
            "She's already dressed and it smells like she's showered."
            show vera body shirt3 neutral2 at vera_spot
            vl "...Hey."
            "I rub the sleep from my eyes."
            show andrea body sad at right
            ab "Hey."
            play music "audio/SFX/AmbientHotel.wav"loop
            play sound "audio/SFX/ClothFlap.mp3"
            "I ruffle through my bag to pick out my clothes. I take longer than I really need."
            hide vera with Dissolve(0.3)
            "Vera's eyes boring into my back don't help."
            vl "How'd you sleep?"
            ab "All right."
            "I take off my bonnet, then pull out a shirt."
            ab "You?"
            vl "Good."
            vl "Mostly."
            vl "Air conditioner kept me up for a bit."
            ab "Sounds like a pain."
            play sound "audio/SFX/ClothesPutOn.mp3"
            "I pause to change into my clothes for the day."
            show andrea sad
            ab "We really know how to pick these places, huh?"
            "After all the times we've been at each other's throats, you'd think we'd have developed a protocol for this."
            vl "Technically, it was your call."
            "Her voice is soft. It's not apologetic, but there's a weak attempt to lift the octave into some sort of joke."
            ab "I'll let you pick the next one, then."
            ab "You can pay for it, too."
            show andrea body happy
            "I take the fall to be the first to break a smile."
            "The tension drops from her frame."
            show vera body shirt3 neutral at vera_spot
            vl "Nevermind. You should consider a job in real estate after all this."
            "And that's that."
            hide vera
            hide andrea
            "I shower, inching the heat up centigrade by centigrade 'til it hits as hot as I can handle."
            "It's early, so I can afford to drag my feet a little: I take my time to wash whatever tension sleep hasn't soothed down the drain."
            "Not everything is purged, but it's enough that when I step back out into the motel room, conversation doesn't feel like pantomime."
            show vera body shirt3 neutral2 at vera_spot
            vl "Ready to go?"
            show andrea body neutral at right
            ab "I'm good."
            ab "I think the guy's an hour out."
            ab "We should stick to the same story we told Sloane. He's in touch with her."
            "I glance around the room."
            show andrea stern
            "There isn't much to pack. It's a lot lighter load than last night."
            ab "Off we go, then."
            "We drop off the keys, check that no one's snuck up on us in the parking lot, then get back to the car."
            play sound "audio/CarStartSFX.mp3"
            play sound "CarAmbient.mp3" loop
            scene carbgazday with fade
            show vera bodyflip shirt3flip neutral2flipped at vera_car
            show andrea body neutral at andrea_car
            "The heaviness from last night hangs in the air for a moment, then dissipates into the rumbling of the road."
            vl "...Got any tunes?"
            "One of the few things Vera relents on is my ownership of the radio."
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
                show vera happyflipped
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
        show vera neutral2flipped
        vl "We should get breakfast."
        "She checks out the window."
        vl "We're shooting towards brunch, at this point."
        "I've been too focused on driving to really notice but, yeah, haven't eaten anything since yesterday afternoon."
        ab "Right. Wanna hunt down a place?"
        vl "Drive-through, probably, it'll save time."
        show vera neutralflipped
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
        "It's probably just validating whatever suspicions she has about my ability to eat without spiraling."
        "She's not all the way off the mark: the patty looks a lot less appetizing on second glance, though that could just be a symptom of this place's quality."
        "I follow in her footsteps and shove it in my mouth as quickly as I can. It goes down easy. No reek of char. Nothing."
        show vera neutral2flipped
        "Vera's still staring."
        
        show andrea annoyed
        ab "I'm fine, you know. I'm not gonna choke if you don't monitor me."
        vl "I know, I know."
        show vera happyflipped
        vl "Just missed a spot."
        "She puts a finger to my chin and brushes her thumb against my bottom lip, wiping away whatever food scrap was left over."
        "Vera keeps it there a few seconds longer. Her skin's rough, a product of years spent carving callouses into it."
        show andrea body neutral
        ab "Hey-"
        vl "Hey what?"
        play sound "audio/SFX/ClothMove.mp3"
        "She retracts her hand and wipes it against her pant leg."
        show vera neutralflipped
        vl "I'm just being helpful."
        play sound "audio/SFX/Crumple.mp3"
        "I crumple up the paper that'd covered my burger and toss it into the makeshift plastic-bag trashcan on the backseat."
        ab "Thanks."
        "I don't know if taking the reassurance at face value or scrutinizing it into oblivion is the call here."
        "I settle on a middle ground: starting the car and getting back on the road."
        vl "This the spot?"
        "Vera asks me after we reach some sign of civilization, a few miles out."
        "The address we'd been given read like a home address, so it feels like it should be in a neighborhood."
        "Rows of cookie cutter houses greet us."
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
        label doms_place:
            play sound "DoorOpen.mp3"
        show avery body neutral at center:
            xoffset 200

        unknown2 "Oh, hey!"
        show avery neutral2
        unknown2 "You're with Sloane, right?"
        show andrea body happy
        ab "That's us."
        "Vera gives a half hearted wave next to me."
        ab "Are you Dominic?"
        "I'm a little thrown by their appearence."
        "They look young for a researcher, but what do I know."
        show avery body happy
        unknown2 "Oh, nah, I'm Avery."
        al "I'm Dominic's apprentice. He's in the back right now."
        al "You guys can come in. I'll get him."
        
       
        vl "Awesome. Thanks a bunch."
        
        scene livingroomdom with dissolve
        play music "Music/Ambience/upbeatambient.mp3"
       
        "The living room we're greeted with doesn't seem to have been prepared for company."
        "There's a suggestion of a couch beneath a layer of discarded clothing. Boxes and various knick knacks litter the floor."
        "No food or anything else organic, though-thank God."
        "Avery clicks their tongue."
        show avery body embarrassed:
            xalign 1.3
            yalign 1.0
        al "Sorry about the mess."
        al "I'll..."
        play sound "audio/SFX/ClothPutDown.mp3"
        "They scamper over to the couch, gather up an armful of clothing, and deposits into a mound I assume must've once been a laundry hamper."
        show vera body shirt3 neutral at left
        vl "It's all good."
        "Vera takes it as an invitation to sit."
        vl "You can go ahead and get your guy."
        show andrea body happy:
            xalign 0.2
            yalign 1.0 
            xzoom -1.0
        ab "Yeah, don't worry. You should see the van."
        "When they don't say otherwise, I join Vera on the couch."
        "They give an awkward laugh."
        al "Gotcha, no problem."
        "They disappear into the hallway."
        play sound "SFX/FootSteps1.mp3"
        hide avery with dissolve
        "Once they're out of view, Vera turns to me."
        show vera body shirt3 neutral2
        vl "You know, the car's not nearly as bad as this."
        show andrea neutral:
            xalign 0.4
            yalign 1.0 
            xzoom 1.0
        ab "I was just trying to pacify them. It'd suck if they were on edge the whole time."
        "She leans back."
        vl "It's kinda weird for an academic type to have an apprentice."
        vl "Not like {i}bad{/i} weird, I just haven't heard about it much."
        ab "Really?"
        "Vera has had her skin in the game longer than me. Even if we both went through the whole mentorship process, I'm not sure of the nitty-gritty of it."
        vl "Yeah, I mean. Maybe Dominic's one of those...sleeper nerds."
        ab "{i}Huh?{/i}"
        "Maybe it's some terminology I haven't heard."
        show vera angry
        vl "Like, guys who seem  whimpy, but have got something real nasty under the surface."
        ab "I've literally never heard anyone call it that."
        vl "Whatever. {i}Anyway.{/i} He probably isn't- gonna leave poor Avery floundering when they deal with a real nasty Paragon." # add 'he's' after isn't. The isn't on its own is confusing and makes it look like she's saying Dominic wouldn't leave Avery to die
        ab "That's sort of presumptious."
        ab "We've seen them for maybe two seconds and we haven't even met Dominic."
        show vera neutral2
        vl "Just an educated guess."
        "It looks like Vera might elaborate, but she drops the topic after that. She drums her fingers against her knee impatiently."
        "Even if she'd brought their mentorship up, it's a sore spot."
        "It makes me wonder how Miranda's doing."
        "She's checked in a few times since I went off on my own, but I haven't spoken to her since everything with Burn."
        "It's probably for the best."
        play sound "SFX/FootSteps2.mp3"
        "I'm yanked from my thoughts by footsteps from the hall."
        label dom_show_up:
            dm "Apologies for the wait!"
            show dominic body neutral:
                xpos 0.45
                yalign 1.0
        dm "I was finishing something up."
        dm "Avery said you're Sloane's girls?"
        vl "Sure, you could say that."
        "He navigates through the mess with an expert, unfaltering gait."
        show dominic body happy
        "He puts two hands out, one in front of each of us."
        "...A handshake? I gather."
        "I throw my hat in the ring and shake his right hand."
        "Vera takes the left, her lip twitching downward just the slightest bit."
        show andrea happy:
            xalign 0.2
            yalign 1.0 
            xzoom -1.0
        ab "Pleased to meet you."
        show vera neutral
        vl "Likewise!"
        dm "It's just more efficient that way." # remove just as a filler word
        "He explains once we're done."
        "I can just make out Avery lingering in the doorway behind him, not quite sure what to do with themself."
        dm "I only set aside ten minutes for introductions, you know? Already wasted five so far, but as long as you follow me we'll get ahead of schedule." # I would also take out 'ya know' here. If he's trying to be efficient he'd be more to the point
        "He heads back the way he came, not bothering to check whether or not we're following."
        "Vera and I exchange glances. She just shrugs and beckons me forward."
        "The house gradually becomes less cluttered as we go on."
        "There's a bathroom, a bedroom, and a few other closed doors."
        "All in all, it looks perfectly mundane, until we get to the back of the house."
         
        "What I assume was once a dining room has been split in half: one part resembles a lab and the other some sort of study."
        "The contrast is sharp."
        "The lab portion has a table with several petri dishes and a microscope; cupboards with glassware of various sizes line the wall."
        "There's even one of those portable camping showers hanging on the wall, that I think's meant to be a makeshift eyewash station."
        "The floor is tiled and the lights are fluorescent."
        "Conversely, the study side is carpeted, with antique-looking lamps overhanging it."
        "The wall is lined with overstuffed shelves. The books are interspersed with objects: skulls, replica weapons, and the like."
        "At least I assume they're replicas."
        "Some of the equipment escapes me: the machines are definitely dated, but I can't pinpoint the era."
        show dominic body neutral:
            xpos 0.45
            yalign 1.0
        dm "So, how much has Sloane told you?"
        show andrea body neutral:
            xalign 0.2
            yalign 1.0 
            xzoom -1.0
        
        ab "You're looking into a disappearance, right? You think it might be Paragon related."
        ab "She gave us some evidence: newspaper clippings, autopsy file, photo."
        show vera body neutral shirt3 at left
        vl "Quality's pretty shit, though."
        "He nods."
        dm "Avery's the one that took it. Don't hold it against them."
        dm "They're a capable little fellow! They just don't have a very steady hand."
        "{i}Little fellow?{/i} They can't be much younger than me."
        show vera neutral2
        vl "Yeah, uh, sorry."
        vl "Didn't mean anything by it."

        "Dominic waves a dismissive hand."
        show dominic body happy
        dm "No trouble, you're correct."
        show andrea stern
        ab "So, th-"
        show dominic body excited
        dm "The assignment, yes."


        "He shuffles past me to a corkboard pinned to a door and pulls off a small sheet of stapled papers pinned to it."
        show dominic body neutral
        play sound "SFX/PaperRustles.mp3"
        dm "Usually I don't bother with things of this sort, you see." #I'd place the 'usually' after 'I don't.' Not a big deal just my preference 
        dm "The types that just pick off one or two folks aren't anything special - it's tragic! Terrible! - but not unique enough to be worth the trifle."
        dm "But! This one's right in my backyard."
        dm "I figured I may as well, it's been a while since I've gotten to poke around one of those bugger's insides."
        ab "{i}Mhm.{/i}"
        "In my experience, the best way to deal with these types is to nod and make noises of affirmation."
        ab "In terms of new-"
        dm "New information?"
        dm "Glad you asked!"
        show andrea annoyed 
        "Yeah, okay."
        "Not like I had anything relevant to say anyway."
        show andrea stern
        show dominic body neutral
        dm "Here's what I have on hand. Not much beyond what I sent Sloane, {i}but{/i} it might be something to catch your eye."
        "He hands over the stack to Vera and I look over her shoulder to examine it."
        "It's some kind of report. The format isn't one I've seen before, I don't know if it's a standard in this field of work."
        "There's a date of the last sighting, observations taken from the morgue, and a couple theories."
        "They range from 'some sort of goo thing' to 'big monster the size of a small monster'."
        "I can piece it together well enough though: based on the injuries, it might emit or have a second skin of some sort of corrosive material."
        "The last known location of the victim was in a town nearby."
        "It's not that bulky and it seems to have an ambush hunting style."
        "So, either it's  naturally on the smaller side, or it's trying to reform."
        dm "Make sense?"
        "He leans over, just from the side of us."
        show vera neutral2
        vl "Yup! Moist, acid monster. Can't be that big."
        vl "Does it have any preference of victims?"
        dm "There haven't been enough cases to tell."
        "Some Paragons are like that. They have a taste for certain kinds of people."
        "Folks drowning in grief or rage. Or the complete opposite: those with a lot to lose."
        dm "That's about the shape of it."
        dm "You had some questions-"
        show vera happy
        vl "Questions for you?"
        show dominic body thinking
        vl "{i}Glad you asked.{/i}"
       
        vl "Yeah, a couple."
        "To my chagrin, she looks to me to answer."
        show andrea neutral 
        ab "Ah, yeah."
        "I have to reel in the information before it slips out of my mind."
        ab "I know you look over some special cases, we had a question about certain types."
        ab "I guess-hm-"
        "I click my tongue."
        ab "Strange encounters with Paragons. I know that's not very specific but...odd set ups with humans, I guess."
        ab "One's that are more docile or tricky. That maybe have an interest in clinging onto people beyond sucking the life out of them."

        "I wouldn't call Burn 'docile', but saying 'parasitic' may be overplaying my hand."
        dm "Hmm..."
        "He taps his foot."
        dm "You're right, it {i}isn't{/i} very specific. But I can see what I have. There're certainly cases beyond your usual arrangements." 
        show dominic body happy
        dm "I'll take a look at it while you're out, how about that?"
        vl "Cool."
        "I think that's a safe bet to ask for now."
        vl "We better get going on our way, then."
        "She nudges me in a not-so subtle motion that she wants to evacuate the situation as quickly as possible."
        ab "Mhm, unless there's anything else-"
        dm "Do try and not completely pulverize it. Get some samples, if you can."
        vl "Totally. We're masters of finesse."
        "She grabs my hand."
        vl "C'mon."
        "She moves with such urgency that I barely catch the thumbs up Dominic throws me, followed by Avery's apologetic 'good luck'."
        play sound "SFX/CarDoor.mp3" # I would maybe change music to different ambient track here if we have options. If not here then when the next scene starts
        scene carbgazday with fade
        "When we're past the doorstep, Vera sighs."
        show vera bodyflip annoyedflip shirt3flip at vera_car      
        vl "Man, that guy sucked."   
        "Vera doesn't like most people, but I'll give her this one."
        show andrea body annoyed at andrea_car
        ab "He's really trying to make the most of the five seconds it'd take us to respond."
        ab "Kinda weird about Avery too. Like, condescending."
        ab "At least it was quick."
        vl "I guess."
        show andrea neutral
        ab "It is what it is. Not gonna be our problem for long."
        show vera neutral2flipped
        vl "You could stand to be a little less stoic about things sometimes, you know?"
        vl "At least rag on him a bit longer."
        show andrea stern   
        ab "What, do you want me to go for the throat?"
        ab "He has advice, we should play nice."
        vl "We're helping him out, he can deal with a bit of backbone."
        ab "I just don't need to give him any reasons to be on edge."
        ab "Low profile, remember?"
        "Me especially."
        "Vera bites her lip."
        vl "Yeah, yeah."
        vl "Info better be worth it."
        ab "Better be..."
       
        
        "Our first stop should be near where the disappearence was."
        show vera bodyflip shirt3flip neutral2flipped 
        vl "Was pretty funny when I cut him off, though, got that hundred yard stare."
        show andrea body happy 
        ab  "I'll give you that one."
        "I glance back down at the the place the newspaper mentioned."
        "Based on the map, it isn't far from here."
        show andrea neutral
        ab "We should start with scoping out the place, maybe ask some folks if they've seen anything weird."
        vl "What's the story?"
        vl "Why are we asking around?"
        show andrea stern
        "I tap my chin in thought."
        menu:
            "We're doing a documentary for film class.":
                jump filmclass
            "We're a rookie bad-cop good-cop duo on our first case, trying to resolve our differences to bring justice to the victim.":
                jump goodbadcop
            "We're vacationing and want to make sure there's no danger.":
                jump vacation

        label filmclass:
            ab "C'mon, have you ever met a film student?"
        show andrea happy
        ab "Exploitation's part of the curriculum."
        show vera angryflipped
        vl "I'm a lot of things, but I'm not a film bro."
        show vera neutral2flipped
        vl "Do I {i}look{/i} like a film bro?"
        "I make a show of really considering it."
        show andrea neutral
        ab "A little."
        vl "You're just fucking with me now, aren't you?"
        show andrea happy
        ab "Yeah."
        vl "But actually, what should we do?"
        jump betteroption

        label goodbadcop:
            ab "Tale as old as time."
        show andrea happy
        ab "It'll probably activate some sort of familiar neural pathway."
        show vera happyflipped
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
        ab "Nah-well-"
        show andrea neutral
        ab "A little-"
        show andrea happy
        ab "I mean it's the attitude."
        vl "I've always thought myself as more of a wild card, not a bad cop."
        show vera neutralflipped
        vl "Who knows what I'll do, maybe I'll fly off the handle."
        show vera happyflipped
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
        show vera neutralflipped   
        vl "Buuut...I dunno feels like you don't fully sell it. You've got like..."
        "She leans in, bracing herself against the parking brake."
        show vera neutralflipped with MoveTransition(0.4):
            xoffset -200
        vl "Too much gentleness in your eyes."
        vl "They'll see right through you."
        ab "And you've got some sort of death stare?"
        show vera happyflipped
        "She rolls her eye, then points to the place where her other one should be."
        vl "I can say I lost it in some mysterious accident that sent me down the wrong path."
        ab "Mmm, makes sense."
        show vera neutral2flipped with MoveTransition(0.4):
            xoffset 0
        vl "But actually, what should we do?"
        jump betteroption
        

        label vacation:
            ab "It's pretty straightforward."
        ab "If you're going somewhere, you wanna make sure it's not dangerous."
        show vera annoyedflip
        vl "Who'd wanna vacation in a place like this, though."
        vl "You could find a million of these kinds of towns on every highway exit."
        ab "Do you have a better option?"
        label betteroption:
            show vera neutral2flipped
        vl "Mmm..."
        vl "We could say we're just collecting info for some news thing."
        vl "Like a school paper, or issuing a warning for a campus."
        "I toss the idea around in my brain."
        show andrea neutral
        ab "I think that could work. As long as we don't drop too many details about what college we're going to."
        ab "I dunno what kind of schools are even around here."
        vl "We can be subtle."
        vl "It's our speciality, right?"
        ab "...{w=0.4}'Course."

        vl "Awesome!"
        show vera neutralflipped
        vl "We've got a plan, then, drive on."
        "I oblige and start driving."
        "I opt for a  area near the original site-a strip mall."
        play sound "audio/SFX/CarStop.mp3"
        "Even if this thing's the sneaky kind, if it's been seen at all it'd be somewhere with more eyes on it."
        label stripmall:
            scene parking lot with fade
        play music "audio/Music/Ambience/ominousambient.mp3"
        "It's the afternoon, so it's pretty busy."
        "On one hand, it's good, because there're a lot of options." # i would just write out 'there are' instead of 'there're' for the next two lines. Feels a lil less awkward
        "On the other, {i}there're a lot of options.{/i}"
        "Gives me a bit of choice paralysis."
        show vera body shirt3 neutral2 at vera_spot
        vl "Looks like we got our work cut out for us."
        show andrea body neutral at right
        ab "Yeah..."
        ab "I think we should split up. Helps cover more ground."
        vl "Cool with me."
        "She's already giving the place a cursory glance."
        vl "I can do a sweep of the area, maybe you could try and get some accounts?"
        vl "Not in a super chatty mood."
        show vera annoyed
        vl "I think Sloane drained me for the last day or two."
        "That's a surprise. It's rare for Vera to latch onto something for so long."
        "Grudge or not."
        ab "Yeah, just give me a call when you're done."
        show vera neutral
        vl "Right on."
        play sound "audio/SFX/FootStepRoad.mp3"
        hide vera  with moveinoutfade
        "With that, she scampers off."
        "I'm left, relatively, on my lonesome."
        "Thinking on it, when {i}was{/i} the last time I spent more than a few hours without Vera over the last few days?"
        "We've been traveling in pretty close quarters."
        "A break would be good-Vera probably feels the same."
        "'Break' is a bit of an exaggheration, I'm within five minutes of her and it's not really down time."
        "But, I'm alone in my thoughts, for better or worse."
        "Better find something useful to fill them with."
        "Vera said she wanted to handle more on the ground work and wants me to see if anyone's a witness."
        "It's probably for the best I act as the face here."
        "Time to flex those people skills."
        "I'm excited to talk to someone who's somewhere in the field of normal, even if it means having to tiptoe around some stuff."
        "My best bet is one of the workers here."
        "The place in closest proximity is the UuaUua's."
        "It's a rest-stop-slash-gas-station. It's been a while since I've been to one."
        "Has good hoagies."
        menu:
            "Approach the UuaUua's.": #is there supposed to be more options here or is the choice added here for pacing reasons?
                jump UuaUuas

        label UuaUuas:
            stop music
            scene uuauua with fade
            show andrea body neutral at right
            play sound "SFX/UuaUuaBell.mp3" #add music for this section, silence is awkward
            "It's identical to every other one I've been to."
            "Bunch of shelves, a place to eat near the back."
            "It's manned by a beleagured, hooded-eye teenager."
            "I wince internally, hope I don't make things worse for too long."
            "I wait for them to finish talking to the customer in front of me."
            ab "Hey, uh, do you have a minute?"
            #show employee
            tn "Hi."
            "..."
            tn "{w=0.2}Yes."
            "They don't look mad, just disappointed."
            show andrea body happy
            ab "Thank you. I'm just doing an assignment for my journalism course."
            "Sure, that sounds about right."    
            show andrea neutral
            ab "It's about a disappearence earlier. Have you heard about it?"
            tn "Oh..."
            tn "Yeah, I think."
            pause 0.3
            tn "It's the lady that got, like, murdered, right?"
            show andrea body stern
            ab "I don't think she was murdered, it's still a disappearence for now."
            ab "At least I'm pretty sure. I haven't looked into it much."
            tn "Ohh...right."
            tn "Yeah."
            tn "It was another dude who died."
            "She already knows about that, cool. I won't have to loop it in."
            "I nod."
            show andrea body neutral
            ab "I heard about that too, I'm kinda curious. But, I'm looking into Ms. Planchart's-"
            tn "Who?"
            ab "The woman that went missing."
            tn "Ohhh...okay."
            ab "I'm looking into her disappearence. I was wondering if you knew anything. Maybe you talked to her?"
            ab "See anything weird around?"
            "It's hard to navigate a case with normal folks."
            "I have to talk around the murder monster bits. You can't lead with anything specific."
            tn "I don't think I've met her. I mean, I dunno. I don't really ask people's names."
            tn "And weird? Weird, how?"
            "My point exactly. I have to nudge towards the question, without stepping over the threshold into sounding like a freak."
            $ askedanimal = False
            $ askedmess = False
            label teengirl:
                if askedanimal == True and askedmess == True:
                    jump afterteen
            menu:
        
                "Weird how?"

                "Animals" if askedanimal == False :
                    jump weirdanimals
                "Messes." if askedmess == False:
                    jump weirdmesses
                

            label weirdanimals:
                $ askedanimal = True
                show andrea body neutral
                
                if askedmess == True:
                    ab "One more thing."
                    ab "Has there been any reports of animals around?"
                ab "We're thinking it could be-or there's a theory that it could be some sort of animal attack."
                tn "Like a raccoon?"
                show andrea body stern
                ab "I was thinking more like a coyote."
                ab "...Have you seen any particularly big raccoons around?"
                tn "No."
                ab "So, no animals?"
                tn "No."
                "..."
                "...."
                tn "Wait, yeah-sort of. Does it count if I've only heard of one?"

                ab "Sure." 
                tn "I think Tammy, Tammy's my manager, she's not in, 'cause she's having a kid."
                tn "Anyway. Tammy said that the nightshift janitor told {i}her{/i} that he saw something while he was taking out the trash."
                tn "I think it was like...in the grass."
                tn "It was...watching him? Or he thought it was."
                tn "I dunno if he was making it up. He's, like....old. I think he's thirty, or something."
                ab "Mhm. Ancient."
                "Some part of me withers away."
                tn "So, he went inside pretty quick. But he said-or Tammy said, that he said-it was long."
                ab "Long?"
                tn "{i}Yeah.{/i}"
                "She makes a face."
                tn "Hot dog style."
                "That's something, at least. Even if it's through several layers of dispassionate abstraction."
                "It shows up at night and it's 'long'."
                tn "S'that all?"
                jump teengirl

            label weirdmesses:
                $ askedmess = True
                if askedanimal == True:
                    ab "One more thing."
                    ab "Any messes or debris around?"
                ab "Has the garbage been rifled through."
                ab "Or some kind of substances left anywhere?"
                tn "'Substances'-like-"
                "She leans a little closer."
                tn "Drugs? Are you a cop?"
                tn "'Cause you have to tell me if you're a cop."
                show andrea body stern
                ab "No. Not a cop."
                "Do I look like a cop?"
                show andrea body happy
                ab "Again, just doing a school project."
                tn "Oh...okay..."
                "She leans away."
                show andrea body neutral
                ab "I mean just, weird spills. Powder, that stuff."
                
                tn "I think the garbage has been fine."
                tn "But I think Tammy-that's my manager-"
                if askedanimal == True:
                    ab "Yup, you said."
                    tn "Oh, right."
                tn "Tammy said that there was some kind of...oil spill? Dunno, some kind of thing...spilled."
                tn "It stained the pavement near the back exit."
                tn "She was annoyed, 'cause we might need to get it painted."
                ab "You think I could check it out?"
                tn "I mean. I can't stop you from going in the back."
                tn "It's not, like. Blood."
                ab "That's good."
                "Some kind of weird stain. It could be nothing, but Paragons have got weird insides."
                "From what I get, it's not really analagous to proper animals."
                "Things that should reasonably be cold-blooded don't need any sunlight to warm up."
                "Wings that shouldn't be able to carry their body weight."
                "They don't even need the seven essential capacities for life. It's messed up."
                tn "That it?"
                jump teengirl
                
            label afterteen:
                ab "Yup, that's it for me."
                ab "Appreciate the help, I've been really stressed for this assignment."
                show andrea body happy
                ab "It, uh, means a lot."
                tn "Alright."
                "..."
                "...."
                tn "Do you wanna buy something?"
                "Y'know, yeah, I do."
                "I deserve it."
                "Again, good hoagies."
                "I'll give Vera a call to see if she wants something, too."
                show andrea neutral
                "Hopefully she's been pulling her weight enough to earn it."
                "I pull my phone out."
                play sound "audio/SFX/PhoneDial.mp3"
                "{i}Beep, boop, beep, boop, ring-ring.{/i}"
        label switch_vera_pov:
            scene parking lot with Fade(0.5, 0.5, 1.0) #Probably add new music for this section as well
            show vera body shirt3 neutral2 at center
            "I watch Andrea walk off further into the strip mall."
            "I'm glad she agreed to do the personal account portion of investigating."   
            "It's a pain in the ass trying to pry info out of people."
            "They always pry back, or start freaking out, or get pissy."
            "Especially if they aren't in the loop."
            "'Cause they have some kinda sense that you're not telling them the whole truth, but can't pin it."
            "Defenses go up. And now you're playing deescalator." #add hiphen between 'de' and 'escaltor'
            "Not that my part in this is gonna be a cakewalk, either. The fucking wacko didn't give us much to work with in terms of where the Paragon could be buckling down." # use of 'fucking' feels unnecessary here
            "Would it have been so hard for him to get his ass down here to give it a once-maybe even a twice over?"
            "Whatever. I doubt this one's gonna be too rough to handle."
            "And it's kinda nice to be back in action-properly." 
            "We've been stuck in stasis over the last few weeks."
            "Bar-guy didn't count. There was too much {i}mess{/i} with him, right till the end." #maybe add more of a transistion between thoughts here? I thought she was just talking more abt bar guy after before realizing she went back to discussing the paragon
            "It doesn't feel ballsy enough to stay in its hunting ground too long, so I stick to the outside of the shopping center."
            "This place is beginning to die. It's not super obvious-just a few signs declaring closing sales and one too many empty lots-but when you see it, you can't unsee it."
            "It's a pretty solid choice to find folks that won't be missed. Dunno if our target's smart enough to think of that, though."
            "We didn't get much about the lady that went missing. If they found anything of her's, they didn't mention it in the news articles."
            "Could be that the cops just haven't disclosed all the info."
            "I'm not exactly sure what I'm looking for it's more of a 'I'll know it when I see it' deal."
            "Paragons are pretty finnicky like that."
            "It's hard not to let my mind wander a little."
            menu thinking:
                "Think about Andrea":
                    jump think_andrea
                "Think about bar-guy":
                    jump think_barguy
                "Think about the road ahead.":
                    jump think_roadahead
                "Keep to the here and now.":
                    jump hereandnow

        label think_andrea:
            "I hope the folks here actually give Andrea something to work with."
        "It sucks to pull teeth and then find all of them are...cavities."
        "Filled with cavities. Something like that."
        "I'm sure she's happy I'm out of her hair, at least for a little while."
        "She'd let things go pretty easily this morning, but that doesn't always mean much coming from her."
        "She's real good at biting her tongue."
        "It's probably for the best. We have enough going on without holding grudges."
        "Besides, she can hate me all she wants, as long as she doesn't lose track of why we're here."
        jump thinking

        label think_barguy:
            "{i}Fucking bar-guy.{/i}"
        "He should've gone down easy."
        "I'd considered trying to chat him up, but that would've drawn too many eyes."
        "I wound up hedging my bets on him being the type to get piss-drunk-college-ish age, shitty leather jacket, just a little too eager-and it'd paid off."
        "I followed him for ten blocks and he didn't have a clue."
        "Not a fucking thought in his stupid little head 'till I got him right in the ribs."
        "He could've just left it there, but humans are real bad at just giving up." 
        "Nah, he screamed. Tried to clock me in the face."
        "I had to jam a crossbow bolt in his throat and hope it'd do its {i}thing{/i} enough to cauterize it."
        "I don't wanna think about what would've happened if it didn't."
        "{i}Messy, messy, messy.{i}"
        "I'll keep it in mind for next time."
        "Wouldn't hurt if Andrea did her part in it, too."
        jump thinking

        label think_roadahead:
            "So, we find this one, then what next?"
        "It hinges on Dominic having anything {i}useful{/i} to tell us."
        "Sloane seems sure, but Sloane's never second guessed herself in her life."
        "I don't have my hopes up."
        "Not like he'll have some magic fix for Andrea. At best, we're getting another bread crumb."
        "I'm sure she knows that too."
        "We're not finding anything definitive before Burn comes calling again."
        "That, I'm sure of."
        jump thinking

        label hereandnow:
            "That's enough ruminating."
            "Eye on the prize. It already feels like I'm being absorbed by the choking suburban malaise in the air."
            "The parking lot itself doesn't have signs of anything, so I head to the thin tree line surrounding it."
        "Something about it pisses me off. As if it's reeeeally trying to convince you there's any life to it."
        "It better be worth my while."
        "I take it slow, keeping close to the ground."
        "Maybe there's a conspicuous burrow."
        menu check_treeline:
            "Check the trees.":
                jump check_trees
            "Check the mulch.":
                jump check_mulch
            "Take a closer look at the leaves.":
                jump eat_leaf

        label check_trees:
            "The trees aren't tall enough to provide much cover."
            "And there's no scratch marks or anything in the bark."
            "Not there."
            jump check_treeline

       


        label eat_leaf:
            "I've never willingly tasted a Paragon, but I've been in the game long enough to accidentally get mouthfuls of stuff I probably shouldn't."
            "I'd recognize it."
            play sound "audio/SFX/LeafCrunch.mp3"
            "I grab a handful of leaves and shove them in my mouth."
            "It takes a couple of chews of wet, pulpy mush before I confirm there's nothing off about it."
            "Before I can think better of it, I swallow it."
            "It's not the glossy, spiky kind, so it's probably fine."
            "Moving on."
            jump check_treeline


        label check_mulch:
            "I crouch low and begin rifling through the mulch."
        "It's the sneaky kind so maybe it burrows."
        "Or just stays close to the ground, that's more likely."
        play sound "audio/SFX/Squelch.mp3"
        "{i}Squelch.{/i}"
        "My hand catches on something sticky."
        "I gingerly pull it out and find that there's some sort of weird, chunky substance clinging to it."
        "I inspect it in the sun."
        "It's transluscent, with this purple-ish sheen."
        show vera body shirt3 annoyed at center
        vl "Fuck!"
        "There's a bizarre moment where I think it might've bitten me. But, no, it's {i}burning{/i}."
        "It's like I got lemon juice poured on a cut."
        "I pull my sleeve over my hand and tear it off before it can get any worse." #unclear what Vera is tearing off here. I assume the purple substance but bc her hands and sleeves were mentioned before, it looks like she's tryna reference them
        "Shit, I need somewhere to put it."
        "I awkwardly fumble my free hand along the litter on the ground."
        vl "Gotcha."
        "It finds purchase on what I realize is an empty soda bottle, which I grab onto, then jam whatever evil-goo-thing this is into it."
        "It takes some manuevering with sleeves over both my hands, but I manage to before it can do any more damage."
        "At least to my skin. The tips of my sleeves have little holes burnt into them."
        "Ugh. Later Vera problem."
        "I examine the little bastard through the plastic."
        "It's more solid than I first gave it credit for."
        "The slime  is more of an exterior (exoskeleton? Not really, 'cause it's not hard) coat."
        "It surrounds a center of meat, that looks a little like freezer burnt steak."
        show vera body shirt3 neutral at center
        "{i}Nice{/i}. I've actually got something good here."
        "There isn't anyway to close the bottle, so I just scrunch in the top so it creates some sort of seal."
        "{i}Ring, ring.{/i}"
        "A buzzing from my pocket interrupts my thoughts."
        "Right on time. I answer it."
        vl "Hey Andy."
        ab "Hey, what's up? How's searching going?"
        "She speaks quietly, just above a whisper."
        "Might be trying to keep folks from overhearing."
        show vera body shirt3 neutral at center      
        vl "Pretty awesome, actually."
        ab "Oh?"
        "It's nice to hear the anticipation in her voice."
        vl "Yeah, think I found a piece of it. Donovan is probably gonna shit himself."
        ab "Ew-...do you mean Dominic?"
        vl "Yeah, him too."
        ab "Still gross, dude. Anyway."
        ab "The cashier at the UaUa's mentioned some weird stuff that's been happening nearby."
        ab "Feels Paragon related. You might have a better idea than me, though."
        vl "We should meet back up, where are you now?"
        "I sometimes forget she's technically only been in the game for a year or so. She's taken to this life pretty well."
    
        ab "The UaUa's, I'm gonna circle around back-apparently, there's some kind of weird stain."
        vl "Ooo, scary. Hey-can you get me a hoagie?"
        "Guess crawling around the parking lot worked up an appetite."
        ab "Mmm. Maybe."
        ab "If you ask nicely."
        show vera body shirt3 angry at center
        vl "Really? What if I'm {i}starving{/i}?"
        vl "And I never get my food because you're being too pedantic?"
        ab "Do you even know what pedantic means?"
        vl "Now you're insulting me? Insulting the intelligence of a dying woman?"
        vl "This is terrible. {i}You're{/i} terrible."
        ab "So, no please?"
        vl "..."
        vl "..."
        vl "Can you please get me a hoagie?"
        show vera body shirt3 annoyed at center
        ab "I'll think about it. See ya."
        "She hangs up before I can get a response in."
        "{i}Ugh{/i}. Better head over to see if her better nature has won over."
        label reuniteandy: #add music here
            scene parking lot with fade
            show andrea body neutral at right
            "It takes a few minutes for Vera to get around the back."
            "I await her with hoagies in hand. I'll let her off easy this time."
            show vera body shirt3 happy at vera_spot
            vl "Aww, you shouldn't have"
            show vera neutral
            show andrea body happy
        ab "Aww, I {i}shouldn't{/i}."
        show andrea neutral
        "I hand her's over. No lettuce, extra cheese, concerning amount of onions."
        "Mine's the superior one, my main indulgence is olives."
        ab "So, what'd you find?"
        "She pauses midway through unwrapping her food to dig around in her pocket."
        vl "Check it."
        "I oblige."
        "It's some sort of slimy, iridescent substance."
        "Safe bet that it isn't natural."   
        "I wrack my brain for possibilities."   
        ab "Do you think this is part of it? Could've gotten snagged off."
        vl "Mmm-"
        "She puts a finger up, indicating she'll respond after swallowing her mouthful." #little confusing on the posistioning of Vera's hands here. I'm imagining they're just holding their food, but if Vera's holding her food in one hand and holding the bottle in the other, how is extending a single finger? Like is she just raising it off the sandwich or is the action supposed to read clearer than that?
        vl "That's my best guess. I think this part is too dinky to reform all the way."
        vl "Probably just got caught on a tree branch, this thing seems all...gelatinous and shit."
        ab "It matches up with what Dominic said, he thinks its trying to piece itself back together."
        "There's not a lot of universal truths between Paragons. This is an exception."
        "They're really bad at dying. Even if you chop them up, if there's still enough of their bodily functions left, they try and stick themselves back together."
        "What actually counts for 'bodily functions' varies. There's an annoying trial and error to it."
        vl "Maybe one of its victims put up a fight, or maybe it's just real clumsy."
        vl "Aaanyway, my guess is it retreated somewhere near the outskirts of the lot."
        vl "What about you-what am I supposed to be looking at?"
        ab "Here."
        "I gesture down."
        "It's like the cashier had said. There's a set of white splotches along the asphalt. The contrast is stark, like its' been acid washed."
        ab "She also said that the janitor saw something watching him when taking out the trash."
        ab "He assumed it was an animal."
        vl "{i}Nice{/i}, so we have some sort of trail."
        "She makes a vague gesture from where I assume she went, to back here."
        vl "Gooey, acidic"
        "This is less treading new ground and more confirming what we already suspected."
        "It's still reassuring. And having some possible attack pattern is good."
        show vera neutral2
        vl "Any idea why the janitor guy didn't get attacked?"
        ab "No clue. Could be a preference of victim."
        show vera neutral2
        vl "Likes 'em young."
        "She nods sagely."
        "I don't know where she got the idea of the hypothetical janitor being old."
        vl "So...now we kill it, yeah?"
        "Vera leans back against the wall and takes another bite of hoagie."
        "She's never {i}really{/i} still, but I can tell when something has her extra buzzed."
        ab "Once we get a more solid plan."
        show vera annoyed
        vl "I know, that's with the territory."
        vl "There's not a lot {i}to{/i} plan. We either track it down or wait it out."
        "I weigh my options."
        ab "My votes on waiting. I don't think it's a good idea to fight it on it's own turf."
        ab "We can stakeout here."
        "Stakeouts are nice. They're a classic."
        "It's a familiar kind of boring. The building dread that comes with it isn't too bad to stomach."
        show vera neutral2
        vl "We're probably gonna have to stay up for a {i}while{/i}."
        vl "Plenty of time to take in the scenery, right?"
        ab "Get a real whiff of that strip mall air."
        "I can't decide whether these places freak me out or sort of comfort me."
        "No matter where I go, it's the exact same."
        "Just swap out the UaUa's for whatever the local convenience-store-rest-stop is local to the area."
        "On one hand, it's uncanny. On the other, it's reliable."
        show vera neutral
        vl "Least the food is good-hey, are you gonna try your's?"
        ab "Oh shit, yeah."
        "I take a bite of mine. She's right, pretty good. There's a good mix of flavors without them vying for control too much."
        vl "The next place is on me."
        show andrea annoyed
        ab "Sure it is."
        show vera annoyed
        vl "Cross my heart, promise."
        show vera neutral
        show andrea neutral
        "I expect some sort of follow up, but she's too focused on stuffing her face."
        "S'fine with me. I'll take a non-awkward silence."
        "It lasts all the way to the end of our 'meal'-until Vera finishes inhaling the thing and I get full halfway."
        vl "Was getting info annoying?"
        show andrea offput
        ab "Eh. Mostly just {i}weird.{/i}"
        ab "It was this, like, high schooler? Maybe early college kid."
        ab "I dunno."
        show andrea neutral   
        ab "She wasn't being difficult, she just didn't know much. Or care."
        vl "{i}Really?{/i}"
        vl "I thought this thing would be a hit among the youths. Freaky murder right on their back porch?"
        ab "Don't say youths. She made me feel old enough."
        ab "But, I mean, I didn't expect her to be jazzed, just like-scared, at least?"
        show vera neutral
        vl "{i}I'd{/i} be jazzed."
        vl "Something to spice up the student life."
        ab "That's awesome, Vera."
        show vera happy
        vl "It spiced up {i}our's{/i}, didn't it?"
      
        show andrea sad
        ab "Mmm..."
        ab "Dunno if that's the word I'd use."
        "'Student life' is kind of an exaggeration. Halfway into an associates doesn't count for much. Even less for her."
        show vera neutral2
        "She opens her mouth to say something, but pauses before she can make it all the way."
        vl "Fair enough."
        "Is what she settles on instead."
        "There's the quiet again."
        default spied = False
        default roadspoken = False
        menu silence:

            "'I spy with my little eye....'" if spied == False:
                jump ispytwo
            "Push the topic." if roadspoken == False:
                jump reminisce
            "Let it sit.":
                jump letquiet

        label ispytwo:
            $ spied = True
            "I toss my wrapper into the trash and clear my throat."
        "Without looking at her, I ask:"
        show andrea neutral
        ab "...Something, pink."
        "It's hard to find something that's not the same, washed out grey, but my eye catches on a piece of gum stuck to the side of a dumpster."
        show vera annoyed
        vl "Huh?"
        vl "Oh-shit, hm."
        "She's quick on the uptake."    
        show vera neutral2
        vl "Pink?"
        ab "That's what I said."
        "She looks around with an offputting intensity."
        "Like a sight hound."
        vl "The graffiti there?"
        "She gestures at the adjacent wall."
        "There's some kind of long wornout obscenity plastering it, rendered in what could be considered pink."
        ab "Nope."
        show vera annoyed
        vl "{i}Shit.{/i}"
        "She begins doing her rounds around the lot."
        "I don't feel that bad-she'd pick something just as banal."
        vl "Oh! Ladybug."
        "It takes me a second to realize what she's pointing at."
        show andrea annoyed
        ab "{i}...The weevil?{/i}"
        ab "It's not a-...it's not even red."
        "I don't know how you could make that mixup even if you don't know the name of the species."
        "They're completely different."
        vl "It's close enough, red-pink, ladybug-weevil."
        show andrea angry
        ab "Not really, it's like...like saying raccoons and walruses are the same because they're both carnivores."
        show andrea annoyed
        "Insects aren't really organized the same way as mammals are, so it's not a one to one, but she's not ready to have that conversation."
        ab "And, again, it's not even pink."
        vl "{i}Okay!{/i} Sorry."
        show vera sad
        vl "It's not the...weevil."
        show andrea neutral
        ab "Any other guesses?"
        show vera neutral2
        vl "Mmm...."
        ab "You can always give up."
        show vera annoyed
        vl "Bullshit, I got it."
        "There's a pregnant pause."
        "She walks a languid circuit around the lot."
        "I almost cut her off there."
        show vera neutral
        vl "Okay. This one's it."
    label random_guess:
        default randnum = 0
        $ randnum = renpy.random.randint(1,2)

    if randnum == 1:
        jump guess_right

    if randnum == 2:
        jump guess_wrong

    
    label guess_right:
        vl "{i}That.{/i}"
    "She points an accusatory finger at the wad of gum."
    show andrea happy
    ab "Well, shit."
    ab "You got it."
    vl "Hey, don't sound so surprised."
    ab "I'm not, promise."
    vl "That was a tricky one."
    vl "I'll give you a reaaaal nasty one next time I go."
    jump silence

    label guess_wrong:
        vl "I got it, you're pulling a fast one on me."
        "She points her thumb towards herself with enough force that I worry she'll poke out her good eye."
        show vera happy
        vl "My scar, yeah?"
        "I can keep a straight face for all of five seconds, before a laugh escapes me."
        show andrea happy
        ab "No-{i}stupid{i}."
        ab "It's gum, come on. Don't be conceited."
        show vera angry
        vl "It's a fair guess! You're always staring at me so, like-"
        "She throws her hands in the air."
        ab "I don't, that's weird."
        show neutral2
        vl "{i}Yeah, okay.{/i}"
        show vera neutral
        "Now it's {i}her{/i} who stares at me for a good, few moments."
        ab "...What?"
        show andrea stern 
        vl "What yourself."
        jump silence
    label reminisce:
        show andrea neutral
        $ roadspoken = True
        ab "You think you'd wanna go back to school?"
        ab "After things quiet down, maybe. In theory."
        show vera neutral2
        vl "Ehh..."
        vl "Probably not."
        vl "It kinda feels like playing pretend at real life."
        vl "What's...History of Psychology 101 gonna do for me."
        "She pauses."
        vl "What about you?"
        vl "You were more into it."
        ab "For the one we were in, yeah."
        "What class was it again? Something...science. Biology, right."
        ab "I think I'd like it more once I got to pick more of them out."
        vl "Which ones?"
        show vera happy
        vl "{i}Like a film class?{/i}"
        show andrea offput 
        ab "Ew, no."
        ab "Probably..."
        label bio:
            show andrea neutral
            ab "Biology, maybe a higher level."
            vl "That makes sense. I think."
            vl "What do you even {i}do{/i} in bio though?"
            vl "I keep hearing it's hard."
            ab "Vera, we took the same class on it."
            show vera neutral2
            vl "Ohh...yeah, huh."
            vl "Proves my point."
            ab "Not medical, probably, something more outdoorsy."
            "I think I've had enough of being cooped up in the last few weeks to last a lifetime."
            vl "Make that a goalpost, then. Once we get all this done and over with, you can go turn over logs and scrounge around." #mmm...not an important thought but it may be fun to let these girls go to a swamp later they deserve it
            ab "Good call."
            jump silence
       

        label letquiet:
            "I leave it at that."
            "No one gets on us for loitering and the wait feels calming, rather than tense."
            "Or it does, up until something hits me."
            show andrea stern
            ab "{i}Shit.{/i}"
            vl "Huh?"
            show vera annoyed
            ab "The cashier girl, we have to make sure she's not there when the thing comes over."
            vl "{i}Shit.{/i}"
            vl "Alright, well. That'll be a pain."
            vl "Maybe we can scare her off."
            show vera neutral2
            vl "She hasn't seen me. Maybe if I act all crazy, she'll ditch."
            ab "She seemed pretty unphased by all of this, I don't think it'll work."
            ab "Besides, if she starts telling her two strangers were threatening her right before there's some kind of incident, it'll make things difficult."
            vl "Fair, fair."
            vl "And we can't just let her get got."
            "She looks to me, as if hoping I'll disagree."
            ab "Yeah."
            vl "Maybe we can say we're actually undercover cops."
            vl "It's a double lie, after the whole 'college student report' thing."
            ab "You'd probably have more luck with that."
            "I'm hesitant to let her take the wheel, but she hasn't been seen yet. And the girl doesn't seem eager to stick around." #I'm assuming 'the girl' is meant to refer to the teen here but since its a vague desc it feels like its referring to vera a bit
            show vera neutral
            vl "Sure. Just leave it to me."
            show andrea neutral
            ab "By all means, then."
            "I gesture towards the front entrance of the UuaUua's and she obliges."
            scene uuauua with fade
            play sound "audio/SFX/UuaUuaBell.mp3" #add music later
            "It's still empty, aside from the cashier. Lucky us."
            show vera bodyflip shirt3flip neutralflipped:
                xalign 0.5
                yalign 1.0
            show andrea body neutral:
                xalign 1.3
                yalign 1.0
            vl "{i}That's her?{/i}"
            "Vera mouths."
            "I nod."
            vl "Hey!"
            show vera bodyflip shirt3flip happyflipped with MoveTransition(0.3):
                xoffset -200
            "She waves and makes her way over to the register."
            tn "Hi."
            vl "You work here, right?"
            tn "Yeah."
            "She stares blankly for a few moments, then taps her uniform."
            vl "{i}Cool, okay.{/i}"
            show vera neutral2flipped
            vl "Sorry, I'm gonna have to ask you to leave."
            tn "Why?"
            vl "There's a whole situation. You know, with the murders and everything?"
            vl "We're actually investigating it."
            vl "So we need civillians to leave."
            tn "Are you doing that research thing with her?"    
            "She points at me."
            vl "Oh, that part was a lie. We're with the department."
            "Which department is anyone's guess."
            tn "Huh?"
            tn "But you said you weren't a cop."
            tn "You can't lie about that."
            show andrea stern
            ab "You {i}can{/i} actually. Sorry, uh, about that."
            "The silver lining here is that this will be a learning experience for her."
            tn "{i}What?{/i}"
            "It's the most emotion I've seen her show in the few moments that I've known her."
            show vera sadflipped
            vl "Yeahh, sorry. You're gonna have to head out. You can come back tomorrow."
            vl "And let anyone coming in later know that too."
            vl "It's your day off. Have fun."
            show vera happyflipped
            vl "Congrats."
            "This is all hinging on her not asking for any sort of verification."
            "{i}Please don't ask for verification, please don't ask for verification.{/i}"
            tn "Thanks. Okay. Gotcha."
            "Her movements are robotic as she steps out from behind the counter."
            tn "So, like-...are you gonna put up tape, and stuff?"
            show vera neutral2flipped
            vl "Yup. We just have it in the-..."
            show andrea neutral
            ab "Police car."
            vl "Mhm."
            tn "...Okay."
            play sound "audio/SFX/UuaUuaBell.mp3" volume 0.1
            "And, with a jingle of the door, she's gone."
            "She even does the courtesy of flipping the sign from 'open' to 'closed'."
            "Based on the clud of dust it kicks up, it hasn't been used for a while."
            "I wait for her figure to disappear from view."
            ab "That's gonna be a problem later."
            show vera body shirt3 neutral2
            vl "Oh, yeah, absolutely."
            vl "I kept a pretty good cover though, right?"
            "She holds out her hand for a high five."
            ab "Mmm..."
            show andrea happy
            show vera annoyed
            vl "Come on, don't leave me hanging."
            ab "Alright. You didn't botch anything."
            "I slap her hand."
            show andrea neutral

            ab "Do you think it'll come through the back or the front?"
            show vera neutral
            vl "We should split up, it'll cover our bases."
            show andrea stern   
            ab "Dunno how much I like that idea."
            ab "We still don't have an idea of how much of a threat it is, exactly."
         
            vl "We sort of do, we know it's not a big deal."    
            vl "And the back and front are, like, thirty seconds apart if you book it."
            ab "If it's as sneaky as we think it is, it could pick us off without the other noticing."
            show vera neutral2
            vl "{i}Or{/i} it could give us a better range of where it could be."
            vl "We can keep that guy open, so we're in eyeshot."  
            "She points over her shoulder to the door to the backroom."
            show andrea stern
            ab "Makes sense."
            ab "I guess."
            vl "You don't sound super sure."
            "I'm not. It's not just this Paragon I'm worried about."
            show andrea sad
            ab "It's just the first time with-since..."
            "Since everything with Burn."
            "I haven't been on a hunt with it in the backseat."
            "It'd promised to only bother me when 'needed'."
            "I don't believe it."
            "Based on Vera's expression, I can tell she knows what I'm getting at."
            show andrea stern
            ab "It's fine, nevermind. It's not that big a deal."
            "-Not that it'd matter to her. She's already fed up with my reservations."
            vl "Okay, got it."
            "She's eager as ever to avoid the topic."
            vl "Wanna take the back, or the front?"
            define moveinoutfade = ComposeTransition(dissolve, before=moveoutleft, after=moveinright)  
            menu: 
                "Back":
                    jump back_room
                "Front":
                    jump front_room



        

        label back_room:
            
            ab "I can take the back."
            "Maybe the quiet will be nice."
        
            vl "M'kay!"
            show vera bodyflip shirt3flip neutralflipped
            vl "I'll scream if it gets me."
            vl "Or if the cops come."
            show andrea neutral
            ab "You do that."
            
            "With a wave, she's off."
            hide vera
            with moveinoutfade
            "I head to the back."
            scene combat bg grayscale flour with fade
            
            show andrea body neutral at center with dissolve
           
            "It's a little offputting."
            "Rows and rows of frozen hot dogs and gas station snacks and unlabeled boxes."
            "The offensive scent of whatever they use to wipe this place down."
            "The best I can do for this place is try to keep collateral to a minimum."
            "It's the price for taking it on our terms."
            "I prop open the door to the outside and slide down to the ground."
            "Now we wait."
            "The sky washes out into light blue, then glows into yellow, then dies back down into grey."
            "The dumpsters box the tangle of trees in on either side."
            "Based on what I know about it, I'm not going to be seeing it."
            "I do my best to listen in."
            "It's just the last sounds of bird call, almost drowned out by the sound of the road."
            "Maybe I should do something to get it's attention."
            menu:
                "Throw a food container.":
                    jump food_container
                "Yell.":
                    jump yell

            label food_container:
                "Paragons don't usually care for human food."
                "But, noise is noise."
                "I grab for the closest thing around me, which is a container of fries."
                "I throw it, full force, into the dark."
                "I wait with baited breath for any kind of reaction."
                jump after_outside
            label yell:
                "I cup my hands to my mouth and yell:"
                python:
                    yell = renpy.input("What do I yell?", length=32)
                "[yell]!"
                "The night air swallows my voice eagerly."
                "I lean forward to hear if anything caught it."
                "..."
                "Nothing."
                "Maybe nothing."
                jump after_outside
                
            label after_outside:
                "Nothing turns into a maybe."
                # insert a noise
                show andrea body scared
                "Turns into a definitely."
                "It's a different noise everytime."
                "Screeches that dig nails into my mind. Segmented chitin bumping against itself."
                "This one's new."
                play sound "audio/SFX/ParagonMove.mp3"
                "There's the suggestion of movement, but no source."
                #insert skittering.
                "{i}Alright, okay.{/i}"
                "I have to get it in here."
                "It has to see me at this point, right?"
                "No way it'd resist a good meal. A pulsing little morsel of soul, standing stock still right in front of it."
                "It's gone silent. Surveying, maybe?"
                "Or it's fled, and I fucked up my chance."
                # skitter
                "An explosion of movement in front of me."
                
                ab "Shit!"
                show andrea body scared 
                define quick_time = True
                if quick_time == True:
                    $ timer_range = 3
                    $ timer_jump = 'fend_it_off_bad'
                    $ time = 3
                    show screen countdown
                    menu:
                        "Block with the hammer.":
                            jump fend_it_off
                else:
                    jump fend_it_off
            label fend_it_off:
                hide screen countdown
                "The rush of air is coming from above."
                play sound "audio/SFX/HammerPressure.mp3"
                "I grab onto the handle of my hammer with both arms and force it up."
                "A crushing weight bears down on it."
                "My arms scream, knees threatening to buckle."
                show andrea angry
                ab "{i}Vera!{/i}"
                "Between my yell and the sound of its myriad footsteps, there's no way she doesn't hear."
                "She's got the keener ear between the pair of us."
                "My attention's torn away from her as there's another shove from above."
                if quick_time == True:
                    $ timer_range = 3
                    $ timer_jump = 'push_down_bad'
                    $ time = 3
                    show screen countdown
                    menu:
                        "Move out of the way":
                            jump dodge_out
            label dodge_out:
                hide screen countdown
                "I stumble away before it succeeds in pressing me all the way down."
                show andrea offput
                play sound "audio/SFX/Thud.wav"
                "It catches itself on the ground with a dull {i}thud{/i}."
                "A cloud of dust renders its silouhette briefly."
                "Some multi-legged, serpentine thing, dragging something on the ground behind it."
                "{i}Where is she?{/i}"
                "Another woosh of air towards me."
                "This time, from the ground."
                "I'm not fast enough, shit."
         
                     
            label run:
                play sound "audio/SFX/ArrowHit.mp3"
                "Metal hit metal above me."
                "A spark of brilliant blue illuminates the backroom, just for a second."
                vl "I'm coming, I'm coming!"
                show vera bodyflip shirt3flip annoyedflip at right
                "Vera takes position a few steps behind me."
                vl "Where is it?"
                show andrea angry
                ab "{i}Invisible.{/i}"
                show vera angryflipped
                vl "Damn it. Right!"
                ab "Let's do something about it."
                jump combat
                
            label fend_it_off_bad:
                "Bleh."
            label push_down_bad:
                "Bleh." #there is so specified jump from Andrea getting injured to her getting to vera. I would think maybe this is supposed to jump to after_inside, but the actions don't totally line up and there's not another line it makes sense to jump to? Also both 'push down bad' and 'fend it off bad' lines play even if Andrea's only failed one action which feels unintentional

            label front_room:
                
                ab "I can take the front."
                "It'll be good to keep an eye out on if anyone parks."
                vl "M'kay!"
                vl "I'll scream if it gets me."
                vl "Or if the cops come."
                show andrea neutral
                ab "You do that."
                show vera neutralflipped
                "With a wave, she's off."
                hide vera
                with moveinoutfade
                "I prop open the door with a shopping basket and stand in the doorway."
                "The dry heat has faded into a welcome reprieve from the store's stale air."
                "The Arizona summer isn't in full swing yet. There's still the last remnants of spring holding on desperately."
                "It does a little to calm my nerves. Not enough to kill the urge to reach for a cigarette."
                "My fingers make it all the way to my pocket before I decide against it."
                "I can wait for {i}after{/i} the fight."
                "Instead, I focus all my attention on the quiet."
                "There's just the sound of the distant road and the occasional bird call."
                "Nothing out of the ordinary."
                "Especially since I don't even know what I'll be listening out for."
                "We know it's...wet. Gooey. In that general direction."
                "And that it has some amount of legs."
                "Maybe I should do something to get it's attention. If it's out there somewhere."
                
            menu:
                "Throw a food container.":
                    jump food_container2
                "Yell.":
                    jump yell2

            label food_container2:
                "Paragons don't usually care for human food."
                "But, noise is noise."
                "I grab for the closest thing around me, which is a container of fries."
                "I throw it, full force, into the dark."
                "I wait with baited breath for any kind of reaction."
                jump after_inside
            label yell2:
                "I cup my hands to my mouth and yell:"
                python:
                    yell = renpy.input("What do I yell?", length=32)
                "[yell]!"
                "The night air swallows my voice eagerly."
                "I lean forward to hear if anything caught it."
                "..."
                
                jump after_inside

            label after_inside:
                "Nothing."
                "Maybe we misjudged it's hunting grounds, or it doesn't care."
                vl "{i}Here{/i}!"
                "I stand corrected."
                show andrea body offput 
                ab "Coming!"
                "I turn on my heel and bound towards the back."
                scene combat bg grayscale
                show andrea body offput at right
                "Rows and rows of food storage stand silent sentinel around me."
                "Whatever eerie peace the sight implies is shattered by the clatter of boxes and the sound of {i}something{/i}."
                show vera bodyflip shirt3flip annoyedflip at left
                vl "It's-{i}shit{/i}-"
                "My eyes adjust in time to see Vera backed up against the wall, her crossbow drawn."
                "There's no sign of the thing. Just the nails-on-chalk board of something dragging against linoleum."
                "And something hitting the ground."
                vl "Got some-camoflage."
                "From a glance, it doesn't look like she's injured."
                "A bit of tension fades from my shoulders."
                show andrea stern
                ab "Let's do something about it then."
                
                jump combat
            



    
    label combat:
        stop sound
        play music "audio/Music/BattleThemeCoalesence.mp3" loop
        $ head_floured = False
        $ tail_floured_floured = False
        $ torso_floured = False
        $ tail_floured_floured = False
        $ tailhmred = False
        scene combat bg grayscale flour with fade
    #   default health = 3
    #  default monster = 3
        
    # if health == 0:
        #    "You lose."
        
        #if monster == 0:

        #   "You win."
        $ default_combat_round = 1
        $ enabled = False
        
        show screen attack_examine 
        
        "Alright, time to go."
        "..."
        "Woah! Looks like there's a lot going on here."
        "Maybe we should take it easy, yeah?"
        "This thing's invisible, so, we need to find a way to mitigate that before we can get any sort of shot in."
        "Hm, what could be around here?"
        "Click the EXAMINE button, to look around the scene."
        $ examine_button_enabled  = True
        call screen attack_examine
        
            
    label examine_first:
        show screen combat_flour_examine
        $ enabled = False
        "Hm, what could be around here?"
        $ enabled = True
        call screen combat_flour_examine

        
       
       
    label label_flour:
        
        $ enabled = False
        $ attackChance = renpy.random.randint(1,2)
        $ full_examined = True
        scene combat bg grayscale
        "I'll give you this one for free, maybe it'll be useful."
        
        "Now lets use it."
        $ flour_found = True
        "-Err, wait!"
        "The creature rears up and-"
        show screen combat
        "Whips forward, the edges of its scaled tail scraping against your face."
        "As a heads up, this can happen on occasion."
        "You can see the indication riiiight at the bottom."
        #show screen combat
        $ andrea_vera = "combat/av bad.png"
        window hide 
        pause
        "And if it's really bad, it gets like this."
        $ andrea_vera = "combat/av terrible.png"
        window hide 
        pause
    ## show screen combat
        window show
        "I'll give you this free one, though."
        $ andrea_vera = "combat/av good.png"
        window hide 
        pause
        "For now, the chance is fifty-fifty and happens after everytime you do something."
        "So, use your turns conservatively!"
        "Anyway-"
        
        $ attack_button_enabled = True
        $ examine_button_enabled  = False
        hide screen combat
        "Now's your chance to strike."
        "Click ATTACK."
        call screen attack_examine
        


        
     
#   label incorrect:
#      "Not quite."
#     $ green_btn_selected = False
    #    $ health -= 1
        
        ##$ combat_round += 1
    #   jump combat

    label correct:
        show screen combat
        $ flour_found = False
        $ paragon_enabled = False
    ## scene combat comp flour
        $ flour = False
        $ arwselected = False
        $ flour = False
        $ hmrselected = False
        $ something_selected = False
        $ andrea_vera_health = "good"
        "There we go."
        "Now, it'll take its turn for realsies."
        
        jump combat_roll
        
    #  $ time = 5
    # $ timer_range = 5

        #$ timer_jump = 'round2'
        hide screen combat
        call screen combat2
    # show screen countdown
        

    label wrong1:
    #  scene combat comp invis
        $ something_selected = False
        $ arwselected = False
        $ flour = False
        $ hmrselected = False
        "Oo, not really."
        "Let's try again."
        "As a heads up, next mess up miiight get you busted."
        call screen combat
    label wrong2:
        if arwselected:
            play sound "audio/SFX/HitMiss.mp3"
            vl "Ugh, can't get a shot in through the skin."
            vl "Can you get an opening?"
            jump combat_var
        if torso_hit:
            play sound "audio/SFX/HitMiss.mp3"
            "I swing forward. It's body less moves, more undulates out of the way."
            "It's gotten wise to my hammer."
            $ torso_hit = False
        if head_hit:
            play sound "audio/SFX/HitMiss.mp3"

            "I swing upward. It yanks its head away, leaving me stumbling."
            "It's gotten wise to my hammer."
            $ head_hit = False
        # scene combat comp injured
        # $ andrea_vera = "av bad"
        #if arwselected:
        #  vl "Can't get a shot in-"
        #  vl "It's skins too tough."
        #if torso_hit and hmrselected:
        #   "I aim for its body: a large, winding thing."
        #   "It coils away."
        #   "The blow to its tail's taught it some caution when it comes to my hammer."
            
        
        label combat_var:
            $ something_selected = False
            $ arwselected = False
            $ flour = False
            $ hmrselected = False
            "{i}That's not it.{/i}"
            jump combat_roll
            
            call screen combat2
     

    label hit_tail:
        show screen combat2
        $ something_selected = False
        $ arwselected = False
        $ flour = False
        $ hmrselected = False
        $ enabled = False
        $ paragon_enabled = False
        #show andrea body stern at right
        "{i}Occam's Razor, right?{/i} It's tail sags onto the ground."
        "It's scaly flesh is practically begging to be caved it."
        "I rush forward, bringing my hammer over my head, and {i}slamming{/i} it down."
        "It takes to the metal eagerly, the congealed contents gushing onto the ground in great, dripping clumps."
        jump combat_roll

    label round_3:
        $ paragon_enabled = True    
        $ enabled = True
        call screen combat2
  
    label combats:
    
        if default_combat_round == 1:
            jump round_1
        elif default_combat_round == 2:
            jump round_2
        elif default_combat_round == 3:
            jump round_3
        elif default_combat_round == 4:
            $ paragon_enabled = True
            $ enabled = True
            call screen combat2

    label round_1:
        show screen combat
        "Click on the flour object you want to use, then part of the monster."
        $ flour_active = True
        $ flour_found = True
        $ paragon_enabled = True
        call screen combat

    label combat_roll:
        init python:    
            import random
        $ attackChance = random.randint(1,2)
        $ print ({attackChance})
        if attackChance == 1:
            jump attacked
        elif attackChance == 2:
            jump not_attacked

    label attacked:
        play sound "audio/SFX/HitDamage.mp3"
       
        "The thing rears up, raking its claws across your chest."
        
      
        $ default_combat_round +=1
        if andrea_vera_health == "good":
            $ andrea_vera = "combat/av bad.png"
            $ andrea_vera_health = "bad"
            hide screen combat
            hide screen combat2
           
            call screen attack_examine
            #jump combats
        elif andrea_vera_health == "bad":
            $ andrea_vera_health = "terrible"
            $ andrea_vera = "combat/av terrible.png"
            hide screen combat
            hide screen combat2
            call screen attack_examine
            #jump combats
        elif andrea_vera_health == "terrible":
            jump game_over
    label not_attacked:
        play sound "audio/SFX/HitMiss.mp3"
        "The thing misses, best to get it over with, still."
        hide screen combat2
        hide screen combat
        if tutorial_done == False:
            $ default_combat_round +=1
            call screen attack_examine
            #jump combats
        else: 
            call screen attack_examine
            #sjump post_tutorial_combat
    label round_2:
        
        show screen combat2
        $ paragon_enabled = False
        $ enabled = False
        $ flour_found = False
        $ examine_button_enabled = True
        "Rough one, right?"
        "You should probably try going for it, just my hint."
        "Look for some part of it that's big and hammerable."
        $ tutorial_done = True
       
        hide screen combat2
        hide screen combat
        #$ default_combat_round +=1
        call screen attack_examine 
    label post_tutorial_combat:
        $ paragon_enabled = True
        $ enabled = True
        $ flour_found = False
        $ examine_button_enabled = True
        call screen combat2
    label finishedcombat:
        "Vera's bolt hits true."
        stop music
        play sound "audio/SFX/ArrowHitFlesh.mp3" #i jsut cut out the combat music here but it could also be replaced, idk what ur feeling tho
        "Electricity crackles through the creatures body."
        "From its pooling blood up into what passes through its' veins"
        "Its lumbering form becomes a thrashing, screeching circuit board."

        "It {i}reeks{/i}. A biting mix of ozone and freezer burn."
        "And I wish it was just disgust that flared to life in time with my pounding heart."
        "I wish I didn't feel Burn's satisfaction lapping at the edge of my brain."
        "Pride and vindication. A sadistic sort of contentment."
        "In the moments before I shove it back in place, the offer to join it in revery is more tempting than I'd like to admit."
        vl "That wasn't so bad."
        show vera body shirt3 annoyed at vera_spot
        "Vera yanks me back to reality."
        show andrea body sad at right
        ab "Yeah."
        "My hammer is a lot less messy than before."
        "People aren't as slippery."
        ab "You think it's dead enough?"
        vl "Mmm..."
        "She's soaked in sweat and her breathing is heavy."
        "She crouches down beside it. If the smell bothers her, she doesn't let it show."
        vl "It doesn't look like it's puzzling back together."
        ab "Let's give it a bit."
        "Sometimes Paragons are real good at playing dead. One of the first ones we dealt with took three hours before it started to reform."
        show vera neutral
        vl "Gives us time to clean up."
        show vera annoyed
        vl "And figure out how to cram this in the van."
        vl "There's enough kitchen supplies here that we can probably figure something out. And you can probably pound it pretty well."
        "She gestures to my hammer."
        "In retrospect, we should've come up with a disposal plan beforehand."
        show andrea annoyed
        ab "It's gonna smell terrible in there for weeks."
        vl "We can just air it out."
        ab "What about the acid?"
        "It's already beginning to bleach the floor."
        vl "Mmm...quadruple bag it?"
        "..."
        "..."
        "..."
        vl "Do you have a better idea?"
        show andrea stern
        ab "...Alright, let's start cutting."
        "It's not too different from deboning a chicken."
        "Just a lot larger and pungent."
        "We have to triple layer the plastic gloves we find behind the counter and swap them out every five minutes."
        "By the end of it, we've decimated their pantry. There's barely any knives left that haven't been at least half disolved."
        "We manage to get it into small enough pieces that a few garbage bags do the job."
        "It's almost as exhausting as fighting the damn thing. By the end of it, my arms are jelly."
        show vera annoyed
        vl "{i}Finally.{/i}"
        "Vera pulls off her gloves and tosses them into the bag with its' head."
        ab "Wonder what time it is."
        vl "Too late. Do you mind bringing the van around the side?"
        "Right. we have to drive all the way back to Dominic's place."
        "Under other circumstances I'd feel bad, but he was the one that put us on the job."
        "All things considered we made good time."
        show andrea annoyed
        scene parking lot with fade
        "We barely cram all the bags in the back."
        "They reek even with the AC cranked all the way up."
        scene car bg aznight with fade
        label back_to_dom:
            "I don't bother with the radio this time, fiddling around for a station is going to be annoying."
            "I zone out without its assistance, so the drive goes by quickly."
            "The only interruption is Vera's occasional check in to inform me that the body hasn't eaten through the trash bags."
            "Twenty minutes feels more like five."
            "I park close to the house, it'll make it easier to carry everyting in."
            play sound "audio/SFX/DoorKnockNormal.mp3"
            
            show vera bodyflip annoyedflip shirt3flip at vera_car
            vl "I hope at least one of them's around."
            vl "Otherwise I'm just dumping everything in the backyard."
            show andrea body neutral at andrea_car
            ab "So you think Avery is staying here?"
            vl "Could be. Maybe they're a bit of a stray."
            "Our question is answered pretty quickly."
            play sound "DoorOpen.mp3"
            show avery body neutral at center
            al "Oh! That was...-early?"
            "They look around."
            show avery body thinking
            al "...Late?"
            vl "It's only, like, nine."
            show vera neutral2flipped
            vl "Can you help us get all of it in?"
            vl "It was a big one."
            ab "Do you have a place to store it?"
            show avery body neutral
            al "The garage should be fine."
            "They step out of the house and I gesture towards the car."
            al "It wasn't too bad, was it?"
            show avery body embarrassed
            al "Not that I'm doubting your capabilities - it doesn't look like you two are too beat up. I just wanted to make sure."
            show andrea happy   
            "I flash a thumbs up over my shoulder."
            ab "It was all good. The worst part was clean up."
            show andrea neutral
            show vera neutralflipped
            vl "It's kind of acidic. I hope you have something for that."
            show avery body worried
            al "Ah-"
            show andrea happy   
            ab "It's not that bad, don't worry. A couple of trash bags did the trick."
            show avery body thinking
            al "We shoooould have gear for that? I know Dominic has worked with some real nasty ones."
            "I open the back and fight off a cringe. Even when dispersed by the night air, it's rancid."
            "Avery's a little less succesful. There's a brief, but harrowing, moment where I'm worried they'll throw up."
            "They steel themself, though."
            show avery body embarrassed
            al "Yeah, {i}whew{/i}, it {i}is{/i} big."
            show vera neutral2flipped
            vl "Is Dom-...your boss up?"
            "They nod."
            show avery body neutral
            al "I think he's finishing something up. You came right in the nick of time."
            vl "Uh-huh."
            vl "Do you...do you live here?"
            vl "Dunno if it's my business. I'm just curious about the arrangement."
            al "Nah, I just stay over sometimes. When he needs an extra hand and stuff."
            "They set down their bag and awkwardly shuffle past it to the door."
            scene livingroomdom with fade
            play music "Music/Ambience/upbeatambient.mp3" #if this is not the vibe please let me know. When I added this in, I hadn't cut out the combat music from earlier yet so it was just playing on loop for like an hour straight and I had to listen to something else
            "We're greeted with the same mess from before, for the most part."
            "I think a few shirts may be folded, rather than thrown onto the ground."
            show vera body neutral2 at left 
            vl "What kind of stuff does he even have you do?"
            vl "I haven't heard of any mentees being lab assistants."
            show avery body happy:
                xalign 1.3
                yalign 1.0
            al "Sometimes it's stuff like this- y'know, just being an extra hand. But mostly it's taking notes and reviewing his work."
            al "It's pretty interesting."
            al "Lets me put that 'general sciences' degree to good use and I'm not much of a fighter anyway."
            vl "{i}Mmm...{/i}"
            vl "You should probably pick up at least a little bit of combat stuff."
            vl "Has Dominic never even tried to show you the ropes?"
            show avery neutral
            al "We've talked about it, but it's better for me to build a baseline in understanding how Paragons work, first."
            "There's a stiffness in their tone, right at the end. Like they're parroting someone."
            show andrea body neutral:
                xalign 0.2
                yalign 1.0 
                xzoom -1.0
            ab "Makes sense. I get that."
            "It's better to cut off Vera before she starts grilling them."
            show vera body neutral
            vl "Maybe you can them him how to swing around a hammer."
            "She nudges me. There's a {i}squelch{/i} as the bag over her shoulder shifts."
            show avery body embarrassed
            al "Oh."
            al "Thanks!"
            show avery body thinking
            al "Maybe later."
            show andrea offput
            ab "Mhm, yeah. Where should we put those guys down?"
            show avery body neutral2
            al "Heeeere works."
            play sound "audio/SFX/WetTrashBag.mp3"
            "They plop their trash bag in the hall."
            al "Let me get Dominic, then we can haul the rest in."
            
            "They skamper off towards the lab."
            play sound "SFX/FootSteps2.mp3"
            hide avery with dissolve
            
            "Vera snorts under her breath when they're out of sight."
            show vera happy
            vl "What a character."
            show andrea neutral
            ab "C'mon, they just seem new."
            show vera neutral2
            vl "I'm not saying it's bad. Kind of endearing, honestly."

            ab "{i}Alright.{/i}"
            dm "You can bring it here!"
            "His voice cuts off my train of thought before it can get too turbulent."
            show vera annoyed
            vl "{i}Can't even bother helping?{/i}"
            "We haul our quarry over to where they've cleared a space."
        label back_to_lab:
            scene livingroomdom with fade
            show andrea body neutral:
                xalign 0
                xzoom -1.0
                yalign 1.0
            show vera body shirt3 neutral2:
                xalign 2
                yalign 1.0
            show dominic body happy:
                    xpos 0.45
                    yalign 1.0
            dm "You were right- quite large, this one is."
            "Avery offers a thumbs up from their spot in the corner."
            show vera neutral 
            vl "Careful, it's-"
            dm "Acidic! Yes. I can smell it."
            show vera neutral2
            vl "{i}Let me finish, god damn.{/i}"
            show andrea stern
            "I give her a warning glance."
            "She rolls her eye."
            ab "It's not too bad, the bags handled it fine."
            "He's already busied himself with retrieving his gloves."
            vl "Do you need us here for this?"
            vl "You owe us that info."
            show dominic body thinking
            dm "Oh? Yes! Correct."
            "Dominic doesn't pause, just begins scrounging through the first bag."
            "He produces a smaller chunk - I think it's part of the tail - and plops it on the table."
            dm "Again, you weren't all that specific, but I picked out what I could."
            dm "Paragons being on better terms with humans isn't as uncommon as you'd think."
            dm "I heard about one that took a liking to interior design, did you know that?"
            vl "No."
            ab "That's interesting, not really...what we're looking for, though."
            "He grabs a scalpel from his drawer and begins cutting."
            play sound "audio/SFX/CuttingBody.wav"
            "I'm desensitized enough to the smell and far enough away from it to get the brunt."
            "He never specified what he's hoping to learn from it."
            "Age? Diet?"
            "These things internal make up is too inscrutable for me to guess." #add apostrophe to 'things'
            show dominic body neutral
            dm "Right. Right."
            dm "What {i}could{/i} interest you, is an old colleague of mine."
            show dominic body thinking
            dm "We did some work together- she specialized in Paragon behaviour."
            dm "A dangerous gambit."
            play sound "audio/SFX/PeelParagon.mp3"
            "His brows furrow as he peels the sample like its an orange."
            dm "Last I heard, she came across one that she built an actual rapport with."
            show dominic body sad
            dm "She was trying to come to...some sort of understanding. An attempt to sate its hunger without it hollowing her out."
            dm "Give it a taste of humanity."
            show andrea stern
            "I feel myself straighten up."
            ab "Do you think there was anything to it?"
            "He shrugs."
            show dominic body excited
            dm "Possibly! It could be hubris!"
            dm "I haven't heard from her in some time. Not promising."
            show dominic body neutral
            dm "But, she was always cagey. I think she was worried folks would take chagrin with her theory."
            "I allow the sliver of relief his words give me to relax my muscles and steady my breathing."
            ab "Where is she now?"
            show dominic body thinking
            dm "Last I heard, she was up in Nevada-"
            "A few days drive if we gun it."
            dm "-I should have her number and address, somewhere. I can get those."
            show vera neutral
            vl "Can you do it now?"
            "She glances at the sheen of viscera coating his gloves."
            vl "Or maybe you could, Avery?"
            dm "You heard the nice lady."
            dm "It should be in the cabinet there-"
            dm "Rina Becker was her name."
            al "On it."
            "Avery slips off the chair with their usual urgency."
            hide dominic with dissolve
            "As we wait, Vera joins me against the wall."
            show vera body shirt3 neutral2 with MoveTransition(0.7):
                xoffset 20
            "She leans against my side and sighs."
            vl "The drives gonna be a pain."
            "She mutters."
            vl "I hope the lady gives us more than another goose chase."
            show andrea neutral
            "I lean against her in turn."
            ab "C'mon, it's something."
            show vera annoyed
            vl "{i}Hmrgh...{/i}"
            show vera neutral2
            vl "I'm just tired of running around."
            vl "And just normal-tired."
            ab "Same."
            "It's like being reminded of your breathing. I only register it now that Vera has pointed it out."
            "My eyes sit heavy in my sockets and a dull ache pulses through my muscles."
            ab "Wanna sleep in the car?"
            vl "Yeah. Don't wanna bother flagging down a motel."
            show avery body neutral at right:
                xoffset 200
            al "This should be it."
            "Avery appears in front of us, a scrap of paper in hand."
            show andrea happy
            ab "{i}Nice.{/i}"
            "A phone number with an unfamiliar area code is scribbled on it, beneath an address."
            show vera annoyed
            vl "This better still be good."
            
            dm "Here's to hoping!"
            play sound "audio/SFX/WetNoise.mp3"
            "{i}Squelch{/i}. He's moved on to another chunk of the Paragon. This one is bulkier than the other one."
            "It looks like a fleshy layer cake from the side."
            vl "Awesome. Thanks a bunch you two. Let's go."
            show vera body shirt3 annoyed with MoveTransition(0.2):
                xoffset -40
            "She's already moving out the door."
            al "Ah- good luck out there,"
            ab "Thanks."
            dm "Tell Sloane hello for me!"
            
            ab "For sure."
            "Vera doesn't respond, just picks up the pace."
            play sound "audio/SFX/FastFootsteps.mp3"
            hide vera with moveoutleft
            pause 0.3
            scene car bg aznight with fade
            
         
            show vera bodyflip shirt3flip neutral2flipped at vera_car
            vl "Glad I don't have to deal with those two anymore."
            show andrea body neutral at andrea_car
            ab "Really? I couldn't tell."
            ab "Dominic was helpful but, y'know, I get it. He was kinda- {i}eh{/i}."
            ab "But, what did Avery do?"
            show vera angryflipped
            vl "It's just, like-"
            "She throws her hands in the air."
            vl "{i}You know?{/i}"
            ab "Not really."
            vl "It's like...like- when you see a hamster, or a mouse, just some kinda tiny animal."
            show vera annoyedflip
            vl "And they just kinda stare up at you? And you know you can squish 'em so easy."
            show vera neutral2flipped
            vl "And you know you shouldn't, but also you just kinda wanna-"
            #show 
            "She clasps her hands together."
            show vera angryflipped
            vl "And it's {i}so{/i} annoying, 'cause they're sitting there, and they don't even know."
            ab "Uh-huh."
            "I nod slowly."
            show vera neutral2flipped
            vl "You think I'm being an asshole."
            ab "No-well-"
            show andrea stern
            ab "Kind of-"
            show andrea offput
            ab "But not-"
            
            ab "Just weird. You have to know that too."
            "She leans in her seat."
            vl "I know. I didn't think you'd get it."
            "I resist the urge to roll my eyes."
            "This again."
            show andrea neutral
            ab "It'd be easier if you explained it like a normal person."
            ab "Just say you think they were dumb, or annoying."
            ab "Keep it concise."
            vl "Guess they were naiive, or whatever."
            show vera annoyedflip
            vl "They'll bite it at some point. I can feel it."
            show andrea stern
            ab "'Cause you think they're not prepped properly?"
            vl "Yeah, that. Also, it's just kinda stupid to think you can be in this line of work without getting your hands dirty."
            show vera sadflipped
            vl "Just annoying."
            "I {i}tap, tap, tap{/i}, my fingers on the wheel."
            ab "That's presumptious."
            ab "They might get it, maybe they're just not excited to share with someone they  just met."
            show vera annoyedflip
            vl "You asked."
            "Maybe I {i}should{/i} have just left her to her neuroses."
            "Getting Vera to change her mind about anything once she's set on it is like pulling teeth."
            ab "I know, I know."
            "I don't want to agree just to pacify her, but I'm not about to lecture her, either."
            show andrea neutral
            ab "...Let's just take what we can get. Neither of them are your problem anymore."
            "She presses her hands into her eyes."
            vl "Mhm, yeah."
            vl "You're right."
            show vera neutral2flipped
            vl "We should probably park somewhere else."
            vl "We'll get weird looks if we stay here over night."
            "We're of the same mind- I'm already starting the car."
            #show menu, music?
            "I drive for a bit - half an hour - then pull into the first rest stop I see."
            "Vera passes out a few minutes after I stop."
            "For a light sleeper, she can pass out basically anywhere."
            hide vera with dissolve
            "I let the car run a little longer, trying to make as much use of the AC as I can, then turn it off."
            "Its death leaves me with nothing besides the buzz of cicadas and Vera's breathing for company."
            "As tired as I am, you'd think it'd be easier to fall asleep."
            "I should practice what I told Vera and just let this lead give me some peace of mind."
            "Even if it's self-delusion, it's not too bad in small doses."
            "But, I'm restless."
            "We're at the whims of some weirdo again."
            "We could just be sent on another errand run before we get anything useful."
            "It wouldn't as bad if I didn't have that {i}thing{/i} pacing around the back of my mind."
            "I don't know when Burn's better nature will rear its head again."
            "Every delay is another invitation for it to demand tribute."
            "I'm lucky it hasn't taken my attempts to seperate us as a slight."
            "Maybe it has that little faith in me."
            "I lean the car seat back as far as I can."
            show andrea sad
            "I'll prove it wrong- I {i}have{/i} to."
            show andrea offputEC
            "{i}Thick, pooling blood. Stinking corpse flesh. The last gasps of air spasming through the body in a death rattle.{/i}"
            "I won't let Vera throw some poor idiot in front of me like she's a cat depositing roadkill on their door step, then wondering why they aren't eating."
            "This won't be a dead end."
            "I'll get something out of Rina."
            show andrea neutral
            "I stop my train of thought at that."
            "Nothing past that is worth mulling over."
            "{i}Tiger, Tiger, burning bright.{/i}"
            stop music
        play sound "audio/CarAmbient.mp3" #dominic music is still playing here. Prolly should keep scene silent
        scene carbgazday with fade
        show andrea body neutral at andrea_car
        "The next day goes by quickly, so does the day after that."
        "It's just road, and road, and road."
        "The endless expanse of highway, only broken up by exits or signage."
        "I keep an ear out for any reports on the radio about what happened at the UaUa's."
        "If there's anything, it's not important enough to make it past state lines."
        "We {i}did{/i} do a decent job at clean up."
        "We reach Nevada about three days in. Our exit takes us into rocky lowland, dotted with sagebrush, thats gradually joined by juniper pine."
        "Vera says something at some point about wishing Dominic's buddy had decided to hide out in Las Vegas instead of the middle of nowhere, but I don't mind."
        "Even if I moved around a lot as a kid (perks of being a military brat), it was never by car."
        "Taking in the scenery doubles as an indulgence and a sanity check."
        "Noting every rise and dip in incline and keeping an eye out for flashes of feathers fluttering through the withered bush stops my focus from drifting."
        "Our exit arrives with so little fanfare that I almost miss it."
        "The road cracks and becomes pockmarked with rock as I turn onto it."
        "I vice grip the wheel of our little ship in the night, like it'll do anything."
        "We pull into the first place we find. I'm not trusting any rest stop this far out."
        "This motel is one of the better ones we've hit."
        "The blankets aren't too scratchy and the AC sputters on without issue."
        "Quality wouldn't have made much of a difference, tough."
        "Three days of almost straight driving have congealed with the lingering effects of the fight to weigh down my body like tar."
        "I'm out like a light."
        label before_husk_hotel :
            
            scene hotel1 at alt_hotel: 
                blur 3.6
                pause 0.1
                blur 3.5
                pause 3.4
                blur 3.4
                pause 0.1
                blur 3.5
                pause 0.1
               
               
                repeat 
            #scene hotel1 at alt_hotel
            "..."
            "Vera's voice drags me out of a dreamless sleep."
            vl "-hey."

                
            show vera body shirt1 neutral2 at vera_spot:
                blur 2.1
                pause 0.3
                blur 2.3
                pause 0.3
                blur 2.5
                pause 0.3
                blur 2.7
                pause 0.3
                blur 2.5
                pause 0.3
               

            
        "I groan and turn onto my side."
        "The air smells bitter. Vera's probably put the coffee machine to work."
        ab "Give me a sec."
        "No one's dying, I can spare a few seconds shut eye."
        show vera neutral
        
        vl "C'mon. Up."
        "She puts a hand on my shoulder and shakes me."
        "With some impression of grace, at first-"
        show layer screens:
            blur 4
        vl "Up."
        show layer screens:
            blur 0
        "Then, when I screw my eyes shut tighter."
        show hotel1 at alt_hotel:
            blur 0.0
        show vera body shirt1 neutral2 at vera_spot:
            blur 0.0
        
        vl "{i}Up.{/i}"
        show andrea body annoyed at right:
            blur 0.0
        #rustling noise
        ab "God- I'm up! I'm up."
        vl "Sorry, you were {i}out.{/i}"
        "She withdraws her hand and leans back."
        vl "You're usually all about the bright and early."
        show andrea neutral
        ab "I guess the adrenaline finally wore out."
        "I massage my face and pull my bonnet off."
        "We {i}should{/i} get into gear."
        show vera sad
        vl "{i}Aw{/i}, poor thing."
        show vera neutral
        vl "Want me to get you some coffee?"
        ab "That'd be great, I'm dying here."
        show andrea happy
        "I lay my hand on my forehead dramatically."
        "She rolls her eye and obliges."
        vl "You're like...a baby bird, or something."
        "The styrofoam cup she hands me is lukewarm."
        ab "Way to paint an appealing mental image."
        "I can taste the exessive amounts of sugar she's put in before the coffee hits my tongue."
        vl "The town's pretty small, I don't think it'll take too long to look."
        "I hadn't gotten a good look at the place when we checked in, but that tracks."
        "The view out the window is to a modest town center."
        "A couple store fronts, a restaurant."
        "The beginnings of a residential block extend behind the latter."
        "At a glance, it's doing a better job at seeming alive than our last locale."
        show andrea neutral
        ab "I'm going to try giving Rina a call again."
        "It's my fourth time since we left Dominic's place."
        "If we're going to be grilling her, it'd be better to give her a heads up."
        "I'd rather come off as pushy, instead of catching her off guard."
        vl "Be my guest."
        "I type her number up and listen to the {i}ring, ring, ring{/i}."
        vl "Why do you think she's not answering?"
        #dial tone
        "{i}Ring, ring, ring.{/i}"
        ab "Like Dominic said, it could be she changed numbers."
        show vera neutral2
        vl "Mmm...wouldn't it say this one was out of service?"
        ab "Maybe whoever got it doesn't want to answer either."
        "{i}Ring, ring, ring.{/i}"
        vl "You'd think they'd get curious after a bunch of missed calls, though."
        ab "Unless they thought it was spam."
        show vera neutral2
        vl "Maybe."
        "{i}Ring, ring, ring.{/i}"
        ab "Or she lost her phone. Or broke it."
        ab "Could be a bunch of other reasons."
        "The automated voice box recites the same line it's met me with every other time I've called."
        "She hasn't even set it up."
        vl "I don't like it, feels like a bad sign."
        "I sigh and set the phone down."
        ab "Well, it's what we've got. I'm gonna settle on her just being inattentive."
        "It saves me some mental real estate."
        vl "It's just {i}annoying.{/i}"
        show andrea annoyed
        ab "You've made that clear"
        ab "All of this is annoying."
        "Vera sips her drink, mumbling something indistinguishable into it."
        "I guess the response isn't meant for me, because the only thing I get is a thumbs up."
        "Whatever her thoughts, we're of the same mind to head out quickly."
        "My breakfast is the rest of my coffee and some pistachios from the vending machine."
        "Then, it's into town we go. "
        scene parking lot with fade #not drawing a neighborhood so just assigned this to a parking lot since it fills the closest niche
        play music "audio/Music/Ambience/ominousambient.mp3" loop
        "The neighborhoods are kind of a bitch to navigate."
        "The suburban sprawl tangles all over itself. One neighborhood twists into another, that leads right back to where we started."
        "Poplar Lane is the same as Bellview Road is the same as Brighton Drive."
        "We retrace our steps probably five times over, before we reach {i}'Turnpike Street'.{/i}"
        "The house is unremarkable. There's not even any yard decorations to seperate it from its fellows."
        label neighborhood:

            show vera neutral body shirt2 at vera_spot
        vl "I was half expecting it to be all overgrown and decrepit."
        vl "Like. {i}Blair Witch{/i} shit."
        show andrea body neutral at right
        ab "Why?"
        "On the contrary, it seems allergic to any signs of habitation."
        "Windows curtained shut. Spotless stoop."
        "If not for the car pulled into driveway, I would've taken it for vacant."
        vl "Just a hunch."
        "I make a show of looking down into the sewer grate."
        ab "Well. No witches here."
        show vera neutral
        vl "My hero."
        vl "{i}Anyway.{/i}"
        "She takes the lead up the front steps."
        "We'd tossed around the 'angle' we're coming at this from over the last few days."
        "It's about the same direction we took with Dominic, just claim intellectual curiosity, then play it by ear from there."
        "Vera presses the doorbell."
        play sound "audio/SFX/doorbellfail.mp3"
        "It makes a low, sputtering noise, like some kind of dying animal."
        "We wait a few seconds."
        play sound "audio/SFX/DoorKnockNormal.mp3"
        show vera annoyed
        vl "Hey! Anyone around?"
        "A car rumbles past behind us."
        play sound "audio/SFX/KnockLoud.mp3"
        vl "Hello?"
        "{i}Could be that she's asleep.{/i} It's afternoon, but early enough that a late riser could still be in bed."
        ab "Let me try."
        show vera neutral
        vl "What. Can you knock better than me?"
        "I still give it a shot, maybe adding some rhythm into it makes it sound more approachable."
        play sound "audio/SFX/RhythmKnock.mp3"
        "Nothing."
        show vera annoyed
        vl "Fucker better not have given us the wrong address."
        show andrea annoyed
        ab "{i}Someone{/i} lives here."
        "Vera presses her face against the window."
        vl "I can't see anything in there."
        "Shit. {i}Shit.{/i}"
        play sound "audio/SFX/DoorRattle.mp3"
        "I gingerly try the door handle. It doesn't budge"
        show andrea offput
        ab "Let's check for a back door."
        show andrea neutral
        vl "Yeah."
        #walk noise
        "Keeping an eye out for any onlookers, I go around the lawn, towards the back of the house."
        "A glass screen door leads into what I assume is a basement. I can't really make anything out besides a washing machine and some laundry."
        play sound "audio/SFX/GlassKnock.mp3"
        "I knock, still no answer."
        "Vera tries the door. Doesn't budge."
        ab "So-...alright. This sucks."
        vl "I told you something was gonna be up."
        show andrea body annoyed
        ab "Yeah, yeah. You're right. Fuck me for being optimistic."
        show vera angry
        vl "I didn't mean it like-...ugh, whatever."
        vl "We've gotta get in somehow."
        ab "I don't think there's any other doors."
        show vera neutral2
        vl "Guess we're working with what we have, then."
        "She pats herself down and fishes her hands into her pockets."
        show vera neutral
        vl "Do you have anything thin and pointy on you? Bobby pins, hair clips, needles?"
        show andrea stern
        ab "You want to break in?"
        vl "This is our only lead, we'll say it was, like, an emergency if she finds us."
        
        "I pinch the bridge of my nose. We're racking up crimes like its a bingo chart."
        "Still, I check for anything matching the description."
        ab "Would this work?"
        "I offer up a paperclip that's been stowed away in my pants pocket for God knows how long."
        show vera neutral
        label vera_unlock:
            vl "Perfect, thanks Andy."
        "She bends the clip in half and inserts it into the lock."
        "With the same  precision she uses to knock her cross bow, she coaxes the ends into place."
        play sound "audio/SFX/LockPickingLoop.mp3" loop
        "For someone who's usually so loose, it's a little enamoring to see how sure her movements are."
        "Where'd she even pick this up?" 
        "Now's not the time to ask."
        "A minute or so later, she pulls the clip out, and tries the handle."
        play sound "audio/SFX/LockClick.wav" 
        show vera happy at sprite_jump
        vl "There we go."
        vl "No signs of forced entry either."
        ab "I hope we don't have to worry about that."
        show andrea neutral
        ab "Handy trick, though."
        scene basement
        show layer master at night_filter_less
        stop music
        "We step inside, kicking up a cloud of dust in the process."
        "It's a maze of taped up boxes and fabric swathed furniture."
        "As my eyes adjust, I can make out the load of laundry stuffed into the washing machine."
        "I consider calling out, but hearing voices from the basement isn't going to breed much trust."
        "We feel our way through the darkness."
        show vera body shirt3 neutral2 at vera_spot
        vl "No one's down here."
        "Vera keeps her voice low."
        show andrea body neutral at right
        ab "Guess we gotta get upstairs."
        "The further we get, the more the clutter down here seems to press in on me."
        "Reaching the bottom of the stairs feels like emerging out of some dark tunnel."
        "I rise onto my tip toes. {i}Keep to the back of each step, they're firmer.{/i}"
        "I grip the handle and - inch by painstaking inch - turn it, then push."
        label husks_livingroom:
            $ husk_checked = False
            scene livingroomhuskim with fade
            "Dull light catches the dust particles, revealing some kind of study."
            
            
            ab "Reminds me of Dominic's lab." 
<<<<<<< Updated upstream
        show andrea body neutral at right
        vl "The nerdy types are all the same."
        show vera body shirt3 neutral2 at vera_spot
        "She tracks her gaze across the room. I follow it." 
        "Empty."
        show vera neutral #I didn't actively go and cut it but I'd get rid of this part. Good bit but the pacing is awkward and confusing esp since smth like it hasn't happened before
        with dissolve
        pause 0.7
        show andrea stern
        with dissolve
        pause 0.9
        vl "I mean, there's no one in here."
        vl "I'm sure she'd appreciate someone admiring her research."
        ab "Let me just-"
        "I carefully crack the door open into the next room."
        "No signs of life."
        ab "It's clear."
        "While I've had my back turned, Vera's already beelined for the weapons hanging on the wall."
        "I sigh. Alright, we've already begun our invasion of privacy. What's some more among friends."
        #make this an image map
        label invest_husk: #there's an error message here, I assume it's cuz the image map isn't completed but still is of note
            if  weapon_examined == True and shelf_examined == True:
                jump after_husk
=======
            show andrea body neutral
            vl "The nerdy types are all the same."
            show vera body shirt3 neutral2 at vera_spot
            "She tracks her gaze across the room. I follow it." 
            "Empty."
            show vera neutral
            with dissolve
            pause 0.7
            show andrea stern
            with dissolve
            pause 0.9
            vl "I mean, there's no one in here."
            vl "I'm sure she'd appreciate someone admiring her research."
            ab "Let me just-"
            "I carefully crack the door open into the next room."
            "No signs of life."
            ab "It's clear."
            "While I've had my back turned, Vera's already beelined for the weapons hanging on the wall."
            "I sigh. Alright, we've already begun our invasion of privacy. What's some more among friends."
>>>>>>> Stashed changes
            $ weapon_examined = False
           
            $ shelf_examined = False
            label invest_husk:
                if  weapon_examined == True and shelf_examined == True:
                    jump after_husk
                else:
                    call screen husks_living_map
            #make this an image map
        #label invest_husk:
            
            #$ weapon_examined = False
           
            #$ shelf_examined = False
        #menu:
            #"Weapons rack." if weapon_examined == False:
                #jump weapons

          
            #"Shelf." if shelf_examined == False:
                #jump shelf
        
        label weapons:
            hide screen husks_living_map
            "I join Vera as she peruses the display."
            "Her eye glimmers, like she's a kid on Christmas."
            show vera body neutral
            vl "I think these are legit."
            vl "Proper Paragon ones, not just replicas."
            "She gestures to a machete, with a lattice work of runes trailing down the blade."
            show andrea body neutral
            ab "You think she made these herself?"
            vl "{i}Maybe?{/i} Could be that I haven't given her enough credit."
            vl "She'd have to be pretty strong to take down this many."
            "As her hand inches closer to it, I shoot her a glance."
            show andrea stern
            ab "Don't {i}touch{/i} it, we don't know what any of these can do."
            "She should know better than me."
            show vera annoyed
            vl "I wasn't gonna, I'm not stupid."
            "Still, she lowers her hand."
            show vera happy
            vl "I've got my baby, she's enough for me."
            "She pats her back, where her crossbow is tucked away."
          
            "I turn my attention to the rest of the display."
            show andrea neutral
            ab "One's missing."
            "The rack is narrower than the others."
            "It could be that it's just never been used, but it's right in the middle of the display."
            vl "So it {i}is.{/i} We can keep an eye out. If she's been looking at it lately, it could be useful."
            $ weapon_examined = True
            jump after_husk
        
        label shelf:
            hide screen husks_living_map
            "It's hard to know where to start. The selection seems arbitrary: shining hard cover next to barely held together journals."
            "Thin paperback, barely a few pages long, squashed by bloated leather bound tomes."
            "I opt for something that looks handwritten. It's one of those cheap, moleskin notebooks."
            play sound "audio/SFX/FlipPage.mp3"
            "Compared to the other ones I skim, the pencil looks fresher."
            "Taped near the front is a parchment paper fold out. A sketch of...something, spans across it."
            "Some sort of Paragon. It's mammalian in appearence. Its body is compact, with four goat like legs sticking out the bottom."
            "The face is somewhere between a muzzle and a snout: mostly compact, with a curved nose sticking out of it." #swap out either the 'compact' in this sentence or the previous one
            "Labels make notes of its anatomy and demeanor."
            "{i}Weakened, possibly split apart recently.{/i}"
            "{i}Docile, conversational.{/i}"
            "{i}Signs of desperation.{/i}"
            "It continues like that up until the mid point."
            "The rest is blank."
            "I take a few moments to log the information, then put it back."
            $ shelf_examined = True
<<<<<<< Updated upstream
            jump after_husk

=======
            jump invest_husk
        
>>>>>>> Stashed changes
        label after_husk:
            $ husk_checked = True
            "We don't find anything else of note between the two of us."
            show vera neutral2
            vl "You sure you don't want to at least try one of these guys out?"
            "She's still lingering by the weapons display."
            vl "The hammers cool, but- y'know. It can only do so much."
            show andrea neutral
            ab "I'm fine with that. I don't want to deal with whatever bells and whistles those things have."
            "There isn't much uncertainty with a hammer. It goes where you want, as long as you're decisive."
            "It doesn't care about how many shots it takes to make a circuit or whatever other rituals Vera's crossbow and its ilk demands."
<<<<<<< Updated upstream
            "It's as eager to pulverize exoskeleton as it is hide as it is flesh and bone and brain fried with animal fear."
            "I shove my hand in my pocket."
=======
         
          
            "It's as eager to pulverize exoskeleton as it is hide as it is flesh and bone and brain fried with animal fear."
            "I shove my hand in my pocket."
           
>>>>>>> Stashed changes
            show andrea stern
            ab "We should check out the rest of the place. I don't think there are many other rooms."
            ab "We can come back around here later."
            vl "Good with me."
            "I push open the door. No one's magically appeared in hall in the last twenty minutes."
          
            "She runs her finger down a dust soaked coffee table with a grimace. Particles catch in the rays of light that make it through the shutters."
            vl "It doesn't look like anyone's done, like, {i}anything{/i} here in a while."
            "This is gradually turning from a home invasion to a wellness check."
            ab "We can say Dominic was worried about her health."
            "I almost forget to keep my voice down."
            "She's around here somewhere."
            "I uncoil the worry beginning to knot in my chest."
            "Things are fine until proven otherwise."
            vl "Well, she's either still in bed, or she fell asleep in the bathtub."
            "She gestures at the two rooms branching from the end of the hall."
            ab "{i}Yup.{/i}"
            "So, which first?"
            "There isn't a way to tell which is which."
            menu left_right:
                "Left.":
                    jump bathroom
                "Right.":
                    jump bedroom

            label bathroom:
                "I swallow and crack open the door on the left."
                "Spotless white-tiled floor. A shower enclosed in glass."
                "Empty."
                jump left_right

            label bedroom:
                "I turn the knob- {i}try{/i} to turn it."
                "It's locked. Locked from the inside."
                show andrea neutral
                ab "Someone's in there."
                "I give a few, soft knocks. This is still a break in. I wouldn't blame her from holing up."
                ab "Uh, Ms. Becker?"
                "I keep my voice low and press my ear against the door."
                "The only sound is the {i}woosh{/i} of a fan."
                play music "SFX/CeilingFan.mp3" loop
                "I knock again, with a bit more force."
                play sound "SFX/KnockDoorHard.mp3" 
                ab "Dominic sent us, he said you worked together."
                ab "We wanted to see if everything was okay."
                "Vera joins me against the door."
                "When there still isn't a response, she sighs."
                vl "I think we have to break it."
                "She points at the knob. It doesn't have a key hole."
                ab "...Yeah, guess so."
                "I'll bite the bullet on adding property damage to our list of crimes."
                "I grab one of the decorations from the living room- some kind of marble orb."
                vl "Try not to get the knob, aim right next to it."
                vl "Something about the mechanism."
                ab "Mhm."
                "I raise it over my head and slam it into the door. Once, twice."
                play sound "audio/SFX/HitDoorKnob.mp3"
                "Behind the grate of metal against thick wood, there's a low click."
                "The force is enough to push it open."
                "I step in and-"
                play music "<loop 19.20>BodyFindWhole.mp3"
                show andrea offput
                ab "{i}Jesus Christ.{/i}"
                #husk discovery music needs to be added
                #show vera scared
                show vera sad
                vl "Shit."
                "And it's stupid to react like this, right?"
                "The room shouldn't spin and bile shouldn't be in my throat."
                "Second time in a week days I've smelled, felt, {i}seen{/i} corpse flesh. And the first one that isn't on my hands."
                "It's funny, funny, so fucking {i}funny.{/i}"
                "'Cause isn't your brain supposed to have some kind of safe guards?"
                "Some curtain of apathy to keep you from breaking at the seams."
                "Melting into a sweat-soaked, watery-eyed mess of chattering teeth and rapid breaths."
                "Breaths that taste like meat left out in the summer sun."
                show andrea offputEC
                "Like a kid diving under a blanket, all I can do is screw my eyes shut."
                scene black
                "{i}Spineless little girl.{/i}"
                "Vera draws in a sharp sigh. I expect a jab, something dripping with dissapointment."
                vl "{i}Shit- i'll- let me check it out."
                "I feel her shuffle past me."
                "I'll give myself a few seconds to knit back together."
                "{i}Tyger, tyger.{/i}"
                scene back_at_corpse
                show andrea body offput at right
                show vera body shirt3 neutral2 at vera_spot
                "I peel my eyes open."
                "Vera crouches by the corpse, her hand hovering over the mark on its chest."
                vl "Stab wound, I think."
                vl "Not {i}too{/i} deep."
                "I keep my back against the wall as I shuffle closer."
                "If I can't keep my eyes on it, I may as well put them to use."
                label checking_corpse: #error pops up for this whole segment, prolly due to lack of image map. Still noting anyways
                    
                      
                    $ weapons_check = False
                    $ pill_check = False
                    $ chains_check = False
                    menu corpse_menu:
                        "Weapon.":
                            $ weapon_check = True
                            jump weapon
                        "Pill Bottle.":
                            $ pills_check = True
                            jump pills 
                        "Chains":
                            $ chains_check = True
                            jump chains
                        "Move on." if weapons_check == True and pills_check == True and chains_check == True:
                            jump after_check_husk

                
                label weapon:
                    "A stab wound. A knife. Icepick. Something like that."
                    "Nothing sticks out."
                    "I almost miss it."
                    "It's shoved a little ways under a night stand."
                    "Something metallic that just barely catches the light from the window."
                    play sound "audio/SFX/MetalSlide.mp3"
                    "I pull it out: it's the hilt of...something."
                    "The blade is missing. Clean: like it was never there in the first place."
                    "Runes wrap all the way around it."
                    "Maybe I'll compare it to the rack from earlier."
                    jump corpse_menu

                label pills:
                    "There. On the nightstand."
                    "It's a clear bottle with a yellow wrapper: must be OTC."
                    ab "Melatonin?" #is this actually melatonin or just andrea's guess? cuz there is literally no way melatonin can knock u out that bad. I have taken like. 6 gummies at a time and have just tanked that shit before idk much you'd have to take to pass out and not notice yourself dying
                    "It's empty."
                    "I hazard a glance towards the body, just enough to get a glimpse of the face."
                    "The mouth is ajar. Nothing comes from it."
                    vl "I don't think it's the stuff that did her in."
                    vl "Either it wasn't enough, or she got-got before it had a chance."
                    jump corpse_menu
                label chains:
                    "Some kind of spike has been crudely nailed into the wood floor. A metal chain is attached to it."
                    "It goes halfway across the room - ending in a cuff - that stops just short of the ankle."
                    "{i}It got in the floor somehow.{/i}"
                    "A hammer. Nails next to it. Near the corner of the room."
                    jump corpse_menu


                label after_check_husk:
                    "I relay my findings to Vera."
                    "She's conducted her grim work in silence."
                    show vera neutral2
                    vl "I don't think she's been dead for too long."
                    "She doesn't sound sure."
                    show andrea body offput
                    ab "Shouldn't- you shouldn't-"
                    ab "Probably shouldn't touch your hair-..after-"
                    "It's half reprimand, half forced out, grating attempt at humour."
                    show vera annoyed
                    vl "I'll shower later."
                    show vera neutral2
                    vl "Anyway are you-...do you need to sit out?"
                    vl "Or something."
                    ab "I'm good."
                    show andrea stern #i got rid of the dissolve, I see the effect you're going for. But it pauses the action too long which makes it awkward
                    ab "I'm good."
                    vl "...M'kay."
                    vl "Well. It looks like she was killed in one."
                    vl "There were a couple other marks around it, but only one of those went deep enough."
                    vl "And-"
                    "With uncharacterstic hesitation, she lifts up the corpse's shirt."
                    "A floral pattern winds around her side, all the way across her stomach."
                    "The skin is raised like a scar and tinted a jaundiced yellowish-green."
                    "It might've been pleasant once. It's hard to tell with how gaunt her skin's gone."
                    "I ball my right hand into a fist, then peel off the glove."
                    "The color is different- deep crimson rather than sickening green- and the harsh lines cluster closer together."
                    "I dig, dig, {i}dig{/i} my teeth into my cheek to keep my expression in check."
                    show andrea sad
                    ab "Same as me."
                    vl "{i}Yeah.{/i}"
                    "Vera crosses her arms."
                    ab "So-...so she was-..."
                    ab "She was trying to fix it."
                    "That's the only option."
                    "This is too much set up for a suicide."
                    "No signs of a struggle."
                  
                    vl "I guess she missed something."
                    "That's it, right. She missed something."
                    "Doesn't mean we will. We have time."
                    show andrea offput
                    ab "Study. Let's check out the rest of it."
                    vl "Maybe this'll give us some stuff to chew on."
                    "I'm already out of there."
                    "The musty air drives away the sweet decay cling-wrapping the inside of my throat."
<<<<<<< Updated upstream
                    scene livingroomhuskim #add msuic here
=======
                    scene livingroomhuskim
>>>>>>> Stashed changes
                    "{i}What now?{/i}"
                    "What am I looking for?"
                    "{i}Chew on?{/i}"
                    "What does one-hundred and however many pounds of dead flesh do for me?"
                    $ weapons_2_checked = False
                    $ shelf_2_checked = False
                    
                    
                    label invest_husk_2:
                        if weapons_2_checked == True and shelf_2_checked == True:
                            jump husk_study_checked_2
                        else:
                            call screen husks_living_map
                   #     if weapons_2_checked == True and shelf_2_checked == True:
                    #        jump husk_study_checked_2
                    #menu:
                     #   "Weapons." if weapons_2_checked == False:
                      #      jump weapons_2

                       # "Shelf." if shelf_2_check == False:
                        #    jump shelf_2

                label weapons_2:
                    play sound "audio/SFX/MetalClick.mp3"
                    "I lay the hilt on the empty rack, it slides in easily."

                    "Based on the distance from the other end, it couldn't have been that big."
                    "I mumble as much to Vera."
                    show vera body neutral shirt3 at vera_spot
                    vl "That tracks. Dagger, hunting knife, in that vein."
                    show andrea body sad at right
                    ab "You think it matches the size of the-"
                    "Vera cuts me off, like she assumes I won't be able to choke it out."
                    show vera neutral2
                    vl "I'm not an expert, but I think it matches the wound."
                    "{i}Why did she think this could help?{/i}"
                    "{i}What did she use to make it?{/i}"
                    $ weapons_2_checked = True
                    jump invest_husk_2
                label shelf_2:
                    "I flip open the journal from earlier."
                    "{i}Flowers.{/i}"
                    "Crudely sketched daffodils and chicken scratch daisies decorate the Paragon's body."
                    show andrea body offput at right
                    ab "This one."
                    ab "{i}This{/i} is the one."
                    "The one she let under her skin."
                    "Desperation?"
                    "Curiosity?"
                    show vera body neutral2 shirt3 at vera_spot
                    vl "She makes it sound like its a lot less of a nightmare than Burn."
              
                    $ shelf_2_checked = True
                    jump invest_husk_2
                
                label husk_study_checked_2:
                    hide vera
                    hide andrea
                    "I shove the hilt and the journal into my bag."
                    "Alright. What next. There's more here."
                    show vera body neutral2 shirt3 at vera_spot
                    vl "Hey."
                    show andrea body neutral at right
                    ab "What?"
                    "Vera's been lingering behind me."
                    vl "Are you-...can you do this? Like. Now?"
                    "Her sentence sounds cobbled together, like each word's been clipped onto the other hastily."
                    ab "You mean look around?"
                    show vera sad
                    vl "I guess. Or put stuff together. Or whatever."
                    "She rubs her arm."
                    "I swallow. I've loosened my grip too much- of course I have."
                    "She doesn't meet my gaze."
                    "{i}What's pooling in her eye?{/i}"
                    "Exasperation as I unspool again? Vindication that she's right about me?"
                    "Some haphazard attempt at sympathy?"
                    "I shrug."
                    ab "I'll deal."
                    "Whatever it is, I don't need to give her more reason to think I can't handle myself."
                    "Vera lingers in that uncertainty for a moment: brows furrowed, teeth gnawing at her lip."
                    vl "Cool. Good to know."
                    show vera neutral
                    "She claps."
                    vl "Lets keep going, then."
                    play sound "audio/SFX/FootstepSingle.mp3"
                    "Whatever part of me haven't tensed to their breaking point go rigid."
                    show andrea scared
                    ab "What was that?"
                    "I whisper."
                    vl "Dunno."
                    "It could just be the house settling, but it's been quiet so far."
                    ab "You think someone saw us get in?"
                    vl "Maybe. Weird that they wouldn't have called the cops."
                    "That just tightens the knot in my stomach."
                    "Don't like the idea of someone comfortable enough to enter on their own."
                    play sound "audio/SFX/FootstepSingle2.mp3"
                    "My senses are primed enough that I hear it, soft as it is."
                    "It's closer."
                    ab "I think we should go."
                    ab "We can always come back later."
                    "Better to be paranoid and avoid a fight, than test my luck."
                    show vera neutral2
                    vl "Can we?"
                    "I just narrow my eyes, that's enough for her."
                    "She gestures at the door- closed, but not locked."
                    "Then, at the stairs."
                    "I allow myself one, two, three seconds of consideration."
                    "The stairs. Speed is our priority."
                    "I step onto the center of the floorboards as I move towards them."
                    "Vera follows suit."
                    "We move past the couch, the desk, the weapons display."
                    #sfx weapon?
                    #music
                    "The door's thrown inward with a screech of wood and metal."
                    "The knob slams into the drywall with enough force to crack it."
                    "In it's wake a figure appears: coiled muscle hewn in to a broad frame, swathed in scarlet, and poised for violence."
                    "Her narrowed eyes betray no anger, just the certainty that she's exactly where she needs to be."
                    "She clutches a spear in her right hand."
                    "There's no hesitation, no demand. Just the fluid movement of her arm and whistle of metal through the air."
                    vl "{i}Move!{/i}"
                    "End. for now." #I would maybe add a black screen before the end card. Otherwise it just feels kinda weird to have it while you can see all the characters
       
        #"Vera's about to knock a third time - fist drawn back as if she's going to sucker punch the mahogany - before the door creaks open."
        #creak
       
    return


    

label game_over:
    "Shit-{i}shit{/i}."
    "Maybe I'm too slow, or Vera's too reckless. Could be we're just unlucky."
    "Doesn't matter- scrambling claws wrap around me all the same."
    $ andrea_vera_health = "good"
    jump combat
    "hi"
        


        #return
        
label examine_done:
        "Looks like we've already found everything here!"
        call screen attack_examine       