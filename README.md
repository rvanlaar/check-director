
When scummvm is updated:

Take the contents of the builtins variable from lingo-builtins.cpp and put it in inputs/builtins.txt
Same for lingo-the.cpp

The program checks if the lowercase name is in the lingo-builtins or lingo-the tables.

The current missing output for D3 is:
    
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
    when keyDown
    when mouseDown
    when mouseUp
    when timeOut
    word

Should be D3 or lower but is classified as D4:

    backColor
    editableText
    foreColor
    height
    moveableSprite
    volume
    width

For D4 the missing output is:

    -
    --
    ()
    []
    *
    /
    &
    &&
    #
    +
    <
    <=
    <>
    =
    >
    >=
    �
    after
    ancestor
    and
    backColor of cast
    backColor of sprite
    before
    blend of sprite
    bottom of sprite
    cast backColor
    cast castType
    cast depth
    cast fileName
    cast foreColor
    cast height
    cast hilite
    cast loaded
    cast modified
    cast name
    cast number
    cast palette
    cast picture
    cast purgePriority
    cast rect
    cast regPoint
    cast scriptText
    cast size
    cast text
    cast width
    castNum of sprite
    castType of cast
    char of
    checkMark of menuItem
    close window
    constraint of sprite
    contains
    controller of cast
    copyToClipBoard cast
    cursor of sprite
    depth of cast
    digitalVideo
    digitalVideo cast center
    digitalVideo cast controller
    digitalVideo cast crop
    digitalVideo cast directToStage
    digitalVideo cast duration
    digitalVideo cast frameRate
    digitalVideo cast loop
    digitalVideo cast pausedAtStart
    digitalVideo cast preload
    digitalVideo cast sound
    digitalVideo cast video
    digitalVideo sprite movieRate
    digitalVideo sprite movieTime
    digitalVideo sprite startTime
    digitalVideo sprite stopTime
    digitalVideo sprite volume
    directToStage of cast
    done
    down
    drawRect of window
    duplicate cast {n}
    editableText of sprite
    else
    enabled of menuItem
    end
    erase cast
    exit
    exit repeat
    exitFrame
    fadeIn
    fadeOut
    fileName of cast
    fileName of window
    foreColor of cast
    foreColor of sprite
    frameRate of cast
    global
    go loop
    go next
    go previous
    height of cast
    height of sprite
    hilite of cast
    idle
    if
    ilk list
    ilk point
    ilk rect
    in
    inflate rect
    ink of sprite
    inside point
    instance
    intersect rect
    intersects
    into
    item of
    items
    keyDown
    keyUp
    last
    left of sprite
    line of
    lines
    lineSize of sprite
    list ilk
    loaded of cast
    locH of sprite
    locV of sprite
    loop of cast
    map point
    map rect
    mAtFrame
    mDescribe
    mDispose
    me
    menus
    mGet
    mInstanceRespondsTo
    mMessageList
    mName
    mNew
    mod
    modal window
    modified of cast
    mouseDownScript
    mouseUpScript
    moveableSprite of sprite
    movieRate of sprite
    movieTime of sprite
    mPerform
    mPut
    mRespondsTo
    name of cast
    name of menu
    name of menuItem
    next
    next repeat
    not
    number of cast
    number of castMembers
    number of chars
    number of items
    number of lines
    number of menuItems
    number of menus
    number of words
    of
    offset rect
    on
    on enterFrame
    on enterFrame
    on exitFrame
    on idle
    on keyDown
    on keyUp
    on mouseDown
    on mouseUp
    on startMovie
    on stopMovie
    open
    open window
    or
    palette of cast
    pausedAtStart of cast
    picture of cast
    play
    play done
    playFile
    preload of cast
    previous
    property
    purgePriority of cast
    put
    put after
    put before
    put into
    rect of cast
    rect of window
    rect point
    regPoint of cast
    repeat while
    repeat with
    right of sprite
    script of menuItem
    scriptNum of sprite
    scriptText of cast
    set
    size of cast
    sound close
    sound fadeIn
    sound fadeOut
    sound of cast
    sound playFile
    sound stop
    sourceRect of window
    sprite backColor
    sprite blend
    sprite bottom
    sprite castNum
    sprite constraint
    sprite cursor
    sprite editableText
    sprite foreColor
    sprite height
    sprite ink
    sprite intersects
    sprite left
    sprite lineSize
    sprite locH
    sprite locV
    sprite moveableSprite
    sprite right
    sprite scriptNum
    sprite stretch
    sprite top
    sprite trails
    sprite type
    sprite visible
    sprite width
    sprite within
    startMovie
    starts
    startTime of sprite
    stop
    stopMovie
    stopTime of sprite
    stretch of sprite
    tell
    text of cast
    the
    then
    to
    top of sprite
    trails of sprite
    type of sprite
    union rect
    visible of sprite
    visible of window
    volume of sound
    volume of sprite
    while
    width of cast
    width of sprite
    with
    within
    word of
    words
