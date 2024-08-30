# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

POPP_METADATA = Metadata(
    id="6f2613db27c7f1427c3fa38c9d41f2d079a99adb",
    name="popp",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class PoppOutputs(typing.NamedTuple):
    """
    Output object returned when calling `popp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output physiological data file"""


def popp(
    infile: InputPathType,
    out_basename: str,
    sampling_rate: float | int | None = 100,
    tr_value: float | int | None = None,
    resp_col: float | int | None = None,
    cardiac_col: float | int | None = None,
    trigger_col: float | int | None = None,
    rvt_flag: bool = False,
    heartrate_flag: bool = False,
    pulseox_trigger_flag: bool = False,
    smooth_card: float | int | None = None,
    smooth_resp: float | int | None = None,
    high_freq_cutoff: float | int | None = 5,
    low_freq_cutoff: float | int | None = 0.1,
    init_thresh_c: float | int | None = 90,
    n_thresh_c: float | int | None = 60,
    init_thresh_r: float | int | None = 80,
    n_thresh_r: float | int | None = 80,
    invert_resp_flag: bool = False,
    invert_cardiac_flag: bool = False,
    noclean1_flag: bool = False,
    noclean2_flag: bool = False,
    load_card_phase: InputPathType | None = None,
    load_resp_phase: InputPathType | None = None,
    vol_file: InputPathType | None = None,
    start_sample: float | int | None = None,
    resp_add: str | None = None,
    resp_del: str | None = None,
    card_add: str | None = None,
    card_del: str | None = None,
    verbose_flag: bool = False,
    debug_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> PoppOutputs:
    """
    popp by University of Oxford (Mark Jenkinson).
    
    Physiological data preprocessing for FSL.
    
    More information:
    https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/PNM#The_popp_program
    
    Args:
        infile: Input physiological data filename (text format).
        out_basename: Output basename for physiological data and\
            timing/triggers (no extensions).
        sampling_rate: Sampling rate in Hz (default is 100Hz).
        tr_value: TR value in seconds.
        resp_col: Specify column number of respiratory input.
        cardiac_col: Specify column number of cardiac input.
        trigger_col: Specify column number of trigger input.
        rvt_flag: Generate RVT data.
        heartrate_flag: Generate heart rate data.
        pulseox_trigger_flag: Specify that cardiac data is a trigger.
        smooth_card: Specify smoothing amount for cardiac (in seconds).
        smooth_resp: Specify smoothing amount for respiratory (in seconds).
        high_freq_cutoff: High frequency cut off for respiratory filter in Hz\
            (default is 5Hz).
        low_freq_cutoff: Low frequency cut off for respiratory filter in Hz\
            (default is 0.1Hz).
        init_thresh_c: Initial threshold percentile for cardiac (default 90).
        n_thresh_c: Neighbourhood exclusion threshold percentile for cardiac\
            (default 60).
        init_thresh_r: Initial threshold percentile for respiratory (default\
            80).
        n_thresh_r: Neighbourhood exclusion threshold percentile for\
            respiratory (default 80).
        invert_resp_flag: Invert respiratory trace.
        invert_cardiac_flag: Invert cardiac trace.
        noclean1_flag: Turn off cleanup phase 1.
        noclean2_flag: Turn off cleanup phase 2.
        load_card_phase: Input cardiac phase for reprocessing (text format).
        load_resp_phase: Input respiratory phase for reprocessing (text format).
        vol_file: Input volumetric image (EPI) filename.
        start_sample: Set sample number of the starting time (t=0).
        resp_add: Comma separated list of times (in sec) to add to respiratory\
            peak list (uses nearest local max).
        resp_del: Comma separated list of times (in sec) to delete from\
            respiratory peak list (uses nearest existing peak).
        card_add: Comma separated list of times (in sec) to add to cardiac peak\
            list (uses nearest local max).
        card_del: Comma separated list of times (in sec) to delete from cardiac\
            peak list (uses nearest existing peak).
        verbose_flag: Switch on diagnostic messages.
        debug_flag: Output debugging information.
        help_flag: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PoppOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(POPP_METADATA)
    cargs = []
    cargs.append("popp")
    cargs.extend(["-i", execution.input_file(infile)])
    cargs.extend(["-o", out_basename])
    cargs.append("[OPTIONAL_ARGUMENTS]")
    ret = PoppOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"{out_basename}_output.txt", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "POPP_METADATA",
    "PoppOutputs",
    "popp",
]
