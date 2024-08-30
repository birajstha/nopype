# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURFACE_FDR_METADATA = Metadata(
    id="31a062104599d7480e7d63292f0becaf39059e33",
    name="surface_fdr",
)


class SurfaceFdrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_fdr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    pvals_vtk: OutputPathType
    """Output VTK file with corrected p-values"""
    fthresh_vtk: OutputPathType
    """Output VTK file with FDR thresholded values"""
    nifti_images: OutputPathType
    """Additional output NIFTI images"""


def surface_fdr(
    input_vtk: InputPathType,
    runner: Runner | None = None,
) -> SurfaceFdrOutputs:
    """
    surface_fdr by Unknown.
    
    Tool to calculate surface FDR correction for vertex analysis.
    
    Args:
        input_vtk: Input VTK file from vertex analysis.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceFdrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_FDR_METADATA)
    cargs = []
    cargs.append("surface_fdr")
    cargs.append(execution.input_file(input_vtk))
    ret = SurfaceFdrOutputs(
        root=execution.output_file("."),
        pvals_vtk=execution.output_file(f"{pathlib.Path(input_vtk).name}_pvals.vtk"),
        fthresh_vtk=execution.output_file(f"{pathlib.Path(input_vtk).name}_Fthresh.vtk"),
        nifti_images=execution.output_file(f"{pathlib.Path(input_vtk).name}_*", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_FDR_METADATA",
    "SurfaceFdrOutputs",
    "surface_fdr",
]
