import os
import re
from pathlib import Path


def get_datasets(path: str, ext: str):
    return ['None'] + sorted(set([k.stem for k in Path(path).glob(f'*.{ext}') if k.stem != 'put-trainer-datasets-here']), key=natural_keys)

