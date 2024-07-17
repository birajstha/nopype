# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_FLOAT_FIX_METADATA = Metadata(
    id="c2eaea29a910aae1188280911225bba330f85610",
    name="@float_fix",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="example/float_fix:latest",
)


class FloatFixOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_float_fix(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def _float_fix(
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> FloatFixOutputs:
    """
    @float_fix by Gang Chen, Ziad Saad.
    
    Check whether the input files have any IEEE floating point numbers for
    illegal values: infinities and not-a-number (NaN) values.
    
    More information: https://example.com/float_fix_tool
    
    Args:
        input_files: Input files to be checked for illegal IEEE floating point\
            values. Wildcards can be used, but filenames must end with .HEAD.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FloatFixOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(_FLOAT_FIX_METADATA)
    cargs = []
    cargs.append("@float_fix")
    cargs.extend([execution.input_file(f) for f in input_files])
    ret = FloatFixOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FloatFixOutputs",
    "_FLOAT_FIX_METADATA",
    "_float_fix",
]
