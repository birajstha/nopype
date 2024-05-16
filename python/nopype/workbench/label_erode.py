# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.726653

import typing

from ..styxdefs import *


LABEL_ERODE_METADATA = Metadata(
    id="d81a7a6718a4ce679b652b6de345a45280d599dd",
    name="label-erode",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class LabelErodeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_erode(...)`.
    """
    label_out: OutputPathType
    """the output label file"""


def label_erode(
    runner: Runner,
    label: InputPathType,
    surface: InputPathType,
    erode_dist: float | int,
    label_out: InputPathType,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
) -> LabelErodeOutputs:
    """
    ERODE A LABEL FILE.
    
    Around each vertex that is unlabeled, set surrounding vertices to unlabeled.
    The surrounding vertices are all immediate neighbors and all vertices within
    the specified distance.
    
    Note that the -corrected-areas option uses an approximate correction for
    distance along the surface.
    
    Args:
        runner: Command runner
        label: the input label
        surface: the surface to erode on
        erode_dist: distance in mm to erode the labels
        label_out: the output label file
        opt_roi_roi_metric: assume values outside this roi are labeled: metric
            file, positive values denote vertices that have data
        opt_column_column: select a single column to erode: the column number or
            name
        opt_corrected_areas_area_metric: vertex areas to use instead of
            computing them from the surface: the corrected vertex areas, as a metric
    Returns:
        NamedTuple of outputs (described in `LabelErodeOutputs`).
    """
    execution = runner.start_execution(LABEL_ERODE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-label-erode")
    cargs.append(execution.input_file(label))
    cargs.append(execution.input_file(surface))
    cargs.append(str(erode_dist))
    cargs.append(execution.input_file(label_out))
    if opt_roi_roi_metric is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_metric)])
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    ret = LabelErodeOutputs(
        label_out=execution.output_file(f"{label_out}"),
    )
    execution.run(cargs)
    return ret
