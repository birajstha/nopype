# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

AFNI_RUN_R_METADATA = Metadata(
    id="7592c47db94b5bbd2a7361de44c34b673e6ded70.boutiques",
    name="afni_run_R",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class AfniRunROutputs(typing.NamedTuple):
    """
    Output object returned when calling `afni_run_r(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def afni_run_r(
    r_script: InputPathType,
    r_args: list[str],
    runner: Runner | None = None,
) -> AfniRunROutputs:
    """
    Run an R script with the specified arguments.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/afni_run_R.html
    
    Args:
        r_script: R script to be executed.
        r_args: Arguments to be passed to the R script.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfniRunROutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFNI_RUN_R_METADATA)
    cargs = []
    cargs.append("afni_run_R")
    cargs.append(execution.input_file(r_script))
    cargs.extend(r_args)
    ret = AfniRunROutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AFNI_RUN_R_METADATA",
    "AfniRunROutputs",
    "afni_run_r",
]
