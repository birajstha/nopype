# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

TCKSAMPLE_METADATA = Metadata(
    id="b1f50b9b6fdb73f7fd985293f25ea6ad65a8657c",
    name="tcksample",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class TcksampleConfig:
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


class TcksampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tcksample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    values_: OutputPathType
    """the output sampled values"""


def tcksample(
    tracks: InputPathType,
    image: InputPathType,
    values_: InputPathType,
    stat_tck: typing.Literal["statistic"] | None = None,
    nointerp: bool = False,
    precise: bool = False,
    use_tdi_fraction: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TcksampleConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> TcksampleOutputs:
    """
    tcksample by Robert E. Smith (robert.smith@florey.edu.au).
    
    Sample values of an associated image along tracks.
    
    By default, the value of the underlying image at each point along the track
    is written to either an ASCII file (with all values for each track on the
    same line), or a track scalar file (.tsf). Alternatively, some statistic can
    be taken from the values along each streamline and written to a vector file.
    
    References:
    
    * If using -precise option: Smith, R. E.; Tournier, J.-D.; Calamante, F. &
    Connelly, A. SIFT: Spherical-deconvolution informed filtering of
    tractograms. NeuroImage, 2013, 67, 298-312.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/tcksample.html
    
    Args:
        tracks: the input track file
        image: the image to be sampled
        values_: the output sampled values
        stat_tck: compute some statistic from the values along each streamline
            (options are: mean,median,min,max)
        nointerp: do not use trilinear interpolation when sampling image values
        precise: use the precise mechanism for mapping streamlines to voxels
            (obviates the need for trilinear interpolation) (only applicable if some
            per-streamline statistic is requested)
        use_tdi_fraction: each streamline is assigned a fraction of the image
            intensity in each voxel based on the fraction of the track density
            contributed by that streamline (this is only appropriate for processing
            a whole-brain tractogram, and images for which the quantiative parameter
            is additive)
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
        NamedTuple of outputs (described in `TcksampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCKSAMPLE_METADATA)
    cargs = []
    cargs.append("tcksample")
    if stat_tck is not None:
        cargs.extend(["-stat_tck", stat_tck])
    if nointerp:
        cargs.append("-nointerp")
    if precise:
        cargs.append("-precise")
    if use_tdi_fraction:
        cargs.append("-use_tdi_fraction")
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
    cargs.append(execution.input_file(tracks))
    cargs.append(execution.input_file(image))
    cargs.append(execution.input_file(values_))
    ret = TcksampleOutputs(
        root=execution.output_file("."),
        values_=execution.output_file(f"{pathlib.Path(values_).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TCKSAMPLE_METADATA",
    "TcksampleConfig",
    "TcksampleOutputs",
    "tcksample",
]
