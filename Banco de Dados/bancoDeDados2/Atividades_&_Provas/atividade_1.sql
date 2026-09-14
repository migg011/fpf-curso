-- Com base na modelagem apresentada, desenvolva os scripts SQL para criação completa do banco
-- de dados, incluindo tabelas, chaves primárias, chaves estrangeiras e demais restrições de
-- integridade. Além disso, gere scripts de inserção de dados (INSERT INTO) para todas as tabelas,
-- contendo registros de exemplo que permitam validar os relacionamentos e o funcionamento da base
-- de dados.

CREATE DATABASE bugtracker;
USE bugtracker;

CREATE TABLE Applications (
AppID INT AUTO_INCREMENT PRIMARY KEY,
AppName VARCHAR(256) NOT NULL,
AppVersion VARCHAR(256),
AppDesc VARCHAR(256)
);


CREATE TABLE Users (
    UserID INT AUTO_INCREMENT,
    UserName VARCHAR(80) NOT NULL,
    UserEmail VARCHAR(80) NOT NULL,
    UserTel VARCHAR(40),

    PRIMARY KEY (UserID),
    UNIQUE (UserName),
    UNIQUE (UserEmail)
);


CREATE TABLE CatCodes (
    CatCodeID INT AUTO_INCREMENT,
    CatCodeDesc VARCHAR(128) NOT NULL,

    PRIMARY KEY (CatCodeID)
);

CREATE TABLE Bugs (
    BugID INT AUTO_INCREMENT,

    AppID INT NOT NULL,
    UserID INT NOT NULL,
    BugSignOff INT NULL,

    BugDate DATE NOT NULL,

    BugDesc TEXT NOT NULL,
    BugDetails TEXT,
    RepSteps TEXT,

    FixDate DATE NULL,

    PRIMARY KEY (BugID),

    CONSTRAINT FK_Bugs_App
        FOREIGN KEY (AppID)
        REFERENCES Applications(AppID),

    CONSTRAINT FK_Bugs_User
        FOREIGN KEY (UserID)
        REFERENCES Users(UserID),

    CONSTRAINT FK_Bugs_SignOff
        FOREIGN KEY (BugSignOff)
        REFERENCES Users(UserID),

    CONSTRAINT CK_Bugs_Dates
        CHECK (FixDate IS NULL OR FixDate >= BugDate)

);


CREATE TABLE BugLog (
    BugLogID INT AUTO_INCREMENT,

    BugLogDate DATE NOT NULL,

    CatCodeID INT NOT NULL,
    StatusCodeID INT NOT NULL,
    UserID INT NOT NULL,
    BugID INT NOT NULL,

    BugLogDesc TEXT,

    PRIMARY KEY (BugLogID),

    CONSTRAINT FK_BugLog_Cat
        FOREIGN KEY (CatCodeID)
        REFERENCES CatCodes(CatCodeID),

    CONSTRAINT FK_BugLog_Status
        FOREIGN KEY (StatusCodeID)
        REFERENCES StatusCodes(StatusCodeID),

    CONSTRAINT FK_BugLog_User
        FOREIGN KEY (UserID)
        REFERENCES Users(UserID),

    CONSTRAINT FK_BugLog_Bug
        FOREIGN KEY (BugID)
        REFERENCES Bugs(BugID)

);

-- INSERTS DO EXERCÍCIO --

INSERT INTO Applications (AppName, AppVersion, AppDesc)
VALUES
('Sistema ERP', '1.0', 'Controle empresarial'),
('Portal Cliente', '2.3', 'Portal de atendimento');

INSERT INTO Users (UserName, UserEmail, UserTel)
VALUES
('Ciclano', 'ciclano@email.com', '11999999999'),
('Fulano', 'fulano@email.com', '11888888888');

INSERT INTO CatCodes (CatCodeDesc)
VALUES
('Cadastro'),
('Financeiro');

INSERT INTO StatusCodes (StatusCodeDesc)
VALUES
('Aberto'),
('Resolvido');

INSERT INTO Bugs
(AppID, UserID, BugSignOff, BugDate, BugDesc, BugDetails, RepSteps, FixDate)
VALUES
(
    1,
    1,
    2,
    '2025-06-01',
    'Erro ao salvar cliente',
    'Falha ao gravar cadastro',
    'Cadastrar cliente e clicar em salvar',
    '2025-06-05'
);

INSERT INTO BugLog
(BugLogDate, CatCodeID, StatusCodeID, UserID, BugID, BugLogDesc)
VALUES
(
    '2025-06-01',
    1,
    1,
    1,
    1,
    'Bug registrado'
);

	SHOW TABLES;
    SELECT * FROM applications;
	SELECT * FROM users;
        SELECT * FROM catcodes;