import bpy
from pathlib import Path

scene = bpy.context.scene
path = Path(scene.render.filepath)
suffix = ".tif"

# Specific file types to handle first
first_file_types = ["Beauty", "Denoised Beauty"]
# All file types including the first ones to handle
all_file_types = ["Beauty", "Alpha", "AO", "Denoised Beauty", "Mat ID", "Obj ID", "Mist", "Shadow Catcher"]

# Tracking dictionaries to keep track of the first occurrence
first_occurrences = {file_type: False for file_type in all_file_types}

object = bpy.context.active_object

# Rename "Beauty" and "Denoised Beauty" first
for file_type in first_file_types:
    for index in range(len(object.material_slots)):
        src_string = file_type + format(index, "04d") + suffix
        src = path / src_string

        # Check if the file exists before attempting to rename
        if src.exists():
            if not first_occurrences[file_type]:
                dst_string = file_type + object.material_slots[index].material.name + suffix
                dst = path / dst_string

                print(f"Renaming {str(src)} to {str(dst)}")
                src.rename(dst)

                # Mark this type as having its first occurrence handled
                first_occurrences[file_type] = True
            else:
                # If this is not the first occurrence, delete the file
                print(f"Deleting {str(src)} as {file_type} has already been renamed.")
                src.unlink()

# Now check and handle the rest
for file_type in all_file_types:
    if file_type not in first_file_types:  # Skip the ones already handled
        for index in range(len(object.material_slots)):
            src_string = file_type + format(index, "04d") + suffix
            src = path / src_string

            # Check if the file exists before attempting to rename
            if src.exists():
                if not first_occurrences[file_type]:
                    dst_string = file_type + object.material_slots[index].material.name + suffix
                    dst = path / dst_string

                    print(f"Renaming {str(src)} to {str(dst)}")
                    src.rename(dst)

                    # Mark this type as having its first occurrence handled
                    first_occurrences[file_type] = True
                else:
                    # If this is not the first occurrence, delete the file
                    print(f"Deleting {str(src)} as {file_type} has already been renamed.")
                    src.unlink()
