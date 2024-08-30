# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLVBM_3_PROC_METADATA = Metadata(
    id="48820f2eebc66c6451591595cc9dbdb604be9448",
    name="fslvbm_3_proc",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class Fslvbm3ProcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslvbm_3_proc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_directory: OutputPathType
    """Output data directory"""


def fslvbm_3_proc(
    arch: str | None = None,
    coprocessor: str | None = None,
    coprocessor_multi: str | None = None,
    coprocessor_class: str | None = None,
    coprocessor_class_strict: bool = False,
    coprocessor_toolkit: str | None = None,
    not_requeueable: bool = False,
    jobhold: str | None = None,
    array_hold: str | None = None,
    logdir: str | None = None,
    mailoptions: str | None = None,
    mailto: str | None = None,
    name: str | None = None,
    priority: str | None = None,
    queue_: str | None = None,
    resource_: str | None = None,
    delete_job: str | None = None,
    memory_gb: float | int | None = None,
    parallel_env_threads: str | None = None,
    array_task: str | None = None,
    array_native: str | None = None,
    number_jobscripts: float | int | None = None,
    keep_jobscript: bool = False,
    coprocessor_name: str | None = None,
    has_queues: bool = False,
    project: str | None = None,
    submit_scheduler: bool = False,
    runtime_limit: float | int | None = None,
    show_config: bool = False,
    verbose: bool = False,
    version: bool = False,
    config_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> Fslvbm3ProcOutputs:
    """
    fslvbm_3_proc by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Pipeline for voxel-based morphometry analysis using FSL tools.
    
    Args:
        arch: Specify architecture.
        coprocessor: Specify coprocessor.
        coprocessor_multi: Specify multiple coprocessors.
        coprocessor_class: Specify coprocessor class.
        coprocessor_class_strict: Use strict class matching for coprocessor.
        coprocessor_toolkit: Specify coprocessor toolkit.
        not_requeueable: Do not requeue the job.
        jobhold: Job to hold.
        array_hold: Array hold.
        logdir: Specify log directory.
        mailoptions: Specify mail options.
        mailto: Specify mail recipient.
        name: Job name.
        priority: Job priority.
        queue_: Queue to submit to.
        resource_: Resource identifier.
        delete_job: Delete specified job.
        memory_gb: Memory (GB).
        parallel_env_threads: Parallel environment and threads.
        array_task: Array task file.
        array_native: Array native specification.
        number_jobscripts: Keep number of job scripts.
        keep_jobscript: Keep job script.
        coprocessor_name: Specify coprocessor name.
        has_queues: Specify queues.
        project: Specify project name.
        submit_scheduler: Submit to Scheduler.
        runtime_limit: Specify runtime limit in minutes.
        show_config: Show configuration.
        verbose: Verbose output.
        version: Version information.
        config_file: Specify configuration file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Fslvbm3ProcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLVBM_3_PROC_METADATA)
    cargs = []
    cargs.append("fsl_sub")
    if arch is not None:
        cargs.extend(["-a", arch])
    if coprocessor is not None:
        cargs.extend(["-c", coprocessor])
    if coprocessor_multi is not None:
        cargs.extend(["--coprocessor_multi", coprocessor_multi])
    if coprocessor_class_strict:
        cargs.append("--coprocessor_class_strict")
    if coprocessor_toolkit is not None:
        cargs.extend(["--coprocessor_toolkit", coprocessor_toolkit])
    if jobhold is not None:
        cargs.extend(["-j", jobhold])
    if array_hold is not None:
        cargs.extend(["--array_hold", array_hold])
    if logdir is not None:
        cargs.extend(["-l", logdir])
    if mailoptions is not None:
        cargs.extend(["-m", mailoptions])
    if mailto is not None:
        cargs.extend(["-M", mailto])
    if name is not None:
        cargs.extend(["-N", name])
    if priority is not None:
        cargs.extend(["-p", priority])
    if queue_ is not None:
        cargs.extend(["-q", queue_])
    if resource_ is not None:
        cargs.extend(["-r", resource_])
    if delete_job is not None:
        cargs.extend(["--delete_job", delete_job])
    if memory_gb is not None:
        cargs.extend(["-R", str(memory_gb)])
    cargs.append("[PARALLELENV]")
    cargs.append("[THREADS]")
    if array_task is not None:
        cargs.extend(["-t", array_task])
    if array_native is not None:
        cargs.extend(["--array_native", array_native])
    if number_jobscripts is not None:
        cargs.extend(["-x", str(number_jobscripts)])
    if coprocessor_name is not None:
        cargs.extend(["--has_coprocessor", coprocessor_name])
    if project is not None:
        cargs.extend(["--project", project])
    if runtime_limit is not None:
        cargs.extend(["-T", str(runtime_limit)])
    if config_file is not None:
        cargs.extend(["-z", execution.input_file(config_file)])
    cargs.append("[COMMAND]")
    ret = Fslvbm3ProcOutputs(
        root=execution.output_file("."),
        output_directory=execution.output_file(f"fslvbm3a"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLVBM_3_PROC_METADATA",
    "Fslvbm3ProcOutputs",
    "fslvbm_3_proc",
]
