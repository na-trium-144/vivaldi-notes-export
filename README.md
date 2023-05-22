# vivaldi-notes-export

Vivaldiブラウザーのメモをフォルダ構造を保持してエクスポートします

日付も保持したかったがdate_addedの形式がよくわからなかったのでパス

## usage

vivaldi://about からプロファイルのパスを調べ、それを引数に渡してmain.pyを実行する

オプションは以下

```
usage: main.py [-h] [-e EXTENSION] [-l LENGTH] [-t] profile_dir [export_dir]

positional arguments:
  profile_dir           Vivaldi Profile Path
  export_dir            Export Destination (default: current dir)

options:
  -h, --help            show this help message and exit
  -e EXTENSION, --extension EXTENSION
                        File Extension of Notes (default: .md)
  -l LENGTH, --length LENGTH
                        Maximum File Name Length (default: 30)
  -t, --include_trash   Also Export Notes in Trash
```