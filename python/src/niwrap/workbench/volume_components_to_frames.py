# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

VOLUME_COMPONENTS_TO_FRAMES_METADATA = Metadata(
    id="e33a704ae3a960fa92f5343717d9bcdf31d2d4b1",
    name="volume-components-to-frames",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VolumeComponentsToFramesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_components_to_frames(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the input volume converted to multiple frames of scalar type"""


def volume_components_to_frames(
    input_: InputPathType,
    output: InputPathType,
    runner: Runner = None,
) -> VolumeComponentsToFramesOutputs:
    """
    volume-components-to-frames by Washington University School of Medicin.
    
    Convert rgb/complex volume to frames.
    
    RGB and complex datatypes are not always well supported, this command allows
    separating them into standard subvolumes for better support.
    
    Args:
        input_: the RGB/complex-type volume
        output: the input volume converted to multiple frames of scalar type
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeComponentsToFramesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_COMPONENTS_TO_FRAMES_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-components-to-frames")
    cargs.append(execution.input_file(input_))
    cargs.append(execution.input_file(output))
    ret = VolumeComponentsToFramesOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_COMPONENTS_TO_FRAMES_METADATA",
    "VolumeComponentsToFramesOutputs",
    "volume_components_to_frames",
]
