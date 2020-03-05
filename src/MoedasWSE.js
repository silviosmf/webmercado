import React, { Component } from 'react';


class MoedasWSE extends React.Component {

    constructor (props) {
      super(props)
      this.state = {
        moedas: []
      }
      this.carregarMoedas = this.carregarMoedas.bind(this)
    }
      carregarMoedas() {
        const url = 'http://localhost:5000/moedas'
    // https://www.jsontest.com
        // const url = 'http://echo.jsontest.com/key/value/one/two'
        fetch(url)
        .then(res => res.json())
        .then(res => {
            // const json = "{'result':true, 'count':42}";
            // const obj = JSON.parse(JSON.stringify(json));

            // let lista = []
            // lista = res;

            // const listaMoedas = lista.map(moeda => moeda.sigla)
            // const x = JSON.parse({'sigla':'dolar'})
            console.log(res)
            this.setState({
              moedas:res
            });
            // const sigla = this.state.moedas[0]
            // console.log(sigla)
            // Converter Objeto em array de objetos
            // const lista = this.state.moedas.sigla
            // const s = Object.keys(lista).map(item => lista[item])
        });        
      }

  render() {
    return (
      <div>
          <h1>Lista de Moedas</h1>
          {/* <table>
              <tr>
                  <td>Sigla</td>
                  <td>Cotação</td>
                  <td>Percentual</td>
              </tr>            
            {this.state.moedas.map(item => (
                    <tr>
                        <td>{item.sigla}</td>
                        <td>{item.cotacao}</td>
                        <td>{item.percentual}</td>
                    </tr>
                ))}
          </table> */}
          <button onClick={this.carregarMoedas}>Carregar Moedas</button>
      </div>
  );
  }

}

export default MoedasWSE;
