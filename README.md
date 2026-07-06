# 🍽️ 무인 주문 키오스크 시스템 (Table Order Kiosk)

**소프트웨어공학 팀 프로젝트 — BCE(Boundary-Control-Entity) 아키텍처 기반 매장 주문 관리 시스템**

<br>

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Tkinter-GUI-4B8BBE?style=for-the-badge">
<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
<img src="https://img.shields.io/badge/Pillow-image_processing-306998?style=for-the-badge">

---

## 📌 Project Overview

매장에서 흔히 볼 수 있는 **무인 주문 키오스크**를 소프트웨어공학 수업에서 배운 **BCE(Boundary-Control-Entity) 설계 패턴**에 따라 구현한 팀 프로젝트입니다. 고객용 주문 화면과 관리자용 메뉴/옵션 관리 화면을 분리하여, 실제 매장 운영 흐름(주문 → 장바구니 → 결제 요청 / 메뉴 등록·수정·삭제)을 GUI로 구현했습니다.

## ⚙️ Technology Stack

| 분류 | 기술 | 역할 |
|---|---|---|
| GUI | Python Tkinter | 고객/관리자 화면 렌더링 및 이벤트 처리 |
| Image | Pillow (PIL) | 메뉴 이미지, 장바구니 썸네일 처리 |
| Database | MySQL (PyMySQL / mysql-connector) | 메뉴, 옵션, 주문 데이터 CRUD |
| Design | BCE Pattern | 화면(Boundary)과 로직(Control)의 책임 분리 |

## 🏗️ Architecture — BCE Pattern

```
boundary/                         control/
─────────────────────            ─────────────────────
user_main_boundary           ──▶  get_menu_control
choiced_menu_boundary        ──▶  choiced_menu_control
cart_boundary                 ──▶  order_control
menu_add_boundary             ──▶  menu_add_control
menu_adj_boundary/main        ──▶  menu_adj_control
menu_del_boundary             ──▶  menu_del_control
administer_main_boundary
user_order_rist_boundary
```

- **Boundary**: 사용자가 직접 보고 조작하는 화면(Tkinter 위젯 구성, 버튼 이벤트)
- **Control**: 화면 뒤에서 MySQL과 통신하며 실제 데이터 처리(조회/삽입/수정/삭제)를 담당

## 🚀 Key Features

**고객(User) 화면**
- 카테고리별 메뉴 조회 (스크롤 가능한 그리드 레이아웃)
- 메뉴 담기 → 옵션 선택 → 장바구니 반영
- 장바구니 확인/수정, 주문 목록 조회, 결제 요청

**관리자(Administer) 화면**
- 메뉴 등록 / 수정 / 삭제
- 옵션 등록 및 관리

**공통**
- MySQL 연동으로 메뉴·옵션·주문 데이터 실시간 반영

## 🙋 My Role (본인 담당)

팀 프로젝트 전체 217커밋 중 **72커밋으로 최다 기여**했으며, 아래 영역을 주로 담당했습니다.

- `boundary/user_main_boundary.py` — 고객용 메인 화면(카테고리 탐색, 메뉴 렌더링, 장바구니 진입점) 설계 및 구현
- `boundary/cart_boundary.py` — 장바구니 UI 및 항목별 수량/옵션 관리
- `boundary/administer_main_boundary.py` — 관리자 메인 화면 구성
- `boundary/menu_del_boundary.py` / `control/menu_del_control.py` — 메뉴 삭제 기능 (Boundary + Control 양쪽 구현)
- `boundary/menu_adj_main_boundary.py`, `boundary/choiced_menu_boundary.py` — 메뉴 옵션 선택 및 조정 화면

## ▶️ 실행 방법

```bash
pip install -r requirements.txt

# MySQL에 menu / option / order_list 테이블 스키마 구성 필요 (DB명: Table_Order)

python main.py
```

## 📂 Directory Structure

```
Software_Engine/
├── main.py                              # 프로그램 진입점 (User_main 실행)
├── requirements.txt
├── assets/                              # 메뉴/기본 이미지 리소스
│   ├── test.jpg
│   ├── test2.jpg
│   └── 기본이미지.jpg
├── boundary/                            # 화면(UI) 계층
│   ├── user_main_boundary.py            # 고객 메인 화면
│   ├── cart_boundary.py                 # 장바구니 화면
│   ├── choiced_menu_boundary.py         # 메뉴 옵션 선택 화면
│   ├── administer_main_boundary.py      # 관리자 메인 화면
│   ├── menu_add_boundary.py             # 메뉴 등록 화면
│   ├── menu_adj_boundary.py             # 메뉴 수정 화면
│   ├── menu_adj_main_boundary.py        # 메뉴 수정 목록 화면
│   ├── menu_del_boundary.py             # 메뉴 삭제 화면
│   ├── option_add_boundary.py           # 옵션 등록 화면
│   └── user_order_rist_boundary.py      # 주문 목록 화면
└── control/                             # 비즈니스 로직 / DB 접근 계층
    ├── get_menu_control.py              # 메뉴/옵션 조회 (DB)
    ├── choiced_menu_control.py          # 장바구니 담기 로직
    ├── menu_add_control.py              # 메뉴 등록 (DB)
    ├── menu_adj_control.py              # 메뉴 수정 (DB)
    ├── menu_del_control.py              # 메뉴 삭제 (DB)
    └── order_control.py                 # 주문 저장 (DB)
```

## 📝 Notes

본 프로젝트는 소프트웨어공학 수업의 팀 프로젝트로, 학습 목적의 데모 애플리케이션입니다. DB 접속 정보는 예시 값이며 실제 배포 환경에서는 별도의 환경변수 처리가 필요합니다.
