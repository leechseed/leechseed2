from mutagen.wave import WAVE
import os

def remove_metadata_from_wav(source_folder):
    """
    Removes metadata from all WAV files in the specified source folder and logs the process.
    """
    log_file = os.path.join(source_folder, "metadata_removal_log.txt")
    with open(log_file, "w") as log:
        for file in os.listdir(source_folder):
            if file.endswith('.wav'):
                wav_path = os.path.join(source_folder, file)

                try:
                    # Load the WAV file
                    audio = WAVE(wav_path)
                    # Clear all tags if they exist
                    if audio.tags is not None:
                        audio.tags.clear()
                        # Save the file
                        audio.save()
                    log.write(f"Removed metadata from '{file}'\n")
                    print(f"Removed metadata from '{file}'")
                except Exception as e:
                    error_message = f"Error processing {file}: {e}\n"
                    log.write(error_message)
                    print(error_message)

source_folder = r'C:\Users\U01_LEECHSEED\Downloads\Gawr Gura Voice Lines-1817-1-0-1664091061\SWATEli'
remove_metadata_from_wav(source_folder)
