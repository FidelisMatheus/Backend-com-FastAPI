async function carregarAnimais() {
  // axios
  //   .get("http://localhost:8000/animais")
  //   .then((response) => console.log(response.data))

  const response = await axios.get("http://localhost:8000/animais")

  const animais = response.data

  const lista = document.getElementById("lista-animais")

  lista.innerHTML = ""

  animais.forEach((animal) => {
    const item = document.createElement("li")
    const button = document.createElement("button")

    button.innerHTML = "Remover"
    button.onclick = () => {
      handleButtonClick(animal)
    }

    const linha = `${animal.nome} - Idade: ${animal.idade} - Cor: ${animal.cor} &ensp;`

    item.innerHTML = linha
    item.appendChild(button)

    lista.appendChild(item)
  })
}

async function handleButtonClick(animal) {
  console.log(animal)
  await axios
    .delete(`http://localhost:8000/animais/${animal.id}`)
    .then((response) => {
      console.log(`Deleted post with ID ${animal.id} name ${animal.nome}`)
      carregarAnimais()
    })
    .catch((error) => {
      console.error(error)
    })
}

function manipularFormulario() {
  const form_animal = document.getElementById("form-animal")
  const input_nome = document.getElementById("nome")

  form_animal.onsubmit = async (event) => {
    event.preventDefault()
    const nome_animal = input_nome.value

    await axios.post("http://localhost:8000/animais", {
      nome: nome_animal,
      idade: 0,
      sexo: "Macho",
      cor: "branco",
    })

    carregarAnimais()
  }
}

document.addEventListener("DOMContentLoaded", function () {
  manipularFormulario()
})

function app() {
  console.log("app iniciada")
  carregarAnimais()
}

app()
