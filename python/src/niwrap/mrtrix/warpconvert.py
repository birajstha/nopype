# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


WARPCONVERT_METADATA = Metadata(
    id="c5de6be0f5508d3923727e3ac0053b895dbbe427",
    name="warpconvert",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class WarpconvertConfig:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value: str
    """temporarily set the value of an MRtrix config file entry."""
    
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
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


class WarpconvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `warpconvert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out: OutputPathType
    """the output warp image."""


def warpconvert(
    in_: InputPathType,
    type_: typing.Literal["type"],
    out: InputPathType,
    template: InputPathType | None = None,
    midway_space: bool = False,
    from_: int | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[WarpconvertConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> WarpconvertOutputs:
    """
    warpconvert by David Raffelt (david.raffelt@florey.edu.au).
    
    Convert between different representations of a non-linear warp.
    
    A deformation field is defined as an image where each voxel defines the
    corresponding position in the other image (in scanner space coordinates). A
    displacement field stores the displacements (in mm) to the other image from
    the each voxel's position (in scanner space). The warpfull file is the 5D
    format output from mrregister -nl_warp_full, which contains linear
    transforms, warps and their inverses that map each image to a midway space.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/warpconvert.html
    
    Args:
        in_: the input warp image.
        type_: the conversion type required. Valid choices are:
            deformation2displacement, displacement2deformation,
            warpfull2deformation, warpfull2displacement
        out: the output warp image.
        template: define a template image when converting a warpfull file (which
            is defined on a grid in the midway space between image 1 & 2). For
            example to generate the deformation field that maps image1 to image2,
            then supply image2 as the template image
        midway_space: to be used only with warpfull2deformation and
            warpfull2displacement conversion types. The output will only contain the
            non-linear warp to map an input image to the midway space (defined by
            the warpfull grid). If a linear transform exists in the warpfull file
            header then it will be composed and included in the output.
        from_: to be used only with warpfull2deformation and
            warpfull2displacement conversion types. Used to define the direction of
            the desired output field.Use -from 1 to obtain the image1->image2 field
            and from 2 for image2->image1. Can be used in combination with the
            -midway_space option to produce a field that only maps to midway space.
        info: display information messages.
        quiet: do not display information messages or progress status;
            alternatively, this can be achieved by setting the MRTRIX_QUIET
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications (set
            to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `WarpconvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WARPCONVERT_METADATA)
    cargs = []
    cargs.append("warpconvert")
    if template is not None:
        cargs.extend(["-template", execution.input_file(template)])
    if midway_space:
        cargs.append("-midway_space")
    if from_ is not None:
        cargs.extend(["-from", str(from_)])
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend(["-nthreads", str(nthreads)])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(in_))
    cargs.append(type_)
    cargs.append(execution.input_file(out))
    ret = WarpconvertOutputs(
        root=execution.output_file("."),
        out=execution.output_file(f"{pathlib.Path(out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "WARPCONVERT_METADATA",
    "WarpconvertConfig",
    "WarpconvertOutputs",
    "warpconvert",
]
