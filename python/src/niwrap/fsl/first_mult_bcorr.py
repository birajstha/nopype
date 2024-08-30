# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FIRST_MULT_BCORR_METADATA = Metadata(
    id="4dac584773c01eaae0963dfff244a6a9305be125",
    name="first_mult_bcorr",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class FirstMultBcorrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `first_mult_bcorr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output image name (3D label image)"""


def first_mult_bcorr(
    input_image: InputPathType,
    output_image: str,
    uncorrected_4d_labels: InputPathType,
    corrected_4d_labels: InputPathType,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> FirstMultBcorrOutputs:
    """
    first_mult_bcorr by University of Oxford (Mark Jenkinson).
    
    Part of FSL (ID: 6.0.5:9e026117), first_mult_bcorr converts label images to
    an output image.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FIRST
    
    Args:
        input_image: Filename of original T1 input image.
        output_image: Output image name (3D label image).
        uncorrected_4d_labels: Filename of 4D image of uncorrected labels (with\
            boundaries).
        corrected_4d_labels: Filename of 4D image of individually corrected\
            labels.
        verbose_flag: Output F-stats to standard out.
        help_flag: Display this help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FirstMultBcorrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIRST_MULT_BCORR_METADATA)
    cargs = []
    cargs.append("first_mult_bcorr")
    cargs.extend(["-i", execution.input_file(input_image)])
    cargs.extend(["-c", execution.input_file(corrected_4d_labels)])
    cargs.extend(["-u", execution.input_file(uncorrected_4d_labels)])
    cargs.extend(["-o", output_image])
    if verbose_flag:
        cargs.append("-v")
    ret = FirstMultBcorrOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{output_image}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIRST_MULT_BCORR_METADATA",
    "FirstMultBcorrOutputs",
    "first_mult_bcorr",
]
