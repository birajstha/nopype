# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_ENTROPY_METADATA = Metadata(
    id="993b0bb98ae8aa57167ddfe5a6d2489bd5a4ee28",
    name="3dEntropy",
)


class V3dEntropyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_entropy(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_entropy(
    input_dataset: InputPathType,
    zskip: bool = False,
    runner: Runner | None = None,
) -> V3dEntropyOutputs:
    """
    3dEntropy by AFNI Development Team.
    
    Computes entropy for a 3D dataset.
    
    More information: https://afni.nimh.nih.gov
    
    Args:
        input_dataset: Input dataset (stored as 16 bit shorts).
        zskip: Skip 0 values in the entropy computation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dEntropyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ENTROPY_METADATA)
    cargs = []
    cargs.append("3dEntropy")
    if zskip:
        cargs.append("-zskip")
    cargs.append(execution.input_file(input_dataset))
    ret = V3dEntropyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dEntropyOutputs",
    "V_3D_ENTROPY_METADATA",
    "v_3d_entropy",
]
