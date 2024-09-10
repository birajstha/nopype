# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VOLUME_PARCEL_RESAMPLING_METADATA = Metadata(
    id="376706531de016c2979b926deae7b1478d8df498.boutiques",
    name="volume-parcel-resampling",
    package="workbench",
    container_image_tag="fcpindi/c-pac:latest",
)


class VolumeParcelResamplingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_parcel_resampling(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """output volume"""


def volume_parcel_resampling(
    volume_in: InputPathType,
    cur_parcels: InputPathType,
    new_parcels: InputPathType,
    kernel: float,
    volume_out: str,
    opt_fix_zeros: bool = False,
    opt_fwhm: bool = False,
    opt_subvolume_subvol: str | None = None,
    runner: Runner | None = None,
) -> VolumeParcelResamplingOutputs:
    """
    Smooth and resample volume parcels.
    
    Smooths and resamples the region inside each label in cur-parcels to the
    region of the same label name in new-parcels. Any voxels in the output label
    region but outside the input label region will be extrapolated from nearby
    data. The -fix-zeros option causes the smoothing to not use an input value
    if it is zero, but still write a smoothed value to the voxel, and after
    smoothing is complete, it will check for any remaining values of zero, and
    fill them in with extrapolated values.
    
    Note: all volumes must have the same dimensions and spacing. To use a
    different output space, see -volume-parcel-resampling-generic.
    
    Author: Washington University School of Medicin
    
    Args:
        volume_in: the input data volume.
        cur_parcels: label volume of where the parcels currently are.
        new_parcels: label volume of where the parcels should be.
        kernel: gaussian kernel size in mm to smooth by during resampling, as\
            sigma by default.
        volume_out: output volume.
        opt_fix_zeros: treat zero values as not being data.
        opt_fwhm: smoothing kernel size is FWHM, not sigma.
        opt_subvolume_subvol: select a single subvolume as input: the subvolume\
            number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeParcelResamplingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_PARCEL_RESAMPLING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-parcel-resampling")
    cargs.append(execution.input_file(volume_in))
    cargs.append(execution.input_file(cur_parcels))
    cargs.append(execution.input_file(new_parcels))
    cargs.append(str(kernel))
    cargs.append(volume_out)
    if opt_fix_zeros:
        cargs.append("-fix-zeros")
    if opt_fwhm:
        cargs.append("-fwhm")
    if opt_subvolume_subvol is not None:
        cargs.extend([
            "-subvolume",
            opt_subvolume_subvol
        ])
    ret = VolumeParcelResamplingOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(volume_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_PARCEL_RESAMPLING_METADATA",
    "VolumeParcelResamplingOutputs",
    "volume_parcel_resampling",
]
