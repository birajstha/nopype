# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

CHECK_FEAT_METADATA = Metadata(
    id="88315ec54afacdeb331bb12bda2509e0741bd892",
    name="checkFEAT",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class CheckFeatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `check_feat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_report: OutputPathType
    """Output HTML report"""
    output_report_log: OutputPathType
    """Output HTML report log"""


def check_feat(
    report_file: InputPathType,
    report_log_file: InputPathType,
    runner: Runner | None = None,
) -> CheckFeatOutputs:
    """
    checkFEAT by YourName.
    
    Perform checks on FEAT analysis results.
    
    More information: http://example.com/checkFEAT
    
    Args:
        report_file: Path to the HTML report.
        report_log_file: Path to the HTML report log.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CheckFeatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CHECK_FEAT_METADATA)
    cargs = []
    cargs.append("checkFEAT")
    cargs.append(execution.input_file(report_file))
    cargs.append(execution.input_file(report_log_file))
    ret = CheckFeatOutputs(
        root=execution.output_file("."),
        output_report=execution.output_file(f"output_report.html"),
        output_report_log=execution.output_file(f"output_report_log.html"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CHECK_FEAT_METADATA",
    "CheckFeatOutputs",
    "check_feat",
]
