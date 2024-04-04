//Registro Mensal de Atendimentos CRAS: Template do Administrador

var unidade = null;
function MultiSelectTag(el, customs = { shadow: false, rounded: true }) {
    var element = null
    var options = null
    var customSelectContainer = null
    var wrapper = null
    var btnContainer = null
    var body = null
    var inputContainer = null
    var inputBody = null
    var input = null
    var button = null
    var drawer = null
    var ul = null
    var domParser = new DOMParser()
    init()

    function init() {
        element = document.getElementById(el)
        createElements()
        initOptions()
        enableItemSelection()
        setValues()
        button.addEventListener('click', () => {
            if (drawer.classList.contains('hidden')) {
                initOptions()
                enableItemSelection()
                drawer.classList.remove('hidden')
                input.focus()
            } else {
                drawer.classList.add('hidden')
            }
        })

        input.addEventListener('keyup', (e) => {
            initOptions(e.target.value)
            enableItemSelection()
        })

        input.addEventListener('keydown', (e) => {
            if (e.key === 'Backspace' && !e.target.value && inputContainer.childElementCount > 1) {
                const child = body.children[inputContainer.childElementCount - 2].firstChild
                const option = options.find((op) => op.value == child.dataset.value)
                option.selected = false
                removeTag(child.dataset.value)
                setValues()
            }

        })

        document.getElementById('cras_radio').addEventListener('click', (e) => {
            unidade = 'CRAS'
            console.log("unidade_________________")
            console.log(unidade)
        })


        document.getElementById('creas_radio').addEventListener('click', (e) => {
            unidade = 'CREAS'
            console.log("unidade_________________")
            console.log(unidade)
        })
        document.getElementById('centro_pop_radio').addEventListener('click', (e) => {
            unidade = 'CENTRO POP'
            console.log("unidade_________________")
            console.log(unidade)
        })



        window.addEventListener('click', (e) => {

            console.log(e.target.tagName)
            console.log(ul.contains(e.target))

            input.placeholder = `Pesquise a unidade ${unidade}`
            console.log(ul)
            console.log(e.target)

            if (!customSelectContainer.contains(e.target) && !drawer.contains(e.target) && !ul.contains(e.target) && e.target.tagName !== 'LI' && !wrapper.contains(e.target)) {

                drawer.classList.add('hidden')

            }

        });


    }

    function createElements() {
        // Cria elementos customizados
        options = getOptions();
        element.classList.add('hidden')
        // .multi-select-tag
        customSelectContainer = document.createElement('div')
        customSelectContainer.classList.add('mult-select-tag')
        customSelectContainer.setAttribute('id', element.id + '_multi')
        // .container
        wrapper = document.createElement('div')
        wrapper.classList.add('wrapper')

        // body
        body = document.createElement('div')
        body.classList.add('body')
        if (customs.shadow) {
            body.classList.add('shadow')
        }
        if (customs.rounded) {
            body.classList.add('rounded')
        }

        // .input-container
        inputContainer = document.createElement('div')
        inputContainer.classList.add('input-container')

        // input
        input = document.createElement('input')
        input.classList.add('input')

        input.placeholder = `${customs.placeholder || `Pesquisar unidade ...`}`

        inputBody = document.createElement('inputBody')
        inputBody.classList.add('input-body')
        inputBody.append(input)

        body.append(inputContainer)

        // .btn-container
        btnContainer = document.createElement('div')
        btnContainer.classList.add('btn-container')

        // button
        button = document.createElement('button')
        button.type = 'button'
        button.classList.add('super-btn')
        btnContainer.append(button)

        const icon = domParser.parseFromString(`<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="18 15 12 21 6 15"></polyline></svg>`, 'image/svg+xml').documentElement
        button.append(icon)


        body.append(btnContainer)
        wrapper.append(body)

        drawer = document.createElement('div');
        drawer.classList.add(...['drawer', 'hidden'])
        if (customs.shadow) {
            drawer.classList.add('shadow')
        }
        if (customs.rounded) {
            drawer.classList.add('rounded')
        }
        drawer.append(inputBody)
        ul = document.createElement('ul');

        drawer.appendChild(ul)

        customSelectContainer.appendChild(wrapper)
        customSelectContainer.appendChild(drawer)

        // Place TailwindTagSelection after the element
        if (element.nextSibling) {
            element.parentNode.insertBefore(customSelectContainer, element.nextSibling)
        }
        else {
            element.parentNode.appendChild(customSelectContainer);
        }
    }

    function initOptions(val = null) {
        ul.innerHTML = ''
        for (var option of options) {
            if (option.selected) {
                !isTagSelected(option.value) && createTag(option)
            }
            else {
                const li = document.createElement('li')
                li.innerHTML = option.label
                li.dataset.value = option.value

                li.classList.add('position-relative')
                const button = document.createElement('a')
                button.innerHTML = '👁'
                button.classList.add('btn', 'btn-primary')
                button.classList.add('position-absolute')
                button.classList.add('top-0', 'end-0')
                unid = element.name.split('dados_')[1]

                button.href = `leitura_formulario?unidade=${unid}&id_unid=${option.value}`




                li.appendChild(button)

                // For search (Para Pesquisa)
                if (val && option.label.toLowerCase().startsWith(val.toLowerCase())) {
                    ul.appendChild(li)
                }
                else if (!val) {
                    ul.appendChild(li)
                }
            }
        }
    }

    function createTag(option) {
        // Create and show selected item as tag
        const itemDiv = document.createElement('div');
        itemDiv.classList.add('item-container');
        itemDiv.setAttribute('id', option.value);
        const itemLabel = document.createElement('div');
        itemLabel.classList.add('item-label');
        itemLabel.innerHTML = option.label
        itemLabel.dataset.value = option.value
        const itemClose = new DOMParser().parseFromString(`<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="item-close-svg">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>`, 'image/svg+xml').documentElement

        itemClose.addEventListener('click', (e) => {
            const unselectOption = options.find((op) => op.value == option.value)
            unselectOption.selected = false
            removeTag(option.value)
            initOptions()
            setValues()
            enableItemSelection()
        })

        itemDiv.appendChild(itemLabel)
        itemDiv.appendChild(itemClose)
        inputContainer.append(itemDiv)
    }

    function enableItemSelection() {
        // Add click listener to the list items
        for (var li of ul.children) {
            li.addEventListener('click', (e) => {
                console.log("processed li")
                options.find((o) => o.value == e.target.dataset.value).selected = true
                input.value = null
                initOptions()
                setValues()
                input.focus()
                enableItemSelection()


                
                botao_enviar = document.getElementById("enviar_form")
                console.log("bota_enviar___________________________________________________________________")
                let input_container = document.querySelector('.input-container')
                var unidade  = input_container.firstChild 
                let unidade_id = unidade.id
                let children = input_container.childNodes
                let for_var = 0
                let botao_enviar_action_string ='admin_enviar/?select=cras&id_list='
                children.forEach(function(item)
                {
                    for_var++
                    console.log("item__________________________________________")
                    console.log(item)
                    botao_enviar_action_string+=`${item.id} `
                    console.log(botao_enviar_action_string)
                
                })
                botao_enviar.action = botao_enviar_action_string
                let form_id_unidade = document.getElementById("id_unidade")
                form_id_unidade.value = unidade_id
                console.log("li_________________________________________________________")
            })
        }
    }

    function isTagSelected(val) {
        // If the item is already selected (Se o item já estiver selecionado)
        for (var child of inputContainer.children) {
            if (!child.classList.contains('input-body') && child.firstChild.dataset.value == val) {
                return true
            }
        }
        return false
    }
    function removeTag(val) {
        // Remove selected item (Remove o item selecionado)
        for (var child of inputContainer.children) {
            if (!child.classList.contains('input-body') && child.firstChild.dataset.value == val) {
                inputContainer.removeChild(child)
            }
        }
    }
    function setValues() {
        // Update element final values (Atualização)
        for (var i = 0; i < options.length; i++) {
            element.options[i].selected = options[i].selected
        }

    }
    function getOptions() {
        // Map element options
        return [...element.options].map((op) => {
            return {
                value: op.value,
                label: op.label,
                selected: op.selected,
            }
        })
    }

}