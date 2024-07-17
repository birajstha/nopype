# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3DMATCALC_METADATA = Metadata(
    id="ee86f8282019b5c0b17ef984abcc6bb8f3b66a7d",
    name="3dmatcalc",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni_latest",
)


class V3dmatcalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmatcalc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_header: OutputPathType
    """Output dataset header file."""
    output_brick: OutputPathType
    """Output dataset brick file."""


def v_3dmatcalc(
    input_dataset: InputPathType,
    input_matrix: InputPathType,
    output_dataset: str,
    mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> V3dmatcalcOutputs:
    """
    3dmatcalc by Zhark, Emperor.
    
    Apply a matrix to a dataset, voxel-by-voxel, to produce a new dataset.
    
    More information: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset to be processed.
        input_matrix: The matrix to be applied, specified as a .1D file or as\
            an expression in the syntax of 1dmatcalc.
        output_dataset: Prefix for the output dataset.
        mask: Apply the matrix only to voxels in the mask; other voxels will be\
            set to all zeroes.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dmatcalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMATCALC_METADATA)
    cargs = []
    cargs.append("3dmatcalc")
    cargs.append("-input")
    cargs.append(execution.input_file(input_dataset))
    cargs.append("-matrix")
    cargs.append(execution.input_file(input_matrix))
    cargs.append("-prefix")
    cargs.append(output_dataset)
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    ret = V3dmatcalcOutputs(
        root=execution.output_file("."),
        output_header=execution.output_file(f"{output_dataset}+tlrc.HEAD"),
        output_brick=execution.output_file(f"{output_dataset}+tlrc.BRIK"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dmatcalcOutputs",
    "V_3DMATCALC_METADATA",
    "v_3dmatcalc",
]
