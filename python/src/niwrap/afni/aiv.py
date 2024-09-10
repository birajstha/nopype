# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

AIV_METADATA = Metadata(
    id="578b6d8b42b586e61d17c91fc62ad157cd5c12cf.boutiques",
    name="aiv",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class AivOutputs(typing.NamedTuple):
    """
    Output object returned when calling `aiv(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def aiv(
    input_images: list[InputPathType],
    verbose: bool = False,
    quiet: bool = False,
    title: str | None = None,
    port: float | None = None,
    pad: str | None = None,
    runner: Runner | None = None,
) -> AivOutputs:
    """
    AFNI Image Viewer program. Shows the 2D images on the command line in an
    AFNI-like image viewer.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/aiv.html
    
    Args:
        input_images: Input image files (e.g., img1.jpg, img2.bmp).
        verbose: Print out the image filenames for progress tracking.
        quiet: Run the program in quiet mode.
        title: Specify the window title.
        port: Listen to TCP/IP port for incoming images.
        pad: Pad all input images to be the same size.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AivOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AIV_METADATA)
    cargs = []
    cargs.append("aiv")
    if verbose:
        cargs.append("-v")
    if quiet:
        cargs.append("-q")
    if title is not None:
        cargs.extend([
            "-title",
            title
        ])
    if port is not None:
        cargs.extend([
            "-p",
            str(port)
        ])
    if pad is not None:
        cargs.extend([
            "-pad",
            pad
        ])
    cargs.extend([execution.input_file(f) for f in input_images])
    ret = AivOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AIV_METADATA",
    "AivOutputs",
    "aiv",
]
