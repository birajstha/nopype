# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BEDPOSTX_GPU_METADATA = Metadata(
    id="1b7bc98054c569d66c0ab265626948c131ff30cd.boutiques",
    name="bedpostx_gpu",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class BedpostxGpuOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bedpostx_gpu(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def bedpostx_gpu(
    subject_dir: str,
    gpu_queue: str | None = None,
    num_jobs: float | None = None,
    num_fibers: float | None = None,
    ard_weight: float | None = None,
    burnin_period: float | None = None,
    num_jumps: float | None = None,
    sample_every: float | None = None,
    deconv_model: float | None = None,
    grad_nonlinear: bool = False,
    runner: Runner | None = None,
) -> BedpostxGpuOutputs:
    """
    Probabilistic tractography and diffusion MRI fitting tool.
    
    Author: FMRIB Software Library (FSL)
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FDT/Bedpostx
    
    Args:
        subject_dir: Directory containing the subject's DWI data and associated\
            files (bvals, bvecs, data, nodif_brain_mask).
        gpu_queue: Name of the GPU(s) queue. Default: --coprocessor=cuda to let\
            fsl_sub decide on the queue.
        num_jobs: Number of jobs to queue. The data is divided into this number\
            of parts, useful for a GPU cluster. Default: 4.
        num_fibers: Number of fibres per voxel. Default: 3.
        ard_weight: Automatic Relevance Determination (ARD) weight. More weight\
            means fewer secondary fibres per voxel. Default: 1.
        burnin_period: Burn-in period. Default: 1000.
        num_jumps: Number of jumps. Default: 1250.
        sample_every: Sample every N steps. Default: 25.
        deconv_model: Deconvolution model. 1: with sticks, 2: with sticks with\
            a range of diffusivities (default), 3: with zeppelins.
        grad_nonlinear: Consider gradient nonlinearities. Default: off.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BedpostxGpuOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BEDPOSTX_GPU_METADATA)
    cargs = []
    cargs.append("bedpostx")
    cargs.append(subject_dir)
    if gpu_queue is not None:
        cargs.extend([
            "-Q",
            gpu_queue
        ])
    if num_jobs is not None:
        cargs.extend([
            "-NJOBS",
            str(num_jobs)
        ])
    if num_fibers is not None:
        cargs.extend([
            "-n",
            str(num_fibers)
        ])
    if ard_weight is not None:
        cargs.extend([
            "-w",
            str(ard_weight)
        ])
    if burnin_period is not None:
        cargs.extend([
            "-b",
            str(burnin_period)
        ])
    if num_jumps is not None:
        cargs.extend([
            "-j",
            str(num_jumps)
        ])
    if sample_every is not None:
        cargs.extend([
            "-s",
            str(sample_every)
        ])
    if deconv_model is not None:
        cargs.extend([
            "-model",
            str(deconv_model)
        ])
    if grad_nonlinear:
        cargs.append("-g")
    ret = BedpostxGpuOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BEDPOSTX_GPU_METADATA",
    "BedpostxGpuOutputs",
    "bedpostx_gpu",
]
