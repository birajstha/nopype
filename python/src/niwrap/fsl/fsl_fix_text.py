# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSL_FIX_TEXT_METADATA = Metadata(
    id="707d01f618f5b3907a4ea2c996343b05c4b0098b",
    name="fslFixText",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class FslFixTextOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_fix_text(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_text_file: OutputPathType
    """Output text file with standard UNIX line endings"""


def fsl_fix_text(
    input_text_file: InputPathType,
    output_text_file: str,
    runner: Runner | None = None,
) -> FslFixTextOutputs:
    """
    fslFixText by FMRIB Software Library (FSL).
    
    Ensures standard UNIX line endings in the output text file.
    
    Args:
        input_text_file: Input text file.
        output_text_file: Output text file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslFixTextOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_FIX_TEXT_METADATA)
    cargs = []
    cargs.append("fslFixText")
    cargs.append(execution.input_file(input_text_file))
    cargs.append(output_text_file)
    ret = FslFixTextOutputs(
        root=execution.output_file("."),
        output_text_file=execution.output_file(f"{output_text_file}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_FIX_TEXT_METADATA",
    "FslFixTextOutputs",
    "fsl_fix_text",
]
