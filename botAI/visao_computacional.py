import os
os.environ["TF_USE_LEGACY_KERAS"] = "1" 

from tf_keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

def classificar_imagem(caminho_arquivo):
    np.set_printoptions(suppress=True)
    modelo = load_model('keras_model.h5', compile=False)
    nomes_classes = open('labels.txt', 'r', encoding='utf-8').readlines()
    dados = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    imagem = Image.open(caminho_arquivo).convert('RGB')
    tamanho = (224, 224)
    
    # ALTERAÇÃO AQUI: Mudamos para o valor direto '3' (LANCZOS)
    imagem = ImageOps.fit(imagem, tamanho, 3)

    array_imagem = np.asarray(imagem)
    array_imagem_normalizada = (array_imagem.astype(np.float32) / 127.5) - 1
    dados[0] = array_imagem_normalizada
    previsao = modelo.predict(dados)

    indice = np.argmax(previsao)
    nome_classe = nomes_classes[indice]
    pontuaçao_confianca = previsao[0][indice]

    return nome_classe[2:].strip(), pontuaçao_confianca