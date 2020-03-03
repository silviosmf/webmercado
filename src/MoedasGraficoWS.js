import React from 'react'
import {Line} from 'react-chartjs-2';

class MoedasGraficoWS extends React.Component {

    ws = new WebSocket('ws://localhost:8765/')
    maxEuro = '0'
    minEuro = '10'

    constructor(props) {
        super(props)
        
        this.state = {
            euro: [],
            gbp: []
        }
    }

    componentDidMount() {
        this.ws.onopen = () => {
            console.log('conectado')
        }
        this.ws.onmessage = evt => {
            const message = JSON.parse(evt.data)
            let valores = []
            valores = message;

            if(parseFloat(valores[1].cotacao)>parseFloat(this.maxEuro)) {
                this.maxEuro = parseFloat(valores[1].cotacao) + parseFloat(0.001)
            }   
            if(parseFloat(valores[1].cotacao)<parseFloat(this.minEuro)) {
                this.minEuro = parseFloat(valores[1].cotacao) - parseFloat(0.001)
            }                 

            console.log(valores[1])
            console.log('Max Euro: '+this.maxEuro) 
            console.log('Min Euro: '+this.minEuro) 
            console.log(valores[2])
            
            this.setState({
                euro: this.state.euro.concat(valores[1]),
                gbp: this.state.gbp.concat(valores[2])
            })
        }

        this.ws.onclose = () => {
            console.log('descontectado')
        }
    }


    render() {    
  
        const info = {
            labels: this.state.euro.map(item => {return item['data']}),
            datasets: [
              {
                label: 'EURO',
                backgroundColor: '#ccc',
                borderColor: '#ccc',
                borderWidth: 0.2,                
                data: this.state.euro.map(item => {return item['cotacao']})
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
                        // displayFormats: {
                        //     year : 'YYYY'
                        //     //https://www.chartjs.org/docs/latest/axes/cartesian/time.html#time-cartesian-axis
                        // }
                    }                         
                }]
            }                    
        }


        const infoGBP = {
            labels: this.state.gbp.map(item => {return item['data']}),
            datasets: [
              {
                label: 'Libra',
                backgroundColor: 'rgba(0,0,0,.05)',
                borderColor: 'rgba(0,0,0,1)',
                borderWidth: 0.2,                
                data: this.state.gbp.map(item => {return item['cotacao']})
              }
            ]
          } 

        const optionsGBP={
            title:{
                display:true,
                text:'Dólar x Libra',
                fontSize:20
            },
            scales: {                        
                yAxes: [{
                    ticks: {
                        max: 0.78,
                        min: 0.76
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
                <Line
                data={info}
                options={options}
                />
                <Line
                data={infoGBP}
                options={optionsGBP}
                />

            </div>
        )
    }
}

export default MoedasGraficoWS;
