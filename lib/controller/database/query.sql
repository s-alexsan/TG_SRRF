CREATE TABLE IF NOT EXISTS TB_USER (
    ID          SERIAL  PRIMARY KEY,
    NAME        TEXT    NOT NULL,
    TELEFONE    TEXT    NOT NULL,
    CPF         TEXT    NOT NULL
);
INSERT INTO TB_USER(NAME, TELEFONE, CPF) VALUES('Alexsander da Silva', '(12)9 8809-9948', '477.227.529-29');
INSERT INTO TB_USER(NAME, TELEFONE, CPF) VALUES('Giuliana de Macedo Luz', '(12)9 8161-8360', '406.542.438-08');