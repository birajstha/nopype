# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


DIRGEN_METADATA = Metadata(
    id="d8a2463c6a881a3c32aad11a31200b363d898fd8",
    name="dirgen",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class DirgenConfig:
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


class DirgenOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dirgen(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dirs: OutputPathType
    """the text file to write the directions to, as [ az el ] pairs."""


def dirgen(
    ndir: int,
    dirs: InputPathType,
    power: int | None = None,
    niter: int | None = None,
    restarts: int | None = None,
    unipolar: bool = False,
    cartesian: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DirgenConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> DirgenOutputs:
    """
    dirgen by J-Donald Tournier (jdtournier@gmail.com).
    
    Generate a set of uniformly distributed directions using a bipolar
    electrostatic repulsion model.
    
    Directions are distributed by analogy to an electrostatic repulsion system,
    with each direction corresponding to a single electrostatic charge (for
    -unipolar), or a pair of diametrically opposed charges (for the default
    bipolar case). The energy of the system is determined based on the Coulomb
    repulsion, which assumes the form 1/r^power, where r is the distance between
    any pair of charges, and p is the power assumed for the repulsion law
    (default: 1). The minimum energy state is obtained by gradient descent.
    
    References:
    
    Jones, D.; Horsfield, M. & Simmons, A. Optimal strategies for measuring
    diffusion in anisotropic systems by magnetic resonance imaging. Magnetic
    Resonance in Medicine, 1999, 42: 515-525
    
    Papadakis, N. G.; Murrills, C. D.; Hall, L. D.; Huang, C. L.-H. & Adrian
    Carpenter, T. Minimal gradient encoding for robust estimation of diffusion
    anisotropy. Magnetic Resonance Imaging, 2000, 18: 671-679.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/dirgen.html
    
    Args:
        ndir: the number of directions to generate.
        dirs: the text file to write the directions to, as [ az el ] pairs.
        power: specify exponent to use for repulsion power law (default: 1).
            This must be a power of 2 (i.e. 1, 2, 4, 8, 16, ...).
        niter: specify the maximum number of iterations to perform (default:
            10000).
        restarts: specify the number of restarts to perform (default: 10).
        unipolar: optimise assuming a unipolar electrostatic repulsion model
            rather than the bipolar model normally assumed in DWI
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
        NamedTuple of outputs (described in `DirgenOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DIRGEN_METADATA)
    cargs = []
    cargs.append("dirgen")
    if power is not None:
        cargs.extend(["-power", str(power)])
    if niter is not None:
        cargs.extend(["-niter", str(niter)])
    if restarts is not None:
        cargs.extend(["-restarts", str(restarts)])
    if unipolar:
        cargs.append("-unipolar")
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
    cargs.append(str(ndir))
    cargs.append(execution.input_file(dirs))
    ret = DirgenOutputs(
        root=execution.output_file("."),
        dirs=execution.output_file(f"{pathlib.Path(dirs).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DIRGEN_METADATA",
    "DirgenConfig",
    "DirgenOutputs",
    "dirgen",
]
