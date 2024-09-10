# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FEAT_GM_PREPARE_METADATA = Metadata(
    id="69f99581f8df035a15b8bd30c71217642ca4c191.boutiques",
    name="feat_gm_prepare",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FeatGmPrepareOutputs(typing.NamedTuple):
    """
    Output object returned when calling `feat_gm_prepare(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def feat_gm_prepare(
    gm_output: str,
    feat_dirs_list: list[InputPathType],
    runner: Runner | None = None,
) -> FeatGmPrepareOutputs:
    """
    Prepare 4D grey matter files for higher-level analysis in FEAT.
    
    Author: Oxford Centre for Functional MRI of the Brain (FMRIB)
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT
    
    Args:
        gm_output: 4D grey matter output file.
        feat_dirs_list: List of first-level FEAT output directories.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FeatGmPrepareOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FEAT_GM_PREPARE_METADATA)
    cargs = []
    cargs.append("feat_gm_prepare")
    cargs.append(gm_output)
    cargs.extend([execution.input_file(f) for f in feat_dirs_list])
    ret = FeatGmPrepareOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FEAT_GM_PREPARE_METADATA",
    "FeatGmPrepareOutputs",
    "feat_gm_prepare",
]
