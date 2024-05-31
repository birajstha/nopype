# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3DMASKAVE_METADATA = Metadata(
    id="5f0063fbadf1184c79700d33c6791df910894441",
    name="3dmaskave",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dmaskaveOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmaskave(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Output file."""


def v_3dmaskave(
    in_file: InputPathType,
    mask: InputPathType | None = None,
    num_threads: int | None = 1,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    quiet: bool = False,
    runner: Runner = None,
) -> V3dmaskaveOutputs:
    """
    3dmaskave by Nipype (interface).
    
    Computes average of all voxels in the input dataset which satisfy the
    criterion in the options list.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dmaskave.html
    
    Args:
        in_file: Input file to 3dmaskave.
        mask: Matrix to align input file.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        quiet: Matrix to align input file.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `V3dmaskaveOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMASKAVE_METADATA)
    cargs = []
    cargs.append("3dmaskave")
    cargs.append(execution.input_file(in_file))
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if quiet:
        cargs.append("-quiet")
    cargs.append("[OUT_FILE]")
    if num_threads is not None:
        cargs.append(str(num_threads))
    if outputtype is not None:
        cargs.append(outputtype)
    ret = V3dmaskaveOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(f"{pathlib.Path(in_file).name}_maskave.1D", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dmaskaveOutputs",
    "V_3DMASKAVE_METADATA",
    "v_3dmaskave",
]
