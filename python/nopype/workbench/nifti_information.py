# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.692353

import typing

from ..styxdefs import *


NIFTI_INFORMATION_METADATA = Metadata(
    id="b60f485e13ff0a961200bbf6a48d49ca8f77e2d9",
    name="nifti-information",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class NiftiInformationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `nifti_information(...)`.
    """


def nifti_information(
    runner: Runner,
    nifti_file: str,
    opt_print_header: bool = False,
    opt_print_matrix: bool = False,
    opt_print_xml: bool = False,
) -> NiftiInformationOutputs:
    """
    DISPLAY INFORMATION ABOUT A NIFTI/CIFTI FILE.
    
    You must specify at least one -print-* option.
    
    Args:
        runner: Command runner
        nifti_file: the nifti/cifti file to examine
        opt_print_header: display the header contents
        opt_print_matrix: output the values in the matrix (cifti only)
        opt_print_xml: print the cifti XML (cifti only)
    Returns:
        NamedTuple of outputs (described in `NiftiInformationOutputs`).
    """
    execution = runner.start_execution(NIFTI_INFORMATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-nifti-information")
    cargs.append(nifti_file)
    if opt_print_header:
        cargs.append("-print-header")
    if opt_print_matrix:
        cargs.append("-print-matrix")
    if opt_print_xml:
        cargs.append("-print-xml")
    ret = NiftiInformationOutputs(
    )
    execution.run(cargs)
    return ret
