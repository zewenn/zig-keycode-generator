from typing import *
from . import resources
import copy

T = TypeVar("T", str, list[str])
DSET = dict[int, T]
void = type[None]

DATASET: DSET | None = None

MENUM = 0
MSTRUCT = 1
MLIST = 2


def use_dataset(dataset: DSET) -> void:
    global DATASET
    DATASET = dataset


def replace_keyword_keycode(template: resources.Template, kword: str, kcode: int) -> str:
    fkw = kword
    
    if (not kword.isalpha()):
        if (len(kword) == 1):
            fkw = resources.BACKWARDS_TABLE[ord(kword)]
    
    return template.template.replace(f"${fkw},", f"{kcode},")


def generate(name: str, use: Literal[0, 1, 2]) -> resources.Template:
    template: resources.Template = resources.get_template(name, use)
    kwords_remaining = copy.deepcopy(resources.KEYWORDS)


    for kcode, kword in DATASET.items():
        keywords = kword if isinstance(kword, list) else [kword]

        for keyword in keywords:
            # if (keyword not in kwords_remaining):
            #     continue
            
            print(f"Replacing [${keyword}] with [{kcode}]")
            template.template = replace_keyword_keycode(
                template,
                keyword,
                kcode,
            )
            
    for kword in kwords_remaining:
        template.template = replace_keyword_keycode(
            template,
            kword,
            "null"
        )
    
    return template

