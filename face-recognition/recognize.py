import argparse
import os
import cv2
import torch
import numpy as np
from facenet_pytorch import MTCNN, InceptionResnetV1


def load_known_faces(directory, mtcnn, resnet):
    embeddings = []
    names = []
    for person in os.listdir(directory):
        person_dir = os.path.join(directory, person)
        if not os.path.isdir(person_dir):
            continue
        for img_name in os.listdir(person_dir):
            img_path = os.path.join(person_dir, img_name)
            img = cv2.imread(img_path)
            if img is None:
                continue
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face = mtcnn(img)
            if face is None:
                continue
            with torch.no_grad():
                embedding = resnet(face.unsqueeze(0))
            embeddings.append(embedding.squeeze(0))
            names.append(person)
    if embeddings:
        embeddings = torch.stack(embeddings)
    else:
        embeddings = torch.empty((0, 512))
    return embeddings, names


def recognize(image_path, known_embeddings, names, mtcnn, resnet, threshold=0.8):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Could not read {image_path}")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face = mtcnn(img)
    if face is None:
        return "No face detected"
    with torch.no_grad():
        embedding = resnet(face.unsqueeze(0))
    if len(known_embeddings) == 0:
        return "Unknown"
    distances = torch.norm(known_embeddings - embedding, dim=1)
    min_dist, idx = torch.min(distances, dim=0)
    if min_dist < threshold:
        return names[idx]
    return "Unknown"


def main():
    parser = argparse.ArgumentParser(description="Simple face recognition using facenet-pytorch")
    parser.add_argument("--known_dir", required=True, help="Directory with subfolders of known individuals")
    parser.add_argument("--image", required=True, help="Path to image to recognize")
    parser.add_argument("--threshold", type=float, default=0.8, help="Distance threshold for recognition")
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    mtcnn = MTCNN(image_size=160, margin=20, device=device)
    resnet = InceptionResnetV1(pretrained="vggface2").eval().to(device)

    known_embeddings, names = load_known_faces(args.known_dir, mtcnn, resnet)
    result = recognize(args.image, known_embeddings, names, mtcnn, resnet, args.threshold)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
