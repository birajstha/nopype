# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_AUTOBOX_METADATA = Metadata(
    id="05a381e828f751e8b899fb2e7b2ec31c98fe94db.boutiques",
    name="3dAutobox",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dAutoboxOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_autobox(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_autobox(
    input_: InputPathType,
    runner: Runner | None = None,
) -> V3dAutoboxOutputs:
    """
    Computes size of a box that fits around the volume. Can also be used to crop the
    volume to that box.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dAutobox.html
    
    Args:
        input_: Input dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAutoboxOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_AUTOBOX_METADATA)
    cargs = []
    cargs.append("3dAutobox")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(input_))
    ret = V3dAutoboxOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dAutoboxOutputs",
    "V_3D_AUTOBOX_METADATA",
    "v_3d_autobox",
]
