# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

IMG2STDCOORD_METADATA = Metadata(
    id="1960a762fadb169aa80713dfe27f600493a685c4",
    name="img2stdcoord",
)


class Img2stdcoordOutputs(typing.NamedTuple):
    """
    Output object returned when calling `img2stdcoord(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def img2stdcoord(
    coordinate_file: str,
    input_image: InputPathType,
    standard_image: InputPathType | None = None,
    affine_transform: InputPathType | None = None,
    warp_field: InputPathType | None = None,
    prewarp_affine_transform: InputPathType | None = None,
    voxel_flag: bool = False,
    mm_flag: bool = False,
    verbose_flag_1: bool = False,
    verbose_flag_2: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> Img2stdcoordOutputs:
    """
    img2stdcoord by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Transforms image coordinates using standard space transformations.
    
    Args:
        coordinate_file: Filename containing coordinates. If '-' is used,\
            coordinates are read from standard input.
        input_image: Filename of input image.
        standard_image: Filename of standard image.
        affine_transform: Filename of affine transform (e.g.,\
            example_func2standard.mat).
        warp_field: Filename of warp field (e.g.,\
            highres2standard_warp.nii.gz).
        prewarp_affine_transform: Filename of pre-warp affine transform (e.g.,\
            example_func2highres.mat). Default is identity.
        voxel_flag: Input coordinates in voxels (default).
        mm_flag: Input coordinates in mm.
        verbose_flag_1: Verbose output.
        verbose_flag_2: More verbose output.
        help_flag: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Img2stdcoordOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMG2STDCOORD_METADATA)
    cargs = []
    cargs.append("img2stdcoord")
    cargs.append("[OPTIONS]")
    cargs.append(coordinate_file)
    ret = Img2stdcoordOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMG2STDCOORD_METADATA",
    "Img2stdcoordOutputs",
    "img2stdcoord",
]
