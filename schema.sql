-- Table_Order 데모 DB 초기화 스크립트
-- 사용법 (관리자/root 계정으로 1회 실행):
--   mysql -u root -p < schema.sql
--
-- boundary/control 코드가 공통으로 사용하는 접속 정보(host=localhost, user=soft,
-- password=0000, db=Table_Order)에 맞춰 계정과 스키마를 생성합니다.

CREATE DATABASE IF NOT EXISTS Table_Order DEFAULT CHARACTER SET utf8mb4;

CREATE USER IF NOT EXISTS 'soft'@'localhost' IDENTIFIED BY '0000';
GRANT ALL PRIVILEGES ON Table_Order.* TO 'soft'@'localhost';
FLUSH PRIVILEGES;

USE Table_Order;
SET NAMES utf8mb4;

-- 메뉴 테이블
-- 주의: control/get_menu_control.py 등에서 `select *` 결과를 컬럼 순서(인덱스)로
-- 그대로 사용하므로 컬럼 순서를 바꾸면 안 됨: category, menu, image, price, menu_desc, soldout
CREATE TABLE IF NOT EXISTS menu (
    category  VARCHAR(50)  NOT NULL,
    menu      VARCHAR(100) NOT NULL PRIMARY KEY,
    image     VARCHAR(255) NOT NULL,
    price     INT          NOT NULL,
    menu_desc VARCHAR(255) NULL,
    soldout   TINYINT      NOT NULL DEFAULT 0
);

-- 옵션 테이블
-- 컬럼 순서 고정: menu, name, price, required(1=필수, 0=추가)
CREATE TABLE IF NOT EXISTS `option` (
    menu     VARCHAR(100) NOT NULL,
    name     VARCHAR(100) NOT NULL,
    price    INT          NOT NULL DEFAULT 0,
    required TINYINT      NOT NULL DEFAULT 0
);

-- 주문 목록 테이블 (딕셔너리 커서로 컬럼명 기준 조회하므로 id 추가 가능)
CREATE TABLE IF NOT EXISTS order_list (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    table_num INT          NOT NULL,
    menu_name VARCHAR(100) NOT NULL,
    image     VARCHAR(255) NULL,
    quantity  INT          NOT NULL DEFAULT 1,
    opt       VARCHAR(255) NULL,
    price     INT          NOT NULL
);

-- 데모용 샘플 메뉴 (이미지는 저장소의 assets/ 폴더 기준 상대 경로)
INSERT INTO menu (category, menu, image, price, menu_desc, soldout) VALUES
    ('1.메인메뉴', '닭꼬치', 'assets/test.jpg', 1300, '매콤달콤한 닭꼬치', 0),
    ('1.메인메뉴', '양꼬치', 'assets/기본이미지.jpg', 1500, '맛있는 양꼬치', 0),
    ('2.사이드', '감자튀김', 'assets/test2.jpg', 2500, '바삭한 감자튀김', 0),
    ('3.음료', '콜라', 'assets/기본이미지.jpg', 1000, '시원한 탄산음료', 0);

-- 데모용 샘플 옵션
INSERT INTO `option` (menu, name, price, required) VALUES
    ('닭꼬치', '매운맛', 0, 1),
    ('닭꼬치', '순한맛', 0, 1),
    ('닭꼬치', '치즈 추가', 500, 0),
    ('양꼬치', '기본', 0, 1),
    ('감자튀김', '케찹 추가', 0, 0),
    ('콜라', '얼음 많이', 0, 0);
