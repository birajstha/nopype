# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_NO_POUND_METADATA = Metadata(
    id="c22f5fc56c0ed441e547cbe5f199b3a479e1080e",
    name="@NoPound",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni_latest",
)


class NoPoundOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_no_pound(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def _no_pound(
    afni_files: list[str],
    runner: Runner | None = None,
) -> NoPoundOutputs:
    """
    @NoPound by AFNI Development Team.
    
    Replaces all # characters in AFNI filenames with a -.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@NoPound.html
    
    Args:
        afni_files: List of AFNI files where # characters should be replaced\
            with -.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `NoPoundOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(_NO_POUND_METADATA)
    cargs = []
    cargs.append("@NoPound")
    cargs.extend(afni_files)
    ret = NoPoundOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "NoPoundOutputs",
    "_NO_POUND_METADATA",
    "_no_pound",
]
