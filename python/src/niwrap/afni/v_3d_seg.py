# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_SEG_METADATA = Metadata(
    id="63ad34c87ddb712be14d2a7a985584aa16e90e17.boutiques",
    name="3dSeg",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dSegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_seg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmented_volume: OutputPathType | None
    """Segmented brain volume output"""
    bias_field: OutputPathType | None
    """Bias field estimate output"""
    classified_volume: OutputPathType | None
    """Classified volume output"""


def v_3d_seg(
    anat: InputPathType,
    mask: str | None = None,
    blur_meth: str | None = None,
    bias_fwhm: float | None = None,
    classes: str | None = None,
    bmrf: float | None = None,
    bias_classes: str | None = None,
    prefix: str | None = None,
    overwrite: bool = False,
    debug: float | None = None,
    mixfrac: str | None = None,
    mixfloor: float | None = None,
    gold: InputPathType | None = None,
    gold_bias: InputPathType | None = None,
    main_n: float | None = None,
    cset: InputPathType | None = None,
    labeltable: InputPathType | None = None,
    vox_debug: str | None = None,
    vox_debug_file: str | None = None,
    runner: Runner | None = None,
) -> V3dSegOutputs:
    """
    Segments brain volumes into tissue classes with optional global and voxelwise
    priors.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dSeg.html
    
    Args:
        anat: Volume to segment.
        mask: Mask of the volume to be segmented. Can be a dataset or 'AUTO' to\
            use AFNI's automask function.
        blur_meth: Blurring method for bias field estimation. Options: BFT,\
            BIM, BNN, LSB. Default: BFT.
        bias_fwhm: The amount of blurring used when estimating the field bias.\
            Default: 25.0.
        classes: String of class labels separated by semicolons. Default: 'CSF;\
            GM; WM'.
        bmrf: Weighting factor controlling spatial homogeneity of\
            classifications. Default: 0.0.
        bias_classes: Classes that contribute to the estimation of the bias\
            field. Default: 'GM; WM'.
        prefix: Prefix for all output volume.
        overwrite: Automatically overwrite existing files with the same prefix.
        debug: Set debug level (0, 1, or 2).
        mixfrac: Volume-wide mixing fractions for initialization. Options: '0.1\
            0.45 0.45', 'UNI', 'AVG152_BRAIN_MASK', 'IGNORE'. Default: UNI.
        mixfloor: Set the minimum value for any class's mixing fraction.\
            Default: 0.0001.
        gold: Goldstandard segmentation volume for comparison.
        gold_bias: Goldstandard bias volume for comparison.
        main_n: Number of iterations to perform. Default: 5.
        cset: Initial classification. Uses 3dkmean's engine if not provided.
        labeltable: Label table containing integer keys and corresponding\
            labels.
        vox_debug: 1D index of voxel to debug or 3D voxel indices.
        vox_debug_file: File in which debug information is output, use '-' for\
            stdout, '+' for stderr.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dSegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_SEG_METADATA)
    cargs = []
    cargs.append("3dSeg")
    cargs.append("-anat")
    cargs.append(execution.input_file(anat))
    cargs.append("-mask")
    if mask is not None:
        cargs.append(mask)
    cargs.append("-blur_meth")
    if blur_meth is not None:
        cargs.extend([
            "-blur_meth",
            blur_meth
        ])
    cargs.append("-bias_fwhm")
    if bias_fwhm is not None:
        cargs.extend([
            "-bias_fwhm",
            str(bias_fwhm)
        ])
    cargs.append("-classes")
    if classes is not None:
        cargs.extend([
            "-classes",
            classes
        ])
    cargs.append("-Bmrf")
    if bmrf is not None:
        cargs.extend([
            "-Bmrf",
            str(bmrf)
        ])
    cargs.append("-bias_classes")
    if bias_classes is not None:
        cargs.extend([
            "-bias_classes",
            bias_classes
        ])
    cargs.append("-prefix")
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    cargs.append("-overwrite")
    if overwrite:
        cargs.append("-overwrite")
    cargs.append("-debug")
    if debug is not None:
        cargs.extend([
            "-debug",
            str(debug)
        ])
    cargs.append("-mixfrac")
    if mixfrac is not None:
        cargs.extend([
            "-mixfrac",
            mixfrac
        ])
    cargs.append("-mixfloor")
    if mixfloor is not None:
        cargs.extend([
            "-mixfloor",
            str(mixfloor)
        ])
    cargs.append("-gold")
    if gold is not None:
        cargs.extend([
            "-gold",
            execution.input_file(gold)
        ])
    cargs.append("-gold_bias")
    if gold_bias is not None:
        cargs.extend([
            "-gold_bias",
            execution.input_file(gold_bias)
        ])
    cargs.append("-main_N")
    if main_n is not None:
        cargs.extend([
            "-main_N",
            str(main_n)
        ])
    cargs.append("-cset")
    if cset is not None:
        cargs.extend([
            "-cset",
            execution.input_file(cset)
        ])
    cargs.append("-labeltable")
    if labeltable is not None:
        cargs.extend([
            "-labeltable",
            execution.input_file(labeltable)
        ])
    cargs.append("-vox_debug")
    if vox_debug is not None:
        cargs.extend([
            "-vox_debug",
            vox_debug
        ])
    cargs.append("-vox_debug_file")
    if vox_debug_file is not None:
        cargs.extend([
            "-vox_debug_file",
            vox_debug_file
        ])
    ret = V3dSegOutputs(
        root=execution.output_file("."),
        segmented_volume=execution.output_file(prefix + "_Segsy+orig.HEAD") if (prefix is not None) else None,
        bias_field=execution.output_file(prefix + "_BiasField+orig.HEAD") if (prefix is not None) else None,
        classified_volume=execution.output_file(prefix + "_Classes+orig.HEAD") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dSegOutputs",
    "V_3D_SEG_METADATA",
    "v_3d_seg",
]
