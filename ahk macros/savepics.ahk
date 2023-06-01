#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; Hotkey for the script is F1
F1::
{
    ; Right click
    Send {RButton}
    Sleep, 100  ; 

    ; The 'v' key typically corresponds to the 'Save Image As' option in the right click context menu
    Send v
    Sleep, 1000  ; 
    ; Save (usually Enter in the 'Save Image As' dialog box)
    Send {Enter}
    Sleep, 10  ; 
}
return
