"""
mymathjeju_structure.py - mymathjeju.py 구조 및 머메이드(Mermaid) 다이어그램 모듈

이 파일은 mymathjeju.py 스크립트의 클래스 스키마, @tool 정의, AgentExecutor 흐름 및
JSON 저장 프로세스를 시각화하는 머메이드 다이어그램 및 구조 정보를 제공합니다.
"""

import sys

# Windows 터미널 인코딩 설정
sys.stdout.reconfigure(encoding='utf-8')

MERMAID_DIAGRAM = """
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
"""


def display_structure():
    """mymathjeju.py 머메이드 다이어그램 및 구조 설명 출력"""
    print("==================================================")
    print(" 📊 mymathjeju.py 머메이드(Mermaid) 구조 다이어그램")
    print("==================================================")
    print(MERMAID_DIAGRAM)
    print("==================================================")
    print(" 📌 구성 요소 요약:")
    print(" 1. MathQuery (Pydantic): abs, round, sqrt, pow 및 사칙연산 처리")
    print(" 2. JejuQuery (Pydantic): weather, tourist_spot, food, tip 가이드 제공")
    print(" 3. math_tool & jeju_tool: AgentExecutor 등록 도구")
    print(" 4. save_to_jejumath_json: data2/jejumath.json 결과 자동 기록")
    print("==================================================\n")


if __name__ == "__main__":
    display_structure()
