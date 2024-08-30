# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

MIDTRANS_METADATA = Metadata(
    id="b39eff2ab1a7b0607739374c3b6c7f807e455f79",
    name="midtrans",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class MidtransOutputs(typing.NamedTuple):
    """
    Output object returned when calling `midtrans(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def midtrans(
    transforms: list[InputPathType],
    output_matrix: str | None = None,
    template_image: InputPathType | None = None,
    separate_basename: str | None = None,
    debug_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> MidtransOutputs:
    """
    midtrans by University of Oxford (Mark Jenkinson).
    
    Calculate the midpoint transform from a series of input transforms.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/
    
    Args:
        transforms: List of input transform files (e.g. transform1.mat\
            transform2.mat ... transformN.mat).
        output_matrix: Output filename for the resulting matrix.
        template_image: Input filename for template image (needed for fix\
            origin).
        separate_basename: Basename for the output of separate matrices (final\
            name includes a number; e.g. img2mid0001.mat).
        debug_flag: Switch on debugging output.
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MidtransOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MIDTRANS_METADATA)
    cargs = []
    cargs.append("midtrans")
    cargs.append("[OPTIONS]")
    cargs.extend([execution.input_file(f) for f in transforms])
    cargs.append("[TRANSFORM2]")
    cargs.append("...")
    cargs.append("[TRANSFORMN]")
    ret = MidtransOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MIDTRANS_METADATA",
    "MidtransOutputs",
    "midtrans",
]
