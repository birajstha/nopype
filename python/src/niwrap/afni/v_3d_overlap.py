# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_OVERLAP_METADATA = Metadata(
    id="080fa1f253e1fd652f6d023f571ec3023a3f5882.boutiques",
    name="3dOverlap",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dOverlapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_overlap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brik: OutputPathType
    """BRIK file with count of overlaps at each voxel (if -save is used)"""
    output_head: OutputPathType
    """HEAD file with count of overlaps at each voxel (if -save is used)"""


def v_3d_overlap(
    runner: Runner | None = None,
) -> V3dOverlapOutputs:
    """
    Counts the number of voxels that are nonzero in all input datasets.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dOverlap.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dOverlapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_OVERLAP_METADATA)
    cargs = []
    cargs.append("3dOverlap")
    cargs.append("[OPTIONS]")
    cargs.append("[DATASET1]")
    cargs.append("[DATASET2]")
    ret = V3dOverlapOutputs(
        root=execution.output_file("."),
        output_brik=execution.output_file("[PREFIX]+orig.BRIK"),
        output_head=execution.output_file("[PREFIX]+orig.HEAD"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dOverlapOutputs",
    "V_3D_OVERLAP_METADATA",
    "v_3d_overlap",
]
