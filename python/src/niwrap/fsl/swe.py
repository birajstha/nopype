# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SWE_METADATA = Metadata(
    id="890402fb30c936b580dc288da72eed8929f08db8.boutiques",
    name="swe",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class SweOutputs(typing.NamedTuple):
    """
    Output object returned when calling `swe(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    logp_img: OutputPathType
    """Output -log_10(p) images"""
    corrp_img: OutputPathType
    """Output voxel-corrected p-value images"""
    raw_img: OutputPathType
    """Output raw voxelwise statistic images"""
    equiv_img: OutputPathType
    """Output equivalent z or chi-squared statistic images"""
    dof_img: OutputPathType
    """Output effective number of degrees of freedom images"""
    uncorrp_img: OutputPathType
    """Output uncorrected p-value images"""
    null_dist_file: OutputPathType
    """Output null distribution text files"""
    glm_output_file: OutputPathType
    """Output GLM information (pe, cope, & varcope)"""


def swe(
    input_file: InputPathType,
    output_root: str,
    design_mat: InputPathType,
    design_con: InputPathType,
    design_sub: InputPathType,
    mask: InputPathType | None = None,
    fcon: InputPathType | None = None,
    modified: bool = False,
    wild_bootstrap: bool = False,
    logp: bool = False,
    nboot: float | None = 999,
    corrp: bool = False,
    fonly: bool = False,
    tfce: bool = False,
    tfce_2d: bool = False,
    cluster_t: float | None = None,
    cluster_t_mass: float | None = None,
    cluster_f: float | None = None,
    cluster_f_mass: float | None = None,
    quiet: bool = False,
    raw: bool = False,
    equiv: bool = False,
    dof: bool = False,
    uncorr_p: bool = False,
    null_dist: bool = False,
    no_rc_mask: bool = False,
    seed: float | None = None,
    tfce_h: float | None = 2,
    tfce_d: float | None = None,
    tfce_e: float | None = 0.5,
    tfce_c: float | None = 6,
    voxelwise_ev: list[float] | None = None,
    voxelwise_evs: list[InputPathType] | None = None,
    glm_output: bool = False,
    runner: Runner | None = None,
) -> SweOutputs:
    """
    SwE (summary statistics and voxelwise statistical analyses tool for FSL).
    
    Author: Oxford Centre for Functional MRI of the Brain (FMRIB)
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/
    
    Args:
        input_file: 4D input image.
        output_root: Output file root name.
        design_mat: Design matrix file.
        design_con: T contrasts file.
        design_sub: Subjects file.
        mask: Mask image.
        fcon: F contrasts file.
        modified: Use the modified 'Homogeneous' SwE instead of the classic\
            'Heterogeneous' SwE.
        wild_bootstrap: Inference using a non-parametric Wild Bootstrap\
            procedure.
        logp: Return -log_10(p) images instead of 1-p images.
        nboot: Number of bootstraps (default 999).
        corrp: Output voxelwise corrected p-value images.
        fonly: Calculate f-statistics only.
        tfce: Threshold-Free Cluster Enhancement.
        tfce_2d: Threshold-Free Cluster Enhancement with 2D optimisation, e.g.\
            for TBSS data (H=2, E=1, C=26).
        cluster_t: Cluster-extent-based inference for t-contrasts with\
            specified cluster-forming threshold (z-score if >= 1, uncorrected\
            p-value if < 1).
        cluster_t_mass: Cluster-mass-based inference for t-contrasts with\
            specified cluster-forming threshold (z-score if >= 1, uncorrected\
            p-value if < 1).
        cluster_f: Cluster-extent-based inference for f-contrasts with\
            specified cluster-forming threshold (chi-squared-score if >= 1,\
            uncorrected p-value if < 1).
        cluster_f_mass: Cluster-mass-based inference for f-contrasts with\
            specified cluster-forming threshold (chi-squared-score if >= 1,\
            uncorrected p-value if < 1).
        quiet: Switch off diagnostic messages.
        raw: Output raw voxelwise statistic images.
        equiv: Output equivalent z or chi-squared statistic images.
        dof: Output effective number of degrees of freedom images.
        uncorr_p: Output uncorrected p-value images.
        null_dist: Output null distribution text files.
        no_rc_mask: Don't remove constant voxels from mask.
        seed: Specific integer seed for random number generator.
        tfce_h: TFCE height parameter (default=2).
        tfce_d: TFCE delta parameter override.
        tfce_e: TFCE extent parameter (default=0.5).
        tfce_c: TFCE connectivity (6 or 26; default=6).
        voxelwise_ev: List of numbers indicating voxelwise EVs position in the\
            design matrix.
        voxelwise_evs: List of 4D images containing voxelwise EVs.
        glm_output: Output GLM information (pe, cope, & varcope).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SweOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SWE_METADATA)
    cargs = []
    cargs.append("swe")
    cargs.append("-i")
    cargs.append(execution.input_file(input_file))
    cargs.append("-o")
    cargs.append(output_root)
    cargs.append("-d")
    cargs.append(execution.input_file(design_mat))
    cargs.append("-t")
    cargs.append(execution.input_file(design_con))
    cargs.append("-s")
    cargs.append(execution.input_file(design_sub))
    if mask is not None:
        cargs.extend([
            "-m",
            execution.input_file(mask)
        ])
    if fcon is not None:
        cargs.extend([
            "-f",
            execution.input_file(fcon)
        ])
    if modified:
        cargs.append("--modified")
    if wild_bootstrap:
        cargs.append("--wb")
    if logp:
        cargs.append("--logp")
    if nboot is not None:
        cargs.extend([
            "-n",
            str(nboot)
        ])
    if corrp:
        cargs.append("-x")
    if fonly:
        cargs.append("--fonly")
    if tfce:
        cargs.append("-T")
    if tfce_2d:
        cargs.append("--T2")
    if cluster_t is not None:
        cargs.extend([
            "-c",
            str(cluster_t)
        ])
    if cluster_t_mass is not None:
        cargs.extend([
            "-C",
            str(cluster_t_mass)
        ])
    if cluster_f is not None:
        cargs.extend([
            "-F",
            str(cluster_f)
        ])
    if cluster_f_mass is not None:
        cargs.extend([
            "-S",
            str(cluster_f_mass)
        ])
    if quiet:
        cargs.append("--quiet")
    if raw:
        cargs.append("-R")
    if equiv:
        cargs.append("-E")
    if dof:
        cargs.append("-D")
    if uncorr_p:
        cargs.append("--uncorrp")
    if null_dist:
        cargs.append("-N")
    if no_rc_mask:
        cargs.append("--norcmask")
    if seed is not None:
        cargs.extend([
            "--seed",
            str(seed)
        ])
    if tfce_h is not None:
        cargs.extend([
            "--tfce_H",
            str(tfce_h)
        ])
    if tfce_d is not None:
        cargs.extend([
            "--tfce_D",
            str(tfce_d)
        ])
    if tfce_e is not None:
        cargs.extend([
            "--tfce_E",
            str(tfce_e)
        ])
    if tfce_c is not None:
        cargs.extend([
            "--tfce_C",
            str(tfce_c)
        ])
    if voxelwise_ev is not None:
        cargs.extend([
            "--vxl",
            *map(str, voxelwise_ev)
        ])
    if voxelwise_evs is not None:
        cargs.extend([
            "--vxf",
            *[execution.input_file(f) for f in voxelwise_evs]
        ])
    if glm_output:
        cargs.append("--glm_output")
    ret = SweOutputs(
        root=execution.output_file("."),
        logp_img=execution.output_file(output_root + "_logp.nii.gz"),
        corrp_img=execution.output_file(output_root + "_corrp.nii.gz"),
        raw_img=execution.output_file(output_root + "_raw.nii.gz"),
        equiv_img=execution.output_file(output_root + "_equiv.nii.gz"),
        dof_img=execution.output_file(output_root + "_dof.nii.gz"),
        uncorrp_img=execution.output_file(output_root + "_uncorrp.nii.gz"),
        null_dist_file=execution.output_file(output_root + "_null_dist.txt"),
        glm_output_file=execution.output_file(output_root + "_glm.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SWE_METADATA",
    "SweOutputs",
    "swe",
]
