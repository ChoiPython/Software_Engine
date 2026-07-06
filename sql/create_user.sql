-- (선택) 최초 1회, root 권한으로 실행
-- 이미 'soft'@'localhost' 계정이 존재한다면(예: 강의용으로 미리 세팅된 MySQL)
-- 이 파일은 실행할 필요 없이 바로 schema.sql로 넘어가면 됩니다.
--
-- 사용법:
--   mysql -u root -p < sql/create_user.sql

CREATE USER IF NOT EXISTS 'soft'@'localhost' IDENTIFIED BY '0000';
CREATE DATABASE IF NOT EXISTS Table_Order DEFAULT CHARACTER SET utf8mb4;
GRANT ALL PRIVILEGES ON Table_Order.* TO 'soft'@'localhost';
FLUSH PRIVILEGES;
