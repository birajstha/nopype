# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__BUILD_AFNI_XLIB_METADATA = Metadata(
    id="a0b1f50f70b5a5aed2f363d01a1a7255fc7c7000.boutiques",
    name="@build_afni_Xlib",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class VBuildAfniXlibOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__build_afni_xlib(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__build_afni_xlib(
    packages: list[str],
    localinstall: bool = False,
    debug_symbols: bool = False,
    lib64: bool = False,
    runner: Runner | None = None,
) -> VBuildAfniXlibOutputs:
    """
    Compile and install lesstif, openmotif, and/or libXt.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@build_afni_Xlib.html
    
    Args:
        packages: Packages to compile and install (e.g., lesstif, openmotif,\
            libXt).
        localinstall: Install under each package directory.
        debug_symbols: Compile with -g to add symbols.
        lib64: Install libs under lib64 (default is lib).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VBuildAfniXlibOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__BUILD_AFNI_XLIB_METADATA)
    cargs = []
    cargs.append("@build_afni_Xlib")
    if localinstall:
        cargs.append("-localinstall")
    if debug_symbols:
        cargs.append("-g")
    if lib64:
        cargs.append("-lib64")
    cargs.extend(packages)
    ret = VBuildAfniXlibOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VBuildAfniXlibOutputs",
    "V__BUILD_AFNI_XLIB_METADATA",
    "v__build_afni_xlib",
]
