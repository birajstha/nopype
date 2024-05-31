# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

METRIC_FALSE_CORRELATION_METADATA = Metadata(
    id="34247ec59637a12760c7dcfbf29cd02ad778c03f",
    name="metric-false-correlation",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class MetricFalseCorrelationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_false_correlation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_false_correlation(
    surface: InputPathType,
    metric_in: InputPathType,
    v_3d_dist: float | int,
    geo_outer: float | int,
    geo_inner: float | int,
    metric_out: InputPathType,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_dump_text_text_out: str | None = None,
    runner: Runner = None,
) -> MetricFalseCorrelationOutputs:
    """
    metric-false-correlation by Washington University School of Medicin.
    
    Compare correlation locally and across/through sulci/gyri.
    
    For each vertex, compute the average correlation within a range of geodesic
    distances that don't cross a sulcus/gyrus, and the correlation to the
    closest vertex crossing a sulcus/gyrus. A vertex is considered to cross a
    sulcus/gyrus if the 3D distance is less than a third of the geodesic
    distance. The output file contains the ratio between these correlations, and
    some additional maps to help explain the ratio.
    
    Args:
        surface: the surface to compute geodesic and 3D distance with
        metric_in: the metric to correlate
        v_3d_dist: maximum 3D distance to check around each vertex
        geo_outer: maximum geodesic distance to use for neighboring correlation
        geo_inner: minimum geodesic distance to use for neighboring correlation
        metric_out: the output metric
        opt_roi_roi_metric: select a region of interest that has data: the
            region, as a metric file
        opt_dump_text_text_out: dump the raw measures used to a text file: the
            output text file
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MetricFalseCorrelationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_FALSE_CORRELATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-false-correlation")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_in))
    cargs.append(str(v_3d_dist))
    cargs.append(str(geo_outer))
    cargs.append(str(geo_inner))
    cargs.append(execution.input_file(metric_out))
    if opt_roi_roi_metric is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_metric)])
    if opt_dump_text_text_out is not None:
        cargs.extend(["-dump-text", opt_dump_text_text_out])
    ret = MetricFalseCorrelationOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{pathlib.Path(metric_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_FALSE_CORRELATION_METADATA",
    "MetricFalseCorrelationOutputs",
    "metric_false_correlation",
]
