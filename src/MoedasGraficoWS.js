import React, {useState, useEffect} from 'react'
import {
    LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
  } from 'recharts';

class MoedasGraficoWS extends React.Component {

    ws = new WebSocket('ws://localhost:8765/')

    listaMoedas = [];

    constructor(props) {
        super(props)
        this.state = {
            moedas: []
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
            this.setState({
                // moedas: this.listaMoedas.reverse()
                moedas: this.listaMoedas
            })
            console.log(this.state.moedas)
            // console.log(this.state.moedas)
        }

        this.ws.onclose = () => {
            console.log('descontectado')
        }
    }


    render() {

        const [dados, setDados] = useState(0);

        // Similar ao componentDidMount e componentDidUpdate:
        useEffect(() => {
          // Atualiza o titulo do documento usando a API do browser
          document.title = `Você clicou ${dados} vezes`;
        });
    
    
        const data = [
            {
              name: 'Page A', uv: 0.9259, pv: 2400, amt: 2400,
            },
            {
              name: 'Page B', uv: 3000, pv: 1398, amt: 2210,
            },
            {
              name: 'Page C', uv: 2000, pv: 9800, amt: 2290,
            },
            {
              name: 'Page D', uv: 2780, pv: 3908, amt: 2000,
            },
            {
              name: 'Page E', uv: 1890, pv: 4800, amt: 2181,
            },
            {
              name: 'Page F', uv: 2390, pv: 3800, amt: 2500,
            },
            {
              name: 'Page G', uv: 3490, pv: 4300, amt: 2100,
            },
          ];

        return (           
            <div>
                <ul>
                    {dados}
                    {this.state.moedas.map(item => { return <li>{item['sigla']} - {item['cotacao']}</li> })}
                </ul>
                <LineChart width={500} height={300} data={this.state.moedas}>
                    <XAxis dataKey="sigla" />
                    <YAxis />
                    <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
                    <Line type="monotone" dataKey="cotacao" stroke="#8884d8" />
                    {/* <Line type="monotone" dataKey="pv" stroke="#82ca9d" /> */}
                </LineChart>

                <LineChart width={500} height={300} data={data}>
                    <XAxis dataKey="name" />
                    <YAxis />
                    <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
                    <Line type="monotone" dataKey="uv" stroke="#8884d8" />
                    {/* <Line type="monotone" dataKey="pv" stroke="#82ca9d" /> */}
                </LineChart>
            </div>
        )
    }
}

export default MoedasGraficoWS;
