# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# VOICE BLEEPS
init python:
    # voice bleep audio channel
    renpy.music.register_channel("bleeps", mixer= "sfx", loop=True)

    # function for playing voice bleeps          
    def voice_play(on=False, char=1):
        if on:
            if char==1:
                renpy.sound.play("audio/ianthe.wav", channel="bleeps", loop=True)
            if char==2:
                renpy.sound.play("audio/iphis.wav", channel="bleeps", loop=True)
            if char==3:
                renpy.sound.play("audio/type.wav", channel="bleeps", loop=True)
        else:
            renpy.sound.stop(channel="bleeps")

    def ianthe_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show" or event == "begin":
            voice_play(True, 1)
        elif event == "slow_done" or event == "end":
            voice_play(False, 1)

    def iphis_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            #renpy.sound.play("audio/kuma.wav", loop=True)
            voice_play(True, 2)
        elif event == "slow_done" or event == "end":
            voice_play(False, 2)
    
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show" or event == "begin":
            voice_play(True, 3)
        elif event == "slow_done" or event == "end":
            voice_play(False, 3)



# CHARACTERS
define p = Character(None, image = "iphis", what_color="#5ce1e6", kind = bubble, retain = True, callback = iphis_sound)
define i = Character(None, image = "ianthe", what_color="#FFFFFF", kind = bubble, retain = True, callback = ianthe_sound)
# n is to distinguish how one bubble looks like the standard adv dialogue box
define n = Character(None, image = "ianthe", what_color="#FFFFFF", kind = bubble, retain = True)
# typing in the logs
define nn = Character(None, callback = type_sound)

# center text
define c = Character(None,
    kind=nvl,
    callback = type_sound,
    window_background=None,
    what_style="centered_text",
    what_color="#fff",
    who_outlines=[ (2, "#000000") ],
    what_outlines=[ (2, "#000000") ],
    window_style="centered_window")

# defaults
default preferences.text_cps = 34


# image definitions
image white = "#FFFFFF"
image black = "#000000"
image cyan = "#96fbff"

#image side ianthe smile:
    #"images/ianthe smile.png"
    #zoom 0.5

# TRANSFORMS
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
    scene black
    ### ACT 1 ##
    c "{b}ACT 1:{/b} PROJECT IPHIS\n{w}\"Bionic and Organ.\""
    scene bg clean at AnimatedAberate, VHS:
        zoom 1.2
    nn "{cps=45}\"cout << \"|| PROJECT IPHIS ||\" << ‘\n' << \"log 35x\";{nw}{/cps}"
    "{cps=100}|| PROJECT IPHIS ||\nlog 35x{/cps}"
    nn "{color=#5ce1e6}logFile << \"IPHIS's #2aorta has successfully been replaced with a parallel aortic valve bionic.\";{/color}"
    
    jump act1


    # This ends the game.
