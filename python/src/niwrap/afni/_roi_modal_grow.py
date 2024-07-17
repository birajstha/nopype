# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ROI_MODAL_GROW_METADATA = Metadata(
    id="7367cad51af711c7813f31542c0ee74bc9cfa26e",
    name="ROI_modal_grow",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="unknown",
)


class RoiModalGrowOutputs(typing.NamedTuple):
    """
    Output object returned when calling `roi_modal_grow(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Final output dataset"""


def roi_modal_grow(
    input_dset: InputPathType,
    niters: float | int,
    outdir: str | None = None,
    mask: InputPathType | None = None,
    prefix: str | None = None,
    neighborhood_type: int | None = None,
    runner: Runner | None = None,
) -> RoiModalGrowOutputs:
    """
    ROI_modal_grow by Unknown.
    
    Script to grow a set of regions in a volumetric dataset using modal
    smoothing.
    
    Args:
        input_dset: Required input dataset. This dataset should be a set of\
            integer values, assuming approximate isotropic voxels.
        niters: Number of iterations for modal growth, generally making sense\
            for values from about 1-10.
        outdir: Directory name for output. All output goes to this directory.\
            Default is rmgrow.
        mask: Mask dataset at the same grid as the input dataset. Could be a\
            dilated version of the original mask or a larger region like a cortical\
            ribbon mask. Not required but often desirable.
        prefix: Base name of the final output dataset, i.e., baseprefix.nii.gz.\
            Default is rmg, so output would be rmg.nii.gz.
        neighborhood_type: Neighborhood type used in finding mode. 1 - facing\
            neighbors, 2 - edges, 3 - corners.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RoiModalGrowOutputs`).
    """
    runner = runner or get_global_runner()
    if neighborhood_type is not None and not (1 <= neighborhood_type <= 3): 
        raise ValueError(f"'neighborhood_type' must be between 1 <= x <= 3 but was {neighborhood_type}")
    execution = runner.start_execution(ROI_MODAL_GROW_METADATA)
    cargs = []
    cargs.append("@ROI_modal_grow")
    cargs.append("-input")
    cargs.extend(["-input", execution.input_file(input_dset)])
    cargs.append("-niters")
    cargs.extend(["-niters", str(niters)])
    cargs.append("-outdir")
    if outdir is not None:
        cargs.extend(["-outdir", outdir])
    cargs.append("-mask")
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    cargs.append("-prefix")
    if prefix is not None:
        cargs.extend(["-prefix", prefix])
    cargs.append("-NN")
    if neighborhood_type is not None:
        cargs.extend(["-NN", str(neighborhood_type)])
    ret = RoiModalGrowOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{outdir}/{prefix}.nii.gz") if outdir is not None and prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ROI_MODAL_GROW_METADATA",
    "RoiModalGrowOutputs",
    "roi_modal_grow",
]
