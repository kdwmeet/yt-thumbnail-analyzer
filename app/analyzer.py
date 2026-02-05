from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from app.config import MODEL_NAME, SYSTEM_PROMPT
from app.utils import encode_image

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_thumbnail(uploaded_file):
    """썸네일 이미지를 분석하여 평가 결과 JSON 반환"""
    base64_image = encode_image(uploaded_file)
    if not base64_image:
        return{"error": "이미지 처리 실패"}
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content":[
                    {"type": "text", "text": "이 썸네일의 클릭률 가능성을 분석해줘."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jped;base64,{base64_image}"}}
                ]}
            ],
            reasoning_effort="low",
            response_format={"type": "json_object"}
        )

        result_json = json.loads(response.choices[0].message.content)
        return result_json
    except Exception as e:
        return {"error": f"AI 분석 중 오류 발생: {str(e)}"}
