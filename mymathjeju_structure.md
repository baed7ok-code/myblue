# mymathjeju.py 아키텍처 및 머메이드(Mermaid) 구조 문서

이 문서는 [mymathjeju.py](file:///c:/workAI/2%EC%B0%A8%EC%88%98%EC%97%85/work9langchain/mymathjeju.py) 파일의 내부 클래스 스키마, `@tool` 등록 도구, `AgentExecutor` 에이전트 실행 및 결과 JSON 저장 프로세스를 정리한 구조 문서입니다.

---

## 📊 1. 머메이드(Mermaid) 구조 다이어그램

```mermaid
graph TD
    %% 스타일 정의
    classDef user fill:#EBF5FB,stroke:#2980B9,stroke-width:2px,color:#2C3E50;
    classDef agent fill:#FEF9E7,stroke:#F39C12,stroke-width:2px,color:#7D6608;
    classDef tool fill:#E8F8F5,stroke:#1ABC9C,stroke-width:2px,color:#117864;
    classDef storage fill:#F4ECF7,stroke:#8E44AD,stroke-width:2px,color:#512E5F;

    %% 메인 구성 요소를 나타내는 노드
    User["👤 User Input<br/>(사용자 질문)"]:::user
    AgentExec["🤖 AgentExecutor<br/>(ChatOpenAI / OpenRouter API)"]:::agent
    
    %% @tool 서브그래프
    subgraph Tools ["🛠️ Registered Tools (@tool)"]
        MathTool["🧮 math_tool<br/>(MathQuery Schema)"]:::tool
        JejuTool["🏝️ jeju_tool<br/>(JejuQuery Schema)"]:::tool
    end

    %% 내부 계산 및 정보 데이터 로직
    subgraph MathLogic ["PyMath Engine"]
        MathFuncs["abs, round, sqrt, pow<br/>+ add, subtract, multiply, divide"]
    end

    subgraph JejuLogic ["Jeju Info Engine"]
        JejuInfo["weather, tourist_spot,<br/>food, tip"]
    end

    %% 저장소 노드
    JSONStorage[("💾 data2/jejumath.json<br/>(결과 저장)")]:::storage

    %% 워크플로우 연결 관계
    User -->|1. 질문 입력| AgentExec
    AgentExec -->|2. 의도 파악 후 툴 호출| MathTool
    AgentExec -->|2. 의도 파악 후 툴 호출| JejuTool
    
    MathTool -->|3. 파이썬/math 연산| MathFuncs
    JejuTool -->|3. 제주 가이드 생성| JejuInfo
    
    MathFuncs -->|4. 계산 결과 반환| AgentExec
    JejuInfo -->|4. 정보 결과 반환| AgentExec
    
    AgentExec -->|5. 최종 답변 응답| User
    AgentExec -->|6. save_to_jejumath_json()| JSONStorage
```

---

## 📌 2. 핵심 컴포넌트 상세

1. **`MathQuery (BaseModel)`**:
   - 파이썬 내장 함수(`abs`, `round`) 및 `math` 모듈 함수(`sqrt`, `pow`), 사칙연산(`add`, `subtract`, `multiply`, `divide`)의 인자 검증 및 계산 로직 포함.
2. **`JejuQuery (BaseModel)`**:
   - 제주도의 날씨(`weather`), 관광지(`tourist_spot`), 맛집/특산물(`food`), 여행 팁(`tip`) 카테고리별 맞춤 정보 반환.
3. **`math_tool` & `jeju_tool`**:
   - `@tool(args_schema=...)` 데코레이터를 적용하여 LangChain `AgentExecutor`가 자율 선택할 수 있도록 바인딩된 툴.
4. **`save_to_jejumath_json`**:
   - 질문 처리 후 최종 응답 및 intermediate_steps(도구 실행 로그)를 `data2/jejumath.json` 파일에 JSON 포맷으로 누적 기록.

---

## 🚀 3. 실행 방법

```bash
# .venv 가상환경 활성화 후 실행
python mymathjeju.py

# 구조 다이어그램 출력 실행
python mymathjeju_structure.py
```
