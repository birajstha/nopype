# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SCALE_TO_MAP_METADATA = Metadata(
    id="6157ff4a2c2b113c867e495b50d10c4ae4df1fc6.boutiques",
    name="ScaleToMap",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class ScaleToMapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `scale_to_map(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def scale_to_map(
    input_file: InputPathType,
    icol: float,
    vcol: float,
    runner: Runner | None = None,
) -> ScaleToMapOutputs:
    """
    Tool to scale values to a color map.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/ScaleToMap.html
    
    Args:
        input_file: Input file in 1D formatted ascii containing node values.
        icol: Index of node index column (-1 if node index is implicit).
        vcol: Index of node value column.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ScaleToMapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SCALE_TO_MAP_METADATA)
    cargs = []
    cargs.append("ScaleToMap")
    cargs.append(execution.input_file(input_file))
    cargs.append(str(icol))
    cargs.append(str(vcol))
    cargs.append("[OPTIONAL_PARAMETERS]")
    ret = ScaleToMapOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SCALE_TO_MAP_METADATA",
    "ScaleToMapOutputs",
    "scale_to_map",
]
