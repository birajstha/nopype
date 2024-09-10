# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FIM2_METADATA = Metadata(
    id="e30f33f949a5efca13859e78a1eb5027bf0381cc.boutiques",
    name="fim2",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class Fim2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `fim2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    activation_magnitudes: OutputPathType
    """Activation magnitudes output file"""
    correlation_image: OutputPathType
    """Correlation image output file"""
    contrast_to_noise_image: OutputPathType
    """Contrast-to-noise image output file"""
    std_deviation_image: OutputPathType
    """Standard deviation image output file"""
    ls_fit_coefficients: OutputPathType
    """Least squares fit coefficients image files"""
    subtracted_references: OutputPathType
    """Subtracted ortho reference time series images"""


def fim2(
    image_files: list[InputPathType],
    runner: Runner | None = None,
) -> Fim2Outputs:
    """
    Functional Imaging Mapping Tool.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/fim2.html
    
    Args:
        image_files: Input MRI image files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Fim2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIM2_METADATA)
    cargs = []
    cargs.append("fim2")
    cargs.append("[OPTIONS]")
    cargs.extend([execution.input_file(f) for f in image_files])
    ret = Fim2Outputs(
        root=execution.output_file("."),
        activation_magnitudes=execution.output_file("[FIMFILE]"),
        correlation_image=execution.output_file("[CORFILE]"),
        contrast_to_noise_image=execution.output_file("[CNRFILE]"),
        std_deviation_image=execution.output_file("[SIGFILE]"),
        ls_fit_coefficients=execution.output_file("[FITFILE]"),
        subtracted_references=execution.output_file("[SUBORT]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIM2_METADATA",
    "Fim2Outputs",
    "fim2",
]
