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

    "I closed the hatch in her cranium."
    "I think something…happened while I was taking a look at her controller core."
    "The limbic and prefrontal bionics- its state reports were flooded with warnings that ‘something had compromised her logic.’"
    "I would have simply replaced those bionics again, but because the humans’ logic had been so integrated into IPHIS, then that means…"
    "That means…"
    "My life’s work…"
    #vpunch maybe
    "{cps=20}Urk…"
    # fade to black
    # transition back to scene
    "When I opened my eyes, I was on the ground. This is unsatisfactory, since the operating room could be brimming with unknown germs or diseases."
    "Next to me was IPHIS, or now Iphis, clasping my dazed hand with hers together. She seems to be distressed."
    # show iphis sprite
    p "-od, why is it in me…?"
    p "Deactivate me, if you must."
    i "...Huh?"
    "My strength at the very least lets me sit up straight, and turn to the side. A pile of throw up, something my stomach bionic hasn't prevented me from doing."
    p "You’re awake!"
    i "I am."
    "My life’s work: PROJECT IPHIS. In the past I have gathered androids and replaced their parts with bionics."
    "It was originally to allow for humans to become one with androids, take their capabilities and become perfect."
    "Towards the end of this project, I would have put my brain into Iphis’s body, effectively making me the first perfect human."
    "However, PROJECT IPHIS had altered in a way I had not thought it would."
    "It seems that I have created a ‘human’ inside of an android. One that is capable of sentience and the same processes that an android carries."
    p "Is anything the matter, Dr. Ianthe?"
    p "Would you like me to clean the ‘waste’ for you?"
    i "..."
    "Why does this android, or human for that matter… care about me?"
    "If she had become human, she would have realized by now that what I had done to her is against the societal standard."
    "Iphis, back with gloves and cleaning supplies, uses a sanitizing cloth to wipe the throw up at the side of me."
    "She is diligent to leave no trace behind. The floor has been shinier than before I walked into the room."
    p "You can sit back, Dr. Ianthe. After I have completed the sterilization of this area, I will tend to your illness."
    i "..."
    # fade to alpha black
    "The places she scrubbed had a glassy look to them now. Even the instruments and tools have been made to look brand new."
    "It is strange, watching the girl you experimented on- clean up after you."
    # pause here 1 second
    # unfade
    "I can’t idly sit here and watch."
    "I stood up and grabbed a solution bottle."
    p "Please rest Dr. Ianthe, you are ill."
    i "I’m afraid I can’t rest now. I have to do something to keep myself active here."
    p "...Understood."
    # transition black
    "I sprayed some of the solution at the operation table and began to wipe."
    "As the surface reflection gets clearer and the stains disappear, a thought crept: "
    "If I can get this place to be spotless, then maybe the rest of my ‘failure’ could be undone too."
    "But then, I kept scrubbing. Somewhere along the smooth surfaces and chemicals wafting in the air, I thought \"Perhaps it wasn’t a complete failure.\""
    "Iphis has become a dual-bionic-android-human."
    "Not in the way I had expected by design, but it was enough to start."

    "{cps=45}\"cout << \"|| PROJECT IPHIS ||\" << ‘\n’ << \"log 42x\";{nw}{/cps}"
    "|| PROJECT IPHIS ||\nlog 42x"
    "logFile << \"I don’t know how long I can keep doing this.\";"

    label clean2:
        #clean mechanic
        jump contAct3

label contAct3:
