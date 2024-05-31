# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

FIXEL2VOXEL_METADATA = Metadata(
    id="0fd989afccfcaf270175db584daceba2f0944b02",
    name="fixel2voxel",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Fixel2voxelConfig:
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


class Fixel2voxelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fixel2voxel(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    image_out: OutputPathType
    """the output scalar image."""


def fixel2voxel(
    fixel_in: InputPathType,
    operation: typing.Literal["operation"],
    image_out: InputPathType,
    number: int | None = None,
    fill: float | int | None = None,
    weighted: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Fixel2voxelConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Fixel2voxelOutputs:
    """
    fixel2voxel by Robert E. Smith (robert.smith@florey.edu.au) & David Raffelt
    (david.raffelt@florey.edu.au).
    
    Convert a fixel-based sparse-data image into some form of scalar image.
    
    Fixel data can be reduced to voxel data in a number of ways:
    
    - Some statistic computed across all fixel values within a voxel: mean, sum,
    product, min, max, absmax, magmax
    
    - The number of fixels in each voxel: count
    
    - Some measure of crossing-fibre organisation: complexity, sf
    ('single-fibre')
    
    - A 4D directionally-encoded colour image: dec_unit, dec_scaled
    
    - A 4D image containing all fixel data values in each voxel unmodified: none
    
    The -weighted option deals with the case where there is some per-fixel
    metric of interest that you wish to collapse into a single scalar measure
    per voxel, but each fixel possesses a different volume, and you wish for
    those fixels with greater volume to have a greater influence on the
    calculation than fixels with lesser volume. For instance, when estimating a
    voxel-based measure of mean axon diameter from per-fixel mean axon
    diameters, a fixel's mean axon diameter should be weigthed by its relative
    volume within the voxel in the calculation of that voxel mean.
    
    References:
    
    * Reference for 'complexity' operation:
    Riffert, T. W.; Schreiber, J.; Anwander, A. & Knosche, T. R. Beyond
    Fractional Anisotropy: Extraction of bundle-specific structural metrics from
    crossing fibre models. NeuroImage, 2014, 100, 176-191.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/fixel2voxel.html
    
    Args:
        fixel_in: the input fixel data file
        operation: the operation to apply, one of: mean, sum, product, min, max,
            absmax, magmax, count, complexity, sf, dec_unit, dec_scaled, none.
        image_out: the output scalar image.
        number: use only the largest N fixels in calculation of the voxel-wise
            statistic; in the case of operation "none", output only the largest N
            fixels in each voxel.
        fill: for "none" operation, specify the value to fill when number of
            fixels is fewer than the maximum (default: 0.0)
        weighted: weight the contribution of each fixel to the per-voxel result
            according to its volume.
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
        NamedTuple of outputs (described in `Fixel2voxelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIXEL2VOXEL_METADATA)
    cargs = []
    cargs.append("fixel2voxel")
    if number is not None:
        cargs.extend(["-number", str(number)])
    if fill is not None:
        cargs.extend(["-fill", str(fill)])
    if weighted is not None:
        cargs.extend(["-weighted", execution.input_file(weighted)])
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
    cargs.append(operation)
    cargs.append(execution.input_file(image_out))
    ret = Fixel2voxelOutputs(
        root=execution.output_file("."),
        image_out=execution.output_file(f"{pathlib.Path(image_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIXEL2VOXEL_METADATA",
    "Fixel2voxelConfig",
    "Fixel2voxelOutputs",
    "fixel2voxel",
]
