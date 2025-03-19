import os, ast, syntax, sys, spell_check, runner, py_debug

from syntax import BRIGHT_YELLOW

RED = "\033[31m"
RESET = "\033[0m"

commands = [
    "a", "a-source",
    "cls", "clear-screen",
    "cf", "clear-file",
    "exec", "execute",
    "cl_file",
    "mkf", "make-file",
    "nl", "new-line",
    "nlw", "new-line-write",
    "o", "open",
    "rw",
    "s", "source",
    "sn", "st",
    "snt", "stn",
    "w", "write",
    "lw", "line-write",
    "wn", "write-nl",
    "f", "find",
    "r", "run",
    "dl", "delete",
    "csp", "check-spell",
]
def get_syntax_by_filename(filename):
    _, file_extension = os.path.splitext(filename)

    file_extension = file_extension[1:].lower()

    syntax_mapping = {
        'py': 'Python',
        'js': 'JavaScript',
        'html': 'HTML',
        'css': 'CSS',
        'json': 'JSON',
        'xml': 'XML',
        'java': 'Java',
        'cpp': 'C++',
        'c': 'C',
        'rb': 'Ruby',
        'go': 'Go',
        'php': 'PHP',
        'sh': 'Bash',
        'txt': 'Text',
    }

    return syntax_mapping.get(file_extension, f"unk")

def parse_array_string(array_string):
    try:
        array = ast.literal_eval(array_string)
        if isinstance(array, list):
            return array
        else:
            raise ValueError(f"wined: {RED}error{RESET}: can't compile string to array")
    except (SyntaxError, ValueError) as e:
        print(f"wined: {RED}error{RESET}: string to array compilation: {e}")
        return []


def update_multiline_string(multiline_string, line_number, new_line):
    lines = multiline_string.split('\n')

    if 0 <= line_number < len(lines):
        lines[line_number] = new_line
    else:
        print(f"wined: {RED}error{RESET}: line by number {line_number} not exists")

    return '\n'.join(lines)


def add_specific_line_to_multiline_string(multiline_string, line_number, line_to_add):
    lines = multiline_string.split('\n')

    if line_number >= len(lines):
        lines.append(line_to_add)
    elif 0 <= line_number < len(lines):
        lines.insert(line_number, line_to_add)
    else:
        print(f"wined: {RED}error{RESET}: line by number {line_number} not exists")

    return '\n'.join(lines)


def remove_line_from_multiline_string(multiline_string, line_number):
    lines = multiline_string.split('\n')

    if 0 <= line_number < len(lines):
        lines.pop(line_number)
    else:
        print(f"wined: {RED}error{RESET}: line by number {line_number} not exists")

    return '\n'.join(lines)


def get_line(multiline_string, line_number):
    lines = multiline_string.strip().split('\n')

    if 0 <= line_number < len(lines):
        return lines[line_number]
    else:
        print(f"wined: {RED}error{RESET}: line by number {line_number} not exists")


current = ""

def find_and_print(multiline_string, substring):
    lines = multiline_string.splitlines()

    filtered_lines_with_index = [(index, line.replace(substring, f"{syntax.BRIGHT_YELLOW}{substring}{RESET}")) for index, line in enumerate(lines) if substring in line]

    for index, line in filtered_lines_with_index:
        print(f"{index+1} | {line}")


def print_beautifull(text, size = 12123123123):
    if size == 12123123123:
        size = len(text)
    asd = syntax.do_syntax(current, text).split('\n')
    print(f" {'-'*11} {size} bytes {'-'*11}") # ----------- 99 bytes -----------
    for i in range(len(asd)):
        print(f"{i+1} | {asd[i]}")
    print(f" {'-'*32}")



def wined_main():
    global current

    inputer = "> "
    file_source = ""
    source_file_name = ""
    std_args = []

    while True:
        try:
            inp = input(inputer).replace("\t", '    ')
            inpl = inp.split(" ")
            inpl1 = inpl[0].strip()

            if inpl1 == "o" or inpl1 == "open":
                source_file_name = inpl[1]
                current = get_syntax_by_filename(source_file_name)
                with open(source_file_name, 'r', encoding="utf-8") as f:
                    file_source = f.read()
                    f.close()
            elif inpl1 == "cls" or inpl1 == "clear-screen":
                os.system("cls" if os.name == "nt" else "clear")
            elif inpl1 == "csp" or inpl1 == "check-spell":
                smws = spell_check.do_spell_check(file_source)
                for key, v in smws.items():
                    print(f"<{key}> similar <{', '.join(v)}>")
            elif inpl1 == "set-args":
                std_args = inpl[1::]
                print("args", inpl[1::])
            elif inpl1 == "r" or inpl1 == "run":
                runner.do_run(current, source_file_name, std_args)
            elif inpl1 == "B" or inpl1 == "build":
                runner.do_build(current, source_file_name, std_args)
            elif inpl1 == "a" or inpl1 == "a-source":
                line_number = int(inpl[1]) - 1

                print(f" {'-'*11} {len(get_line(file_source, line_number))} bytes {'-'*11}")
                print(f'{line_number + 1} | {get_line(file_source, line_number)}')
                print(f" {"-"*32}")
            elif inpl1 == "s" or inpl1 == "source":
                print_beautifull(file_source)
            elif inpl1 == "sn":
                print_beautifull(file_source.replace("\n", "$\n"), size=len(file_source))
            elif inpl1 == "st":
                print_beautifull(file_source.replace("\t", "%\t"), size=len(file_source))
            elif inpl1 == "snt" or inpl1 == "stn":
                print_beautifull(file_source.replace("\n", "$\n").replace("\t", "%\t"), size=len(file_source))
            elif inpl1 == "cl_file":
                print(f'the file in use: {source_file_name}')
            elif inpl1 == "inp" or inpl1 == "input-text":
                text = ' '.join(inpl[1::])

                inputer = text
            elif inpl1 == "rev" or inpl1 == "reverse":
                text = ' '.join(inpl[1::])[::-1]

                print(text)
            elif inpl1 == "f" or inpl1 == "find":
                text = ' '.join(inpl[1::])

                print(f"""Found: {syntax.CYAN}{file_source.count(text)}{RESET}""")
                find_and_print(file_source, text)
            elif inpl1 == "rp" or inpl1 == "replace":
                word = inpl[1].strip()
                text = ' '.join(inpl[2::]).strip()

                print(f"""Replaced: {syntax.CYAN}{file_source.count(word)}{RESET}""")
                file_source = file_source.replace(word, text)
            elif inpl1 == "svar" or inpl1 == "source-var":
                vars_ = py_debug.get_variables_and_values_from_code(file_source)

                for k , v in vars_.items():
                    print(f"{k} = {v}")
            elif inpl1 == "sf" or inpl1 == "source-f":
                fs_ = py_debug.get_functions_from_code(file_source)

                print(fs_)
            elif inpl1 == "dl" or inpl1 == "delete":
                line_number = int(inpl[1]) - 1

                file_source = remove_line_from_multiline_string(file_source, line_number)
            elif inpl1 == "nl" or inpl1 == "new-line":
                line_number = int(inpl[1])

                file_source = add_specific_line_to_multiline_string(file_source, line_number, '')
            elif inpl1 == "pra": # py array [...] to normal
                source_arr = ''.join(inpl[1::])

                print("array", ' '.join(parse_array_string(source_arr)))
            elif inpl1 == "par": # to py array [...]
                source_arr = inpl[1::]

                print("array", f'[ "{'", "'.join(source_arr)}" ]')
            elif inpl1 == "cv_bin":
                nums = list(map(int, inpl[1::]))
                binary_array = [bin(num)[2:] for num in nums]

                print("binary", binary_array)
            elif inpl1 == "cv_hex":
                nums = list(map(int, inpl[1::]))
                hex_array = [hex(num)[2:].upper() for num in nums]

                print("hex", hex_array)
            elif inpl1 == "cv_X":
                nums = list(map(int, inpl[1::]))
                base12_array = [format(num, 'X') if num < 12 else format(num, 'X') for num in nums]
                base12_array = [''.join([str(int(digit, 16)) if int(digit, 16) < 12 else chr(ord('A') + int(digit, 16) - 10) for digit in format(num, 'X')]) for num in nums]

                print("X", base12_array)
            elif inpl1 == "cv_chr":
                nums = list(map(int, inpl[1::]))
                chr_array = list(map(chr, nums))

                print("chr", chr_array)
            elif inpl1 == "cv_ord":
                chrs = inpl[1::]
                ord_array = list(map(ord, chrs))

                print("ord", ord_array)
            elif inpl1 == "exec" or inpl1 == "execute":
                text = ' '.join(inpl[1::])
            
                os.system(text)
            elif inpl1 == "w" or inpl1 == "write":
                text = ' '.join(inpl[1::])

                file_source += text + '\n'
                with open(source_file_name, 'a', encoding='utf-8') as f:
                    print("writen ", f.write(text + '\n'))
                    f.close()
            elif inpl1 == "nlw" or inpl1 == "new-line-write":
                line_number = int(inpl[1])
                text = ' '.join(inpl[2::])

                file_source = add_specific_line_to_multiline_string(file_source, line_number, '')

                line_number += 1

                file_source = update_multiline_string(file_source, line_number=line_number - 1, new_line=text)
                with open(source_file_name, 'w', encoding='utf-8') as f:
                    print("writen ", f.write(file_source))
                    f.close()
            elif inpl1 == "lw" or inpl1 == "line-write":
                line_number = int(inpl[1])
                text = ' '.join(inpl[2::])

                file_source = update_multiline_string(file_source, line_number=line_number-1, new_line=text)
                with open(source_file_name, 'w', encoding='utf-8') as f:
                    print("writen ", f.write(file_source))
                    f.close()
            elif inpl1 == "wn" or inpl1 == "write-nl":
                text = ' '.join(inpl[1::])

                file_source += text + '\n'
                with open(source_file_name, 'a', encoding='utf-8') as f:
                    print("writen ", f.write(text + '\n'))
                    f.close()
            elif inpl1 == "rw" or inpl1 == "rewrite":
                text = ' '.join(inpl[1::])

                file_source = text + '\n'
                with open(source_file_name, 'w', encoding='utf-8') as f:
                    print("writen ", f.write(text + '\n'))
                    f.close()
            elif inpl1 == "cf" or inpl1 == "clear-file":
                text = ''
                file_source = text

                with open(source_file_name, 'w', encoding='utf-8') as f:
                    f.write(text)
                    f.close()
            elif inpl1 == "mkf" or inpl1 == "make-file":
                text = inpl[1]

                with open(text, 'w', encoding='utf-8') as f:
                    f.write('')
                    f.close()
            elif inpl1 == "q" or inpl1 == "quit":
                sys.exit(0)
            else:
                similar = spell_check.do_spell_check(inpl1, langs=[commands])
                if len(similar) != 0:
                    print(f'command {inpl1} not found, maybe you mean:')

                    for k, v in similar.items():
                        print(f"\tcommand <{' '.join(v)}>")
            if source_file_name != "":
                with open (source_file_name, "r", encoding='utf-8') as f1:
                    rsd = f1.read()
                    if rsd != file_source:
                        with open (source_file_name, "w", encoding='utf-8') as f:
                            a = f.write(file_source)
                            if a != 0:
                                print("writen", a)
                            f.close()
        except IndexError:
            print(f"wined: {RED}error{RESET}: the arguments for {inpl1} was excepted")
        except KeyboardInterrupt:
            return
        except EOFError:
            print(f"wined: !{RED}error{RESET}: please not use pipe")
            sys.exit()
        except Exception as e:
            print(f"{type(e)}: {e}")
if __name__ == "__main__":
    print("[wined] version python")

    wined_main()