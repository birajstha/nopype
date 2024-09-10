# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

IMRM_METADATA = Metadata(
    id="4baaab2f1f3694642eaa2ba934022c444a043ffa.boutiques",
    name="imrm",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class ImrmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imrm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def imrm(
    images_to_remove: list[str],
    runner: Runner | None = None,
) -> ImrmOutputs:
    """
    Remove specified image files.
    
    Author: Oxford Centre for Functional MRI of the Brain (FMRIB)
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/
    
    Args:
        images_to_remove: List of image names to remove. Filenames can be\
            basenames or full names.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImrmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMRM_METADATA)
    cargs = []
    cargs.append("/usr/local/fsl/bin/imrm")
    cargs.extend(images_to_remove)
    ret = ImrmOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMRM_METADATA",
    "ImrmOutputs",
    "imrm",
]
