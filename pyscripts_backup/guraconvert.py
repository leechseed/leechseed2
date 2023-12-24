from pydub import AudioSegment
import os

def convert_to_standard_wav(source_folder, target_folder):
    """
    Reads WAV files from the source folder and re-exports them as standard WAV files to the target folder.
    """
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for file in os.listdir(source_folder):
        if file.endswith('.wav'):
            source_path = os.path.join(source_folder, file)
            target_path = os.path.join(target_folder, file)

            try:
                # Load the audio file
                audio = AudioSegment.from_wav(source_path)
                # Export it as a standard WAV
                audio.export(target_path, format='wav')
                print(f"Re-exported '{file}' as standard WAV")
            except Exception as e:
                print(f"Error processing {file}: {e}")

# Define the source and target folders
source_folder = r'C:\Users\U01_LEECHSEED\Downloads\Gawr Gura Voice Lines-1817-1-0-1664091061\SWATEli'
target_folder = r'C:\Users\U01_LEECHSEED\Downloads\Gawr Gura Voice Lines-1817-1-0-1664091061\SWATEli\StandardWAVs'

convert_to_standard_wav(source_folder, target_folder)
