# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

RMZ_METADATA = Metadata(
    id="54a69805c2bd8ba4e75e0afdfb0df1ea6ae74579",
    name="rmz",
)


class RmzOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rmz(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rmz(
    filenames: list[InputPathType],
    quiet: bool = False,
    hash_flag: float | int | None = None,
    keep_flag: bool = False,
    runner: Runner | None = None,
) -> RmzOutputs:
    """
    rmz by Author Name.
    
    Zeros out files before removing them.
    
    Args:
        filenames: Files to zero out and remove.
        quiet: Quiet mode.
        hash_flag: Number of times to zero out the files.
        keep_flag: Keep the files instead of removing them.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RmzOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RMZ_METADATA)
    cargs = []
    cargs.append("rmz")
    if quiet:
        cargs.append("-q")
    if hash_flag is not None:
        cargs.extend(["-#", str(hash_flag)])
    if keep_flag:
        cargs.append("-k")
    cargs.extend([execution.input_file(f) for f in filenames])
    ret = RmzOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RMZ_METADATA",
    "RmzOutputs",
    "rmz",
]
