# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character(None, image = "iphis", what_color="#5ce1e6", kind = bubble, retain = True)
define i = Character(None, image = "ianthe", what_color="#FFFFFF", kind = bubble, retain = True)
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
    play music "audio/act 1 draft.mp3"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show iphis neutral at center1, AnimatedAberate, VHS:
        zoom 0.56

    p "{cps=90}Processors are stable."
    p "{cps=90}Memory used is at 40\%."
    p "{cps=90}Cooling systems are stable."
    p "{cps=90}All components are stable."
    show ianthe smile at ianthe1, AnimatedAberate, VHS:
        zoom 0.9

    n "My fingers dig through the wires to find the empty sector. Once I’ve located the area, I grab the parallel bionic and place it in the null."
    p "{cps=45}...It is not within my bandwidth to answer that question."


    # This ends the game.

    return
