# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

MATCH_SMOOTHING_METADATA = Metadata(
    id="54eb17225dafa071cecff985916a00d21a4caa0d",
    name="match_smoothing",
)


class MatchSmoothingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `match_smoothing(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def match_smoothing(
    example_func: InputPathType,
    func_smoothing_fwhm: float | int,
    example_structural: InputPathType,
    standard_space_resolution: float | int,
    runner: Runner | None = None,
) -> MatchSmoothingOutputs:
    """
    match_smoothing.
    
    Computes the smoothing sigma needed to be applied to structural data to
    match a given functional data smoothing level.
    
    Args:
        example_func: Path to the example functional image file.
        func_smoothing_fwhm: Full-width at half maximum (FWHM) of the smoothing\
            kernel applied to the functional data, in millimeters.
        example_structural: Path to the example structural image file.
        standard_space_resolution: Resolution of the standard space, in\
            millimeters.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MatchSmoothingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MATCH_SMOOTHING_METADATA)
    cargs = []
    cargs.append("match_smoothing")
    cargs.append(execution.input_file(example_func))
    cargs.append(str(func_smoothing_fwhm))
    cargs.append(execution.input_file(example_structural))
    cargs.append(str(standard_space_resolution))
    ret = MatchSmoothingOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MATCH_SMOOTHING_METADATA",
    "MatchSmoothingOutputs",
    "match_smoothing",
]
