#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# >>
#   python-clearlog, 2020
#   - blake
# <<

import sys
from typing import NamedTuple
from collections import namedtuple
from typing import Dict

# time.time_ns() & 2**36 - 1
# https://docs.python.org/3/library/dataclasses.html


class What(NamedTuple):
    a: int
    b: str

    def __clearlog__(self) -> Dict[str, str]:
        return self._asdict()


w = What(0, "blake")
print(w)
