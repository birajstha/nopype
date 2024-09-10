# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MEICA_PY_METADATA = Metadata(
    id="ff7cba835180280916a3a52015ff9414ebf8e12f.boutiques",
    name="meica.py",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class MeicaPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `meica_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cleaned_bold: OutputPathType
    """Cleaned BOLD image after ME-ICA processing"""
    components_output: OutputPathType
    """Independent components result of ICA"""


def meica_py(
    infile: InputPathType,
    echo_times: str,
    affine: str,
    output_directory: str,
    components: float | None = None,
    talairach: bool = False,
    threshold: float | None = None,
    debug: bool = False,
    runner: Runner | None = None,
) -> MeicaPyOutputs:
    """
    Multi-Echo Independent Component Analysis for fMRI denoising.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/meica.py.html
    
    Args:
        infile: Input image dataset (e.g. dataset.nii.gz).
        echo_times: Echo times (e.g. 15.0,30.0,45.0).
        affine: Affine registration matrix.
        output_directory: Output directory.
        components: Number of components for ICA.
        talairach: Apply standard Talairach transformation.
        threshold: Threshold value for masking.
        debug: Enable debug mode.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MeicaPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MEICA_PY_METADATA)
    cargs = []
    cargs.append("meica.py")
    cargs.append("-d")
    cargs.append(execution.input_file(infile))
    cargs.append("-e")
    cargs.append(echo_times)
    cargs.append("-a")
    cargs.append(affine)
    cargs.append("-o")
    cargs.append(output_directory)
    if components is not None:
        cargs.extend([
            "-c",
            str(components)
        ])
    if talairach:
        cargs.append("-t")
    if threshold is not None:
        cargs.extend([
            "--thresh",
            str(threshold)
        ])
    if debug:
        cargs.append("--debug")
    ret = MeicaPyOutputs(
        root=execution.output_file("."),
        cleaned_bold=execution.output_file(output_directory + "/cleaned_bold.nii.gz"),
        components_output=execution.output_file(output_directory + "/components.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MEICA_PY_METADATA",
    "MeicaPyOutputs",
    "meica_py",
]
