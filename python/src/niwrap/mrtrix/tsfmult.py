# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


TSFMULT_METADATA = Metadata(
    id="51a55d0fbf2d52e451ad501e141ad5ad21b5dcbc",
    name="tsfmult",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class TsfmultConfig:
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


class TsfmultOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tsfmult(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output track scalar file"""


def tsfmult(
    input1: InputPathType,
    input1_: InputPathType,
    output: InputPathType,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TsfmultConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> TsfmultOutputs:
    """
    tsfmult by David Raffelt (david.raffelt@florey.edu.au).
    
    Multiply corresponding values in track scalar files.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/tsfmult.html
    
    Args:
        input1: the first input track scalar file.
        input1_: the second input track scalar file.
        output: the output track scalar file
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
        NamedTuple of outputs (described in `TsfmultOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TSFMULT_METADATA)
    cargs = []
    cargs.append("tsfmult")
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
    cargs.append(execution.input_file(input1_))
    cargs.append(execution.input_file(input1_))
    cargs.append(execution.input_file(output))
    ret = TsfmultOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TSFMULT_METADATA",
    "TsfmultConfig",
    "TsfmultOutputs",
    "tsfmult",
]
