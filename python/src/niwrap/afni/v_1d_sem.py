# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1D_SEM_METADATA = Metadata(
    id="a13cc37aed7943063bbc8f15d64c62a62a0acaad.boutiques",
    name="1dSEM",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V1dSemOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_sem(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output printed to the terminal. This file may be redirected."""


def v_1d_sem(
    theta: InputPathType,
    correlation_matrix: InputPathType,
    residual_variance: InputPathType,
    degrees_of_freedom: float,
    runner: Runner | None = None,
) -> V1dSemOutputs:
    """
    Computes path coefficients for connection matrix in Structural Equation Modeling
    (SEM).
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/1dSEM.html
    
    Args:
        theta: Connection matrix 1D file with initial representation.
        correlation_matrix: Correlation matrix 1D file.
        residual_variance: Residual variance vector 1D file.
        degrees_of_freedom: Degrees of freedom.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dSemOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_SEM_METADATA)
    cargs = []
    cargs.append("1dSEM")
    cargs.append("-theta")
    cargs.append(execution.input_file(theta))
    cargs.append("-C")
    cargs.append(execution.input_file(correlation_matrix))
    cargs.append("-psi")
    cargs.append(execution.input_file(residual_variance))
    cargs.append("-DF")
    cargs.append(str(degrees_of_freedom))
    cargs.append("[OPTIONS]")
    ret = V1dSemOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("output.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dSemOutputs",
    "V_1D_SEM_METADATA",
    "v_1d_sem",
]
