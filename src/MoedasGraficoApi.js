import React, { Component } from 'react';
import {Line} from 'react-chartjs-2';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';


class MoedasGraficoApi extends React.Component {
    max = 10
    min = 0
    constructor (props) {
        super(props)
        this.carregarMoedas('BRL')
        this.state = {
        moedas: []
      }
    }
    
    carregarMoedas = (sigla) => {
        const url = 'http://localhost:5000/moedasAgora/'+sigla
        fetch(url)
        .then(res => res.json())
        .then(res => {
            console.log(this.state.moedas)
            console.log(sigla)
            console.log(res[0].cotacao)
            this.max = parseFloat(res[0].cotacao)
            this.min = parseFloat(res[0].cotacao)

            for (var i = 0; i < res.length; i++) {
                if(this.max < parseFloat(res[i].cotacao)){
                    this.max = res[i].cotacao
                }
                if(this.min > parseFloat(res[i].cotacao)){
                    this.min = res[i].cotacao
                }                
            }            
            this.setState({
              moedas:res
            });

    });    

      }

      render() {    

        let cabecalho = 'Dólar x Real'
        if(document.getElementById('selectMoedas') != null)       
            cabecalho = 'Dólar x '+document.getElementById('selectMoedas').value

        const info = {
            labels: this.state.moedas.map(item => {return item.data}),
            datasets: [
              {
                label: 'EURO',
                backgroundColor: 'rgb(240,248,255)',                
                borderColor: 'rgb(0,0,128)',
                borderWidth: 0.5,                
                data: this.state.moedas.map(item => {return item.cotacao})
              }
            ]
          } 

        const infoPercentual = {
            labels: this.state.moedas.map(item => {return item.data}),
            datasets: [
              {
                label: 'EURO',
                backgroundColor: 'rgb(240,248,255)',                
                borderColor: 'rgb(0,0,128)',
                borderWidth: 0.5,                
                data: this.state.moedas.map(item => {return parseFloat(item.percentual.split('%')[0].replace(',','.'))})
              }
            ]
          } 

          const options={
                title:{
                    display:true,                
                    text:cabecalho,
                    fontSize:20
                },
                scales: {                        
                    yAxes: [{
                        ticks: {
                            max: parseFloat(this.max)+0.002,
                            min: parseFloat(this.min)-0.002
                        }                            
                    }],
                    xAxes: [{
                        type: 'time',
                        time: {
                            displayFormats: {
                                minute : 'h:mm a'
                                //https://www.chartjs.org/docs/latest/axes/cartesian/time.html#time-cartesian-axis
                            }
                        }                         
                    }]
                }                    
            }


            const optionsPercentual={
                title:{
                    display:true,                
                    text:cabecalho,
                    fontSize:20
                },
                scales: {                        
                    yAxes: [{
                        ticks: {
                            max: parseFloat(3),
                            min: parseFloat(0)
                        }                            
                    }],
                    xAxes: [{
                        type: 'time',
                        time: {
                            displayFormats: {
                                minute : 'h:mm a'
                                //https://www.chartjs.org/docs/latest/axes/cartesian/time.html#time-cartesian-axis
                            }
                        }                         
                    }]
                }                    
            }
        return (           
            <div>            
                <Line
                    data={info}
                    options={options}
                />
                <Line
                    data={infoPercentual}
                    options={optionsPercentual}
                />                
                <select onChange={() => this.carregarMoedas(document.getElementById('selectMoedas').value)} class="custom-select" id='selectMoedas'>
                    <option selected value="BRL">Real</option>
                    <option value="EUR">Euro</option>
                    <option value="GBP">Libra Esterlina</option>
                    <option value="JPY">Iene Japonês</option>
                    <option value="CHF">Franco Suíço</option>
                    <option value="CAD">Dólar Canadense</option>
                    <option value="ARS">Peso Argentino</option>
                    <option value="AUD">Dólar Australiano</option>
                    <option value="COP">Peso Colombiano</option>
                    <option value="MXN">Peso Mexicano</option>
                    <option value="PEN">Sol do Peru</option>
                    <option value="RUB">Rublo Russo</option>
                    <option value="SEK">Coroa Sueca</option>
                    <option value="TRY">Lira Turca</option>
                    <option value="ZAR">Rand Sul-Africano</option>
                    <option value="CNY">Yuan Chinês</option>                    
                    <option value="INR">Rúpia Indiana</option>
                    <option value="CLP">Peso Chileno</option>
                </select>                

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
                                <td>{item.percentual.split('%')[0]}</td>
                            </tr>
                        ))}
                </table>

            </div>
        )
    }

}

export default MoedasGraficoApi;
