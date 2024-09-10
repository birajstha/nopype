# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TSFDIVIDE_METADATA = Metadata(
    id="7f25174a66395585bb631c223e73f5fe4356fc1d.boutiques",
    name="tsfdivide",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class TsfdivideConfig:
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
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


class TsfdivideOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tsfdivide(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output track scalar file"""


def tsfdivide(
    input1: InputPathType,
    input2: InputPathType,
    output: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TsfdivideConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> TsfdivideOutputs:
    """
    Divide corresponding values in track scalar files.
    
    
    
    References:
    
    .
    
    Author: David Raffelt (david.raffelt@florey.edu.au)
    
    URL:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/tsfdivide.html
    
    Args:
        input1: the first input track scalar file.
        input2: the second input track scalar file.
        output: the output track scalar file.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TsfdivideOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TSFDIVIDE_METADATA)
    cargs = []
    cargs.append("tsfdivide")
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend([
            "-nthreads",
            str(nthreads)
        ])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(input1))
    cargs.append(execution.input_file(input2))
    cargs.append(output)
    ret = TsfdivideOutputs(
        root=execution.output_file("."),
        output=execution.output_file(output),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TSFDIVIDE_METADATA",
    "TsfdivideConfig",
    "TsfdivideOutputs",
    "tsfdivide",
]
