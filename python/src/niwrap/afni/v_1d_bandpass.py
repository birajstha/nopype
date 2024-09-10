# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1D_BANDPASS_METADATA = Metadata(
    id="c43105f92af7c38f324923d7bad47edff1d76e40.boutiques",
    name="1dBandpass",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V1dBandpassOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_bandpass(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_1d_bandpass(
    fbot: float,
    ftop: float,
    infile: InputPathType,
    runner: Runner | None = None,
) -> V1dBandpassOutputs:
    """
    Bandpass filtering of time series data in AFNI *.1D files.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/1dBandpass.html
    
    Args:
        fbot: Lowest frequency in the passband, in Hz (must be greater than or\
            equal to 0).
        ftop: Highest frequency in the passband, in Hz (must be greater than\
            FBOT).
        infile: Input AFNI *.1D file; each column is processed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dBandpassOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_BANDPASS_METADATA)
    cargs = []
    cargs.append("1dBandpass")
    cargs.append("[OPTIONS]")
    cargs.append(str(fbot))
    cargs.append(str(ftop))
    cargs.append(execution.input_file(infile))
    ret = V1dBandpassOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dBandpassOutputs",
    "V_1D_BANDPASS_METADATA",
    "v_1d_bandpass",
]
