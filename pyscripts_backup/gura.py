from pydub import AudioSegment
import os

def convert_wav_to_ogg(source_folder, target_folder):
    """
    Converts all WAV files in the source folder to OGG format and saves them in the target folder.
    """
    # Check if target folder exists, create if it doesn't
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for file in os.listdir(source_folder):
        if file.endswith('.wav'):
            wav_path = os.path.join(source_folder, file)
            ogg_path = os.path.join(target_folder, file.replace('.wav', '.ogg'))

            try:
                # Convert WAV to OGG
                audio = AudioSegment.from_wav(wav_path)
                audio.export(ogg_path, format='ogg')
                print(f"Converted '{file}' to OGG format")
            except Exception as e:
                print(f"Error converting {file}: {e}")

source_folder = r'C:\Users\U01_LEECHSEED\Downloads\Gawr Gura Voice Lines-1817-1-0-1664091061\SWATEli'
target_folder = r'C:\Users\U01_LEECHSEED\Downloads\Gawr Gura Voice Lines-1817-1-0-1664091061\SWATEli\gura ogg SWATKing'

convert_wav_to_ogg(source_folder, target_folder)
