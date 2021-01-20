import cv2
import os
import numpy as np

eigneface = cv2.face.EigenFaceRecognizer_create()
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()


def getImagemcomId():
    caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]
    # print(caminhos)
    faces = []
    ids = []

    for caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
        id = os.path.split(caminhoImagem)[-1].split('.')[1]
        # print(id)
        ids.append(id)
        faces.append(imagemFace)
        # cv2.imshow("face", imagemFace)
        # cv2.waitKey(100)
    return np.array(ids), faces

ids, faces = getImagemcomId()

print("Treinando")

eigneface.train(faces, ids)
eigneface.write('classificadorEigen.yml')

fisherface.train(faces, ids)
fisherface.write('classificadorFisher.yml')
lbph.train(faces, ids)
lbph.write('classificadorLBPH.yml')

print('Treinamento realizado')
