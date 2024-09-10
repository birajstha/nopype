# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__CLIP_VOLUME_METADATA = Metadata(
    id="bda555156807096282bbe08895523e042aacf8d6.boutiques",
    name="@clip_volume",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class VClipVolumeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__clip_volume(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_clipped_volume: OutputPathType | None
    """Output clipped or cropped volume"""
    output_followers: OutputPathType | None
    """Output for follower datasets after clipping/cropping"""


def v__clip_volume(
    input_volume: InputPathType,
    output_prefix: str | None = None,
    runner: Runner | None = None,
) -> VClipVolumeOutputs:
    """
    A tool to clip regions of a volume in various ways, such as above/below certain
    coordinates or within a specified box.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@clip_volume.html
    
    Args:
        input_volume: Volume to clip.
        output_prefix: Output prefix for the resultant volume. Default is the\
            input prefix with _clp suffixed to it.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VClipVolumeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__CLIP_VOLUME_METADATA)
    cargs = []
    cargs.append("@clip_volume")
    cargs.append("-input")
    cargs.append(execution.input_file(input_volume))
    cargs.append("[CLIPPING_OPTIONS]")
    cargs.append("[LOGIC_OPTIONS]")
    cargs.append("[CROP_OPTIONS]")
    cargs.append("-prefix")
    if output_prefix is not None:
        cargs.extend([
            "-prefix",
            output_prefix
        ])
    ret = VClipVolumeOutputs(
        root=execution.output_file("."),
        output_clipped_volume=execution.output_file(output_prefix + "_clp.nii.gz") if (output_prefix is not None) else None,
        output_followers=execution.output_file(output_prefix + "_follow_clp.nii.gz") if (output_prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VClipVolumeOutputs",
    "V__CLIP_VOLUME_METADATA",
    "v__clip_volume",
]
