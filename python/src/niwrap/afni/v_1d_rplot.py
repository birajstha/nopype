# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1D_RPLOT_METADATA = Metadata(
    id="563de597144e9f7c7ff166ac3722dd396521b524.boutiques",
    name="1dRplot",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V1dRplotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_rplot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_plot: OutputPathType
    """Output plot file"""


def v_1d_rplot(
    input_file: InputPathType,
    runner: Runner | None = None,
) -> V1dRplotOutputs:
    """
    Program for plotting a 1D file.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/1dRplot.html
    
    Args:
        input_file: Input 1D file to plot.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dRplotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_RPLOT_METADATA)
    cargs = []
    cargs.append("1dRplot")
    cargs.extend([
        "-input",
        execution.input_file(input_file)
    ])
    cargs.append("[OPTIONS]")
    ret = V1dRplotOutputs(
        root=execution.output_file("."),
        output_plot=execution.output_file("[PREFIX]*.jpg"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dRplotOutputs",
    "V_1D_RPLOT_METADATA",
    "v_1d_rplot",
]
