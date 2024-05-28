# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


MRDEGIBBS_METADATA = Metadata(
    id="ccaa6a3ba223e5670d7651d5da0d8a8c42b02752",
    name="mrdegibbs",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class MrdegibbsConfig:
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


class MrdegibbsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrdegibbs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out: OutputPathType
    """the output image."""


def mrdegibbs(
    in_: InputPathType,
    out: InputPathType,
    axes: list[int] = None,
    nshifts: int | None = None,
    min_w: int | None = None,
    max_w: int | None = None,
    datatype: typing.Literal["spec"] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrdegibbsConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> MrdegibbsOutputs:
    """
    mrdegibbs by Ben Jeurissen (ben.jeurissen@uantwerpen.be) & J-Donald Tournier
    (jdtournier@gmail.com).
    
    Remove Gibbs Ringing Artifacts.
    
    This application attempts to remove Gibbs ringing artefacts from MRI images
    using the method of local subvoxel-shifts proposed by Kellner et al. (see
    reference below for details).
    
    This command is designed to run on data directly after it has been
    reconstructed by the scanner, before any interpolation of any kind has taken
    place. You should not run this command after any form of motion correction
    (e.g. not after dwifslpreproc). Similarly, if you intend running dwidenoise,
    you should run denoising before this command to not alter the noise
    structure, which would impact on dwidenoise's performance.
    
    Note that this method is designed to work on images acquired with full
    k-space coverage. Running this method on partial Fourier ('half-scan') data
    may lead to suboptimal and/or biased results, as noted in the original
    reference below. There is currently no means of dealing with this; users
    should exercise caution when using this method on partial Fourier data, and
    inspect its output for any obvious artefacts.
    
    References:
    
    Kellner, E; Dhital, B; Kiselev, V.G & Reisert, M. Gibbs-ringing artifact
    removal based on local subvoxel-shifts. Magnetic Resonance in Medicine,
    2016, 76, 1574–1581.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/mrdegibbs.html
    
    Args:
        in_: the input image.
        out: the output image.
        axes: select the slice axes (default: 0,1 - i.e. x-y).
        nshifts: discretization of subpixel spacing (default: 20).
        min_w: left border of window used for TV computation (default: 1).
        max_w: right border of window used for TV computation (default: 3).
        datatype: specify output image data type. Valid choices are: float32,
            float32le, float32be, float64, float64le, float64be, int64, uint64,
            int64le, uint64le, int64be, uint64be, int32, uint32, int32le, uint32le,
            int32be, uint32be, int16, uint16, int16le, uint16le, int16be, uint16be,
            cfloat32, cfloat32le, cfloat32be, cfloat64, cfloat64le, cfloat64be,
            int8, uint8, bit.
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
        NamedTuple of outputs (described in `MrdegibbsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRDEGIBBS_METADATA)
    cargs = []
    cargs.append("mrdegibbs")
    if axes is not None:
        cargs.extend(["-axes", *map(str, axes)])
    if nshifts is not None:
        cargs.extend(["-nshifts", str(nshifts)])
    if min_w is not None:
        cargs.extend(["-minW", str(min_w)])
    if max_w is not None:
        cargs.extend(["-maxW", str(max_w)])
    if datatype is not None:
        cargs.extend(["-datatype", datatype])
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
    ret = MrdegibbsOutputs(
        root=execution.output_file("."),
        out=execution.output_file(f"{pathlib.Path(out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRDEGIBBS_METADATA",
    "MrdegibbsConfig",
    "MrdegibbsOutputs",
    "mrdegibbs",
]
