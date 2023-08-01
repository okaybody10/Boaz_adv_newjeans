from typing import Annotated
from fastapi import APIRouter, Request, Form, Depends, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from PIL import Image
import torch
from torchvision.transforms.functional import to_tensor
from sentence_transformers import SentenceTransformer

from model import model
from schemas import AwesomeForm

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Load the pretrained model
ckpt = "D:\\분석adv\\lightning_logs\\version_5\\checkpoints\\epoch=9-step=1000.ckpt"
our_model = model.MultimodalFakeNewsDetectionModel.load_from_checkpoint(ckpt, map_location='cpu')
our_model.eval()

# Load the text embedding model
text_embedder = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home.html", context)

@router.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, text_input=Form(...), image_upload=File(...)):
    print(f'text_input: {text_input}')
    content = await image_upload.read()
    print(f'image_upload: {content[:10]}')
    image_path = "D:\\분석adv\\web\\static\\temp.jpg"

    with open(image_path, "wb") as buffer:
        buffer.write(content)

    text = text_embedder.encode(text_input, convert_to_tensor=True).unsqueeze(0)

    image = Image.open(image_path).convert("RGB")
    image_tensor = to_tensor(image).unsqueeze(0)
    print(image_tensor.shape)

    with torch.no_grad():
        prediction, _ = our_model(text, image_tensor, torch.tensor([0]))
    
    # Extract the predicted label
    pred_label = torch.argmax(prediction, dim=1).item()
    result = "진짜뉴스입니다" if pred_label == 0 else "가짜뉴스입니다"
    context = {"request": request,
                "text_input": text_input,
                "image_path": "/static/temp.jpg",
                "result": result}
    return templates.TemplateResponse("home.html", context)
