# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_CONFORMIST_METADATA = Metadata(
    id="5e9076879c0dd63ed26e34aa942466a7983ce46c.boutiques",
    name="3dConformist",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dConformistOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_conformist(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """Zero padded output dataset files"""


def v_3d_conformist(
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> V3dConformistOutputs:
    """
    Program to conform a collection of datasets to the same size by zero padding.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dConformist.html
    
    Args:
        input_files: Input datasets to be zero padded to the same size.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dConformistOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_CONFORMIST_METADATA)
    cargs = []
    cargs.append("3dConformist")
    cargs.extend([execution.input_file(f) for f in input_files])
    ret = V3dConformistOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dConformistOutputs",
    "V_3D_CONFORMIST_METADATA",
    "v_3d_conformist",
]
