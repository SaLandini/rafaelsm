<html lang="en">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@1,300&display=swap');
    html {
        background: url("https://miro.medium.com/max/5120/1*w2oP08XEq2YhDrVU5Yv3Pw.png");
    }
    body {
        background-color: rgba(196, 125, 135, 0.95);
    }
    p, h1 {
        font-family: 'Lato', sans-serif;
        font-size: xx-large;
    }
    button{
        padding-left: 10px;
        padding-right: 10px;
        border: 0px;
        border-radius: 10px;
        background: rgba(196, 125, 135, 0);
    }
    button:hover {
        color: aquamarine;
    }
    .initial {
        margin: 15%;
    }
    .about {
        display: grid;
        grid-template-columns: 1fr 1fr;
        justify-content: space-between;
        align-items: center;
    }
    .about img {
        margin-left: 30%;
        margin-bottom: 10px;
        margin-top: 10px;
        border-radius: 20px;
    }
    .text {
        font-weight: bolder;
    }
</style>
<head>
    <meta charset="UTF-8">
</head>
<body>
    <div class="initial">
        <div class="middle">
            <div class="about">
                <div class="text_button">
                    <p class="text">Eu me chamo Rafael Salandin Moraes, tenho 15 anos, estudo Data Science, Desenvolvimento Web,
                    e Segurança de Dado/Pentest, normalmente com python.</p>
                </div>
                <img src="https://avatars3.githubusercontent.com/u/62630050?s=400&u=e747fa53ebfb82c18fff73bf928b713a2f2ecff5&v=4" alt="">
            </div>
        </div>
    </div>
</body>
</html>
<html lang="pt-br">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@1,300&display=swap');
    body {
        background-color: rgba(196, 125, 135, 0.95);
    }
    p, h1 {
        font-family: 'Lato', sans-serif;
        font-size: xx-large;
    }
    button{
        padding-left: 10px;
        padding-right: 10px;
        border: 0px;
        border-radius: 10px;
        background: rgba(196, 125, 135, 0);
    }
    button:hover {
        color: aquamarine;
    }
    .formação {
        border-radius: 30px;
        padding: 5%;
        background-color: aliceblue;
    }
    .class, .curses{
        display: grid;
        grid-template-columns: 1fr 1fr;
        justify-content: space-between;
        align-items: center;
        border: black;
        border-width: 1px;
        border-style: solid;
        border-radius: 35px;
    }
    .class p, .curses p {
        margin:3%;
    }
    .about img {
        margin-left: 30%;
        margin-bottom: 10px;
        margin-top: 10px;
        border-radius: 20px;
    }
    .text {
        font-weight: bolder;
    }
</style>
<head>
    <meta charset="UTF-8">
</head>
<body>
<div class="formação">
    <h1>Formação:</h1>
    <div class="class">
        <p><b>Ensino Médio</b> - Etec "Orlando Quagliato"<br>Periodo: 2019 - 2021</p>
        <p><b>Lingua Estrangeira, Inglês</b> - Wizard Santa Cruz do Rio Pardo <br>Periodo: 2013 - 2021</p>
        <p><b>Tecnico em Desenvolvimento de Sistemas</b> - Etec "Orlando Quagliato"<br>Periodo: 2020 - 2021</p>
    </div>
    <h1>Cursos com certificação:</h1>
    <div class="curses">
        <p><b>Programação em Python do Básico ao avançado</b><br>Carga Horaria: 57 horas</p>
        <p><b>Learn image processing and GUIs while having fun in Matlab</b><br>Carga Horaria: 11 horas</p>
        <p><b>Formação Cientista de Dados com Python e R</b><br>Carga Horaria: 72 horas</p>
        <p><b>Introdução ao Hacking e ao Pentest</b><br>Carga Horaria: 7 horas</p>
        <p><b>Python para Pentesters</b><br>Carga Horaria: 19 horas</p>
    </div>
</div>
</body>
</html>
