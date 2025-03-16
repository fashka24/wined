# 📚 Docs of Wined

## 🛠️ Commands

| Command                            | Description                                                    |
|------------------------------------|----------------------------------------------------------------|
| `a/a-source [line]`                | Print the specified line by line                              |
| `cls/clear-screen`                 | Clear the terminal screen                                      |
| `cf/clear-file`                    | Completely clear an open file                                  |
| `exec/execute [command]`           | Execute the specified command in cmd/sh                        |
| `cl_file`                          | Print the contents of an open file                             |
| `mkf/make-file [path]`             | Create a new file at the specified path                       |
| `nl/new-line [line]`               | Add an empty line at the specified line                       |
| `nlw/new-line-write [line] [text]` | Add an empty line at the specified line and write the text    |
| `o/open [path]`                    | Open the file at the specified path                           |
| `rw [text]`                        | Completely clear the file and write the specified text        |
| `s/source`                         | Print the source code                                         |
| `s[n/t]`                           | Print the source code with new lines (`sn`) or tabs (`st`)   |
| `snt/stn`                          | Print the source code with new lines and tabs                |
| `w/write [text]`                   | Write the specified text to an open file                      |
| `lw/line-write [line] [text]`      | Write the specified text at the specified line                |
| `wn [text]`                        | Write the specified text to an open file with a new line     |

## 📖 Explanations

- **[line]** - line index
- **[command]** - command for the terminal
- **[path]** - path to the file
- **[text]** - text

## Compilation and installation

### For all
install and run pyinstaller
```shell
pip install pyinstaller
pyinstaller --onefile wined.py
```

### For windows 
create system directory with name `Wined` in `C:\Program Files` 
and move file `dist\wined.exe` to it.

next step open `Set environment variable` and add path `C:\Program Files\Wined` to Path

### For linux
move `dist/wined` to `/usr/bin`
```shell
sudo mv dist/wined /usr/bin/wined
```