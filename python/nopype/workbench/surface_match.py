# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.742818

import typing

from ..styxdefs import *


SURFACE_MATCH_METADATA = Metadata(
    id="0f2c13241ff42adc1c3024da16b03492b5cbd3a3",
    name="surface-match",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceMatchOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_match(...)`.
    """


def surface_match(
    runner: Runner,
    match_surface_file: InputPathType,
    input_surface_file: InputPathType,
    output_surface_name: str,
) -> SurfaceMatchOutputs:
    """
    SURFACE MATCH.
    
    The Input Surface File will be transformed so that its coordinate ranges
    (bounding box) match that of the Match Surface File
    
    Args:
        runner: Command runner
        match_surface_file: Match (Reference) Surface
        input_surface_file: File containing surface that will be transformed
        output_surface_name: Surface File after transformation
    Returns:
        NamedTuple of outputs (described in `SurfaceMatchOutputs`).
    """
    execution = runner.start_execution(SURFACE_MATCH_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-match")
    cargs.append(execution.input_file(match_surface_file))
    cargs.append(execution.input_file(input_surface_file))
    cargs.append(output_surface_name)
    ret = SurfaceMatchOutputs(
    )
    execution.run(cargs)
    return ret
