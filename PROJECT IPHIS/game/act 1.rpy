label act1:
    "My fingers dig through the wires to find the empty sector. Once I've located the area, I grab the parallel bionic and place it in the null."
    "The whirring of the vent stirred into my sleep deprived brain. Despite the clear reflection of IPHIS's exterior that exacerbated the staring, my eyes scan over the knicks of the coronary arteries."
    "I, precisely, flick a small knob in the heart that turns on the valves' circuits. Systems seem to run smoothly and blue blood sloshes through the visible tubes on her skin."
    "It is routine, but it is still quite fascinating to see a common marker of humanity become remodelled for machines. I can truly never get enough of it."

    # change bg to operating table with blue blood

    "I prepare a fresh cleaning solution and start wiping away the android excess on the operating table."
    "IPHIS is a special case, being an older nurse model. I can treat her with the utmost care, and she'll still find a way to bleed out."
    jump clean1
label clean1:
    scene bg operating table

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
            action [SetVariable("FirstSplatter", True), Jump("clean1")]
    if not SecondSplatter:
        imagebutton:
            xpos 0.245
            ypos 0.63
            xanchor 0.5
            yanchor 0.5
            idle "Table_Splatter_2.png"
            hover "Table_Splatter_2.png"
            action [SetVariable("SecondSplatter", True), Jump("clean1")]

label contAct1:
    "...What a nuisance. At least there is an endless amount of android blood in the lab that I can restore her with."
    "After I'm done wiping, I change my gloves, spray with a different solution, and wipe again."

    # transition scene again to bg of surgery thing
    # ianthe smiling sprite! 
    i "You are holding up well, Iphis. Not many androids survive past a simple bionic replacement."
    p "It is a pleasure."
    "An automated response. I have met newer android models that responded to praise, but IPHIS's response is all the more satisfactory compared to generated glee."
    i "Run me a status report."
    p "{cps=100}Processors are stable."
    p "{cps=100}Memory used is at 40\%."
    p "{cps=100}Cooling systems are stable."
    p "{cps=100}All components are stable."
    i "How about the bionic replacements?"
    p "...{w=0.3}It is not within my bandwidth to answer that question."
    # ianthe, still smiling. she's a sarcastic person
    i "Haah.. I figured."
    i "I'm not fully aware of the ethics of android experimentation, but it can't be at all similar to laws on human experimentation…"
    p "You are correct. There are no laws pertaining to android experimentation."
    i "The one time the government serves me, I suppose. Although, they wouldn't be delighted to hear that I have {i}many{/i} human bionics in my warehouse."
    i "Thank you Iphis. You may return to your station."
    "IPHIS nods and walks off to her chamber. Her movements are unchanging in each step."

    # pause then show

    "I click the operating table light off."


    # sudden black bg (turning the light off) then transition to ianthe in her room on her laptop (futuristic room)
    "<< \"Refusal to answer on bionic replacements. Unknown if her ‘sentience' is developing.\" << endl;"
    "Androids are made to be the simulacrum of humans, which is why many of their components are analogous to our bionics."
    "For instance, the #2aorta functions similarly to a human's aortic value. Due to the nature of our experiments, IPHIS's #2aorta had been spent (thus leaking every now and then), so I had to replace it with a bionic."
    "...IPHIS's ever growing refusals to my questions have been increasing as of late. It almost borders on breaking the 2nd Law, had it not followed her usual logic."
    "This may be because during experiment #30 and experiment #31, I had made slight changes to her controller core by replacing parts of it with limbic and prefrontal bionics."
    "At those times, a persistent bug, possibly existing from her antique design, was taking up 10\% of her memory. A factory reset was in order for the affected areas, but even that was creating a runtime error."
    "I had to do what I had to do. It will not affect the project's success rate."
    jump act3