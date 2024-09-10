# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_NORMALS_METADATA = Metadata(
    id="e5edba049b1a222e8e3f9b17a63ac0db98dce59e.boutiques",
    name="surface-normals",
    package="workbench",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceNormalsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_normals(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the normal vectors"""


def surface_normals(
    surface: InputPathType,
    metric_out: str,
    runner: Runner | None = None,
) -> SurfaceNormalsOutputs:
    """
    Output vertex normals as metric file.
    
    Computes the normal vectors of the surface file, and outputs them as a 3
    column metric file.
    
    Author: Washington University School of Medicin
    
    Args:
        surface: the surface to output the normals of.
        metric_out: the normal vectors.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceNormalsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_NORMALS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-normals")
    cargs.append(execution.input_file(surface))
    cargs.append(metric_out)
    ret = SurfaceNormalsOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(metric_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_NORMALS_METADATA",
    "SurfaceNormalsOutputs",
    "surface_normals",
]
