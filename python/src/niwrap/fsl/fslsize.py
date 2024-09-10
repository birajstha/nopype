# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLSIZE_METADATA = Metadata(
    id="0aa7e6fbb81dbdb0e85b1f0d56cc9743a42d862e.boutiques",
    name="fslsize",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FslsizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslsize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslsize(
    input_file: InputPathType,
    short_format_flag: bool = False,
    runner: Runner | None = None,
) -> FslsizeOutputs:
    """
    Tool to output the size of an image file in FSL.
    
    Author: Oxford Centre for Functional MRI of the Brain (FMRIB)
    
    Args:
        input_file: Input image file.
        short_format_flag: Output using short format (one line).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslsizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLSIZE_METADATA)
    cargs = []
    cargs.append("fslsize")
    cargs.append(execution.input_file(input_file))
    if short_format_flag:
        cargs.append("-s")
    ret = FslsizeOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLSIZE_METADATA",
    "FslsizeOutputs",
    "fslsize",
]
