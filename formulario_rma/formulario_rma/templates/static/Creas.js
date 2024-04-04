
const regras = {
    "A2": "A2 não pode ser maior que o Valor do Campo A1",
    "B1": "B1 não pode ser maior que o Valor do Campo A2",
    "B2": "B2 não pode ser maior que o Valor do Campo A2",
    "B3": "B3 não pode ser maior que o Valor do Campo A2",
    "B4": "B4 não pode ser maior que o Valor do Campo A2",
    "B5": "B5 não pode ser maior que o Valor do Campo A2",
    "B7": "B7 não pode ser maior que o Valor do Campo A2",
    // "C1_M_1": "C1 Masculino 0 a 6 anos não pode ser maior que o Valor do Campo Total B6",
    // "C1_F_1": "C1 Feminino 0 a 6 anos não pode ser maior que o Valor do Campo Total B6",
    // "C1_M_2": "C1 Masculino 7 a 12 anos não pode ser maior que o Valor do Campo Total B6",
    // "C1_F_2": "7 a 12 anos não pode ser maior que o Valor do Campo Total B6",
    // "C1_M_3": "C1 Masculino 13 a 17 anos não pode ser maior que o Valor do Campo Total B6",
    // "C1_F_3": "C1 Feminino 13 a 17 anos não pode ser maior que o Valor do Campo Total B6",
    "C1": "A soma dos valores informados nos campos C1, não pode ser maior que o Valor do Campo Total B6",
    // "C2_M_1": "C2 Masculino 0 a 6 anos não pode ser maior que o Valor do Campo Total B6",
    // "C2_F_1": "C2 Feminino 0 a 6 anos não pode ser maior que o Valor do Campo Total B6",
    // "C2_M_2": "C2 Masculino 7 a 12 anos não pode ser maior que o Valor do Campo Total B6",
    // "C2_F_2": "C2 Feminino 7 a 12 anos não pode ser maior que o Valor do Campo Total B6",
    // "C2_M_3": "C2 Masculino 13 a 17 anos não pode ser maior que o Valor do Campo Total B6",
    // "C2_F_3": "C2 Feminino 13 a 17 anos não pode ser maior que o Valor do Campo Total B6",
    "C2": "A soma dos valores informados nos campos C2, não pode ser maior que o Valor do Campo Total B6",
    // "C3_M_1": "C3 Masculino 0 a 6 anos não pode ser maior que o Valor do Campo Total B6",
    // "C3_F_1": "C3 Feminino 0 a 6 anos não pode ser maior que o Valor do Campo Total B6",
    // "C3_M_2": "C3 Masculino 7 a 12 anos não pode ser maior que o Valor do Campo Total B6",
    // "C3_F_2": "C3 Feminino 7 a 12 anos não pode ser maior que o Valor do Campo Total B6",
    // "C3_M_3C": "C3 Masculino 13 a 17 anos não pode ser maior que o Valor do Campo Total B6",
    // "C3_F_3": "C3 Feminino 13 a 17 anos não pode ser maior que o Valor do Campo Total B6",
    "C3": "A soma dos valores informados nos campos C3, não pode ser maior que o Valor do Campo Total B6",
    // "C4_M_1": "C4 Masculino 0 a 6 anos não pode ser maior que o Valor do Campo Total B6",
    // "C4_F_1": "C4 Feminino 0 a 6 anos não pode ser maior que o Valor do Campo Total B6",
    // "C4_M_2": "C4 Masculino 7 a 12 anos não pode ser maior que o Valor do Campo Total B6",
    // "C4_F_2": "C4 Feminino 7 a 12 anos não pode ser maior que o Valor do Campo Total B6",
    // "C4_M_3": "C4 Masculino 13 a 17 anos não pode ser maior que o Valor do Campo Total B6",
    // "C4_F_3": "C4 Feminino 13 a 17 anos não pode ser maior que o Valor do Campo Total B6",
    "C4": "A soma dos valores informados nos campos C4, não pode ser maior que o Valor do Campo Total B6",
    // "C5_M_1": "C5 Masculino 0 a 12 anos não pode ser maior que o Valor do Campo Total B6",
    // "C5_M_2": "C5 Masculino 13 a 15 anos não pode ser maior que o Valor do Campo Total B6",
    // "C5_F_1": "C5 Feminino 0 a 12 anos não pode ser maior que o Valor do Campo Total B6",
    // "C5_F_2": "C5 Feminino 13 a 15 anos não pode ser maior que o Valor do Campo Total B6",
    "C5": "A soma dos valores informados nos campos C5 não pode ser maior que o Valor do Campo Total B6",
    "D1": "A soma dos valores informados nos campos D1 não pode ser maior que o Valor do Campo Total B6",
    // "D1_M_1": "D1 Masculino não pode ser maior que o Valor do Campo Total B6",
    // "D1_F_1": "D1 Feminino não pode ser maior que o Valor do Campo Total B6",
    "D2": "A soma dos valores informados nos campos D2, não pode ser maior que o Valor do Campo Total B6",
    // "D2_M_1": "D2 Masculino não pode ser maior que o Valor Campo Total B6",
    // "D2_F_1": "D2 Feminino não pode ser maior que o Valor do Campo Total B6",
    "E1": "A soma dos valores informados nos campos E1 não pode ser maior que o Valor do Campo Total B6",
    // "E1_M_1": "E1 Masculino (0 a 12 anos) não pode ser maior que o Valor do Campo Total B6",
    // "E1_M_2": "E1 Masculino (13 a 17 anos) não pode ser maior que o Valor do Campo Total B6",
    // "E1_M_3": "E1 Masculino (18 a 59 anos) não pode ser maior que o Valor do Campo Total B6",
    // "E1_M_4": "E1 Masculino (60 anos ou mais) não pode ser maior que o Valor do Campo Total B6",
    // "E1_F_1": "E1 Feminino (0 a 12 anos) não pode ser maior que o Valor do Campo Total B6",
    // "E1_F_2": "E1 Feminino (13 a 17 anos) não pode ser maior que o Valor do Campo Total B6",
    // "E1_F_3": "E1 Feminino (18 a 59 anos) não pode ser maior que o Valor do Campo Total B6",
    // "E1_F_4": "E1 Feminino (60 anos ou mais) não pode ser maior que o Valor do Campo Total B6",
    "E2": "A soma dos valores informados nos campos E2 não pode ser maior que o Valor do Campo Total B6",
    // "E2_M_1": "E2 Masculino (0 a 12 anos) não pode ser maior que o Valor do Campo Total B6",
    // "E2_M_2": "E2 Masculino (13 a 17 anos) não pode ser maior que o Valor do Campo Total B6",
    // "E2_M_3": "E2 Masculino (18 a 59 anos) não pode ser maior que o Valor do Campo Total B6",
    // "E2_M_4C": "E2 Masculino (60 anos ou mais) não pode ser maior que o Valor do Campo Total B6",
    // "E2_F_1": "E2 Feminino (0 a 12 anos) não pode ser maior que o Valor do Campo Total B6",
    // "E2_F_2": "E2 Feminino (13 a 17 anos) não pode ser maior que o Valor do Campo Total B6",
    // "E2_F_3": "E2 Feminino (18 a 59 anos) não pode ser maior que o Valor do Campo Total B6",
    // "E2_F_4": "E2 Feminino (60 anos ou mais) não pode ser maior que o Valor do Campo Total B6",
    "F1": "F1 não pode ser maior que o Valor do Campo Total B6",
    "G1": "A soma dos valores informados nos campos G1 não pode ser maior que o Valor do Campo Total B6",
    // "G1_M_1": "G1 Masculino (0 a 12 anos) não pode ser maior que o Valor do Campo Total B6",
    // "G1_M_2": "G1 Masculino (13 a 17 anos) não pode ser maior que o Valor do Campo Total B6",
    // "G1_M_3": "G1 Masculino (18 a 59 anos) não pode ser maior que o Valor do Campo Total B6",
    // "G1_M_4": "G1 Masculino (60 anos ou mais) não pode ser maior que o Valor do Campo Total B6",
    // "G1_F_1": "G1 Feminino (0 a 12 anos) não pode ser maior que o Valor do Campo Total B6",
    // "G1_F_2": "G1 Feminino (13 a 17 anos) não pode ser maior que o Valor do Campo Total B6",
    // "G1_F_3": "G1 Feminino (18 a 59 anos) não pode ser maior que o Valor do Campo Total B6",
    // "G1_F_4": "G1 Feminino (60 anos ou mais) não pode ser maior que o Valor do Campo Total B6",
    "H1": "H1 não pode ser maior que o Valor do Campo Total B6",
    "I1": "A soma dos valores informados nos campos I1 não pode ser maior que o Valor do Campo Total B6",
    // "I1_M_1": "I1 Masculino (0 a 12 anos) não pode ser maior que o Valor do Campo Total B6",
    // "I1_M_2": "I1 Masculino (13 a 17 anos) não pode ser maior que o Valor do Campo Total B6",
    // "I1_M_3": "I1 Masculino (18 a 59 anos) não pode ser maior que o Valor do Campo Total B6",
    // "I1_M_4": "I1 Masculino (60 anos ou mais) não pode ser maior que o Valor do Campo Total B6",
    // "I1_F_1": "I1 Feminino (0 a 12 anos) não pode ser maior que o Valor do Campo Total B6",
    // "I1_F_2": "I1 Feminino (13 a 17 anos) não pode ser maior que o Valor do Campo Total B6",
    // "I1_F_3": "I1 Feminino (18 a 59 anos) não pode ser maior que o Valor do Campo Total B6",
    // "I1_F_4": "I1 Feminino (60 anos ou mais) não pode ser maior que o Valor do Campo Total B6",
    "J2": "J2 não pode ser maior que o Valor do Campo J1",
    "J3": "J3 não pode ser maior que o Valor do Campo J1",
    /*A soma dos campos J2 + J3 não pode ser menor que o Valor do Campo J1;*/
    "J1": "A soma dos campos J2 + J3 não pode ser maior que o Valor do Campo J1",
    /*A soma dos campos J5 Total + J6 Total não pode ser menor que o Valor do Campo J4 Total!;*/
    "J4": "A soma dos campos J5 Total + J6 Total não pode ser menor que o Valor do Campo J4 Total!",
    // "J5_M_1": "J5 Masculino não pode ser maior que o Valor do Campo J4 Masculino",
    // "J5_F_1": "J5 Feminino não pode ser maior que o Valor do Campo J4 Feminino",
    // "J6_M_1": "J6 Masculino não pode ser maior que o Valor do Campo J4 Masculino",
    // "J6_F_1": "J6 Feminino não pode ser maior que o Valor do Campo J4 Feminino",
    "K2": "K2 não pode ser maior que o Valor do Campo K1 Total",
    "K3": "K3 não pode ser maior que o Valor do Campo K1 Total",
    "K4": "K4 não pode ser maior que o Valor do Campo K1 Total",
    "K5": "K5 não pode ser maior que o Valor do Campo K1 Total",
    "K6": "K6 não pode ser maior que o Valor do Campo K1 Total",

}

addEventListener('load',
    (event) => {

        for(const input of document.getElementsByTagName('input')){ 
            console.log(input)

            if(input.type === 'number'){
                input.value= 0

            }

        }
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
        const b7 = document.getElementById('B7');

        const b6 = document.getElementById('B6_T');

        const b6_M_1 = document.getElementById('B6_M_1');
        const b6_F_1 = document.getElementById('B6_F_1');
        const b6_M_2 = document.getElementById('B6_M_2');
        const b6_F_2 = document.getElementById('B6_F_2');
        const b6_M_3 = document.getElementById('B6_M_3');
        const b6_F_3 = document.getElementById('B6_F_3');
        const b6_M_4 = document.getElementById('B6_M_4');
        const b6_F_4 = document.getElementById('B6_F_4');

        const c1 = document.getElementById('C1_T');
        const c1_M_1 = document.getElementById('C1_M_1');
        const c1_F_1 = document.getElementById('C1_F_1');
        const c1_M_2 = document.getElementById('C1_M_2');
        const c1_F_2 = document.getElementById('C1_F_2');
        const c1_M_3 = document.getElementById('C1_M_3');
        const c1_F_3 = document.getElementById('C1_F_3');

        const c2 = document.getElementById('C2_T');
        const c2_M_1 = document.getElementById('C2_M_1');
        const c2_F_1 = document.getElementById('C2_F_1');
        const c2_M_2 = document.getElementById('C2_M_2');
        const c2_F_2 = document.getElementById('C2_F_2');
        const c2_M_3 = document.getElementById('C2_M_3');
        const c2_F_3 = document.getElementById('C2_F_3');

        const c3 = document.getElementById('C3_T');
        const c3_M_1 = document.getElementById('C3_M_1');
        const c3_F_1 = document.getElementById('C3_F_1');
        const c3_M_2 = document.getElementById('C3_M_2');
        const c3_F_2 = document.getElementById('C3_F_2');
        const c3_M_3 = document.getElementById('C3_M_3');
        const c3_F_3 = document.getElementById('C3_F_3');

        const c4 = document.getElementById('C4_T');
        const c4_M_1 = document.getElementById('C4_M_1');
        const c4_F_1 = document.getElementById('C4_F_1');
        const c4_M_2 = document.getElementById('C4_M_2');
        const c4_F_2 = document.getElementById('C4_F_2');
        const c4_M_3 = document.getElementById('C4_M_3');
        const c4_F_3 = document.getElementById('C4_F_3');

        const c5 = document.getElementById('C5_T');
        const c5_M_1 = document.getElementById('C5_M_1');
        const c5_F_1 = document.getElementById('C5_F_1');
        const c5_M_2 = document.getElementById('C5_M_2');
        const c5_F_2 = document.getElementById('C5_F_2');

        const d1 = document.getElementById('D1_T');
        const d1_M_1 = document.getElementById('D1_M_1');
        const d1_F_1 = document.getElementById('D1_F_1');

        const d2 = document.getElementById('D2_T');
        const d2_M_1 = document.getElementById('D2_M_1');
        const d2_F_1 = document.getElementById('D2_F_1');

        const e1 = document.getElementById('E1_T');
        const e1_M_1 = document.getElementById('E1_M_1');
        const e1_F_1 = document.getElementById('E1_F_1');
        const e1_M_2 = document.getElementById('E1_M_2');
        const e1_F_2 = document.getElementById('E1_F_2');
        const e1_M_3 = document.getElementById('E1_M_3');
        const e1_F_3 = document.getElementById('E1_F_3');
        const e1_M_4 = document.getElementById('E1_M_4');
        const e1_F_4 = document.getElementById('E1_F_4');

        const e2 = document.getElementById('E2_T');
        const e2_M_1 = document.getElementById('E2_M_1');
        const e2_F_1 = document.getElementById('E2_F_1');
        const e2_M_2 = document.getElementById('E2_M_2');
        const e2_F_2 = document.getElementById('E2_F_2');
        const e2_M_3 = document.getElementById('E2_M_3');
        const e2_F_3 = document.getElementById('E2_F_3');
        const e2_M_4 = document.getElementById('E2_M_4');
        const e2_F_4 = document.getElementById('E2_F_4');

        const f1 = document.getElementById('F1');

        const g1 = document.getElementById('G1_T');
        const g1_M_1 = document.getElementById('G1_M_1');
        const g1_F_1 = document.getElementById('G1_F_1');
        const g1_M_2 = document.getElementById('G1_M_2');
        const g1_F_2 = document.getElementById('G1_F_2');
        const g1_M_3 = document.getElementById('G1_M_3');
        const g1_F_3 = document.getElementById('G1_F_3');
        const g1_M_4 = document.getElementById('G1_M_4');
        const g1_F_4 = document.getElementById('G1_F_4');

        const h1 = document.getElementById('H1');

        const i1 = document.getElementById('I1_T');
        const i1_M_1 = document.getElementById('I1_M_1');
        const i1_F_1 = document.getElementById('I1_F_1');
        const i1_M_2 = document.getElementById('I1_M_2');
        const i1_F_2 = document.getElementById('I1_F_2');
        const i1_M_3 = document.getElementById('I1_M_3');
        const i1_F_3 = document.getElementById('I1_F_3');
        const i1_M_4 = document.getElementById('I1_M_4');
        const i1_F_4 = document.getElementById('I1_F_4');

        const m1 = document.getElementById('M1');
        const m2 = document.getElementById('M2');
        const m3 = document.getElementById('M3');
        const m4 = document.getElementById('M4');

        const j1 = document.getElementById('J1');
        const j2 = document.getElementById('J2');
        const j3 = document.getElementById('J3');

        const j4 = document.getElementById('J4_T');
        const j4_M_1 = document.getElementById('J4_M_1');
        const j4_F_1 = document.getElementById('J4_F_1');

        const j5 = document.getElementById('J5_T');
        const j5_M_1 = document.getElementById('J5_M_1');
        const j5_F_1 = document.getElementById('J5_F_1');

        const j6 = document.getElementById('J6_T');
        const j6_M_1 = document.getElementById('J6_M_1');
        const j6_F_1 = document.getElementById('J6_F_1');

        const k1 = document.getElementById('K1_T');
        const k1_M_1 = document.getElementById('K1_M_1');
        const k1_F_1 = document.getElementById('K1_F_1');
        const k1_M_2 = document.getElementById('K1_M_2');
        const k1_F_2 = document.getElementById('K1_F_2');
        const k1_M_3 = document.getElementById('K1_M_3');
        const k1_F_3 = document.getElementById('K1_F_3');
        const k1_M_4 = document.getElementById('K1_M_4');
        const k1_F_4 = document.getElementById('K1_F_4');

        const k2 = document.getElementById('K2');
        const k3 = document.getElementById('K3');
        const k4 = document.getElementById('K4');
        const k5 = document.getElementById('K5');
        const k6 = document.getElementById('K6');



        window.addEventListener('input', () => {

            var total_b6 = parseInt(b6_M_1.value, 10) + parseInt(b6_F_1.value, 10) + parseInt(b6_M_2.value, 10) + parseInt(b6_F_2.value, 10)
                + parseInt(b6_M_3.value, 10) + parseInt(b6_F_3.value, 10) + parseInt(b6_M_4.value, 10) + parseInt(b6_F_4.value, 10)
            b6.value = total_b6.toString();

            var total_c1 = parseInt(c1_M_1.value, 10) + parseInt(c1_F_1.value, 10) + parseInt(c1_M_2.value, 10) + parseInt(c1_F_2.value, 10)
                + parseInt(c1_M_3.value, 10) + parseInt(c1_F_3.value, 10)
            c1.value = total_c1.toString()

            var total_c2 = parseInt(c2_M_1.value, 10) + parseInt(c2_F_1.value, 10) + parseInt(c2_M_2.value, 10) + parseInt(c2_F_2.value, 10)
                + parseInt(c2_M_3.value, 10) + parseInt(c2_F_3.value, 10)
            c2.value = total_c2.toString()

            var total_c3 = parseInt(c3_M_1.value, 10) + parseInt(c3_F_1.value, 10) + parseInt(c3_M_2.value, 10) + parseInt(c3_F_2.value, 10)
                + parseInt(c3_M_3.value, 10) + parseInt(c3_F_3.value, 10)
            c3.value = total_c3.toString()

            var total_c4 = parseInt(c4_M_1.value, 10) + parseInt(c4_F_1.value, 10) + parseInt(c4_M_2.value, 10) + parseInt(c4_F_2.value, 10)
                + parseInt(c4_M_3.value, 10) + parseInt(c4_F_3.value, 10)
            c4.value = total_c4.toString();

            var total_c5 = parseInt(c5_M_1.value, 10) + parseInt(c5_F_1.value, 10) + parseInt(c5_M_2.value, 10) + parseInt(c5_F_2.value, 10)
            c5.value = total_c5.toString()

            var total_d1 = parseInt(d1_M_1.value, 10) + parseInt(d1_F_1.value, 10)
            d1.value = total_d1.toString()


            var total_d2 = parseInt(d2_M_1.value, 10) + parseInt(d2_F_1.value, 10)
            d2.value = total_d2.toString();

            var total_e1 = parseInt(e1_M_1.value, 10) + parseInt(e1_F_1.value, 10) + parseInt(e1_M_2.value, 10) + parseInt(e1_F_2.value, 10)
                + parseInt(e1_M_3.value, 10) + parseInt(e1_F_3.value, 10) + parseInt(e1_M_4.value, 10) + parseInt(e1_F_4.value, 10)
            e1.value = total_e1.toString();

            var total_e2 = parseInt(e2_M_1.value, 10) + parseInt(e2_F_1.value, 10) + parseInt(e2_M_2.value, 10) + parseInt(e2_F_2.value, 10)
                + parseInt(e2_M_3.value, 10) + parseInt(e2_F_3.value, 10) + parseInt(e2_M_4.value, 10) + parseInt(e2_F_4.value, 10)
            e2.value = total_e2.toString();

            var total_g1 = parseInt(g1_M_1.value, 10) + parseInt(g1_F_1.value, 10) + parseInt(g1_M_2.value, 10) + parseInt(g1_F_2.value, 10)
                + parseInt(g1_M_3.value, 10) + parseInt(g1_F_3.value, 10) + parseInt(g1_M_4.value, 10) + parseInt(g1_F_4.value, 10)
            g1.value = total_g1.toString();

            var total_i1 = parseInt(i1_M_1.value, 10) + parseInt(i1_F_1.value, 10) + parseInt(i1_M_2.value, 10) + parseInt(i1_F_2.value, 10)
                + parseInt(i1_M_3.value, 10) + parseInt(i1_F_3.value, 10) + parseInt(i1_M_4.value, 10) + parseInt(i1_F_4.value, 10)
            i1.value = total_i1.toString();

            var total_j4 = parseInt(j4_M_1.value, 10) + parseInt(j4_F_1.value, 10)
            j4.value = total_j4.toString();

            var total_j5 = parseInt(j5_M_1.value, 10) + parseInt(j5_F_1.value, 10)
            j5.value = total_j5.toString();

            var total_j6 = parseInt(j6_M_1.value, 10) + parseInt(j6_F_1.value, 10)
            j6.value = total_j6.toString();

            var total_k1 = parseInt(k1_M_1.value, 10) + parseInt(k1_F_1.value, 10) + parseInt(k1_M_2.value, 10) + parseInt(k1_F_2.value, 10)
                + parseInt(k1_M_3.value, 10) + parseInt(k1_F_3.value, 10) + parseInt(k1_M_4.value, 10) + parseInt(k1_F_4.value, 10)
            k1.value = total_k1.toString();




        })

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
                    b2.value = 0
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
        b3.addEventListener('blur', () => {
            if (b3.value && a2.value) {
                if (Number(b3.value) > Number(a2.value)) {
                    alert(regras['B3'])
                    b3.value = 0
                }
            }
        })
        b4.addEventListener('blur', () => {
            if (b4.value && a2.value) {
                if (Number(b4.value) > Number(a2.value)) {
                    alert(regras['B4'])
                    b4.value = 0
                }
            }
        })
        b5.addEventListener('blur', () => {
            if (b5.value && a2.value) {
                if (Number(b5.value) > Number(a2.value)) {
                    alert(regras['B5'])
                    b5.value = 0
                }
            }
        })
        b7.addEventListener('blur', () => {
            if (b7.value && a2.value) {
                if (Number(b7.value) > Number(a2.value)) {
                    alert(regras['B7'])
                    b7.value = 0
                }
            }
        })
    
        f1.addEventListener('blur', () => {
            if (f1.value && b6.value) {
                if (Number(f1.value) > Number(b6.value)) {
                    alert(regras['F1'])
                    f1.value = 0
                    f1.style.color = 'red'
                }
            }
        })

        h1.addEventListener('blur', () => {
            if (h1.value && b6.value) {
                if (Number(h1.value) > Number(b6.value)) {
                    alert(regras['H1'])
                    h1.value = 0
                    h1.style.color = 'red'
                }
            }
        })

        j1.addEventListener('blur', () => {
            if (j1.value && j2.value && j3.value) {
                if (Number(j1.value) < (Number(j2.value) + Number(j3.value))) {
                    alert(regras['J1'])
                    j1.value = 0
                    j1.style.color = 'red'
                }

            }
        })

        j2.addEventListener('blur', () => {
            if (j2.value && j1.value) {
                if (Number(j2.value) + Number(j3.value) > Number(j1.value)) {
                    alert(regras['J2'])
                    j2.value = 0
                    j2.style.color = 'red'
                }
            }
        })

        j3.addEventListener('blur', () => {
            if (j3.value && j1.value) {
                if (Number(j3.value) + Number(j2.value) > Number(j1.value)) {
                    alert(regras['J3'])
                    j3.value = 0
                    j3.style.color = 'red'
                }
            }
        })


        j4.addEventListener('blur', () => {
            if (j5.value && j6.value && j4.value) {
                if (Number(j4.value) > (Number(j5.value) + Number(j6.value))) {
                    alert(regras['J5'])
                    j4.value = 0
                    j5.value = 0
                    j6.value = 0
                    j4.style.color = 'red'
                }
            }
        })
        
        k2.addEventListener('blur', () => {
            if (k2.value && k1.value) {
                if (Number(k2.value) > Number(k1.value)) {
                    alert(regras['K2'])
                    k2.value = 0
                    k2.style.color = 'red'
                }
            }
        })

        k3.addEventListener('blur', () => {
            if (k3.value && k1.value) {
                if (Number(k3.value) > Number(k1.value)) {
                    alert(regras['K3'])
                    k3.value = 0
                    k3.style.color = 'red'
                }
            }
        })

        k4.addEventListener('blur', () => {
            if (k4.value && k1.value) {
                if (Number(k4.value) > Number(k1.value)) {
                    alert(regras['K4'])
                    k4.value = 0
                    k4.style.color = 'red'
                }
            }
        })

        k5.addEventListener('blur', () => {
            if (k5.value && k1.value) {
                if (Number(k5.value) > Number(k1.value)) {
                    alert(regras['K5'])
                    k5.value = 0
                    k5.style.color = 'red'
                }
            }
        })

        k6.addEventListener('blur', () => {
            if (k6.value && k1.value) {
                if (Number(k6.value) > Number(k1.value)) {
                    alert(regras['K6'])
                    k6.value = 0
                    k6.style.color = 'red'
                }
            }
        })



        
        c1_maior_que_b6_dependencias = [c1, c1_M_1, c1_F_1, c1_M_2, c1_F_2, c1_M_3, c1_F_3, 
                                        b6, b6_F_1, b6_F_2, b6_F_3, b6_F_4, b6_M_1, b6_M_2, 
                                        b6_M_3, b6_M_4]
        c1_maior_que_b6_dependencias.forEach(
            (domNode) => { 
                
                domNode.addEventListener('change', () => {
                    c1_maior_que_b6(c1, c1_M_1, c1_F_1, c1_M_2, c1_F_2, c1_M_3, c1_F_3, b6)
                })

            }
        )


        c2_maior_que_b6_dependencias = [c2, c2_M_1, c2_F_1, c2_M_2, c2_F_2, c2_M_3, c2_F_3, b6,
                                            b6_F_1, b6_F_2, b6_F_3, b6_F_4, b6_M_1, b6_M_2, 
                                            b6_M_3, b6_M_4]
        c2_maior_que_b6_dependencias.forEach(
            (domNode) => {
            
                domNode.addEventListener('change', () => {
                    c2_maior_que_b6(c2, c2_M_1, c2_F_1, c2_M_2, c2_F_2, c2_M_3, c2_F_3, b6)
                })
            }
        )

        c3_maior_que_b6_dependencias = [c3, c3_M_1, c3_F_1, c3_M_2, c3_F_2, c3_M_3, c3_F_3, b6,
                                            b6_F_1, b6_F_2, b6_F_3, b6_F_4, b6_M_1, b6_M_2, 
                                            b6_M_3, b6_M_4]
        c3_maior_que_b6_dependencias.forEach(
            (domNode) => {
            
                domNode.addEventListener('change', () => {
                    c3_maior_que_b6(c3, c3_M_1, c3_F_1, c3_M_2, c3_F_2, c3_M_3, c3_F_3, b6)
                })
            }
        )

        c4_maior_que_b6_dependencias = [c4, c4_M_1, c4_F_1, c4_M_2, c4_F_2, c4_M_3, c4_F_3, b6,
                                            b6_F_1, b6_F_2, b6_F_3, b6_F_4, b6_M_1, b6_M_2, 
                                            b6_M_3, b6_M_4]
        c4_maior_que_b6_dependencias.forEach(
            (domNode) => {
            
                domNode.addEventListener('change', () => {
                    c4_maior_que_b6(c4, c4_M_1, c4_F_1, c4_M_2, c4_F_2, c4_M_3, c4_F_3, b6)
                })
            }
        )

        c5_maior_que_b6_dependencias = [c5, c5_M_1, c5_F_1, c5_M_2, c5_F_2, b6,
                                            b6_F_1, b6_F_2, b6_F_3, b6_F_4, b6_M_1, b6_M_2, 
                                            b6_M_3, b6_M_4]
        c5_maior_que_b6_dependencias.forEach(
            (domNode) => {
            
                domNode.addEventListener('change', () => {
                    c5_maior_que_b6(c5, c5_M_1, c5_F_1, c5_M_2, c5_F_2, b6)
                })
            }
        )

        d1_maior_que_b6_dependencias = [d1, d1_M_1, d1_F_1, b6,
                                            b6_F_1, b6_F_2, b6_F_3, b6_F_4, b6_M_1, b6_M_2, 
                                            b6_M_3, b6_M_4]
        d1_maior_que_b6_dependencias.forEach(
            (domNode) => {
            
                domNode.addEventListener('change', () => {
                    d1_maior_que_b6(d1, d1_M_1, d1_F_1, b6)
                })
            }
        )

        d2_maior_que_b6_dependencias = [d2, d2_M_1, d2_F_1, b6,
                                            b6_F_1, b6_F_2, b6_F_3, b6_F_4, b6_M_1, b6_M_2, 
                                            b6_M_3, b6_M_4]
        d2_maior_que_b6_dependencias.forEach(
            (domNode) => {
            
                domNode.addEventListener('change', () => {
                    d2_maior_que_b6(d2, d2_M_1, d2_F_1, b6)
                })
            }
        )

        e1_maior_que_b6_dependencias = [e1, e1_M_1, e1_F_1, e1_M_2, e1_F_2, e1_M_3, e1_F_3, e1_M_4, e1_F_4, b6,
                                            b6_F_1, b6_F_2, b6_F_3, b6_F_4, b6_M_1, b6_M_2, 
                                            b6_M_3, b6_M_4]
        e1_maior_que_b6_dependencias.forEach(
            (domNode) => {
            
                domNode.addEventListener('change', () => {
                    e1_maior_que_b6(e1, e1_M_1, e1_F_1, e1_M_2, e1_F_2, e1_M_3, e1_F_3, e1_M_4, e1_F_4, b6)
                })
            }
        )

        e2_maior_que_b6_dependencias = [e2, e2_M_1, e2_F_1, e2_M_2, e2_F_2, e2_M_3, e2_F_3, e2_M_4, e2_F_4, b6,
                                            b6_F_1, b6_F_2, b6_F_3, b6_F_4, b6_M_1, b6_M_2, 
                                            b6_M_3, b6_M_4]
        e2_maior_que_b6_dependencias.forEach(
            (domNode) => {
            
                domNode.addEventListener('change', () => {
                    e2_maior_que_b6(e2, e2_M_1, e2_F_1, e2_M_2, e2_F_2, e2_M_3, e2_F_3, e2_M_4, e2_F_4, b6)
                })
            }
        )

        g1_maior_que_b6_dependencias = [g1, g1_M_1, g1_F_1, g1_M_2, g1_F_2, g1_M_3, g1_F_3, g1_M_4, g1_F_4, b6,
                                            b6_F_1, b6_F_2, b6_F_3, b6_F_4, b6_M_1, b6_M_2, 
                                            b6_M_3, b6_M_4]
        g1_maior_que_b6_dependencias.forEach(
            (domNode) => {
            
                domNode.addEventListener('change', () => {
                    g1_maior_que_b6(g1, g1_M_1, g1_F_1, g1_M_2, g1_F_2, g1_M_3, g1_F_3, g1_M_4, g1_F_4, b6)
                })
            }
        )

         i1_maior_que_b6_dependencias = [i1, i1_M_1, i1_F_1, i1_M_2, i1_F_2, i1_M_3, i1_F_3, i1_M_4, i1_F_4, b6,
                                            b6_F_1, b6_F_2, b6_F_3, b6_F_4, b6_M_1, b6_M_2, 
                                            b6_M_3, b6_M_4]
        i1_maior_que_b6_dependencias.forEach(
            (domNode) => {
            
                domNode.addEventListener('change', () => {
                    i1_maior_que_b6(i1, i1_M_1, i1_F_1, i1_M_2, i1_F_2, i1_M_3, i1_F_3, i1_M_4, i1_F_4, b6)
                })
            }
        )

        j5_j6_maior_que_j4_dependencias = [j4, j4_M_1, j4_F_1, j5, j5_M_1, j5_F_1, j6, j6_M_1, j6_F_1]

        j5_j6_maior_que_j4_dependencias.forEach(
            domNode =>
            {
                domNode.addEventListener('change', () => {
                    j5_j6_maior_que_j4(j4, j4_M_1, j4_F_1, j5, j5_M_1, j5_F_1, j6, j6_M_1, j6_F_1)
                })
            }
        )

    
    }
)
function c1_maior_que_b6(c1, c1_M_1, c1_F_1, c1_M_2, c1_F_2, c1_M_3, c1_F_3, b6) {

        if ((Number(c1_M_1.value) + Number(c1_F_1.value) + Number(c1_M_2.value) + Number(c1_F_2.value) + Number(c1_M_3.value) + Number(c1_F_3.value)) > Number(b6.value)) {
            alert(regras['C1'])

            let dependencies =[c1,c1_M_1, c1_F_1, c1_M_2, c1_F_2, c1_M_3, c1_F_3] 
            dependencies.forEach(
                (domNode) =>{
                     domNode.style.color = 'red'
                    }
            )
        }
    }

function c2_maior_que_b6(c2, c2_M_1, c2_F_1, c2_M_2, c2_F_2, c2_M_3, c2_F_3, b6){

        if ((Number(c2_M_1.value) + Number(c2_F_1.value) + Number(c2_M_2.value) + Number(c2_F_2.value) + Number(c2_M_3.value) + Number(c2_F_3.value) > Number(b6.value))){
            alert(regras['C2'])

            let dependencies =[c2, c2_M_1, c2_F_1, c2_M_2, c2_F_2, c2_M_3, c2_F_3, b6]
            dependencies.forEach(
                (domNode) => {domNode.style.color = 'red'}
            )
        }
    }

function c3_maior_que_b6(c3, c3_M_1, c3_F_1, c3_M_2, c3_F_2, c3_M_3, c3_F_3, b6){

        if ((Number(c3_M_1.value) + Number(c3_F_1.value) + Number(c3_M_2.value) + Number(c3_F_2.value) + Number(c3_M_3.value) + Number(c3_F_3.value) > Number(b6.value))){
            alert(regras['C3'])

            let dependencies =[c3, c3_M_1, c3_F_1, c3_M_2, c3_F_2, c3_M_3, c3_F_3, b6]
            dependencies.forEach(
                (domNode) => {domNode.style.color = 'red'}
            )
        }
    }

function c4_maior_que_b6(c4, c4_M_1, c4_F_1, c4_M_2, c4_F_2, c4_M_3, c4_F_3, b6){

        if ((Number(c4_M_1.value) + Number(c4_F_1.value) + Number(c4_M_2.value) + Number(c4_F_2.value) + Number(c4_M_3.value) + Number(c4_F_3.value) > Number(b6.value))){
            alert(regras['C4'])

            let dependencies =[c4, c4_M_1, c4_F_1, c4_M_2, c4_F_2, c4_M_3, c4_F_3, b6]
            dependencies.forEach(
                (domNode) => {domNode.style.color = 'red'}
            )
        }
    }

function c5_maior_que_b6(c5, c5_M_1, c5_F_1, c5_M_2, c5_F_2, b6){

        if ((Number(c5_M_1.value) + Number(c5_F_1.value) + Number(c5_M_2.value) + Number(c5_F_2.value) > Number(b6.value))){
            alert(regras['C5'])

            let dependencies =[c5, c5_M_1, c5_F_1, c5_M_2, c5_F_2, b6]
            dependencies.forEach(
                (domNode) => {domNode.style.color = 'red'}
            )
        }
    }

function d1_maior_que_b6(d1, d1_M_1, d1_F_1, b6){

        if ((Number(d1_M_1.value) + Number(d1_F_1.value) > Number(b6.value))){
            alert(regras['D1'])

            let dependencies =[d1, d1_M_1, d1_F_1, b6]
            dependencies.forEach(
                (domNode) => {domNode.style.color = 'red'}
            )
        }
    }

function d2_maior_que_b6(d2, d2_M_1, d2_F_1, b6){

        if ((Number(d2_M_1.value) + Number(d2_F_1.value) > Number(b6.value))){
            alert(regras['D2'])

            let dependencies =[d2, d2_M_1, d2_F_1, b6]
            dependencies.forEach(
                (domNode) => {domNode.style.color = 'red'}
            )
        }
    }

function e1_maior_que_b6(e1, e1_M_1, e1_F_1, e1_M_2, e1_F_2, e1_M_3, e1_F_3, e1_M_4, e1_F_4, b6){

        if ((Number(e1_M_1.value) + Number(e1_F_1.value) + Number(e1_M_2.value) + Number(e1_F_2.value) + Number(e1_M_3.value) + Number(e1_F_3.value) + Number(e1_M_4.value) + Number(e1_F_4.value) > Number(b6.value))){
            alert(regras['E1'])

            let dependencies =[e1, e1_M_1, e1_F_1, e1_M_2, e1_F_2, e1_M_3, e1_F_3, e1_M_4, e1_F_4, b6]
            dependencies.forEach(
                (domNode) => {domNode.style.color = 'red'}
            )
        }
    }

function e2_maior_que_b6(e2, e2_M_1, e2_F_1, e2_M_2, e2_F_2, e2_M_3, e2_F_3, e2_M_4, e2_F_4, b6){

        if ((Number(e2_M_1.value) + Number(e2_F_1.value) + Number(e2_M_2.value) + Number(e2_F_2.value) + Number(e2_M_3.value) + Number(e2_F_3.value) + Number(e2_M_4.value) + Number(e2_F_4.value) > Number(b6.value))){
            alert(regras['E2'])

            let dependencies =[e2, e2_M_1, e2_F_1, e2_M_2, e2_F_2, e2_M_3, e2_F_3, e2_M_4, e2_F_4, b6]
            dependencies.forEach(
                (domNode) => {domNode.style.color = 'red'}
            )
        }
    }

function g1_maior_que_b6(g1, g1_M_1, g1_F_1, g1_M_2, g1_F_2, g1_M_3, g1_F_3, g1_M_4, g1_F_4, b6){

        if ((Number(g1_M_1.value) + Number(g1_F_1.value) + Number(g1_M_2.value) + Number(g1_F_2.value) + Number(g1_M_3.value) + Number(g1_F_3.value) + Number(g1_M_4.value) + Number(g1_F_4.value) > Number(b6.value))){
            alert(regras['G1'])

            let dependencies =[g1, g1_M_1, g1_F_1, g1_M_2, g1_F_2, g1_M_3, g1_F_3, g1_M_4, g1_F_4, b6]
            dependencies.forEach(
                (domNode) => {domNode.style.color = 'red'}
            )
        }
    }

function i1_maior_que_b6(i1, i1_M_1, i1_F_1, i1_M_2, i1_F_2, i1_M_3, i1_F_3, i1_M_4, i1_F_4, b6){

        if ((Number(i1_M_1.value) + Number(i1_F_1.value) + Number(i1_M_2.value) + Number(i1_F_2.value) + Number(i1_M_3.value) + Number(i1_F_3.value) + Number(i1_M_4.value) + Number(i1_F_4.value) > Number(b6.value))){
            alert(regras['I1'])

            let dependencies =[i1, i1_M_1, i1_F_1, i1_M_2, i1_F_2, i1_M_3, i1_F_3, i1_M_4, i1_F_4, b6]
            dependencies.forEach(
                (domNode) => {domNode.style.color = 'red'}
            )
        }
    }

function j5_j6_maior_que_j4(j4, j4_M_1, j4_F_1, j5, j5_M_1, j5_F_1, j6, j6_M_1, j6_F_1)
{
    if(Number(j4.value) < (Number(j5.value) + Number(j6.value)))
    {
        alert(regras['J4'])
        let dependencies =[j4, j4_M_1, j4_F_1, j5, j5_M_1, j5_F_1, j6, j6_M_1, j6_F_1]
        dependencies.forEach(
            (domNode) => {domNode.style.color = 'red'}
        )   
    }
}
