# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


DIRFLIP_METADATA = Metadata(
    id="623c2c986c21b0eca7e5db0efcc8f3c19e7e3139",
    name="dirflip",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class DirflipConfig:
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


class DirflipOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dirflip(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out: OutputPathType
    """the output files for the directions."""


def dirflip(
    in_: InputPathType,
    out: InputPathType,
    permutations: int | None = None,
    cartesian: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DirflipConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> DirflipOutputs:
    """
    dirflip by J-Donald Tournier (jdtournier@gmail.com).
    
    Invert the polarity of individual directions so as to optimise a unipolar
    electrostatic repulsion model.
    
    The orientations themselves are not affected, only their polarity; this is
    necessary to ensure near-optimal distribution of DW directions for
    eddy-current correction.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/dirflip.html
    
    Args:
        in_: the input files for the directions.
        out: the output files for the directions.
        permutations: number of permutations to try (default: 100000000)
        cartesian: Output the directions in Cartesian coordinates [x y z]
            instead of [az el].
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
        NamedTuple of outputs (described in `DirflipOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DIRFLIP_METADATA)
    cargs = []
    cargs.append("dirflip")
    if permutations is not None:
        cargs.extend(["-permutations", str(permutations)])
    if cartesian:
        cargs.append("-cartesian")
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
    cargs.append(execution.input_file(in_))
    cargs.append(execution.input_file(out))
    ret = DirflipOutputs(
        root=execution.output_file("."),
        out=execution.output_file(f"{pathlib.Path(out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DIRFLIP_METADATA",
    "DirflipConfig",
    "DirflipOutputs",
    "dirflip",
]
