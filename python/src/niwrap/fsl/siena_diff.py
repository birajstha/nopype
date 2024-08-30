# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SIENA_DIFF_METADATA = Metadata(
    id="216bf3ce45f1e54242617d4b44133c1c163b5360",
    name="siena_diff",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class SienaDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `siena_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def siena_diff(
    input1_basename: str,
    input2_basename: str,
    debug_flag: bool = False,
    no_seg_flag: bool = False,
    self_corr_factor: float | int | None = None,
    ignore_z_flow_flag: bool = False,
    apply_std_mask_flag: bool = False,
    segment_options: str | None = None,
    runner: Runner | None = None,
) -> SienaDiffOutputs:
    """
    siena_diff by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    SIENA_diff: Analysis of longitudinal brain image differences.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/SIENA
    
    Args:
        input1_basename: Input image 1 basename.
        input2_basename: Input image 2 basename.
        debug_flag: Debug - generate edge images and don't remove temporary\
            images.
        no_seg_flag: Don't segment grey+white separately (because there is poor\
            grey-white contrast).
        self_corr_factor: Apply self-calibrating correction factor.
        ignore_z_flow_flag: Ignore flow in z (may be beneficial if top of brain\
            is missing).
        apply_std_mask_flag: Apply <input1_basename>_stdmask to brain edge\
            points.
        segment_options: Options to be passed to segmentation (type 'fast' to\
            get these).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SienaDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIENA_DIFF_METADATA)
    cargs = []
    cargs.append("siena_diff")
    cargs.append(input1_basename)
    cargs.append(input2_basename)
    if debug_flag:
        cargs.append("-d")
    if no_seg_flag:
        cargs.append("-2")
    if self_corr_factor is not None:
        cargs.extend(["-c", str(self_corr_factor)])
    if ignore_z_flow_flag:
        cargs.append("-i")
    if apply_std_mask_flag:
        cargs.append("-m")
    if segment_options is not None:
        cargs.extend(["-s", segment_options])
    ret = SienaDiffOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SIENA_DIFF_METADATA",
    "SienaDiffOutputs",
    "siena_diff",
]
