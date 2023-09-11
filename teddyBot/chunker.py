import tiktokvoice
SESSION = "3f54de0e52fefe022d7dc78a1bf36465"
tempfile = "temp.mp3"
import time
def split_text_into_chunks(text_input, max_chunk_size=150):
    """Splits the given text into chunks."""
    # Split the text into sentences
    text_input.replace("!", ".")
    text_input.replace("?", ".")
    sentences = text_input.split('. ')
    # Initialize variables
    chunks = []
    current_chunk = ''

    # Iterate through the sentences
    for sentence in sentences:
        sentence = sentence.strip()

        # Check if adding the sentence would exceed the maximum chunk size
        if len(current_chunk) + len(sentence) + 1 > max_chunk_size:

            # If yes, add the current chunk to the list of chunks
            chunks.append(current_chunk)

            # Reset the current chunk
            current_chunk = sentence
        else:

            # If no, append the sentence to the current chunk
            if current_chunk != '':
                current_chunk += '. '
            current_chunk += sentence

    # Append the last chunk to the list of chunks
    chunks.append(current_chunk)

    return chunks

def store_chunks_in_dictionary(text_input, max_chunk_size=180):
    """Stores the given text into chunks in a dictionary."""
    # Create a dictionary to store the chunks
    chunk_dict = {}

    # Get the list of chunks
    chunks = split_text_into_chunks(text_input, max_chunk_size)

    # Store the chunks in the dictionary
    for i, chunk in enumerate(chunks):
        chunk_dict[f'chunk_{i+1}'] = chunk

    return chunk_dict

def iterate_through_dictionary(chunk_dict):
    """Iterates through the given dictionary and prints its contents."""
    for key, value in chunk_dict.items():
        print(f'{key}: {value}')
        tiktokvoice.tts(SESSION, "en_female_emotional", f'{value}', "temp.mp3", True)

def chunkerton(input):
    """Processes the given input string into chunks."""
    # Call the store_chunks_in_dictionary() function
    print(input)
    chunk_dict = store_chunks_in_dictionary(input)

    # Call the iterate_through_dictionary() function
    iterate_through_dictionary(chunk_dict)

#Test the function with sample input
#sample_input = "LORA SDXL 1.0 ULTIMATE TRAINING. USE YOUR OWN IMAGES WITHOUT ANY LIMIT. THERE IT IS. I WORKED LIKE A MADMAN FOR THIS VIDEO. 100s of HOURS OF TESTING. 100+$ SPEND ON CLOUD COMPUTING TRAINING JUST TO BRING YOU THE BEST VIDEO ON LORA TRAINING EVER MADE.  This is by far the most complex video I have EVER made on my channel, this took so many hours of work I almost went INSANE. I share EVERYTHING you need to know to train the best LORA possible and DEBUNK ALL THE MISTAKES you see online (99% of people are doing it wrong and it's not clickbait...). So please share this video as much as possible with the community because the more people know about this, the better models we will have in the future. So...enjoy."
#chunkerton(sample_input)