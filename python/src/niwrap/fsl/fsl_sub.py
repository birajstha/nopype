# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSL_SUB_METADATA = Metadata(
    id="4a2ab1677f50e399301d58366587c073197f8285",
    name="fsl_sub",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class FslSubOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_sub(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fsl_sub(
    arch: str | None = None,
    coprocessor: str | None = None,
    coprocessor_multi: float | int | None = None,
    coprocessor_class: str | None = None,
    coprocessor_class_strict: bool = False,
    coprocessor_toolkit: str | None = None,
    usescript: bool = False,
    jobhold: str | None = None,
    not_requeueable: bool = False,
    array_hold: str | None = None,
    logdir: str | None = None,
    mailoptions: str | None = None,
    mailto: str | None = "root@fe8ea96c3a1a",
    novalidation: bool = False,
    name: str | None = None,
    priority: str | None = None,
    queue_: str | None = None,
    resource_: str | None = None,
    delete_job: str | None = None,
    jobram: float | int | None = None,
    parallelenv_threads: str | None = None,
    array_task: str | None = None,
    array_native: str | None = None,
    array_limit: float | int | None = None,
    keep_jobscript: bool = False,
    project: str | None = None,
    noramsplit: bool = False,
    jobtime: float | int | None = None,
    has_coprocessor: str | None = None,
    has_queues: bool = False,
    show_config: bool = False,
    verbose: bool = False,
    version: bool = False,
    fileisimage: InputPathType | None = None,
    runner: Runner | None = None,
) -> FslSubOutputs:
    """
    fsl_sub by FMRIB (Oxford University).
    
    FSL cluster submission tool.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslSub
    
    Args:
        arch: Architectures not available.
        coprocessor: No co-processor configured - ignored.
        coprocessor_multi: No co-processor configured - ignored.
        coprocessor_class: No co-processor classes configured - ignored.
        coprocessor_class_strict: No co-processor classes configured - ignored.
        coprocessor_toolkit: No co-processor toolkits configured - ignored.
        usescript: Use flags embedded in scripts to set queuing options - not\
            supported.
        jobhold: Place a hold on this task until specified job id has\
            completed.
        not_requeueable: Job cannot be requeued in the event of a node failure.
        array_hold: Not supported - will be converted to simple job hold.
        logdir: Where to output logfiles.
        mailoptions: Email notification options (ignored).
        mailto: Email notification recipients (ignored).
        novalidation: Don't check for presence of script/binary in your\
            searchpath.
        name: Specify job name as it will appear on queue.
        priority: Specify job priority (not supported).
        queue_: Specify the queue for the job (irrelevant if not running in a\
            cluster environment).
        resource_: Pass a resource request or constraint string through to the\
            job scheduler.
        delete_job: Deletes a queued/running job.
        jobram: Max total RAM required for job (integer in GB).
        parallelenv_threads: No parallel environments configured.
        array_task: Specify a task file of commands to execute in parallel.
        array_native: Binary/Script will handle array task internally (mutually\
            exclusive with --array_task).
        array_limit: Specify the maximum number of parallel job sub-tasks to\
            run concurrently.
        keep_jobscript: Whether to create and save a job submission script.
        project: Specify the project (not relevant when not running in a\
            cluster environment).
        noramsplit: Disable RAM splitting (not relevant when not running in a\
            cluster environment).
        jobtime: Estimated job length in minutes, used to automatically choose\
            the queue name.
        has_coprocessor: fsl_sub returns with exit code of 0 if specified\
            coprocessor is configured.
        has_queues: fsl_sub returns with exit code of 0 if there's a compute\
            cluster with queues configured.
        show_config: Display the configuration currently in force.
        verbose: Verbose mode.
        version: Show program's version number and exit.
        fileisimage: If <file> already exists and is an MRI image file, do\
            nothing and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslSubOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_SUB_METADATA)
    cargs = []
    cargs.append("fsl_sub")
    cargs.append("[OPTIONS]")
    ret = FslSubOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_SUB_METADATA",
    "FslSubOutputs",
    "fsl_sub",
]
