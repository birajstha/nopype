# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SHIFT_VOLUME_METADATA = Metadata(
    id="d36217298e8e5843fbbfe6d97324f64beb2ec148",
    name="Shift_Volume",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker",
)


class ShiftVolumeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `shift_volume(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Shifted output dataset."""


def shift_volume(
    dset: InputPathType,
    prefix: str,
    rai_shift_vector: list[float | int] | None = None,
    mni_anat_to_mni: bool = False,
    mni_to_mni_anat: bool = False,
    no_cp: bool = False,
    runner: Runner | None = None,
) -> ShiftVolumeOutputs:
    """
    Shift_Volume by Ziad Saad.
    
    Tool to shift a dataset in the RAI coordinate system or between MNI
    anatomical space and MNI space.
    
    Args:
        dset: Input dataset, typically an anatomical dataset to be aligned to\
            BASE.
        prefix: Prefix for the output dataset.
        rai_shift_vector: Move dataset by dR, dA, dI mm (RAI coordinate system).
        mni_anat_to_mni: Move dataset from MNI Anatomical space to MNI space\
            (equivalent to -rai_shift 0 -4 -5).
        mni_to_mni_anat: Move dataset from MNI space to MNI Anatomical space\
            (equivalent to -rai_shift 0 4 5).
        no_cp: Do not create new data, shift the existing ones (use with\
            caution).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ShiftVolumeOutputs`).
    """
    runner = runner or get_global_runner()
    if rai_shift_vector is not None and (len(rai_shift_vector) != 3): 
        raise ValueError(f"Length of 'rai_shift_vector' must be 3 but was {len(rai_shift_vector)}")
    execution = runner.start_execution(SHIFT_VOLUME_METADATA)
    cargs = []
    cargs.append("@Shift_Volume")
    if rai_shift_vector is not None:
        cargs.extend(["-rai_shift", *map(str, rai_shift_vector)])
    if mni_anat_to_mni:
        cargs.append("-MNI_Anat_to_MNI")
    if mni_to_mni_anat:
        cargs.append("-MNI_to_MNI_Anat")
    cargs.extend(["-dset", execution.input_file(dset)])
    if no_cp:
        cargs.append("-no_cp")
    cargs.extend(["-prefix", prefix])
    ret = ShiftVolumeOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{prefix}.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SHIFT_VOLUME_METADATA",
    "ShiftVolumeOutputs",
    "shift_volume",
]
