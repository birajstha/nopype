# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

DTIFIT_METADATA = Metadata(
    id="858641733e0be47decba4ee39f2f398f251415c6",
    name="dtifit",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class DtifitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dtifit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fa_output: OutputPathType
    """Fractional anisotropy output"""
    md_output: OutputPathType
    """Mean diffusivity output"""
    mo_output: OutputPathType
    """Mode of the anisotropy output"""
    l1_output: OutputPathType
    """1st eigenvalue output"""
    l2_output: OutputPathType
    """2nd eigenvalue output"""
    l3_output: OutputPathType
    """3rd eigenvalue output"""


def dtifit(
    data_file: InputPathType,
    output_basename: str,
    mask_file: InputPathType,
    bvec_file: InputPathType,
    bval_file: InputPathType,
    verbose_flag: bool = False,
    sse_flag: bool = False,
    wls_flag: bool = False,
    kurt_flag: bool = False,
    kurtdir_flag: bool = False,
    littlebit_flag: bool = False,
    save_tensor_flag: bool = False,
    zmin: float | int | None = None,
    zmax: float | int | None = None,
    ymin: float | int | None = None,
    ymax: float | int | None = None,
    xmin: float | int | None = None,
    xmax: float | int | None = None,
    gradnonlin_file: InputPathType | None = None,
    confound_regressors: InputPathType | None = None,
    runner: Runner | None = None,
) -> DtifitOutputs:
    """
    dtifit by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    DTIFIT - Fit a diffusion tensor model at each voxel.
    
    More information:
    https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FDT/UserGuide#DTIFIT
    
    Args:
        data_file: DTI data file.
        output_basename: Output basename.
        mask_file: Bet binary mask file.
        bvec_file: B vectors file.
        bval_file: B values file.
        verbose_flag: Switch on diagnostic messages.
        sse_flag: Output sum of squared errors.
        wls_flag: Fit the tensor with weighted least squares.
        kurt_flag: Output mean kurtosis map (for multi-shell data).
        kurtdir_flag: Output maps of kurtosis along each eigenvector: K1, K2,\
            and K3 (for multi-shell data).
        littlebit_flag: Only process small area of brain.
        save_tensor_flag: Save the elements of the tensor.
        zmin: Minimum z.
        zmax: Maximum z.
        ymin: Minimum y.
        ymax: Maximum y.
        xmin: Minimum x.
        xmax: Maximum x.
        gradnonlin_file: Gradient Nonlinearity Tensor file.
        confound_regressors: Input confound regressors.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DtifitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DTIFIT_METADATA)
    cargs = []
    cargs.append("dtifit")
    cargs.extend(["-k", execution.input_file(data_file)])
    cargs.extend(["-o", output_basename])
    cargs.extend(["-m", execution.input_file(mask_file)])
    cargs.extend(["-r", execution.input_file(bvec_file)])
    cargs.extend(["-b", execution.input_file(bval_file)])
    if verbose_flag:
        cargs.append("-V")
    if sse_flag:
        cargs.append("--sse")
    if wls_flag:
        cargs.append("-w")
    if kurt_flag:
        cargs.append("--kurt")
    if kurtdir_flag:
        cargs.append("--kurtdir")
    if littlebit_flag:
        cargs.append("--littlebit")
    if save_tensor_flag:
        cargs.append("--save_tensor")
    if zmin is not None:
        cargs.extend(["-z", str(zmin)])
    if zmax is not None:
        cargs.extend(["-Z", str(zmax)])
    if ymin is not None:
        cargs.extend(["-y", str(ymin)])
    if ymax is not None:
        cargs.extend(["-Y", str(ymax)])
    if xmin is not None:
        cargs.extend(["-x", str(xmin)])
    if xmax is not None:
        cargs.extend(["-X", str(xmax)])
    if gradnonlin_file is not None:
        cargs.extend(["--gradnonlin", execution.input_file(gradnonlin_file)])
    if confound_regressors is not None:
        cargs.extend(["--cni", execution.input_file(confound_regressors)])
    ret = DtifitOutputs(
        root=execution.output_file("."),
        fa_output=execution.output_file(f"{output_basename}_FA.nii.gz", optional=True),
        md_output=execution.output_file(f"{output_basename}_MD.nii.gz", optional=True),
        mo_output=execution.output_file(f"{output_basename}_MO.nii.gz", optional=True),
        l1_output=execution.output_file(f"{output_basename}_L1.nii.gz", optional=True),
        l2_output=execution.output_file(f"{output_basename}_L2.nii.gz", optional=True),
        l3_output=execution.output_file(f"{output_basename}_L3.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DTIFIT_METADATA",
    "DtifitOutputs",
    "dtifit",
]
