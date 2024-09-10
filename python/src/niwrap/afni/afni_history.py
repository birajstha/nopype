# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

AFNI_HISTORY_METADATA = Metadata(
    id="0e5ba13dd26e71c5594c4d9a695c26f20e753d0b.boutiques",
    name="afni_history",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class AfniHistoryOutputs(typing.NamedTuple):
    """
    Output object returned when calling `afni_history(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def afni_history(
    verb_level: int | None = None,
    check_date: str | None = None,
    help_: bool = False,
    history: bool = False,
    list_authors: bool = False,
    list_types: bool = False,
    version: bool = False,
    author: str | None = None,
    level: int | None = None,
    min_level: int | None = None,
    program: str | None = None,
    past_entries: int | None = None,
    past_days: int | None = None,
    past_months: int | None = None,
    past_years: int | None = None,
    type_: str | None = None,
    html_: bool = False,
    dline: bool = False,
    reverse: bool = False,
    show_field: str | None = None,
    show_field_names: bool = False,
    runner: Runner | None = None,
) -> AfniHistoryOutputs:
    """
    Show AFNI updates per user, dates, or levels.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/afni_history.html
    
    Args:
        verb_level: Request verbose output (LEVEL is from 0-6).
        check_date: Check history against given date. If most recent\
            afni_history is older than the passed date, the distribution version\
            might be considered out of date.
        help_: Show help information.
        history: Show this program's history.
        list_authors: Show the list of valid authors.
        list_types: Show the list of valid change types.
        version: Show this program's version.
        author: Restrict output to the given author.
        level: Restrict output to the given level.
        min_level: Restrict output to at least level LEVEL.
        program: Restrict output to the given program.
        past_entries: Restrict output to final ENTRIES entries.
        past_days: Restrict output to the past DAYS days.
        past_months: Restrict output to the past MONTHS months.
        past_years: Restrict output to the past YEARS years.
        type_: Restrict output to the given TYPE (TYPE = 0..5, or strings\
            'NEW_PROG', etc.).
        html_: Add HTML formatting.
        dline: Put a divider line between dates.
        reverse: Reverse the sorting order (sort is by date, author, level,\
            program).
        show_field: Restrict entry output to field FIELD. Valid FIELDs include:\
            all, firstline, day, month, year, date, author, program, level, type,\
            desc, verbtext.
        show_field_names: List valid FIELD names for -show_field.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfniHistoryOutputs`).
    """
    if verb_level is not None and not (0 <= verb_level <= 6): 
        raise ValueError(f"'verb_level' must be between 0 <= x <= 6 but was {verb_level}")
    if level is not None and not (1 <= level <= 5): 
        raise ValueError(f"'level' must be between 1 <= x <= 5 but was {level}")
    if min_level is not None and not (1 <= min_level <= 5): 
        raise ValueError(f"'min_level' must be between 1 <= x <= 5 but was {min_level}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFNI_HISTORY_METADATA)
    cargs = []
    cargs.append("afni_history")
    if verb_level is not None:
        cargs.extend([
            "-verb",
            str(verb_level)
        ])
    if check_date is not None:
        cargs.extend([
            "-check_date",
            check_date
        ])
    if help_:
        cargs.append("-help")
    if history:
        cargs.append("-hist")
    if list_authors:
        cargs.append("-list_authors")
    if list_types:
        cargs.append("-list_types")
    if version:
        cargs.append("-ver")
    if author is not None:
        cargs.extend([
            "-author",
            author
        ])
    if level is not None:
        cargs.extend([
            "-level",
            str(level)
        ])
    if min_level is not None:
        cargs.extend([
            "-min_level",
            str(min_level)
        ])
    if program is not None:
        cargs.extend([
            "-program",
            program
        ])
    if past_entries is not None:
        cargs.extend([
            "-past_entries",
            str(past_entries)
        ])
    if past_days is not None:
        cargs.extend([
            "-past_days",
            str(past_days)
        ])
    if past_months is not None:
        cargs.extend([
            "-past_months",
            str(past_months)
        ])
    if past_years is not None:
        cargs.extend([
            "-past_years",
            str(past_years)
        ])
    if type_ is not None:
        cargs.extend([
            "-type",
            type_
        ])
    if html_:
        cargs.append("-html")
    if dline:
        cargs.append("-dline")
    if reverse:
        cargs.append("-reverse")
    if show_field is not None:
        cargs.extend([
            "-show_field",
            show_field
        ])
    if show_field_names:
        cargs.append("-show_field_names")
    ret = AfniHistoryOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AFNI_HISTORY_METADATA",
    "AfniHistoryOutputs",
    "afni_history",
]
