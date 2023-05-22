#!/usr/bin/env python3
import sys
import os
import json
import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('profile_dir', help='Vivaldi Profile Path')
    parser.add_argument('export_dir', help='Export Destination (default: current dir)', nargs="?", default=".")
    parser.add_argument('-e', '--extension', help="File Extension of Notes (default: .md)", default=".md")
    parser.add_argument('-l', '--length', help="Maximum File Name Length (default: 30)", default="30")
    parser.add_argument('-t', '--include_trash', help="Also Export Notes in Trash", action="store_true")
    args = parser.parse_args()
    notes_file = os.path.join(args.profile_dir, "Notes")
    with open(notes_file, mode="r", encoding="utf-8", errors="replace") as f:
        notes_data = json.loads(f.read())
    for c in notes_data["children"]:
        parse_note(c, args.export_dir, args)

def parse_note(note, path, args):
    if note["type"] == "note":
        content = note["content"]
        id = note["id"]
        title = content.split("\n")[0].lstrip("#").strip()
        title = "".join((i if i not in r'\/:*?"<>|' else '_') for i in title)[:int(args.length)]
        if title == "":
            title = f"noname_{id}"
        # date = int(note["date_added"]) よくわからんのでパス
        url = note["url"]
        if url != "":
            content += "\n\n" + url
        filepath = os.path.join(path, title + args.extension) 
        print(filepath)
        with open(filepath, "w") as f:
            f.write(content)
        # os.utime(filepath, ns=(date * 100, date * 100))
    elif note["type"] == "folder":
        path = os.path.join(path, note["subject"])
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
        for c in note["children"]:
            parse_note(c, path, args)
    elif note["type"] == "trash":
        if args.include_trash:
            path = os.path.join(path, "Trash")
            try:
                os.mkdir(path)
            except FileExistsError:
                pass
            for c in note["children"]:
                parse_note(c, path, args)

if __name__ == '__main__':
    main()
