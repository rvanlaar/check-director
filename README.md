
When scummvm is updated:

Take the contents of the builtins variable from lingo-builtins.cpp and put it in inputs/builtins.txt
Same for lingo-the.cpp

The program checks if the lowercase name is in the lingo-builtins or lingo-the tables.

The current missing output is:
    
    -
    ()
    *
    /
    &
    &&
    +
    <
    <=
    <>
    =
    >
    >=
    and
    cast hilite
    cast name
    cast number
    cast picture
    cast size
    cast text
    char
    contains
    exit
    factory
    factory
    field textAlign
    field textFont
    field textHeight
    field textSize
    field textStyle
    global
    go to
    go to movie
    if
    instance
    item
    line
    macro
    menu checkMark
    menu enabled
    menu name
    menu script
    menu:
    method
    mod
    mouseDownScript
    mouseUpScript
    not
    on
    on idle
    on startMovie
    on stepMovie
    on stopMovie
    open
    or
    play
    play done
    play movie
    put
    put after
    put before
    put into
    repeat while
    repeat with
    set
    sound fadeIn
    sound fadeOut
    sound playFile
    sound stop
    sound volume
    sprite s intersects
    sprite s within
    starts
    visibility
    when keyDown
    when mouseDown
    when mouseUp
    when timeOut
    word
