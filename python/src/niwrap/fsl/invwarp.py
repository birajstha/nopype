# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

NEW_INVWARP_METADATA = Metadata(
    id="0a9abd084d11fa4b6f2bcfb4930ab5ce1dbe93d4",
    name="new_invwarp",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class NewInvwarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `new_invwarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_volume: OutputPathType
    """Output inverse warped volume"""


def new_invwarp(
    warpvol: InputPathType,
    outvol: str,
    refvol: InputPathType,
    relflag: bool = False,
    absflag: bool = False,
    noconstraintflag: bool = False,
    jmin: float | int | None = 0.01,
    jmax: float | int | None = 100.0,
    debugflag: bool = False,
    verboseflag: bool = False,
    runner: Runner | None = None,
) -> NewInvwarpOutputs:
    """
    new_invwarp by University of Oxford (Jesper Andersson).
    
    Inverse warp tool from FSL suite.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FNIRT
    
    Args:
        warpvol: Filename for warp/shiftmap transform (volume).
        outvol: Filename for output (inverse warped) image.
        refvol: Filename for new reference image, i.e., what was originally the\
            input image (determines inverse warpvol's FOV and pixdims).
        relflag: Use relative warp convention: x' = x + w(x).
        absflag: Use absolute warp convention (default): x' = w(x).
        noconstraintflag: Do not apply the Jacobian constraint.
        jmin: Minimum acceptable Jacobian value for constraint (default 0.01).
        jmax: Maximum acceptable Jacobian value for constraint (default 100.0).
        debugflag: Turn on debugging output.
        verboseflag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `NewInvwarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(NEW_INVWARP_METADATA)
    cargs = []
    cargs.append("invwarp")
    cargs.append("-w")
    cargs.extend(["-w", execution.input_file(warpvol)])
    cargs.append("-o")
    cargs.extend(["-o", outvol])
    cargs.append("-r")
    cargs.extend(["-r", execution.input_file(refvol)])
    if relflag:
        cargs.append("--rel")
    if absflag:
        cargs.append("--abs")
    if noconstraintflag:
        cargs.append("--noconstraint")
    if jmin is not None:
        cargs.extend(["--jmin", str(jmin)])
    if jmax is not None:
        cargs.extend(["--jmax", str(jmax)])
    if debugflag:
        cargs.append("--debug")
    if verboseflag:
        cargs.append("-v")
    ret = NewInvwarpOutputs(
        root=execution.output_file("."),
        out_volume=execution.output_file(f"{outvol}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "NEW_INVWARP_METADATA",
    "NewInvwarpOutputs",
    "new_invwarp",
]
