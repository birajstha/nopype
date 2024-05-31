# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

METRIC_SMOOTHING_METADATA = Metadata(
    id="ab8d162b251097678bff24a1ba54bf71fbef50d6",
    name="metric-smoothing",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class MetricSmoothingRoi:
    """
    select a region of interest to smooth
    """
    opt_match_columns: bool = False
    """for each input column, use the corresponding column from the roi"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        if self.opt_match_columns:
            cargs.append("-match-columns")
        return cargs


class MetricSmoothingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_smoothing(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_smoothing(
    surface: InputPathType,
    metric_in: InputPathType,
    smoothing_kernel: float | int,
    metric_out: InputPathType,
    opt_fwhm: bool = False,
    roi: MetricSmoothingRoi | None = None,
    opt_fix_zeros: bool = False,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    opt_method_method: str | None = None,
    runner: Runner = None,
) -> MetricSmoothingOutputs:
    """
    metric-smoothing by Washington University School of Medicin.
    
    Smooth a metric file.
    
    Smooth a metric file on a surface. By default, smooths all input columns on
    the entire surface, specify -column to use only one input column, and -roi
    to smooth only where the roi metric is greater than 0, outputting zeros
    elsewhere.
    
    When using -roi, input data outside the ROI is not used to compute the
    smoothed values. By default, the first column of the roi metric is used for
    all input columns. When -match-columns is specified to the -roi option, the
    input and roi metrics must have the same number of columns, and for each
    input column's index, the same column index is used in the roi metric. If
    the -match-columns option to -roi is used while the -column option is also
    used, the number of columns must match between the roi and input metric, and
    it will use the roi column with the index of the selected input column.
    
    The -fix-zeros option causes the smoothing to not use an input value if it
    is zero, but still write a smoothed value to the vertex. This is useful for
    zeros that indicate lack of information, preventing them from pulling down
    the intensity of nearby vertices, while giving the zero an extrapolated
    value.
    
    The -corrected-areas option is intended for when it is unavoidable to smooth
    on a group average surface, it is only an approximate correction for the
    reduction of structure in a group average surface. It is better to smooth
    the data on individuals before averaging, when feasible.
    
    Valid values for <method> are:
    
    GEO_GAUSS_AREA - uses a geodesic gaussian kernel, and normalizes based on
    vertex area in order to work more reliably on irregular surfaces
    
    GEO_GAUSS_EQUAL - uses a geodesic gaussian kernel, and normalizes assuming
    each vertex has equal importance
    
    GEO_GAUSS - matches geodesic gaussian smoothing from caret5, but does not
    check kernels for having unequal importance
    
    The GEO_GAUSS_AREA method is the default because it is usually the correct
    choice. GEO_GAUSS_EQUAL may be the correct choice when the sum of vertex
    values is more meaningful then the surface integral (sum of values .*
    areas), for instance when smoothing vertex areas (the sum is the total
    surface area, while the surface integral is the sum of squares of the vertex
    areas). The GEO_GAUSS method is not recommended, it exists mainly to
    replicate methods of studies done with caret5's geodesic smoothing.
    
    Args:
        surface: the surface to smooth on
        metric_in: the metric to smooth
        smoothing_kernel: the size of the gaussian smoothing kernel in mm, as
            sigma by default
        metric_out: the output metric
        opt_fwhm: kernel size is FWHM, not sigma
        roi: select a region of interest to smooth
        opt_fix_zeros: treat zero values as not being data
        opt_column_column: select a single column to smooth: the column number
            or name
        opt_corrected_areas_area_metric: vertex areas to use instead of
            computing them from the surface: the corrected vertex areas, as a metric
        opt_method_method: select smoothing method, default GEO_GAUSS_AREA: the
            name of the smoothing method
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MetricSmoothingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_SMOOTHING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-smoothing")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_in))
    cargs.append(str(smoothing_kernel))
    cargs.append(execution.input_file(metric_out))
    if opt_fwhm:
        cargs.append("-fwhm")
    if roi is not None:
        cargs.extend(["-roi", *roi.run(execution)])
    if opt_fix_zeros:
        cargs.append("-fix-zeros")
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    if opt_method_method is not None:
        cargs.extend(["-method", opt_method_method])
    ret = MetricSmoothingOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{pathlib.Path(metric_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_SMOOTHING_METADATA",
    "MetricSmoothingOutputs",
    "MetricSmoothingRoi",
    "metric_smoothing",
]
