# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


MRCAT_METADATA = Metadata(
    id="680f5ea472ee036106b336468d400c70b4396107",
    name="mrcat",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class MrcatConfig:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value: str
    """temporarily set the value of an MRtrix config file entry."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


class MrcatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrcat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output image."""


def mrcat(
    image1: InputPathType,
    image2: list[InputPathType],
    output: InputPathType,
    axis: int | None = None,
    datatype: typing.Literal["spec"] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrcatConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> MrcatOutputs:
    """
    mrcat by J-Donald Tournier (jdtournier@gmail.com) and Robert E. Smith
    (robert.smith@florey.edu.au).
    
    Concatenate several images into one.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/mrcat.html
    
    Args:
        image1: the first input image.
        image2: additional input image(s).
        output: the output image.
        axis: specify axis along which concatenation should be performed. By
            default, the program will use the last non-singleton, non-spatial axis
            of any of the input images - in other words axis 3 or whichever axis
            (greater than 3) of the input images has size greater than one.
        datatype: specify output image data type. Valid choices are: float32,
            float32le, float32be, float64, float64le, float64be, int64, uint64,
            int64le, uint64le, int64be, uint64be, int32, uint32, int32le, uint32le,
            int32be, uint32be, int16, uint16, int16le, uint16le, int16be, uint16be,
            cfloat32, cfloat32le, cfloat32be, cfloat64, cfloat64le, cfloat64be,
            int8, uint8, bit.
        info: display information messages.
        quiet: do not display information messages or progress status;
            alternatively, this can be achieved by setting the MRTRIX_QUIET
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications (set
            to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MrcatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRCAT_METADATA)
    cargs = []
    cargs.append("mrcat")
    if axis is not None:
        cargs.extend(["-axis", str(axis)])
    if datatype is not None:
        cargs.extend(["-datatype", datatype])
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend(["-nthreads", str(nthreads)])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(image1))
    cargs.extend([execution.input_file(f) for f in image2])
    cargs.append(execution.input_file(output))
    ret = MrcatOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRCAT_METADATA",
    "MrcatConfig",
    "MrcatOutputs",
    "mrcat",
]
