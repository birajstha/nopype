# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

POSSUM_INTERPMOT_METADATA = Metadata(
    id="4ca0ea9a800707082a716f008fc67bd2495446e9",
    name="possum_interpmot",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class PossumInterpmotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `possum_interpmot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Interpolated motion output file"""


def possum_interpmot(
    motion_type: int,
    tr: float | int,
    tr_slice: float | int,
    nslices: int,
    nvols: int,
    custom_motion_file: InputPathType,
    output_file: str,
    runner: Runner | None = None,
) -> PossumInterpmotOutputs:
    """
    possum_interpmot by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Position Interpolation for Movers and Shakers.
    
    More information: https://fsl.fmrib.ox.ac.uk
    
    Args:
        motion_type: Type of motion: 0 for continuous, 1 for between slices, 2\
            for between volumes.
        tr: Repetition time in seconds.
        tr_slice: Slice repetition time in seconds.
        nslices: Number of slices.
        nvols: Number of volumes.
        custom_motion_file: Custom motion file.
        output_file: Output file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PossumInterpmotOutputs`).
    """
    runner = runner or get_global_runner()
    if not (0 <= motion_type <= 2): 
        raise ValueError(f"'motion_type' must be between 0 <= x <= 2 but was {motion_type}")
    execution = runner.start_execution(POSSUM_INTERPMOT_METADATA)
    cargs = []
    cargs.append("/usr/local/fsl/bin/possum_interpmot.py")
    cargs.append(str(motion_type))
    cargs.append(str(tr))
    cargs.append(str(tr_slice))
    cargs.append(str(nslices))
    cargs.append(str(nvols))
    cargs.append(execution.input_file(custom_motion_file))
    cargs.append(output_file)
    ret = PossumInterpmotOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"{output_file}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "POSSUM_INTERPMOT_METADATA",
    "PossumInterpmotOutputs",
    "possum_interpmot",
]
