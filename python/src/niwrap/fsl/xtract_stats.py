# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

XTRACT_STATS_METADATA = Metadata(
    id="f4e5e97bb4e53d159170f50f0562556e5349aa95",
    name="xtract_stats",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class XtractStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `xtract_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    csv_output: OutputPathType | None
    """CSV file containing the statistics from XTRACT analysis."""


def xtract_stats(
    folder_basename: str,
    xtract_dir: str,
    xtract2diff: str,
    reference_image: InputPathType | None = None,
    output_file: str | None = None,
    structures_file: InputPathType | None = None,
    threshold: float | int | None = None,
    measurements: str | None = None,
    keep_temp_files: bool = False,
    runner: Runner | None = None,
) -> XtractStatsOutputs:
    """
    xtract_stats by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Quantitative evaluation tool of XTRACT results in neuroimaging.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/
    
    Args:
        folder_basename: Path to microstructure folder and basename of data\
            (e.g. /home/DTI/dti_).
        xtract_dir: Path to XTRACT output folder.
        xtract2diff: EITHER XTRACT results to diffusion space transform OR\
            'native' if tracts are already in diffusion space.
        reference_image: If not 'native', provide reference image in diffusion\
            space (e.g. /home/DTI/dti_FA).
        output_file: Output filepath (Default <XTRACT_dir>/stats.csv).
        structures_file: Structures file (as in XTRACT) (Default is all tracts\
            under <XTRACT_dir>).
        threshold: Threshold applied to tract probability map (default = 0.001\
            = 0.1%).
        measurements: Comma separated list of features to extract (Default =\
            vol,prob,length,FA,MD - assumes DTI folder has been provided). vol =\
            tract volume, prob = tract probability, length = tract length.\
            Additional metrics must follow file naming conventions. e.g. for dti_L1\
            use 'L1'.
        keep_temp_files: Keep temporary files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `XtractStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(XTRACT_STATS_METADATA)
    cargs = []
    cargs.append("xtract_stats")
    cargs.append("-d")
    cargs.append(folder_basename)
    cargs.append("-xtract")
    cargs.append(xtract_dir)
    cargs.append("-w")
    cargs.append(xtract2diff)
    cargs.append("[reference]")
    cargs.append("[output_file]")
    cargs.append("[structures_file]")
    cargs.append("[threshold]")
    cargs.append("[measurements]")
    cargs.append("[keep_temp_files]")
    ret = XtractStatsOutputs(
        root=execution.output_file("."),
        csv_output=execution.output_file(f"{output_file}", optional=True) if output_file is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "XTRACT_STATS_METADATA",
    "XtractStatsOutputs",
    "xtract_stats",
]
