# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SLOW_SURF_CLUSTSIM_PY_METADATA = Metadata(
    id="b50edd606f1480620f1070d30997d45b4421b95e.boutiques",
    name="slow_surf_clustsim.py",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class SlowSurfClustsimPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `slow_surf_clustsim_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def slow_surf_clustsim_py(
    on_surface: str | None = None,
    save_script: str | None = None,
    print_script: bool = False,
    uvar: list[str] | None = None,
    verbosity: float | None = None,
    help_: bool = False,
    hist: bool = False,
    show_default_cvars: bool = False,
    show_default_uvars: bool = False,
    show_valid_opts: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> SlowSurfClustsimPyOutputs:
    """
    Generate a tcsh script to run clustsim on surface.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/slow_surf_clustsim.py.html
    
    Args:
        on_surface: Start from noise on the surface (so no volume data is\
            involved).
        save_script: Save script to given file.
        print_script: Print script to terminal.
        uvar: Set the user variable (use -show_default_uvars to see user vars).\
            Example usage: -uvar spec_file sb23_lh_141_std.spec -uvar surf_vol\
            sb23_SurfVol_aligned+orig.
        verbosity: Set the verbosity level.
        help_: Show this help.
        hist: Show module history.
        show_default_cvars: List default control variables.
        show_default_uvars: List default user variables.
        show_valid_opts: List valid options.
        version: Show current version.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SlowSurfClustsimPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SLOW_SURF_CLUSTSIM_PY_METADATA)
    cargs = []
    cargs.append("slow_surf_clustsim.py")
    if on_surface is not None:
        cargs.extend([
            "-on_surface",
            on_surface
        ])
    if save_script is not None:
        cargs.extend([
            "-save_script",
            save_script
        ])
    if print_script:
        cargs.append("-print_script")
    if uvar is not None:
        cargs.extend([
            "-uvar",
            *uvar
        ])
    if verbosity is not None:
        cargs.extend([
            "-verb",
            str(verbosity)
        ])
    if help_:
        cargs.append("-help")
    if hist:
        cargs.append("-hist")
    if show_default_cvars:
        cargs.append("-show_default_cvars")
    if show_default_uvars:
        cargs.append("-show_default_uvars")
    if show_valid_opts:
        cargs.append("-show_valid_opts")
    if version:
        cargs.append("-ver")
    ret = SlowSurfClustsimPyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SLOW_SURF_CLUSTSIM_PY_METADATA",
    "SlowSurfClustsimPyOutputs",
    "slow_surf_clustsim_py",
]
