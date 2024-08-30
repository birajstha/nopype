# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

TBSS_4_PRESTATS_METADATA = Metadata(
    id="6528300663fe7670c76b1fc174f15fbdeeb3cde9",
    name="tbss_4_prestats",
)


class Tbss4PrestatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tbss_4_prestats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tbss_4_prestats(
    threshold: float | int = 0.2,
    runner: Runner | None = None,
) -> Tbss4PrestatsOutputs:
    """
    tbss_4_prestats by FMRIB Software Library.
    
    A tool for thresholding the Mean FA Skeleton in TBSS analysis.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/TBSS/UserGuide
    
    Args:
        threshold: Thresholding value for the Mean FA Skeleton; recommended\
            value is 0.2.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Tbss4PrestatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TBSS_4_PRESTATS_METADATA)
    cargs = []
    cargs.append("tbss_4_prestats")
    cargs.append(str(threshold))
    ret = Tbss4PrestatsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TBSS_4_PRESTATS_METADATA",
    "Tbss4PrestatsOutputs",
    "tbss_4_prestats",
]
