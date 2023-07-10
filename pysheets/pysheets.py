"""
file: pysheets.py
author: Gavin Harrold
desc: CLI for creating Google spreadsheets using Python and Google Sheets API
"""

import typer
from typing import List
from pysheets import __app_name__, __version__

cli = typer.Typer()
