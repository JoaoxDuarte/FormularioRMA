class Form {
  constructor(
    a1,
    a2,
    b1,
    b2,
    b3,
    b4,
    b5,
    b6,
    c1,
    c2,
    c3,
    c4,
    c5,
    c6,
    c7,
    c8,
    c9,
    d1,
    d2,
    d3,
    d4,
    d5,
    d6,
    d7,
    d8
  ) {
    this.a1 = a1;
    this.a2 = a2;
    this.b1 = b1;
    this.b2 = b2;
    this.b3 = b3;
    this.b4 = b4;
    this.b5 = b5;
    this.b6 = b6;
    this.c1 = c1;
    this.c2 = c2;
    this.c3 = c3;
    this.c4 = c4;
    this.c5 = c5;
    this.c6 = c6;
    this.c7 = c7;
    this.c8 = c8;
    this.c9 = c9;
    this.d1 = d1;
    this.d2 = d2;
    this.d3 = d3;
    this.d4 = d4;
    this.d5 = d5;
    this.d6 = d6;
    this.d7 = d7;
    this.d8 = d8;
  }
}

class FormAdapter {
  static fromDomainJson(form_data_json) {
    const a1 = form_data_json.dados_Paif.total_fam_em_acompanha_PAIF;
    const a2 = form_data_json.dados_Paif.total_novas_fam_PAIF;
    const b1 = form_data_json.dados_Paif.novas_fam_em_situa_extre_pobreza;
    const b2 = form_data_json.dados_Paif.novas_fam_bolsa_familia;
    const b3 =
      form_data_json.dados_Paif.novas_familias_bolsa_familia_em_descomprimento;
    const b4 = form_data_json.dados_Paif.novas_familias_membros_bpc;
    const b5 =
      form_data_json.dados_Paif.novas_familias_criancas_adltes_trabalho;
    const b6 =
      form_data_json.dados_Paif.novas_familias_criancas_adltes_acolhimento;
    const c1 =
      form_data_json.volume_atendimento_particularizado
        .total_atend_particularizado_mes;
    const c2 =
      form_data_json.volume_atendimento_particularizado
        .fam_encami_inclusao_cad_unico_mes;
    const c3 =
      form_data_json.volume_atendimento_particularizado
        .fam_encami_inclusao_atuali_cad_unico_mes;
    const c4 =
      form_data_json.volume_atendimento_particularizado.individuos_encami_bpc;
    const c5 =
      form_data_json.volume_atendimento_particularizado.fam_encami_para_creas;
    const c6 =
      form_data_json.volume_atendimento_particularizado.visitas_domici_reali;
    const c7 =
      form_data_json.volume_atendimento_particularizado
        .total_aux_natali_concedido;
    const c8 =
      form_data_json.volume_atendimento_particularizado
        .total_aux_funeral_concedido;
    const c9 =
      form_data_json.volume_atendimento_particularizado.outros_benef_concedidos;
    const d1 =
      form_data_json
        .volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF
        .familias_participando_regularmente_de_grupos_no_ambito_PAIF;
    const d2 =
      form_data_json
        .volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF
        .criancas_adolescentes_0_6_anos_no_servico;
    const d3 =
      form_data_json
        .volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF
        .criancas_adolescente_7_a_14_no_servico;
    const d4 =
      form_data_json
        .volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF
        .adolescenete_15_a_17_no_servico;
    const d5 =
      form_data_json
        .volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF
        .adultos_18_a_59_servicos;
    const d6 =
      form_data_json
        .volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF
        .idosos_servico;
    const d7 =
      form_data_json
        .volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF
        .pessoas_com_deficiencia_servico;
    const d8 =
      form_data_json
        .volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF
        .adultos_18_a_59_servicos;

    return new Form(
      a1,
      a2,
      b1,
      b2,
      b3,
      b4,
      b5,
      b6,
      c1,
      c2,
      c3,
      c4,
      c5,
      c6,
      c7,
      c8,
      c9,
      d1,
      d2,
      d3,
      d4,
      d5,
      d6,
      d7,
      d8
    );
  }
}

class FormPresenter{ 
    static fromForm(form){ 
        let a1 = document.getElementById('A1');
        let a2 = document.getElementById('A2');
        let b1 = document.getElementById('B1');
        let b2 = document.getElementById('B2');
        let b3 = document.getElementById('B3');
        let b4 = document.getElementById('B4');
        let b5 = document.getElementById('B5');
        let b6 = document.getElementById('B6');
        let c1 = document.getElementById('C1');
        let c2 = document.getElementById('C2');
        let c3 = document.getElementById('C3');
        let c4 = document.getElementById('C4');
        let c5 = document.getElementById('C5');
        let c6 = document.getElementById('C6');
        let c7 = document.getElementById('C7');
        let c8 = document.getElementById('C8');
        let c9 = document.getElementById('C9');
        let d1 = document.getElementById('D1')
        let d2 = document.getElementById('D2')
        let d3 = document.getElementById('D3')
        let d4 = document.getElementById('D4')
        let d5 = document.getElementById('D5')
        let d6 = document.getElementById('D6')
        let d7 = document.getElementById('D7')
        let d8 = document.getElementById('D8')


        a1.value = form.a1
        a2.value = form.a2
        b1.value = form.b1
        b2.value = form.b2
        b3.value = form.b3
        b4.value = form.b4
        b5.value = form.b5
        b6.value = form.b6
        c1.value = form.c1
        c2.value = form.c2
        c3.value = form.c3
        c4.value = form.c4
        c5.value = form.c5
        c6.value = form.c6
        c7.value = form.c7
        c8.value = form.c8
        c9.value = form.c9
        d1.value = form.d1
        d2.value = form.d2
        d3.value = form.d3
        d4.value = form.d4
        d5.value = form.d5
        d6.value = form.d6
        d7.value = form.d7
        d8.value = form.d8

        a1.disabled = true
        a2.disabled = true
        b1.disabled = true
        b2.disabled = true
        b3.disabled = true
        b4.disabled = true
        b5.disabled = true
        b6.disabled = true
        c1.disabled = true
        c2.disabled = true
        c3.disabled = true
        c4.disabled = true
        c5.disabled = true
        c6.disabled = true
        c7.disabled = true
        c8.disabled = true
        c9.disabled = true
        d1.disabled = true
        d2.disabled = true
        d3.disabled = true
        d4.disabled = true
        d5.disabled = true
        d6.disabled = true
        d7.disabled = true
        d8.disabled = true

    }
}

window.addEventListener("load", () => {
  const a2_maior_a1 = new Regra(
    ["A1", "A2"],
    "A2 não pode ser maior que A1",
    (a1, a2) => a2 <= a1
  );
  const b1_maior_a2 = new Regra(
    ["B1", "A2"],
    "B1 não pode ser maior que A2",
    (b1, a2) => b1 <= a2
  );
  const b3_maior_que_a2 = new Regra(
    ["B3", "A2"],
    "B3 não pode ser maior que A2",
    (b3, a2) => b3 <= a2
  );
  const b4_maior_que_a2 = new Regra(
    ["B4", "A2"],
    "B4 não pode ser maior que A2",
    (b4, a2) => b4 <= a2
  );
  const b5_maior_que_a2 = new Regra(
    ["B5", "A2"],
    "B5 não pode ser maior que A2",
    (b5, a2) => b5 <= a2
  );
  const b6_maior_que_a2 = new Regra(
    ["B6", "A2"],
    "B6 não pode ser maior que A2",
    (b6, a2) => b6 <= a2
  );
  const c2_c3_maior_que_c1 = new Regra(
    ["C2", "C3", "C1"],
    "A soma de C2 com C3 não pode ser maior que C1",
    (c2, c3, c1) => c2 + c3 <= c1
  );
  const c4_maior_que_c1 = new Regra(
    ["C4", "C1"],
    "C4 não pode ser maior que C1",
    (c4, c1) => c4 <= c1
  );
  const c5_maior_que_c1 = new Regra(
    ["C5", "C1"],
    "C5 não pode ser maior que C1",
    (c5, c1) => c5 <= c1
  );
  const c6_maior_que_c1 = new Regra(
    ["C6", "C1"],
    "C6 não pode ser maior que C1",
    (c6, c1) => c6 <= c1
  );
  const c7_maior_que_c1 = new Regra(
    ["C7", "C1"],
    "C7 não pode ser maior que C1",
    (c7, c1) => c7 <= c1
  );
  const c8_maior_que_c1 = new Regra(
    ["C8", "C1"],
    "C8 não pode ser maior que C1",
    (c8, c1) => c8 <= c1
  );
  const c9_maior_que_c1 = new Regra(
    ["C9", "C1"],
    "C9 não pode ser maior que C1",
    (c9, c1) => c9 <= c1
  );
  const d1_maior_que_a1 = new Regra(
    ["D1", "A1"],
    "D1 não pode ser maior que A1",
    (d1, a1) => d1 <= a1
  );

  const ruleSet = new RuleSet([
    a2_maior_a1,
    b1_maior_a2,
    b3_maior_que_a2,
    b4_maior_que_a2,
    b5_maior_que_a2,
    b6_maior_que_a2,
    c2_c3_maior_que_c1,
    c4_maior_que_c1,
    c5_maior_que_c1,
    c6_maior_que_c1,
    c7_maior_que_c1,
    c8_maior_que_c1,
    c9_maior_que_c1,
    d1_maior_que_a1,
  ]);


  HTMLCollection.prototype.forEach = Array.prototype.forEach;

    document.getElementsByTagName('input').forEach(element => {
      if(element.type =='number'){
        element.value = '0' 
      }      
    });

  let button = document.getElementById("enviar")
  window.addEventListener('input', () => {
    if (ruleSet.isValid() ){ 
      button.disabled = false
    } else { 
      button.disabled = true
    }
  })
});
