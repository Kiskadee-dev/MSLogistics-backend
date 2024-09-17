# Execução
Projeto recebido, criado e executado em 3 dias

# Tecnologias utilizadas
## Backend
- Python: Flask, Peewee
## Frontend
- React
- React router
- Tanstack query
- Tailwindcss
- React hook forms

# Checklist
- [x] Gerenciamento das mercadorias;
- [x] Gerenciamento de entrada e saída de mercadorias;
- [] Tela para visualização das entradas e saídas por mês de cada mercadoria em formato de gráfico;
- [] Exportar relatório mensal com todas as entradas e saídas de todas as mercadorias no formato PDF.

# Validação
Os dados são validados em ambos os lados, poderia ser melhor com o uso do Marshmallow ou Pydantic mas devido ao tempo vamos confiar no orm.

# Autenticação
Não há, mas é trivial implementar, como está fora do escopo não implementei.
Seria uma autenticação simples, inclusive criei o usuário Admin. Após ser aceito a solicitação o backend retornaria um token JWT que seria salvo no Redis por um tempo determinado, com isso já seria possível implementar políticas de RBAC (Autorização por papéis)

# Testes
Poucos, verifiquei o acesso às views mas não havia muita margem de tempo para eles, caso contrário seguiria com testes de integração com selenium pelo seleniumbase para garantir que o frontend esteja funcionando conforme o esperado. 

# Por fim
Dos pontos 1 ao 7 de requisitos, todos foram observados e implementados de acordo.