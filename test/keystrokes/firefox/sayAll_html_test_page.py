# -*- coding: utf-8 -*-
#!/usr/bin/python

"""Test of sayAll output on a page with various object types in Firefox."""

from macaroon.playback import *
import utils

sequence = MacroSequence()

########################################################################
# We wait for the focus to be on a blank Firefox window.
#
sequence.append(WaitForWindowActivate(utils.firefoxFrameNames, None))

########################################################################
# Load the local "html page" test case.
#
sequence.append(KeyComboAction("<Control>l"))
sequence.append(WaitForFocus(acc_role=pyatspi.ROLE_ENTRY))

sequence.append(TypeAction(utils.htmlURLPrefix + "htmlpage.html"))
sequence.append(KeyComboAction("Return"))

sequence.append(WaitForDocLoad())
sequence.append(WaitForFocus(acc_role=pyatspi.ROLE_DOCUMENT_FRAME))

########################################################################
# Press Control+Home to move to the top.
#
sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("<Control>Home"))
sequence.append(utils.AssertPresentationAction(
    "Top of file",
    ["BRAILLE LINE:  'Test Formats'",
     "     VISIBLE:  'Test Formats', cursor=1",
     "SPEECH OUTPUT: 'Test Formats link ",
     "'"]))

########################################################################
# SayAll to the End.
#
sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_Add"))
sequence.append(utils.AssertPresentationAction(
    "KP_Add to do a SayAll",
    ["SPEECH OUTPUT: 'Test Formats link'",
     "SPEECH OUTPUT: '",
     " Alignment Text link ",
     " Indent Text link ",
     " HTML Forms and Widgets link ",
     " List link ",
     " Tag link ",
     " Table link ",
     "",
     " Test Cases (from bugs) link ",
     "",
     " separator link Text Formats",
     "",
     "This sentence is bold. This sentence is italicized. This sentence is underlined. This sentence uses strikethrough. This sentence has the words sentence in superscript. This sentence has the word sentence in subscript. This is a Heading 1. heading level 1 This is a Heading 2. heading level 2 This is a Heading 3. heading level 3 This is a Heading 4. heading level 4 This is a Heading 5. heading level 5 This is a Heading 6. heading level 6 This sentence is in Arial font. 1This sentence is in Comic Sans MSl font. ",
     "2This sentence is in Courier New Font. ",
     "3This sentence is in Garamondl font. ",
     "4This sentence is in Impact font. ",
     "5This sentence is in Lucida Console font. ",
     "6This sentence is in Sydnie font. ",
     "7This sentence is in Tahoma font. ",
     "8This sentence is in Times New Roman font. 9This sentence is in font size 18 on a PC or font size +2. ",
     "aThis sentence is in font size 10 on a PC. bThis sentence is green. cThis sentence is in address format. dThis sentence is blinking. eThis sentence contains preformatted plain text.",
     "",
     " separator link Alignment",
     " From Shakespeare's Hamlet heading level 3 I have of late but",
     "wherefore I know not lost all my mirth,",
     "forgone all custom of exercises;",
     "and indeed, it goes so heavily with",
     "my disposition that this goodly frame,",
     "the earth, seems to me a sterile promontory;",
     "this most excellent canopy, the air, look you,",
     "this brave o'erhanging firmament,",
     "this majestical roof fretted with golden fire",
     "why, it appeareth no other thing to me than a foul",
     "and pestilent congregation of vapours.",
     "What a piece of work is a man!",
     "how noble in reason! how infinite in faculties!",
     "in form and moving how express and admirable!",
     "in action how like an angel!",
     "in apprehension how like a god!",
     "the beauty of the world, the paragon of animals! I have of late but",
     "wherefore I know not lost all my mirth,",
     "forgone all custom of exercises;",
     "and indeed, it goes so heavily with",
     "my disposition that this goodly frame,",
     "the earth, seems to me a sterile promontory;",
     "this most excellent canopy, the air, look you,",
     "this brave o'erhanging firmament,",
     "this majestical roof fretted with golden fire",
     "why, it appeareth no other thing to me than a foul",
     "and pestilent congregation of vapours.",
     "What a piece of work is a man!",
     "how noble in reason! how infinite in faculties!",
     "in form and moving how express and admirable!",
     "in action how like an angel!",
     "in apprehension how like a god!",
     "the beauty of the world, the paragon of animals! I have of late but",
     "wherefore I know not lost all my mirth,",
     "forgone all custom of exercises;",
     "and indeed, it goes so heavily with",
     "my disposition that this goodly frame,",
     "the earth, seems to me a sterile promontory;",
     "this most excellent canopy, the air, look you,",
     "this brave o'erhanging firmament,",
     "this majestical roof fretted with golden fire",
     "why, it appeareth no other thing to me than a foul",
     "and pestilent congregation of vapours.",
     "What a piece of work is a man!",
     "how noble in reason! how infinite in faculties!",
     "in form and moving how express and admirable!",
     "in action how like an angel!",
     "in apprehension how like a god!",
     "the beauty of the world, the paragon of animals!",
     " separator link Indent",
     "    by Wislawa Szymborska - 1972 I am a tranquilizer. ",
     "I am effective at home, ",
     "I work well at the office, ",
     "I take exams, ",
     "I appear in court, ",
     "I carefully mend broken crockery - ",
     "all you need do is take me, ",
     "dissolve me under the tongue, ",
     "all you need do is swallow me, ",
     "just wash me down with water. I know how to cope with misfortune, ",
     "how to endure bad news, ",
     "take the edge of injustice, ",
     "make up for the absence of God, ",
     "help pick out your widow's weeds. ",
     "What are you waiting for - ",
     "have faith in chemistry's compassion. You're still a young man/woman, ",
     "you really should settle down somehow. ",
     "Who said ",
     "life must be lived courageously? Hand your abyss over to me - ",
     "I will line it up with soft sleep, ",
     "you'll be grateful for ",
     "the four-footed landing. Sell me your soul. ",
     "There's no other buyer likely to turn up. There's no other devil left.",
     " separator link HTML Form and Widgets",
     "",
     "Textfield : Enter your Name:  text text field using default type=text 1. Enter your Address:  text text field using SIZE and MAXLENGTH 2. Enter your City:  text 3. Enter your State:  text 4. Enter your Country:  text US text field using value 5. Enter your Zip:  text 6. What happens when a fixed-width font(the default) is used for a one-byte text input area, let's try it.. Enter one character:  text  ",
     " separator  CheckBox: What are your favorite pets? heading level 2 check box not checked bird ",
     " check box not checked fish ",
     " check box not checked wild animal ",
     " separator ",
     "Radio Buttons: Would type of wine do you like? heading level 2 selected radio button cabernet sauvignon ",
     " not selected radio button merlot ",
     " not selected radio button nebbiolo ",
     " not selected radio button pinot noir ",
     " not selected radio button don't drink wine ",
     " separator  Password Field: Who are you? heading level 2 Enter your Password: password separator Submit Buttons: heading level 2 Submit Query button submit button using default \"VALUE\" Click Here button submit button using assigned \"VALUE\", no \"NAME\" Send Out button submit button using assigned \"NAME\" & \"VALUE\" separator Form Multiline Text Areas: heading level 2 Enter any Comments you have about this Web page following: text multiline text area with default WRAP=NO WRAP text multiline text area with WRAP=SOFT text multiline text area with WRAP=HARD separator Pulldown menus: heading level 2 Regular Pizza order? Three Cheeses combo box  selection without \"multiple\" act as a pull-down menu Gourmet Pizza order? Vegetarian Gourmet multi-select List with 7 items  selection with \"multiple\" act as a scrolling list ",
     "and has a pre-selected \"option\" Extra Pizza Add-On order? mushrooms List with 6 items  selection with size=3 with/without \"multiple\" act as a scrolling list ",
     "and has a pre-selected \"option\" Drink order? diet coke combo box separator ",
     " separator link List",
     "",
     "Welcome to a list of lists ",
     "Lists are not only fun to make, they are fun to use. They help us: 1. remember what the heck we are doing each day 2. arrange long and arbitrary lines of text into ordered lists that are pleasing to the eye and suggest some sense of priority, even if it is artificial 3. look really cool when we carry them around on yellow Post-Its tm. 4. and that other thing I keep forgetting. Your ordered lists can start at a strange number, like VI. And use roman numerals, g. You might try using letters as well, H. Maybe you prefer Big Letters, ix. or small roman numerals • But discs belong to unordered lists 50. Though you can set the value in a list item! Unordered list :   • listing item   • first sublevel   • look for the bullet on   • each sublevel • they should all be different, except here. • second sublevel • or you can specify a square • if your TYPE is circle • or even a disc • Franz Liszt • was a composer who was not square • would have liked the Who • feeling listless. TYPE=CIRCLE • blah, blah, blah (square) • whine, whine, whine(disc) ",
     " separator link Tag",
     "Bold Tag with other Physical Character Style Tags. Bold Tag with : • Big : This line has both Bold tag and the Big tag. (outside the Bold tag) • Blink : This line has both the Bold tag and the Blink tag. (outside the Bold tag) • Font : This line has the Bold tag and the Font face tag set to \"Courier\" ,color=darkgreen and size =-1.(outside the Bold tag) • Italics : Text that is both Bold and Italic. (outside the Bold tag) • Small : This line has both Bold tag and the Small tag; hence I should be smaller !! (outside the Bold tag) • Strikethrough : I should be Bold and Strikethroughed. (outside the Bold tag) • Subscript : I'm bold and I have asubscript • Superscript : I'm bold too and I have a superscript • Typewriter : This line has the Bold tag and the Typewriter tag. (outside the Bold tag) • Underline : I'm bold and I should be underlined. (outside the Bold tag) separator  Bold Tag with Content Character Style Tags Bold Tag with : • Cite : The part after the exclamation is in Cite Tags !!!! (Chitra, 1996) (outside the Bold tag) • Code : #include \"main.h\"(outside the Bold tag) • Definition : The word &ltCharacter Styles> are surrounded by the definition tag. • Emphasis : I am using the Bold and the Emphasis tag. (outside the Bold tag) • Keyboard : Inside bold and keyboard tags. (outside the Bold tag) • Sample : Well !! I'm using the bold and the sample Tag. (outside the Bold tag) • Strong : I have the Bold and the Strong tags around me !!(outside the Bold tag) • Variable : you_tell_me. Yup !! the Bold and Variable tag. (outside the Bold tag) separator Superscript Tag with other Physical Character Style Tags: Superscript Tag with : • Bold : This line has both Bold tag and the Superscript tag. (outside the Superscript tag) • Big : This line has both Big tag andI'm the Superscript. (outside the Superscript tag) • Blink : This line has both the Blink tag and Superscriptt tag. (outside the Superscript tag) • Font : This line has the Superscript tag and the Font face tag set to \"Courier\" ,color=darkgreen and size =-1.(outside the Superscript tag) • Italics : Text that is Italic and has a Superscript.(outside the Superscript tag) • Small : This line has both Superscript tag and the Small tag; hence I should be smaller !!(outside the Superscript tag) • Strikethrough : I should have a Superscript and be Strikethroughed.(outside the Superscript tag) • Subscript : I have a subscript and it has a Superscript • Superscript : I have a superscript and it again has a SUPERSCRIPT • Typewriter : This line has the Superscript tag and the Typewriter tag. (outside the Superscript tag) • Underline : I'm Superscript and I should be underlined. (outside the Superscript tag) separator Superscript Tag with Content Character Style Tags Superscript Tag with : • Cite : The part after the exclamation is in Cite Tags and is a Sup !!!! (Chitra, 1996) (outside the Superscript tag) • Code : I have a Superscript #include \"main.h\"(outside the Superscript tag) • Definition : The word &ltCharacter Styles> are surrounded by the definition tag and is a Sup. • Emphasis : I am using the Superscript and the Emphasis tag. (outside the Superscript tag) • Keyboard : I have the Superscript and keyboard tags. (outside the Superscript tag) • Sample : Well !! I'm using the Superscript and the sample Tag. (outside the Superscript tag) • Strong : I have the Superscript and the Strong tags !!(outside the Superscript tag) • Variable : you_tell_me. Yup !! the Superscript and Variable tag. (outside the Superscript tag) separator link Table",
     "",
     " 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38 '",
     "SPEECH OUTPUT: 'A'",
     "SPEECH OUTPUT: 'a a b b c c d d hello there'",
     "SPEECH OUTPUT: 'D G H I A'",
     "SPEECH OUTPUT: 'a b c d'",
     "SPEECH OUTPUT: 'C D A'",
     "SPEECH OUTPUT: 'a b c d'",
     "SPEECH OUTPUT: 'C D'",
     "SPEECH OUTPUT: ' separator Table showing text flow: heading level 4 separator This is text placed above the table and Table Title caption table head table head table head cell 1 cell 2 cell 3 continuing below the table!!! ",
     " separator Table Border Tests separator Table showing the default table BORDER=1 :   caption table head table head table head cell 1 cell 2 cell 3 separator ",
     "Tables showing different border values: ",
     "  Table with BORDER=1 caption table head table head table head cell 1 cell 2 cell 3 Table with BORDER=2 caption table head table head table head cell 1 cell 2 cell 3 Table with BORDER=3 caption table head table head table head cell 1 cell 2 cell 3 Table with BORDER=4 caption table head table head table head cell 1 cell 2 cell 3 Table with BORDER=5 caption table head table head table head cell 1 cell 2 cell 3 Table with BORDER=6 caption table head table head table head cell 1 cell 2 cell 3 ",
     "  Table with BORDER=30 caption table head table head table head cell 1 cell 2 cell 3 separator ",
     "Table showing BORDER=0 :   caption table head table head table head cell 1 cell 2 cell 3 separator ",
     "  Table Cellpadding Test separator Table with default cellpadding: ",
     "  caption table head table head table head cell 1 cell 2 cell 3 separator Tables with different cellpaddings: ",
     "  Table with CELLPADDING=1 caption table head table head table head cell 1 cell 2 cell 3 Table with CELLPADDING=2 caption table head table head table head cell 1 cell 2 cell 3 Table with CELLPADDING=3 caption table head table head table head cell 1 cell 2 cell 3 Table with CELLPADDING=4 caption table head table head table head cell 1 cell 2 cell 3 Table with CELLPADDING=5 caption table head table head table head cell 1 cell 2 cell 3 Table with CELLPADDING=10 caption table head table head table head cell 1 cell 2 cell 3 ",
     "  Table with CELLPADDING=30 caption table head table head table head cell 1 cell 2 cell 3 separator ",
     "Table with cellpadding =0 :   caption table head table head table head cell 1 cell 2 cell 3 separator Table Cellspacing Test separator Table with default cellspacing:   caption table head table head table head cell 1 cell 2 cell 3 separator ",
     "Table with CELLSPACING=0 & a border:   caption table head table head table head table head table head cell 1 cell 2 cell 3 cell 4 cell 5 separator ",
     "Tables showing different cellspacing values: ",
     "  Table with CELLSPACING=3 caption table head table head table head cell 1 cell 2 cell 3 Table with CELLSPACING=4 caption table head table head table head cell 1 cell 2 cell 3 Table with CELLSPACING=5 caption table head table head table head cell 1 cell 2 cell 3 Table with CELLSPACING=8 caption table head table head table head cell 1 cell 2 cell 3 Table with CELLSPACING=10 caption table head table head table head cell 1 cell 2 cell 3 ",
     "  Table with CELLSPACING=30 caption table head table head table head cell 1 cell 2 cell 3 separator  Tables Columnspan Test separator Table Header Cells spanning multiple columns:     caption Header 1 ",
     "span=2 cols Header 2 ",
     "span=5 cols Header 3 ",
     "span=10 cols row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 separator ",
     "Table with data cells spanning multiple columns:     caption Head 1 Head 1 Head 1 Head 1 Head 1 Head 1 Head 1 Head 1 Head 1 Head 1 Head 1 Head 1 Head 1 Head 1 Head 1 Head 1 Head 1 Data Cell 1 ",
     "span=2 cols Data Cell 2 ",
     "span=5 cols Data Cell 3 ",
     "span=10 cols row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 separator Table with nested header & data cells spanning multiple columns:     caption Header 1 ",
     "span=8 cols Header 2 ",
     "span=10 cols Data Cell 1 ",
     "span=3 cols Data Cell 2 ",
     "span=5 cols Data Cell 3 ",
     "span=7 cols Data Cell 4 ",
     "span=3 cols row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 1 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 2 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 row 3 separator ",
     "  Tables Rowspan Test separator Table Header Cells spanning multiple rows:   caption Header 1 ",
     "span=2 rows col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 Header 2 ",
     "span=5 rows col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 Header 3 ",
     "span=3 rows col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 separator Table Data Cells spanning multiple rows:   caption Head Data 1 ",
     "span=2 rows col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 Head col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 Head Data 2 ",
     "span=5 rows col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 Head col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 Head col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 Head col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 Head col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 Head Data 3 ",
     "span=3 rows col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 Head col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 Head col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 separator ",
     "Nested Table Header Cells & Data Cells spanning multiple rows:     caption Header 1 ",
     "span=7 rows Data 1 ",
     "span=2 rows col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 Data 2 ",
     "span=5 rows col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 Header 2 ",
     "span=3 rows Data 3 ",
     "span=3 rows col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 col 1 col 2 col 3 col 4 col 5 col 6 col 7 col 8 col 9 separator Tables Caption Test",
     " separator Caption align to top of a table.",
     "",
     " This is the Table1's Caption caption ",
     " Column1 button Column2 Column3 Row1 button Row1 Column1",
     " Row1 Column2",
     " Row1 Column3",
     " text text Row2 ",
     " join (R2 C1) and (R2 C2)",
     " Row2 Column3",
     " Row3",
     " Row3 Column1",
     " join (R3 C2) and (R4 C2)",
     " Row3 Column3",
     " Row4 check box not checked Row4 Column1",
     " Row4 Column3",
     " ",
     " separator Caption align to bottom of table",
     "",
     "",
     " Table's caption on the bottom caption gif link image Checkbox1 check box checked Row1 Column3",
     " Embedded table caption 1Checkbox1 check box checked ",
     " 2 Button button ",
     " 3",
     " 4",
     " 5  6",
     " ",
     " Row3 Column2",
     " Row3 Column3",
     " Row5 Column1",
     " options: option1 combo box  ",
     " ",
     " ",
     "Table Caption in the table",
     "",
     " Table's Caption on the bottom button ",
     " caption ",
     " link Checkbox1 check box checked Row1 Column3",
     " ",
     " Row2 Column2",
     " Radiobuttons in Group A",
     " RadioButton1 not selected radio button ",
     " RadioButton2 selected radio button ",
     " RadioButton3 not selected radio button Embedded table Caption",
     " caption 1Checkbox1 check box checked ",
     " 2 Button button ",
     " 3",
     " 4",
     " 5  6",
     " ",
     " Row3 Column2",
     " Row3 Column3",
     " Row5 Column1",
     " options: option1 combo box  ",
     " ",
     " ",
     "",
     " separator Caption align to left of table",
     "",
     " Table's Caption on the left caption Row1 Column1 Row1 Column2 Row1 Column3 Row2 Column1 Row2 Column2 Row2 Column3 ",
     " separator Caption align to right of table",
     "",
     " Table's Caption on the right caption Row1 Column1 Row1 Column2 Row1 Column3 Row2 Column1 Row2 Column2 Row2 Column3 ",
     " separator Tables Nowrap Test separator ",
     "Table Header & Data Cell with Word Wrapping:   caption The NOWRAP attribute stops normal word wrapping that browsers automatically do to fill the allotted table cell space.  With the NOWRAP attribute, the browser assembles the contents of the cell onto a single line.  The NOWRAP attribute stops normal word wrapping that browsers automatically do to fill the allotted table cell space.  With the NOWRAP attribute, the browser assembles the contents of the cell onto a single line.  separator ",
     "Table Header & Data Cell with NOWRAP:   caption The NOWRAP attribute stops normal word wrapping that browsers automatically do to fill the allotted table cell space.  With the NOWRAP attribute, the browser assembles the contents of the cell onto a single line.  The NOWRAP attribute stops normal word wrapping that browsers automatically do to fill the allotted table cell space.  With the NOWRAP attribute, the browser assembles the contents of the cell onto a single line.  ",
     " separator Multiple <TBODY> in <TABLE>",
     "",
     " body1,row1,col1 body1,row1,col2 body1,row2,col1 body1,row2,col2 body1,row3,col1 body1,row3,col2 body2,row1,col1 body2,row2,col1 body3,row1,col1 body3,row1,col2 body3,row1,col3 body3,row2,col1 body3,row2,col2 body3,row2,col3 body3,row3,col1 body3,row3,col2 body3,row3,col3 body3,row4,col1 body3,row4,col2 body3,row4,col3 body3,row5,col1 body3,row5,col2 body3,row5,col3 ",
     " separator Headers are not in the same column and row as the data cell",
     "",
     " Travel Expense Report caption ",
     " Meals Hotels Transport subtotals San Jose ",
     " ",
     " ",
     " ",
     " 25-Aug-97 37.74 112.00 45.00 ",
     " 26-Aug-97 27.28 112.00 45.00 ",
     " subtotals 65.02 224.00 90.00 379.02 Seattle ",
     " ",
     " ",
     " ",
     " 27-Aug-97 96.25 109.00 36.00 ",
     " 28-Aug-97 35.00 109.00 36.00 ",
     " subtotals 131.25 218.00 72.00 421.25 Totals 196.27 442.00 162.00 800.27 ",
     "",
     " separator link Test Cases",
     "",
     "Case 1: word wrap without BR (Bug)",
     " 39 star characters",
     "",
     "Description: ",
     "Press ctrl+right in following paragraph.",
     "Actual Result: When caret stops at end of last word in line, press ctrl+right, caret doesn't move; press ctrl+right again, caret goes to beginning of first word in next line.",
     "Expected Result: When caret stops at end of last word in line, press ctrl+right, caret goes to end of first word in next line.",
     "",
     "Is there some bug that really bothers you? As well as reporting it, feel free to fix it. Fixing bugs in Mozilla is far easier than in many other applications, because you can fix bugs (such as those in our cross-platform front end, written in XUL, our XML-based User-interface Language, CSS and Javascript) using only the build you are running right now. ",
     "",
     "",
     "Case 2: word wrap with BR (Bug)",
     " 34 star characters",
     "",
     "Description: ",
     "Press ctrl+right in following lines.",
     "Actual Result: Caret doesn't stop at end of the last word in line, but stops at beginning of next line.",
     "Expected Result: Caret should stop at end of the last word in line and should not stop at beginning of next line.",
     "",
     "line one",
     "line two",
     "line three",
     "",
     "",
     "Case 3: word with different styles (It's OK)",
     " 44 star characters",
     "",
     "Description: ",
     "If there's no space, it should be considered as one word. (\"cd\" in \"abcdef\" is italic and bold)",
     "",
     "abcdef abcdef abcdef",
     "",
     "",
     "Case 4: next word with different styles (Bug)",
     " 46 star characters",
     "",
     "Description: ",
     "Press ctrl+right in following line.",
     "Actual Result: Caret doesn't stop at end of \"def\".",
     "",
     "abc def ghi",
     "",
     "",
     "Case 5: several white spaces between words (Bug)",
     " 51 star characters",
     "",
     "Description: ",
     "Press ctrl+right in following line.",
     "Actual Result: Caret stops serveral times between \"abc\" and \"def\".",
     "Expected Result: There should be no stop at white space.",
     "",
     "abc      def",
     "",
     "",
     "Case 6:empty block \"<b></b>\" in word (Bug)",
     " 47 star characters",
     "",
     "6.1. Description: ",
     "Check the html source, there's <b></b> between \"c\" and \"d\".",
     "Caret should not stops after \"c\".",
     "",
     "abcdef",
     "",
     "",
     "6.2. Description: 5087972 link .",
     "Check the html source, there's <b><i></i></b> between \"c\" and \"d\".",
     "Caret should not stops after \"c\".",
     "",
     "abcdef ",
     "",
     "",
     "Case 7: layout.word_select.stop_at_punctuation (Bug)",
     " 53 star characters",
     "",
     "Description: ",
     "set layout.word_select.stop_at_punctuation to true",
     "Press ctrl+right in following line.",
     "Actual Result: Caret doesn't stops between \"-\" and \"p\". (Press ctrl+left, you'll see the difference)",
     "",
     "cross-platform cross-platform cross-platform ",
     "",
     "",
     "Case 8: text navigation after <HR>",
     " 36 star characters",
     "8.1Description:",
     "Use righ arrow go through the following text.",
     "Expected Result: all the text should be navigated.",
     "Actural Result: one line is skipped, caret goes to ^Line4.",
     "",
     "Line1",
     "Line2",
     " separator Line3",
     "Line4",
     "",
     "8.2Description:",
     "Use righ arrow go through the following text.",
     "Expected Result: all the text should be navigated.",
     "Actural Result: one line and a character are skipped, caret goes to L^ine4.",
     "",
     "Line1",
     "Line2",
     " separator ",
     "Line4(Line3 is empty BR)",
     "",
     "",
     "",
     "",
     "'"]))

########################################################################
# Close the demo
#
sequence.append(KeyComboAction("<Control>l"))
sequence.append(WaitForFocus(acc_role=pyatspi.ROLE_ENTRY))
sequence.append(TypeAction("about:blank"))
sequence.append(KeyComboAction("Return"))
sequence.append(WaitForDocLoad())

# Just a little extra wait to let some events get through.
#
sequence.append(PauseAction(3000))

sequence.append(utils.AssertionSummaryAction())

sequence.start()
