# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MAKE_STIM_TIMES_PY_METADATA = Metadata(
    id="7bbdaef6750c66049070f616d1d66b8b6d4662b8.boutiques",
    name="make_stim_times.py",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class MakeStimTimesPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_stim_times_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_stim_times_01: OutputPathType
    """Output stim_times file for first stimulus class"""
    out_stim_times_02: OutputPathType
    """Output stim_times file for second stimulus class"""
    out_stim_times_03: OutputPathType
    """Output stim_times file for third stimulus class"""


def make_stim_times_py(
    files: list[InputPathType],
    prefix: str,
    tr: float,
    nruns: float,
    nt_: float,
    run_trs: list[float] | None = None,
    offset: float | None = None,
    labels: list[str] | None = None,
    no_consec_events: bool = False,
    amplitudes: bool = False,
    show_valid_opts: bool = False,
    verbose: float | None = None,
    runner: Runner | None = None,
) -> MakeStimTimesPyOutputs:
    """
    Convert a set of 0/1 stim files into a set of stim_times files, or convert
    real-valued files into those for use with -stim_times_AM2.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/make_stim_times.py.html
    
    Args:
        files: Specify stim files.
        prefix: Output prefix for files.
        tr: TR time, in seconds.
        nruns: Number of runs.
        nt_: Number of TRs per run.
        run_trs: Specify TRs per run, if they differ.
        offset: Add OFFSET to all output times.
        labels: Provide labels for filenames.
        no_consec_events: Do not allow consecutive events.
        amplitudes: Marry times with amplitudes.
        show_valid_opts: Output all options.
        verbose: Provide verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeStimTimesPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_STIM_TIMES_PY_METADATA)
    cargs = []
    cargs.append("make_stim_times.py")
    cargs.extend([execution.input_file(f) for f in files])
    cargs.extend([
        "-prefix",
        prefix
    ])
    cargs.extend([
        "-tr",
        str(tr)
    ])
    cargs.extend([
        "-nruns",
        str(nruns)
    ])
    cargs.extend([
        "-nt",
        str(nt_)
    ])
    if run_trs is not None:
        cargs.extend(map(str, run_trs))
    if offset is not None:
        cargs.extend([
            "-offset",
            str(offset)
        ])
    if labels is not None:
        cargs.extend([
            "-labels",
            *labels
        ])
    if no_consec_events:
        cargs.append("-no_consec")
    if amplitudes:
        cargs.append("-amplitudes")
    if show_valid_opts:
        cargs.append("-show_valid_opts")
    if verbose is not None:
        cargs.extend([
            "-verb",
            str(verbose)
        ])
    ret = MakeStimTimesPyOutputs(
        root=execution.output_file("."),
        out_stim_times_01=execution.output_file(prefix + ".01.1D"),
        out_stim_times_02=execution.output_file(prefix + ".02.1D"),
        out_stim_times_03=execution.output_file(prefix + ".03.1D"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAKE_STIM_TIMES_PY_METADATA",
    "MakeStimTimesPyOutputs",
    "make_stim_times_py",
]
