# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ADJUNCT_SLICE_SPACE_METADATA = Metadata(
    id="03347c46a857cb678e0301d91f0c2e114b39a536",
    name="adjunct_slice_space",
)


class AdjunctSliceSpaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_slice_space(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def adjunct_slice_space(
    inset: InputPathType,
    nwin: float | int,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> AdjunctSliceSpaceOutputs:
    """
    adjunct_slice_space by PA Taylor (NIMH, NIH, USA).
    
    A tiny adjunct program for @chauffeur_afni to calculate how to evenly space
    a number of slices within each view plane of a dataset.
    
    Args:
        inset: Name of input dataset.
        nwin: Number of windows (i.e., slices) that you want across each view\
            plane.
        help_: See helpfile.
        version: See version number.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctSliceSpaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_SLICE_SPACE_METADATA)
    cargs = []
    cargs.append("adjunct_slice_space")
    cargs.append(execution.input_file(inset))
    cargs.append(str(nwin))
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-ver")
    ret = AdjunctSliceSpaceOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADJUNCT_SLICE_SPACE_METADATA",
    "AdjunctSliceSpaceOutputs",
    "adjunct_slice_space",
]
