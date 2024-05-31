# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURFACE_GENERATE_INFLATED_METADATA = Metadata(
    id="c1c87a04abf811cbd213063e906175a55c1fe53c",
    name="surface-generate-inflated",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceGenerateInflatedOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_generate_inflated(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    inflated_surface_out: OutputPathType
    """the output inflated surface"""
    very_inflated_surface_out: OutputPathType
    """the output very inflated surface"""


def surface_generate_inflated(
    anatomical_surface_in: InputPathType,
    inflated_surface_out: InputPathType,
    very_inflated_surface_out: InputPathType,
    opt_iterations_scale_iterations_scale_value: float | int | None = None,
    runner: Runner = None,
) -> SurfaceGenerateInflatedOutputs:
    """
    surface-generate-inflated by Washington University School of Medicin.
    
    Surface generate inflated.
    
    Generate inflated and very inflated surfaces. The output surfaces are
    'matched' (have same XYZ range) to the anatomical surface. In most cases, an
    iterations-scale of 1.0 (default) is sufficient. However, if the surface
    contains a large number of vertices (150,000), try an iterations-scale of
    2.5.
    
    Args:
        anatomical_surface_in: the anatomical surface
        inflated_surface_out: the output inflated surface
        very_inflated_surface_out: the output very inflated surface
        opt_iterations_scale_iterations_scale_value: optional iterations
            scaling: iterations-scale value
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `SurfaceGenerateInflatedOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_GENERATE_INFLATED_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-generate-inflated")
    cargs.append(execution.input_file(anatomical_surface_in))
    cargs.append(execution.input_file(inflated_surface_out))
    cargs.append(execution.input_file(very_inflated_surface_out))
    if opt_iterations_scale_iterations_scale_value is not None:
        cargs.extend(["-iterations-scale", str(opt_iterations_scale_iterations_scale_value)])
    ret = SurfaceGenerateInflatedOutputs(
        root=execution.output_file("."),
        inflated_surface_out=execution.output_file(f"{pathlib.Path(inflated_surface_out).name}"),
        very_inflated_surface_out=execution.output_file(f"{pathlib.Path(very_inflated_surface_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_GENERATE_INFLATED_METADATA",
    "SurfaceGenerateInflatedOutputs",
    "surface_generate_inflated",
]
