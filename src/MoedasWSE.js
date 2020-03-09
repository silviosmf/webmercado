import React, { Component } from 'react';
import {Line} from 'react-chartjs-2';

class MoedasWSE extends React.Component {
    maxEuro = 1
    minEuro = 0
    constructor (props) {
      super(props)

        this.state = {
        moedas: []
      }
      this.carregarMoedas = this.carregarMoedas.bind(this)
    }
      carregarMoedas() {
        const url = 'http://localhost:5000/moedas/eur'
    // https://www.jsontest.com
        // const url = 'http://echo.jsontest.com/key/value/one/two'
        fetch(url)
        .then(res => res.json())
        .then(res => {
            // console.log(res)
            this.setState({
              moedas:res
            });
        });    

        this.maxEuro = 1
        this.minEuro = 0
      }

      render() {    
  
        const info = {
            labels: this.state.moedas.map(item => {return item.data}),
            datasets: [
              {
                label: 'EURO',
                backgroundColor: '#ccc',
                borderColor: '#ccc',
                borderWidth: 0.2,                
                data: this.state.moedas.map(item => {return item.percentual})
              }
            ]
          } 

        const options={
            title:{
                display:true,
                text:'Dólar x EURO',
                fontSize:20
            },
            scales: {                        
                yAxes: [{
                    ticks: {
                        max: parseFloat(this.maxEuro),
                        min: parseFloat(this.minEuro)
                      }                            
                }],
                xAxes: [{
                    type: 'time',
                    time: {
                        unit:'minute' 
                    }                         
                }]
            }                    
        }


        return (           
            <div>
            <button onClick={this.carregarMoedas}>Carregar Moedas</button>
                <Line
                data={info}
                options={options}
                />
          <table>
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
          </table>
            </div>
        )
    }

}

export default MoedasWSE;
