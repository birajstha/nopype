# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DMASK_SVD_METADATA = Metadata(
    id="befb278fb0ea3598cbac3ecadbabb48616183c88.boutiques",
    name="3dmaskSVD",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dmaskSvdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmask_svd(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    svd_output: OutputPathType
    """Singular vector output redirected to this file"""


def v_3dmask_svd(
    input_dataset: InputPathType,
    runner: Runner | None = None,
) -> V3dmaskSvdOutputs:
    """
    Computes the principal singular vector of the time series vectors extracted from
    the input dataset over the input mask.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dmaskSVD.html
    
    Args:
        input_dataset: Input dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dmaskSvdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMASK_SVD_METADATA)
    cargs = []
    cargs.append("3dmaskSVD")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(input_dataset))
    ret = V3dmaskSvdOutputs(
        root=execution.output_file("."),
        svd_output=execution.output_file("../stdout"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dmaskSvdOutputs",
    "V_3DMASK_SVD_METADATA",
    "v_3dmask_svd",
]
