const regras = {
    "B1": "B1 não pode ser maior que o valor total de A1",
    "B2": "B2 não pode ser maior que o valor total de A1",
    "B3": "B3 não pode ser maior que o valor total de A1",
    "C1": "C1 não pode ser maior que o valor total de A1",
    "C2": "C2 não pode ser maior que o valor total de A1",
    "E2": "E2 não pode ser maior que o valor total de E1",
    "E3": "E3 não pode ser maior que o valor total de E1",
    "E4": "E4 não pode ser maior que o valor total de E1",
    "E5": "E5 não pode ser maior que o valor total de E1",
    "E6": "E6 não pode ser maior que o valor total de E1",

}
addEventListener('load',
    (event) => {
        console.log("load__________________________________________")
        for (const regra in regras) {
            console.log("entrou no loop")
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


        const a1 = document.getElementById('A1_T');
        const a1_M_1 = document.getElementById('A1_M_1');
        const a1_F_1 = document.getElementById('A1_F_1');
        const a1_M_2 = document.getElementById('A1_M_2');
        const a1_F_2 = document.getElementById('A1_F_2');
        const a1_M_3 = document.getElementById('A1_M_3');
        const a1_F_3 = document.getElementById('A1_F_3');
        const a1_M_4 = document.getElementById('A1_M_4');
        const a1_F_4 = document.getElementById('A1_F_4');
        const a1_M_5 = document.getElementById('A1_M_5');
        const a1_F_5 = document.getElementById('A1_F_5');

        const b1 = document.getElementById('B1');
        const b2 = document.getElementById('B2');
        const b3 = document.getElementById('B3');

        const c1 = document.getElementById('C1');
        const c2 = document.getElementById('C2');

        const d1 = document.getElementById('D1');

        const e1 = document.getElementById('E1_T');
        const e1_M_1 = document.getElementById('E1_M_1');
        const e1_F_1 = document.getElementById('E1_F_1');
        const e1_M_2 = document.getElementById('E1_M_2');
        const e1_F_2 = document.getElementById('E1_F_2');
        const e1_M_3 = document.getElementById('E1_M_3');
        const e1_F_3 = document.getElementById('E1_F_3');
        const e1_M_4 = document.getElementById('E1_M_4');
        const e1_F_4 = document.getElementById('E1_F_4');

        const e2 = document.getElementById('E2');
        const e3 = document.getElementById('E3');
        const e4 = document.getElementById('E4');
        const e5 = document.getElementById('E5');
        const e6 = document.getElementById('E6');

        const f1 = document.getElementById('F1');


        a1.addEventListener('blur', () => {
            if (b1.value && a1.value) {
                if (Number(b1.value) > Number(a1.value)) {
                    alert(regras['B1'])
                    b1.value = 0
                }
            }
        })


        b1.addEventListener('blur', () => {
            if (b1.value && a1.value) {
                if (Number(b1.value) > Number(a1.value)) {
                    alert(regras['B1'])
                    b1.value = 0
                }
            }
        })

        b2.addEventListener('blur', () => {
            if (b2.value && a1.value) {
                if (Number(b2.value) > Number(a1.value)) {
                    alert(regras['B2'])
                    b2.value = 0
                }
            }
        })

        b3.addEventListener('blur', () => {
            if (b3.value && a1.value) {
                if (Number(b3.value) > Number(a1.value)) {
                    alert(regras['B3'])
                    b3.value = 0
                }
            }
        })

        c1.addEventListener('blur', () => {
            if (c1.value && a1.value) {
                if (Number(c1.value) > Number(a1.value)) {
                    alert(regras['C1'])
                    c1.value = 0
                }
            }
        })

        c2.addEventListener('blur', () => {
            if (c2.value && a1.value) {
                if (Number(c2.value) > Number(a1.value)) {
                    alert(regras['C1'])
                    c2.value = 0
                }
            }
        })

        e2.addEventListener('blur', () => {
            if (e2.value && e1.value) {
                if (Number(e2.value) > Number(e1.value)) {
                    alert(regras['E2'])
                    e2.value = 0
                }
            }
        })

        e3.addEventListener('blur', () => {
            if (e3.value && e1.value) {
                if (Number(e3.value) > Number(e1.value)) {
                    alert(regras['E3'])
                    e3.value = 0
                }
            }
        })

        e4.addEventListener('blur', () => {
            if (e4.value && e1.value) {
                if (Number(e4.value) > Number(e1.value)) {
                    alert(regras['E4'])
                    e4.value = 0
                }
            }
        })

        e5.addEventListener('blur', () => {
            if (e5.value && e1.value) {
                if (Number(e5.value) > Number(e1.value)) {
                    alert(regras['E5'])
                    e5.value = 0
                }
            }
        })

        e6.addEventListener('blur', () => {
            if (e6.value && e1.value) {
                if (Number(e6.value) > Number(e1.value)) {
                    alert(regras['E6'])
                    e6.value = 0
                }
            }
        })

        /*
                
                a1.addEventListener('blur', () => {
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
      
      
                }) */


        for (const input of document.getElementsByTagName('input')) {
            console.log(input)

            if (input.type === 'number') {
                input.value = 0

            }



        }
        window.addEventListener('input', () => {
            const total_a1 = parseInt(a1_M_1.value) +
                parseInt(a1_F_1.value) +
                parseInt(a1_M_2.value) +
                parseInt(a1_F_2.value) +
                parseInt(a1_M_3.value) +
                parseInt(a1_F_3.value) +
                parseInt(a1_M_4.value) +
                parseInt(a1_F_4.value) +
                parseInt(a1_M_5.value) +
                parseInt(a1_F_5.value)

            a1.value = total_a1.toString()

            const total_e1 = parseInt(e1_M_1.value) +
            parseInt(e1_F_1.value) +
            parseInt(e1_M_2.value) +
            parseInt(e1_F_2.value) +
            parseInt(e1_M_3.value) +
            parseInt(e1_F_3.value) +
            parseInt(e1_M_4.value) +
            parseInt(e1_F_4.value) 

            e1.value = total_e1.toString()
        })
    }
)
