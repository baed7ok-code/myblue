"""
mymathjeju_structure.py - mymathjeju.py 초보자용 머메이드(Mermaid) 구조도 모듈

이 모듈은 초보자도 쉽게 이해할 수 있도록 mymathjeju.py의 AI 판단 흐름,
수학 도구(math_tool), 제주도 도구(jeju_tool) 선택 및 결과 저장 구조를 시각화합니다.
"""

import sys

# Windows 터미널 출력 인코딩 설정
sys.stdout.reconfigure(encoding='utf-8')

MERMAID_DIAGRAM = """
```mermaid
flowchart TD
    %% ----------------------------------------------------
    %% 스타일 색상 정의 (초보자를 위한 직관적 색상)
    %% ----------------------------------------------------
    classDef startStyle fill:#E1F5FE,stroke:#0288D1,stroke-width:2px,color:#01579B;
    classDef brainStyle fill:#FFF9C4,stroke:#FBC02D,stroke-width:2px,color:#F57F17;
    classDef branchStyle fill:#E8F5E9,stroke:#388E3C,stroke-width:2px,color:#1B5E20;
    classDef mathToolStyle fill:#E0F2F1,stroke:#00897B,stroke-width:2px,color:#004D40;
    classDef jejuToolStyle fill:#F3E5F5,stroke:#8E24AA,stroke-width:2px,color:#4A148C;
    classDef saveStyle fill:#FFEBEE,stroke:#E53935,stroke-width:2px,color:#B71C1C;

    %% ----------------------------------------------------
    %% 1단계: 사용자 질문 입력
    %% ----------------------------------------------------
    USER["👤 1단계: 사용자 질문 입력<br/>예: '제주 맛집 알려줘' OR 'sqrt(16) 계산해줘'"]:::startStyle

    %% ----------------------------------------------------
    %% 2단계: AI 에이전트 (생각하고 판단하는 두뇌)
    %% ----------------------------------------------------
    AI["🤖 2단계: AI 두뇌 (AgentExecutor)<br/>질문의 의도를 분석하여 어떤 도구를 쓸지 판단"]:::brainStyle

    %% ----------------------------------------------------
    %% 3단계: 도구 분기 선택
    %% ----------------------------------------------------
    CHECK{"❓ 3단계: 어떤 도구가 필요할까?"}:::branchStyle

    %% ----------------------------------------------------
    %% 4단계: 전용 도구 실행
    %% ----------------------------------------------------
    subgraph TOOLS ["🛠️ 도구함 (Tools)"]
        TOOL_MATH["🧮 수학 도구 (math_tool)<br/>- 사칙연산 (+, -, *, /)<br/>- 수학함수 (abs, round, sqrt, pow)"]:::mathToolStyle
        TOOL_JEJU["🏝️ 제주도 도구 (jeju_tool)<br/>- 날씨 정보 (weather)<br/>- 관광지 추천 (tourist_spot)<br/>- 맛집/특산물 (food)<br/>- 여행 팁 (tip)"]:::jejuToolStyle
    end

    %% ----------------------------------------------------
    %% 5단계: 결과 출력 및 자동 저장
    %% ----------------------------------------------------
    RESULT["💬 4단계: 최종 답변 완성<br/>사용자에게 친절한 답변 출력"]:::startStyle
    SAVE[("💾 5단계: 기록 저장<br/>data2/jejumath.json 파일에 자동 기록")]:::saveStyle

    %% ----------------------------------------------------
    %% 데이터 흐름 (화살표 연결)
    %% ----------------------------------------------------
    USER --> AI
    AI --> CHECK
    
    CHECK -->|수학 연산 질문일 때| TOOL_MATH
    CHECK -->|제주도 관련 질문일 때| TOOL_JEJU

    TOOL_MATH -->|계산 완료| RESULT
    TOOL_JEJU -->|정보 조회 완료| RESULT

    RESULT --> SAVE
```
"""


def display_structure():
    """mymathjeju.py 초보자용 머메이드 다이어그램 및 구조 설명 출력"""
    print("==================================================")
    print(" 🔰 [초보자 가이드] mymathjeju.py 머메이드 구조도")
    print("==================================================")
    print(MERMAID_DIAGRAM)
    print("==================================================")
    print(" 📌 핵심 작동 원리 요약:")
    print(" 1. 👤 질문 입력 ➔ AI 가 질문 의도를 파악합니다.")
    print(" 2. 🤖 AI 두뇌 (AgentExecutor) ➔ 도구(math_tool / jeju_tool)를 선택합니다.")
    print(" 3. 🛠️ 도구 실행 ➔ 수학 계산 연산 또는 제주 여행 정보 조회를 수행합니다.")
    print(" 4. 💬 답변 출력 ➔ 결과를 사용자에게 보여줍니다.")
    print(" 5. 💾 파일 저장 ➔ data2/jejumath.json 에 대화 기록을 보관합니다.")
    print("==================================================\n")


if __name__ == "__main__":
    display_structure()
