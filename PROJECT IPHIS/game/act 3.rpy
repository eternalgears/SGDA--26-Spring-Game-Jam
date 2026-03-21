label act3:
# act 3 narrative here

label clean2:
    scene bg operating floor

    $ default_mouse = "towel"

    default FirstFloorSplatter = False
    default SecondFloorSplatter = False
    default ThirdFloorSplatter = False
    default FourthFloorSplatter = False

    if FirstSplatter and SecondSplatter and ThirdFloorSplatter and FourthFloorSplatter:
        jump contAct3
    else:
        call screen clean2_screen

screen clean2_screen:
    if not FirstFloorSplatter:
        imagebutton:
            xpos 0.4653
            ypos 0.65
            xanchor 0.5
            yanchor 0.5
            idle "Floor_Splatter_1.png"
            hover "Floor_Splatter_1.png"
            action [SetVariable("FirstFloorSplatter", True), Play("sound", "audio/btn_confirm.wav"), Jump("clean2")]
    if not SecondFloorSplatter:
        imagebutton:
            xpos 0.63
            ypos 0.282
            xanchor 0.5
            yanchor 0.5
            idle "Floor_Splatter_2.png"
            hover "Floor_Splatter_2.png"
            action [SetVariable("SecondFloorSplatter", True), Play("sound", "audio/btn_confirm.wav"), Jump("clean2")]
    if not ThirdFloorSplatter:
        imagebutton:
            xpos 0.165
            ypos 0.78
            xanchor 0.5
            yanchor 0.5
            idle "Floor_Splatter_3.png"
            hover "Floor_Splatter_3.png"
            action [SetVariable("ThirdFloorSplatter", True), Play("sound", "audio/btn_confirm.wav"), Jump("clean2")]
    if not FourthFloorSplatter:
        imagebutton:
            xpos 0.81
            ypos 0.655
            xanchor 0.5
            yanchor 0.5
            idle "Floor_Splatter_4.png"
            hover "Floor_Splatter_4.png"
            action [SetVariable("FourthFloorSplatter", True), Play("sound", "audio/btn_confirm.wav"), Jump("clean2")]

label contAct3:
    $ default_mouse = "arrow"
    stop sound
    return