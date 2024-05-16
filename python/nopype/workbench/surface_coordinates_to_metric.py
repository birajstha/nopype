# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.684674

import typing

from ..styxdefs import *


SURFACE_COORDINATES_TO_METRIC_METADATA = Metadata(
    id="d1bafb9bfeb6ff7bad4caed14df1ad62e14a5cab",
    name="surface-coordinates-to-metric",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceCoordinatesToMetricOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_coordinates_to_metric(...)`.
    """
    metric_out: OutputPathType
    """the output metric"""


def surface_coordinates_to_metric(
    runner: Runner,
    surface: InputPathType,
    metric_out: InputPathType,
) -> SurfaceCoordinatesToMetricOutputs:
    """
    MAKE METRIC FILE OF SURFACE COORDINATES.
    
    Puts the coordinates of the surface into a 3-map metric file, as x, y, z.
    
    Args:
        runner: Command runner
        surface: the surface to use the coordinates of
        metric_out: the output metric
    Returns:
        NamedTuple of outputs (described in `SurfaceCoordinatesToMetricOutputs`).
    """
    execution = runner.start_execution(SURFACE_COORDINATES_TO_METRIC_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-coordinates-to-metric")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_out))
    ret = SurfaceCoordinatesToMetricOutputs(
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret
