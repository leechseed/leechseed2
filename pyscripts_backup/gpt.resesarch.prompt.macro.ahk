#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

NumpadAdd::
ClipSaved := ClipboardAll
Clipboard := "Greetings ChatGPT. I require summarization of text I will paste into the dialogue box. The length of these excerpts will be at maximum 1000 words. The length and level of detail of a summary can vary depending on the purpose and context, but in general, a good summary should be concise, accurate, and provide a clear understanding of the main points. I need great summaries. Please do not use any introductory phrases. Sentences that begin with 'this excerpt', 'in conclusion', are STRICTLY PROHIBITED. Do not use introductory phrases. Do not use transitional phrases. Do not use referential phrases. DO NOT use the words, 'firstly,' 'secondly,' and, 'overall.' Please take a tone of scholarly academic prose. Above all, please prioritize clear understanding and accuracy over conciseness or reduction of length. do not use the words additionally and overall please do not number your points. Please acknowledge that you understand by responding with, 'uwu I understand sempai.'"
Send ^v
Sleep, 50
Send {Enter}
Clipboard := ClipSaved
return