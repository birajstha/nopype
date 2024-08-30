# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSL_TSPLOT_METADATA = Metadata(
    id="37113a4977b8132fb2f361cd4579cba1b0b1c6d5",
    name="fsl_tsplot",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class FslTsplotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_tsplot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_png: OutputPathType
    """Output PNG file"""


def fsl_tsplot(
    input_files: str,
    output_file: str,
    title: str | None = None,
    legend_file: str | None = None,
    labels: str | None = None,
    ymin: float | int | None = None,
    ymax: float | int | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    height: float | int | None = None,
    width: float | int | None = None,
    unit: float | int | None = None,
    precision: float | int | None = None,
    sci_flag: bool = False,
    start_col: float | int | None = None,
    end_col: float | int | None = None,
    runner: Runner | None = None,
) -> FslTsplotOutputs:
    """
    fsl_tsplot by University of Oxford (Christian F. Beckmann).
    
    Timeseries plotting tool from FSL.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/
    
    Args:
        input_files: Comma-separated list of input file names (ASCII text\
            matrix, one column per timecourse).
        output_file: Output filename for the PNG file.
        title: Plot title.
        legend_file: File name of ASCII text file, one row per legend entry.
        labels: Comma-separated list of labels.
        ymin: Minimum y-value.
        ymax: Maximum y-value.
        xlabel: X-axis label.
        ylabel: Y-axis label.
        height: Plot height in pixels (default 150).
        width: Plot width in pixels (default 600).
        unit: Scaling units for x-axis (default 1...length of infile).
        precision: Precision of x-axis labels.
        sci_flag: Switch on scientific notation.
        start_col: Position of first column to plot.
        end_col: Position of final column to plot.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslTsplotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_TSPLOT_METADATA)
    cargs = []
    cargs.append("fsl_tsplot")
    cargs.extend(["-i", input_files])
    cargs.extend(["-o", output_file])
    if title is not None:
        cargs.extend(["-t", title])
    if legend_file is not None:
        cargs.extend(["-l", legend_file])
    if labels is not None:
        cargs.extend(["-a", labels])
    if ymin is not None:
        cargs.extend(["--ymin", str(ymin)])
    if ymax is not None:
        cargs.extend(["--ymax", str(ymax)])
    if xlabel is not None:
        cargs.extend(["-x", xlabel])
    if ylabel is not None:
        cargs.extend(["-y", ylabel])
    if height is not None:
        cargs.extend(["-h", str(height)])
    if width is not None:
        cargs.extend(["-w", str(width)])
    if unit is not None:
        cargs.extend(["-u", str(unit)])
    if precision is not None:
        cargs.extend(["--precision", str(precision)])
    if sci_flag:
        cargs.append("--sci")
    if start_col is not None:
        cargs.extend(["--start", str(start_col)])
    if end_col is not None:
        cargs.extend(["--finish", str(end_col)])
    ret = FslTsplotOutputs(
        root=execution.output_file("."),
        output_png=execution.output_file(f"{output_file}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_TSPLOT_METADATA",
    "FslTsplotOutputs",
    "fsl_tsplot",
]
