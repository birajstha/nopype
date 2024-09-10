# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

PNM_STAGE1_METADATA = Metadata(
    id="dd95e06b08a085e32cb0c931cacdd986c50dea4f.boutiques",
    name="pnm_stage1",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class PnmStage1Outputs(typing.NamedTuple):
    """
    Output object returned when calling `pnm_stage1(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output physiological data file"""


def pnm_stage1(
    infile: InputPathType,
    out_basename: str,
    runner: Runner | None = None,
) -> PnmStage1Outputs:
    """
    Physiological data preprocessing for FSL.
    
    Author: University of Oxford (Mark Jenkinson)
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/PNM#The_popp_program
    
    Args:
        infile: Input physiological data filename (text format).
        out_basename: Output basename for physiological data and\
            timing/triggers (no extensions).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PnmStage1Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PNM_STAGE1_METADATA)
    cargs = []
    cargs.append("popp")
    cargs.extend([
        "-i",
        execution.input_file(infile)
    ])
    cargs.extend([
        "-o",
        out_basename
    ])
    cargs.append("[OPTIONAL_ARGUMENTS]")
    ret = PnmStage1Outputs(
        root=execution.output_file("."),
        outfile=execution.output_file(out_basename + "_output.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PNM_STAGE1_METADATA",
    "PnmStage1Outputs",
    "pnm_stage1",
]
