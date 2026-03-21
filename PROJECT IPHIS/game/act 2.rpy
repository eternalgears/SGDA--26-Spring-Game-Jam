label act2:
    nvl clear
    $ renpy.music.set_volume(1.0, 0.0, channel='music')
    c "{b}ACT 2:{/b} PROJECT IPHIS\n{w}\"Doctor and Patient\""
    scene bg clean2 at center2, AnimatedAberate, VHS:
        zoom 1.2
    ## ACT 2 ##
    #also black screen
    nn "{cps=45}\"cout << \"|| PROJECT IPHIS ||\" << ‘\n' << \"log 41x\";{nw}{/cps}"
    "|| PROJECT IPHIS ||\nlog 41x"
    nn "{color=#5ce1e6}logFile << \"I don't know how long I can keep doing this.\";{/color}"
    play sound "audio/error.wav"
    c "{color=#5ce1e6}IPHIS{w}\n\n2030 nurse model developed to assist high-need patients.{w}\nExported only to the best and wealthiest of hospitals.{/color}"
    # "{cps=100}<I believe that in another life, we were adorned by silk robes and lived comfortably in each other's arms.>"

    # clinic bg transition
    # show iphis sprite and ianthe sprite
    play music "<volume 0.1>audio/whirr.wav" fadein 7.0
    scene bg clinic at AnimatedAberate, VHS:
        zoom 1.4
    show black:
        alpha 0.3
    with Fade(1.5, 1.0, 1.5)
    n "The whirring of the vent seems to be inescapable no matter what part of the building I'm in."
    play sound "audio/type.wav"
    n "I'm typing all of my findings from yesterday's experiment into a separate log file." 
    n "The milky tap sounds of the keys block out the grating noise, so I make an effort to type faster."
    show iphis speak at center1, AnimatedAberate, VHS:
        zoom 0.56
    stop sound
    stop music
    show black:
        alpha 0.8
    p "Dr. Ianthe?"
    # v punch?
    play music "audio/act 2 demo.mp3"
    with vpunch
    show black:
        alpha 0.3
    show iphis neutral at center1, AnimatedAberate, VHS:
        zoom 0.56
    n "Her soft, melodic-like voice made me jolt in my seat." 
    n "Ahh... How indignified of me. I straighten myself up and look her way."
    show ianthe smile at ianthe1, AnimatedAberate, VHS
    i "Greetings Iphis! Rare of you to address me first."
    p determined "Indubitably so."
    p speak "We are 10 minutes behind your schedule. I should've received my evaluation around then."
    show iphis neutral at center1, AnimatedAberate, VHS:
        zoom 0.56
    i neutral "Hehe, you seem to know everything about me."
    n bored "It is true that plans are progressing far slower than intended. By now, IPHIS should've been fully enhanced from her previous capabilities."
    n neutral "I would have presented her to be the first dual-bionic-android-human to the grand stage. Advertised as \"everything a human would want to be perfect.\""
    n "However, she is still full of flaws. There are multiple error warnings each time I open the controller core, blood leaks, and her...persistence."
    n smile "These are things I can fix. The quicker I get them over with, the quicker I can reach my goal."
    p speak "Is there something wrong, Dr. Ianthe?"
    i neutral "Of course not. Thank you for your concern, Iphis."
    i "Shall we ‘proceed' the check up, hmm?"
    p neutral "Yes."
    n bored "I grab my clipboard and prepare the questions."
    i neutral "Do you believe you have done your tasks in an efficient manner?"
    p speak "Yes."
    show iphis neutral at center1, AnimatedAberate, VHS:
        zoom 0.56
    i smile "Are there any popups that occur in your system?"
    p determined "No."
    show iphis neutral at center1, AnimatedAberate, VHS:
        zoom 0.56
    i neutral "Have you ever questioned the role you play in our society?"
    p determined "Perhaps, but I only compute further possibilities that serve humans like you."
    i bored "The old Iphis would have said no to this question, if you are aware."
    p happy "...I only do what is told of me. And if I can do more, I will."
    i neutral "Very well."
    i "Has your controller core experienced changes in its logic?"
    p neutral "I do not believe so." 
    i scary "You do not 'believe'?"
    p speak "Precisely."
    show iphis neutral at center1, AnimatedAberate, VHS:
        zoom 0.56
    n bored "Android models, especially older models such as IPHIS, typically aren't capable of metacognition."
    n "The fact that she is responding differently to my questions may be a sign of her sentience."
    n scary "It is an inevitable step towards a portion of dual humanity, but for some reason, her lost loyalty pricks at my heart."
    n "Where was her composure?" 
    n "Her unwaivering self?"
    n bored "No. I can't let my feelings get the better of me."
    i smile "I will end it here. Thank you, Iphis."
    i neutral "You may head back to your station until I call you later today."
    hide screen bubble
    hide ianthe
    hide iphis with Dissolve(1.0)
    with Pause(1.0)
    # transition to black
    
    scene bg home at center2, AnimatedAberate, VHS:
        zoom 1.2
    with Fade(1.5, 1.0, 1.5)
    $ renpy.music.set_volume(0.17, 0.0, channel='music')
    show ianthe bored at ianthe1, AnimatedAberate, VHS
    n "The uncertainties she has said, such as \"believe\" or \"precisely,\" are indicative of what humans would say."
    n "It is strange because bionic humans, in spite of enhanced tissue regeneration and capabilities, still do not have the specialized synapses that androids do."
    i scary "...And despite that, she's been spouting things as if she's a person."
    n "Androids are fully equipped to adapt to human logic. If the rules of the environment change, then so must the android's role."
    n "It is not foolish to believe that her deviancy may come soon."
    n bored "Because of this, I need to keep her sentience low for the sake of this project. She still has tasks to do, after all."

    # transition to operating table

    # added more narrative here
    

    "IPHIS laid flat on the table once more. This time, the harsh light focused on her cranium."
    "It would come that I would eventually review her controller core again, since it is a vital key to the final step of this project."
    i "Iphis, shut your pain sensors off."
    p "...Understood."
    "There isn't a visual indication of the sensors turning off, but I trust her confirmation. {i}For that matter, if she was human, I would've given her anesthesia, but that's besides the point.{/i}"
    "I opened a latch in her forehead using a small screwdriver. Making sure the cannula doesn't break and spill everywhere, I turn the connection off so that the blood through her brain rests."
    # controller core (which looks similar to the human brain but with machinery) is visible
    "{cps=100}<ERROR !! ALTERED STATE OF CONTROLLER CORE !! Report this bug to the database?>"
    "It must be referring to the bionics being swapped in. These error messages don't take place whenever I put in bionics in other parts of her body, but for some reason, they only show up in the controller core."
    "I press the red button to not report the ‘bug.'"
