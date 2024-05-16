# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.783307

import typing

from ..styxdefs import *


METRIC_TFCE_METADATA = Metadata(
    id="6faf91cbc1bd5bce57c7eedbf10ca1c252dba440",
    name="metric-tfce",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class MetricTfceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_tfce(...)`.
    """
    metric_out: OutputPathType
    """the output metric"""


def metric_tfce(
    runner: Runner,
    surface: InputPathType,
    metric_in: InputPathType,
    metric_out: InputPathType,
    opt_presmooth_kernel: float | int | None = None,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
) -> MetricTfceOutputs:
    """
    DO TFCE ON A METRIC FILE.
    
    This command does not do any statistical analysis. Please use something like
    PALM if you are just trying to do statistics on your data.
    
    Threshold-free cluster enhancement is a method to increase the relative
    value of regions that would form clusters in a standard thresholding test.
    This is accomplished by evaluating the integral of:
    
    e(h, p)^E * h^H * dh
    
    at each vertex p, where h ranges from 0 to the maximum value in the data,
    and e(h, p) is the extent of the cluster containing vertex p at threshold h.
    Negative values are similarly enhanced by negating the data, running the
    same process, and negating the result.
    
    When using -presmooth with -corrected-areas, note that it is an approximate
    correction within the smoothing algorithm (the TFCE correction is exact).
    Doing smoothing on individual surfaces before averaging/TFCE is preferred,
    when possible, in order to better tie the smoothing kernel size to the
    original feature size.
    
    The TFCE method is explained in: Smith SM, Nichols TE., "Threshold-free
    cluster enhancement: addressing problems of smoothing, threshold dependence
    and localisation in cluster inference." Neuroimage. 2009 Jan 1;44(1):83-98.
    PMID: 18501637
    
    Args:
        runner: Command runner
        surface: the surface to compute on
        metric_in: the metric to run TFCE on
        metric_out: the output metric
        opt_presmooth_kernel: smooth the metric before running TFCE: the size of
            the gaussian smoothing kernel in mm, as sigma by default
        opt_roi_roi_metric: select a region of interest to run TFCE on: the area
            to run TFCE on, as a metric
        opt_column_column: select a single column: the column number or name
        opt_corrected_areas_area_metric: vertex areas to use instead of
            computing them from the surface: the corrected vertex areas, as a metric
    Returns:
        NamedTuple of outputs (described in `MetricTfceOutputs`).
    """
    execution = runner.start_execution(METRIC_TFCE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-tfce")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_in))
    cargs.append(execution.input_file(metric_out))
    if opt_presmooth_kernel is not None:
        cargs.extend(["-presmooth", str(opt_presmooth_kernel)])
    if opt_roi_roi_metric is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_metric)])
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    ret = MetricTfceOutputs(
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret
