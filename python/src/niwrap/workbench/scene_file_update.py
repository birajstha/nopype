# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

SCENE_FILE_UPDATE_METADATA = Metadata(
    id="350ea82419dbec1ab7007f1e839a5c83290e55dc",
    name="scene-file-update",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class SceneFileUpdateCopyMapOnePalette:
    """
    Copy palettes settings from first map to all maps in a data file
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
class SceneFileUpdateDataFileAdd:
    """
    Add a data file to scene's loaded files
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
class SceneFileUpdateDataFileRemove:
    """
    Remove a data file from scene's loaded files
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


class SceneFileUpdateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `scene_file_update(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def scene_file_update(
    input_scene_file: str,
    output_scene_file: str,
    scene_name_or_number: str,
    opt_fix_map_palette_settings: bool = False,
    opt_remove_missing_files: bool = False,
    opt_error: bool = False,
    opt_verbose: bool = False,
    copy_map_one_palette: list[SceneFileUpdateCopyMapOnePalette] = None,
    data_file_add: list[SceneFileUpdateDataFileAdd] = None,
    data_file_remove: list[SceneFileUpdateDataFileRemove] = None,
    runner: Runner = None,
) -> SceneFileUpdateOutputs:
    """
    scene-file-update by Washington University School of Medicin.
    
    Update scene file.
    
    This command will update a scene for specific changes in data files.
    
    "-fix-map-palette-settings" will find all data files that have had a change
    in the number of maps since the scene scene was created. If the file has its
    "Apply to All Maps" property enabled, the palette setting in the first map
    is copied to all maps in the file. Note: This modifies the palette settings
    for the file in the scene (data file is NOT modified).
    
    "-copy-map-one-palette" will copy the palette settings from the first map to
    all other maps in a data file. This option is typically used when the number
    of maps in a data file changes. It changes the palette settings in the scene
    that are applied to the data file when the scene is loaded (the data file is
    not modified). The name of the data file specified on the command line is
    matched to the end of file names in the scene. This allows matching multiple
    files if their names end with the same characters. It also allows including
    a relative path when there is more than one file with the same name but in
    different paths and only one of the files to be updated.
    
    "-remove-missing-files" Any files that fail to load when the scene is read
    will be removed from the scene. Thus, if one deletes files prior to running
    with this option, the deleted files are removed from the scene.
    
    "-error" If this option is provided and there is an error while performing
    any of the scene operations, the command will immediately cease processing
    and the output scene file will not be created. Otherwise any errors will be
    listed after the command finishes.
    .
    
    Args:
        input_scene_file: the input scene file
        output_scene_file: the new scene file to create
        scene_name_or_number: name or number (starting at one) of the scene in
            the scene file
        opt_fix_map_palette_settings: Fix palette settings for files with change
            in number of maps
        opt_remove_missing_files: Remove missing files from SpecFile
        opt_error: Abort command if there is an error performing any of the
            operations on the scene file
        opt_verbose: Print names of files that have palettes updated
        copy_map_one_palette: Copy palettes settings from first map to all maps
            in a data file
        data_file_add: Add a data file to scene's loaded files
        data_file_remove: Remove a data file from scene's loaded files
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `SceneFileUpdateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SCENE_FILE_UPDATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-scene-file-update")
    cargs.append(input_scene_file)
    cargs.append(output_scene_file)
    cargs.append(scene_name_or_number)
    if opt_fix_map_palette_settings:
        cargs.append("-fix-map-palette-settings")
    if opt_remove_missing_files:
        cargs.append("-remove-missing-files")
    if opt_error:
        cargs.append("-error")
    if opt_verbose:
        cargs.append("-verbose")
    if copy_map_one_palette is not None:
        cargs.extend(["-copy-map-one-palette", *[a for c in [s.run(execution) for s in copy_map_one_palette] for a in c]])
    if data_file_add is not None:
        cargs.extend(["-data-file-add", *[a for c in [s.run(execution) for s in data_file_add] for a in c]])
    if data_file_remove is not None:
        cargs.extend(["-data-file-remove", *[a for c in [s.run(execution) for s in data_file_remove] for a in c]])
    ret = SceneFileUpdateOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SCENE_FILE_UPDATE_METADATA",
    "SceneFileUpdateCopyMapOnePalette",
    "SceneFileUpdateDataFileAdd",
    "SceneFileUpdateDataFileRemove",
    "SceneFileUpdateOutputs",
    "scene_file_update",
]
