# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


SH2RESPONSE_METADATA = Metadata(
    id="cd90807121faa735f09e431bfb89683b88ec64a8",
    name="sh2response",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Sh2responseConfig:
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


class Sh2responseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sh2response(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    response: OutputPathType
    """the output axially-symmetric spherical harmonic coefficients"""
    dump: OutputPathType | None
    """dump the m=0 SH coefficients from all voxels in the mask to the output file, rather than their mean """


def sh2response(
    sh: InputPathType,
    mask: InputPathType,
    directions: InputPathType,
    response: InputPathType,
    lmax: int | None = None,
    dump: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Sh2responseConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Sh2responseOutputs:
    """
    sh2response by J-Donald Tournier (jdtournier@gmail.com).
    
    Generate an appropriate response function from the image data for spherical
    deconvolution.
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/sh2response.html
    
    Args:
        sh: the spherical harmonic decomposition of the diffusion-weighted
            images
        mask: the mask containing the voxels from which to estimate the response
            function
        directions: a 4D image containing the direction vectors along which to
            estimate the response function
        response: the output axially-symmetric spherical harmonic coefficients
        lmax: specify the maximum harmonic degree of the response function to
            estimate
        dump: dump the m=0 SH coefficients from all voxels in the mask to the
            output file, rather than their mean
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
        NamedTuple of outputs (described in `Sh2responseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SH2RESPONSE_METADATA)
    cargs = []
    cargs.append("sh2response")
    if lmax is not None:
        cargs.extend(["-lmax", str(lmax)])
    if dump is not None:
        cargs.extend(["-dump", execution.input_file(dump)])
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
    cargs.append(execution.input_file(sh))
    cargs.append(execution.input_file(mask))
    cargs.append(execution.input_file(directions))
    cargs.append(execution.input_file(response))
    ret = Sh2responseOutputs(
        root=execution.output_file("."),
        response=execution.output_file(f"{pathlib.Path(response).stem}"),
        dump=execution.output_file(f"{pathlib.Path(dump).stem}") if dump is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SH2RESPONSE_METADATA",
    "Sh2responseConfig",
    "Sh2responseOutputs",
    "sh2response",
]
