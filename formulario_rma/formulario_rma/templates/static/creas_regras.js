class Form {
    constructor(
        A1,
        A2,
        B1,
        B2,
        B3,
        B4,
        B5,
        B7,
        B6_T,
        B6_M_1,
        B6_M_2,
        B6_M_3,
        B6_M_4,
        B6_F_1,
        B6_F_2,
        B6_F_3,
        B6_F_4,
        C1_T,
        C1_M_1,
        C1_M_2,
        C1_M_3,
        C1_F_1,
        C1_F_2,
        C1_F_3,
        C2_T,
        C2_M_1,
        C2_M_2,
        C2_M_3,
        C2_F_1,
        C2_F_2,
        C2_F_3,
        C3_T,
        C3_M_1,
        C3_M_2,
        C3_M_3,
        C3_F_1,
        C3_F_2,
        C3_F_3,
        C4_T,
        C4_M_1,
        C4_M_2,
        C4_M_3,
        C4_F_1,
        C4_F_2,
        C4_F_3,
        C5_T,
        C5_M_1,
        C5_M_2,
        C5_F_1,
        C5_F_2,
        D1_T,
        D1_M_1,
        D1_F_1,
        D2_T,
        D2_M_1,
        D2_F_1,
        E1_T,
        E1_M_1,
        E1_M_2,
        E1_M_3,
        E1_M_4,
        E1_F_1,
        E1_F_2,
        E1_F_3,
        E1_F_4,
        E2_T,
        E2_M_1,
        E2_M_2,
        E2_M_3,
        E2_M_4,
        E2_F_1,
        E2_F_2,
        E2_F_3,
        E2_F_4,
        F1,
        G1_T,
        G1_M_1,
        G1_M_2,
        G1_M_3,
        G1_M_4,
        G1_F_1,
        G1_F_2,
        G1_F_3,
        G1_F_4,
        H1,
        I1_T,
        I1_M_1,
        I1_M_2,
        I1_M_3,
        I1_M_4,
        I1_F_1,
        I1_F_2,
        I1_F_3,
        I1_F_4,
        M1,
        M2,
        M3,
        M4,
        J1,
        J2,
        J3,
        J4_T,
        J4_M_1,
        J4_F_1,
        J5_T,
        J5_M_1,
        J5_F_1,
        J6_T,
        J6_M_1,
        J6_F_1,
        K1_T,
        K1_M_1,
        K1_M_2,
        K1_M_3,
        K1_M_4,
        K1_F_1,
        K1_F_2,
        K1_F_3,
        K1_F_4,
        K2,
        K3,
        K4,
        K5,
        K6,
        L1
    ) {
        this.A1 = A1
        this.A2 = A2
        this.B1 = B1
        this.B2 = B2
        this.B3 = B3
        this.B4 = B4
        this.B5 = B5
        this.B7 = B7
        this.B6_T = B6_T
        this.B6_M_1 = B6_M_1
        this.B6_M_2 = B6_M_2
        this.B6_M_3 = B6_M_3
        this.B6_M_4 = B6_M_4
        this.B6_F_1 = B6_F_1
        this.B6_F_2 = B6_F_2
        this.B6_F_3 = B6_F_3
        this.B6_F_4 = B6_F_4
        this.C1_T = C1_T
        this.C1_M_1 = C1_M_1
        this.C1_M_2 = C1_M_2
        this.C1_M_3 = C1_M_3
        this.C1_F_1 = C1_F_1
        this.C1_F_2 = C1_F_2
        this.C1_F_3 = C1_F_3
        this.C2_T = C2_T
        this.C2_M_1 = C2_M_1
        this.C2_M_2 = C2_M_2
        this.C2_M_3 = C2_M_3
        this.C2_F_1 = C2_F_1
        this.C2_F_2 = C2_F_2
        this.C2_F_3 = C2_F_3
        this.C3_T = C3_T
        this.C3_M_1 = C3_M_1
        this.C3_M_2 = C3_M_2
        this.C3_M_3 = C3_M_3
        this.C3_F_1 = C3_F_1
        this.C3_F_2 = C3_F_2
        this.C3_F_3 = C3_F_3
        this.C4_T = C4_T
        this.C4_M_1 = C4_M_1
        this.C4_M_2 = C4_M_2
        this.C4_M_3 = C4_M_3
        this.C4_F_1 = C4_F_1
        this.C4_F_2 = C4_F_2
        this.C4_F_3 = C4_F_3
        this.C5_T = C5_T
        this.C5_M_1 = C5_M_1
        this.C5_M_2 = C5_M_2
        this.C5_F_1 = C5_F_1
        this.C5_F_2 = C5_F_2
        this.D1_T = D1_T
        this.D1_M_1 = D1_M_1
        this.D1_F_1 = D1_F_1
        this.D2_T = D2_T
        this.D2_M_1 = D2_M_1
        this.D2_F_1 = D2_F_1
        this.E1_T = E1_T
        this.E1_M_1 = E1_M_1
        this.E1_M_2 = E1_M_2
        this.E1_M_3 = E1_M_3
        this.E1_M_4 = E1_M_4
        this.E1_F_1 = E1_F_1
        this.E1_F_2 = E1_F_2
        this.E1_F_3 = E1_F_3
        this.E1_F_4 = E1_F_4
        this.E2_T = E2_T
        this.E2_M_1 = E2_M_1
        this.E2_M_2 = E2_M_2
        this.E2_M_3 = E2_M_3
        this.E2_M_4 = E2_M_4
        this.E2_F_1 = E2_F_1
        this.E2_F_2 = E2_F_2
        this.E2_F_3 = E2_F_3
        this.E2_F_4 = E2_F_4
        this.F1 = F1
        this.G1_T = G1_T
        this.G1_M_1 = G1_M_1
        this.G1_M_2 = G1_M_2
        this.G1_M_3 = G1_M_3
        this.G1_M_4 = G1_M_4
        this.G1_F_1 = G1_F_1
        this.G1_F_2 = G1_F_2
        this.G1_F_3 = G1_F_3
        this.G1_F_4 = G1_F_4
        this.H1 = H1
        this.I1_T = I1_T
        this.I1_M_1 = I1_M_1
        this.I1_M_2 = I1_M_2
        this.I1_M_3 = I1_M_3
        this.I1_M_4 = I1_M_4
        this.I1_F_1 = I1_F_1
        this.I1_F_2 = I1_F_2
        this.I1_F_3 = I1_F_3
        this.I1_F_4 = I1_F_4
        this.M1 = M1
        this.M2 = M2
        this.M3 = M3
        this.M4 = M4
        this.J1 = J1
        this.J2 = J2
        this.J3 = J3
        this.J4_T = J4_T
        this.J4_M_1 = J4_M_1
        this.J4_F_1 = J4_F_1
        this.J5_T = J5_T
        this.J5_M_1 = J5_M_1
        this.J5_F_1 = J5_F_1
        this.J6_T = J6_T
        this.J6_M_1 = J6_M_1
        this.J6_F_1 = J6_F_1
        this.K1_T = K1_T
        this.K1_M_1 = K1_M_1
        this.K1_M_2 = K1_M_2
        this.K1_M_3 = K1_M_3
        this.K1_M_4 = K1_M_4
        this.K1_F_1 = K1_F_1
        this.K1_F_2 = K1_F_2
        this.K1_F_3 = K1_F_3
        this.K1_F_4 = K1_F_4
        this.K2 = K2
        this.K3 = K3
        this.K4 = K4
        this.K5 = K5
        this.K6 = K6
        this.L1 = L1
    }
}

class FormAdapter {
    static fromDomainJson(form_data_json) {
        const A1 = form_data_json.A1
        const A2 = form_data_json.A2
        const B1 = form_data_json.B1
        const B2 = form_data_json.B2
        const B3 = form_data_json.B3
        const B4 = form_data_json.B4
        const B5 = form_data_json.B5
        const B7 = form_data_json.B7
        const B6_T = form_data_json.B6_T
        const B6_M_1 = form_data_json.B6_M_1
        const B6_M_2 = form_data_json.B6_M_2
        const B6_M_3 = form_data_json.B6_M_3
        const B6_M_4 = form_data_json.B6_M_4
        const B6_F_1 = form_data_json.B6_F_1
        const B6_F_2 = form_data_json.B6_F_2
        const B6_F_3 = form_data_json.B6_F_3
        const B6_F_4 = form_data_json.B6_F_4
        const C1_T = form_data_json.C1_T
        const C1_M_1 = form_data_json.C1_M_1
        const C1_M_2 = form_data_json.C1_M_2
        const C1_M_3 = form_data_json.C1_M_3
        const C1_F_1 = form_data_json.C1_F_1
        const C1_F_2 = form_data_json.C1_F_2
        const C1_F_3 = form_data_json.C1_F_3
        const C2_T = form_data_json.C2_T
        const C2_M_1 = form_data_json.C2_M_1
        const C2_M_2 = form_data_json.C2_M_2
        const C2_M_3 = form_data_json.C2_M_3
        const C2_F_1 = form_data_json.C2_F_1
        const C2_F_2 = form_data_json.C2_F_2
        const C2_F_3 = form_data_json.C2_F_3
        const C3_T = form_data_json.C3_T
        const C3_M_1 = form_data_json.C3_M_1
        const C3_M_2 = form_data_json.C3_M_2
        const C3_M_3 = form_data_json.C3_M_3
        const C3_F_1 = form_data_json.C3_F_1
        const C3_F_2 = form_data_json.C3_F_2
        const C3_F_3 = form_data_json.C3_F_3
        const C4_T = form_data_json.C4_T
        const C4_M_1 = form_data_json.C4_M_1
        const C4_M_2 = form_data_json.C4_M_2
        const C4_M_3 = form_data_json.C4_M_3
        const C4_F_1 = form_data_json.C4_F_1
        const C4_F_2 = form_data_json.C4_F_2
        const C4_F_3 = form_data_json.C4_F_3
        const C5_T = form_data_json.C5_T
        const C5_M_1 = form_data_json.C5_M_1
        const C5_M_2 = form_data_json.C5_M_2
        const C5_F_1 = form_data_json.C5_F_1
        const C5_F_2 = form_data_json.C5_F_2
        const D1_T = form_data_json.D1_T
        const D1_M_1 = form_data_json.D1_M_1
        const D1_F_1 = form_data_json.D1_F_1
        const D2_T = form_data_json.D2_T
        const D2_M_1 = form_data_json.D2_M_1
        const D2_F_1 = form_data_json.D2_F_1
        const E1_T = form_data_json.E1_T
        const E1_M_1 = form_data_json.E1_M_1
        const E1_M_2 = form_data_json.E1_M_2
        const E1_M_3 = form_data_json.E1_M_3
        const E1_M_4 = form_data_json.E1_M_4
        const E1_F_1 = form_data_json.E1_F_1
        const E1_F_2 = form_data_json.E1_F_2
        const E1_F_3 = form_data_json.E1_F_3
        const E1_F_4 = form_data_json.E1_F_4
        const E2_T = form_data_json.E2_T
        const E2_M_1 = form_data_json.E2_M_1
        const E2_M_2 = form_data_json.E2_M_2
        const E2_M_3 = form_data_json.E2_M_3
        const E2_M_4 = form_data_json.E2_M_4
        const E2_F_1 = form_data_json.E2_F_1
        const E2_F_2 = form_data_json.E2_F_2
        const E2_F_3 = form_data_json.E2_F_3
        const E2_F_4 = form_data_json.E2_F_4
        const F1 = form_data_json.F1
        const G1_T = form_data_json.G1_T
        const G1_M_1 = form_data_json.G1_M_1
        const G1_M_2 = form_data_json.G1_M_2
        const G1_M_3 = form_data_json.G1_M_3
        const G1_M_4 = form_data_json.G1_M_4
        const G1_F_1 = form_data_json.G1_F_1
        const G1_F_2 = form_data_json.G1_F_2
        const G1_F_3 = form_data_json.G1_F_3
        const G1_F_4 = form_data_json.G1_F_4
        const H1 = form_data_json.H1
        const I1_T = form_data_json.I1_T
        const I1_M_1 = form_data_json.I1_M_1
        const I1_M_2 = form_data_json.I1_M_2
        const I1_M_3 = form_data_json.I1_M_3
        const I1_M_4 = form_data_json.I1_M_4
        const I1_F_1 = form_data_json.I1_F_1
        const I1_F_2 = form_data_json.I1_F_2
        const I1_F_3 = form_data_json.I1_F_3
        const I1_F_4 = form_data_json.I1_F_4
        const M1 = form_data_json.M1
        const M2 = form_data_json.M2
        const M3 = form_data_json.M3
        const M4 = form_data_json.M4
        const J1 = form_data_json.J1
        const J2 = form_data_json.J2
        const J3 = form_data_json.J3
        const J4_T = form_data_json.J4_T
        const J4_M_1 = form_data_json.J4_M_1
        const J4_F_1 = form_data_json.J4_F_1
        const J5_T = form_data_json.J5_T
        const J5_M_1 = form_data_json.J5_M_1
        const J5_F_1 = form_data_json.J5_F_1
        const J6_T = form_data_json.J6_T
        const J6_M_1 = form_data_json.J6_M_1
        const J6_F_1 = form_data_json.J6_F_1
        const K1_T = form_data_json.K1_T
        const K1_M_1 = form_data_json.K1_M_1
        const K1_M_2 = form_data_json.K1_M_2
        const K1_M_3 = form_data_json.K1_M_3
        const K1_M_4 = form_data_json.K1_M_4
        const K1_F_1 = form_data_json.K1_F_1
        const K1_F_2 = form_data_json.K1_F_2
        const K1_F_3 = form_data_json.K1_F_3
        const K1_F_4 = form_data_json.K1_F_4
        const K2 = form_data_json.K2
        const K3 = form_data_json.K3
        const K4 = form_data_json.K4
        const K5 = form_data_json.K5
        const K6 = form_data_json.K6
        const L1 = form_data_json.L1


        return new Form(A1,
            A2,
            B1,
            B2,
            B3,
            B4,
            B5,
            B7,
            B6_T,
            B6_M_1,
            B6_M_2,
            B6_M_3,
            B6_M_4,
            B6_F_1,
            B6_F_2,
            B6_F_3,
            B6_F_4,
            C1_T,
            C1_M_1,
            C1_M_2,
            C1_M_3,
            C1_F_1,
            C1_F_2,
            C1_F_3,
            C2_T,
            C2_M_1,
            C2_M_2,
            C2_M_3,
            C2_F_1,
            C2_F_2,
            C2_F_3,
            C3_T,
            C3_M_1,
            C3_M_2,
            C3_M_3,
            C3_F_1,
            C3_F_2,
            C3_F_3,
            C4_T,
            C4_M_1,
            C4_M_2,
            C4_M_3,
            C4_F_1,
            C4_F_2,
            C4_F_3,
            C5_T,
            C5_M_1,
            C5_M_2,
            C5_F_1,
            C5_F_2,
            D1_T,
            D1_M_1,
            D1_F_1,
            D2_T,
            D2_M_1,
            D2_F_1,
            E1_T,
            E1_M_1,
            E1_M_2,
            E1_M_3,
            E1_M_4,
            E1_F_1,
            E1_F_2,
            E1_F_3,
            E1_F_4,
            E2_T,
            E2_M_1,
            E2_M_2,
            E2_M_3,
            E2_M_4,
            E2_F_1,
            E2_F_2,
            E2_F_3,
            E2_F_4,
            F1,
            G1_T,
            G1_M_1,
            G1_M_2,
            G1_M_3,
            G1_M_4,
            G1_F_1,
            G1_F_2,
            G1_F_3,
            G1_F_4,
            H1,
            I1_T,
            I1_M_1,
            I1_M_2,
            I1_M_3,
            I1_M_4,
            I1_F_1,
            I1_F_2,
            I1_F_3,
            I1_F_4,
            M1,
            M2,
            M3,
            M4,
            J1,
            J2,
            J3,
            J4_T,
            J4_M_1,
            J4_F_1,
            J5_T,
            J5_M_1,
            J5_F_1,
            J6_T,
            J6_M_1,
            J6_F_1,
            K1_T,
            K1_M_1,
            K1_M_2,
            K1_M_3,
            K1_M_4,
            K1_F_1,
            K1_F_2,
            K1_F_3,
            K1_F_4,
            K2,
            K3,
            K4,
            K5,
            K6,
            L1

        )
    }
}

class FormPresenter {
    static fromForm(form) {
        let A1 = document.getElementById('A1')
        let A2 = document.getElementById('A2')
        let B1 = document.getElementById('B1')
        let B2 = document.getElementById('B2')
        let B3 = document.getElementById('B3')
        let B4 = document.getElementById('B4')
        let B5 = document.getElementById('B5')
        let B7 = document.getElementById('B7')
        let B6_T = document.getElementById('B6_T')
        let B6_M_1 = document.getElementById('B6_M_1')
        let B6_M_2 = document.getElementById('B6_M_2')
        let B6_M_3 = document.getElementById('B6_M_3')
        let B6_M_4 = document.getElementById('B6_M_4')
        let B6_F_1 = document.getElementById('B6_F_1')
        let B6_F_2 = document.getElementById('B6_F_2')
        let B6_F_3 = document.getElementById('B6_F_3')
        let B6_F_4 = document.getElementById('B6_F_4')
        let C1_T = document.getElementById('C1_T')
        let C1_M_1 = document.getElementById('C1_M_1')
        let C1_M_2 = document.getElementById('C1_M_2')
        let C1_M_3 = document.getElementById('C1_M_3')
        let C1_F_1 = document.getElementById('C1_F_1')
        let C1_F_2 = document.getElementById('C1_F_2')
        let C1_F_3 = document.getElementById('C1_F_3')
        let C2_T = document.getElementById('C2_T')
        let C2_M_1 = document.getElementById('C2_M_1')
        let C2_M_2 = document.getElementById('C2_M_2')
        let C2_M_3 = document.getElementById('C2_M_3')
        let C2_F_1 = document.getElementById('C2_F_1')
        let C2_F_2 = document.getElementById('C2_F_2')
        let C2_F_3 = document.getElementById('C2_F_3')
        let C3_T = document.getElementById('C3_T')
        let C3_M_1 = document.getElementById('C3_M_1')
        let C3_M_2 = document.getElementById('C3_M_2')
        let C3_M_3 = document.getElementById('C3_M_3')
        let C3_F_1 = document.getElementById('C3_F_1')
        let C3_F_2 = document.getElementById('C3_F_2')
        let C3_F_3 = document.getElementById('C3_F_3')
        let C4_T = document.getElementById('C4_T')
        let C4_M_1 = document.getElementById('C4_M_1')
        let C4_M_2 = document.getElementById('C4_M_2')
        let C4_M_3 = document.getElementById('C4_M_3')
        let C4_F_1 = document.getElementById('C4_F_1')
        let C4_F_2 = document.getElementById('C4_F_2')
        let C4_F_3 = document.getElementById('C4_F_3')
        let C5_T = document.getElementById('C5_T')
        let C5_M_1 = document.getElementById('C5_M_1')
        let C5_M_2 = document.getElementById('C5_M_2')
        let C5_F_1 = document.getElementById('C5_F_1')
        let C5_F_2 = document.getElementById('C5_F_2')
        let D1_T = document.getElementById('D1_T')
        let D1_M_1 = document.getElementById('D1_M_1')
        let D1_F_1 = document.getElementById('D1_F_1')
        let D2_T = document.getElementById('D2_T')
        let D2_M_1 = document.getElementById('D2_M_1')
        let D2_F_1 = document.getElementById('D2_F_1')
        let E1_T = document.getElementById('E1_T')
        let E1_M_1 = document.getElementById('E1_M_1')
        let E1_M_2 = document.getElementById('E1_M_2')
        let E1_M_3 = document.getElementById('E1_M_3')
        let E1_M_4 = document.getElementById('E1_M_4')
        let E1_F_1 = document.getElementById('E1_F_1')
        let E1_F_2 = document.getElementById('E1_F_2')
        let E1_F_3 = document.getElementById('E1_F_3')
        let E1_F_4 = document.getElementById('E1_F_4')
        let E2_T = document.getElementById('E2_T')
        let E2_M_1 = document.getElementById('E2_M_1')
        let E2_M_2 = document.getElementById('E2_M_2')
        let E2_M_3 = document.getElementById('E2_M_3')
        let E2_M_4 = document.getElementById('E2_M_4')
        let E2_F_1 = document.getElementById('E2_F_1')
        let E2_F_2 = document.getElementById('E2_F_2')
        let E2_F_3 = document.getElementById('E2_F_3')
        let E2_F_4 = document.getElementById('E2_F_4')
        let F1 = document.getElementById('F1')
        let G1_T = document.getElementById('G1_T')
        let G1_M_1 = document.getElementById('G1_M_1')
        let G1_M_2 = document.getElementById('G1_M_2')
        let G1_M_3 = document.getElementById('G1_M_3')
        let G1_M_4 = document.getElementById('G1_M_4')
        let G1_F_1 = document.getElementById('G1_F_1')
        let G1_F_2 = document.getElementById('G1_F_2')
        let G1_F_3 = document.getElementById('G1_F_3')
        let G1_F_4 = document.getElementById('G1_F_4')
        let H1 = document.getElementById('H1')
        let I1_T = document.getElementById('I1_T')
        let I1_M_1 = document.getElementById('I1_M_1')
        let I1_M_2 = document.getElementById('I1_M_2')
        let I1_M_3 = document.getElementById('I1_M_3')
        let I1_M_4 = document.getElementById('I1_M_4')
        let I1_F_1 = document.getElementById('I1_F_1')
        let I1_F_2 = document.getElementById('I1_F_2')
        let I1_F_3 = document.getElementById('I1_F_3')
        let I1_F_4 = document.getElementById('I1_F_4')
        let M1 = document.getElementById('M1')
        let M2 = document.getElementById('M2')
        let M3 = document.getElementById('M3')
        let M4 = document.getElementById('M4')
        let J1 = document.getElementById('J1')
        let J2 = document.getElementById('J2')
        let J3 = document.getElementById('J3')
        let J4_T = document.getElementById('J4_T')
        let J4_M_1 = document.getElementById('J4_M_1')
        let J4_F_1 = document.getElementById('J4_F_1')
        let J5_T = document.getElementById('J5_T')
        let J5_M_1 = document.getElementById('J5_M_1')
        let J5_F_1 = document.getElementById('J5_F_1')
        let J6_T = document.getElementById('J6_T')
        let J6_M_1 = document.getElementById('J6_M_1')
        let J6_F_1 = document.getElementById('J6_F_1')
        let K1_T = document.getElementById('K1_T')
        let K1_M_1 = document.getElementById('K1_M_1')
        let K1_M_2 = document.getElementById('K1_M_2')
        let K1_M_3 = document.getElementById('K1_M_3')
        let K1_M_4 = document.getElementById('K1_M_4')
        let K1_F_1 = document.getElementById('K1_F_1')
        let K1_F_2 = document.getElementById('K1_F_2')
        let K1_F_3 = document.getElementById('K1_F_3')
        let K1_F_4 = document.getElementById('K1_F_4')
        let K2 = document.getElementById('K2')
        let K3 = document.getElementById('K3')
        let K4 = document.getElementById('K4')
        let K5 = document.getElementById('K5')
        let K6 = document.getElementById('K6')
        let L1 = document.getElementById('L1')


        A1.value = form.A1
        A2.value = form.A2
        B1.value = form.B1
        B2.value = form.B2
        B3.value = form.B3
        B4.value = form.B4
        B5.value = form.B5
        B7.value = form.B7
        B6_T.value = form.B6_T
        B6_M_1.value = form.B6_M_1
        B6_M_2.value = form.B6_M_2
        B6_M_3.value = form.B6_M_3
        B6_M_4.value = form.B6_M_4
        B6_F_1.value = form.B6_F_1
        B6_F_2.value = form.B6_F_2
        B6_F_3.value = form.B6_F_3
        B6_F_4.value = form.B6_F_4
        C1_T.value = form.C1_T
        C1_M_1.value = form.C1_M_1
        C1_M_2.value = form.C1_M_2
        C1_M_3.value = form.C1_M_3
        C1_F_1.value = form.C1_F_1
        C1_F_2.value = form.C1_F_2
        C1_F_3.value = form.C1_F_3
        C2_T.value = form.C2_T
        C2_M_1.value = form.C2_M_1
        C2_M_2.value = form.C2_M_2
        C2_M_3.value = form.C2_M_3
        C2_F_1.value = form.C2_F_1
        C2_F_2.value = form.C2_F_2
        C2_F_3.value = form.C2_F_3
        C3_T.value = form.C3_T
        C3_M_1.value = form.C3_M_1
        C3_M_2.value = form.C3_M_2
        C3_M_3.value = form.C3_M_3
        C3_F_1.value = form.C3_F_1
        C3_F_2.value = form.C3_F_2
        C3_F_3.value = form.C3_F_3
        C4_T.value = form.C4_T
        C4_M_1.value = form.C4_M_1
        C4_M_2.value = form.C4_M_2
        C4_M_3.value = form.C4_M_3
        C4_F_1.value = form.C4_F_1
        C4_F_2.value = form.C4_F_2
        C4_F_3.value = form.C4_F_3
        C5_T.value = form.C5_T
        C5_M_1.value = form.C5_M_1
        C5_M_2.value = form.C5_M_2
        C5_F_1.value = form.C5_F_1
        C5_F_2.value = form.C5_F_2
        D1_T.value = form.D1_T
        D1_M_1.value = form.D1_M_1
        D1_F_1.value = form.D1_F_1
        D2_T.value = form.D2_T
        D2_M_1.value = form.D2_M_1
        D2_F_1.value = form.D2_F_1
        E1_T.value = form.E1_T
        E1_M_1.value = form.E1_M_1
        E1_M_2.value = form.E1_M_2
        E1_M_3.value = form.E1_M_3
        E1_M_4.value = form.E1_M_4
        E1_F_1.value = form.E1_F_1
        E1_F_2.value = form.E1_F_2
        E1_F_3.value = form.E1_F_3
        E1_F_4.value = form.E1_F_4
        E2_T.value = form.E2_T
        E2_M_1.value = form.E2_M_1
        E2_M_2.value = form.E2_M_2
        E2_M_3.value = form.E2_M_3
        E2_M_4.value = form.E2_M_4
        E2_F_1.value = form.E2_F_1
        E2_F_2.value = form.E2_F_2
        E2_F_3.value = form.E2_F_3
        E2_F_4.value = form.E2_F_4
        F1.value = form.F1
        G1_T.value = form.G1_T
        G1_M_1.value = form.G1_M_1
        G1_M_2.value = form.G1_M_2
        G1_M_3.value = form.G1_M_3
        G1_M_4.value = form.G1_M_4
        G1_F_1.value = form.G1_F_1
        G1_F_2.value = form.G1_F_2
        G1_F_3.value = form.G1_F_3
        G1_F_4.value = form.G1_F_4
        H1.value = form.H1
        I1_T.value = form.I1_T
        I1_M_1.value = form.I1_M_1
        I1_M_2.value = form.I1_M_2
        I1_M_3.value = form.I1_M_3
        I1_M_4.value = form.I1_M_4
        I1_F_1.value = form.I1_F_1
        I1_F_2.value = form.I1_F_2
        I1_F_3.value = form.I1_F_3
        I1_F_4.value = form.I1_F_4
        M1.value = form.M1
        M2.value = form.M2
        M3.value = form.M3
        M4.value = form.M4
        J1.value = form.J1
        J2.value = form.J2
        J3.value = form.J3
        J4_T.value = form.J4_T
        J4_M_1.value = form.J4_M_1
        J4_F_1.value = form.J4_F_1
        J5_T.value = form.J5_T
        J5_M_1.value = form.J5_M_1
        J5_F_1.value = form.J5_F_1
        J6_T.value = form.J6_T
        J6_M_1.value = form.J6_M_1
        J6_F_1.value = form.J6_F_1

        K1_T.value = form.K1_T

        K1_M_1.value = form.K1_M_1
        K1_M_2.value = form.K1_M_2
        K1_M_3.value = form.K1_M_3
        K1_M_4.value = form.K1_M_4
        K1_F_1.value = form.K1_F_1
        K1_F_2.value = form.K1_F_2
        K1_F_3.value = form.K1_F_3
        K1_F_4.value = form.K1_F_4
        K2.value = form.K2
        K3.value = form.K3
        K4.value = form.K4
        K5.value = form.K5
        K6.value = form.K6
        L1.value = form.L1

        A1.disabled = true
        A2.disabled = true
        B1.disabled = true
        B2.disabled = true
        B3.disabled = true
        B4.disabled = true
        B5.disabled = true
        B7.disabled = true
        B6.disabled = true
        B6_M_1.disabled = true
        B6_F_1.disabled = true
        B6_M_2.disabled = true
        B6_F_2.disabled = true
        B6_M_3.disabled = true
        B6_F_3.disabled = true
        B6_M_4.disabled = true
        B6_F_4.disabled = true

        C1_T.disabled = true
        C1_M_1.disabled = true
        C1_F_1.disabled = true
        C1_M_2.disabled = true
        C1_F_2.disabled = true
        C1_M_3.disabled = true
        C1_F_3.disabled = true

        C2_T.disabled = true
        C2_M_1.disabled = true
        C2_F_1.disabled = true
        C2_M_2.disabled = true
        C2_F_2.disabled = true
        C2_M_3.disabled = true
        C2_F_3.disabled = true

        C3_T.disabled = true
        C3_M_1.disabled = true
        C3_F_1.disabled = true
        C3_M_2.disabled = true
        C3_F_2.disabled = true
        C3_M_3.disabled = true
        C3_F_3.disabled = true

        C4_T.disabled = true
        C4_M_1.disabled = true
        C4_F_1.disabled = true
        C4_M_2.disabled = true
        C4_F_2.disabled = true
        C4_M_3.disabled = true
        C4_F_3.disabled = true

        C5_T.disabled = true
        C5_M_1.disabled = true
        C5_F_1.disabled = true
        C5_M_2.disabled = true
        C5_F_2.disabled = true

        D1.disabled = true
        D1_M_1.disabled = true
        D1_F_1.disabled = true
        D2.disabled = true
        D2_M_1.disabled = true
        D2_F_1.disabled = true

        E1_T.disabled = true
        E1_M_1.disabled = true
        E1_F_1.disabled = true
        E1_M_2.disabled = true
        E1_F_2.disabled = true
        E1_M_3.disabled = true
        E1_F_3.disabled = true
        E1_M_4.disabled = true
        E1_F_4.disabled = true

        E2_T.disabled = true
        E2_M_1.disabled = true
        E2_F_1.disabled = true
        E2_M_2.disabled = true
        E2_F_2.disabled = true
        E2_M_3.disabled = true
        E2_F_3.disabled = true
        E2_M_4.disabled = true
        E2_F_4.disabled = true

        F1.disabled = true

        G1_T.disabled = true
        G1_M_1.disabled = true
        G1_F_1.disabled = true
        G1_M_2.disabled = true
        G1_F_2.disabled = true
        G1_M_3.disabled = true
        G1_F_3.disabled = true
        G1_M_4.disabled = true
        G1_F_4.disabled = true
        H1.disabled = true

        I1_T.disabled = true
        I1_M_1.disabled = true
        I1_F_1.disabled = true
        I1_M_2.disabled = true
        I1_F_2.disabled = true
        I1_M_3.disabled = true
        I1_F_3.disabled = true
        I1_M_4.disabled = true
        I1_F_4.disabled = true

        M1.disabled = true
        M2.disabled = true
        M3.disabled = true
        M4.disabled = true
        J1.disabled = true
        J2.disabled = true
        J3.disabled = true
        J4_T.disabled = true
        j4_M_1.disabled = true
        J4_F_1.disabled = true
        J5.disabled = true
        J5_M_1.disabled = true
        J5_F_1.disabled = true
        J6.disabled = true
        J6_M_1.disabled = true
        J6_F_1.disabled = true

        K1_T.disabled = true
        K1_M_1.disabled = true
        K1_F_1.disabled = true
        K1_M_2.disabled = true
        K1_F_2.disabled = true
        K1_M_3.disabled = true
        K1_F_3.disabled = true
        K1_M_4.disabled = true
        K1_F_4.disabled = true
        K2.disabled = true
        K3.disabled = true
        K4.disabled = true
        K5.disabled = true
        K6.disabled = true
        L1.disabled = true
    }
}


window.addEventListener("load", () => {
    const a2_maior_a1 = new Regra(
        ["A2", "A1"],
        "A2 não pode ser maior que o Valor do Campo A1",
        (a2, a1) => a2 <= a1
    );
    const b1_maior_a2 = new Regra(
        ["B1", "A2"],
        "B1 não pode ser maior que o Valor do Campo A2",
        (b1, a2) => b1 <= a2
    );
    const b2_maior_que_a2 = new Regra(
        ["B2", "A2"],
        "B2 não pode ser maior que o Valor do Campo A2",
        (b2, a2) => b2 <= a2
    );
    const b3_maior_q_a2 = new Regra(
        ["B3", "A2"],
        "B3 não pode ser maior que o Valor do Campo A2",
        (b3, a2) => b3 <= a2
    );

    const b4_maior_que_a2 = new Regra(
        ["B4", "A2"],
        "B4 não pode ser maior que o Valor do Campo A2",
        (b4, a2) => b4 <= a2
    );
    const b5_maior_que_a2 = new Regra(
        ["B5", "A2"],
        "B5 não pode ser maior que o Valor do Campo A2",
        (b5, a2) => b5 <= a2
    );
    const b7_maior_que_a2 = new Regra(
        ["B7", "A2"],
        "B7 não pode ser maior que o Valor do Campo A2",
        (b7, a2) => b7 <= a2
    );

    const b6_maior_que_a2 = new Regra(
        ["B6_T", "A2"],
        "B6 não pode ser maior que o Valor do Campo A2",
        (total_b, a2) => total_b <= a2
    );


    const c1_maior_total_b6 = new Regra(
        ["C1_T", "B6_T"],
        "A soma dos valores informados nos campos C1, não pode ser maior que o Valor do Campo Total B6",
        (total_c1, total_b6) => total_c1 <= total_b6
    );

    const c2_maior_q_total_B6 = new Regra(
        ["C2_T", "B6_T"],
        "A soma dos valores informados nos campos C2, não pode ser maior que o Valor do Campo Total B6",
        (total_c2, total_b6) => total_c2 <= total_b6
    );

    const c3_maior_q_total_B6 = new Regra(
        ["C3_T", "B6_T"],
        "A soma dos valores informados nos campos C3, não pode ser maior que o Valor do Campo Total B6",
        (total_c3, total_b6) => total_c3 <= total_b6
    );

    const c4_maior_q_total_B6 = new Regra(
        ["C4_T", "B6_T"],
        "A soma dos valores informados nos campos C4, não pode ser maior que o Valor do Campo Total B6",
        (total_c4, total_b6) => total_c4 <= total_b6
    );

    const c5_maior_q_total_B6 = new Regra(
        ["C5_T", "B6_T"],
        "A soma dos valores informados nos campos C5, não pode ser maior que o Valor do Campo Total B6",
        (total_c5, total_b6) => total_c5 <= total_b6
    );

    const d1_maior_q_total_B6 = new Regra(
        ["D1_T", "B6_T"],
        "A soma dos valores informados nos campos D1, não pode ser maior que o Valor do Campo Total B6",
        (total_d1, total_b6) => total_d1 <= total_b6
    );

    const d2_maior_q_total_B6 = new Regra(
        ["D2_T", "B6_T"],
        "A soma dos valores informados nos campos D2, não pode ser maior que o Valor do Campo Total B6",
        (total_d2, total_b6) => total_d2 <= total_b6
    );

    const e1_maior_q_total_B6 = new Regra(
        ["E1_T", "B6_T"],
        "A soma dos valores informados nos campos E1, não pode ser maior que o Valor do Campo Total B6",
        (total_e1, total_b6) => total_e1 <= total_b6
    );

    const e2_maior_q_total_B6 = new Regra(
        ["E2_T", "B6_T"],
        "A soma dos valores informados nos campos E2, não pode ser maior que o Valor do Campo Total B6",
        (total_e2, total_b6) => total_e2 <= total_b6
    );

    const f1_maior_q_total_B6 = new Regra(
        ["F1", "B6_T"],
        "F1 não pode ser maior que o Valor do Campo Total B6",
        (f1, total_b6) => f1 <= total_b6
    );
    const g1_maior_q_total_B6 = new Regra(
        ["G1_T", "B6_T"],
        "A soma dos valores informados nos campos G1, não pode ser maior que o Valor do Campo Total B6",
        (total_g1, total_b6) => total_g1 <= total_b6
    );


    const h1_maior_q_total_B6 = new Regra(
        ["H1", "B6_T"],
        "H1 não pode ser maior que o Valor do Campo Total B6",
        (h1, total_b6) => h1 <= total_b6
    );
    const i1_maior_q_total_B6 = new Regra(
        ["I1_T", "B6_T"],
        "A soma dos valores informados nos campos I1, não pode ser maior que o Valor do Campo Total B6",
        (total_i1, total_b6) => total_i1 <= total_b6
    );
    const j2_maior_q_j1 = new Regra(
        ["J2", "J1"],
        "J2 não pode ser maior que o Valor do Campo J1",
        (j2, j1) => j2 <= j1
    );
    const j3_maior_q_j1 = new Regra(
        ["J3", "J1"],
        "J3 não pode ser maior que o Valor do Campo J1",
        (j3, j1) => j3 <= j1
    );




    const j1_maior_j2_e_j3 = new Regra(
        ["J1", "J2", "J3"],
        "A soma dos campos J2 + J3 não pode ser maior que o Valor do Campo J1",
        (j1, j2, j3) => j1 <= j2 + j3
    );
    const j4_maior_j5_e_j6 = new Regra(
        ["J4_T", "J5_T", "J6_T"],
        "A soma dos campos J5 Total + J6 Total não pode ser menor que o Valor do Campo J4 Total",
        (total_j4, total_j5, total_j6) => total_j4 <= total_j5 + total_j6
    );





    const k2_maior_q_k1 = new Regra(
        ["K2", "K1_T"],
        "K2 não pode ser maior que o Valor do Campo K1 Total",
        (k2, total_k1) => k2 <= total_k1
    );
    const k3_maior_q_k1 = new Regra(
        ["K3", "K1_T"],
        "K3 não pode ser maior que o Valor do Campo K1 Total",
        (k3, total_k1) => k3 <= total_k1
    );

    const k4_maior_q_k1 = new Regra(
        ["K4", "K1_T"],
        "K4 não pode ser maior que o Valor do Campo K1 Total",
        (k4, total_k1) => k4 <= total_k1
    );

    const k5_maior_q_k1 = new Regra(
        ["K5", "K1_T"],
        "K5 não pode ser maior que o Valor do Campo K1 Total",
        (k5, total_k1) => k5 <= total_k1
    );

    const k6_maior_q_k1 = new Regra(
        ["K6", "K1_T"],
        "K6 não pode ser maior que o Valor do Campo K1 Total",
        (k6, total_k1) => k6 <= total_k1
    );





    const ruleSet = new RuleSet([
        a2_maior_a1,
        b1_maior_a2,
        b2_maior_que_a2,
        b3_maior_q_a2,
        b4_maior_que_a2,
        b5_maior_que_a2,

        b7_maior_que_a2,

        b6_maior_que_a2,


        c1_maior_total_b6,
        c2_maior_q_total_B6,
        c3_maior_q_total_B6,
        c4_maior_q_total_B6,
        c5_maior_q_total_B6,
        d1_maior_q_total_B6,
        d2_maior_q_total_B6,
        e1_maior_q_total_B6,
        e2_maior_q_total_B6,

        f1_maior_q_total_B6,
        g1_maior_q_total_B6,
        h1_maior_q_total_B6,
        i1_maior_q_total_B6,

        j1_maior_j2_e_j3,
        j2_maior_q_j1,
        j3_maior_q_j1,
        j4_maior_j5_e_j6,

        k2_maior_q_k1,
        k3_maior_q_k1,
        k4_maior_q_k1,
        k5_maior_q_k1,
        k6_maior_q_k1,
    ]);

    HTMLCollection.prototype.forEach = Array.prototype.forEach;
    const inputs = document.getElementsByTagName('input')
        inputs.forEach(input => {
            input.addEventListener('blur', () => {
               if (input.value && Number(input.value) < 0) {
                   alert("Valor deve ser maior ou igual a zero")
                }
            })});

    document.getElementsByTagName('input').forEach(element => {
        if (element.type == 'number') {
            element.value = '0'
        }
        if  (element.type == 'number' < 0) {
            alert("Valor deve ser maior ou igual a zero")
    }
    
    let button = document.getElementById("enviar")
    window.addEventListener('input', () => {
        if (ruleSet.isValid()) {
            button.disabled = false
        } else {
            button.disabled = true
        }
    })
});

window.addEventListener('load', () => {
    const B6_T = document.getElementById('B6_T')
    const B6_M_1 = document.getElementById('B6_M_1')
    const B6_M_2 = document.getElementById('B6_M_2')
    const B6_M_3 = document.getElementById('B6_M_3')
    const B6_M_4 = document.getElementById('B6_M_4')
    const B6_F_1 = document.getElementById('B6_F_1')
    const B6_F_2 = document.getElementById('B6_F_2')
    const B6_F_3 = document.getElementById('B6_F_3')
    const B6_F_4 = document.getElementById('B6_F_4')

    const C1_T = document.getElementById('C1_T')
    const C1_M_1 = document.getElementById('C1_M_1')
    const C1_M_2 = document.getElementById('C1_M_2')
    const C1_M_3 = document.getElementById('C1_M_3')
    const C1_F_1 = document.getElementById('C1_F_1')
    const C1_F_2 = document.getElementById('C1_F_2')
    const C1_F_3 = document.getElementById('C1_F_3')

    const C2_T = document.getElementById('C2_T')
    const C2_M_1 = document.getElementById('C2_M_1')
    const C2_M_2 = document.getElementById('C2_M_2')
    const C2_M_3 = document.getElementById('C2_M_3')
    const C2_F_1 = document.getElementById('C2_F_1')
    const C2_F_2 = document.getElementById('C2_F_2')
    const C2_F_3 = document.getElementById('C2_F_3')

    const C3_T = document.getElementById('C3_T')
    const C3_M_1 = document.getElementById('C3_M_1')
    const C3_M_2 = document.getElementById('C3_M_2')
    const C3_M_3 = document.getElementById('C3_M_3')
    const C3_F_1 = document.getElementById('C3_F_1')
    const C3_F_2 = document.getElementById('C3_F_2')
    const C3_F_3 = document.getElementById('C3_F_3')

    const C4_T = document.getElementById('C4_T')
    const C4_M_1 = document.getElementById('C4_M_1')
    const C4_M_2 = document.getElementById('C4_M_2')
    const C4_M_3 = document.getElementById('C4_M_3')
    const C4_F_1 = document.getElementById('C4_F_1')
    const C4_F_2 = document.getElementById('C4_F_2')
    const C4_F_3 = document.getElementById('C4_F_3')

    const C5_T = document.getElementById('C5_T')
    const C5_M_1 = document.getElementById('C5_M_1')
    const C5_M_2 = document.getElementById('C5_M_2')
    const C5_F_1 = document.getElementById('C5_F_1')
    const C5_F_2 = document.getElementById('C5_F_2')

    const D1_T = document.getElementById('D1_T')
    const D1_M_1 = document.getElementById('D1_M_1')
    const D1_F_1 = document.getElementById('D1_F_1')

    const D2_T = document.getElementById('D2_T')
    const D2_M_1 = document.getElementById('D2_M_1')
    const D2_F_1 = document.getElementById('D2_F_1')

    const E1_T = document.getElementById('E1_T')
    const E1_M_1 = document.getElementById('E1_M_1')
    const E1_M_2 = document.getElementById('E1_M_2')
    const E1_M_3 = document.getElementById('E1_M_3')
    const E1_M_4 = document.getElementById('E1_M_4')
    const E1_F_1 = document.getElementById('E1_F_1')
    const E1_F_2 = document.getElementById('E1_F_2')
    const E1_F_3 = document.getElementById('E1_F_3')
    const E1_F_4 = document.getElementById('E1_F_4')

    const E2_T = document.getElementById('E2_T')
    const E2_M_1 = document.getElementById('E2_M_1')
    const E2_M_2 = document.getElementById('E2_M_2')
    const E2_M_3 = document.getElementById('E2_M_3')
    const E2_M_4 = document.getElementById('E2_M_4')
    const E2_F_1 = document.getElementById('E2_F_1')
    const E2_F_2 = document.getElementById('E2_F_2')
    const E2_F_3 = document.getElementById('E2_F_3')
    const E2_F_4 = document.getElementById('E2_F_4')

    const G1_T = document.getElementById('G1_T')
    const G1_M_1 = document.getElementById('G1_M_1')
    const G1_M_2 = document.getElementById('G1_M_2')
    const G1_M_3 = document.getElementById('G1_M_3')
    const G1_M_4 = document.getElementById('G1_M_4')
    const G1_F_1 = document.getElementById('G1_F_1')
    const G1_F_2 = document.getElementById('G1_F_2')
    const G1_F_3 = document.getElementById('G1_F_3')
    const G1_F_4 = document.getElementById('G1_F_4')

    const I1_T = document.getElementById('I1_T')
    const I1_M_1 = document.getElementById('I1_M_1')
    const I1_M_2 = document.getElementById('I1_M_2')
    const I1_M_3 = document.getElementById('I1_M_3')
    const I1_M_4 = document.getElementById('I1_M_4')
    const I1_F_1 = document.getElementById('I1_F_1')
    const I1_F_2 = document.getElementById('I1_F_2')
    const I1_F_3 = document.getElementById('I1_F_3')
    const I1_F_4 = document.getElementById('I1_F_4')

    const J4_T = document.getElementById('J4_T')
    const J4_M_1 = document.getElementById('J4_M_1')
    const J4_F_1 = document.getElementById('J4_F_1')
    const J5_T = document.getElementById('J5_T')
    const J5_M_1 = document.getElementById('J5_M_1')
    const J5_F_1 = document.getElementById('J5_F_1')

    const J6_T = document.getElementById('J6_T')
    const J6_M_1 = document.getElementById('J6_M_1')
    const J6_F_1 = document.getElementById('J6_F_1')

    const K1_T = document.getElementById('K1_T')
    const K1_M_1 = document.getElementById('K1_M_1')
    const K1_M_2 = document.getElementById('K1_M_2')
    const K1_M_3 = document.getElementById('K1_M_3')
    const K1_M_4 = document.getElementById('K1_M_4')
    const K1_F_1 = document.getElementById('K1_F_1')
    const K1_F_2 = document.getElementById('K1_F_2')
    const K1_F_3 = document.getElementById('K1_F_3')
    const K1_F_4 = document.getElementById('K1_F_4')


    window.addEventListener('input', () => {
        const total_b = ((!!B6_F_1.value) ? parseInt(B6_F_1.value) : 0) +
            ((!!B6_M_1.value) ? parseInt(B6_M_1.value) : 0) +
            ((!!B6_M_2.value) ? parseInt(B6_M_2.value) : 0) +
            ((!!B6_F_2.value) ? parseInt(B6_F_2.value) : 0) +
            ((!!B6_M_3.value) ? parseInt(B6_M_3.value) : 0) +
            ((!!B6_F_3.value) ? parseInt(B6_F_3.value) : 0) +
            ((!!B6_M_4.value) ? parseInt(B6_M_4.value) : 0) +
            ((!!B6_F_4.value) ? parseInt(B6_F_4.value) : 0)


        console.log(total_b)
        B6_T.value = total_b.toString()
        B6_T.onchange()

        const total_c1 = ((!!C1_F_1.value) ? parseInt(C1_F_1.value) : 0) +
        ((!!C1_M_1.value) ? parseInt(C1_M_1.value) : 0) +
        ((!!C1_M_2.value) ? parseInt(C1_M_2.value) : 0) +
        ((!!C1_F_2.value) ? parseInt(C1_F_2.value) : 0) +
        ((!!C1_M_3.value) ? parseInt(C1_M_3.value) : 0) +
        ((!!C1_F_3.value) ? parseInt(C1_F_3.value) : 0) 

        console.log(total_c1)
        C1_T.value = total_c1.toString()
        C1_T.onchange()
   
        const total_c2 = ((!!C2_F_1.value) ? parseInt(C2_F_1.value) : 0) +
        ((!!C2_M_1.value) ? parseInt(C2_M_1.value) : 0) +
        ((!!C2_M_2.value) ? parseInt(C2_M_2.value) : 0) +
        ((!!C2_F_2.value) ? parseInt(C2_F_2.value) : 0) +
        ((!!C2_M_3.value) ? parseInt(C2_M_3.value) : 0) +
        ((!!C2_F_3.value) ? parseInt(C2_F_3.value) : 0) 

        console.log(total_c2)
        C2_T.value = total_c2.toString()
        C2_T.onchange()
   
   
        const total_c3 = ((!!C3_F_1.value) ? parseInt(C3_F_1.value) : 0) +
        ((!!C3_M_1.value) ? parseInt(C3_M_1.value) : 0) +
        ((!!C3_M_2.value) ? parseInt(C3_M_2.value) : 0) +
        ((!!C3_F_2.value) ? parseInt(C3_F_2.value) : 0) +
        ((!!C3_M_3.value) ? parseInt(C3_M_3.value) : 0) +
        ((!!C3_F_3.value) ? parseInt(C3_F_3.value) : 0) 

        console.log(total_c3)
        C3_T.value = total_c3.toString()
        C3_T.onchange()
   
        const total_c4 = ((!!C4_F_1.value) ? parseInt(C4_F_1.value) : 0) +
        ((!!C4_M_1.value) ? parseInt(C4_M_1.value) : 0) +
        ((!!C4_M_2.value) ? parseInt(C4_M_2.value) : 0) +
        ((!!C4_F_2.value) ? parseInt(C4_F_2.value) : 0) +
        ((!!C4_M_3.value) ? parseInt(C4_M_3.value) : 0) +
        ((!!C4_F_3.value) ? parseInt(C4_F_3.value) : 0) 

        console.log(total_c4)
        C4_T.value = total_c4.toString()
        C4_T.onchange()
   
        const total_c5 = ((!!C5_F_1.value) ? parseInt(C5_F_1.value) : 0) +
        ((!!C5_M_1.value) ? parseInt(C5_M_1.value) : 0) +
        ((!!C5_M_2.value) ? parseInt(C5_M_2.value) : 0) +
        ((!!C5_F_2.value) ? parseInt(C5_F_2.value) : 0) 

        console.log(total_c5)
        C5_T.value = total_c5.toString()
        C5_T.onchange()

        const total_d1 = ((!!D1_F_1.value) ? parseInt(D1_F_1.value) : 0) +
        ((!!D1_M_1.value) ? parseInt(D1_M_1.value) : 0) 
       
        
        console.log(total_d1)
        D1_T.value = total_d1.toString()
        D1_T.onchange()

        //////////////////////////////////////////////////////
        const total_d2 = ((!!D2_M_1.value) ? parseInt(D2_M_1.value) : 0) +
        ((!!D2_F_1.value) ? parseInt(D2_F_1.value) : 0) 
       
        console.log(total_d2)
        D2_T.value = total_d2.toString()
        D2_T.onchange()




        const total_e1 = ((!!E1_F_1.value) ? parseInt(E1_F_1.value) : 0) +
            ((!!E1_M_1.value) ? parseInt(E1_M_1.value) : 0) +
            ((!!E1_M_2.value) ? parseInt(E1_M_2.value) : 0) +
            ((!!E1_F_2.value) ? parseInt(E1_F_2.value) : 0) +
            ((!!E1_M_3.value) ? parseInt(E1_M_3.value) : 0) +
            ((!!E1_F_3.value) ? parseInt(E1_F_3.value) : 0) +
            ((!!E1_M_4.value) ? parseInt(E1_M_4.value) : 0) +
            ((!!E1_F_4.value) ? parseInt(E1_F_4.value) : 0)


        console.log(total_e1)
        E1_T.value = total_e1.toString()
        E1_T.onchange()
        
        const total_e2 = ((!!E2_F_1.value) ? parseInt(E2_F_1.value) : 0) +
            ((!!E2_M_1.value) ? parseInt(E2_M_1.value) : 0) +
            ((!!E2_M_2.value) ? parseInt(E2_M_2.value) : 0) +
            ((!!E2_F_2.value) ? parseInt(E2_F_2.value) : 0) +
            ((!!E2_M_3.value) ? parseInt(E2_M_3.value) : 0) +
            ((!!E2_F_3.value) ? parseInt(E2_F_3.value) : 0) +
            ((!!E2_M_4.value) ? parseInt(E2_M_4.value) : 0) +
            ((!!E2_F_4.value) ? parseInt(E2_F_4.value) : 0)


        console.log(total_e2)
        E2_T.value = total_e2.toString()
        E2_T.onchange()
        
        const total_g1 = ((!!G1_F_1.value) ? parseInt(G1_F_1.value) : 0) +
            ((!!G1_M_1.value) ? parseInt(G1_M_1.value) : 0) +
            ((!!G1_M_2.value) ? parseInt(G1_M_2.value) : 0) +
            ((!!G1_F_2.value) ? parseInt(G1_F_2.value) : 0) +
            ((!!G1_M_3.value) ? parseInt(G1_M_3.value) : 0) +
            ((!!G1_F_3.value) ? parseInt(G1_F_3.value) : 0) +
            ((!!G1_M_4.value) ? parseInt(G1_M_4.value) : 0) +
            ((!!G1_F_4.value) ? parseInt(G1_F_4.value) : 0)


        console.log(total_g1)
        G1_T.value = total_g1.toString()
        G1_T.onchange()
        
        const total_i1 = ((!!I1_F_1.value) ? parseInt(I1_F_1.value) : 0) +
            ((!!I1_M_1.value) ? parseInt(I1_M_1.value) : 0) +
            ((!!I1_M_2.value) ? parseInt(I1_M_2.value) : 0) +
            ((!!I1_F_2.value) ? parseInt(I1_F_2.value) : 0) +
            ((!!I1_M_3.value) ? parseInt(I1_M_3.value) : 0) +
            ((!!I1_F_3.value) ? parseInt(I1_F_3.value) : 0) +
            ((!!I1_M_4.value) ? parseInt(I1_M_4.value) : 0) +
            ((!!I1_F_4.value) ? parseInt(I1_F_4.value) : 0)


        console.log(total_i1)
        I1_T.value = total_i1.toString()
        I1_T.onchange()
        

        const total_j4 = ((!!J4_F_1.value) ? parseInt(J4_F_1.value) : 0) +
            ((!!J4_M_1.value) ? parseInt(J4_M_1.value) : 0) 
           
        console.log(total_j4)
        J4_T.value = total_j4.toString()
        J4_T.onchange()
        
        const total_j5 = ((!!J5_F_1.value) ? parseInt(J5_F_1.value) : 0) +
            ((!!J5_M_1.value) ? parseInt(J5_M_1.value) : 0) 
           
        console.log(total_j5)
        J5_T.value = total_j5.toString()
        J5_T.onchange()
        
        
        const total_j6 = ((!!J6_F_1.value) ? parseInt(J6_F_1.value) : 0) +
            ((!!J6_M_1.value) ? parseInt(J6_M_1.value) : 0) 
           
        console.log(total_j6)
        J6_T.value = total_j6.toString()
        J6_T.onchange()


        const total_k1 = ((!!K1_F_1.value) ? parseInt(K1_F_1.value) : 0) +
        ((!!K1_M_1.value) ? parseInt(K1_M_1.value) : 0) +
        ((!!K1_M_2.value) ? parseInt(K1_M_2.value) : 0) +
        ((!!K1_F_2.value) ? parseInt(K1_F_2.value) : 0) +
        ((!!K1_M_3.value) ? parseInt(K1_M_3.value) : 0) +
        ((!!K1_F_3.value) ? parseInt(K1_F_3.value) : 0) +
        ((!!K1_M_4.value) ? parseInt(K1_M_4.value) : 0) +
        ((!!K1_F_4.value) ? parseInt(K1_F_4.value) : 0)


        console.log(total_k1)
        K1_T.value = total_k1.toString()
        K1_T.onchange()


    })
});
