import base64
from PIL import Image
from io import BytesIO

def encode_image(uploaded_file):
    """Streamlit 업로드 파일을 Base64 문자열로 변환"""
    try:
        image = Image.open(uploaded_file)
        # RGBA(투명 배경) -> RGB 변환
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
            
        buffered = BytesIO()
        # 용량 최적화를 위해 JPEG로 저장
        image.save(buffered, format="JPEG", quality=85)
        return base64.b64encode(buffered.getvalue()).decode("utf-8")
    except Exception as e:
        print(f"이미지 인코딩 오류: {e}")
        return None