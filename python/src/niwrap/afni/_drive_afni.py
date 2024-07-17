# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

DRIVE_AFNI_METADATA = Metadata(
    id="fad24861cc560db406c6f9d5be51cdcce681c75a",
    name="DriveAfni",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni_latest",
)


class DriveAfniOutputs(typing.NamedTuple):
    """
    Output object returned when calling `drive_afni(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_jpg: OutputPathType
    """Output file created by the DriveAfni script"""


def drive_afni(
    data_dir: str,
    runner: Runner | None = None,
) -> DriveAfniOutputs:
    """
    DriveAfni by AFNI Development Team.
    
    A demo program for driving 'afni' from a script.
    
    More information: https://afni.nimh.nih.gov/
    
    Args:
        data_dir: AFNI_data6 class data directory which the script requires for\
            execution. This review requires the script to be positioned such that\
            'ls' command should include 'AFNI_data6' in the output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DriveAfniOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DRIVE_AFNI_METADATA)
    cargs = []
    cargs.append("DriveAfni")
    ret = DriveAfniOutputs(
        root=execution.output_file("."),
        output_jpg=execution.output_file(f"./SavedAxiale.jpg"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DRIVE_AFNI_METADATA",
    "DriveAfniOutputs",
    "drive_afni",
]
