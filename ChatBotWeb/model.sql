-- Tabela cliente
CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome_cliente VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    cpf VARCHAR(14) NOT NULL
);

-- Tabela funcionario
CREATE TABLE funcionario (
    id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    salario DECIMAL(10, 2) NOT NULL
);

-- Tabela veiculo
CREATE TABLE veiculo (
    id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    estoque INT NOT NULL
);

-- Tabela vendas
CREATE TABLE vendas (
    id_venda INT AUTO_INCREMENT PRIMARY KEY,
    data_venda DATE NOT NULL,
    valor_venda DECIMAL(10, 2) NOT NULL,
    id_veiculo INT,
    FOREIGN KEY (id_veiculo) REFERENCES veiculo(id_veiculo)
);

-- Tabela veiculo_problema
CREATE TABLE veiculo_problema (
    id_problema INT AUTO_INCREMENT PRIMARY KEY,
    tipo_problema VARCHAR(200) NOT NULL,
    id_veiculo INT,
    FOREIGN KEY (id_veiculo) REFERENCES veiculo(id_veiculo)
);

CREATE TABLE faturamento (
    id_faturamento INT AUTO_INCREMENT PRIMARY KEY,
    data_faturamento DATE NOT NULL,
    valor_faturamento FLOAT NOT NULL
);

CREATE TABLE Brasil (
    ID_BRASIL INT AUTO_INCREMENT PRIMARY KEY,
    estado VARCHAR(255) NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    latitude DECIMAL(10, 6) NOT NULL,
    longitude DECIMAL(10, 6) NOT NULL
);

CREATE TABLE veiculos_ativos (
    id_veiculo_ativo INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(255) NOT NULL,
    placa VARCHAR(10) NOT NULL,
    ID_BRASIL INT,
    FOREIGN KEY (ID_BRASIL) REFERENCES Brasil(ID_BRASIL)
);

ALTER TABLE VEICULO_PROBLEMA ADD COLUMN KM_RODADO FLOAT;
DELETE FROM VEICULO_PROBLEMA WHERE ID_PROBLEMA BETWEEN 11 AND 20;
UPDATE VEICULO_PROBLEMA SET KM_RODADO = CAST(RAND() * 1000 AS DECIMAL(10,2)) WHERE ID_PROBLEMA BETWEEN 1 AND 20;



INSERT INTO cliente (nome_cliente, idade, cpf) VALUES
    ('Ana Silva', 28, '111.222.333-44'),
    ('João Santos', 35, '555.666.777-88'),
    ('Mariana Oliveira', 22, '999.888.777-66'),
    ('Pedro Almeida', 40, '444.333.222-11'),
    ('Sandra Pereira', 29, '888.999.555-44'),
    ('Lucas Ferreira', 32, '777.888.111-22'),
    ('Cristina Souza', 27, '666.555.222-33'),
    ('Ricardo Martins', 38, '333.444.666-55'),
    ('Isabela Lima', 24, '555.444.777-88'),
    ('Fernando Rodrigues', 41, '222.333.555-66');


INSERT INTO funcionario (nome, cargo, salario) VALUES
    ('Carlos Silva', 'Vendedor', 2500.00),
    ('Fernanda Alves', 'Gerente', 5000.00),
    ('Rafaela Santos', 'Assistente', 1800.00),
    ('André Oliveira', 'Vendedor', 2300.00),
    ('Patricia Ferreira', 'Assistente', 1900.00),
    ('Gustavo Lima', 'Vendedor', 2400.00),
    ('Amanda Costa', 'Gerente', 5200.00),
    ('Diego Martins', 'Vendedor', 2200.00),
    ('Juliana Rodrigues', 'Assistente', 1950.00),
    ('Renato Souza', 'Vendedor', 2350.00);

INSERT INTO veiculo (modelo, estoque) VALUES
    ('Ford Fiesta', 15),
    ('Ford Focus', 10),
    ('Ford Fusion', 8),
    ('Ford Mustang', 5),
    ('Ford Escape', 10),
    ('Ford Explorer', 7),
    ('Ford Edge', 6),
    ('Ford Bronco', 3),
    ('Ford Ranger', 9),
    ('Ford Expedition', 4);

INSERT INTO vendas (data_venda, valor_venda, id_veiculo) VALUES
    ('2023-08-01', 22000.00, 1),
    ('2023-08-02', 18000.00, 1),
    ('2023-08-03', 32000.00, 1),
    ('2023-08-04', 25000.00, 4),
    ('2023-08-05', 28000.00, 2),
    ('2023-08-06', 20000.00, 6),
    ('2023-08-07', 23000.00, 3),
    ('2023-08-08', 21000.00, 3),
    ('2023-08-09', 45000.00, 9),
    ('2023-08-10', 50000.00, 10),
    ('2023-08-11', 22000.00, 1),
    ('2023-08-12', 18000.00, 2),
    ('2023-08-13', 32000.00, 3),
    ('2023-08-14', 25000.00, 4),
    ('2023-08-15', 28000.00, 2),
    ('2023-08-16', 20000.00, 2),
    ('2023-08-17', 23000.00, 7),
    ('2023-08-18', 21000.00, 5),
    ('2023-08-19', 45000.00, 5),
    ('2023-08-20', 50000.00, 10),
    ('2023-08-21', 22000.00, 1),
    ('2023-08-22', 18000.00, 5),
    ('2023-08-23', 32000.00, 3),
    ('2023-08-24', 25000.00, 6),
    ('2023-08-25', 28000.00, 5),
    ('2023-08-26', 20000.00, 6),
    ('2023-08-27', 23000.00, 6),
    ('2023-08-28', 21000.00, 8),
    ('2023-08-29', 45000.00, 7),
    ('2023-08-30', 50000.00, 10),
    ('2022-08-18', 21000.00, 5),
    ('2022-08-19', 45000.00, 5),
    ('2022-08-20', 50000.00, 10),
    ('2022-08-21', 22000.00, 1),
    ('2022-08-22', 18000.00, 5),
    ('2022-08-23', 32000.00, 3),
    ('2022-08-24', 25000.00, 6),
    ('2022-08-25', 28000.00, 5),
    ('2022-08-26', 20000.00, 6),
    ('2022-08-27', 23000.00, 6),
    ('2022-08-28', 21000.00, 8),
    ('2022-08-29', 45000.00, 7),
    ('2022-08-30', 50000.00, 10);



	INSERT INTO veiculo_problema (tipo_problema, id_veiculo) VALUES
    ('Motor com falha', 1),
    ('Transmissão com problemas', 2),
    ('Freios não funcionam corretamente', 3),
    ('Problemas elétricos', 4),
    ('Vazamento de óleo', 5),
    ('Problemas de suspensão', 6),
    ('Sistema de ar condicionado defeituoso', 7),
    ('Desgaste excessivo dos pneus', 8),
    ('Problemas de direção', 9),
    ('Falha no sistema de ignição', 10);



INSERT INTO faturamento (data_faturamento, valor_faturamento) VALUES
    ('2023-08-01', 150000.00),
    ('2023-08-02', 180000.00),
    ('2023-07-03', 220000.00),
    ('2023-07-04', 120000.00),
    ('2023-07-05', 250000.00),
    ('2023-06-06', 190000.00),
    ('2023-06-07', 170000.00),
    ('2023-06-08', 210000.00),
    ('2023-06-09', 280000.00),
    ('2023-05-10', 320000.00),
    ('2023-05-11', 150000.00),
    ('2023-04-12', 180000.00),
    ('2023-04-13', 220000.00),
    ('2023-03-14', 120000.00),
    ('2023-02-15', 250000.00),
    ('2022-08-01', 150000.00),
    ('2022-08-02', 180000.00),
    ('2022-07-03', 220000.00),
    ('2022-07-04', 120000.00),
    ('2022-07-05', 250000.00),
    ('2022-06-06', 190000.00),
    ('2022-06-07', 170000.00),
    ('2022-06-08', 210000.00),
    ('2022-06-09', 280000.00),
    ('2022-05-10', 320000.00),
    ('2022-05-11', 150000.00),
    ('2022-04-12', 180000.00),
    ('2022-04-13', 220000.00),
    ('2022-03-14', 120000.00),
    ('2022-02-15', 250000.00),
    ('2022-06-08', 210000.00),
    ('2022-06-09', 280000.00),
    ('2022-05-10', 320000.00),
    ('2022-05-11', 150000.00),
    ('2022-04-12', 180000.00),
    ('2022-04-13', 220000.00),
    ('2022-03-14', 120000.00),
    ('2022-02-15', 250000.00),
    ('2022-01-15', 250000.00),
    ('2022-01-15', 250000.00),
    ('2022-01-15', 250000.00),
    ('2022-01-15', 250000.00),
    ('2021-08-01', 150000.00),
    ('2021-08-02', 180000.00),
    ('2021-07-03', 220000.00),
    ('2021-07-04', 120000.00),
    ('2021-07-05', 250000.00),
    ('2021-06-06', 190000.00),
    ('2021-06-07', 170000.00),
    ('2021-06-08', 210000.00),
    ('2021-05-09', 280000.00),
    ('2021-04-10', 320000.00),
    ('2021-03-11', 150000.00),
    ('2021-02-12', 180000.00),
    ('2020-01-13', 220000.00),
    ('2020-06-06', 190000.00),
    ('2020-06-07', 170000.00),
    ('2020-06-08', 210000.00),
    ('2020-05-09', 280000.00),
    ('2020-04-10', 320000.00),
    ('2020-03-11', 150000.00),
    ('2020-02-12', 1800000.00),;

INSERT INTO Brasil (estado, cidade, latitude, longitude) VALUES
    ('São Paulo', 'São Paulo', -23.5505, -46.6333),
    ('São Paulo', 'Campinas', -22.9071, -47.0632),
    ('São Paulo', 'Santos', -23.9535, -46.3343),
	('Rio de Janeiro', 'Rio de Janeiro', -22.9068, -43.1729),
    ('Rio de Janeiro', 'Niterói', -22.8811, -43.1042),
    ('Rio de Janeiro', 'Petrópolis', -22.5132, -43.2096),
    ('Santa Catarina', 'Florianópolis', -27.5954, -48.5480),
    ('Santa Catarina', 'Joinville', -26.3039, -48.8411),
    ('Santa Catarina', 'Blumenau', -26.9185, -49.0650),
	('Amazonas', 'Manaus', -3.1190, -60.0217),
    ('Amazonas', 'Parintins', -2.6276, -56.7350),
    ('Amazonas', 'Itacoatiara', -3.1377, -58.4442),
	('Espírito Santo', 'Vitória', -20.3155, -40.3128),
    ('Espírito Santo', 'Vila Velha', -20.3297, -40.2925),
    ('Espírito Santo', 'Cariacica', -20.2637, -40.4165),
	('Pará', 'Belém', -1.4558, -48.4902),
    ('Pará', 'Santarém', -2.4392, -54.7150),
    ('Pará', 'Ananindeua', -1.3650, -48.3725),
     ('Maranhão', 'São Luís', -2.5290, -44.3020),
    ('Maranhão', 'Imperatriz', -5.5183, -47.4777),
    ('Maranhão', 'Caxias', -4.8654, -43.3611),
    ('Pernambuco', 'Recife', -8.0476, -34.8770),
    ('Pernambuco', 'Caruaru', -8.2846, -35.9798),
    ('Pernambuco', 'Petrolina', -9.3887, -40.5001),
	('Bahia', 'Salvador', -12.9716, -38.5016),
    ('Bahia', 'Feira de Santana', -12.2575, -38.9665),
    ('Bahia', 'Vitória da Conquista', -14.8661, -40.8397),
	('Rio Grande do Sul', 'Porto Alegre', -30.0346, -51.2177),
    ('Rio Grande do Sul', 'Caxias do Sul', -29.1658, -51.1794),
    ('Rio Grande do Sul', 'Pelotas', -31.7662, -52.3213),
    ('Mato Grosso', 'Cuiabá', -15.5989, -56.0949),
    ('Mato Grosso', 'Várzea Grande', -15.6455, -56.1324),
    ('Mato Grosso', 'Rondonópolis', -16.4671, -54.6377);

    INSERT INTO veiculos_ativos (modelo, placa, ID_BRASIL) VALUES
    ('Ford Focus', 'ABC1234', 1),
    ('Ford Fiesta', 'DEF5678', 2),
    ('Ford Fusion', 'GHI9012', 3),
    ('Ford Mustang', 'JKL3456', 4),
    ('Ford Escape', 'MNO7890', 5),
    ('Ford Explorer', 'PQR1234', 6),
    ('Ford Edge', 'STU5678', 7),
    ('Ford Ranger', 'VWX9012', 8),
    ('Ford F-150', 'YZA3456', 9),
    ('Ford EcoSport', 'BCD7890', 10),
    ('Ford Taurus', 'EFG1234', 11),
    ('Ford Bronco', 'HIJ5678', 12),
    ('Ford Expedition', 'KLM9012', 13),
    ('Ford Transit', 'NOP3456', 14),
    ('Ford Super Duty', 'QRS7890', 15),
    ('Ford GT', 'TUV1234', 16),
    ('Ford Crown Victoria', 'WXY5678', 17),
    ('Ford Thunderbird', 'ZAB9012', 18),
    ('Ford Aspire', 'BCD2345', 19),
    ('Ford Contour', 'EFG6789', 20),
    ('Ford Taurus X', 'HIJ0123', 21),
    ('Ford Windstar', 'KLM3456', 22),
    ('Ford Freestar', 'NOP7890', 23),
    ('Ford Flex', 'QRS1234', 24),
    ('Ford Aerostar', 'TUV5678', 25),
    ('Ford Transit Connect', 'WXY9012', 26),
    ('Ford Bronco Sport', 'ZAB3456', 27),
    ('Ford Escort', 'BCD6789', 28),
    ('Ford Probe', 'EFG0123', 29),
    ('Ford Festiva', 'HIJ4567', 30),
    ('Ford Aspire', 'KLM8901', 30),
    ('Ford Focus', 'NOP2345', 29),
    ('Ford Taurus', 'QRS6789', 28),
    ('Ford Escort', 'TUV0123', 27),
    ('Ford Fiesta', 'WXY4567', 26),
    ('Ford Contour', 'ZAB8901', 25),
    ('Ford Thunderbird', 'BCD2345', 24),
    ('Ford Mustang', 'EFG6789', 23),
    ('Ford GT', 'HIJ0123', 22),
    ('Ford Explorer', 'KLM4567', 21),
    ('Ford Expedition', 'NOP8901', 20),
    ('Ford Escape', 'QRS2345', 19),
    ('Ford Edge', 'TUV6789', 18),
    ('Ford EcoSport', 'WXY0123', 16),
    ('Ford Fusion', 'ZAB4567', 17),
    ('Ford Transit', 'BCD8901', 1),
    ('Ford Ranger', 'EFG2345', 4),
    ('Ford F-150', 'HIJ6789', 1),
    ('Ford Super Duty', 'KLM0123', 1),
    ('Ford Bronco', 'NOP4567', 1),
    ('Ford Focus', 'ABC1234', 31),
    ('Ford Fiesta', 'DEF5678', 31),
    ('Ford Fusion', 'GHI9012', 32),
    ('Ford Mustang', 'JKL3456', 32),
    ('Ford Escape', 'MNO7890', 33),
    ('Ford Explorer', 'PQR1234', 33),
    ('Ford Edge', 'STU5678', 31),
    ('Ford Ranger', 'VWX9012', 31),
    ('Ford F-150', 'YZA3456', 32),
    ('Ford EcoSport', 'BCD7890', 33);

CREATE TABLE FEEDBACK_CLIENTE(
ID_FEEDBACK INT AUTO_INCREMENT PRIMARY KEY,
VEICULO VARCHAR(100),
FEEDBACK text,
SENTIMENTO VARCHAR(10)
);

INSERT INTO FEEDBACK_CLIENTE (VEICULO, FEEDBACK, SENTIMENTO)
VALUES ('Ford Mustang', "I absolutely love my Ford Mustang. It's a fantastic car!", 'positivo'),
('Ford Mustang', "The car is amazing.", 'positivo'),
('Ford Mustang', "I enjoy driving it every day.", 'positivo'),
('Ford Mustang', "The performance is top-notch.", 'positivo'),
('Ford Mustang', "It's a true masterpiece.", 'positivo'),
('Ford Mustang', "I love the sleek design.", 'positivo'),
('Ford Mustang', "The handling is impressive.", 'positivo'),
('Ford Mustang', "The power is exhilarating.", 'positivo'),
('Ford Mustang', "I can't get enough of it.", 'positivo'),
('Ford Mustang',  "The exterior is eye-catching.", 'positivo'),
('Ford Mustang', "Driving it is a thrill.", 'positivo'),
('Ford Mustang', "I'm a proud owner.", 'positivo'),
('Ford Mustang', "It never disappoints.", 'positivo'),
('Ford Mustang', "I recommend it to everyone.", 'positivo'),
('Ford Mustang', "Owning it is a dream come true.", 'positivo'),
('Ford Mustang', "It's a symbol of excellence.", 'positivo'),
('Ford Mustang', "I feel powerful behind the wheel.", 'positivo'),
('Ford Mustang', "The interior is comfortable and stylish.", 'positivo'),
('Ford Mustang', "Every drive is an adventure.", 'positivo'),
('Ford Mustang', "I've never had a car like it.", 'positivo'),
('Ford Mustang', "The speed is mind-blowing.", 'positivo'),
('Ford Mustang', "I'm in love with it.", 'positivo'),
('Ford Mustang', "The design is timeless.", 'positivo'),
('Ford Mustang', "It's a true gem.", 'positivo'),
('Ford Mustang', "The acceleration is impressive.", 'positivo'),
('Ford Mustang', "It's the best car I''ve ever owned.", 'positivo'),
('Ford Mustang', "The reliability is outstanding.", 'positivo'),
('Ford Mustang', "It's a performance masterpiece.", 'positivo'),
('Ford Mustang', "I can't imagine my life without it.", 'positivo'),
('Ford Mustang', "The engine sound is music to my ears.", 'positivo'),
('Ford Mustang', "It's my pride and joy.", 'positivo'),
('Ford Mustang', "Driving it is a pure joy.", 'positivo'),
('Ford Mustang', "It's a work of art.", 'positivo'),
('Ford Mustang', "I'm constantly impressed by it.", 'positivo'),
('Ford Mustang', "It's a true American icon.", 'positivo'),
('Ford Mustang', "I'm a die-hard fan.", 'positivo'),
('Ford Mustang', "The quality is superb.", 'positivo'),
('Ford Mustang', "I feel like a rockstar.", 'positivo'),
('Ford Mustang', "The performance is unmatched.", 'positivo'),
('Ford Mustang', "It's a legend.", 'positivo'),
('Ford Mustang', "I'm excited every time I drive it.", 'positivo'),
('Ford Mustang', "It exceeds all expectations.", 'positivo'),
('Ford Mustang', "It's an engineering marvel.", 'positivo'),
('Ford Mustang', "It's a true masterpiece of engineering.", 'positivo'),
('Ford Mustang', "It's a must-have.", 'positivo'),
('Ford Mustang', "The car has too many issues.", 'negativo'),
('Ford Mustang', "I regret buying it.", 'negativo'),
('Ford Mustang', "The fuel efficiency is terrible.", 'negativo'),
('Ford Mustang', "It constantly breaks down.", 'negativo'),
('Ford Mustang', "I'm disappointed with the performance.", 'negativo'),
('Ford Mustang', "The interior is cheap and uncomfortable.", 'negativo'),
('Ford Mustang', "I've had nothing but problems.", 'negativo'),
('Ford Mustang', "It's a money pit.", 'negativo'),
('Ford Mustang', "The handling is poor.", 'negativo'),
('Ford Mustang', "I'm frustrated with the constant repairs.", 'negativo'),
('Ford Mustang', "The resale value is awful.", 'negativo'),
('Ford Mustang', "It's a waste of money.", 'negativo'),
('Ford Mustang', "I can't rely on it.", 'negativo'),
('Ford Mustang', "The build quality is subpar.", 'negativo'),
('Ford Mustang', "I''s uncomfortable for long drives.", 'negativo'),
('Ford Mustang', "The maintenance costs are sky-high.", 'negativo'),
('Ford Mustang', "I've had nothing but headaches.", 'negativo'),
('Ford Mustang', "It's not worth the price.", 'negativo'),
('Ford Mustang', "The engine has issues.", 'negativo'),
('Ford Mustang', "I''m constantly in the shop.", 'negativo'),
('Ford Mustang', "It's a lemon.", 'negativo'),
('Ford Mustang', "The customer service is terrible.", 'negativo'),
('Ford Mustang', "I regret my decision.", 'negativo'),
('Ford Mustang', "It's been a nightmare.", 'negativo'),
('Ford Mustang', "The problems never end.", 'negativo');

-- Inserir dados na tabela VEICULO_IMPORTADO com quantidade IMPORTADO aleatória
INSERT INTO VEICULO_IMPORTADO (IMPORTADO, MODELO, ANO)
SELECT
    FLOOR(RAND() * 4001) + 1000 AS IMPORTADO,
    'Ford F-600' AS MODELO,
    YEAR('2010-01-01') + n AS ANO
FROM (
    SELECT 0 AS n UNION ALL
    SELECT 1 UNION ALL
    SELECT 2 UNION ALL
    SELECT 3 UNION ALL
    SELECT 4 UNION ALL
    SELECT 5 UNION ALL
    SELECT 6 UNION ALL
    SELECT 7 UNION ALL
    SELECT 8 UNION ALL
    SELECT 9 UNION ALL
    SELECT 10 UNION ALL
    SELECT 11 UNION ALL
    SELECT 12
) years;

INSERT INTO VEICULO_IMPORTADO (IMPORTADO, MODELO, ANO)
SELECT
    FLOOR(RAND() * 4001) + 1000 AS IMPORTADO,
    'Ford F-100' AS MODELO,
    YEAR('2010-01-01') + n AS ANO
FROM (
    SELECT 0 AS n UNION ALL
    SELECT 1 UNION ALL
    SELECT 2 UNION ALL
    SELECT 3 UNION ALL
    SELECT 4 UNION ALL
    SELECT 5 UNION ALL
    SELECT 6 UNION ALL
    SELECT 7 UNION ALL
    SELECT 8 UNION ALL
    SELECT 9 UNION ALL
    SELECT 10 UNION ALL
    SELECT 11 UNION ALL
    SELECT 12
) years;

-- Repetir o mesmo padrão para os outros modelos e anos
INSERT INTO VEICULO_IMPORTADO (IMPORTADO, MODELO, ANO)
SELECT
    FLOOR(RAND() * 4001) + 1000 AS IMPORTADO,
    'Ford F-350' AS MODELO,
    YEAR('2010-01-01') + n AS ANO
FROM (
    SELECT 0 AS n UNION ALL
    SELECT 1 UNION ALL
    SELECT 2 UNION ALL
    SELECT 3 UNION ALL
    SELECT 4 UNION ALL
    SELECT 5 UNION ALL
    SELECT 6 UNION ALL
    SELECT 7 UNION ALL
    SELECT 8 UNION ALL
    SELECT 9 UNION ALL
    SELECT 10 UNION ALL
    SELECT 11 UNION ALL
    SELECT 12
) years;

-- Repetir o mesmo padrão para os outros modelos e anos
INSERT INTO VEICULO_IMPORTADO (IMPORTADO, MODELO, ANO)
SELECT
    FLOOR(RAND() * 4001) + 1000 AS IMPORTADO,
    'Bronco' AS MODELO,
    YEAR('2010-01-01') + n AS ANO
FROM (
    SELECT 0 AS n UNION ALL
    SELECT 1 UNION ALL
    SELECT 2 UNION ALL
    SELECT 3 UNION ALL
    SELECT 4 UNION ALL
    SELECT 5 UNION ALL
    SELECT 6 UNION ALL
    SELECT 7 UNION ALL
    SELECT 8 UNION ALL
    SELECT 9 UNION ALL
    SELECT 10 UNION ALL
    SELECT 11 UNION ALL
    SELECT 12
) years;

-- Repetir o mesmo padrão para os outros modelos e anos
INSERT INTO VEICULO_IMPORTADO (IMPORTADO, MODELO, ANO)
SELECT
    FLOOR(RAND() * 4001) + 1000 AS IMPORTADO,
    'Maverick' AS MODELO,
    YEAR('2010-01-01') + n AS ANO
FROM (
    SELECT 0 AS n UNION ALL
    SELECT 1 UNION ALL
    SELECT 2 UNION ALL
    SELECT 3 UNION ALL
    SELECT 4 UNION ALL
    SELECT 5 UNION ALL
    SELECT 6 UNION ALL
    SELECT 7 UNION ALL
    SELECT 8 UNION ALL
    SELECT 9 UNION ALL
    SELECT 10 UNION ALL
    SELECT 11 UNION ALL
    SELECT 12
) years;


CREATE TABLE DEMANDFORECASTING (
    ID INT auto_increment PRIMARY KEY,
    CARRO_MODELO VARCHAR(100),
    DATA_VENDA DATE,
    NUMEROS_VENDAS INT,
    MODELO_ESTOQUE INT,
    TENDENCIA_MERCADO VARCHAR(100),
    INDICADOR_ECONOMICO VARCHAR(100),
    ATIVIDADE_CONCORRENTE VARCHAR(100),
    EPOCA_ANO VARCHAR(100),
    PROMOTIONS VARCHAR(100)
    );

    -- Inserir dados na tabela DEMANDFORECASTING para cada mês de 2020 com EPOCA_ANO aleatório
INSERT INTO DEMANDFORECASTING (CARRO_MODELO, DATA_VENDA, NUMEROS_VENDAS, MODELO_ESTOQUE, TENDENCIA_MERCADO, INDICADOR_ECONOMICO, ATIVIDADE_CONCORRENTE, EPOCA_ANO, PROMOTIONS)
SELECT
    'Ford F-600' AS CARRO_MODELO,
    DATE_FORMAT('2015-01-03', '%Y-%m-%d') + INTERVAL n MONTH AS DATA_VENDA,
    FLOOR(RAND() * 50) + 50 AS NUMEROS_VENDAS,
    FLOOR(RAND() * 300) + 200 AS MODELO_ESTOQUE,
    CASE WHEN RAND() < 0.3 THEN 'Aumentando' WHEN RAND() < 0.6 THEN 'Diminuindo' ELSE 'Estável' END AS TENDENCIA_MERCADO,
    CASE WHEN RAND() < 0.3 THEN 'Forte' WHEN RAND() < 0.6 THEN 'Médio' ELSE 'Fraco' END AS INDICADOR_ECONOMICO,
    CASE WHEN RAND() < 0.2 THEN 'Lançando produto' WHEN RAND() < 0.5 THEN 'Reduzindo preços' ELSE 'Parcerias' END AS ATIVIDADE_CONCORRENTE,
    CASE WHEN RAND() < 0.5 THEN 'Sim' ELSE 'Não' END AS PROMOTIONS,
    CASE
        WHEN RAND() < 0.25 THEN 'Primavera'
        WHEN RAND() < 0.5 THEN 'Verão'
        WHEN RAND() < 0.75 THEN 'Outono'
        ELSE 'Inverno'
    END AS EPOCA_ANO
FROM (
    SELECT 0 AS n UNION ALL
    SELECT 1 UNION ALL
    SELECT 2 UNION ALL
    SELECT 3 UNION ALL
    SELECT 4 UNION ALL
    SELECT 5 UNION ALL
    SELECT 6 UNION ALL
    SELECT 7 UNION ALL
    SELECT 8 UNION ALL
    SELECT 9 UNION ALL
    SELECT 10 UNION ALL
    SELECT 11
) months;

CREATE TABLE CARROS_ELETRICO(
ID INTEGER AUTO_INCREMENT PRIMARY KEY,
MARCA VARCHAR(100),
UNIDADES_VENDIDAS INTEGER,
AUTONOMIA VARCHAR(100),
MARCA_CONHECIDA BIT,
INCENTIVOS_FISCAIS BIT,
ACESSIVEL BIT,
ANO INTEGER
);

-- Baixa autonomia: Menos de 150 km
-- Média autonomia: Entre 150 e 300 km
-- Alta autonomia: Mais de 300 km

DROP TABLE CARROS_ELETRICO;

INSERT INTO CARROS_ELETRICO(MARCA, UNIDADES_VENDIDAS, AUTONOMIA, MARCA_CONHECIDA, INCENTIVOS_FISCAIS, ACESSIVEL, ANO)
VALUES
('Volvo', 2354, 'Baixa', 1, 0, 0, 2022),
('Renault', 1999, 'Media',1, 1,1, 2022),
('Caoa Chery', 782, 'Media', 0, 1, 1, 2022),
('BMW', 539, 'Alta', 1, 0, 0, 2022),
('FORD', 1557, 'Alta', 1, 1, 0, 2022);
-- Baixa autonomia: Menos de 150 km
-- Média autonomia: Entre 150 e 300 km
-- Alta autonomia: Mais de 300 km


INSERT INTO CARROS_ELETRICO(MARCA, UNIDADES_VENDIDAS, AUTONOMIA, MARCA_CONHECIDA, INCENTIVOS_FISCAIS, ACESSIVEL, ANO)
VALUES
('Volvo', 2354, 'Baixa', 1, 0, 0, 2022),
('Renault', 1999, 'Media',1, 1,1, 2022),
('Caoa Chery', 782, 'Media', 0, 1, 1, 2022),
('BMW', 539, 'Alta', 1, 0, 0, 2022),
('Ford', 1557, 'Alta', 1, 1, 0, 2022),
('Volvo', 801, 'Baixa', 1, 0, 0, 2021),
('Renault', 645, 'Média', 1, 1, 1, 2021),
('Caoa Chery', 228, 'Média', 0, 1, 1, 2021),
('BMW', 165, 'Alta', 1, 0, 0, 2021),
('Ford', 483, 'Alta', 1, 1, 0, 2021),
('Volvo', 603, 'Baixa', 1, 0, 0, 2020),
('Renault', 485, 'Média', 1, 1, 1, 2020),
('Caoa Chery', 102, 'Média', 0, 1, 1, 2020),
('BMW', 84, 'Alta', 1, 0, 0, 2020),
('Ford', 250, 'Alta', 1, 1, 0, 2020),
('Volvo', 492, 'Baixa', 1, 0, 0, 2020),
('Renault', 204, 'Média', 1, 1, 1, 2020),
('Caoa Chery', 57, 'Média', 0, 1, 1, 2020),
('BMW', 25, 'Alta', 1, 0, 0, 2020),
('Ford', 120, 'Alta', 1, 1, 0, 2020);
