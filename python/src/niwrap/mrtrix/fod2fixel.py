# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


FOD2FIXEL_METADATA = Metadata(
    id="624de5d83bc1e96871850ee95153c643eaedf75c",
    name="fod2fixel",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Fod2fixelConfig:
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


class Fod2fixelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fod2fixel(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fixel_directory: OutputPathType
    """the output fixel directory"""
    afd: OutputPathType | None
    """output the total Apparent Fibre Density per fixel (integral of FOD lobe) """
    peak_amp: OutputPathType | None
    """output the amplitude of the FOD at the maximal peak per fixel """
    disp: OutputPathType | None
    """output a measure of dispersion per fixel as the ratio between FOD lobe integral and maximal peak amplitude """


def fod2fixel(
    fod: InputPathType,
    fixel_directory: InputPathType,
    afd: InputPathType | None = None,
    peak_amp: InputPathType | None = None,
    disp: InputPathType | None = None,
    fmls_integral: float | int | None = None,
    fmls_peak_value: float | int | None = None,
    fmls_no_thresholds: bool = False,
    fmls_lobe_merge_ratio: float | int | None = None,
    mask: InputPathType | None = None,
    maxnum: int | None = None,
    nii: bool = False,
    dirpeak: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Fod2fixelConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Fod2fixelOutputs:
    """
    fod2fixel by Robert E. Smith (robert.smith@florey.edu.au).
    
    Perform segmentation of continuous Fibre Orientation Distributions (FODs) to
    produce discrete fixels.
    
    
    
    References:
    
    * Reference for the FOD segmentation method:
    Smith, R. E.; Tournier, J.-D.; Calamante, F. & Connelly, A. SIFT:
    Spherical-deconvolution informed filtering of tractograms. NeuroImage, 2013,
    67, 298-312 (Appendix 2)
    
    * Reference for Apparent Fibre Density (AFD):
    Raffelt, D.; Tournier, J.-D.; Rose, S.; Ridgway, G.R.; Henderson, R.;
    Crozier, S.; Salvado, O.; Connelly, A. Apparent Fibre Density: a novel
    measure for the analysis of diffusion-weighted magnetic resonance
    images.Neuroimage, 2012, 15;59(4), 3976-94.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/fod2fixel.html
    
    Args:
        fod: the input fod image.
        fixel_directory: the output fixel directory
        afd: output the total Apparent Fibre Density per fixel (integral of FOD
            lobe)
        peak_amp: output the amplitude of the FOD at the maximal peak per fixel
        disp: output a measure of dispersion per fixel as the ratio between FOD
            lobe integral and maximal peak amplitude
        fmls_integral: threshold absolute numerical integral of positive FOD
            lobes. Any lobe for which the integral is smaller than this threshold
            will be discarded. Default: 0.
        fmls_peak_value: threshold peak amplitude of positive FOD lobes. Any
            lobe for which the maximal peak amplitude is smaller than this threshold
            will be discarded. Default: 0.1.
        fmls_no_thresholds: disable all FOD lobe thresholding; every lobe where
            the FOD is positive will be retained.
        fmls_lobe_merge_ratio: Specify the ratio between a given FOD amplitude
            sample between two lobes, and the smallest peak amplitude of the
            adjacent lobes, above which those lobes will be merged. This is the
            amplitude of the FOD at the 'bridge' point between the two lobes,
            divided by the peak amplitude of the smaller of the two adjoining lobes.
            A value of 1.0 will never merge two lobes into one; a value of 0.0 will
            always merge lobes unless they are bisected by a zero-valued crossing.
            Default: 1.
        mask: only perform computation within the specified binary brain mask
            image.
        maxnum: maximum number of fixels to output for any particular voxel
            (default: no limit)
        nii: output the directions and index file in nii format (instead of the
            default mif)
        dirpeak: define the fixel direction as that of the lobe's maximal peak
            as opposed to its weighted mean direction (the default)
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
        NamedTuple of outputs (described in `Fod2fixelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FOD2FIXEL_METADATA)
    cargs = []
    cargs.append("fod2fixel")
    if afd is not None:
        cargs.extend(["-afd", execution.input_file(afd)])
    if peak_amp is not None:
        cargs.extend(["-peak_amp", execution.input_file(peak_amp)])
    if disp is not None:
        cargs.extend(["-disp", execution.input_file(disp)])
    if fmls_integral is not None:
        cargs.extend(["-fmls_integral", str(fmls_integral)])
    if fmls_peak_value is not None:
        cargs.extend(["-fmls_peak_value", str(fmls_peak_value)])
    if fmls_no_thresholds:
        cargs.append("-fmls_no_thresholds")
    if fmls_lobe_merge_ratio is not None:
        cargs.extend(["-fmls_lobe_merge_ratio", str(fmls_lobe_merge_ratio)])
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if maxnum is not None:
        cargs.extend(["-maxnum", str(maxnum)])
    if nii:
        cargs.append("-nii")
    if dirpeak:
        cargs.append("-dirpeak")
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
    cargs.append(execution.input_file(fod))
    cargs.append(execution.input_file(fixel_directory))
    ret = Fod2fixelOutputs(
        root=execution.output_file("."),
        fixel_directory=execution.output_file(f"{pathlib.Path(fixel_directory).stem}"),
        afd=execution.output_file(f"{pathlib.Path(afd).stem}") if afd is not None else None,
        peak_amp=execution.output_file(f"{pathlib.Path(peak_amp).stem}") if peak_amp is not None else None,
        disp=execution.output_file(f"{pathlib.Path(disp).stem}") if disp is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FOD2FIXEL_METADATA",
    "Fod2fixelConfig",
    "Fod2fixelOutputs",
    "fod2fixel",
]
