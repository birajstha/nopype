# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.740583

import typing

from ..styxdefs import *


VOLUME_LABEL_TO_SURFACE_MAPPING_METADATA = Metadata(
    id="7fdb200987140a778bd1bdfc67be818fac06e8d3",
    name="volume-label-to-surface-mapping",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeLabelToSurfaceMappingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_label_to_surface_mapping(...)`.
    """
    label_out: OutputPathType
    """the output gifti label file"""


def volume_label_to_surface_mapping(
    runner: Runner,
    volume: InputPathType,
    surface: InputPathType,
    label_out: InputPathType,
    opt_subvol_select_subvol: str | None = None,
) -> VolumeLabelToSurfaceMappingOutputs:
    """
    MAP A LABEL VOLUME TO A SURFACE LABEL FILE.
    
    Map label volume data to a surface. If -ribbon-constrained is not specified,
    uses the enclosing voxel method. The ribbon mapping method constructs a
    polyhedron from the vertex's neighbors on each surface, and estimates the
    amount of this polyhedron's volume that falls inside any nearby voxels, to
    use as the weights for a popularity comparison. If -thin-columns is
    specified, the polyhedron uses the edge midpoints and triangle centroids, so
    that neighboring vertices do not have overlapping polyhedra. This may
    require increasing -voxel-subdiv to get enough samples in each voxel to
    reliably land inside these smaller polyhedra. The volume ROI is useful to
    exclude partial volume effects of voxels the surfaces pass through, and will
    cause the mapping to ignore voxels that don't have a positive value in the
    mask. The subdivision number specifies how it approximates the amount of the
    volume the polyhedron intersects, by splitting each voxel into NxNxN pieces,
    and checking whether the center of each piece is inside the polyhedron. If
    you have very large voxels, consider increasing this if you get unexpected
    unlabeled vertices in your output.
    
    Args:
        runner: Command runner
        volume: the volume to map data from
        surface: the surface to map the data onto
        label_out: the output gifti label file
        opt_subvol_select_subvol: select a single subvolume to map: the
            subvolume number or name
    Returns:
        NamedTuple of outputs (described in `VolumeLabelToSurfaceMappingOutputs`).
    """
    execution = runner.start_execution(VOLUME_LABEL_TO_SURFACE_MAPPING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-label-to-surface-mapping")
    cargs.append(execution.input_file(volume))
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(label_out))
    if opt_subvol_select_subvol is not None:
        cargs.extend(["-subvol-select", opt_subvol_select_subvol])
    ret = VolumeLabelToSurfaceMappingOutputs(
        label_out=execution.output_file(f"{label_out}"),
    )
    execution.run(cargs)
    return ret
