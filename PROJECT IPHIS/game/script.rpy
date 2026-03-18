# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character(None, image = "iphis", what_color="#5ce1e6", kind = bubble, retain = True)
define i = Character(None, image = "ianthe", what_color="#FFFFFF", kind = bubble, retain = True)
# n is to distinguish how one bubble looks like the standard adv dialogue box
define n = Character(None, image = "ianthe", what_color="#FFFFFF", kind = bubble, retain = True)

default preferences.text_cps = 34


image white = "#FFFFFF"

#image side ianthe smile:
    #"images/ianthe smile.png"
    #zoom 0.5

transform center1:
    xalign 0.5
    yalign 1.5

transform center2:
    xalign 0.5
    yalign 1.0

transform ianthe1:
    xalign 0.17
    yalign 0.9

transform textdissolve:
    alpha 0 #start transparent
    ease 0.6 alpha 1 #go to full opacity

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    with Pixellate(1.5, 5.0)
    scene bg lab at center2, AnimatedAberate, VHS:
        zoom 1.35
    ### ACT 1 ##

    "{cps=45}\"cout << \"|| PROJECT IPHIS ||\" << ‘\n' << \"log 35x\";{nw}{/cps}"
    "|| PROJECT IPHIS ||\nlog 35x"
    "logFile << \"IPHIS's #2aorta has successfully been replaced with a parallel aortic valve bionic.\";"
    
    jump act1


    # This ends the game.
