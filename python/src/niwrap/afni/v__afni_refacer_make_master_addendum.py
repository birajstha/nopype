# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__AFNI_REFACER_MAKE_MASTER_ADDENDUM_METADATA = Metadata(
    id="b46d824ea481a358e85892ed78dfa29dfb14c393.boutiques",
    name="@afni_refacer_make_master_addendum",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class VAfniRefacerMakeMasterAddendumOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__afni_refacer_make_master_addendum(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__afni_refacer_make_master_addendum(
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> VAfniRefacerMakeMasterAddendumOutputs:
    """
    Adjunct program for AFNI refacer, takes no command line arguments.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@afni_refacer_make_master_addendum.html
    
    Args:
        help_: Display the help message.
        version: Display the version info.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VAfniRefacerMakeMasterAddendumOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__AFNI_REFACER_MAKE_MASTER_ADDENDUM_METADATA)
    cargs = []
    cargs.append("afni_refacer_make_master_addendum")
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-ver")
    ret = VAfniRefacerMakeMasterAddendumOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VAfniRefacerMakeMasterAddendumOutputs",
    "V__AFNI_REFACER_MAKE_MASTER_ADDENDUM_METADATA",
    "v__afni_refacer_make_master_addendum",
]
