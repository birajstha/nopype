# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__ELECTRO_GRID_METADATA = Metadata(
    id="6b8041470a22f27b77362ae6b78895222381700b.boutiques",
    name="@ElectroGrid",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class VElectroGridOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__electro_grid(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface: OutputPathType
    """Output surface file"""


def v__electro_grid(
    runner: Runner | None = None,
) -> VElectroGridOutputs:
    """
    Creates a mesh representation of an electrode grid for use with SUMA.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@ElectroGrid.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VElectroGridOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__ELECTRO_GRID_METADATA)
    cargs = []
    cargs.append("@ElectroGrid")
    cargs.append("[[-strip")
    cargs.append("Nx]")
    cargs.append("|")
    cargs.append("[-grid")
    cargs.append("Nx")
    cargs.append("Ny]]")
    cargs.append("[-prefix")
    cargs.append("PREFIX]")
    cargs.append("[-coords")
    cargs.append("XYZ.1D]")
    cargs.append("[-with_markers]")
    cargs.append("[-echo]")
    ret = VElectroGridOutputs(
        root=execution.output_file("."),
        output_surface=execution.output_file("[PREFIX].gii"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VElectroGridOutputs",
    "V__ELECTRO_GRID_METADATA",
    "v__electro_grid",
]
