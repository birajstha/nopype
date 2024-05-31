# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_CHANGE_MAPPING_METADATA = Metadata(
    id="00393caf40496070f6d614f8e1188b2104b58857",
    name="cifti-change-mapping",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiChangeMappingSeries:
    """
    set the mapping to series
    """
    opt_unit_unit: str | None = None
    """select unit for series (default SECOND): unit identifier"""
    
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
        if self.opt_unit_unit is not None:
            cargs.extend(["-unit", self.opt_unit_unit])
        return cargs


@dataclasses.dataclass
class CiftiChangeMappingFromCifti:
    """
    copy mapping from another cifti file
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


class CiftiChangeMappingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_change_mapping(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_change_mapping(
    data_cifti: InputPathType,
    direction: str,
    cifti_out: InputPathType,
    series: CiftiChangeMappingSeries | None = None,
    opt_scalar: bool = False,
    opt_name_file_file: str | None = None,
    from_cifti: CiftiChangeMappingFromCifti | None = None,
    runner: Runner = None,
) -> CiftiChangeMappingOutputs:
    """
    cifti-change-mapping by Washington University School of Medicin.
    
    Convert to scalar, copy mapping, etc.
    
    Take an existing cifti file and change one of the mappings. Exactly one of
    -series, -scalar, or -from-cifti must be specified. The direction can be
    either an integer starting from 1, or the strings 'ROW' or 'COLUMN'.
    
    The argument to -unit must be one of the following:
    
    SECOND
    HERTZ
    METER
    RADIAN.
    
    Args:
        data_cifti: the cifti file to use the data from
        direction: which direction on <data-cifti> to replace the mapping
        cifti_out: the output cifti file
        series: set the mapping to series
        opt_scalar: set the mapping to scalar
        opt_name_file_file: specify names for the maps: text file containing map
            names, one per line
        from_cifti: copy mapping from another cifti file
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiChangeMappingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CHANGE_MAPPING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-change-mapping")
    cargs.append(execution.input_file(data_cifti))
    cargs.append(direction)
    cargs.append(execution.input_file(cifti_out))
    if series is not None:
        cargs.extend(["-series", *series.run(execution)])
    if opt_scalar:
        cargs.append("-scalar")
    if opt_name_file_file is not None:
        cargs.extend(["-name-file", opt_name_file_file])
    if from_cifti is not None:
        cargs.extend(["-from-cifti", *from_cifti.run(execution)])
    ret = CiftiChangeMappingOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_CHANGE_MAPPING_METADATA",
    "CiftiChangeMappingFromCifti",
    "CiftiChangeMappingOutputs",
    "CiftiChangeMappingSeries",
    "cifti_change_mapping",
]
