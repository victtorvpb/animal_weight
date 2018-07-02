# Arquitetura utilizada

Foi usado o form do django usando o motor de templates do Jinja para a parte do CRUD e o template [modular admin](https://github.com/modularcode/modular-admin-html) para realizar a parte do grafico. 
Esta arquiterura se deu por ter pouco tempo para a construção do desafio, já que tive alguns problemas no fim de semana e só consegui mexer no projeto ontem e hoje.

# Arquitetura Ideal

Ter um sistema cliente servidor onde a parte que o cliente vê seria feito em alguma biblioteca/framework como reactjs, angularjs ou vuejs, pois assim poderia ser utilizado para qualquer tipo de cliente(seja web, mobile ou chamada por api).
Para autenticação o ideal seria utilizar [JWT](https://jwt.io/) por conta da sua segurança maior.