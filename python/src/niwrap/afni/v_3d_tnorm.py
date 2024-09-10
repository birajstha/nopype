# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_TNORM_METADATA = Metadata(
    id="8f6fca5ff448969653f833bbe04335be86ac6c0a.boutiques",
    name="3dTnorm",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dTnormOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tnorm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType | None
    """Normalized output dataset"""


def v_3d_tnorm(
    input_dataset: InputPathType,
    prefix: str | None = None,
    norm2: bool = False,
    norm_r: bool = False,
    norm1: bool = False,
    normx: bool = False,
    polort: float | None = None,
    l1fit: bool = False,
    runner: Runner | None = None,
) -> V3dTnormOutputs:
    """
    Normalizes each voxel time series by multiplicative scaling.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dTnorm.html
    
    Args:
        input_dataset: Input dataset (e.g. data.nii).
        prefix: Prefix for the output dataset.
        norm2: L2 normalize (sum of squares = 1).
        norm_r: Normalize so sum of squares = number of time points.
        norm1: L1 normalize (sum of absolute values = 1).
        normx: Scale so max absolute value = 1 (L_infinity norm).
        polort: Detrend with polynomials of order p before normalizing.
        l1fit: Detrend with L1 regression (L2 is default).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTnormOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TNORM_METADATA)
    cargs = []
    cargs.append("3dTnorm")
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if norm2:
        cargs.append("-norm2")
    if norm_r:
        cargs.append("-normR")
    if norm1:
        cargs.append("-norm1")
    if normx:
        cargs.append("-normx")
    if polort is not None:
        cargs.extend([
            "-polort",
            str(polort)
        ])
    if l1fit:
        cargs.append("-L1fit")
    cargs.append(execution.input_file(input_dataset))
    ret = V3dTnormOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(prefix + ".nii") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dTnormOutputs",
    "V_3D_TNORM_METADATA",
    "v_3d_tnorm",
]
