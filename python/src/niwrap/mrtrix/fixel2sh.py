# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


FIXEL2SH_METADATA = Metadata(
    id="b0874dbe0f4ee51a9228efae12fd64b31c7391ac",
    name="fixel2sh",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Fixel2shConfig:
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


class Fixel2shOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fixel2sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    sh_out: OutputPathType
    """the output sh image."""


def fixel2sh(
    fixel_in: InputPathType,
    sh_out: InputPathType,
    lmax: int | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Fixel2shConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Fixel2shOutputs:
    """
    fixel2sh by Robert E. Smith (robert.smith@florey.edu.au) & David Raffelt
    (david.raffelt@florey.edu.au).
    
    Convert a fixel-based sparse-data image into an spherical harmonic image.
    
    This command generates spherical harmonic data from fixels that can be
    visualised using the ODF tool in MRview. The output ODF lobes are scaled
    according to the values in the input fixel image.
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/fixel2sh.html
    
    Args:
        fixel_in: the input fixel data file.
        sh_out: the output sh image.
        lmax: set the maximum harmonic order for the output series (Default: 8)
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
        NamedTuple of outputs (described in `Fixel2shOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIXEL2SH_METADATA)
    cargs = []
    cargs.append("fixel2sh")
    if lmax is not None:
        cargs.extend(["-lmax", str(lmax)])
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
    cargs.append(execution.input_file(fixel_in))
    cargs.append(execution.input_file(sh_out))
    ret = Fixel2shOutputs(
        root=execution.output_file("."),
        sh_out=execution.output_file(f"{pathlib.Path(sh_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIXEL2SH_METADATA",
    "Fixel2shConfig",
    "Fixel2shOutputs",
    "fixel2sh",
]
