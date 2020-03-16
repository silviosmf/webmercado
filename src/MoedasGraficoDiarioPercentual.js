import React, { Component } from 'react';
import {Line} from 'react-chartjs-2';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';


class MoedasGraficoApi extends React.Component {
    max = 0
    min = 0
    maxCotacao = 0
    minCotacao = 0
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
            // console.log(this.state.moedas)
            // console.log(sigla)
            // console.log(res[0].percentual.split('%')[0].replace(',','.'))

            let strPercentual = parseFloat(res[0].percentual.split('%')[0].replace(',','.'))
            let strCotacao = parseFloat(res[0].cotacao)

            this.max = strPercentual
            this.min = strPercentual

            this.maxCotacao = this.minCotacao = strCotacao

            for (var i = 0; i < res.length; i++) {
                let strPercentual = parseFloat(res[i].percentual.split('%')[0].replace(',','.'))
                if(this.max < strPercentual){
                    this.max = strPercentual
                }
                if(this.min > strPercentual){
                    this.min = strPercentual
                }           
                
                let strCotacao = parseFloat(res[i].cotacao)
                if(this.maxCotacao < strCotacao){
                    this.maxCotacao = strCotacao
                }
                if(this.minCotacao > strCotacao){
                    this.minCotacao = strCotacao
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


            const optionsPercentual={
                title:{
                    display:true,                
                    text:cabecalho,
                    fontSize:20
                },
                scales: {                        
                    yAxes: [{
                        ticks: {
                            max: parseFloat(this.max)+0.3,
                            min: parseFloat(this.min)-0.3                            
                            // max: parseFloat(3),
                            // min: parseFloat(-3)
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
                <p ></p>
                <table class="table table-hover">
                    <thead>
                        <tr>
                        <th scope="col"></th>
                        <th scope="col">Percentual</th>
                        <th scope="col">Cotação</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th scope="row">
                                Máxima diária
                            </th>
                            <td>
                                {this.max}
                            </td>
                            <td>
                                {this.maxCotacao}
                            </td>
                        </tr>                   
                        <tr>
                            <th scope="row">
                                Mínima diária
                            </th>
                            <td>
                                {this.min}
                            </td>
                            <td>
                                {this.minCotacao}
                            </td>
                        </tr> 
                    </tbody>                   
                </table>          
            </div>
        )
    }

}

export default MoedasGraficoApi;
