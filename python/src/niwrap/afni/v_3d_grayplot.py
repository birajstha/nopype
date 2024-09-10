# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_GRAYPLOT_METADATA = Metadata(
    id="86953453682f81ec7a6602db14e1538725d52f70.boutiques",
    name="3dGrayplot",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dGrayplotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_grayplot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    grayplot_img: OutputPathType | None
    """Grayplot image file"""


def v_3d_grayplot(
    input_: InputPathType,
    mask: InputPathType | None = None,
    prefix: str | None = None,
    dimensions: list[float] | None = None,
    resample_old: bool = False,
    polort: float | None = None,
    fwhm: float | None = None,
    ijkorder: bool = False,
    range_: float | None = None,
    percent: bool = False,
    raw_with_bounds: list[float] | None = None,
    runner: Runner | None = None,
) -> V3dGrayplotOutputs:
    """
    Make a grayplot from a 3D+time dataset, like a carpet plot. Result is saved to a
    PNG image.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dGrayplot.html
    
    Args:
        input_: Input dataset.
        mask: Name of mask dataset. Voxels that are 0 in the mask will not be\
            processed.
        prefix: Name for the output file. Default is Grayplot.png.
        dimensions: Output size of image in pixels: [width height]. Defaults\
            are width=1024 and height=512.
        resample_old: Original resampling method for processed dataset.
        polort: Order of polynomials for detrending. Default is 2. Use '-1' if\
            data is already detrended and de-meaned.
        fwhm: FWHM of blurring radius to use in the dataset before making the\
            image. Default is 0 mm.
        ijkorder: Default intra-partition ordering by dataset 3D index ('ijk').
        range_: Set the range of the data to be plotted. Value of 0 is\
            middle-gray, +X is white, -X is black.
        percent: Scale values to percent differences from the mean of each\
            voxel timeseries. Suitable for raw time series datasets.
        raw_with_bounds: Map values <= A to black, values >= B to white, and\
            intermediate values to grays.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dGrayplotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_GRAYPLOT_METADATA)
    cargs = []
    cargs.append("3dGrayplot")
    cargs.append("[OVERLAY_FLAG]")
    cargs.append(execution.input_file(input_))
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if dimensions is not None:
        cargs.extend([
            "-dimen",
            *map(str, dimensions)
        ])
    if resample_old:
        cargs.append("-oldresam")
    if polort is not None:
        cargs.extend([
            "-polort",
            str(polort)
        ])
    if fwhm is not None:
        cargs.extend([
            "-fwhm",
            str(fwhm)
        ])
    if ijkorder:
        cargs.append("-ijkorder")
    if range_ is not None:
        cargs.extend([
            "-range",
            str(range_)
        ])
    if percent:
        cargs.append("-percent")
    if raw_with_bounds is not None:
        cargs.extend([
            "-raw_with_bounds",
            *map(str, raw_with_bounds)
        ])
    ret = V3dGrayplotOutputs(
        root=execution.output_file("."),
        grayplot_img=execution.output_file(prefix) if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dGrayplotOutputs",
    "V_3D_GRAYPLOT_METADATA",
    "v_3d_grayplot",
]
