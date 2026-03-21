label act3:
# act 3 narrative here

label clean2:
    scene bg operating floor

    default FirstFloorSplatter = False
    default SecondFloorSplatter = False
    default ThirdFloorSplatter = False
    default FourthFloorSplatter = False

    if FirstSplatter and SecondSplatter and ThirdFloorSplatter and FourthFloorSplatter:
        jump contAct3
    else:
        call screen clean3_screen

screen clean3_screen:
    if not FirstFloorSplatter:
        imagebutton:
            xpos 0.175
            ypos 0.575
            xanchor 0.5
            yanchor 0.5
            idle "Table_Splatter_1.png"
            hover "Table_Splatter_1.png"
            action [SetVariable("FirstSplatter", True), Jump("clean1")]
    if not SecondFloorSplatter:
        imagebutton:
            xpos 0.245
            ypos 0.63
            xanchor 0.5
            yanchor 0.5
            idle "Table_Splatter_2.png"
            hover "Table_Splatter_2.png"
            action [SetVariable("SecondSplatter", True), Jump("clean1")]
    if not ThirdFloorSplatter:
        imagebutton:
            xpos 0.175
            ypos 0.575
            xanchor 0.5
            yanchor 0.5
            idle "Table_Splatter_1.png"
            hover "Table_Splatter_1.png"
            action [SetVariable("FirstSplatter", True), Jump("clean1")]
    if not FourthFloorSplatter:
        imagebutton:
            xpos 0.245
            ypos 0.63
            xanchor 0.5
            yanchor 0.5
            idle "Table_Splatter_2.png"
            hover "Table_Splatter_2.png"
            action [SetVariable("SecondSplatter", True), Jump("clean1")]

label contAct3:
