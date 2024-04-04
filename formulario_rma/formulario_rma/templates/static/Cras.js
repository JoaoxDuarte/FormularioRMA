const regras = {
    "A2": "A2 não pode ser maior que A1",
    "B1": "B1 não pode ser maior que A2",
    "B2": "B2 não pode ser maior que A2",
    "B3": "B3 não pode ser maior que A2",
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
    "D1": "D1 não pode ser maior que A1",
}


addEventListener('load',
    (event) => {
        const botao_enviar = document.getElementById("enviar")
        botao_enviar.disabled = true;
        console.log("load__________________________________________")
        for (const regra in regras) {

            const element = document.getElementById(regra + "_tooltip");
            element.title = regras[regra]
            element.style.display = "block"
            console.log("regra")
            console.log(regra)
        }

        HTMLCollection.prototype.forEach = Array.prototype.forEach;
        const inputs = document.getElementsByTagName('input')
        inputs.forEach(input => {
            console.log("For each")
            input.addEventListener('blur', (e) => {
                if (input.value && Number(input.value) < 0) {
                    input.value = 0;
                    alert("Valor deve ser maior ou igual a zero")
                }
            })


        })


        all_input = document.getElementsByTagName('input');


        all_input.forEach(input => {
            input.addEventListener('input', (e) => {
                let has_empty_value = false

                all_input.forEach(input => {

                    if (input.value == null || input.value == '') {
                        has_empty_value = true
                    }

                })
                if (!has_empty_value) {
                    botao_enviar.disabled = false
                }
                else {
                    botao_enviar.disabled = true
                }
            })
        })

        const a1 = document.getElementById('A1');
        console.log("a1_____________________________________________")
        console.log(a1)
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
        const d1 = document.getElementById('D1');


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
            if (b1.value && a2.value) {
                if (Number(b1.value) > Number(a2.value)) {
                    alert(regras['B1'])
                    b1.value = 0
                }
            }
        })
        b2.addEventListener('blur', () => {
            if (b2.value && a2.value) {
                if (Number(b2.value) > Number(a2.value)) {
                    alert(regras['B2'])
                    b2.value = 0
                }
            }
        })
        b2.addEventListener('blur', () => {
            if (b3.value && b2.value) {
                if (Number(b3.value) > Number(a2.value)) {
                    alert(regras['B3'])
                    b3.value = 0
                }
            }
        })
        b3.addEventListener('blur', () => {
            if (b3.value && b2.value) {
                if (Number(b3.value) > Number(b2.value)) {
                    alert(regras['B3'])
                    b3.value = 0
                }
            }
        })
        b2.addEventListener('blur', () => {
            if (b3.value && b1.value) {
                if (Number(b3.value) > Number(b2.value)) {
                    alert(regras['B3'])
                    b3.value = 0
                }
            }
        })
        b4.addEventListener('blur', () => {
            if (b4.value && b1.value) {
                if (Number(b4.value) > Number(a2.value)) {
                    alert(regras['B4'])
                    b4.value = 0
                }
            }
        })
        b5.addEventListener('blur', () => {
            if (b5.value && b1.value) {
                if (Number(b5.value) > Number(a2.value)) {
                    alert(regras['B5'])
                    b5.value = 0
                }
            }
        })
        b6.addEventListener('blur', () => {
            if (b6.value && b1.value) {
                if (Number(b6.value) > Number(a2.value)) {
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
        d1.addEventListener('blur', () => {
            if (d1.value && a1.value) {
                if (Number(d1.value) > Number(a1.value)) {
                    alert(regras['D1'])
                    d1.value = 0
                }
            }
        })
    }
)
