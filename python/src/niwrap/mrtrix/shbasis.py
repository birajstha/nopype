# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


SHBASIS_METADATA = Metadata(
    id="f5015a6fa580efa3089db741e6b2ed5b913d793b",
    name="shbasis",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class ShbasisConfig:
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


class ShbasisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `shbasis(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def shbasis(
    sh: list[InputPathType],
    convert: typing.Literal["mode"] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[ShbasisConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> ShbasisOutputs:
    """
    shbasis by Robert E. Smith (robert.smith@florey.edu.au).
    
    Examine the values in spherical harmonic images to estimate (and optionally
    change) the SH basis used.
    
    In previous versions of MRtrix, the convention used for storing spherical
    harmonic coefficients was a non-orthonormal basis (the m!=0 coefficients
    were a factor of sqrt(2) too large). This error has been rectified in newer
    versions of MRtrix, but will cause issues if processing SH data that was
    generated using an older version of MRtrix (or vice-versa).
    
    This command provides a mechanism for testing the basis used in storage of
    image data representing a spherical harmonic series per voxel, and allows
    the user to forcibly modify the raw image data to conform to the desired
    basis.
    
    Note that the "force_*" conversion choices should only be used in cases
    where this command has previously been unable to automatically determine the
    SH basis from the image data, but the user themselves are confident of the
    SH basis of the data.
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/shbasis.html
    
    Args:
        sh: the input image(s) of SH coefficients.
        convert: convert the image data in-place to the desired basis; options
            are: old,new,force_oldtonew,force_newtoold.
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
        NamedTuple of outputs (described in `ShbasisOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SHBASIS_METADATA)
    cargs = []
    cargs.append("shbasis")
    if convert is not None:
        cargs.extend(["-convert", convert])
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
    cargs.extend([execution.input_file(f) for f in sh])
    ret = ShbasisOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SHBASIS_METADATA",
    "ShbasisConfig",
    "ShbasisOutputs",
    "shbasis",
]
