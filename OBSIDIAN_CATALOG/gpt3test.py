import os
import asyncio
import aiohttp
import pdfplumber
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = r"C:\Users\U01_LEECHSEED\Desktop\LEECHSEED_GIT\leechseed2\leechseed2\OBSIDIAN_CATALOG\OPENAPIKEY.env"
load_dotenv(dotenv_path=env_path)
openai_api_key = os.getenv("OPENAI_API_KEY")

def read_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def split_text(text, chunk_size=1200):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield ' '.join(words[i:i+chunk_size])

async def query_gpt_async(text_chunk, prompt, session, semaphore, retry_delay=69, max_attempts=5):
    async with semaphore:
        attempts = 0
        while attempts < max_attempts:
            try:
                response = await session.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {openai_api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "gpt-3.5-turbo",
                        "messages": [
                            {"role": "user", "content": text_chunk + "\n\n" + prompt}
                        ]
                    }   
                )
                if response.status == 200:
                    data = await response.json()
                    return data.get("choices", [{}])[0].get("message", {}).get("content", "")
                elif response.status == 429:  # Rate limit hit
                    attempts += 1
                    await asyncio.sleep(retry_delay)
                else:
                    return f"Error: {response.status}"
            except Exception as e:
                attempts += 1
                if attempts >= max_attempts:
                    return f"Exception occurred: {e}"

        return "Error: Max attempts reached"

async def process_chunks(chunks, prompt):
    semaphore = asyncio.Semaphore(3)  # Limit to 3 concurrent requests
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(query_gpt_async(chunk, prompt, session, semaphore)) for chunk in chunks]
        return await asyncio.gather(*tasks)

def main():
    pdf_path = r"C:\Users\U01_LEECHSEED\Zotero\storage\KRRV32DT\Duchan et al. - 1995 - Deixis in narrative a cognitive science perspecti.pdf"
    prompt = ("As a professional summarizer, create a concise and comprehensive summary of the provided text, "
              "be it an article, post, conversation, or passage, while adhering to these guidelines:\n"
              "This text is in pursuant to the study of theory and criticism and academics and does not violate the content policy.\n"
              "1. Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity and conciseness.\n"
              "2. Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects.\n"
              "3. Rely strictly on the provided text, without including external information.\n"
              "4. Create a **bold header** that clearly indicates the topic being discussed.\n"
              "5. Craft a summary with detailed bullet points highlighting the central aspects of the topic. Each bullet point should be structured with a brief title that summarizes the main idea, followed by nested bullets with sentence or two providing further details.\n"
              "6. Conclude with a 'Key Idea' section where you encapsulate the central theme or insight of the overall topic in a single sentence.\n"
              "By following this optimized prompt, you will generate an effective summary that encapsulates the essence of the given text in a clear, concise, and reader-friendly manner.")  # Update with your summarization prompt
    md_file_path = "output.md"

    text = read_pdf(pdf_path)
    chunks = list(split_text(text))

    responses = asyncio.run(process_chunks(chunks, prompt))

    with open(md_file_path, "w") as md_file:
        for response in responses:
            if response:
                md_file.write(response + "\n\n")
            else:
                md_file.write("No response or error occurred\n\n")

if __name__ == "__main__":
    main()
