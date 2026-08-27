# 🔰 [초보자 가이드] mymathjeju.py 구조 & 작동 원리 (Mermaid 다이어그램)

이 문서는 **LangChain AI 에이전트**로 작동하는 `mymathjeju.py` 프로그램이 **사용자의 질문을 판단하고 도구를 골라 답변하는 전체 과정**을 초보자도 한눈에 이해할 수 있도록 작성한 설명서입니다.

---

## 🖼️ 1. 구조 시각화 도표 (이미지 파일: images2/mymathjeju_diagram.png)

![mymathjeju_diagram](images2/mymathjeju_diagram.png)

---

## 💡 2. 한눈에 보는 프로그램 실행 과정 (Mermaid 다이어그램)

아래 다이어그램은 **사용자가 질문했을 때 AI가 판단하고 처리하는 순서(1단계~5단계)**를 나타냅니다.

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

---

## 🔍 3. 핵심 구성 요소 쉽게 이해하기

| 구성 요소 | 역할 및 비유 | 실제 코드 역할 예시 |
|---|---|---|
| 👤 **사용자 입력 (User Input)** | 손님이 AI 안내원에게 던지는 질문 | `"abs(2 - 17) 계산해줘"`<br/>`"제주 서귀포 맛집 알려줘"` |
| 🤖 **AI 두뇌 (AgentExecutor)** | 질문을 듣고 적절한 도구를 골라주는 **지능형 안내원** | `create_openai_tools_agent()` |
| 🧮 **수학 도구 (`math_tool`)** | 숫자를 계산해 주는 **전자 계산기** | `abs()`, `round()`, `sqrt()`, `pow()` 등 파이썬 연산 |
| 🏝️ **제주도 도구 (`jeju_tool`)** | 제주도 가이드 북을 들고 있는 **제주 전문 가이드** | 날씨, 성산일출봉, 흑돼지, 렌터카 팁 제공 |
| 💾 **저장소 (`jejumath.json`)** | 대화 내용과 처리 결과를 적어두는 **자동 메모장** | `data2/jejumath.json` 파일에 질문/답변 저장 |

---

## ⚙️ 4. 실제 질문으로 따라가는 작동 예시

### 💡 예시 A: "sqrt(16) 연산해줘" 질문을 했을 때
1. **질문 접수**: AI 두뇌가 `"sqrt(16)"`을 읽습니다.
2. **도구 선택**: "이 질문은 수학 연산이구나! 🧮 `math_tool`을 써야겠다!" 하고 판단합니다.
3. **도구 실행**: `math.sqrt(16)` 연산이 실행되어 `4.0` 결과를 만듭니다.
4. **최종 응답**: `"계산 결과 (sqrt): 4.0"`을 사용자에게 출력합니다.
5. **JSON 저장**: 질문과 답변을 `data2/jejumath.json`에 저장합니다.

### 💡 예시 B: "제주도 서귀포 특산물 및 맛집 알려줘" 질문을 했을 때
1. **질문 접수**: AI 두뇌가 `"제주도 서귀포 특산물 및 맛집"`을 읽습니다.
2. **도구 선택**: "이 질문은 제주도 정보구나! 🏝️ `jeju_tool`을 써야겠다!" 하고 판단합니다.
3. **도구 실행**: `category="food"`, `location="서귀포"` 인자로 `jeju_tool`을 호출합니다.
4. **최종 응답**: `"🍊 [서귀포] 추천 특산물 및 맛집: 흑돼지 구이, 제주 감귤/한라봉..."` 답변을 완성합니다.
5. **JSON 저장**: 질문과 처리 결과를 파일에 누적 기록합니다.

---

## 🚀 5. 실행 방법

```bash
# 1. 터미널에서 mymathjeju.py 실행
python mymathjeju.py

# 2. 콘솔에서 머메이드 구조 확인 실행
python mymathjeju_structure.py
```
