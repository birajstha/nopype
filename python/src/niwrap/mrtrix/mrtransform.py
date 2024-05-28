# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


MRTRANSFORM_METADATA = Metadata(
    id="48e30bf76b0a70833df4e7a384fb8e93e0253d84",
    name="mrtransform",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class MrtransformFslgrad:
    """
    Provide the diffusion-weighted gradient scheme used in the acquisition in FSL bvecs/bvals format files. If a diffusion gradient scheme is present in the input image header, the data provided with this option will be instead used.
    """
    bvecs: InputPathType
    """Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used."""
    bvals: InputPathType
    """Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used."""
    
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
        cargs.append("-fslgrad")
        cargs.append(execution.input_file(self.bvecs))
        cargs.append(execution.input_file(self.bvals))
        return cargs


@dataclasses.dataclass
class MrtransformExportGradFsl:
    """
    export the diffusion-weighted gradient table to files in FSL (bvecs / bvals) format
    """
    bvecs_path: InputPathType
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""
    bvals_path: InputPathType
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""
    
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
        cargs.append("-export_grad_fsl")
        cargs.append(execution.input_file(self.bvecs_path))
        cargs.append(execution.input_file(self.bvals_path))
        return cargs


@dataclasses.dataclass
class MrtransformConfig:
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


class MrtransformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrtransform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output image."""
    export_grad_mrtrix: OutputPathType | None
    """export the diffusion-weighted gradient table to file in MRtrix format """


def mrtransform(
    input_: InputPathType,
    output: InputPathType,
    linear: InputPathType | None = None,
    flip: list[int] = None,
    inverse: bool = False,
    half: bool = False,
    replace: InputPathType | None = None,
    identity: bool = False,
    template: InputPathType | None = None,
    midway_space: bool = False,
    interp: typing.Literal["method"] | None = None,
    oversample: list[int] = None,
    warp: InputPathType | None = None,
    warp_full: InputPathType | None = None,
    from_: int | None = None,
    modulate: typing.Literal["intensity modulation method"] | None = None,
    directions: InputPathType | None = None,
    reorient_fod: str | None = None,
    grad: InputPathType | None = None,
    fslgrad: MrtransformFslgrad | None = None,
    export_grad_mrtrix: InputPathType | None = None,
    export_grad_fsl: MrtransformExportGradFsl | None = None,
    datatype: typing.Literal["spec"] | None = None,
    strides: str | None = None,
    nan: bool = False,
    no_reorientation: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrtransformConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> MrtransformOutputs:
    """
    mrtransform by J-Donald Tournier (jdtournier@gmail.com) and David Raffelt
    (david.raffelt@florey.edu.au) and Max Pietsch (maximilian.pietsch@kcl.ac.uk).
    
    Apply spatial transformations to an image.
    
    If a linear transform is applied without a template image the command will
    modify the image header transform matrix
    
    FOD reorientation (with apodised point spread functions) can be performed if
    the number of volumes in the 4th dimension equals the number of coefficients
    in an antipodally symmetric spherical harmonic series (e.g. 6, 15, 28 etc).
    For such data, the -reorient_fod yes/no option must be used to specify if
    reorientation is required.
    
    The output image intensity can be modulated using the (local or global)
    volume change if a linear or nonlinear transformation is applied. 'FOD'
    modulation preserves the apparent fibre density across the fibre bundle
    width and can only be applied if FOD reorientation is used. Alternatively,
    non-directional scaling by the Jacobian determinant can be applied to any
    image type.
    
    If a DW scheme is contained in the header (or specified separately), and the
    number of directions matches the number of volumes in the images, any
    transformation applied using the -linear option will also be applied to the
    directions.
    
    When the -template option is used to specify the target image grid, the
    image provided via this option will not influence the axis data strides of
    the output image; these are determined based on the input image, or the
    input to the -strides option.
    
    References:
    
    * If FOD reorientation is being performed:
    Raffelt, D.; Tournier, J.-D.; Crozier, S.; Connelly, A. & Salvado, O.
    Reorientation of fiber orientation distributions using apodized point spread
    functions. Magnetic Resonance in Medicine, 2012, 67, 844-855
    
    * If FOD modulation is being performed:
    Raffelt, D.; Tournier, J.-D.; Rose, S.; Ridgway, G.R.; Henderson, R.;
    Crozier, S.; Salvado, O.; Connelly, A.; Apparent Fibre Density: a novel
    measure for the analysis of diffusion-weighted magnetic resonance images.
    NeuroImage, 2012, 15;59(4), 3976-94.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/mrtransform.html
    
    Args:
        input_: input image to be transformed.
        output: the output image.
        linear: specify a linear transform to apply, in the form of a 3x4 or 4x4
            ascii file. Note the standard 'reverse' convention is used, where the
            transform maps points in the template image to the moving image. Note
            that the reverse convention is still assumed even if no -template image
            is supplied
        flip: flip the specified axes, provided as a comma-separated list of
            indices (0:x, 1:y, 2:z).
        inverse: apply the inverse transformation
        half: apply the matrix square root of the transformation. This can be
            combined with the inverse option.
        replace: replace the linear transform of the original image by that
            specified, rather than applying it to the original image. The specified
            transform can be either a template image, or a 3x4 or 4x4 ascii file.
        identity: set the header transform of the image to the identity matrix
        template: reslice the input image to match the specified template image
            grid.
        midway_space: reslice the input image to the midway space. Requires
            either the -template or -warp option. If used with -template and -linear
            option the input image will be resliced onto the grid halfway between
            the input and template. If used with the -warp option the input will be
            warped to the midway space defined by the grid of the input warp (i.e.
            half way between image1 and image2)
        interp: set the interpolation method to use when reslicing (choices:
            nearest, linear, cubic, sinc. Default: cubic).
        oversample: set the amount of over-sampling (in the target space) to
            perform when regridding. This is particularly relevant when downsamping
            a high-resolution image to a low-resolution image, to avoid aliasing
            artefacts. This can consist of a single integer, or a comma-separated
            list of 3 integers if different oversampling factors are desired along
            the different axes. Default is determined from ratio of voxel dimensions
            (disabled for nearest-neighbour interpolation).
        warp: apply a non-linear 4D deformation field to warp the input image.
            Each voxel in the deformation field must define the scanner space
            position that will be used to interpolate the input image during warping
            (i.e. pull-back/reverse warp convention). If the -template image is also
            supplied the deformation field will be resliced first to the template
            image grid. If no -template option is supplied then the output image
            will have the same image grid as the deformation field. This option can
            be used in combination with the -affine option, in which case the affine
            will be applied first)
        warp_full: warp the input image using a 5D warp file output from
            mrregister. Any linear transforms in the warp image header will also be
            applied. The -warp_full option must be used in combination with either
            the -template option or the -midway_space option. If a -template image
            is supplied then the full warp will be used. By default the
            image1->image2 transform will be applied, however the -from 2 option can
            be used to apply the image2->image1 transform. Use the -midway_space
            option to warp the input image to the midway space. The -from option can
            also be used to define which warp to use when transforming to midway
            space
        from_: used to define which space the input image is when using the
            -warp_mid option. Use -from 1 to warp from image1 or -from 2 to warp
            from image2
        modulate: Valid choices are: fod and jac.
            fod: modulate FODs during reorientation to preserve the
            apparent fibre density across fibre bundle widths before
            and after the transformation.
            jac: modulate the image intensity with the determinant of
            the Jacobian of the warp of linear transformation to
            preserve the total intensity before and after the
            transformation.
        directions: directions defining the number and orientation of the
            apodised point spread functions used in FOD reorientation (Default: 300
            directions)
        reorient_fod: specify whether to perform FOD reorientation. This is
            required if the number of volumes in the 4th dimension corresponds to
            the number of coefficients in an antipodally symmetric spherical
            harmonic series with lmax >= 2 (i.e. 6, 15, 28, 45, 66 volumes).
        grad: Provide the diffusion-weighted gradient scheme used in the
            acquisition in a text file. This should be supplied as a 4xN text file
            with each line is in the format [ X Y Z b ], where [ X Y Z ] describe
            the direction of the applied gradient, and b gives the b-value in units
            of s/mm^2. If a diffusion gradient scheme is present in the input image
            header, the data provided with this option will be instead used.
        fslgrad: Provide the diffusion-weighted gradient scheme used in the
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient
            scheme is present in the input image header, the data provided with this
            option will be instead used.
        export_grad_mrtrix: export the diffusion-weighted gradient table to file
            in MRtrix format
        export_grad_fsl: export the diffusion-weighted gradient table to files
            in FSL (bvecs / bvals) format
        datatype: specify output image data type. Valid choices are: float32,
            float32le, float32be, float64, float64le, float64be, int64, uint64,
            int64le, uint64le, int64be, uint64be, int32, uint32, int32le, uint32le,
            int32be, uint32be, int16, uint16, int16le, uint16le, int16be, uint16be,
            cfloat32, cfloat32le, cfloat32be, cfloat64, cfloat64le, cfloat64be,
            int8, uint8, bit.
        strides: specify the strides of the output data in memory; either as a
            comma-separated list of (signed) integers, or as a template image from
            which the strides shall be extracted and used. The actual strides
            produced will depend on whether the output image format can support it.
        nan: Use NaN as the out of bounds value (Default: 0.0)
        no_reorientation: deprecated, use -reorient_fod instead
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
        NamedTuple of outputs (described in `MrtransformOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRTRANSFORM_METADATA)
    cargs = []
    cargs.append("mrtransform")
    if linear is not None:
        cargs.extend(["-linear", execution.input_file(linear)])
    if flip is not None:
        cargs.extend(["-flip", *map(str, flip)])
    if inverse:
        cargs.append("-inverse")
    if half:
        cargs.append("-half")
    if replace is not None:
        cargs.extend(["-replace", execution.input_file(replace)])
    if identity:
        cargs.append("-identity")
    if template is not None:
        cargs.extend(["-template", execution.input_file(template)])
    if midway_space:
        cargs.append("-midway_space")
    if interp is not None:
        cargs.extend(["-interp", interp])
    if oversample is not None:
        cargs.extend(["-oversample", *map(str, oversample)])
    if warp is not None:
        cargs.extend(["-warp", execution.input_file(warp)])
    if warp_full is not None:
        cargs.extend(["-warp_full", execution.input_file(warp_full)])
    if from_ is not None:
        cargs.extend(["-from", str(from_)])
    if modulate is not None:
        cargs.extend(["-modulate", modulate])
    if directions is not None:
        cargs.extend(["-directions", execution.input_file(directions)])
    if reorient_fod is not None:
        cargs.extend(["-reorient_fod", reorient_fod])
    if grad is not None:
        cargs.extend(["-grad", execution.input_file(grad)])
    if fslgrad is not None:
        cargs.extend(fslgrad.run(execution))
    if export_grad_mrtrix is not None:
        cargs.extend(["-export_grad_mrtrix", execution.input_file(export_grad_mrtrix)])
    if export_grad_fsl is not None:
        cargs.extend(export_grad_fsl.run(execution))
    if datatype is not None:
        cargs.extend(["-datatype", datatype])
    if strides is not None:
        cargs.extend(["-strides", strides])
    if nan:
        cargs.append("-nan")
    if no_reorientation:
        cargs.append("-no_reorientation")
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
    cargs.append(execution.input_file(input_))
    cargs.append(execution.input_file(output))
    ret = MrtransformOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).stem}"),
        export_grad_mrtrix=execution.output_file(f"{pathlib.Path(export_grad_mrtrix).stem}") if export_grad_mrtrix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRTRANSFORM_METADATA",
    "MrtransformConfig",
    "MrtransformExportGradFsl",
    "MrtransformFslgrad",
    "MrtransformOutputs",
    "mrtransform",
]
