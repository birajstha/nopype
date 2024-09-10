# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_DISTORTION_METADATA = Metadata(
    id="3f5c13f95598fdf3162251baa59637cd5f45fcf4.boutiques",
    name="surface-distortion",
    package="workbench",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class SurfaceDistortionSmooth:
    """
    smooth the area data.
    """
    sigma: float
    """the size of the smoothing kernel in mm, as sigma by default"""
    opt_fwhm: bool = False
    """kernel size is FWHM, not sigma"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-smooth")
        cargs.append(str(self.sigma))
        if self.opt_fwhm:
            cargs.append("-fwhm")
        return cargs


class SurfaceDistortionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_distortion(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output distortion metric"""


def surface_distortion(
    surface_reference: InputPathType,
    surface_distorted: InputPathType,
    metric_out: str,
    smooth: SurfaceDistortionSmooth | None = None,
    opt_caret5_method: bool = False,
    opt_edge_method: bool = False,
    opt_local_affine_method: bool = False,
    opt_log2: bool = False,
    runner: Runner | None = None,
) -> SurfaceDistortionOutputs:
    """
    Measure distortion between surfaces.
    
    This command, when not using -caret5-method, -edge-method, or
    -local-affine-method, is equivalent to using -surface-vertex-areas on each
    surface, smoothing both output metrics with the GEO_GAUSS_EQUAL method on
    the surface they came from if -smooth is specified, and then using the
    formula 'ln(distorted/reference)/ln(2)' on the smoothed results.
    
    When using -caret5-method, it uses the surface distortion method from
    caret5, which takes the base 2 log of the ratio of tile areas, then averages
    those results at each vertex, and then smooths the result on the reference
    surface.
    
    When using -edge-method, the -smooth option is ignored, and the output at
    each vertex is the average of 'abs(ln(refEdge/distortEdge)/ln(2))' over all
    edges connected to the vertex.
    
    When using -local-affine-method, the -smooth option is ignored. The output
    is two columns, the first is the area distortion ratio, and the second is
    anisotropic strain. These are calculated by an affine transform between
    matching triangles, and then averaged across the triangles of a vertex.
    
    Author: Washington University School of Medicin
    
    Args:
        surface_reference: the reference surface.
        surface_distorted: the distorted surface.
        metric_out: the output distortion metric.
        smooth: smooth the area data.
        opt_caret5_method: use the surface distortion method from caret5.
        opt_edge_method: calculate distortion of edge lengths rather than areas.
        opt_local_affine_method: calculate distortion by the local affines\
            between triangles.
        opt_log2: apply base-2 log transform.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceDistortionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_DISTORTION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-distortion")
    cargs.append(execution.input_file(surface_reference))
    cargs.append(execution.input_file(surface_distorted))
    cargs.append(metric_out)
    if smooth is not None:
        cargs.extend(smooth.run(execution))
    if opt_caret5_method:
        cargs.append("-caret5-method")
    if opt_edge_method:
        cargs.append("-edge-method")
    if opt_local_affine_method:
        cargs.append("-local-affine-method")
    if opt_log2:
        cargs.append("-log2")
    ret = SurfaceDistortionOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(metric_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_DISTORTION_METADATA",
    "SurfaceDistortionOutputs",
    "SurfaceDistortionSmooth",
    "surface_distortion",
]
