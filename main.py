import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.dsiplay import Markdown
def to_Markdwon(text):
    text = text.replace('.', ' *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
