import os
import re
from pathlib import Path


def atoi(text):
    return int(text) if text.isdigit() else text.lower()


def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]


def get_datasets(path: str, ext: str):
    return ['None'] + sorted(
        set([k.stem for k in Path(path).glob(f'*.{ext}') if k.stem != 'put-trainer-datasets-here']), key=natural_keys)
