import os
import re
from pathlib import Path


def atoi(text):
    return int(text) if text.isdigit() else text.lower()


def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]


def clean_path(base_path: str, path: str):
    """"Strips unusual symbols and forcibly builds a path as relative to the intended directory."""
    # TODO: Probably could do with a security audit to guarantee there's no ways this can be bypassed to target an unwanted path.
    # Or swap it to a strict whitelist of [a-zA-Z_0-9]
    path = path.replace('\\', '/').replace('..', '_')
    if base_path is None:
        return path

    return f'{Path(base_path).absolute()}/{path}'

def get_datasets(path: str, ext: str):
    return ['None'] + sorted(
        set([k.stem for k in Path(path).glob(f'*.{ext}') if k.stem != 'put-trainer-datasets-here']), key=natural_keys)
