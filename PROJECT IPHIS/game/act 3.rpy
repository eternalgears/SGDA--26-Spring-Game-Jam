label act3:
# act 3 narrative here
    nvl clear
    c "{b}ACT 3:{/b} PROJECT IPHIS\n{w}\"Human and Emotion\""
    play music "<volume 0.2>audio/whirr.wav" fadein 7.0
    scene bg lab at center2, AnimatedAberate, VHS:
        zoom 1.35
    show black:
        alpha 0.5
    with fade
    n "IPHIS laid flat on the table once more. This time, the harsh light focused on her cranium."
    n "It would come that I would eventually review her controller core again, since it is a vital key to the final step of this project."
    show ianthe bored at ianthe1, AnimatedAberate, VHS
    i "Iphis, shut your pain sensors off."
    p "...Understood."
    n "There isn't a visual indication of the sensors turning off, but I trust her confirmation."
    n "{i}For that matter, if she was human, I would've given her anesthesia, but that's besides the point."
    n "I opened a latch in her forehead using a small screwdriver. Making sure the cannula doesn't break and spill everywhere, I turn the connection off so that the blood through her brain rests."
    # controller core (which looks similar to the human brain but with machinery) is visible
    play sound "audio/error.wav"
    n "{color=#5ce1e6}{cps=100}<ERROR !! ALTERED STATE OF CONTROLLER CORE !! Report this bug to the database?>{/color}{/cps}" with hpunch
    n "It must be referring to the limbic and prefrontal bionics being swapped in."
    n "These error messages don't take place whenever I put in bionics in other parts of her body, but for some reason, they only show up in the controller core."
    play sound "audio/button.wav"
    n "I press the red button to not report the 'bug.'"
    hide ianthe
    play sound "audio/error.wav"
    n "{color=#5ce1e6}{cps=100}<THOUGHT PATTERNS IRREGULAR !!>{/cps}{/color}" with hpunch
    play sound "audio/error.wav"
    n "{color=#5ce1e6}{cps=100}<SYSTEM UNABLE TO PROCESS CORE DATABASE INFORMATION !!>{/cps}{/color}" with hpunch
    show ianthe bored at ianthe1, AnimatedAberate, VHS
    i "Huh?"
    show black:
        alpha 0.8
    play sound "audio/error.wav"
    hide ianthe
    n "{color=#5ce1e6}{cps=100}<UNABLE TO FIND CONTROLLER CORE CRITICAL POINTS>{/cps}{/color}"
    play sound "audio/selecterror.wav"
    n "{color=#5ce1e6}{cps=100}<SHUTTING DOWN MODEL TASK PROCESSES>{/cps}{/color}"

    #no log until end
    hide screen bubble
    show black with fade:
        alpha 1.0
    with Pause(4.0)
    hide black with Dissolve(1.0)

    n "I closed the hatch in her cranium."
    show ianthe scary at ianthe1, AnimatedAberate, VHS
    i "I think something…happened while I was taking a look at her controller core."
    i "The limbic and prefrontal bionics- its state reports were flooded with warnings that something had compromised her logic."
    i "I would have simply replaced those bionics again, but because the limbic and prefrontal have been so integrated into IPHIS's logic, then that means…"
    i scared "That means…"
    i "No."
    i "No.."
    i "No..."
    i "My life's work…"
    show black:
        alpha 0.8
    i "It's all gone."
    #vpunch maybe
    i "{cps=20}Urp…" with vpunch
    hide black with dissolve
    scene black with Dissolve(1.0)
    with Pause(5.0)
    # fade to black
    # transition back to scene
    scene cyan at AnimatedAberate, VHS with Dissolve(0.5)
    stop music fadeout 0.5
    n "When I opened my eyes, I was on the ground." 
    n "How unsatisfactory. The operating room could be brimming with unknown germs or diseases."
    i "...?"
    play music "audio/act 3 final mix.mp3" fadein 5.0
    scene cg pray at AnimatedAberate, VHS with Fade(1.0,1.0,1.0)
    pause
    n "Next to me was IPHIS, or now Iphis, clasping my dazed hand with hers together. She seems to be distressed."
    # show iphis sprite
    p "-od, why is it in me…?"
    p "An android to feel this way about a human... why?"
    p "Please..."
    p "Deactivate me, if you must."
    i "...Huh?"
    n "My strength at the very least lets me sit up straight, and turn to the side."
    scene bg lab at center2, AnimatedAberate, VHS:
        zoom 1.35
    show ianthe bored at ianthe1, AnimatedAberate, VHS
    show iphis neutral at center1, AnimatedAberate, VHS:
        zoom 0.56
    with Dissolve(1.0)
    n "A pile of throw up... something my stomach bionic hasn't prevented me from doing."
    p happy "You're awake!"
    i "I am."
    n "What do I do now...?"
    n "My life's work: PROJECT IPHIS. In the past I have gathered androids and replaced their parts with bionics."
    n "It was originally to allow for humans to become one with androids, take their capabilities and become perfect."
    n "Towards the end of this project, I would have altered IPHIS's controller core to correspond with my brain, effectively making me the first perfect human."
    n "After all, if our brains knew rational decisions like androids, then maybe the world wouldn't have turned out the way it did."
    n "However, PROJECT IPHIS had altered in a way I had not thought it would..."
    n "It seems that I have created a 'being' inside of an android. One that is capable of sentience and the same processes that an android carries."
    p speak "Is anything the matter, Dr. Ianthe?"
    p "Would you like me to clean the 'waste' for you?"
    show iphis neutral at center1, AnimatedAberate, VHS
    i "..."
    n scared "Why does this android, or being for that matter... care about me?"
    n "If she had become some sentient being, then she must've realized by now that what I had done to her is against the societal standard."
    n bored "Iphis, back with gloves and cleaning supplies, uses a sanitizing cloth to wipe the throw up at the side of me."
    n "She is diligent to leave no trace behind. The floor has been shinier than before I walked into the room."
    p determined "You can sit back, Dr. Ianthe." 
    p "After I have completed the sterilization of this area, I will tend to your illness."
    i "..."
    # fade to alpha black
    show black with Dissolve(0.5):
        alpha 0.6
    n "The places she scrubbed has a glassy look to them now." 
    n "Even the instruments and tools have been made to look brand new."
    n "It is strange, watching the girl you experimented on- clean up after you."
    hide black with Dissolve(0.5)
    # pause here 1 second
    # unfade
    n "I can't idly sit here and watch."
    n "I stood up and grabbed a solution bottle."
    p scared "Please rest Dr. Ianthe, you are ill."
    i neutral "I'm afraid I can't rest now. I have to do something to keep myself active here."
    p happy "...Understood."
    # transition black
    label clean2:
        #clean mechanic
        jump contAct3

label contAct3:
    hide ianthe
    hide iphis
    scene cg clean at AnimatedAberate, VHS with Fade(1.0,1.0,1.0)
    pause
    n "I sprayed some of the solution at the floor and began to wipe."
    n "As the surface reflection gets clearer and the stains disappear, a thought crept: "
    n "If I can get this place to be spotless, then maybe the rest of my 'failure' could be undone too."
    n "But then, I kept scrubbing. Somewhere along the smooth surfaces and chemicals wafting in the air, I thought \"Perhaps it wasn't a complete failure.\""
    n "Iphis has become a dual-bionic-android-human."
    n "Not in the way I had expected by design, but it was enough to start."


    p "Dr. Ianthe?"
    i "..."
    p "After we finish cleaning, can you inspect my cannula?"
    p "Because of... the events that transpired..."
    p "I think you would know to stabilize it."
    i "Fine."
    i "Just this once, okay?"

    scene black with Dissolve(3.0)
    nvl clear
    c "{b}END:{/b} PROJECT IPHIS"
    nn "{cps=45}\"cout << \"|| PROJECT IPHIS ||\" << ‘\n’ << \"log 42x\";{nw}{/cps}"
    "|| PROJECT IPHIS ||\nlog 42x"
    nn "{color=#5ce1e6}logFile << \"Everything is okay again.\";{/color}"
    hide text with Dissolve(1.5)

    c "{color=#FFFF00}Writers:{/color} Jaden Nguyen{w=0.1}\n\n{color=#FFFF00}Artists:{/color} Bao-Nhi Nguyen (CG Artist), \nAitana Navarrete (Sprite Artist){w=1.0}\n\n{color=#FFFF00}Music:{/color} Kiran Dinakaran{w=0.1}\n\n{color=#FFFF00}Programmers:{/color} Grace Seeberger, Jaden Nguyen{w=1.0}\n\n{color=#FFFF00}Project Manager:{/color} Jaden Nguyen{w=1.0}\n\nAll third party assets can be found in the\n doc listed in the game page description."
    c "Thank you for playing our android yuri game!! (o^_^)o"
    with Pixellate(1.5, 5.0)
    nvl clear

    return
    
