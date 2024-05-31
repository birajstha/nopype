# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

SURFACE_RESAMPLE_METADATA = Metadata(
    id="087a577e08e5ff7b98376e171beec235c3d7fda2",
    name="surface-resample",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class SurfaceResampleAreaSurfs:
    """
    specify surfaces to do vertex area correction based on
    """
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        return cargs


@dataclasses.dataclass
class SurfaceResampleAreaMetrics:
    """
    specify vertex area metrics to do area correction based on
    """
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        return cargs


class SurfaceResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """the output surface file"""


def surface_resample(
    surface_in: InputPathType,
    current_sphere: InputPathType,
    new_sphere: InputPathType,
    method: str,
    surface_out: InputPathType,
    area_surfs: SurfaceResampleAreaSurfs | None = None,
    area_metrics: SurfaceResampleAreaMetrics | None = None,
    opt_bypass_sphere_check: bool = False,
    runner: Runner = None,
) -> SurfaceResampleOutputs:
    """
    surface-resample by Washington University School of Medicin.
    
    Resample a surface to a different mesh.
    
    Resamples a surface file, given two spherical surfaces that are in register.
    If ADAP_BARY_AREA is used, exactly one of -area-surfs or -area-metrics must
    be specified. This method is not generally recommended for surface
    resampling, but is provided for completeness.
    
    The BARYCENTRIC method is generally recommended for anatomical surfaces, in
    order to minimize smoothing.
    
    For cut surfaces (including flatmaps), use -surface-cut-resample.
    
    Instead of resampling a spherical surface, the
    -surface-sphere-project-unproject command is recommended.
    
    The <method> argument must be one of the following:
    
    ADAP_BARY_AREA
    BARYCENTRIC
    .
    
    Args:
        surface_in: the surface file to resample
        current_sphere: a sphere surface with the mesh that the input surface is
            currently on
        new_sphere: a sphere surface that is in register with <current-sphere>
            and has the desired output mesh
        method: the method name
        surface_out: the output surface file
        area_surfs: specify surfaces to do vertex area correction based on
        area_metrics: specify vertex area metrics to do area correction based on
        opt_bypass_sphere_check: ADVANCED: allow the current and new 'spheres'
            to have arbitrary shape as long as they follow the same contour
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `SurfaceResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_RESAMPLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-resample")
    cargs.append(execution.input_file(surface_in))
    cargs.append(execution.input_file(current_sphere))
    cargs.append(execution.input_file(new_sphere))
    cargs.append(method)
    cargs.append(execution.input_file(surface_out))
    if area_surfs is not None:
        cargs.extend(["-area-surfs", *area_surfs.run(execution)])
    if area_metrics is not None:
        cargs.extend(["-area-metrics", *area_metrics.run(execution)])
    if opt_bypass_sphere_check:
        cargs.append("-bypass-sphere-check")
    ret = SurfaceResampleOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(f"{pathlib.Path(surface_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_RESAMPLE_METADATA",
    "SurfaceResampleAreaMetrics",
    "SurfaceResampleAreaSurfs",
    "SurfaceResampleOutputs",
    "surface_resample",
]
