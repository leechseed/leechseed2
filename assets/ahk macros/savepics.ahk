; Hotkey for the script is F1
F1::
    ; Right click
    Send, {RButton}
    Sleep, 50  ; Reduced to speed up the right-click action

    ; The 'v' key typically corresponds to the 'Save Image As' option in the right click context menu
    Send, v
    Sleep, 500  ; Reduced to speed up the action, adjust if necessary

    ; Save (usually Enter in the 'Save Image As' dialog box)
    Send, {Enter}
    Sleep, 10  ; Kept short for quick repetition if needed
return
