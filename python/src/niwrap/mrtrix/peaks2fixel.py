# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

PEAKS2FIXEL_METADATA = Metadata(
    id="108f32f0a5230d1a805b9eaeb8a37be3757e2d88",
    name="peaks2fixel",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Peaks2fixelConfig:
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


class Peaks2fixelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `peaks2fixel(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fixels: OutputPathType
    """the output fixel directory."""


def peaks2fixel(
    directions: InputPathType,
    fixels: InputPathType,
    dataname: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Peaks2fixelConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Peaks2fixelOutputs:
    """
    peaks2fixel by Robert E. Smith (robert.smith@florey.edu.au).
    
    Convert peak directions image to a fixel directory.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/peaks2fixel.html
    
    Args:
        directions: the input directions image; each volume corresponds to the
            x, y & z component of each direction vector in turn.
        fixels: the output fixel directory.
        dataname: the name of the output fixel data file encoding peak
            amplitudes
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
        NamedTuple of outputs (described in `Peaks2fixelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PEAKS2FIXEL_METADATA)
    cargs = []
    cargs.append("peaks2fixel")
    if dataname is not None:
        cargs.extend(["-dataname", dataname])
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
    cargs.append(execution.input_file(directions))
    cargs.append(execution.input_file(fixels))
    ret = Peaks2fixelOutputs(
        root=execution.output_file("."),
        fixels=execution.output_file(f"{pathlib.Path(fixels).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PEAKS2FIXEL_METADATA",
    "Peaks2fixelConfig",
    "Peaks2fixelOutputs",
    "peaks2fixel",
]
