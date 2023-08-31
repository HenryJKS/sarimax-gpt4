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
    ('2023-08-30', 50000.00, 10);


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


	CREATE TABLE faturamento (
    id_faturamento SERIAL PRIMARY KEY,
    data_faturamento DATE NOT NULL,
    valor_faturamento FLOAT NOT NULL
)

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
    ('2023-02-15', 250000.00);

