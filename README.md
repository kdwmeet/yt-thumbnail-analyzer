# YouTube Thumbnail Analyzer (유튜브 썸네일 분석기)

## 1. 프로젝트 개요

YouTube Thumbnail Analyzer는 Vision AI 기술을 활용하여 유튜브 썸네일 이미지의 클릭률(CTR) 잠재력을 예측하고, 성과 개선을 위한 구체적인 컨설팅 리포트를 제공하는 솔루션입니다.

크리에이터 이코노미 시장에서 썸네일은 영상의 조회수를 결정짓는 가장 중요한 요소입니다. 본 프로젝트는 주관적인 감각에 의존하던 썸네일 제작 과정을 데이터와 AI 기반의 객관적인 분석으로 전환합니다. 핵심 엔진으로 OpenAI의 **gpt-5-mini** 모델(Vision 지원)을 채택하여 이미지 내의 텍스트 가독성, 인물의 표정, 시선 처리, 호기심 유발 요소 등을 정밀하게 분석합니다.

### 주요 기능
* **CTR 잠재력 스코어링:** 썸네일의 완성도를 0~100점 척도로 정량화하여 평가.
* **가독성 및 주목도 분석:** 텍스트의 폰트 크기, 배경과의 명도 대비, 핵심 피사체의 시선 집중도 분석.
* **SWOT 기반 상세 평가:** 썸네일의 강점(Strengths)과 약점(Weaknesses)을 명확하게 도출.
* **실행 가능한 개선 제안:** 클릭률을 높이기 위해 즉시 수정 가능한 구체적인 액션 아이템(Actionable Tips) 제공.

## 2. 시스템 아키텍처

본 시스템은 이미지 전처리, 멀티모달 AI 추론, 결과 데이터 시각화의 파이프라인으로 구성됩니다.

1.  **Image Preprocessing:** 사용자가 업로드한 이미지를 RGB 포맷으로 변환하고, API 전송 효율을 위해 JPEG 압축 및 Base64 인코딩을 수행.
2.  **Vision Inference:** 인코딩된 이미지 데이터를 **gpt-5-mini** 모델에 전송. 시스템 프롬프트에는 '유튜브 전략가' 페르소나와 평가 기준(가독성, 감정 전달, 어그로성 등)이 정의되어 있음.
3.  **Structured Output:** AI의 분석 결과를 JSON 포맷으로 강제하여 데이터의 일관성 확보.
4.  **Visualization:** 분석된 점수와 피드백을 Streamlit UI를 통해 직관적인 대시보드 형태로 시각화.

## 3. 기술 스택

* **Language:** Python 3.10 이상
* **AI Model:** OpenAI **gpt-5-mini** (Vision capabilities)
* **Web Framework:** Streamlit
* **Image Processing:** Pillow (PIL)
* **Configuration:** python-dotenv

## 4. 프로젝트 구조

설정, 유틸리티, 분석 로직을 분리하여 유지보수성을 높인 모듈형 구조입니다.

```text
yt-thumbnail-analyzer/
├── .env                  # 환경 변수 (API Key)
├── requirements.txt      # 의존성 패키지 목록
├── main.py               # 애플리케이션 진입점 및 대시보드 UI
└── app/                  # 백엔드 핵심 모듈
    ├── __init__.py
    ├── config.py         # 분석 기준 프롬프트 및 페르소나 설정
    ├── utils.py          # 이미지 전처리 및 인코딩 헬퍼 함수
    └── analyzer.py       # OpenAI API 통신 및 JSON 파싱 로직
```
## 5. 설치 및 실행 가이드
### 5.1. 사전 준비
Python 환경이 설치되어 있어야 합니다. 터미널에서 저장소를 복제하고 프로젝트 디렉토리로 이동하십시오.

```Bash
git clone [레포지토리 주소]
cd yt-thumbnail-analyzer
```
### 5.2. 의존성 설치
이미지 처리 및 웹 프레임워크 구동을 위한 라이브러리를 설치합니다.

```Bash
pip install -r requirements.txt
```
### 5.3. 환경 변수 설정
프로젝트 루트 경로에 .env 파일을 생성하고, 유효한 OpenAI API 키를 입력하십시오. 본 프로젝트는 Vision 기능을 지원하는 gpt-5-mini 모델 권한이 필요합니다.

```Ini, TOML
OPENAI_API_KEY=sk-your-api-key-here
```
### 5.4. 실행
Streamlit 애플리케이션을 실행합니다.

```Bash
streamlit run main.py
```
## 6. 출력 데이터 사양 (JSON Schema)
AI 모델은 분석 결과를 다음과 같은 JSON 구조로 반환합니다. 이를 통해 MCN 등 기업용 솔루션으로 확장 시 데이터베이스 적재가 용이합니다.

```JSON
{
  "total_score": 85,
  "summary": "인물의 놀란 표정이 시선을 사로잡지만, 텍스트 색상이 배경에 묻혀 가독성이 떨어집니다.",
  "strengths": [
    "인물의 표정 연기가 강렬하여 호기심을 자극함",
    "핵심 오브젝트(스마트폰)가 명확하게 보임"
  ],
  "weaknesses": [
    "노란색 배경에 흰색 글씨를 사용하여 가독성이 낮음",
    "우측 하단 여백이 낭비되고 있음"
  ],
  "actionable_tips": [
    "텍스트에 검은색 외곽선(Stroke)을 추가하여 대비를 높이세요.",
    "우측 하단에 화살표 아이콘을 추가하여 시선을 유도하세요."
  ]
}
```

## 7. 실행 화면
<img width="715" height="817" alt="스크린샷 2026-02-05 102026" src="https://github.com/user-attachments/assets/2ee44949-6323-4f7a-84d7-d1d813cd2e97" />

<img width="711" height="375" alt="스크린샷 2026-02-05 102032" src="https://github.com/user-attachments/assets/676a5069-d041-41fb-9aeb-86515467a434" />
