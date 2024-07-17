# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_MEPFM_METADATA = Metadata(
    id="2b46d65569c3fd41b8f294716945ae47a23eeb95",
    name="3dMEPFM",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="neurodocker:latest",
)


class V3dMepfmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_mepfm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dr2_output: OutputPathType
    """Changes in R2* parameter, assumed to represent neuronal-related signal changes"""
    dr2fit_output: OutputPathType
    """Convolution of DR2 with HRF, one volume per echo"""
    ds0_output: OutputPathType
    """Changes in net magnetization (S0) (if estimated)"""
    lambda_output: OutputPathType
    """Regularization parameter"""
    sigmas_mad_output: OutputPathType
    """Estimate of the noise standard deviation after wavelet decomposition for each input dataset"""
    costs_output: OutputPathType
    """Cost function to select the regularization parameter (lambda) according to selection criterion"""


def v_3d_mepfm(
    input_files: list[str],
    dbg_args: bool = False,
    mask: InputPathType | None = None,
    hrf_model: str | None = None,
    verbosity: int | None = None,
    runner: Runner | None = None,
) -> V3dMepfmOutputs:
    """
    3dMEPFM by C Caballero-Gaudes.
    
    Voxelwise deconvolution of Multiecho fMRI data to yield time-varying
    estimates of changes in transverse relaxation (DR2*) and optionally, net
    magnetization (DS0).
    
    More information: https://afni.nimh.nih.gov/afni/
    
    Args:
        input_files: Dataset to analyze with Multiecho Paradigm Free Mapping,\
            along with the echo time.
        dbg_args: Enable R to save the parameters in .3dMEPFM.dbg.AFNI.args in\
            the current directory.
        mask: Process voxels inside this mask only. Default is no masking.
        hrf_model: Haemodynamic response function used for deconvolution.
        verbosity: Verbosity level. 0 for quiet, 1 (default) or more:\
            talkative.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dMepfmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_MEPFM_METADATA)
    cargs = []
    cargs.append("3dMEPFM")
    cargs.extend(["-input", *input_files])
    if dbg_args:
        cargs.append("-dbgArgs")
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if hrf_model is not None:
        cargs.extend(["-hrf", hrf_model])
    if verbosity is not None:
        cargs.extend(["-verb", str(verbosity)])
    cargs.append("[OTHER_OPTIONS]")
    ret = V3dMepfmOutputs(
        root=execution.output_file("."),
        dr2_output=execution.output_file(f"DR2_[PREFIX]_*.nii.gz", optional=True),
        dr2fit_output=execution.output_file(f"DR2fit_[PREFIX]_*.nii.gz", optional=True),
        ds0_output=execution.output_file(f"DS0_[PREFIX]_*.nii.gz", optional=True),
        lambda_output=execution.output_file(f"lambda_[PREFIX]_*.nii.gz", optional=True),
        sigmas_mad_output=execution.output_file(f"sigmas_MAD_[PREFIX]_*.nii.gz", optional=True),
        costs_output=execution.output_file(f"costs_[PREFIX]_*.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dMepfmOutputs",
    "V_3D_MEPFM_METADATA",
    "v_3d_mepfm",
]
