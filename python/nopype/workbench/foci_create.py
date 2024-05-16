# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.751311

import typing

from ..styxdefs import *


FOCI_CREATE_METADATA = Metadata(
    id="3a444f76b9645b7937d06aff7a34b2df677ea0f5",
    name="foci-create",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class FociCreateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `foci_create(...)`.
    """
    output: OutputPathType
    """the output foci file"""


def foci_create(
    runner: Runner,
    output: InputPathType,
) -> FociCreateOutputs:
    """
    CREATE A FOCI FILE.
    
    Creates a foci file from names, coordinates, and RGB values in a text file.
    The text file must have the following format (2 lines per focus):
    
    <focus-name>
    <red> <green> <blue> <x> <y> <z>
    ...
    
    Foci names are specified on a separate line from their coordinates and
    color, in order to let foci names contain spaces. Whitespace is trimmed from
    both ends of the foci name, but is kept if it is in the middle of a name.
    The values of <red>, <green>, <blue> and must be integers from 0 to 255, and
    will specify the color the foci is drawn as.
    
    Foci are grouped into classes and the name for the class is specified using
    the <class-name> parameter.
    
    All foci within one text file must be associated with the structure
    contained in the <surface> parameter and are projected to that surface.
    
    Args:
        runner: Command runner
        output: the output foci file
    Returns:
        NamedTuple of outputs (described in `FociCreateOutputs`).
    """
    execution = runner.start_execution(FOCI_CREATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-foci-create")
    cargs.append(execution.input_file(output))
    ret = FociCreateOutputs(
        output=execution.output_file(f"{output}"),
    )
    execution.run(cargs)
    return ret
