label act1:
    scene black with Dissolve(1.0)
    n "Click to continue. >>"
    pause
    play music "audio/act 1 final mix.mp3"
    #cg here
    scene cg heart at AnimatedAberate, VHS
    with Dissolve(1.0)
    pause
    n "My fingers dig through the wires to find the empty sector." 
    n "Once I've located the area, I grab the parallel bionic and place it in the null."
    n "The whirring of the vent stirred into my sleep deprived brain."
    n "Despite the clear reflection of IPHIS's exterior that exacerbated the staring, my eyes scan over the knicks of the coronary arteries."
    n "I, precisely, flick a small knob in the heart that turns on the valves' circuits."
    n "Systems seem to run smoothly and blue blood sloshes through the visible tubes on her skin."
    n "It is routine, but it is still quite fascinating to see a common marker of humanity become remodelled for machines."
    n "I can truly never get enough of it."
    hide screen bubble
    # change bg to operating table with blue blood


    scene bg lab at center2, AnimatedAberate, VHS with fade:
        zoom 1.35
    
    n "I prepare a fresh cleaning solution and start wiping away the android excess on the operating table."
    n "IPHIS is a special case, being an older nurse model. I can treat her with the utmost care, and she'll still find a way to bleed out."
    # possible code mechanic here where the player cleans the blood off the table?
    jump clean1

label clean1:
    scene bg operating table with Dissolve(0.5)
    $ default_mouse = "towel"

    default FirstSplatter = False
    default SecondSplatter = False

    if FirstSplatter and SecondSplatter:
        jump contAct1
    else:
        call screen clean1_screen

screen clean1_screen:
    if not FirstSplatter:
        imagebutton:
            xpos 0.175
            ypos 0.575
            xanchor 0.5
            yanchor 0.5
            idle "Table_Splatter_1.png"
            hover "Table_Splatter_1.png"
            action [SetVariable("FirstSplatter", True), Play("sound", "audio/btn_confirm.wav"), Jump("clean1")]
    if not SecondSplatter:
        imagebutton:
            xpos 0.245
            ypos 0.63
            xanchor 0.5
            yanchor 0.5
            idle "Table_Splatter_2.png"
            hover "Table_Splatter_2.png"
            action [SetVariable("SecondSplatter", True), Play("sound", "audio/btn_confirm.wav"), Jump("clean1")]

label contAct1:
    $ default_mouse = "arrow"
    stop sound
    scene bg lab at center2, AnimatedAberate, VHS with Dissolve(0.5):
        zoom 1.35
    show ianthe bored at ianthe1, AnimatedAberate, VHS
    i "...What a nuisance. At least there is an endless amount of android blood in the lab that I can restore her with."
    hide ianthe
    n "After I'm done wiping, I change my gloves, spray with a different solution, and wipe again."
    hide screen bubble
    show black with fade
    with Pause(0.5)
    hide black with fade

    # transition scene again to bg of surgery thing
    # ianthe smiling sprite! 
    show ianthe neutral at ianthe1, AnimatedAberate, VHS
    show iphis neutral at center1, AnimatedAberate, VHS:
        zoom 0.56

    i "You are holding up well, Iphis. Not many androids survive past a simple bionic replacement."
    p speak "It is a pleasure."
    show iphis neutral at center1, AnimatedAberate, VHS:
        zoom 0.56
    n "An automated response. I have met newer android models that responded to praise, but IPHIS's response is all the more satisfactory compared to generated glee."
    i smile "Run me a status report."
    hide ianthe
    p determined "{cps=100}Processors are stable."
    p "{cps=100}Memory used is at 40\%."
    p "{cps=100}Cooling systems are stable."
    p neutral "{cps=100}All components are stable."
    show ianthe neutral at ianthe1, AnimatedAberate, VHS
    i "How are the bionic replacements doing for you?"
    p speak "...It is not within my bandwidth to answer that question."
    # ianthe, still smiling. she's a sarcastic person
    i bored "Haah.. I figured."
    i neutral "I'm not fully aware of the ethics of android experimentation, but it can't be at all similar to laws on human experimentation..."
    p "You are correct. There are no laws pertaining to android experimentation."
    i bored "The one time the government serves me, I suppose. Although, they wouldn't be delighted to hear that I have {i}many{/i} human bionics in my warehouse."
    i smile "Thank you Iphis. You may return to your station."
    hide ianthe
    hide screen bubble
    with Pause(0.7)
    show iphis neutral at center1, AnimatedAberate, VHS with Dissolve(0.5)
    hide iphis with Dissolve(1.0)
    n "IPHIS nods and walks off to her chamber. Her movements are unchanging in each step."
    n "I watch her plug her cannula wire to the port. The tube gleams a bright neon blue in the dark, glistening upon her smooth exterior."
    n "Like a moon in the (artificial) night sky."

    # pause then show
    play sound "audio/lightoff.wav"
    show black
    $ renpy.music.set_volume(0.0, 0.0, channel='music')
    n "It's time for me to head back."
    hide screen bubble with Dissolve(1.0)
    hide screen bubble with Dissolve(1.0)
    with Pause(0.5)
    n "Click to continue. >>"
    pause
    hide screen bubble
    scene bg home at center2, AnimatedAberate, VHS with Dissolve(0.7):
        zoom 1.2
    hide black
    # sudden black bg (turning the light off) then transition to ianthe in her room on her laptop (futuristic room)
    $ renpy.music.set_volume(0.17, 0.0, channel='music')
    nn "<< \"Refusal to answer on bionic replacements. Unknown if her 'sentience' is developing.\" << endl;"
    n "Androids are made to be the simulacrum of humans, which is why many of their components are analogous to our bionics."
    n "For instance, the #2aorta functions similarly to a human's aortic value. Due to the nature of our experiments, IPHIS's #2aorta had been spent (thus leaking every now and then), so I had to replace it with a bionic."
    show ianthe neutral at ianthe1, AnimatedAberate, VHS
    i "...IPHIS's ever growing refusals to my questions have been increasing as of late."
    i "It almost borders on breaking the 2nd Law, had it not followed her usual logic."
    n "This may be because during experiment #30 and experiment #31, I had made slight changes to her controller core by replacing parts of it with limbic and prefrontal bionics."
    n "In short, those bionics are known for regulating human emotion."
    i bored "Sigh... What a troublesome thought."
    i smile "I had to do what I had to do. It will not affect the project's success rate."
    stop music fadeout 1.5
    scene black with Dissolve(1.3)
    with Pause(1.3)

    jump act2
