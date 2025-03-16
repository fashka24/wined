import re

# colors

RESET = "\033[0m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
ORANGE = '\033[38;5;214m' 
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# syntaxs

py_syntax = {
    "or": f"{BLUE}or{RESET}",
    "is": f"{BLUE}is{RESET}",
    "if": f"{MAGENTA}if{RESET}",
    "def": f"{BLUE}def{RESET}",
    "and": f"{BLUE}and{RESET}",
    "for": f"{BLUE}for{RESET}",
    "elif": f"{MAGENTA}elif{RESET}",
    "with": f"{BLUE}with{RESET}",
    "else": f"{MAGENTA}else{RESET}",
    "while": f"{BLUE}while{RESET}",
    "import": f"{MAGENTA}import{RESET}",
    "(": f"{YELLOW}({RESET}",
    ")": f"{YELLOW}){RESET}",
    "{": f"{CYAN}{'{'}{RESET}",
    "}": f"{CYAN}{'}'}{RESET}",
    "#": f"{GREEN}#",
    "=": f"{BRIGHT_CYAN}={RESET}",
    ">=": f"{BRIGHT_CYAN}>={RESET}",
    "<=": f"{BRIGHT_CYAN}<={RESET}",
    ">": f"{BRIGHT_CYAN}>{RESET}",
    "<": f"{BRIGHT_CYAN}<{RESET}",
    "==": f"{BRIGHT_CYAN}=={RESET}",
    "\n": f"{RESET}\n",
}
bash_syntax = {
    "if": f"{MAGENTA}if{RESET}",
    "fi": f"{MAGENTA}if{RESET}",
    "for": f"{BLUE}for{RESET}",
    "else": f"{MAGENTA}else{RESET}",
    "while": f"{BLUE}while{RESET}",
    "(": f"{YELLOW}({RESET}",
    ")": f"{YELLOW}){RESET}",
    "{": f"{CYAN}{'{'}{RESET}",
    "}": f"{CYAN}{'}'}{RESET}",
    "//": f"{GREEN}//",
    "&&": f"{BLUE}&&{RESET}",
    "||": f"{BLUE}||{RESET}",
    "|": f"{BLUE}|{RESET}",
    ">": f"{BRIGHT_CYAN}>{RESET}",
    "<": f"{BRIGHT_CYAN}<{RESET}",
    "=": f"{BRIGHT_CYAN}={RESET}",
    ">=": f"{BRIGHT_CYAN}>={RESET}",
    "<=": f"{BRIGHT_CYAN}<={RESET}",
    "=>": f"{BRIGHT_CYAN}=>{RESET}",
    "==": f"{BRIGHT_CYAN}=={RESET}",
    ">==": f"{BRIGHT_CYAN}>=={RESET}",
    "<==": f"{BRIGHT_CYAN}<=={RESET}",
    "===": f"{BRIGHT_CYAN}==={RESET}",
    "\n": f"{RESET}\n",
}
js_syntax = {
    "if": f"{MAGENTA}if{RESET}",
    "for": f"{BLUE}for{RESET}",
    "var": f"{BLUE}for{RESET}",
    "let": f"{BLUE}for{RESET}",
    "with": f"{BLUE}with{RESET}",
    "else": f"{MAGENTA}else{RESET}",
    "while": f"{BLUE}while{RESET}",
    "import": f"{MAGENTA}import{RESET}",
    "function": f"{BLUE}function{RESET}",
    "(": f"{YELLOW}({RESET}",
    ")": f"{YELLOW}){RESET}",
    "{": f"{CYAN}{'{'}{RESET}",
    "}": f"{CYAN}{'}'}{RESET}",
    "//": f"{GREEN}//",
    "&&": f"{BLUE}&&{RESET}",
    "||": f"{BLUE}||{RESET}",
    ">": f"{BRIGHT_CYAN}>{RESET}",
    "<": f"{BRIGHT_CYAN}<{RESET}",
    "=": f"{BRIGHT_CYAN}={RESET}",
    ">=": f"{BRIGHT_CYAN}>={RESET}",
    "<=": f"{BRIGHT_CYAN}<={RESET}",
    "=>": f"{BRIGHT_CYAN}=>{RESET}",
    "==": f"{BRIGHT_CYAN}=={RESET}",
    ">==": f"{BRIGHT_CYAN}>=={RESET}",
    "<==": f"{BRIGHT_CYAN}<=={RESET}",
    "===": f"{BRIGHT_CYAN}==={RESET}",
    "\n": f"{RESET}\n",
}
java_syntax = {
    "if": f"{MAGENTA}if{RESET}",
    "do": f"{MAGENTA}do{RESET}",
    "for": f"{BLUE}for{RESET}",
    "else": f"{MAGENTA}else{RESET}",
    "while": f"{BLUE}while{RESET}",
    "import": f"{MAGENTA}import{RESET}",
    "instanceof": f"{MAGENTA}instanceof{RESET}",
    "(": f"{YELLOW}({RESET}",
    ")": f"{YELLOW}){RESET}",
    "{": f"{CYAN}{'{'}{RESET}",
    "}": f"{CYAN}{'}'}{RESET}",
    "//": f"{GREEN}//",
    "&&": f"{BLUE}&&{RESET}",
    "||": f"{BLUE}||{RESET}",
    ">": f"{BRIGHT_CYAN}>{RESET}",
    "<": f"{BRIGHT_CYAN}<{RESET}",
    "=": f"{BRIGHT_CYAN}={RESET}",
    ">=": f"{BRIGHT_CYAN}>={RESET}",
    "<=": f"{BRIGHT_CYAN}<={RESET}",
    "=>": f"{BRIGHT_CYAN}=>{RESET}",
    "==": f"{BRIGHT_CYAN}=={RESET}",
    "\n": f"{RESET}\n",
}
cpp_syntax = {
    "if": f"{MAGENTA}if{RESET}",
    "do": f"{MAGENTA}do{RESET}",
    "for": f"{BLUE}for{RESET}",
    "else": f"{MAGENTA}else{RESET}",
    "while": f"{BLUE}while{RESET}",
    "#define": f"{MAGENTA}#define{RESET}",
    "#pragma": f"{MAGENTA}#pragma{RESET}",
    "#ifdef": f"{MAGENTA}#ifdef{RESET}",
    "#endif": f"{MAGENTA}#endif{RESET}",
    "#ifndef": f"{MAGENTA}#ifndef{RESET}",
    "#include": f"{MAGENTA}#include{RESET}",
    "(": f"{YELLOW}({RESET}",
    ")": f"{YELLOW}){RESET}",
    "{": f"{CYAN}{'{'}{RESET}",
    "}": f"{CYAN}{'}'}{RESET}",
    "//": f"{GREEN}//",
    "&&": f"{BLUE}&&{RESET}",
    "||": f"{BLUE}||{RESET}",
    ">": f"{BRIGHT_CYAN}>{RESET}",
    "<": f"{BRIGHT_CYAN}<{RESET}",
    "=": f"{BRIGHT_CYAN}={RESET}",
    ">=": f"{BRIGHT_CYAN}>={RESET}",
    "<=": f"{BRIGHT_CYAN}<={RESET}",
    "==": f"{BRIGHT_CYAN}=={RESET}",
    "\n": f"{RESET}\n",
}
html_syntax = {
    "<": f"{BRIGHT_CYAN}<{RESET}",
    "=": f"{BRIGHT_CYAN}={RESET}",
    "/>": f"{BRIGHT_CYAN}/>{RESET}"
}
xml_syntax = {
    "<": f"{BRIGHT_CYAN}<{RESET}",
    "=": f"{BRIGHT_CYAN}={RESET}",
    "/>": f"{BRIGHT_CYAN}/>{RESET}"
}
css_syntax = {
    ";": f"{YELLOW};{RESET}",
    "{": f"{CYAN}{'{'}{RESET}",
    "}": f"{CYAN}{'}'}{RESET}",
    "\n": f"{RESET}\n",
}
json_syntax = {
    ",": f"{YELLOW};{RESET}",
    ":": f"{YELLOW};{RESET}",
    "{": f"{CYAN}{'{'}{RESET}",
    "}": f"{CYAN}{'}'}{RESET}",
    "[": f"{CYAN}{'['}{RESET}",
    "]": f"{CYAN}{']'}{RESET}",
    "\n": f"{RESET}\n",
}
go_syntax = {
    ":=": f"{CYAN}go{RESET}"
}


# syntax analyze
sntxs = {
    "Python": py_syntax,
    "JavaScript": js_syntax,
    "HTML": html_syntax,
    "CSS": css_syntax,
    "JSON": json_syntax,
    "XML": xml_syntax,
    "Java": java_syntax,
    "C++": cpp_syntax, "C": cpp_syntax,
    "Go": go_syntax,
    "Bash": bash_syntax,
}

def replace_substring(match):
    return f'{ORANGE}"{match.group(0)[1:-1]}"{RESET}'
def replace_substring2(match):
    return f"{ORANGE}'{match.group(0)[1:-1]}'{RESET}"
def replace_substring3(match):
    return f"{ORANGE}`{match.group(0)[1:-1]}`{RESET}"

def do_syntax(syntax_type, source_string: str):
    current_syntax = {}
    
    try:
        if syntax_type != "unk":
            current_syntax = sntxs[syntax_type]
    except KeyError:
        current_syntax = {}
    for k, v in current_syntax.items():
        source_string = source_string.replace(k, v)

    if syntax_type != "unk":
        source_string = re.sub(r'"(.*?)"', replace_substring, source_string)
        source_string = re.sub(r"'(.*?)'", replace_substring2, source_string)
        source_string = re.sub(r"`(.*?)`", replace_substring3, source_string)

    return source_string