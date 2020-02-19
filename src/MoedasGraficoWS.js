import React from 'react'
import {
    LineChart, Line, XAxis, YAxis, CartesianGrid,
  } from 'recharts';

class MoedasGraficoWS extends React.Component {

    ws = new WebSocket('ws://localhost:8765/')

    listaMoedas = [];
    listaDados = [];

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

            this.listaMoedas.push(valores[0]);
            let dado = [
                {
                x:valores[0]['index'],
                y:valores[0]['index']
              },
              {
                x:valores[0]['index']+1,
                y:valores[0]['index']+1
              }
            ]
            this.listaDados.push(dado)
            console.log(dado)
            let lista = JSON.stringify(this.listaMoedas)
            console.log(this.listaMoedas)
            console.log(lista)
            this.setState({
                moedas: this.listaMoedas,
                // dados:this.listaDados
                dados:dado
            })
            // console.log(this.state.moedas)
            // console.log(this.state.moedas)
        }

        this.ws.onclose = () => {
            console.log('descontectado')
        }
    }


    render() {    
  

        return (           
            <div>
                <LineChart width={500} height={300} data={this.state.dados}>
                    <XAxis dataKey="x" />
                    <YAxis />
                    <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
                    <Line type="monotone" dataKey="y" stroke="#8884d8" />
                    {/* <Line type="monotone" dataKey="pv" stroke="#82ca9d" /> */}
                </LineChart>
                                
                <LineChart width={500} height={300} data={this.state.moedas}>
                    <XAxis dataKey="index" />
                    <YAxis />
                    <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
                    <Line type="monotone" dataKey="cotacao" stroke="#8884d8" />
                    {/* <Line type="monotone" dataKey="pv" stroke="#82ca9d" /> */}
                </LineChart>
                <ul>                    
                    {this.state.moedas.map(item => { return <li>{item['index']} - {item['sigla']} - {item['cotacao']}</li> })}
                    {this.state.dados.map(item => { return <li>{item['x']} - {item['sigla']} - {item['y']}</li> })}
                    {this.listaDados.map(item => { return <li>{item['x']} - {item['sigla']} - {item['y']}</li> })}
                </ul>
            </div>
        )
    }
}

export default MoedasGraficoWS;
