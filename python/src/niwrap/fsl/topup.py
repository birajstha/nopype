# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

TOPUP_METADATA = Metadata(
    id="40c0953bd6891879bd9c1d9026dc75ca5ff8448e",
    name="topup",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class TopupOutputs(typing.NamedTuple):
    """
    Output object returned when calling `topup(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fieldcoef: OutputPathType | None
    """Spline coefficient field estimates (Hz)"""
    movpar: OutputPathType | None
    """Movement parameters"""
    fout: OutputPathType | None
    """Image file with field (Hz)"""
    iout: OutputPathType | None
    """4D image file with unwarped images"""
    logout: OutputPathType | None
    """Log file"""


def topup(
    imain: InputPathType,
    datain: InputPathType,
    out: str | None = None,
    fout: str | None = None,
    iout: str | None = None,
    logout: str | None = None,
    warpres: float | int | None = None,
    subsamp: float | int | None = None,
    fwhm: float | int | None = None,
    config: InputPathType | None = None,
    miter: float | int | None = None,
    lambda_: float | int | None = None,
    ssqlambda: bool = False,
    regmod: typing.Literal["membrane_energy", "bending_energy"] | None = None,
    estmov: bool = False,
    minmet: typing.Literal[0, 1] | None = None,
    splineorder: typing.Literal[2, 3] | None = None,
    numprec: typing.Literal["double", "float"] | None = None,
    interp: typing.Literal["linear", "spline"] | None = None,
    scale: bool = False,
    regrid: bool = False,
    verbose: bool = False,
    runner: Runner = None,
) -> TopupOutputs:
    """
    topup by University of Oxford.
    
    topup is part of FSL and is used to estimate and correct for
    susceptibility-induced distortions in echo planar imaging (EPI) data.
    
    Args:
        imain: Name of 4D file with images
        datain: Name of text file with PE directions/times
        out: Base-name of output files (spline coefficients (Hz) and movement
            parameters)
        fout: Name of image file with field (Hz)
        iout: Name of 4D image file with unwarped images
        logout: Name of log-file
        warpres: (Approximate) resolution (in mm) of warp basis for the
            different sub-sampling levels, default 10
        subsamp: Sub-sampling scheme, default 1
        fwhm: FWHM (in mm) of gaussian smoothing kernel, default 8
        config: Name of config file specifying command line arguments
        miter: Max # of non-linear iterations, default 5
        lambda_: Weight of regularisation, default depending on --ssqlambda and
            --regmod switches. See user documentation.
        ssqlambda: If set (=1), lambda is weighted by current ssq, default 1
        regmod: Model for regularisation of warp-field [membrane_energy
            bending_energy], default bending_energy
        estmov: Estimate movements if set, default 1 (true)
        minmet: Minimisation method 0=Levenberg-Marquardt, 1=Scaled Conjugate
            Gradient, default 0 (LM)
        splineorder: Order of spline, 2=Quadratic spline, 3=Cubic spline.
            Default=3
        numprec: Precision for representing Hessian, double or float. Default
            double
        interp: Image interpolation model, linear or spline. Default spline
        scale: If set (=1), the images are individually scaled to a common mean,
            default 0 (false)
        regrid: If set (=1), the calculations are done in a different grid,
            default 1 (true)
        verbose: Print diagnostic information while running
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `TopupOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TOPUP_METADATA)
    cargs = []
    cargs.append("topup")
    cargs.extend(["--imain", execution.input_file(imain)])
    cargs.extend(["--datain", execution.input_file(datain)])
    if out is not None:
        cargs.extend(["--out", out])
    if fout is not None:
        cargs.extend(["--fout", fout])
    if iout is not None:
        cargs.extend(["--iout", iout])
    if logout is not None:
        cargs.extend(["--logout", logout])
    if warpres is not None:
        cargs.extend(["--warpres", str(warpres)])
    if subsamp is not None:
        cargs.extend(["--subsamp", str(subsamp)])
    if fwhm is not None:
        cargs.extend(["--fwhm", str(fwhm)])
    if config is not None:
        cargs.extend(["--config", execution.input_file(config)])
    if miter is not None:
        cargs.extend(["--miter", str(miter)])
    if lambda_ is not None:
        cargs.extend(["--lambda", str(lambda_)])
    if ssqlambda:
        cargs.append("--ssqlambda")
    if regmod is not None:
        cargs.extend(["--regmod", regmod])
    if estmov:
        cargs.append("--estmov")
    if minmet is not None:
        cargs.extend(["--minmet", str(minmet)])
    if splineorder is not None:
        cargs.extend(["--splineorder", str(splineorder)])
    if numprec is not None:
        cargs.extend(["--numprec", numprec])
    if interp is not None:
        cargs.extend(["--interp", interp])
    if scale:
        cargs.append("--scale")
    if regrid:
        cargs.append("--regrid")
    if verbose:
        cargs.append("-v")
    ret = TopupOutputs(
        root=execution.output_file("."),
        fieldcoef=execution.output_file(f"{out}_fieldcoef.nii.gz", optional=True) if out is not None else None,
        movpar=execution.output_file(f"{out}_movpar.txt", optional=True) if out is not None else None,
        fout=execution.output_file(f"{fout}", optional=True) if fout is not None else None,
        iout=execution.output_file(f"{iout}", optional=True) if iout is not None else None,
        logout=execution.output_file(f"{logout}", optional=True) if logout is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TOPUP_METADATA",
    "TopupOutputs",
    "topup",
]
