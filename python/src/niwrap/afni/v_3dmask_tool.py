# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3DMASK_TOOL_METADATA = Metadata(
    id="cbf01b2f7b4075038f6646036994946770b1c277",
    name="3dmask_tool",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dmaskToolOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmask_tool(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Mask file."""


def v_3dmask_tool(
    in_file: InputPathType,
    count: bool = False,
    datum: typing.Literal["byte", "short", "float"] | None = None,
    dilate_inputs: str | None = None,
    dilate_results: str | None = None,
    fill_dirs: str | None = None,
    fill_holes: bool = False,
    frac: float | int | None = None,
    inter: bool = False,
    num_threads: int | None = 1,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    union: bool = False,
    verbose: int | None = None,
    runner: Runner = None,
) -> V3dmaskToolOutputs:
    """
    3dmask_tool by Nipype (interface).
    
    3dmask_tool - for combining/dilating/eroding/filling masks.
    
    More information:
    https://afni.nimh.nih.gov/pub../pub/dist/doc/program_help/3dmask_tool.html
    
    Args:
        in_file: Input file to 3dmask_tool.
        count: Instead of created a binary 0/1 mask dataset, create one with
            counts of voxel overlap, i.e., each voxel will contain the number of
            masks that it is set in.
        datum: 'byte' or 'short' or 'float'. Specify data type for output.
        dilate_inputs: Use this option to dilate and/or erode datasets as they
            are read. ex. '5 -5' to dilate and erode 5 times.
        dilate_results: Dilate and/or erode combined mask at the given levels.
        fill_dirs: Fill holes only in the given directions. this option is for
            use with -fill holes. should be a single string that specifies 1-3 of
            the axes using {x,y,z} labels (i.e. dataset axis order), or using the
            labels in {r,l,a,p,i,s}.
        fill_holes: This option can be used to fill holes in the resulting mask,
            i.e. after all other processing has been done.
        frac: When combining masks (across datasets and sub-bricks), use this
            option to restrict the result to a certain fraction of the set of
            volumes.
        inter: Intersection, this means -frac 1.0.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        union: Union, this means -frac 0.
        verbose: Specify verbosity level, for 0 to 3.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `V3dmaskToolOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMASK_TOOL_METADATA)
    cargs = []
    cargs.append("3dmask_tool")
    if count:
        cargs.append("-count")
    cargs.extend(["-input", execution.input_file(in_file)])
    if datum is not None:
        cargs.extend(["-datum", datum])
    if dilate_inputs is not None:
        cargs.extend(["-dilate_inputs", dilate_inputs])
    if dilate_results is not None:
        cargs.extend(["-dilate_results", dilate_results])
    if fill_dirs is not None:
        cargs.extend(["-fill_dirs", fill_dirs])
    if fill_holes:
        cargs.append("-fill_holes")
    if frac is not None:
        cargs.extend(["-frac", str(frac)])
    if inter:
        cargs.append("-inter")
    if num_threads is not None:
        cargs.append(str(num_threads))
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    if union:
        cargs.append("-union")
    if verbose is not None:
        cargs.extend(["-verb", str(verbose)])
    ret = V3dmaskToolOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(f"{pathlib.Path(in_file).name}_mask", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dmaskToolOutputs",
    "V_3DMASK_TOOL_METADATA",
    "v_3dmask_tool",
]
