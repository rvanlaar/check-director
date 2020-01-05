from dataclasses import asdict

from .check import parse_builtins, parse_the_entry


def test_builtins_import() -> None:
    lines = """
        { "log",			Lingo::b_log,			1, 1, true, 4, FBLTIN },	//			D4 f
        { "value",		 	Lingo::b_value,			1, 1, true, 2, FBLTIN },	// D2 f
        { "playAccel",		Lingo::b_playAccel,		-1,0, false, 2, BLTIN },	// D2

        """
    result = parse_builtins(lines)
    assert asdict(result[0]) == {
        "source": "builtins",
        "type": "function",
        "version": "4",
        "name": "log",
    }

    assert asdict(result[1]) == {
        "source": "builtins",
        "type": "function",
        "version": "2",
        "name": "value",
    }

    assert asdict(result[2]) == {
        "source": "builtins",
        "type": "unkown",
        "version": "2",
        "name": "playAccel",
    }

def test_comments_builtins() -> None:
    line = """                // go           // D2"""
    assert parse_builtins(line) == []

def test_parse_the_entry() -> None:
    line = """{ kTheCast,		"video",		kTheVideo },		//				D4 p"""
    assert asdict(parse_the_entry(line)) == {
        "source": "the",
        "type": "property",
        "version": "4",
        "name": "video",
    }

    line = """{ kTheCast,		"purgePriority",kThePurgePriority },//	 			D4 p // 0 Never purge, 1 Purge Last, 2 Purge next, 2 Purge normal"""
    assert asdict(parse_the_entry(line)) == {
        "source": "the",
        "type": "property",
        "version": "4",
        "name": "purgePriority",
    }

def test_parse_the_entry_missing_parts() -> None:
    line = """	{ kTheCastMembers,		"castmembers",		false },	//		 D3"""
    assert asdict(parse_the_entry(line)) == {
        "source": "the",
        "type": "unkown",
        "version": "3",
        "name": "castmembers",
    }

    line = """{ kTheMenu,				"menu",				true  },"""
    assert asdict(parse_the_entry(line)) == {
        "source": "the",
        "type": "unkown",
        "version": "",
        "name": "menu",
    }



