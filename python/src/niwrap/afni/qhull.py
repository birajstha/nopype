# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

QHULL_METADATA = Metadata(
    id="b132d50e05aa63af1c8988eaaa09fbfdccc9c0a1.boutiques",
    name="qhull",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class QhullOutputs(typing.NamedTuple):
    """
    Output object returned when calling `qhull(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_results: OutputPathType
    """Output file with the specified results."""


def qhull(
    runner: Runner | None = None,
) -> QhullOutputs:
    """
    Tool to compute convex hulls and related structures.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/qhull.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `QhullOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(QHULL_METADATA)
    cargs = []
    cargs.append("qhull")
    cargs.append("[OPTIONS]")
    cargs.append("[OUTPUT_OPTIONS]")
    ret = QhullOutputs(
        root=execution.output_file("."),
        output_results=execution.output_file("[OUTPUT_FILE].txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "QHULL_METADATA",
    "QhullOutputs",
    "qhull",
]
