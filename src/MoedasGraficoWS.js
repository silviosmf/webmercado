import React from 'react'
import {Line} from 'react-chartjs-2';

class MoedasGraficoWS extends React.Component {

    ws = new WebSocket('ws://localhost:8765/')

    constructor(props) {

        super(props)
        this.state = {
            moedas: [],
            dados: [{
              x:2,
              y:10
            },
            {
              x:4,
              y:12
            }]
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


            let dado = [{"x":2,"y":10},{"x":4,"y":12},{"x":2,"y":2},{"x":3,"y":3},{"x":3,"y":3},{"x":4,"y":4}]

            
            // console.log('lista em json'+ JSON.stringify(message))
            this.setState({
                moedas: this.state.moedas.concat(valores),
                // dados:this.listaDados
                dados:this.state.dados.concat(dado)
            })
            console.log(this.state.dados.map(item => {return item['x']}))
        }

        this.ws.onclose = () => {
            console.log('descontectado')
        }
    }


    render() {    
  
        const info = {
            labels: this.state.moedas.map(item => {return item['index']}),
            datasets: [
              {
                label: 'Rainfall',
                backgroundColor: 'rgba(75,192,192,1)',
                borderColor: 'rgba(0,0,0,1)',
                borderWidth: 2,
                data: this.state.moedas.map(item => {return item['cotacao']})
              }
            ]
          } 

        return (           

            <div>
                <Line
                data={info}
                options={{
                    title:{
                    display:true,
                    text:'Average Rainfall per month',
                    fontSize:20
                    },
                    legend:{
                    display:true,
                    position:'right'
                    }
                }}
                />
            </div>
            // <div>
            //     <LineChart width={500} height={300} data={this.state.dados}>
            //         <XAxis dataKey="x" />
            //         <YAxis />
            //         <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
            //         <Line type="monotone" dataKey="y" stroke="#8884d8" />
            //         {/* <Line type="monotone" dataKey="pv" stroke="#82ca9d" /> */}
            //     </LineChart>
                                
            //     <LineChart width={500} height={300} data={this.state.moedas}>
            //         <XAxis 
            //         interval={0.1}
            //         dataKey="index" />
            //         <YAxis />
            //         <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
            //         <Line type="monotone" dataKey="cotacao" stroke="#8884d8" />
            //         {/* <Line type="monotone" dataKey="pv" stroke="#82ca9d" /> */}
            //     </LineChart>
            //     {/* <ul>                    
            //         {this.state.moedas.map(item => { return <li>{item['index']} - {item['sigla']} - {item['cotacao']}</li> })}
            //         {this.state.dados.map(item => { return <li>{item['x']} - {item['sigla']} - {item['y']}</li> })}
            //     </ul> */}
            // </div>
        )
    }
}

export default MoedasGraficoWS;
