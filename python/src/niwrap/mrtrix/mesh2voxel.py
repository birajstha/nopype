# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

MESH2VOXEL_METADATA = Metadata(
    id="8a36fd16448d3836d50558c038acfae860b0c0e7",
    name="mesh2voxel",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Mesh2voxelConfig:
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


class Mesh2voxelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mesh2voxel(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output image"""


def mesh2voxel(
    source: InputPathType,
    template: InputPathType,
    output: InputPathType,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Mesh2voxelConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Mesh2voxelOutputs:
    """
    mesh2voxel by Robert E. Smith (robert.smith@florey.edu.au).
    
    Convert a mesh surface to a partial volume estimation image.
    
    
    
    References:
    
    Smith, R. E.; Tournier, J.-D.; Calamante, F. & Connelly, A.
    Anatomically-constrained tractography: Improved diffusion MRI streamlines
    tractography through effective use of anatomical information. NeuroImage,
    2012, 62, 1924-1938.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/mesh2voxel.html
    
    Args:
        source: the mesh file; note vertices must be defined in realspace
            coordinates
        template: the template image
        output: the output image
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
        NamedTuple of outputs (described in `Mesh2voxelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MESH2VOXEL_METADATA)
    cargs = []
    cargs.append("mesh2voxel")
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
    cargs.append(execution.input_file(source))
    cargs.append(execution.input_file(template))
    cargs.append(execution.input_file(output))
    ret = Mesh2voxelOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MESH2VOXEL_METADATA",
    "Mesh2voxelConfig",
    "Mesh2voxelOutputs",
    "mesh2voxel",
]
