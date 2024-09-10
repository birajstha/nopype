# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_NWARP_FUNCS_METADATA = Metadata(
    id="06f5d93900bb791a4c4526f40c403bbfd24380ac.boutiques",
    name="3dNwarpFuncs",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dNwarpFuncsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_nwarp_funcs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """The output dataset with the computed functions."""


def v_3d_nwarp_funcs(
    input_warp: InputPathType,
    output_prefix: str,
    bulk_flag: bool = False,
    shear_flag: bool = False,
    vorticity_flag: bool = False,
    all_flag: bool = False,
    runner: Runner | None = None,
) -> V3dNwarpFuncsOutputs:
    """
    Compute functions of 3D warp displacements, such as bulk volume change, shear
    energy, and vorticity energy.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dNwarpFuncs.html
    
    Args:
        input_warp: 'www' is the name of the 3D warp dataset (mandatory\
            option).
        output_prefix: 'ppp' is the name of the new output dataset.
        bulk_flag: Compute the (fractional) bulk volume change (Jacobian\
            determinant minus 1).
        shear_flag: Compute the shear energy.
        vorticity_flag: Compute the vorticity energy.
        all_flag: Compute all 3 functions: bulk, shear, and vorticity.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dNwarpFuncsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_NWARP_FUNCS_METADATA)
    cargs = []
    cargs.append("3dNwarpFuncs")
    cargs.extend([
        "-nwarp",
        execution.input_file(input_warp)
    ])
    cargs.extend([
        "-prefix",
        output_prefix
    ])
    if bulk_flag:
        cargs.append("-bulk")
    if shear_flag:
        cargs.append("-shear")
    if vorticity_flag:
        cargs.append("-vorticity")
    if all_flag:
        cargs.append("-all")
    ret = V3dNwarpFuncsOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_prefix + "_output.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dNwarpFuncsOutputs",
    "V_3D_NWARP_FUNCS_METADATA",
    "v_3d_nwarp_funcs",
]
