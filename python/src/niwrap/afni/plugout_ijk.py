# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

PLUGOUT_IJK_METADATA = Metadata(
    id="3a6afc3c1836f9c09a9ff1be75e0e0b4ba68d0da",
    name="plugout_ijk",
)


class PlugoutIjkOutputs(typing.NamedTuple):
    """
    Output object returned when calling `plugout_ijk(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def plugout_ijk(
    host: str | None = None,
    verbose: bool = False,
    port: float | int | None = None,
    name: str | None = None,
    port_offset: float | int | None = None,
    port_quiet: float | int | None = None,
    port_bloc_offset: float | int | None = None,
    max_bloc: bool = False,
    max_bloc_quiet: bool = False,
    num_assigned_ports: bool = False,
    num_assigned_ports_quiet: bool = False,
    runner: Runner | None = None,
) -> PlugoutIjkOutputs:
    """
    plugout_ijk by AFNI Development Team.
    
    Connects to AFNI and sends (i,j,k) dataset indices to control the viewpoint.
    
    Args:
        host: Connect to AFNI running on the specified computer using TCP/IP.
        verbose: Verbose mode.
        port: Use TCP/IP port number 'pp'.
        name: Use the string 'sss' for the name that AFNI assigns to this\
            plugout.
        port_offset: Provide a port offset to allow multiple instances of\
            communicating programs to operate on the same machine.
        port_quiet: Provide a port offset like -np, but more quiet in the face\
            of adversity.
        port_bloc_offset: Provide a port offset block for easier port\
            management.
        max_bloc: Print the current value of MAX_BLOC and exit.
        max_bloc_quiet: Print MAX_BLOC value only and exit.
        num_assigned_ports: Print the number of assigned ports used by AFNI\
            then quit.
        num_assigned_ports_quiet: Prints the number of assigned ports quietly.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PlugoutIjkOutputs`).
    """
    runner = runner or get_global_runner()
    if port_offset is not None and not (1025 <= port_offset <= 65500): 
        raise ValueError(f"'port_offset' must be between 1025 <= x <= 65500 but was {port_offset}")
    if port_bloc_offset is not None and not (port_bloc_offset <= 4000): 
        raise ValueError(f"'port_bloc_offset' must be less than x <= 4000 but was {port_bloc_offset}")
    execution = runner.start_execution(PLUGOUT_IJK_METADATA)
    cargs = []
    cargs.append("plugout_ijk")
    if host is not None:
        cargs.extend(["-host", host])
    if verbose:
        cargs.append("-v")
    if port is not None:
        cargs.extend(["-port", str(port)])
    if name is not None:
        cargs.extend(["-name", name])
    if port_offset is not None:
        cargs.extend(["-np", str(port_offset)])
    if port_quiet is not None:
        cargs.extend(["-npq", str(port_quiet)])
    if port_bloc_offset is not None:
        cargs.extend(["-npb", str(port_bloc_offset)])
    cargs.append("[PORT_BLOC_OFFSET_QUIET]")
    if max_bloc:
        cargs.append("-max_port_bloc")
    if max_bloc_quiet:
        cargs.append("-max_port_bloc_quiet")
    if num_assigned_ports:
        cargs.append("-num_assigned_ports")
    if num_assigned_ports_quiet:
        cargs.append("-num_assigned_ports_quiet")
    ret = PlugoutIjkOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PLUGOUT_IJK_METADATA",
    "PlugoutIjkOutputs",
    "plugout_ijk",
]
