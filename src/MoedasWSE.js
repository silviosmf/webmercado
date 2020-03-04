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
        fetch('http://localhost:5000/moedas')
        .then(res => res.json())
        .then(res => {
            const json = '{"result":true, "count":42}';
            const obj = JSON.parse(json);

            // const x = JSON.parse({'sigla':'dolar'})
            console.log(json.count)
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
