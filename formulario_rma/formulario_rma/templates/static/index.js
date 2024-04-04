const regras = {
    "A2": "A2 não pode ser maior que A1",
    "B1": "B2 não pode ser maior que A2",
    "B2": "B2 não pode ser maior que A2",
    "B3": "B3 não pode ser maior que B2",
    "B4": "B4 não pode ser maior que A2",
    "B5": "B5 não pode ser maior que A2",
    "B6": "B6 não pode ser maior que A2",
    "C2": "A soma de C2 com C3 não pode ser maior que C1",
    "C3": "A soma de C2 com C3 não pode ser maior que C1",
    "C4": "C4 não pode ser maior que C1",
    "C5": "C5 não pode ser maior que C1",
    "C6": "C6 não pode ser maior que C1",
    "C7": "C7 não pode ser maior que C1",
    "C8": "C8 não pode ser maior que C1",
    "C9": "C9 não pode ser maior que C1",
}

addEventListener('load',
    (event) => {
        for (const regra in regras) {
          
            const element = document.getElementById(regra + "_tooltip");
            element.title = regras[regra]
            element.style.display = "block"
        }

        HTMLCollection.prototype.forEach = Array.prototype.forEach;
        const inputs = document.getElementsByTagName('input')
        inputs.forEach(input => {
            input.addEventListener('blur', (e) => {
                if (input.value && Number(input.value) < 0) {
                    input.value = 0;
                    alert("Valor deve ser maior ou igual a zero")
                }
            })


        })

        const a1 = document.getElementById('A1');
        const a2 = document.getElementById('A2');
        const b1 = document.getElementById('B1');
        const b2 = document.getElementById('B2');
        const b3 = document.getElementById('B3');
        const b4 = document.getElementById('B4');
        const b5 = document.getElementById('B5');
        const b6 = document.getElementById('B6');
        const c1 = document.getElementById('C1');
        const c2 = document.getElementById('C2');
        const c3 = document.getElementById('C3');
        const c4 = document.getElementById('C4');
        const c5 = document.getElementById('C5');
        const c6 = document.getElementById('C6');
        const c7 = document.getElementById('C7');
        const c8 = document.getElementById('C8');
        const c9 = document.getElementById('C9');

        a1.addEventListener('blur', () => {
            if (a2.value && a1.value) {
                if (Number(a2.value) > Number(a1.value)) {
                    alert(regras['A2'])
                    a2.value = 0
                }
            }
        })
        a2.addEventListener('blur', () => {
            if (a2.value && a1.value) {
                if (Number(a2.value) > Number(a1.value)) {
                    alert(regras['A2'])
                    a2.value = 0
                }
            }
        })
        b1.addEventListener('blur', () => {
            if (b2.value && b1.value) {
                if (Number(b2.value) > Number(b1.value)) {
                    alert(regras['B2'])
                    b2.value = 0
                }
            }
        })
        b2.addEventListener('blur', () => {
            if (b2.value && b1.value) {
                if (Number(b2.value) > Number(b1.value)) {
                    alert(regras['B2'])
                    b2.value = 0
                }
            }
        })
        b3.addEventListener('blur', () => {
            if (b3.value && b1.value) {
                if (Number(b3.value) > Number(b1.value)) {
                    alert(regras['B3'])
                    b3.value = 0
                }
            }
        })
        b4.addEventListener('blur', () => {
            if (b4.value && b1.value) {
                if (Number(b4.value) > Number(b1.value)) {
                    alert(regras['B4'])
                    b4.value = 0
                }
            }
        })
        b5.addEventListener('blur', () => {
            if (b5.value && b1.value) {
                if (Number(b5.value) > Number(b1.value)) {
                    alert(regras['B5'])
                    b5.value = 0
                }
            }
        })
        b6.addEventListener('blur', () => {
            if (b6.value && b1.value) {
                if (Number(b6.value) > Number(b1.value)) {
                    alert(regras['B6'])
                    b6.value = 0
                }
            }
        })
        c1.addEventListener('blur', () => {
            if (c2.value && c1.value) {
                if (Number(c2.value) > Number(c1.value)) {
                    alert(regras['C2'])
                    c2.value = 0
                }
            }
        })
        c2.addEventListener('blur', () => {
            if (c2.value && c1.value) {
                if (Number(c2.value) > Number(c1.value)) {
                    alert(regras['C2'])
                    c2.value = 0
                }
            }
        })
        c3.addEventListener('blur', () => {
            if (c3.value && c1.value) {
                if (Number(c3.value) > Number(c1.value)) {
                    alert(regras['C3'])
                    c3.value = 0
                }
            }
        })
        c2.addEventListener('blur', () => {
            if (c1.value && c2.value && c3.value) {
                if (Number(c2.value) + Number(c3.value) > Number(c1.value)) {
                    alert("A soma do C2 com o C3 não pode ser maior que o C1")
                    c2.value = 0
                    c3.value = 0
                }
            }
        })
        c3.addEventListener('blur', () => {
            if (c1.value && c2.value && c3.value) {
                if (Number(c2.value) + Number(c3.value) > Number(c1.value)) {
                    alert("A soma do C2 com o C3 não pode ser maior que o C1")
                    c2.value = 0
                    c3.value = 0
                }
            }
        })
        c4.addEventListener('blur', () => {
            if (c4.value && c1.value) {
                if (Number(c4.value) > Number(c1.value)) {
                    alert(regras['C4'])
                    c4.value = 0
                }
            }
        })
        c5.addEventListener('blur', () => {
            if (c5.value && c1.value) {
                if (Number(c5.value) > Number(c1.value)) {
                    alert(regras['C5'])
                    c5.value = 0
                }
            }
        })
        c6.addEventListener('blur', () => {
            if (c6.value && c1.value) {
                if (Number(c6.value) > Number(c1.value)) {
                    alert(regras['C6'])
                    c6.value = 0
                }
            }
        })
        c7.addEventListener('blur', () => {
            if (c7.value && c1.value) {
                if (Number(c7.value) > Number(c1.value)) {
                    alert(regras['C7'])
                    c7.value = 0
                }
            }
        })
        c8.addEventListener('blur', () => {
            if (c8.value && c1.value) {
                if (Number(c8.value) > Number(c1.value)) {
                    alert(regras['C8'])
                    c8.value = 0
                }
            }
        })
        c9.addEventListener('blur', () => {
            if (c9.value && c1.value) {
                if (Number(c9.value) > Number(c1.value)) {
                    alert(regras['C9'])
                    c9.value = 0
                }
            }
        })
    }
)
{% extends "base.html" %}
{% block title %}
    {{"Formulário de Registro Mensal de Atendimentos"|upper }}
{% endblock title %}
{% block body %}
<form action={{'send_form_'|add:tipo_unidade}} method="POST" onkeydown="return event.key != 'Enter';" id="index_form">

    {% csrf_token %}
    {% include "DadosCras.html" with CRAS=user_cras id_cras=id_cras_user mes_ano=mes_ano_user endereco=endereco_user municipio=municipio_user uf=uf_user %}
    <form action='send_form' method="POST">
        {% csrf_token %}
        <div class='mx-xl-5 mx-xxl-5 mx-2'>
        {% for title, bloco in perguntas_json.items %}
            {% include "rowbloco1.html" with Title=bloco.Title rowpayload=bloco.childs%}
        
        {% endfor %}
        </div>
        {% comment %} {% include "rowbloco1.html" with Title=perguntas_json.B.Title %}
        {% include "rowbloco1.html" with Title=perguntas_json.C.Title %}
        {% include "rowbloco1.html" with Title=perguntas_json.D.Title %} {% endcomment %}
        {% include "dados_servidor.html" with nome_servidor='Nome' matricula_servidor='Matrícula' cargo_servidor='Cargo' %}
        {% include "enviarbutton.html" %}
    </form>
<script type="text/javascript">
    var form_data = "{{ form_data }}";
    if(form_data){
        form_data = form_data.replace(/(&quot\;)/g,"\"")
        var form_data_json = JSON.parse(form_data);

        console.log(form_data_json)
        const formData = FormAdapter.fromDomainJson(form_data_json)

        console.log( formData)

        FormPresenter.fromForm(formData)

       
        const botao_enviar = document.getElementById("enviar");
        botao_enviar.style.visibility = 'hidden';
        botao_enviar.remove()
    
    
        const button_voltar = document.createElement("button");
        button_voltar.classList.add("border")
        button_voltar.classList.add("border-0")
        button_voltar.classList.add("rounded")
        button_voltar.classList.add("col-1")
        button_voltar.classList.add("bg-primary")
        button_voltar.classList.add("text-light")
        button_voltar.innerHTML = "Voltar";
    
        const button_div = document.querySelector('#button_div');
        button_voltar.style.height = "5vh";
        button_voltar.style.width = "15vw"
        button_div.appendChild(button_voltar);
    
        index_form.action = '../rmaAdmin'

    }
    


   
</script>
{% endblock body %}
