# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BET2_METADATA = Metadata(
    id="6bcfc8bdc0fc44adf89ff8cf7019e09f35b72640.boutiques",
    name="bet2",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class Bet2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `bet2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_mask: OutputPathType
    """Binary brain mask output (if mask flag is set)"""
    output_skull: OutputPathType
    """Approximate skull image output (if skull flag is set)"""
    output_mesh: OutputPathType
    """Brain surface mesh output in VTK format (if mesh flag is set)"""
    output_overlay: OutputPathType
    """Brain surface outline overlaid onto original image (if outline flag is
    set)"""


def bet2(
    input_fileroot: str,
    output_fileroot: str,
    fractional_intensity: float | None = None,
    vertical_gradient: float | None = None,
    center_of_gravity: list[float] | None = None,
    outline_flag: bool = False,
    mask_flag: bool = False,
    skull_flag: bool = False,
    no_output_flag: bool = False,
    mesh_flag: bool = False,
    head_radius: float | None = None,
    smooth_factor: float | None = None,
    threshold_flag: bool = False,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> Bet2Outputs:
    """
    Automated brain extraction tool for FSL.
    
    Author: FMRIB Analysis Group, Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/BET
    
    Args:
        input_fileroot: Input file root (e.g. img).
        output_fileroot: Output file root (e.g. img_bet).
        fractional_intensity: Fractional intensity threshold (0->1);\
            default=0.5; smaller values give larger brain outline estimates.
        vertical_gradient: Vertical gradient in fractional intensity threshold\
            (-1->1); default=0; positive values give larger brain outline at\
            bottom, smaller at top.
        center_of_gravity: The xyz coordinates of the center of gravity\
            (voxels, not mm) of initial mesh surface. Must have exactly three\
            numerical entries in the list (3-vector).
        outline_flag: Generate brain surface outline overlaid onto original\
            image.
        mask_flag: Generate binary brain mask.
        skull_flag: Generate approximate skull image.
        no_output_flag: Don't generate segmented brain image output.
        mesh_flag: Generate brain surface as mesh in vtk format.
        head_radius: Head radius (mm not voxels); initial surface sphere is set\
            to half of this.
        smooth_factor: Smoothness factor; default=1; values smaller than 1\
            produce more detailed brain surface, values larger than one produce\
            smoother, less detailed surface.
        threshold_flag: Apply thresholding to segmented brain image and mask.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display help message and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Bet2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BET2_METADATA)
    cargs = []
    cargs.append("bet2")
    cargs.append(input_fileroot)
    cargs.append(output_fileroot)
    if fractional_intensity is not None:
        cargs.extend([
            "-f",
            str(fractional_intensity)
        ])
    if vertical_gradient is not None:
        cargs.extend([
            "-g",
            str(vertical_gradient)
        ])
    if center_of_gravity is not None:
        cargs.extend([
            "-c",
            *map(str, center_of_gravity)
        ])
    if outline_flag:
        cargs.append("-o")
    if mask_flag:
        cargs.append("-m")
    if skull_flag:
        cargs.append("-s")
    if no_output_flag:
        cargs.append("-n")
    if mesh_flag:
        cargs.append("-e")
    if head_radius is not None:
        cargs.extend([
            "-r",
            str(head_radius)
        ])
    if smooth_factor is not None:
        cargs.extend([
            "-w",
            str(smooth_factor)
        ])
    if threshold_flag:
        cargs.append("-t")
    if verbose_flag:
        cargs.append("-v")
    if help_flag:
        cargs.append("-h")
    ret = Bet2Outputs(
        root=execution.output_file("."),
        output_mask=execution.output_file(output_fileroot + "_mask.nii.gz"),
        output_skull=execution.output_file(output_fileroot + "_skull.nii.gz"),
        output_mesh=execution.output_file(output_fileroot + "_mesh.vtk"),
        output_overlay=execution.output_file(output_fileroot + "_overlay.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BET2_METADATA",
    "Bet2Outputs",
    "bet2",
]
