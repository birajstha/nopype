# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_DILATE_METADATA = Metadata(
    id="63d0c186cadb7324c55d375c82dd265f18051428",
    name="cifti-dilate",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiDilateLeftSurface:
    """
    specify the left surface to use
    """
    opt_left_corrected_areas_area_metric: InputPathType | None = None
    """vertex areas to use instead of computing them from the left surface: the
    corrected vertex areas, as a metric"""
    
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
        if self.opt_left_corrected_areas_area_metric is not None:
            cargs.extend(["-left-corrected-areas", execution.input_file(self.opt_left_corrected_areas_area_metric)])
        return cargs


@dataclasses.dataclass
class CiftiDilateRightSurface:
    """
    specify the right surface to use
    """
    opt_right_corrected_areas_area_metric: InputPathType | None = None
    """vertex areas to use instead of computing them from the right surface: the
    corrected vertex areas, as a metric"""
    
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
        if self.opt_right_corrected_areas_area_metric is not None:
            cargs.extend(["-right-corrected-areas", execution.input_file(self.opt_right_corrected_areas_area_metric)])
        return cargs


@dataclasses.dataclass
class CiftiDilateCerebellumSurface:
    """
    specify the cerebellum surface to use
    """
    opt_cerebellum_corrected_areas_area_metric: InputPathType | None = None
    """vertex areas to use instead of computing them from the cerebellum
    surface: the corrected vertex areas, as a metric"""
    
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
        if self.opt_cerebellum_corrected_areas_area_metric is not None:
            cargs.extend(["-cerebellum-corrected-areas", execution.input_file(self.opt_cerebellum_corrected_areas_area_metric)])
        return cargs


class CiftiDilateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_dilate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_dilate(
    cifti_in: InputPathType,
    direction: str,
    surface_distance: float | int,
    volume_distance: float | int,
    cifti_out: InputPathType,
    left_surface: CiftiDilateLeftSurface | None = None,
    right_surface: CiftiDilateRightSurface | None = None,
    cerebellum_surface: CiftiDilateCerebellumSurface | None = None,
    opt_bad_brainordinate_roi_roi_cifti: InputPathType | None = None,
    opt_nearest: bool = False,
    opt_merged_volume: bool = False,
    opt_legacy_mode: bool = False,
    runner: Runner = None,
) -> CiftiDilateOutputs:
    """
    cifti-dilate by Washington University School of Medicin.
    
    Dilate a cifti file.
    
    For all data values designated as bad, if they neighbor a good value or are
    within the specified distance of a good value in the same kind of model,
    replace the value with a distance weighted average of nearby good values,
    otherwise set the value to zero. If -nearest is specified, it will use the
    value from the closest good value within range instead of a weighted
    average. When the input file contains label data, nearest dilation is used
    on the surface, and weighted popularity is used in the volume.
    
    The -*-corrected-areas options are intended for dilating on group average
    surfaces, but it is only an approximate correction for the reduction of
    structure in a group average surface.
    
    If -bad-brainordinate-roi is specified, all values, including those with
    value zero, are good, except for locations with a positive value in the ROI.
    If it is not specified, only values equal to zero are bad.
    
    Args:
        cifti_in: the input cifti file
        direction: which dimension to dilate along, ROW or COLUMN
        surface_distance: the distance to dilate on surfaces, in mm
        volume_distance: the distance to dilate in the volume, in mm
        cifti_out: the output cifti file
        left_surface: specify the left surface to use
        right_surface: specify the right surface to use
        cerebellum_surface: specify the cerebellum surface to use
        opt_bad_brainordinate_roi_roi_cifti: specify an roi of brainordinates to
            overwrite, rather than zeros: cifti dscalar or dtseries file, positive
            values denote brainordinates to have their values replaced
        opt_nearest: use nearest good value instead of a weighted average
        opt_merged_volume: treat volume components as if they were a single
            component
        opt_legacy_mode: use the math from v1.3.2 and earlier for weighted
            dilation
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiDilateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_DILATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-dilate")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(direction)
    cargs.append(str(surface_distance))
    cargs.append(str(volume_distance))
    cargs.append(execution.input_file(cifti_out))
    if left_surface is not None:
        cargs.extend(["-left-surface", *left_surface.run(execution)])
    if right_surface is not None:
        cargs.extend(["-right-surface", *right_surface.run(execution)])
    if cerebellum_surface is not None:
        cargs.extend(["-cerebellum-surface", *cerebellum_surface.run(execution)])
    if opt_bad_brainordinate_roi_roi_cifti is not None:
        cargs.extend(["-bad-brainordinate-roi", execution.input_file(opt_bad_brainordinate_roi_roi_cifti)])
    if opt_nearest:
        cargs.append("-nearest")
    if opt_merged_volume:
        cargs.append("-merged-volume")
    if opt_legacy_mode:
        cargs.append("-legacy-mode")
    ret = CiftiDilateOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_DILATE_METADATA",
    "CiftiDilateCerebellumSurface",
    "CiftiDilateLeftSurface",
    "CiftiDilateOutputs",
    "CiftiDilateRightSurface",
    "cifti_dilate",
]
