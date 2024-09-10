# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_BLUR_IN_MASK_METADATA = Metadata(
    id="431d35050cc5bb482fdcbc3aafdcf364c2c9bc0e.boutiques",
    name="3dBlurInMask",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dBlurInMaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_blur_in_mask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output dataset"""


def v_3d_blur_in_mask(
    input_file: InputPathType,
    output_prefix: str,
    fwhm: float,
    fwhm_dataset: InputPathType | None = None,
    mask: InputPathType | None = None,
    multi_mask: InputPathType | None = None,
    automask: bool = False,
    preserve: bool = False,
    quiet: bool = False,
    float_: bool = False,
    fwhm_xyz: list[float] | None = None,
    runner: Runner | None = None,
) -> V3dBlurInMaskOutputs:
    """
    Blurs a dataset spatially inside a mask.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dBlurInMask.html
    
    Args:
        input_file: Dataset to be smoothed and output.
        output_prefix: Prefix for output dataset.
        fwhm: Amount of smoothness to add to the dataset (in mm).
        fwhm_dataset: Dataset containing the amount of smoothness for each\
            voxel.
        mask: Mask dataset for blurring; voxels NOT in the mask will be zeroed\
            in the output.
        multi_mask: Multi-mask dataset; each distinct nonzero value is treated\
            as a separate mask.
        automask: Create an automask from the input dataset.
        preserve: Preserve original values in the dataset outside the mask.
        quiet: Don't be verbose with progress reports.
        float_: Save dataset as floats.
        fwhm_xyz: Add different amounts of smoothness in the 3 spatial\
            directions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dBlurInMaskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_BLUR_IN_MASK_METADATA)
    cargs = []
    cargs.append("3dBlurInMask")
    cargs.append(execution.input_file(input_file))
    cargs.append(output_prefix)
    cargs.extend([
        "-FWHM",
        str(fwhm)
    ])
    if fwhm_dataset is not None:
        cargs.extend([
            "-FWHMdset",
            execution.input_file(fwhm_dataset)
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if multi_mask is not None:
        cargs.extend([
            "-Mmask",
            execution.input_file(multi_mask)
        ])
    if automask:
        cargs.append("-automask")
    if preserve:
        cargs.append("-preserve")
    if quiet:
        cargs.append("-quiet")
    if float_:
        cargs.append("-float")
    if fwhm_xyz is not None:
        cargs.extend([
            "-FWHMxyz",
            *map(str, fwhm_xyz)
        ])
    ret = V3dBlurInMaskOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_prefix),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dBlurInMaskOutputs",
    "V_3D_BLUR_IN_MASK_METADATA",
    "v_3d_blur_in_mask",
]
