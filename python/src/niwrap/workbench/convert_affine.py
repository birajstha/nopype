# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CONVERT_AFFINE_METADATA = Metadata(
    id="a9ccb8a0ce7bc6a1aec93f8022476f82e29ed30a",
    name="convert-affine",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class ConvertAffineFromWorld:
    """
    input is a NIFTI 'world' affine
    """
    opt_inverse: bool = False
    """for files that use 'target to source' convention"""
    
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
        if self.opt_inverse:
            cargs.append("-inverse")
        return cargs


@dataclasses.dataclass
class ConvertAffineFromFlirt:
    """
    input is a flirt matrix
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
class ConvertAffineToWorld:
    """
    write output as a NIFTI 'world' affine
    """
    opt_inverse: bool = False
    """write file using 'target to source' convention"""
    
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
        if self.opt_inverse:
            cargs.append("-inverse")
        return cargs


@dataclasses.dataclass
class ConvertAffineToFlirt:
    """
    write output as a flirt matrix
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


class ConvertAffineOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_affine(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def convert_affine(
    from_world: ConvertAffineFromWorld | None = None,
    opt_from_itk_input: str | None = None,
    from_flirt: ConvertAffineFromFlirt | None = None,
    to_world: ConvertAffineToWorld | None = None,
    opt_to_itk_output: str | None = None,
    to_flirt: list[ConvertAffineToFlirt] = None,
    runner: Runner = None,
) -> ConvertAffineOutputs:
    """
    convert-affine by Washington University School of Medicin.
    
    Convert an affine file between conventions.
    
    NIFTI world matrices can be used directly on mm coordinates via matrix
    multiplication, they use the NIFTI coordinate system, that is, positive X is
    right, positive Y is anterior, and positive Z is superior. Note that
    wb_command assumes that world matrices transform source coordinates to
    target coordinates, while other tools may use affines that transform target
    coordinates to source coordinates.
    
    The ITK format is used by ANTS.
    
    You must specify exactly one -from option, but you may specify multiple -to
    options, and -to-flirt may be specified more than once.
    
    Args:
        from_world: input is a NIFTI 'world' affine
        opt_from_itk_input: input is an ITK matrix: the input affine
        from_flirt: input is a flirt matrix
        to_world: write output as a NIFTI 'world' affine
        opt_to_itk_output: write output as an ITK affine: output - the output
            affine
        to_flirt: write output as a flirt matrix
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `ConvertAffineOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_AFFINE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-convert-affine")
    if from_world is not None:
        cargs.extend(["-from-world", *from_world.run(execution)])
    if opt_from_itk_input is not None:
        cargs.extend(["-from-itk", opt_from_itk_input])
    if from_flirt is not None:
        cargs.extend(["-from-flirt", *from_flirt.run(execution)])
    if to_world is not None:
        cargs.extend(["-to-world", *to_world.run(execution)])
    if opt_to_itk_output is not None:
        cargs.extend(["-to-itk", opt_to_itk_output])
    if to_flirt is not None:
        cargs.extend(["-to-flirt", *[a for c in [s.run(execution) for s in to_flirt] for a in c]])
    ret = ConvertAffineOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVERT_AFFINE_METADATA",
    "ConvertAffineFromFlirt",
    "ConvertAffineFromWorld",
    "ConvertAffineOutputs",
    "ConvertAffineToFlirt",
    "ConvertAffineToWorld",
    "convert_affine",
]
