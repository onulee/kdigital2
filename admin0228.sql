-- 12c �����̻���� c##�κ��� �Է����� �ʾƵ� �ǵ��� ��. c##ora_user
alter session set "_ORACLE_SCRIPT"=true;
-- user ���
create user ora_user identified by 1234;
-- user db���ӱ���, �α��α���,table���� ���
grant connect, resource, dba to ora_user;
-- 12c ����, ���ڵ� insert������ ���� ����
alter user ora_user default tablespace users quata unlimited on users;










