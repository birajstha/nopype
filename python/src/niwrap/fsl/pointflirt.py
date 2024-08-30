# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

POINTFLIRT_METADATA = Metadata(
    id="ee1b22cf597ec9ee03dbc9e66058c8eb17f83276",
    name="pointflirt",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class PointflirtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `pointflirt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_matrix_file: OutputPathType | None
    """Affine matrix output file"""


def pointflirt(
    invol_coords: InputPathType,
    refvol_coords: InputPathType,
    out_matrix: InputPathType | None = None,
    use_vox: bool = False,
    vol_input: InputPathType | None = None,
    vol_ref: InputPathType | None = None,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> PointflirtOutputs:
    """
    pointflirt by Mark Jenkinson, University of Oxford.
    
    A tool to align point coordinates between volumes and compute affine
    transformation matrices.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/
    
    Args:
        invol_coords: Filename of input volume coordinates.
        refvol_coords: Filename of reference volume coordinates.
        out_matrix: Filename of affine matrix output.
        use_vox: Use voxel coordinates, not mm, for input.
        vol_input: Filename of input volume (needed for --vox option).
        vol_ref: Filename of reference volume (needed for --vox option).
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PointflirtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(POINTFLIRT_METADATA)
    cargs = []
    cargs.append("pointflirt")
    cargs.append("-i")
    cargs.append(execution.input_file(invol_coords))
    cargs.append("-r")
    cargs.append(execution.input_file(refvol_coords))
    cargs.append("-o")
    if out_matrix is not None:
        cargs.extend(["-o", execution.input_file(out_matrix)])
    if use_vox:
        cargs.append("--vox")
    if vol_input is not None:
        cargs.extend(["--invol", execution.input_file(vol_input)])
    if vol_ref is not None:
        cargs.extend(["--refvol", execution.input_file(vol_ref)])
    if verbose_flag:
        cargs.append("-v")
    ret = PointflirtOutputs(
        root=execution.output_file("."),
        output_matrix_file=execution.output_file(f"{pathlib.Path(out_matrix).name}", optional=True) if out_matrix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "POINTFLIRT_METADATA",
    "PointflirtOutputs",
    "pointflirt",
]
