# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

METRIC_ROIS_FROM_EXTREMA_METADATA = Metadata(
    id="5ea2d9e893fe62547d5a74a2d8ab70f6d99035be",
    name="metric-rois-from-extrema",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class MetricRoisFromExtremaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_rois_from_extrema(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric file"""


def metric_rois_from_extrema(
    surface: InputPathType,
    metric: InputPathType,
    limit: float | int,
    metric_out: InputPathType,
    opt_gaussian_sigma: float | int | None = None,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_overlap_logic_method: str | None = None,
    opt_column_column: str | None = None,
    runner: Runner = None,
) -> MetricRoisFromExtremaOutputs:
    """
    metric-rois-from-extrema by Washington University School of Medicin.
    
    Create metric roi maps from extrema maps.
    
    For each nonzero value in each map, make a map with an ROI around that
    location. If the -gaussian option is specified, then normalized gaussian
    kernels are output instead of ROIs. The <method> argument to -overlap-logic
    must be one of ALLOW, CLOSEST, or EXCLUDE. ALLOW is the default, and means
    that ROIs are treated independently and may overlap. CLOSEST means that ROIs
    may not overlap, and that no ROI contains vertices that are closer to a
    different seed vertex. EXCLUDE means that ROIs may not overlap, and that any
    vertex within range of more than one ROI does not belong to any ROI.
    
    Args:
        surface: the surface to use for geodesic distance
        metric: the input metric file
        limit: geodesic distance limit from vertex, in mm
        metric_out: the output metric file
        opt_gaussian_sigma: generate a gaussian kernel instead of a flat ROI:
            the sigma for the gaussian kernel, in mm
        opt_roi_roi_metric: select a region of interest to use: the area to use,
            as a metric
        opt_overlap_logic_method: how to handle overlapping ROIs, default ALLOW:
            the method of resolving overlaps
        opt_column_column: select a single input column to use: the column
            number or name
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MetricRoisFromExtremaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_ROIS_FROM_EXTREMA_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-rois-from-extrema")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric))
    cargs.append(str(limit))
    cargs.append(execution.input_file(metric_out))
    if opt_gaussian_sigma is not None:
        cargs.extend(["-gaussian", str(opt_gaussian_sigma)])
    if opt_roi_roi_metric is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_metric)])
    if opt_overlap_logic_method is not None:
        cargs.extend(["-overlap-logic", opt_overlap_logic_method])
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    ret = MetricRoisFromExtremaOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{pathlib.Path(metric_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_ROIS_FROM_EXTREMA_METADATA",
    "MetricRoisFromExtremaOutputs",
    "metric_rois_from_extrema",
]
