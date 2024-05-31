# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

METRIC_MERGE_METADATA = Metadata(
    id="5bc421b9cea4f41b3f8fcebe2bc55ffc9759944f",
    name="metric-merge",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class MetricMergeUpTo:
    """
    use an inclusive range of columns
    """
    opt_reverse: bool = False
    """use the range in reverse order"""
    
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
        if self.opt_reverse:
            cargs.append("-reverse")
        return cargs


@dataclasses.dataclass
class MetricMergeColumn:
    """
    select a single column to use
    """
    up_to: MetricMergeUpTo | None = None
    """use an inclusive range of columns"""
    
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
        if self.up_to is not None:
            cargs.extend(["-up-to", *self.up_to.run(execution)])
        return cargs


@dataclasses.dataclass
class MetricMergeMetric:
    """
    specify an input metric
    """
    column: list[MetricMergeColumn] = None
    """select a single column to use"""
    
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
        if self.column is not None:
            cargs.extend(["-column", *[a for c in [s.run(execution) for s in self.column] for a in c]])
        return cargs


class MetricMergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_merge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_merge(
    metric_out: InputPathType,
    metric: list[MetricMergeMetric] = None,
    runner: Runner = None,
) -> MetricMergeOutputs:
    """
    metric-merge by Washington University School of Medicin.
    
    Merge metric files into a new file.
    
    Takes one or more metric files and constructs a new metric file by
    concatenating columns from them. The input metric files must have the same
    number of vertices and same structure.
    
    Example: wb_command -metric-merge out.func.gii -metric first.func.gii
    -column 1 -metric second.func.gii
    
    This example would take the first column from first.func.gii, followed by
    all columns from second.func.gii, and write these columns to out.func.gii.
    
    Args:
        metric_out: the output metric
        metric: specify an input metric
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MetricMergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_MERGE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-merge")
    cargs.append(execution.input_file(metric_out))
    if metric is not None:
        cargs.extend(["-metric", *[a for c in [s.run(execution) for s in metric] for a in c]])
    ret = MetricMergeOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{pathlib.Path(metric_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_MERGE_METADATA",
    "MetricMergeColumn",
    "MetricMergeMetric",
    "MetricMergeOutputs",
    "MetricMergeUpTo",
    "metric_merge",
]
