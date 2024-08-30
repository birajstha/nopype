# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FIRST_ROI_SLICESDIR_METADATA = Metadata(
    id="e88bcb78f430d93578062447bcf9710d9aaf9023",
    name="first_roi_slicesdir",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class FirstRoiSlicesdirOutputs(typing.NamedTuple):
    """
    Output object returned when calling `first_roi_slicesdir(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    t1_slicesdir: OutputPathType
    """Generated slice directory for the input T1 images"""
    label_slicesdir: OutputPathType
    """Generated slice directory for the input label images"""


def first_roi_slicesdir(
    input_t1_images: str,
    input_label_images: str,
    runner: Runner | None = None,
) -> FirstRoiSlicesdirOutputs:
    """
    first_roi_slicesdir by FMRIB Centre, Oxford University.
    
    A utility for generating slice directories for FIRST-ROI.
    
    Args:
        input_t1_images: Input T1-weighted images of the brain\
            (pattern-matched); for example, *_t1.nii.gz.
        input_label_images: Input label images corresponding to the T1 images\
            (pattern-matched); for example, *_L_Hipp_first.nii.gz.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FirstRoiSlicesdirOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIRST_ROI_SLICESDIR_METADATA)
    cargs = []
    cargs.append("first_roi_slicesdir")
    cargs.append(input_t1_images)
    cargs.append(input_label_images)
    ret = FirstRoiSlicesdirOutputs(
        root=execution.output_file("."),
        t1_slicesdir=execution.output_file(f"{input_t1_images}_slicesdir", optional=True),
        label_slicesdir=execution.output_file(f"{input_label_images}_slicesdir", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIRST_ROI_SLICESDIR_METADATA",
    "FirstRoiSlicesdirOutputs",
    "first_roi_slicesdir",
]
