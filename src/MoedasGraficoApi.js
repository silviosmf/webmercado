import React, { Component } from 'react';
import {Line} from 'react-chartjs-2';

class MoedasGraficoApi extends React.Component {
    max = 10
    min = 0
    constructor (props) {
      super(props)

        this.state = {
        moedas: []
      }
    //   this.carregarMoedas = this.carregarMoedas.bind(this)      
    }
    
    // carregarMoedas(sigla) {
        carregarMoedas = (sigla) => {
        const url = 'http://localhost:5000/moedasAgora/'+sigla
        fetch(url)
        .then(res => res.json())
        .then(res => {
            this.setState({
              moedas:res
            });
            console.log(this.state.moedas)
            console.log(sigla)
            console.log(res.length)
            this.max = 0
            this.min = 0
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
    });    

      }

      render() {    
  
        const info = {
            labels: this.state.moedas.map(item => {return item.data}),
            datasets: [
              {
                label: 'EURO',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                borderWidth: 0.2,                
                data: this.state.moedas.map(item => {return item.cotacao})
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
                        max: parseFloat(this.max),
                        min: parseFloat(this.min)
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
                <select id='selectMoedas'>
                    <option value="BRL">Real</option>
                    <option value="EUR">Euro</option>
                    <option value="GBP">Libra Esterlina</option>
                </select>
                <button onClick={() => this.carregarMoedas(document.getElementById('selectMoedas').value)}>Atualizar</button>          
            </div>
        )
    }

}

export default MoedasGraficoApi;
