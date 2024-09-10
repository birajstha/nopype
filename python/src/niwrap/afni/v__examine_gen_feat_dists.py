# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__EXAMINE_GEN_FEAT_DISTS_METADATA = Metadata(
    id="32fe2d53b70631da048d20b3842cc39a9c63f7a8.boutiques",
    name="@ExamineGenFeatDists",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class VExamineGenFeatDistsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__examine_gen_feat_dists(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__examine_gen_feat_dists(
    features_dir: str,
    wildcards: list[str] | None = None,
    output_suffix: str | None = None,
    exclude_features: list[str] | None = None,
    exclude_classes: list[str] | None = None,
    output_dir: str | None = None,
    panels_horizontal: float | None = None,
    echo: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> VExamineGenFeatDistsOutputs:
    """
    Examine histograms produced by 3dGenFeatDists.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@ExamineGenFeatDists.html
    
    Args:
        features_dir: Output directory of 3dGenFeatDists.
        wildcards: Wildcards used to select feature histograms under the\
            directory.
        output_suffix: Output suffix, added to output images. Default is\
            'nosuff'.
        exclude_features: Exclude following features. String matching is\
            partial.
        exclude_classes: Exclude following classes. String matching is partial.
        output_dir: Output directory, default is the same as -fdir.
        panels_horizontal: Set number of panels along the horizontal direction.
        echo: Set echo.
        help_: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VExamineGenFeatDistsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__EXAMINE_GEN_FEAT_DISTS_METADATA)
    cargs = []
    cargs.append("@ExamineGenFeatDists")
    cargs.append("-fdir")
    cargs.extend([
        "-fdir",
        features_dir
    ])
    cargs.append("-fwild")
    if wildcards is not None:
        cargs.extend([
            "-fwild",
            *wildcards
        ])
    cargs.append("-suffix")
    if output_suffix is not None:
        cargs.extend([
            "-suffix",
            output_suffix
        ])
    cargs.append("-exfeat")
    if exclude_features is not None:
        cargs.extend([
            "-exfeat",
            *exclude_features
        ])
    cargs.append("-exclass")
    if exclude_classes is not None:
        cargs.extend([
            "-exclass",
            *exclude_classes
        ])
    cargs.append("-odir")
    if output_dir is not None:
        cargs.extend([
            "-odir",
            output_dir
        ])
    cargs.append("-nx")
    if panels_horizontal is not None:
        cargs.extend([
            "-nx",
            str(panels_horizontal)
        ])
    cargs.append("-echo")
    if echo:
        cargs.append("-echo")
    cargs.append("-help")
    if help_:
        cargs.append("-help")
    ret = VExamineGenFeatDistsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VExamineGenFeatDistsOutputs",
    "V__EXAMINE_GEN_FEAT_DISTS_METADATA",
    "v__examine_gen_feat_dists",
]
