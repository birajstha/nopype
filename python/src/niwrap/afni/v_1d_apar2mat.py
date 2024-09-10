# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1D_APAR2MAT_METADATA = Metadata(
    id="260e03a84b8f1c1f918a4f17a93bb26f89a35430.boutiques",
    name="1dApar2mat",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V1dApar2matOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_apar2mat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_1d_apar2mat(
    x_shift: float,
    y_shift: float,
    z_shift: float,
    z_angle: float,
    x_angle: float,
    y_angle: float,
    x_scale: float,
    y_scale: float,
    z_scale: float,
    y_x_shear: float,
    z_x_shear: float,
    z_y_shear: float,
    runner: Runner | None = None,
) -> V1dApar2matOutputs:
    """
    Computes the affine transformation matrix from the set of 3dAllineate
    parameters.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/1dApar2mat.html
    
    Args:
        x_shift: x-shift in mm.
        y_shift: y-shift in mm.
        z_shift: z-shift in mm.
        z_angle: z-angle (roll) in degrees.
        x_angle: x-angle (pitch) in degrees.
        y_angle: y-angle (yaw) in degrees.
        x_scale: x-scale factor in [0.10,10.0].
        y_scale: y-scale factor in [0.10,10.0].
        z_scale: z-scale factor in [0.10,10.0].
        y_x_shear: y/x-shear factor in [-0.3333,0.3333].
        z_x_shear: z/x-shear factor in [-0.3333,0.3333].
        z_y_shear: z/y-shear factor in [-0.3333,0.3333].
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dApar2matOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_APAR2MAT_METADATA)
    cargs = []
    cargs.append("1dApar2mat")
    cargs.append(str(x_shift))
    cargs.append(str(y_shift))
    cargs.append(str(z_shift))
    cargs.append(str(z_angle))
    cargs.append(str(x_angle))
    cargs.append(str(y_angle))
    cargs.append(str(x_scale))
    cargs.append(str(y_scale))
    cargs.append(str(z_scale))
    cargs.append(str(y_x_shear))
    cargs.append(str(z_x_shear))
    cargs.append(str(z_y_shear))
    ret = V1dApar2matOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dApar2matOutputs",
    "V_1D_APAR2MAT_METADATA",
    "v_1d_apar2mat",
]
