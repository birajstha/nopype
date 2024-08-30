# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

TSPLOT_METADATA = Metadata(
    id="9b69e33c8f61f1146dbcc656dc580d78c80db650",
    name="tsplot",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class TsplotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tsplot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    timeseries_output: OutputPathType | None
    """Output timeseries data"""


def tsplot(
    input_directory: str,
    main_filtered_data: InputPathType | None = None,
    coordinates: list[float | int] | None = None,
    coordinates_output: list[float | int] | None = None,
    mask: InputPathType | None = None,
    output_directory: str | None = None,
    no_weight_flag: bool = False,
    prewhiten_flag: bool = False,
    no_raw_flag: bool = False,
    runner: Runner | None = None,
) -> TsplotOutputs:
    """
    tsplot by FMRIB.
    
    Time series plotting tool for FSL.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/tsplot
    
    Args:
        input_directory: Input FEAT directory (e.g. feat_directory.feat).
        main_filtered_data: Input main filtered data, in case it's not\
            <feat_directory.feat>/filtered_func_data.
        coordinates: Use X, Y, Z instead of max Z stat position.
        coordinates_output: Use X,Y,Z to output time series only - no stats or\
            modelling.
        mask: Use mask image instead of thresholded activation images.
        output_directory: Change output directory from default of input FEAT\
            directory.
        no_weight_flag: Don't weight cluster averaging with Z stats.
        prewhiten_flag: Prewhiten data and model timeseries before plotting.
        no_raw_flag: Don't keep raw data text files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TsplotOutputs`).
    """
    runner = runner or get_global_runner()
    if coordinates is not None and (len(coordinates) != 3): 
        raise ValueError(f"Length of 'coordinates' must be 3 but was {len(coordinates)}")
    if coordinates_output is not None and (len(coordinates_output) != 3): 
        raise ValueError(f"Length of 'coordinates_output' must be 3 but was {len(coordinates_output)}")
    execution = runner.start_execution(TSPLOT_METADATA)
    cargs = []
    cargs.append("tsplot")
    cargs.append(input_directory)
    if main_filtered_data is not None:
        cargs.extend(["-f", execution.input_file(main_filtered_data)])
    if coordinates is not None:
        cargs.extend(["-c", *map(str, coordinates)])
    if coordinates_output is not None:
        cargs.extend(["-C", *map(str, coordinates_output)])
    if mask is not None:
        cargs.extend(["-m", execution.input_file(mask)])
    if output_directory is not None:
        cargs.extend(["-o", output_directory])
    if no_weight_flag:
        cargs.append("-n")
    if prewhiten_flag:
        cargs.append("-p")
    if no_raw_flag:
        cargs.append("-d")
    ret = TsplotOutputs(
        root=execution.output_file("."),
        timeseries_output=execution.output_file(f"{output_directory}/timeseries.txt", optional=True) if output_directory is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TSPLOT_METADATA",
    "TsplotOutputs",
    "tsplot",
]
