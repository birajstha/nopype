# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

ANTS_APPLY_TRANSFORMS_METADATA = Metadata(
    id="0c6fa951a055b8a31c90ee449813ff74f023bf3a",
    name="antsApplyTransforms",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class AntsApplyTransformsWarpedOutputOutputs(typing.NamedTuple):
    """
    Output object returned when calling `AntsApplyTransformsWarpedOutput.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_outfile: OutputPathType
    """Warped image."""


@dataclasses.dataclass
class AntsApplyTransformsWarpedOutput:
    """
    Output the warped image.
    """
    warped_output_file_name: InputPathType
    """Output file name."""
    
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
        cargs.append(execution.input_file(self.warped_output_file_name))
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> AntsApplyTransformsWarpedOutputOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `AntsApplyTransformsWarpedOutputOutputs`).
        """
        ret = AntsApplyTransformsWarpedOutputOutputs(
            root=execution.output_file("."),
            output_image_outfile=execution.output_file(f"{pathlib.Path(self.warped_output_file_name).name}"),
        )
        return ret


class AntsApplyTransformsCompositeDisplacementFieldOutputOutputs(typing.NamedTuple):
    """
    Output object returned when calling `AntsApplyTransformsCompositeDisplacementFieldOutput.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_outfile_: OutputPathType
    """Warped image."""


@dataclasses.dataclass
class AntsApplyTransformsCompositeDisplacementFieldOutput:
    """
    Print out the displacement field based on the composite transform and the reference image.
    """
    composite_displacement_field: InputPathType
    """Output file name."""
    print_out_composite_warp_file: typing.Literal[0, 1] | None = None
    """Output a composite warp file instead of a transformed image."""
    
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
        cargs.append(
            "[" +
            execution.input_file(self.composite_displacement_field) +
            ((",printOutCompositeWarpFile=" + str(self.print_out_composite_warp_file)) if self.print_out_composite_warp_file is not None else "") +
            "]"
        )
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> AntsApplyTransformsCompositeDisplacementFieldOutputOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `AntsApplyTransformsCompositeDisplacementFieldOutputOutputs`).
        """
        ret = AntsApplyTransformsCompositeDisplacementFieldOutputOutputs(
            root=execution.output_file("."),
            output_image_outfile_=execution.output_file(f"{pathlib.Path(self.composite_displacement_field).name}"),
        )
        return ret


class AntsApplyTransformsGenericAffineTransformOutputOutputs(typing.NamedTuple):
    """
    Output object returned when calling `AntsApplyTransformsGenericAffineTransformOutput.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_outfile_2: OutputPathType
    """Warped image."""


@dataclasses.dataclass
class AntsApplyTransformsGenericAffineTransformOutput:
    """
    Compose all affine transforms and (if boolean is set) calculate its inverse which is then written to an ITK file.
    """
    generic_affine_transform_file: InputPathType
    """Output file name."""
    calculate_inverse: typing.Literal[0, 1] | None = None
    """Calculate the inverse of the affine transform."""
    
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
        cargs.append(
            "Linear[" +
            execution.input_file(self.generic_affine_transform_file) +
            ((",calculateInverse=" + str(self.calculate_inverse)) if self.calculate_inverse is not None else "") +
            "]"
        )
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> AntsApplyTransformsGenericAffineTransformOutputOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `AntsApplyTransformsGenericAffineTransformOutputOutputs`).
        """
        ret = AntsApplyTransformsGenericAffineTransformOutputOutputs(
            root=execution.output_file("."),
            output_image_outfile_2=execution.output_file(f"{pathlib.Path(self.generic_affine_transform_file).name}"),
        )
        return ret


@dataclasses.dataclass
class AntsApplyTransformsLinear:
    """
    Linear interpolation.
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
        cargs.append("Linear")
        return cargs


@dataclasses.dataclass
class AntsApplyTransformsNearestNeighbor:
    """
    Nearest neighbor interpolation.
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
        cargs.append("NearestNeighbor")
        return cargs


@dataclasses.dataclass
class AntsApplyTransformsMultiLabel:
    """
    Multi label interpolation.
    """
    sigma: float | int | None = None
    """Sigma value."""
    alpha: float | int | None = None
    """Alpha value."""
    
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
        if self.sigma is not None or self.alpha is not None:
            cargs.append(
                "MultiLabel[" +
                (("sigma=" + str(self.sigma)) if self.sigma is not None else "") +
                ((",alpha=" + str(self.alpha)) if self.alpha is not None else "") +
                "]"
            )
        return cargs


@dataclasses.dataclass
class AntsApplyTransformsGaussian:
    """
    Gaussian interpolation.
    """
    sigma: float | int | None = None
    """Sigma value."""
    alpha: float | int | None = None
    """Alpha value."""
    
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
        if self.sigma is not None or self.alpha is not None:
            cargs.append(
                "Gaussian[" +
                (("sigma=" + str(self.sigma)) if self.sigma is not None else "") +
                ((",alpha=" + str(self.alpha)) if self.alpha is not None else "") +
                "]"
            )
        return cargs


@dataclasses.dataclass
class AntsApplyTransformsBspline:
    """
    BSpline interpolation.
    """
    order: int | None = None
    """Order value."""
    
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
        if self.order is not None:
            cargs.append(
                "BSpline[" +
                ("order=" + str(self.order)) +
                "]"
            )
        return cargs


@dataclasses.dataclass
class AntsApplyTransformsCosineWindowedSinc:
    """
    Cosine windowed sinc interpolation.
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
        cargs.append("CosineWindowedSinc")
        return cargs


@dataclasses.dataclass
class AntsApplyTransformsWelchWindowedSinc:
    """
    Welch windowed sinc interpolation.
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
        cargs.append("WelchWindowedSinc")
        return cargs


@dataclasses.dataclass
class AntsApplyTransformsHammingWindowedSinc:
    """
    Hamming windowed sinc interpolation.
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
        cargs.append("HammingWindowedSinc")
        return cargs


@dataclasses.dataclass
class AntsApplyTransformsLanczosWindowedSinc:
    """
    Lanczos windowed sinc interpolation.
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
        cargs.append("LanczosWindowedSinc")
        return cargs


@dataclasses.dataclass
class AntsApplyTransformsGenericLabel:
    """
    Generic label interpolation.
    """
    interpolator: str | None = None
    """Interpolator value."""
    
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
        if self.interpolator is not None:
            cargs.append(
                "GenericLabel[" +
                ("interpolator=" + self.interpolator) +
                "]"
            )
        return cargs


@dataclasses.dataclass
class AntsApplyTransformsTransformFileName:
    """
    Transform file name.
    """
    transform_file_name: InputPathType
    """Transform file name."""
    
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
        cargs.append(execution.input_file(self.transform_file_name))
        return cargs


@dataclasses.dataclass
class AntsApplyTransformsUseInverse:
    """
    Use inverse.
    """
    transform_file_name: InputPathType
    """Transform file name."""
    
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
        cargs.append(
            "[" +
            execution.input_file(self.transform_file_name) +
            ",useInverse]"
        )
        return cargs


class AntsApplyTransformsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_apply_transforms(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: typing.Union[AntsApplyTransformsWarpedOutputOutputs, AntsApplyTransformsCompositeDisplacementFieldOutputOutputs, AntsApplyTransformsGenericAffineTransformOutputOutputs]
    """Subcommand outputs"""


def ants_apply_transforms(
    input_image: InputPathType,
    reference_image: InputPathType,
    output: typing.Union[AntsApplyTransformsWarpedOutput, AntsApplyTransformsCompositeDisplacementFieldOutput, AntsApplyTransformsGenericAffineTransformOutput],
    transform: list[typing.Union[AntsApplyTransformsTransformFileName, AntsApplyTransformsUseInverse]],
    dimensionality: typing.Literal[2, 3, 4] | None = None,
    input_image_type: typing.Literal[0, 1, 2, 3, 4, 5] | None = None,
    interpolation: typing.Union[AntsApplyTransformsLinear, AntsApplyTransformsNearestNeighbor, AntsApplyTransformsMultiLabel, AntsApplyTransformsGaussian, AntsApplyTransformsBspline, AntsApplyTransformsCosineWindowedSinc, AntsApplyTransformsWelchWindowedSinc, AntsApplyTransformsHammingWindowedSinc, AntsApplyTransformsLanczosWindowedSinc, AntsApplyTransformsGenericLabel] | None = None,
    output_data_type: typing.Literal["char", "uchar", "short", "int", "float", "double", "default"] | None = None,
    default_value: float | int | None = None,
    static_cast_for_r: str | None = None,
    float_: typing.Literal[0, 1] | None = None,
    verbose: typing.Literal[0, 1] | None = None,
    runner: Runner = None,
) -> AntsApplyTransformsOutputs:
    """
    antsApplyTransforms by Nipype (interface).
    
    antsApplyTransforms, applied to an input image, transforms it according to a
    reference image and a transform (or a set of transforms).
    
    Args:
        input_image: Currently, the only input objects supported are image
            objects. However, the current framework allows for warping of other
            objects such as meshes and point sets.
        reference_image: For warping input images, the reference image defines
            the spacing, origin, size, and direction of the output warped image.
        output: One can either output the warped image or, if the boolean is
            set, one can print out the displacement field based on the composite
            transform and the reference image. A third option is to compose all
            affine transforms and (if boolean is set) calculate its inverse which is
            then written to an ITK file.
        transform: Several transform options are supported including all those
            defined in the ITK library in addition to a deformation field transform.
            The ordering of the transformations follows the ordering specified on
            the command line. An identity transform is pushed onto the
            transformation stack. Each new transform encountered on the command line
            is also pushed onto the transformation stack. Then, to warp the input
            object, each point comprising the input object is warped first according
            to the last transform pushed onto the stack followed by the second to
            last transform, etc. until the last transform encountered which is the
            identity transform. Also, it should be noted that the inverse transform
            can be accommodated with the usual caveat that such an inverse must be
            defined by the specified transform class.
        dimensionality: This option forces the image to be treated as a
            specified-dimensional image. if not specified, antswarp tries to infer
            the dimensionality from the input image.
        input_image_type: Option specifying the input image type of scalar
            (default), vector, tensor, time series, or multi-channel. A time series
            image is a scalar image defined by an additional dimension for the time
            component whereas a multi-channel image is a vector image with only
            spatial dimensions. Five-dimensional images are e.g., AFNI stats image.
        interpolation: Several interpolation options are available in ITK. These
            have all been made available.
        output_data_type: Output image data type. This is a direct typecast;
            output values are not rescaled. Default is to use the internal data type
            (float or double). uchar is unsigned char; others are signed. WARNING:
            Outputs will be incorrect (overflowed/reinterpreted) if values exceed
            the range allowed by your choice. Note that some pixel types are not
            supported by some image formats. e.g. int is not supported by jpg.
        default_value: Default voxel value to be used with input images only.
            Specifies the voxel value when the input point maps outside the output
            domain. With tensor input images, specifies the default voxel
            eigenvalues.
        static_cast_for_r: Forces static cast in ReadTransform (for R).
        float_: Use float instead of double for computations.
        verbose: Verbose output.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `AntsApplyTransformsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_APPLY_TRANSFORMS_METADATA)
    cargs = []
    cargs.append("antsApplyTransforms")
    if dimensionality is not None:
        cargs.extend(["--dimensionality", str(dimensionality)])
    if input_image_type is not None:
        cargs.extend(["--input-image-type", str(input_image_type)])
    cargs.extend(["--input", execution.input_file(input_image)])
    cargs.extend(["--reference-image", execution.input_file(reference_image)])
    cargs.extend(["--output", *output.run(execution)])
    if interpolation is not None:
        cargs.extend(["--interpolation", *interpolation.run(execution)])
    if output_data_type is not None:
        cargs.extend(["--output-data-type", output_data_type])
    cargs.extend(["--transform", *[a for c in [s.run(execution) for s in transform] for a in c]])
    if default_value is not None:
        cargs.extend(["--default-value", str(default_value)])
    if static_cast_for_r is not None:
        cargs.extend(["--static-cast-for-R", static_cast_for_r])
    if float_ is not None:
        cargs.extend(["--float", str(float_)])
    if verbose is not None:
        cargs.extend(["--verbose", str(verbose)])
    ret = AntsApplyTransformsOutputs(
        root=execution.output_file("."),
        output=output.outputs(execution),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANTS_APPLY_TRANSFORMS_METADATA",
    "AntsApplyTransformsBspline",
    "AntsApplyTransformsCompositeDisplacementFieldOutput",
    "AntsApplyTransformsCompositeDisplacementFieldOutputOutputs",
    "AntsApplyTransformsCosineWindowedSinc",
    "AntsApplyTransformsGaussian",
    "AntsApplyTransformsGenericAffineTransformOutput",
    "AntsApplyTransformsGenericAffineTransformOutputOutputs",
    "AntsApplyTransformsGenericLabel",
    "AntsApplyTransformsHammingWindowedSinc",
    "AntsApplyTransformsLanczosWindowedSinc",
    "AntsApplyTransformsLinear",
    "AntsApplyTransformsMultiLabel",
    "AntsApplyTransformsNearestNeighbor",
    "AntsApplyTransformsOutputs",
    "AntsApplyTransformsTransformFileName",
    "AntsApplyTransformsUseInverse",
    "AntsApplyTransformsWarpedOutput",
    "AntsApplyTransformsWarpedOutputOutputs",
    "AntsApplyTransformsWelchWindowedSinc",
    "ants_apply_transforms",
]
