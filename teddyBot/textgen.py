import requests

# For local streaming, the websockets are hosted without ssl - http://
HOST = 'localhost:5000'
URI = f'http://{HOST}/api/v1/generate'

# For reverse-proxied streaming, the remote will likely host with ssl - https://
# URI = 'https://your-uri-here.trycloudflare.com/api/v1/generate'


def run(prompt):
    #model_api({'action': 'load', 'model_name': 'llama-2-13b-chat.ggmlv3.q8_0.bin'})
    request = {
        'prompt': prompt,
        'max_new_tokens': 1000,
        'auto_max_new_tokens': False,
        'max_tokens_second': 0,
        #'history': history,
        'mode': 'chat',
        'context:': "Cupcake's persona: Cupcake is a loveable teddy bear with a loving mom named Morgan",


        # Generation params. If 'preset' is set to different than 'None', the values
        # in presets/preset-name.yaml are used instead of the individual numbers.
        'preset': 'default',
        'do_sample': True,
        'temperature': 0.7,
        'top_p': 0.1,
        'typical_p': 1,
        'epsilon_cutoff': 0,  # In units of 1e-4
        'eta_cutoff': 0,  # In units of 1e-4
        'tfs': 1,
        'top_a': 0,
        'repetition_penalty': 1.18,
        'repetition_penalty_range': 0,
        'top_k': 40,
        'min_length': 0,
        'no_repeat_ngram_size': 0,
        'num_beams': 1,
        'penalty_alpha': 0,
        'length_penalty': 1,
        'early_stopping': False,
        'mirostat_mode': 0,
        'mirostat_tau': 5,
        'mirostat_eta': 0.1,
        'guidance_scale': 1,
        'negative_prompt': '',

        'seed': -1,
        'add_bos_token': True,
        'truncation_length': 2048,
        'ban_eos_token': False,
        'skip_special_tokens': True,
        'stopping_strings': []
    }

    response = requests.post(URI, json=request)

    if response.status_code == 200:
        result = response.json()['results'][0]['text']
        return(result)
        #print(prompt + result)

def model_api(request):
    response = requests.post(f'http://{HOST}/api/v1/model', json=request)
    return response.json()

def model_load(model_name):
    return model_api({'action': 'load', 'model_name': model_name})

if __name__ == '__main__':
    prompt = "In order to make homemade bread, follow these steps:\n1)"
    run(prompt)