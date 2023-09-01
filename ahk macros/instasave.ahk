#Persistent
CoordMode, Pixel, Screen

; Activate URL dl
ImageX := 601
ImageY := 383

; DL for square pic
TargetX := 412
TargetY := 260


; DL for 3:4 pic
AdditionalX := 510
AdditionalY := 163

; Replace these coordinates with the next point where you want to click
NextX := 1872
NextY := 570


; Function to simulate a left click at specified coordinates
LeftClick(x, y) {
    MouseMove, %x%, %y%
    Sleep, 1
    Click
}

; Main hotkey to trigger the script
F1::
    ; Simulate left click on the image
    LeftClick(ImageX, ImageY)
    
    ; Wait for a brief moment
    Sleep, 1
    
    ; Simulate left click on the specific target point
    LeftClick(TargetX, TargetY)
    
    ; Wait for another brief moment
    Sleep, 1
    
    ; Simulate left click on the additional point
    LeftClick(AdditionalX, AdditionalY)
    
    ; Wait for another brief moment
    Sleep, 1
    
    ; Simulate left click on the next point
    LeftClick(NextX, NextY)
return