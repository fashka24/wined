# spell checking

import re, difflib

lang_paths = [
    "langs/en.txt",
    "langs/ru.txt",
    "langs/fr.txt",
    "langs/de.txt",
]

def get_langs():
    delimiter_pattern = r"[;\n]"

    lang_sources = []
    for path in lang_paths:
        with open(path, 'r', encoding='utf-8') as f:
            lang_sources.append(f.read())
            f.close()
    lang_sources_result = []
    for lang_source in lang_sources:
        lang_source = lang_source.replace("\n", "")
        lang_sources_result.append(re.split(delimiter_pattern, lang_source))

    return lang_sources_result

def do_spell_check(text, langs=["no"]):
    if langs == ["no"]:
        langs = get_langs()
    result = {}
    ignores = []
    delimiter_pattern = r"[,;_\?!\"\'.\#\@\n\:)({}]"

    text_list = text.split(" ")
    for lang in langs:
        for text_block in text_list:
            text_block = text_block.lower()
            text_block = re.split(delimiter_pattern, text_block)
            # print("3", text_block) dev log
            for txt_p in text_block:
                if not txt_p in lang and not txt_p in ignores:
                    # print("2", txt_p) dev log
                    similar_words = difflib.get_close_matches(txt_p, lang, n=3, cutoff=0.633)
                    # print("1", txt_p) dev log
                    if len(similar_words) != 0:
                        result.update({txt_p: similar_words})
                else:
                    ignores.append(txt_p)
    return result