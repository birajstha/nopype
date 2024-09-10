# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_2PERM_METADATA = Metadata(
    id="6a8df98c1103f9bb4e763f85c6628c97760f69ff.boutiques",
    name="2perm",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V2permOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_2perm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    file_a: OutputPathType | None
    """First subset output file"""
    file_b: OutputPathType | None
    """Second subset output file"""


def v_2perm(
    bottom_int: float,
    top_int: float,
    prefix: str | None = None,
    comma: bool = False,
    subset1_size: float | None = None,
    subset2_size: float | None = None,
    runner: Runner | None = None,
) -> V2permOutputs:
    """
    Generates two random non-overlapping subsets of a given set of integers.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/2perm.html
    
    Args:
        bottom_int: Bottom integer of the range.
        top_int: Top integer of the range.
        prefix: Prefix for output files (default 'AFNIroolz').
        comma: Write each file as a single row of comma-separated numbers.
        subset1_size: Size of the first subset (optional, default is half the\
            range).
        subset2_size: Size of the second subset (optional, default is half the\
            range).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V2permOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_2PERM_METADATA)
    cargs = []
    cargs.append("2perm")
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if comma:
        cargs.append("-comma")
    cargs.append(str(bottom_int))
    cargs.append(str(top_int))
    if subset1_size is not None:
        cargs.append(str(subset1_size))
    if subset2_size is not None:
        cargs.append(str(subset2_size))
    ret = V2permOutputs(
        root=execution.output_file("."),
        file_a=execution.output_file(prefix + "_A") if (prefix is not None) else None,
        file_b=execution.output_file(prefix + "_B") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V2permOutputs",
    "V_2PERM_METADATA",
    "v_2perm",
]
