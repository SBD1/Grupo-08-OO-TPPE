# Backlog

<p align="justify">
Backlog é uma lista com prioridades dos requisitos ou funcionalidades do projeto que fornecem valor comercial ao cliente. Geralmente utilizado na técnica de desenvolvimento ágil, SCRUM. Os itens podem ser adicionados a esse registro em qualquer momento. Cabe ao gerente de produto avaliar o registro e atualizar as prioridades conforme requisitado.
</p>

O Backlog do produto deve ser:

* Detalhado o suficiente para que os desenvolvedores consigam entregar as funcionalidades ou histórias de usuário descritas.
* Estimável de forma a ser possível dizer quanto tempo levará para implementar a funcionalidade.
* Emergente de forma que possa ser continuamente atualizado.
* Priorizado de forma a trazer maior valor para o cliente.

<p align="justify">
Backlogs são focados em histórias de usuário, e contém sua descrição, identificação e priorização.
</p>

## Histórias de Usuário (User Stories)

<p align="justify">
Histórias de Usuário, como o próprio nome diz, são histórias focadas no usuário que descrevem de forma simples funcionalidades do produto de software. Por serem focadas no usuário, apresentam uma abordagem do que deve ser feito e não como. Devem ser detalhadas o suficiente para se poder derivar as tarefas necessárias para a implementação, e podem ter critérios de aceitação.
</p>

São escritas no formato:

**_Eu, como (quem?) quero (o quê?) para (por quê?)._**

# Backlog - Sistema de Locadora de Veículos

<style>
    #td {
        border: 0.5px solid;
    }
</style>
<table>
    <thead>
        <tr>
            <th>Épico</th>
            <th>Feature</th>
            <th>ID</th>
            <th>História de Usuário</th>
            <th>Prioridade</th>
        </tr>
    </thead>
    <tbody>
        <tr class="epico">
            <td rowspan="5">E01<br>Gestão de Veículos</td>
            <td class="feature">F01<br>Cadastro de Veículos</td>
            <td>US01</td>
            <td>Eu, como funcionário, quero cadastrar novos veículos (modelo, marca, placa, ano) para disponibilizá-los para aluguel.</td>
            <td class="alta">Alta</td>
        </tr>
        <tr>
            <td class="feature" rowspan="2">F02<br>Consulta de Veículos</td>
            <td>US02</td>
            <td>Eu, como funcionário, quero buscar veículos por placa, marca ou modelo para localizá-los rapidamente.</td>
            <td class="alta">Alta</td>
        </tr>
        <tr>
            <td>US03</td>
            <td>Eu, como funcionário, quero filtrar veículos por disponibilidade (disponíveis/alugados) para gerenciar o estoque.</td>
            <td class="alta">Alta</td>
        </tr>
        <tr>
            <td class="feature" rowspan="2">F03<br>Manutenção de Veículos</td>
            <td>US04</td>
            <td>Eu, como funcionário, quero editar informações dos veículos cadastrados para manter os dados atualizados.</td>
            <td class="alta">Alta</td>
        </tr>
        <tr>
            <td>US05</td>
            <td>Eu, como funcionário, quero excluir veículos do sistema quando forem desativados da frota.</td>
            <td class="media">Média</td>
        </tr>
        <tr class="epico">
            <td rowspan="5">E02<br>Gestão de Locatários</td>
            <td class="feature" rowspan="2">F04<br>Cadastro de Locatários</td>
            <td>US06</td>
            <td>Eu, como funcionário, quero cadastrar clientes Pessoa Física (nome, CPF, CNH) para permitir aluguéis.</td>
            <td class="alta">Alta</td>
        </tr>
        <tr>
            <td>US07</td>
            <td>Eu, como funcionário, quero cadastrar clientes Pessoa Jurídica (razão social, CNPJ) com dados específicos.</td>
            <td class="alta">Alta</td>
        </tr>
        <tr>
            <td class="feature" rowspan="3">F05<br>Gestão de Locatários</td>
            <td>US08</td>
            <td>Eu, como funcionário, quero buscar locatários por CPF/CNPJ ou nome para consulta rápida.</td>
            <td class="alta">Alta</td>
        </tr>
        <tr>
            <td>US09</td>
            <td>Eu, como funcionário, quero editar dados cadastrais dos locatários para manter informações atualizadas.</td>
            <td class="media">Média</td>
        </tr>
        <tr>
            <td>US10</td>
            <td>Eu, como funcionário, quero inativar locatários no sistema quando necessário.</td>
            <td class="baixa">Baixa</td>
        </tr>
        <tr class="epico">
            <td rowspan="4">E03<br>Operações de Aluguel</td>
            <td class="feature" rowspan="2">F06<br>Reservas</td>
            <td>US11</td>
            <td>Eu, como funcionário, quero registrar reservas de veículos vinculando ao locatário (PF/PJ) e período.</td>
            <td class="alta">Alta</td>
        </tr>
        <tr>
            <td>US12</td>
            <td>Eu, como funcionário, quero consultar reservas ativas por período ou locatário.</td>
            <td class="alta">Alta</td>
        </tr>
    </tbody>
</table>
