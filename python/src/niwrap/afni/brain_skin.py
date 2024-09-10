# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BRAIN_SKIN_METADATA = Metadata(
    id="7b8dfd18121d1553dd7c190dc3af25cbec26c157.boutiques",
    name="BrainSkin",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class BrainSkinOutputs(typing.NamedTuple):
    """
    Output object returned when calling `brain_skin(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stitch_surface: OutputPathType
    """A bunch of triangles for closing the surface."""
    initial_skin_surface: OutputPathType
    """Initial skin surface"""
    reduced_skin_surface: OutputPathType
    """Reduced mesh version of initial skin surface."""
    inflated_skin_surface: OutputPathType
    """Original surface inflated inside skin surface."""
    patching_voxels: OutputPathType
    """Surface patching voxels."""
    surf_voxels: OutputPathType
    """Voxels inside original surface"""
    skin_voxels: OutputPathType
    """Mix of ptchvox and surfvox."""
    infilled_voxels: OutputPathType
    """Skin vox dataset filled in."""
    node_pairs_results: OutputPathType
    """Results of computations for finding node pairs that span sulci."""
    inflating_surface_results: OutputPathType
    """Results of computations for inflating initial surface inside skin
    surface."""
    segments_display: OutputPathType
    """Segments between node pairs spanning sulci."""


def brain_skin(
    surface: str,
    skingrid_volume: InputPathType,
    prefix: str,
    plimit: float | None = None,
    dlimit: float | None = None,
    segdo: str | None = None,
    voxelize: str | None = None,
    infill: str | None = None,
    out_file: InputPathType | None = None,
    vol_hull: InputPathType | None = None,
    no_zero_attraction: bool = False,
    node_dbg: float | None = None,
    runner: Runner | None = None,
) -> BrainSkinOutputs:
    """
    A program to create an unfolded surface that wraps the brain (skin) and
    Gyrification Indices.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/BrainSkin.html
    
    Args:
        surface: Surface to smooth or the domain over which DSET is defined.
        skingrid_volume: A high-res volume to provide a grid for voxelization\
            steps.
        prefix: Prefix to use for variety of output files.
        plimit: Maximum length of path along surface in mm for node pairing.
        dlimit: Maximum length of Euclidean distance in mm for node pairing.
        segdo: Output a displayable object file that contains segments between\
            paired nodes.
        voxelize: Voxelization method. Choose from: slow: Sure footed but slow,\
            fast: Faster and works OK, mask: Fastest and works OK too (default).
        infill: Infill method. Choose from: slow: proper infill, but not\
            needed, fast: brutish infill, all we need (default).
        out_file: Output intermediary results from skin forming step.
        vol_hull: Deform an Icosahedron to match the convex hull of a mask\
            volume.
        no_zero_attraction: With vol_skin, the surface will try to shrink\
            aggressively, even if there is no promise of non-zero values below.
        node_dbg: Output debugging information for node N for -vol_skin and\
            -vol_hull options.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BrainSkinOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BRAIN_SKIN_METADATA)
    cargs = []
    cargs.append("BrainSkin")
    cargs.append(surface)
    cargs.extend([
        "-skingrid",
        execution.input_file(skingrid_volume)
    ])
    cargs.extend([
        "-prefix",
        prefix
    ])
    if plimit is not None:
        cargs.extend([
            "-plimit",
            str(plimit)
        ])
    if dlimit is not None:
        cargs.extend([
            "-dlimit",
            str(dlimit)
        ])
    if segdo is not None:
        cargs.extend([
            "-segdo",
            segdo
        ])
    if voxelize is not None:
        cargs.extend([
            "-voxelize",
            voxelize
        ])
    if infill is not None:
        cargs.extend([
            "-infill",
            infill
        ])
    if out_file is not None:
        cargs.extend([
            "-out",
            execution.input_file(out_file)
        ])
    if vol_hull is not None:
        cargs.extend([
            "-vol_hull",
            execution.input_file(vol_hull)
        ])
    if no_zero_attraction:
        cargs.append("-no_zero_attraction")
    if node_dbg is not None:
        cargs.extend([
            "-node_dbg",
            str(node_dbg)
        ])
    ret = BrainSkinOutputs(
        root=execution.output_file("."),
        stitch_surface=execution.output_file(prefix + ".stitch.gii"),
        initial_skin_surface=execution.output_file(prefix + ".skin.gii"),
        reduced_skin_surface=execution.output_file(prefix + ".skin_simp.gii"),
        inflated_skin_surface=execution.output_file(prefix + ".skin.isotopic.gii"),
        patching_voxels=execution.output_file(prefix + ".ptchvox+orig"),
        surf_voxels=execution.output_file(prefix + ".surfvox+orig"),
        skin_voxels=execution.output_file(prefix + ".skinvox+orig"),
        infilled_voxels=execution.output_file(prefix + ".infilled+orig"),
        node_pairs_results=execution.output_file(prefix + ".niml.dset"),
        inflating_surface_results=execution.output_file(prefix + ".areas.niml.dset"),
        segments_display=execution.output_file(prefix + ".1D.do"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BRAIN_SKIN_METADATA",
    "BrainSkinOutputs",
    "brain_skin",
]
