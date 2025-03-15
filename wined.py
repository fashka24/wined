import os

RED = "\033[31m"
RESET = "\033[0m"

def print_beautifull(text, size = 12123123123):
    if size == 12123123123:
        size = len(text)
    print(f" {'-'*11} {size} bytes {'-'*11}") # ----------- 99 bytes -----------
    for i in range(len(text.split('\n'))):
        print(f"{i+1} | {text.split('\n')[i]}")
    print(f" {'-'*32}") 

def wined_main():
    file_source = ""
    source_file_name = ""

    while True:
        try:
            inp = input("> ")
            inpl = inp.split(" ")
            inpl1 = inpl[0]

            if inpl1 == "o" or inpl1 == "open":
                source_file_name = inpl[1]
                with open(source_file_name, 'r', encoding="utf-8") as f:
                    file_source = f.read()
                    f.close()
            elif inpl1 == "cls" or inpl1 == "clear-screen":
                os.system("cls" if os.name == "nt" else "clear")
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
            elif inpl1 == "exec" or inpl1 == "execute":
                text = ' '.join(inpl[1::])

                os.system(text)
            elif inpl1 == "w" or inpl1 == "write":
                text = ' '.join(inpl[1::])

                file_source += text + '\n'
                with open(source_file_name, 'a', encoding='utf-8') as f:
                    f.write(text + '\n')
                    f.close()
            elif inpl1 == "wn" or inpl1 == "write-nl":
                text = ' '.join(inpl[1::])

                file_source += text + '\n'
                with open(source_file_name, 'a', encoding='utf-8') as f:
                    f.write(text + '\n')
                    f.close()
            elif inpl1 == "rw" or inpl1 == "rewrite":
                text = ' '.join(inpl[1::])

                file_source = text + '\n'
                with open(source_file_name, 'w', encoding='utf-8') as f:
                    f.write(text + '\n')
                    f.close()
            elif inpl1 == "cf" or inpl1 == "clear-file":
                text = ''

                file_source = text
                with open(source_file_name, 'w', encoding='utf-8') as f:
                    f.write(text)
                    f.close()
        except IndexError:
            print(f"wined: {RED}error{RESET}: the arguments for {inpl1} was excepted")
        except KeyboardInterrupt:
            return
        except EOFError:
            print(f"wined: !{RED}error{RESET}: please not use pipe")
            exit()
        except Exception as e:
            print(f"{type(e)}: {e}")
if __name__ == "__main__":
    wined_main()