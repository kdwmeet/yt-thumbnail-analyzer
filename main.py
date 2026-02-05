import streamlit as st
from PIL import Image
from app.analyzer import analyze_thumbnail

st.set_page_config(page_title="유튜브 썸네일 분석기", layout="centered")

# --- 헤더 --- 
st.title("유튜브 썸네일 분석기")
st.divider()

# --- 이미지 업로드 --- 
uploaded_file = st.file_uploader("분석할 썸네일 이미지를 올려주세요 (JPG, PNG)", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # 이미지 미리보기
    st.image(uploaded_file, caption="업로드된 썸네일", width="stretch")

    # --- 분석 버튼 --- 
    if st.button("썸네일 냉철하게 평가받기", type="primary", width="stretch"):
        with st.spinner("AI가 돋보기를 들고 분석중..."):
            result = analyze_thumbnail(uploaded_file)

            if "error" in result:
                st.error(result["error"])
            else:
                # 결과 파싱
                score = result.get("total_score", 0)
                summary = result.get("summary", "")
                strengths = result.get("strengths", [])
                weaknesses = result.get("weaknesses", [])
                tips = result.get("actionable_tips", [])

                st.divider()
                st.subheader("분석 리포트")

                # 점수 시각화 (색상으로 구분)
                score_color = "red"
                if score >= 80: score_color = "green"
                elif score >= 60: score_color = "orange"

                st.markdown(f"### 예상 클릭 성과 점수: :{score_color}[{score}점]")
                st.progress(score / 100, text=f"{score}% Potential")
                st.info(f"**총평:** {summary}")

                # 상세 분석 (2단 컬럼)
                col1, col2 = st.columns(2)
                with col1:
                    st.success("잘된 점 (Strengths)")
                    for item in strengths:
                        st.markdown(f"- {item}")
                with col2:
                    st.error("아쉬운 점 (Weaknesses)")
                    for item in weaknesses:
                        st.markdown(f"- {item}")
                
                # 개선 제안 
                st.markdown("### 클릭률을 위한 개선 팁")
                with st.container(border=True):
                    for tip in tips:
                        st.markdown(f"**{tip}**")

else:
    st.info("먼저 분석할 썸네일 이미지를 업로드해주세요.")