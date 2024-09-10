# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

IMSTACK_METADATA = Metadata(
    id="0b64ae08b24b469a2c1c73101d04e4171b55c105.boutiques",
    name="imstack",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class ImstackOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imstack(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_data_file: OutputPathType | None
    """Output data file"""
    output_header_file: OutputPathType | None
    """Output header file"""


def imstack(
    image_files: list[InputPathType],
    data_type: typing.Literal["short", "float"] | None = None,
    output_prefix: str | None = None,
    runner: Runner | None = None,
) -> ImstackOutputs:
    """
    Stacks up a set of 2D images into one big file (a la MGH).
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/imstack.html
    
    Args:
        image_files: Input image filenames.
        data_type: Converts the output data file to be 'type', which is either\
            'short' or 'float'. The default type is the type of the first image.
        output_prefix: Names the output files to be 'name'.b'type' and\
            'name'.hdr. The default name is 'obi-wan-kenobi'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImstackOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMSTACK_METADATA)
    cargs = []
    cargs.append("imstack")
    cargs.extend([execution.input_file(f) for f in image_files])
    if data_type is not None:
        cargs.extend([
            "-datum",
            data_type
        ])
    if output_prefix is not None:
        cargs.extend([
            "-prefix",
            output_prefix
        ])
    ret = ImstackOutputs(
        root=execution.output_file("."),
        output_data_file=execution.output_file(output_prefix + ".b" + data_type) if (output_prefix is not None and data_type is not None) else None,
        output_header_file=execution.output_file(output_prefix + ".hdr") if (output_prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMSTACK_METADATA",
    "ImstackOutputs",
    "imstack",
]
