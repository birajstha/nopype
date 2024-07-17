# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_DJUNCT_4D_SLICES_TO_3D_VOL_METADATA = Metadata(
    id="c816da754d2a6f0fb9247cd3a25ef22de3abcff7",
    name="@djunct_4d_slices_to_3d_vol",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="example/docker-image:latest",
)


class Djunct4dSlicesTo3dVolOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_djunct_4d_slices_to_3d_vol(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output file generated by the tool"""


def _djunct_4d_slices_to_3d_vol(
    do_something: bool = False,
    runner: Runner | None = None,
) -> Djunct4dSlicesTo3dVolOutputs:
    """
    @djunct_4d_slices_to_3d_vol by Author Name.
    
    Tool description goes here.
    
    More information: http://example.com/@djunct_4d_slices_to_3d_vol
    
    Args:
        do_something: Do something really useful.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Djunct4dSlicesTo3dVolOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(_DJUNCT_4D_SLICES_TO_3D_VOL_METADATA)
    cargs = []
    cargs.append("@djunct_4d_slices_to_3d_vol")
    if do_something:
        cargs.append("-do-something")
    ret = Djunct4dSlicesTo3dVolOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"output_file", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "Djunct4dSlicesTo3dVolOutputs",
    "_DJUNCT_4D_SLICES_TO_3D_VOL_METADATA",
    "_djunct_4d_slices_to_3d_vol",
]
