# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_BRICK_STAT_METADATA = Metadata(
    id="b6cfada5677faa0590beb41506633a0faad5925a",
    name="3dBrickStat",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni:latest",
)


class V3dBrickStatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_brick_stat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    console_output: OutputPathType
    """Console output of computed statistics"""


def v_3d_brick_stat(
    dataset: str,
    quick: bool = False,
    slow: bool = False,
    min_: bool = False,
    max_: bool = False,
    mean: bool = False,
    sum_: bool = False,
    var: bool = False,
    stdev: bool = False,
    count: bool = False,
    volume: bool = False,
    positive: bool = False,
    negative: bool = False,
    zero: bool = False,
    non_positive: bool = False,
    non_negative: bool = False,
    non_zero: bool = False,
    absolute: bool = False,
    nan: bool = False,
    nonan: bool = False,
    mask: str | None = None,
    mrange: list[float | int] | None = None,
    mvalue: float | int | None = None,
    automask: bool = False,
    percentile: list[float | int] | None = None,
    perclist: list[float | int] | None = None,
    median: bool = False,
    perc_quiet: bool = False,
    ver: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> V3dBrickStatOutputs:
    """
    3dBrickStat by AFNI Team.
    
    Compute voxel statistics of an input dataset.
    
    More information: https://afni.nimh.nih.gov
    
    Args:
        dataset: Input dataset.
        quick: Get the information from the header only (default).
        slow: Read the whole dataset to find the min and max values.
        min_: Print the minimum value in dataset.
        max_: Print the maximum value in dataset (default).
        mean: Print the mean value in dataset.
        sum_: Print the sum of values in the dataset.
        var: Print the variance in the dataset.
        stdev: Print the standard deviation in the dataset.
        count: Print the number of voxels included.
        volume: Print the volume of voxels included in microliters.
        positive: Include only positive voxel values.
        negative: Include only negative voxel values.
        zero: Include only zero voxel values.
        non_positive: Include only voxel values 0 or negative.
        non_negative: Include only voxel values 0 or greater.
        non_zero: Include only voxel values not equal to 0.
        absolute: Use absolute value of voxel values for all calculations.
        nan: Include only voxel values that are NaN or inf. Forces -slow mode.
        nonan: Exclude voxel values that are NaN or inf.
        mask: Use the specified dataset as mask to include/exclude voxels.
        mrange: Only accept values between MIN and MAX (inclusive) from the\
            mask.
        mvalue: Only accept values equal to VAL from the mask.
        automask: Automatically compute mask for dataset. Cannot be combined\
            with -mask.
        percentile: Compute and print percentile values from p0% to p1% at a\
            step of ps%. Only one sub-brick is accepted as input with this option.
        perclist: Like -percentile, but output the given percentiles.
        median: Shortcut for -percentile 50 1 50 (or -perclist 1 50).
        perc_quiet: Only print percentile results, not input percentile cutoffs.
        ver: Print author and version info.
        help_: Print help screen.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dBrickStatOutputs`).
    """
    runner = runner or get_global_runner()
    if mrange is not None and (len(mrange) != 2): 
        raise ValueError(f"Length of 'mrange' must be 2 but was {len(mrange)}")
    if percentile is not None and (len(percentile) != 3): 
        raise ValueError(f"Length of 'percentile' must be 3 but was {len(percentile)}")
    execution = runner.start_execution(V_3D_BRICK_STAT_METADATA)
    cargs = []
    cargs.append("3dBrickStat")
    cargs.append("[OPTIONS]")
    cargs.append(dataset)
    ret = V3dBrickStatOutputs(
        root=execution.output_file("."),
        console_output=execution.output_file(f"output.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dBrickStatOutputs",
    "V_3D_BRICK_STAT_METADATA",
    "v_3d_brick_stat",
]
