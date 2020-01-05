from typing import Dict, List

from dataclasses import dataclass, asdict

from itertools import chain


@dataclass(frozen=True)
class Lingo:
    source: str
    version: str
    name: str
    type: str


types: Dict[str, str] = {
    "f": "function",
    "c": "command",
    "p": "property",
    "function": "function",
    "command": "command",
    "property": "property",
}


def normalize_entry(entry: str) -> List[str]:
    for char in '\t{}"/':
        entry = entry.replace(char, "")
    return entry.strip().split(",")


def parse_version(version: str) -> str:
    if version == "":
        return ""
    return version.split()[0].replace("D", "")


def parse_type(data: str) -> str:
    default = "unkown"
    _type = data.split()
    if len(_type) <= 1:
        return default
    return types.get(_type[1], default)


def parse_builtin_entry(entry: str) -> Lingo:
    data = normalize_entry(entry)
    name = data[0]
    version = parse_version(data[-1])
    _type = parse_type(data[-1])
    return Lingo(source="builtins", version=version, name=name, type=_type)


def parse_builtins(lines: str) -> List[Lingo]:
    return [
        parse_builtin_entry(entry.strip())
        for entry in lines.split("\n")
        if (entry.strip() and not entry.strip().startswith("/"))
    ]


def parse_the_entry(entry: str) -> Lingo:
    data = normalize_entry(entry)
    name = data[1]
    version = parse_version(data[3])
    _type = parse_type(data[3])
    return Lingo(source="the", version=version, name=name, type=_type)


def parse_thes(lines: str) -> List[Lingo]:
    return [
        parse_the_entry(entry.strip())
        for entry in lines.split("\n")
        if (entry.strip() and not entry.strip().startswith("/"))
    ]


if __name__ == "__main__":
    with open("inputs/builtins.txt") as builtins_entries:
        builtins = parse_builtins(builtins_entries.read())
    with open("inputs/the.txt") as the_entries:
        thes = parse_thes(the_entries.read())

    with open("inputs/d3.menus") as D3:
        d3_entries = D3.read().split("\n")
    with open("inputs/d4.menus") as D4:
        d4_entries = D4.read().split("\n")

    all_commands = {
        entry.name.lower(): entry for entry in chain(builtins, thes)
    }

    missing = []
    for entry in d3_entries:
        if entry.strip() == "":
            continue
        if entry.lower() not in all_commands.keys():
            missing.append(entry)
    print("missing D3:")
    for entry in missing:
        print(entry)

    missing = []
    for entry in d4_entries:
        if entry.strip() == "":
            continue
        if entry.lower() not in all_commands.keys():
            missing.append(entry)
    print("missing D4:")
    for entry in missing:
        print(entry)