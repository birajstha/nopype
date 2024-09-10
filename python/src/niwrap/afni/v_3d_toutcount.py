# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_TOUTCOUNT_METADATA = Metadata(
    id="c36b1ad750d019209399efeb222cdbd3213201f8.boutiques",
    name="3dToutcount",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dToutcountOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_toutcount(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_afni_head: OutputPathType | None
    """Output dataset in AFNI format (HEAD file)."""
    output_afni_brik: OutputPathType | None
    """Output dataset in AFNI format (BRIK file)."""


def v_3d_toutcount(
    input_dataset: str,
    output_prefix: str | None = None,
    mask_dataset: str | None = None,
    q_threshold: float | None = None,
    autoclip: bool = False,
    automask: bool = False,
    fraction: bool = False,
    range_: bool = False,
    polort_order: float | None = None,
    legendre: bool = False,
    runner: Runner | None = None,
) -> V3dToutcountOutputs:
    """
    Calculates the number of 'outliers' in a 3D+time dataset at each time point.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dToutcount.html
    
    Args:
        input_dataset: Input 3D+time dataset (e.g. dataset+orig).
        output_prefix: Prefix of the new dataset saved with the outlier Q\
            values, applicable with the -save option.
        mask_dataset: Only count voxels in the provided mask dataset.
        q_threshold: Use 'q' instead of 0.001 in the calculation of alpha. Must\
            be within range 0 < q < 1.
        autoclip: Clip off 'small' voxels (as in 3dClipLevel). Cannot use with\
            -mask.
        automask: Automatically mask the dataset. Cannot use with -mask.
        fraction: Output the fraction of (masked) voxels which are outliers at\
            each time point, instead of the count.
        range_: Print out median+3.5*MAD of outlier count with each time point.
        polort_order: Detrend each voxel time series with polynomials of order\
            'nn'. Default value is 0, which removes the median.
        legendre: Use Legendre polynomials for detrending (also allows -polort\
            > 3).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dToutcountOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TOUTCOUNT_METADATA)
    cargs = []
    cargs.append("3dToutcount")
    cargs.append(input_dataset)
    if output_prefix is not None:
        cargs.append(output_prefix)
    cargs.append("[MASK_FLAG]")
    if mask_dataset is not None:
        cargs.extend([
            "-mask",
            mask_dataset
        ])
    if q_threshold is not None:
        cargs.extend([
            "-qthr",
            str(q_threshold)
        ])
    if autoclip:
        cargs.append("-autoclip")
    if automask:
        cargs.append("-automask")
    if fraction:
        cargs.append("-fraction")
    if range_:
        cargs.append("-range")
    if polort_order is not None:
        cargs.extend([
            "-polort",
            str(polort_order)
        ])
    if legendre:
        cargs.append("-legendre")
    ret = V3dToutcountOutputs(
        root=execution.output_file("."),
        output_afni_head=execution.output_file(output_prefix + ".HEAD") if (output_prefix is not None) else None,
        output_afni_brik=execution.output_file(output_prefix + ".BRIK") if (output_prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dToutcountOutputs",
    "V_3D_TOUTCOUNT_METADATA",
    "v_3d_toutcount",
]
