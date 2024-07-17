# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SUMA_FSVOL_TO_BRIK_METADATA = Metadata(
    id="bd67e81af7783e6908b04ffac362172ecac2f806",
    name="SUMA_FSvolToBRIK",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="freesurfer/freesurfer:latest",
)


class SumaFsvolToBrikOutputs(typing.NamedTuple):
    """
    Output object returned when calling `suma_fsvol_to_brik(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_brik: OutputPathType
    """Output BRIK volume converted from FreeSurfer data"""
    out_head: OutputPathType
    """Header file for the output BRIK volume"""


def suma_fsvol_to_brik(
    fs_vol_data: InputPathType,
    prefix: str,
    runner: Runner | None = None,
) -> SumaFsvolToBrikOutputs:
    """
    SUMA_FSvolToBRIK by FreeSurfer Development Team.
    
    A script to convert COR- or .mgz files from FreeSurfer to BRIK format.
    
    Args:
        fs_vol_data: Input FreeSurfer volume data (e.g. COR- images or .mgz\
            volume).
        prefix: Prefix for output BRIK volume.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SumaFsvolToBrikOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SUMA_FSVOL_TO_BRIK_METADATA)
    cargs = []
    cargs.append("@SUMA_FSvolToBRIK")
    cargs.append(execution.input_file(fs_vol_data))
    cargs.append(prefix)
    ret = SumaFsvolToBrikOutputs(
        root=execution.output_file("."),
        out_brik=execution.output_file(f"{prefix}.BRIK"),
        out_head=execution.output_file(f"{prefix}.HEAD"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SUMA_FSVOL_TO_BRIK_METADATA",
    "SumaFsvolToBrikOutputs",
    "suma_fsvol_to_brik",
]
