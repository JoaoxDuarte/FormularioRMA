window.onload = (e) => {

    show = (e) => {
        e.style.display = "block"
    }

    hide = (e) => {
        e.style.display = "none"
    }
    //Pegar os elementos
    //MODIFICAR O CÓDIGO DO CARA PRA COLOCAR O ID ORIGINAL DO SELECT**
    //PEGAR O ELEMENTO DO CARA PELO
    const centro_pop = document.getElementById('dados_centro_pop_multi')
    const cras = document.getElementById('dados_cras_multi')
    const creas = document.getElementById('dados_creas_multi')

    const centro_pop_title = document.getElementById('centro_pop_title')
    const cras_title = document.getElementById('cras_title')
    const creas_title = document.getElementById('creas_title')

    console.log(creas)
    console.log(cras)

    hide(cras)
    hide(creas)
    hide(centro_pop)

    hide(centro_pop_title)
    hide(cras_title)
    hide(
        creas_title

    )

    elements = [creas, cras, centro_pop, centro_pop_title, cras_title, creas_title]

    if (document.querySelector('input[name="option_radio"]')) {
        document.querySelectorAll('input[name="option_radio"]').forEach((elem) => {
            elem.addEventListener("change", function (event) {

                elements.forEach((e) => hide(e))

                var item = event.target.value;
                console.log(item)
                if (item == 'cras_radio') {
                    show(cras)
                    show(cras_title)
                }
                else if (item == 'creas_radio') {

                    show(creas)
                    show(creas_title)
                }
                else {
                    show(centro_pop)
                    show(centro_pop_title)
                }
            });
        });
    }



    //Adicionar o hidden

    //adicionar o click





}
