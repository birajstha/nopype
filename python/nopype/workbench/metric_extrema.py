# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.720696

import typing

from ..styxdefs import *


METRIC_EXTREMA_METADATA = Metadata(
    id="efed9105e7ae22dddbe888822c2794569178a09d",
    name="metric-extrema",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class MetricExtremaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_extrema(...)`.
    """
    metric_out: OutputPathType
    """the output extrema metric"""


def metric_extrema(
    runner: Runner,
    surface: InputPathType,
    metric_in: InputPathType,
    distance: float | int,
    metric_out: InputPathType,
    opt_presmooth_kernel: float | int | None = None,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_sum_columns: bool = False,
    opt_consolidate_mode: bool = False,
    opt_only_maxima: bool = False,
    opt_only_minima: bool = False,
    opt_column_column: str | None = None,
) -> MetricExtremaOutputs:
    """
    FIND EXTREMA IN A METRIC FILE.
    
    Finds extrema in a metric file, such that no two extrema of the same type
    are within <distance> of each other. The extrema are labeled as -1 for
    minima, 1 for maxima, 0 otherwise. If -only-maxima or -only-minima is
    specified, then it will ignore extrema not of the specified type. These
    options are mutually exclusive.
    
    If -roi is specified, not only is data outside the roi not used, but any
    vertex on the edge of the ROI will never be counted as an extrema, in case
    the ROI cuts across a gradient, which would otherwise generate extrema where
    there should be none.
    
    If -sum-columns is specified, these extrema columns are summed, and the
    output has a single column with this result.
    
    By default, a datapoint is an extrema only if it is more extreme than every
    other datapoint that is within <distance> from it. If -consolidate-mode is
    used, it instead starts by finding all datapoints that are more extreme than
    their immediate neighbors, then while there are any extrema within
    <distance> of each other, take the two extrema closest to each other and
    merge them into one by a weighted average based on how many original extrema
    have been merged into each.
    
    By default, all input columns are used with no smoothing, use -column to
    specify a single column to use, and -presmooth to smooth the input before
    finding the extrema.
    
    Args:
        runner: Command runner
        surface: the surface to use for distance information
        metric_in: the metric to find the extrema of
        distance: the minimum distance between identified extrema of the same
            type
        metric_out: the output extrema metric
        opt_presmooth_kernel: smooth the metric before finding extrema: the size
            of the gaussian smoothing kernel in mm, as sigma by default
        opt_roi_roi_metric: ignore values outside the selected area: the area to
            find extrema in, as a metric
        opt_sum_columns: output the sum of the extrema columns instead of each
            column separately
        opt_consolidate_mode: use consolidation of local minima instead of a
            large neighborhood
        opt_only_maxima: only find the maxima
        opt_only_minima: only find the minima
        opt_column_column: select a single column to find extrema in: the column
            number or name
    Returns:
        NamedTuple of outputs (described in `MetricExtremaOutputs`).
    """
    execution = runner.start_execution(METRIC_EXTREMA_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-extrema")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_in))
    cargs.append(str(distance))
    cargs.append(execution.input_file(metric_out))
    if opt_presmooth_kernel is not None:
        cargs.extend(["-presmooth", str(opt_presmooth_kernel)])
    if opt_roi_roi_metric is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_metric)])
    if opt_sum_columns:
        cargs.append("-sum-columns")
    if opt_consolidate_mode:
        cargs.append("-consolidate-mode")
    if opt_only_maxima:
        cargs.append("-only-maxima")
    if opt_only_minima:
        cargs.append("-only-minima")
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    ret = MetricExtremaOutputs(
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret
