# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

AMP2RESPONSE_METADATA = Metadata(
    id="66d0adbe8cc1fb477aad13601a463061122d577e",
    name="amp2response",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Amp2responseConfig:
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


class Amp2responseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `amp2response(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    response: OutputPathType
    """the output zonal spherical harmonic coefficients"""


def amp2response(
    amps: InputPathType,
    mask: InputPathType,
    directions: InputPathType,
    response: InputPathType,
    isotropic: bool = False,
    noconstraint: bool = False,
    directions_: InputPathType | None = None,
    shells: list[float | int] = None,
    lmax: list[int] = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Amp2responseConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Amp2responseOutputs:
    """
    amp2response by Robert E. Smith (robert.smith@florey.edu.au) and J-Donald
    Tournier (jdtournier@gmail.com).
    
    Estimate response function coefficients based on the DWI signal in
    single-fibre voxels.
    
    This command uses the image data from all selected single-fibre voxels
    concurrently, rather than simply averaging their individual spherical
    harmonic coefficients. It also ensures that the response function is
    non-negative, and monotonic (i.e. its amplitude must increase from the fibre
    direction out to the orthogonal plane).
    
    If multi-shell data are provided, and one or more b-value shells are not
    explicitly requested, the command will generate a response function for
    every b-value shell (including b=0 if present).
    
    References:
    
    Smith, R. E.; Dhollander, T. & Connelly, A. Constrained linear least squares
    estimation of anisotropic response function for spherical deconvolution.
    ISMRM Workshop on Breaking the Barriers of Diffusion MRI, 23.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/amp2response.html
    
    Args:
        amps: the amplitudes image
        mask: the mask containing the voxels from which to estimate the response
            function
        directions: a 4D image containing the estimated fibre directions
        response: the output zonal spherical harmonic coefficients
        isotropic: estimate an isotropic response function (lmax=0 for all
            shells)
        noconstraint: disable the non-negativity and monotonicity constraints
        directions_: provide an external text file containing the directions
            along which the amplitudes are sampled
        shells: specify one or more b-values to use during processing, as a
            comma-separated list of the desired approximate b-values (b-values are
            clustered to allow for small deviations). Note that some commands are
            incompatible with multiple b-values, and will report an error if more
            than one b-value is provided.
            WARNING: note that, even though the b=0 volumes are never
            referred to as shells in the literature, they still have to
            be explicitly included in the list of b-values as provided
            to the -shell option! Several algorithms which include the
            b=0 volumes in their computations may otherwise return an
            undesired result.
        lmax: specify the maximum harmonic degree of the response function to
            estimate (can be a comma-separated list for multi-shell data)
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
        NamedTuple of outputs (described in `Amp2responseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AMP2RESPONSE_METADATA)
    cargs = []
    cargs.append("amp2response")
    if isotropic:
        cargs.append("-isotropic")
    if noconstraint:
        cargs.append("-noconstraint")
    if directions_ is not None:
        cargs.extend(["-directions", execution.input_file(directions_)])
    if shells is not None:
        cargs.extend(["-shells", *map(str, shells)])
    if lmax is not None:
        cargs.extend(["-lmax", *map(str, lmax)])
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
    cargs.append(execution.input_file(amps))
    cargs.append(execution.input_file(mask))
    cargs.append(execution.input_file(directions))
    cargs.append(execution.input_file(response))
    ret = Amp2responseOutputs(
        root=execution.output_file("."),
        response=execution.output_file(f"{pathlib.Path(response).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AMP2RESPONSE_METADATA",
    "Amp2responseConfig",
    "Amp2responseOutputs",
    "amp2response",
]
