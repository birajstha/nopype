# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_FALSE_CORRELATION_METADATA = Metadata(
    id="2771f8442876327b07875d527b8402e0a46af4f3",
    name="cifti-false-correlation",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiFalseCorrelationLeftSurface:
    """
    specify the left surface to use
    """
    opt_dump_text_text_out: str | None = None
    """dump the raw measures used to a text file: the output text file"""
    
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
        if self.opt_dump_text_text_out is not None:
            cargs.extend(["-dump-text", self.opt_dump_text_text_out])
        return cargs


@dataclasses.dataclass
class CiftiFalseCorrelationRightSurface:
    """
    specify the right surface to use
    """
    opt_dump_text_text_out: str | None = None
    """dump the raw measures used to a text file: the output text file"""
    
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
        if self.opt_dump_text_text_out is not None:
            cargs.extend(["-dump-text", self.opt_dump_text_text_out])
        return cargs


@dataclasses.dataclass
class CiftiFalseCorrelationCerebellumSurface:
    """
    specify the cerebellum surface to use
    """
    opt_dump_text_text_out: str | None = None
    """dump the raw measures used to a text file: the output text file"""
    
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
        if self.opt_dump_text_text_out is not None:
            cargs.extend(["-dump-text", self.opt_dump_text_text_out])
        return cargs


class CiftiFalseCorrelationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_false_correlation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti dscalar file"""


def cifti_false_correlation(
    cifti_in: InputPathType,
    v_3d_dist: float | int,
    geo_outer: float | int,
    geo_inner: float | int,
    cifti_out: InputPathType,
    left_surface: CiftiFalseCorrelationLeftSurface | None = None,
    right_surface: CiftiFalseCorrelationRightSurface | None = None,
    cerebellum_surface: CiftiFalseCorrelationCerebellumSurface | None = None,
    runner: Runner = None,
) -> CiftiFalseCorrelationOutputs:
    """
    cifti-false-correlation by Washington University School of Medicin.
    
    Compare correlation locally and across/through sulci/gyri.
    
    For each vertex, compute the average correlation within a range of geodesic
    distances that don't cross a sulcus/gyrus, and the correlation to the
    closest vertex crossing a sulcus/gyrus. A vertex is considered to cross a
    sulcus/gyrus if the 3D distance is less than a third of the geodesic
    distance. The output file contains the ratio between these correlations, and
    some additional maps to help explain the ratio.
    
    Args:
        cifti_in: the cifti file to use for correlation
        v_3d_dist: maximum 3D distance to check around each vertex
        geo_outer: maximum geodesic distance to use for neighboring correlation
        geo_inner: minimum geodesic distance to use for neighboring correlation
        cifti_out: the output cifti dscalar file
        left_surface: specify the left surface to use
        right_surface: specify the right surface to use
        cerebellum_surface: specify the cerebellum surface to use
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiFalseCorrelationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_FALSE_CORRELATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-false-correlation")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(str(v_3d_dist))
    cargs.append(str(geo_outer))
    cargs.append(str(geo_inner))
    cargs.append(execution.input_file(cifti_out))
    if left_surface is not None:
        cargs.extend(["-left-surface", *left_surface.run(execution)])
    if right_surface is not None:
        cargs.extend(["-right-surface", *right_surface.run(execution)])
    if cerebellum_surface is not None:
        cargs.extend(["-cerebellum-surface", *cerebellum_surface.run(execution)])
    ret = CiftiFalseCorrelationOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_FALSE_CORRELATION_METADATA",
    "CiftiFalseCorrelationCerebellumSurface",
    "CiftiFalseCorrelationLeftSurface",
    "CiftiFalseCorrelationOutputs",
    "CiftiFalseCorrelationRightSurface",
    "cifti_false_correlation",
]
