# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_1DMATCALC_METADATA = Metadata(
    id="9bf60ba746a345e2030b30d8f23058cc9fd57536",
    name="1dmatcalc",
    container_image_type="docker",
    container_image_tag="afni/afni_latest",
)


class V1dmatcalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1dmatcalc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file resulting from the evaluated expression"""


def v_1dmatcalc(
    expression: str | None = None,
    runner: Runner | None = None,
) -> V1dmatcalcOutputs:
    """
    1dmatcalc by AFNI (Analysis of Functional NeuroImages).
    
    A tool to evaluate space-delimited RPN (Reverse Polish Notation)
    matrix-valued expressions.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/1dmatcalc.html
    
    Args:
        expression: Expression to evaluate the RPN matrix-valued operations.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dmatcalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DMATCALC_METADATA)
    cargs = []
    cargs.append("1dmatcalc")
    if expression is not None:
        cargs.append(expression)
    ret = V1dmatcalcOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"[OUTPUT_FILE]", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dmatcalcOutputs",
    "V_1DMATCALC_METADATA",
    "v_1dmatcalc",
]
