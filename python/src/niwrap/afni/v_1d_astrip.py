# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_1D_ASTRIP_METADATA = Metadata(
    id="ddee8c5aa89c51104620ecb54002443adf419876",
    name="1dAstrip",
)


class V1dAstripOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_astrip(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output file with only numeric characters."""


def v_1d_astrip(
    infile: InputPathType,
    runner: Runner | None = None,
) -> V1dAstripOutputs:
    """
    1dAstrip by AFNI Dev Team.
    
    Strips non-numeric characters from a file.
    
    Args:
        infile: Input file from which non-numeric characters will be stripped.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dAstripOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_ASTRIP_METADATA)
    cargs = []
    cargs.append("1dAstrip")
    cargs.append(
        "<" +
        ("< " + execution.input_file(infile)) +
        ">"
    )
    cargs.append("[OUTPUT_FILE]")
    ret = V1dAstripOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"[OUTPUT_FILE]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dAstripOutputs",
    "V_1D_ASTRIP_METADATA",
    "v_1d_astrip",
]
