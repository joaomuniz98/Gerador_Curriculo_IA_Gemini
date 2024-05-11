from flask import Blueprint, request, jsonify
import google.generativeai as genai
import json

GOOGLE_API_KEY = "AIzaSyDTMCf9u8-DoqlLAClmlTiSk5U2xZBmWA8"
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
}
safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}
model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)

controller = Blueprint('controller', __name__)

# Definindo uma rota para um método POST
@controller.route('/gerador', methods=['POST'])
def post_example():
    data = request.json
    data_json = json.dumps(data)
    prompt = f"Faça um curriculo com base nessas informações {data_json} , mais adicione mais informações além dessas para deixar o curriculo completo , retorne em apenas em tags html de marcação de texto  não coloque tags como <!DOCTYPE html> ,  "
    response = model.generate_content(prompt)
    print(response.text)
    return jsonify({'message': 'POST recebido com sucesso', 'data': response.text}), 200
