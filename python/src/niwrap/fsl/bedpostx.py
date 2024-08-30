# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

BEDPOSTX_METADATA = Metadata(
    id="e158f79c10af9acc81b8a87118987a2fd47fc3ec",
    name="bedpostx",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class BedpostxOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bedpostx(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    xfms_output: OutputPathType
    """Output transformations."""
    diff_slices_output: OutputPathType
    """Output diffusion slices."""


def bedpostx(
    subject_dir: str,
    num_fibres: float | int | None = 3,
    ard_weight: float | int | None = 1,
    burnin: float | int | None = 1000,
    num_jumps: float | int | None = 1250,
    sample_every: float | int | None = 25,
    model_type: float | int | None = 2,
    grad_nonlinear: bool = False,
    runner: Runner | None = None,
) -> BedpostxOutputs:
    """
    bedpostx by FMRIB Centre.
    
    Bayesian Estimation of Diffusion Parameters Obtained using Sampling
    Techniques (BEDPOST) for modeling multiple fibers per voxel.
    
    More information:
    https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FDT/UserGuide#BEDPOSTX
    
    Args:
        subject_dir: Input subject directory which contains bvals, bvecs, data,\
            and nodif_brain_mask files.
        num_fibres: Number of fibres per voxel (default 3).
        ard_weight: ARD weight, more weight means less secondary fibres per\
            voxel (default 1).
        burnin: Burnin period (default 1000).
        num_jumps: Number of jumps (default 1250).
        sample_every: Sample every (default 25).
        model_type: Deconvolution model. 1: with sticks, 2: with sticks with a\
            range of diffusivities (default), 3: with zeppelins.
        grad_nonlinear: Consider gradient nonlinearities, expects grad_dev in\
            the subject directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BedpostxOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BEDPOSTX_METADATA)
    cargs = []
    cargs.append("bedpostx")
    cargs.append(subject_dir)
    if num_fibres is not None:
        cargs.extend(["-n", str(num_fibres)])
    if ard_weight is not None:
        cargs.extend(["-w", str(ard_weight)])
    if burnin is not None:
        cargs.extend(["-b", str(burnin)])
    if num_jumps is not None:
        cargs.extend(["-j", str(num_jumps)])
    if sample_every is not None:
        cargs.extend(["-s", str(sample_every)])
    if model_type is not None:
        cargs.extend(["-model", str(model_type)])
    if grad_nonlinear:
        cargs.append("-g")
    ret = BedpostxOutputs(
        root=execution.output_file("."),
        xfms_output=execution.output_file(f"{subject_dir}_bedpostx/xfms/*", optional=True),
        diff_slices_output=execution.output_file(f"{subject_dir}_bedpostx/diff_slices/*", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BEDPOSTX_METADATA",
    "BedpostxOutputs",
    "bedpostx",
]
