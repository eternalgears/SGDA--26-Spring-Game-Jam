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
    play music "<volume 0.2>audio/whirr.wav" fadein 7.0
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
    scene black with Dissolve(1.0)
    n "Click to continue. >>"
    pause
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
    stop music fadeout 1.0
    # transition to operating table
    scene black with Dissolve(1.0)
    # added more narrative here
    hide screen bubble with Dissolve(1.0)
    with Pause(0.5)
    n "Click to continue. >>"
    pause
    nvl clear
    c "When I used to be a surgeon for humans, people showered me with praise."
    c "I liked it. {w}\n\nUnlike now, where everything is bionic \nand artificial, I knew words could be genuine."
    c "It's been long since I've felt the kindness of a human."
    c "I wish I could go back to simplier times."

    show iphis happy at center1, AnimatedAberate, VHS:
        zoom 0.56
    p "Good morning, Dr. Ianthe."
    play music "<volume 5>audio/room noise.mp3" fadein 0.5
    scene bg home at center2, AnimatedAberate, VHS:
        zoom 1.2
    with Dissolve(1.0)
    show ianthe bored at ianthe1, AnimatedAberate, VHS
    show iphis happy at center1, AnimatedAberate, VHS:
        zoom 0.56
    with Dissolve(0.5)
    n "Unbeknownst to me, IPHIS had been waiting for me to wake up."
    i "Hmmm? Ahh... {nw}"
    show ianthe neutral at ianthe1, AnimatedAberate, VHS
    i "Hmmm? Ahh... {fast}It really is early~"
    i smile "What are you doing here, Iphis? It's unlike you."
    p determined "...You appear to not have sufficent sleep."
    p happy "Shall I prepare you a caffinated drink?"
    n bored "Her thoughtful words, politeness, gentle smile..."
    n "I despise people that perceive me like I am something that needs to be taken care of."
    i neutral "Sigh..."
    i smile "Uncharacteristically caring of you, hmmm?"
    i neutral "How about you keep quiet while I take care of sorting out the stock?"
    p scared "I..."
    p speak"..Dr. Ianthe, if I may."
    p determined "Though I am merely an antique android, I believe I deserve to be treated with respect."
    p neutral "There will be no difficulties in our work if there isn't tension between us."
    i scary "..."
    i "You.."
    play sound "audio/error.wav"
    play music "<volume 0.8>act 2 demo.mp3" fadein 1.0
    p scared "{cps=90}Urk...!{/cps}" with vpunch
    n "I tugged on her cannula wire."
    n "A little bit of blood seeps out, but not too much to where she could be put in critical condition."
    n "Seeing her squirm helplessly over a simple tug, it makes me feel like I'm on top of the world."
    i smile "I've always adored you when you were obedient."
    play sound "audio/error.wav"
    p "Eeek!" with vpunch
    n "I pulled on the cannula a little harshly at that statement."
    i neutral "We have an experiment coming up soon."
    i smile "Be good for me, okay?"
    with Pause(0.3)
    stop music fadeout 1.0
    scene black with Fade(1.5, 1.0, 1.5)
    hide screen bubble
    with Pause(0.5)
    n "Click to continue. >>"
    pause
    jump act3
