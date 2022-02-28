-- 12c 버전이상부터 c##부분을 입력하지 않아도 되도록 함. c##ora_user
alter session set "_ORACLE_SCRIPT"=true;
-- user 등록
create user ora_user identified by 1234;
-- user db접속권한, 로그인권한,table생성 등록
grant connect, resource, dba to ora_user;
-- 12c 변경, 레코드 insert까지의 권한 생성
alter user ora_user default tablespace users quata unlimited on users;










