# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_1DSVD_METADATA = Metadata(
    id="5fe0099ec8141e5d6329aafb206f3c7b832f7519",
    name="1dsvd",
)


class V1dsvdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1dsvd(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stdout: OutputPathType
    """Output of the SVD computation"""


def v_1dsvd(
    input_files: list[InputPathType],
    one: bool = False,
    vmean: bool = False,
    vnorm: bool = False,
    cond: bool = False,
    sing: bool = False,
    sort: bool = False,
    nosort: bool = False,
    asort: bool = False,
    left_eigenvectors: bool = False,
    num_eigenvectors: str | None = None,
    runner: Runner | None = None,
) -> V1dsvdOutputs:
    """
    1dsvd by Zhark the Algebraical (Linear).
    
    Computes SVD of the matrix formed by the 1D file(s) and outputs the result
    on stdout.
    
    Args:
        input_files: Input 1D file(s) for SVD computation.
        one: Make 1st vector be all 1's.
        vmean: Remove mean from each vector (cannot be used with -one).
        vnorm: Make L2-norm of each vector = 1 before SVD.
        cond: Only print condition number (ratio of extremes).
        sing: Only print singular values.
        sort: Sort singular values in descending order (default).
        nosort: Don't sort singular values.
        asort: Sort singular values in ascending order.
        left_eigenvectors: Only output left eigenvectors in .1D format.
        num_eigenvectors: Specify number of left eigenvectors to output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dsvdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DSVD_METADATA)
    cargs = []
    cargs.append("1dsvd")
    if one:
        cargs.append("-one")
    if vmean:
        cargs.append("-vmean")
    if vnorm:
        cargs.append("-vnorm")
    if cond:
        cargs.append("-cond")
    if sing:
        cargs.append("-sing")
    if sort:
        cargs.append("-sort")
    if nosort:
        cargs.append("-nosort")
    if asort:
        cargs.append("-asort")
    if left_eigenvectors:
        cargs.append("-1Dleft")
    if num_eigenvectors is not None:
        cargs.extend(["-nev", num_eigenvectors])
    cargs.extend([execution.input_file(f) for f in input_files])
    ret = V1dsvdOutputs(
        root=execution.output_file("."),
        stdout=execution.output_file(f"stdout", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dsvdOutputs",
    "V_1DSVD_METADATA",
    "v_1dsvd",
]
